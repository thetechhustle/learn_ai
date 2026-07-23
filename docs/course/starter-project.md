# Starter Project

Use the bundled task dashboard as the common practice surface for this course.
It is small enough to understand, but it still gives an agent structure,
behavior, data, styling, and tests to work with.

The project lives in `starter/`. It uses synthetic data, needs no secrets,
makes no network requests, and opens directly from `starter/index.html`.

## Baseline

Before changing anything:

1. Open `starter/index.html` in a browser.
2. Confirm the page reports **6 total**, **4 open**, **2 high-risk open**, and
   **1 unassigned open**.
3. Set Status to **In progress** and Risk to **High**. Only task `T-105` should
   remain.
4. Run:

    ```console
    $ node starter/verify.js
    ```

The result should end with `8 checks passed.` This is the deterministic
baseline: the browser view is the human check and the script is the machine
check.

!!! note "Commands in this guide"
    Commands assume you are at the repository root. If your terminal prompt is
    inside `starter/`, run `node verify.js` instead.

## Choose a lane

=== "No-code lane"

    Your first change is content and data, not program logic.

    1. Open `starter/index.html` in a text editor.
    2. Find the task with ID `T-104`.
    3. Change its empty owner from `"owner":""` to `"owner":"You"`.
    4. Save, refresh the browser, and confirm the task shows **You**.
    5. Run `node starter/verify.js`.

    The verifier will now report that the expected summary is stale because
    **Unassigned open** changed from 1 to 0. That failure is useful evidence.
    Change `unassignedOpen` in `starter/expected/summary.json` to `0`, rerun the
    verifier, and confirm all eight checks pass.

    A good agent request for this lane:

    > In the starter dashboard, assign T-104 to "You." Update only the expected
    > output affected by that data change. Run the verifier and explain its
    > result. Do not add packages, network calls, or credentials.

=== "Engineer lane"

    Your first change is a tested behavior.

    Add an owner filter without changing the task schema:

    1. Extend `filterTasks` in `starter/task-tools.js`.
    2. Add an owner control to `starter/index.html`.
    3. Wire it into `starter/app.js`.
    4. Add a focused check to `starter/verify.js`.
    5. Test keyboard use and the empty state in the browser.

    Define the acceptance criteria before delegating: **All owners** restores
    the complete set, selecting one owner shows only that owner's tasks, and
    the filter composes with status and risk.

    A good agent request for this lane:

    > Add the owner filter described in the course starter-project guide.
    > Preserve direct file opening and dependency-free verification. First
    > inspect the existing filter function and describe the files you expect to
    > change. After implementation, run the verifier and report the manual
    > keyboard checks I still need to perform.

## Checkpoints

Use these gates for either lane:

| Gate | Evidence |
| --- | --- |
| Baseline | Clean starter reports eight passing checks |
| Plan | Request names files, constraints, and observable acceptance criteria |
| Small change | `git diff -- starter` contains only intended work |
| Machine verification | `node starter/verify.js` exits successfully |
| Human verification | Browser content, filters, focus, and narrow layout work |
| Reflection | Journal records failure, fix, and remaining uncertainty |

At each gate, stop if the evidence disagrees with the plan. Read the diff and
error output before asking the agent to try again.

## Accessibility alternatives

The dashboard is not the only way to complete the exercise:

- If visual inspection is difficult, use the verifier output plus a screen
  reader's table navigation. The table has a caption, row headers, native
  selects, live result counts, and a skip link.
- If a mouse is difficult to use, complete the manual check with
  ++tab++, arrow keys, ++space++, and ++enter++.
- If color is difficult to distinguish, use the written Risk column; color is
  not the only high-risk indicator.
- If editing JSON punctuation creates a barrier, ask a partner or agent to make
  the precise data edit, then verify the diff and run the same acceptance
  checks yourself.
- If running Node is blocked, inspect the expected summary manually and have a
  partner run `verify.js`. Record that the machine check was delegated rather
  than claiming you ran it.

Accessibility changes are valid starter-project work. Preserve semantic HTML
and keyboard behavior, then add a verifier check where automation can provide
reliable evidence.

## Definition of done

A starter-project change is done only when:

- Its acceptance criteria are observable.
- The diff contains no unexplained files.
- The verifier passes, or the journal explains a known failure.
- A human checks the browser behavior.
- No real customer, employee, health, financial, or account data was added.
- No dependency, credential, or network access was introduced silently.

When a check fails, use the [Recovery Guide](recovery-guide.md).
