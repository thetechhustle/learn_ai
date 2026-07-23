"use strict";

var fs = require("fs");
var path = require("path");
var tools = require("./task-tools.js");

var root = __dirname;
var failures = [];
var passed = 0;

function check(name, test) {
  try {
    var result = test();
    if (result === false) {
      throw new Error("check returned false");
    }
    passed += 1;
    process.stdout.write("PASS " + name + "\n");
  } catch (error) {
    failures.push(name + ": " + error.message);
    process.stdout.write("FAIL " + name + "\n");
  }
}

function read(relativePath) {
  return fs.readFileSync(path.join(root, relativePath), "utf8");
}

function parseTasks() {
  var html = read("index.html");
  var match = html.match(/<script id="task-data" type="application\/json">([\s\S]*?)<\/script>/);
  if (!match) {
    throw new Error("index.html is missing the task-data JSON block");
  }
  return JSON.parse(match[1]);
}

check("required starter files exist", function requiredFilesExist() {
  [
    "README.md",
    "index.html",
    "styles.css",
    "task-tools.js",
    "app.js",
    "expected/summary.json"
  ].forEach(function requireFile(file) {
    if (!fs.existsSync(path.join(root, file))) {
      throw new Error("missing " + file);
    }
  });
});

var tasks;
check("task data parses as JSON", function taskDataParses() {
  tasks = parseTasks();
  return Array.isArray(tasks);
});

check("task data matches the schema", function taskDataIsValid() {
  var errors = tools.validateTasks(tasks);
  if (errors.length > 0) {
    throw new Error(errors.join(" "));
  }
});

check("summary matches expected output", function summaryMatches() {
  var actual = tools.summarizeTasks(tasks);
  var expected = JSON.parse(read("expected/summary.json"));
  if (JSON.stringify(actual) !== JSON.stringify(expected)) {
    throw new Error(
      "expected " + JSON.stringify(expected) + " but received " + JSON.stringify(actual)
    );
  }
});

check("filters combine status and risk", function filtersCompose() {
  var filtered = tools.filterTasks(tasks, {status: "in-progress", risk: "high"});
  if (filtered.length !== 1 || filtered[0].id !== "T-105") {
    throw new Error("expected only T-105");
  }
});

check("page exposes accessible landmarks", function pageHasLandmarks() {
  var html = read("index.html");
  ["<main>", "<table", "<caption", 'aria-live="polite"', 'class="skip-link"'].forEach(
    function requireMarkup(fragment) {
      if (html.indexOf(fragment) === -1) {
        throw new Error("missing " + fragment);
      }
    }
  );
});

check("page loads local assets", function pageLoadsLocalAssets() {
  var html = read("index.html");
  ["styles.css", "task-tools.js", "app.js"].forEach(function requireAsset(asset) {
    if (html.indexOf(asset) === -1) {
      throw new Error("missing asset reference " + asset);
    }
  });
});

check("runtime files contain no network or credential markers", function runtimeIsLocalOnly() {
  var runtime = ["index.html", "styles.css", "task-tools.js", "app.js"]
    .map(read)
    .join("\n");
  var forbidden = [
    /https?:\/\//i,
    /\bfetch\s*\(/,
    /\bXMLHttpRequest\b/,
    /\bWebSocket\b/,
    /\b(api[_-]?key|access[_-]?token|client[_-]?secret)\b/i
  ];
  forbidden.forEach(function rejectPattern(pattern) {
    if (pattern.test(runtime)) {
      throw new Error("found forbidden runtime pattern " + pattern);
    }
  });
});

if (failures.length > 0) {
  process.stderr.write("\n" + failures.join("\n") + "\n");
  process.exitCode = 1;
} else {
  process.stdout.write("\n" + passed + " checks passed.\n");
}
