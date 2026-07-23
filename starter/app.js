(function startDashboard() {
  "use strict";

  var dataElement = document.getElementById("task-data");
  var summaryElement = document.getElementById("summary-grid");
  var rowsElement = document.getElementById("task-rows");
  var resultCountElement = document.getElementById("result-count");
  var emptyStateElement = document.getElementById("empty-state");
  var statusFilter = document.getElementById("status-filter");
  var riskFilter = document.getElementById("risk-filter");

  var tasks;
  try {
    tasks = JSON.parse(dataElement.textContent);
  } catch (error) {
    showError("The task data is not valid JSON. Run node verify.js for details.");
    return;
  }

  var validationErrors = window.TaskTools.validateTasks(tasks);
  if (validationErrors.length > 0) {
    showError(validationErrors.join(" "));
    return;
  }

  renderSummary(window.TaskTools.summarizeTasks(tasks));
  renderTasks();
  statusFilter.addEventListener("change", renderTasks);
  riskFilter.addEventListener("change", renderTasks);

  function renderSummary(summary) {
    var items = [
      ["Total tasks", summary.total],
      ["Open tasks", summary.open],
      ["High-risk open", summary.highRiskOpen],
      ["Unassigned open", summary.unassignedOpen]
    ];

    summaryElement.replaceChildren();
    items.forEach(function addSummaryItem(item) {
      var wrapper = document.createElement("div");
      var value = document.createElement("strong");
      var label = document.createElement("span");
      wrapper.className = "summary-item";
      value.textContent = item[1];
      label.textContent = item[0];
      wrapper.append(value, label);
      summaryElement.append(wrapper);
    });
  }

  function renderTasks() {
    var visibleTasks = window.TaskTools.filterTasks(tasks, {
      status: statusFilter.value,
      risk: riskFilter.value
    });

    rowsElement.replaceChildren();
    visibleTasks.forEach(function addTaskRow(task) {
      var row = document.createElement("tr");
      [
        task.id,
        task.title,
        labelStatus(task.status),
        labelStatus(task.risk),
        task.owner || "Unassigned"
      ].forEach(function addCell(value, index) {
        var cell = document.createElement(index === 0 ? "th" : "td");
        if (index === 0) {
          cell.scope = "row";
        }
        if (index === 3 && task.risk === "high") {
          cell.className = "risk-high";
        }
        cell.textContent = value;
        row.append(cell);
      });
      rowsElement.append(row);
    });

    resultCountElement.textContent =
      visibleTasks.length + (visibleTasks.length === 1 ? " task shown" : " tasks shown");
    emptyStateElement.hidden = visibleTasks.length !== 0;
  }

  function labelStatus(value) {
    return value
      .split("-")
      .map(function capitalize(part) {
        return part.charAt(0).toUpperCase() + part.slice(1);
      })
      .join(" ");
  }

  function showError(message) {
    summaryElement.textContent = message;
    summaryElement.setAttribute("role", "alert");
  }
})();
