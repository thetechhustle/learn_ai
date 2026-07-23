# Recovery Guide

Errors are part of agent work. Recovery starts by preserving evidence, finding
the smallest broken surface, and returning only that surface to a known state.
Do not begin with a blanket restore, reset, clean, or delete command.

## Stop and inspect

From the repository root, capture the current state:

```console
$ git status --short
$ git diff -- starter
$ node starter/verify.js
```

Read the first useful error, not just the last line. Copy the command, error,
and current `git status --short` into your project journal before changing
anything else.

If the task-data JSON cannot be parsed, the verifier reports its approximate
line and column and marks the schema, summary, and filter checks
`SKIP: task data unavailable`. Those skips are one dependency failure, not
three new defects. Repair the parse error first, then rerun all checks.

!!! warning "Protect work Git does not track"
    Git cannot restore untracked or ignored files, browser state, databases,
    external services, or overwritten secrets. Before recovery, copy any
    important untracked file outside the repository and confirm what is
    actually backed up.

## Match the symptom

| Symptom | Likely cause | First check |
| --- | --- | --- |
| Browser shows raw text or no styling | Asset path or file name changed | Confirm the three local asset names in `index.html` |
| Browser reports invalid JSON | Missing quote, comma, bracket, or brace | Run the verifier and inspect the `task-data` block |
| Expected summary fails | Data changed but expected output did not | Compare actual and expected values in the error |
| Schema check fails | Field missing or unsupported status/risk | Find the task number named by the verifier |
| Filters show the wrong task | Filter condition changed | Run the focused filter check and inspect `filterTasks` |
| `node: command not found` | Node is absent or terminal path is stale | Follow [Setup](setup.md), then reopen the terminal |
| `Cannot find module` | Command ran from the wrong directory | Use `node starter/verify.js` at the repository root |
| Agent changed unrelated files | Request scope was too broad | Inspect `git diff --name-only` before restoring anything |

## Repair the smallest surface

=== "No-code lane"

    1. Ask the agent to explain the exact verifier error without editing.
    2. Compare the changed line with the baseline shape around it.
    3. Correct one value or punctuation error.
    4. Save and rerun `node starter/verify.js`.
    5. Refresh the browser only after the machine check passes.

    If the agent proposes packages, a server, credentials, or a rewrite for a
    data error, stop it and restate the constraint: repair the existing local,
    dependency-free project.

=== "Engineer lane"

    1. Isolate the failing pure function in `task-tools.js`.
    2. Add or tighten one check in `verify.js` that reproduces the failure.
    3. Confirm the new check fails for the expected reason.
    4. Make the minimum implementation change.
    5. Rerun the full verifier and inspect the diff.

    Keep the failing check as regression evidence unless it only asserted an
    implementation detail.

## Restore one known file

First inspect the file and confirm that it contains no work you need:

```console
$ git diff -- starter/styles.css
```

To discard only the unstaged edits in that reviewed file:

```console
$ git restore --worktree starter/styles.css
```

To restore a reviewed file to a specific checkpoint:

```console
$ git log --oneline -- starter/styles.css
$ git show CHECKPOINT:starter/styles.css
$ git restore --source=CHECKPOINT --worktree starter/styles.css
```

Replace `CHECKPOINT` with a commit ID you inspected. These commands affect the
named file. They do not recover untracked work or external state.

If a change is staged, inspect both versions before deciding:

```console
$ git diff --cached -- starter/styles.css
$ git diff -- starter/styles.css
```

Do not copy a recovery command from an agent until you can name which file,
which version, and which work the command will discard.

## Recover without Git

If this is a downloaded clean copy rather than a Git checkout:

1. Rename the broken folder to `starter-investigation`.
2. Extract a second clean course copy into a different folder.
3. Run the clean copy's verifier before moving any files.
4. Compare one file at a time.
5. Move only the repaired work into the clean copy.

Keeping the broken copy preserves evidence and prevents an attempted recovery
from becoming permanent data loss.

## Recover in the simulation path

If you cannot run Git or Node, use the supplied evidence without claiming live
execution:

1. Preserve your written decision before opening the answer artifact.
2. Compare `starter/simulation/before/task-data.json` with
   `starter/simulation/after/task-data.json`.
3. Use `starter/simulation/changes.patch` to identify the exact changed lines.
4. Compare your predicted verifier result with
   `starter/simulation/verifier-transcript.txt`.
5. Record which artifact you inspected and mark the result **simulated**, not
   machine-executed by you.

Return to the clean `before` artifact to reset the exercise. This rehearses
diagnosis and evidence review; it does not demonstrate command execution or
live system recovery. The full sequence is in the
[Simulation Path](simulation-path.md).

## Ask for useful agent help

Use a bounded repair request:

> Diagnose the first failure from `node starter/verify.js`. Do not edit yet.
> Identify the smallest responsible file and show how the current output differs
> from the expected output. Preserve untracked work and unrelated changes. Do
> not run reset, clean, blanket restore, or delete commands.

After the explanation is credible:

> Make the minimum repair in the identified file. Run the full verifier and
> show `git diff -- starter`. Stop if another file must change.

## Recovery checkpoint

Recovery is complete when:

- The original symptom is reproducible or explained.
- The smallest relevant check passes.
- The full verifier passes.
- The browser behavior is checked again.
- `git diff --name-only` contains no surprise files.
- The project journal says what failed, what changed, and what remains unknown.

Return to the [Starter Project](starter-project.md) only after this checkpoint.
