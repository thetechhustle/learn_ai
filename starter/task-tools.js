(function exposeTaskTools(root) {
  "use strict";

  var statuses = ["backlog", "in-progress", "done"];
  var risks = ["low", "medium", "high"];

  function summarizeTasks(tasks) {
    var summary = {
      total: tasks.length,
      open: 0,
      done: 0,
      highRiskOpen: 0,
      unassignedOpen: 0
    };

    tasks.forEach(function countTask(task) {
      var isOpen = task.status !== "done";
      if (isOpen) {
        summary.open += 1;
      } else {
        summary.done += 1;
      }
      if (isOpen && task.risk === "high") {
        summary.highRiskOpen += 1;
      }
      if (isOpen && task.owner.trim() === "") {
        summary.unassignedOpen += 1;
      }
    });

    return summary;
  }

  function filterTasks(tasks, filters) {
    return tasks.filter(function taskMatches(task) {
      var statusMatches = filters.status === "all" || task.status === filters.status;
      var riskMatches = filters.risk === "all" || task.risk === filters.risk;
      return statusMatches && riskMatches;
    });
  }

  function validateTasks(tasks) {
    var errors = [];
    var ids = {};

    if (!Array.isArray(tasks) || tasks.length === 0) {
      return ["Task data must be a non-empty array."];
    }

    tasks.forEach(function validateTask(task, index) {
      var location = "Task " + (index + 1);
      ["id", "title", "status", "risk", "owner"].forEach(function requireField(field) {
        if (typeof task[field] !== "string") {
          errors.push(location + " needs a string " + field + ".");
        }
      });

      if (typeof task.id === "string") {
        if (ids[task.id]) {
          errors.push("Task IDs must be unique: " + task.id + ".");
        }
        ids[task.id] = true;
      }
      if (typeof task.status === "string" && statuses.indexOf(task.status) === -1) {
        errors.push(location + " has an unsupported status: " + task.status + ".");
      }
      if (typeof task.risk === "string" && risks.indexOf(task.risk) === -1) {
        errors.push(location + " has an unsupported risk: " + task.risk + ".");
      }
    });

    return errors;
  }

  var api = {
    filterTasks: filterTasks,
    summarizeTasks: summarizeTasks,
    validateTasks: validateTasks
  };

  if (typeof module !== "undefined" && module.exports) {
    module.exports = api;
  } else {
    root.TaskTools = api;
  }
})(typeof window !== "undefined" ? window : globalThis);
