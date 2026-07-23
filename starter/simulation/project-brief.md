# Synthetic Dashboard Change Brief

## Goal

Assign task `T-104` to the learner and keep the dashboard summary accurate.

## Context

- The dashboard is a dependency-free static page.
- Its six tasks are synthetic and stored in the `task-data` JSON block.
- `expected/summary.json` is the machine-readable expected summary.
- The browser view and verifier are complementary evidence.

## Constraints

- Change only the owner for `T-104` and the directly affected expected value.
- Add no package, network request, credential, tracking, or real-person data.
- Preserve direct browser opening, semantic table markup, and existing filters.
- Stop if another production file appears necessary.

## Acceptance criteria

- `T-104` shows owner `You`.
- The dashboard reports zero unassigned open tasks.
- Status **In progress** plus Risk **High** still shows only `T-105`.
- The supplied verifier evidence ends with all eight checks passing.
- The diff contains only the intended data and expected-output lines.

## Claim to challenge

This two-line data change will make the dashboard useful for every project
team.

That sentence is an untested product hypothesis, not an acceptance criterion.
