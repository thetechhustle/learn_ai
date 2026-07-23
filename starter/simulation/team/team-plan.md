# Mock Agent-Team Plan

No agents or worktrees are started by this fixture.

## Goal

Prepare the two-line synthetic owner change and review it independently.

## Roles and exclusive file ownership

- **Implementer:** may propose changes only to `starter/index.html` and
  `starter/expected/summary.json`.
- **Reviewer:** read-only review of the brief, diff, and verifier evidence;
  writes only `starter/simulation/team/reviewer-report.md`.
- **Integrator:** accepts or rejects the proposed patch after review; makes no
  additional feature edits.

## Shared resources

Even with separate worktrees, the roles could share account credentials,
network destinations, package caches, service rate limits, local ports, and
external data. This simulation permits none of them. Worktrees isolate checked
out files, not those shared resources.

## Order and gates

1. Implementer proposes the named patch.
2. Verifier evidence records expected failure, then corrected pass.
3. Reviewer maps every line to the brief and lists residual human checks.
4. Integrator stops if any unrelated path, real data, external action,
   unexplained line, or failed check remains.
5. Human acceptance happens before release.

## Deliberate review question

The implementation passes the supplied machine checks. Is that sufficient to
claim that keyboard behavior and narrow-screen reflow were tested?
