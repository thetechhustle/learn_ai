# No-Install, No-Paid Simulation Path

This path teaches the course's decision-making and evidence-review skills when
you cannot install software, open a paid account, or connect a live tool. It
uses a synthetic task dashboard and prerecorded artifacts under
`starter/simulation/`. No artifact contains real credentials, customer data, or
live service access.

You need only a web browser and a place to write. You may read the artifacts on
GitHub without downloading them. If downloads are permitted, use **Code >
Download ZIP** on the
[course repository](https://github.com/thetechhustle/learn_ai), extract it, and
open `starter/simulation/README.md`.

## What this path proves

A complete submission can demonstrate that you can:

- write a bounded brief and distinguish context from instructions;
- predict and review an agent's gather, act, and verify loop;
- approve or deny actions based on scope, data, reversibility, and necessity;
- inspect a proposed diff and interpret verification evidence;
- evaluate a Skill, mock MCP tool, hook policy, and agent-team plan;
- plan recovery and a reviewable private or public release.

It does **not** prove that you installed a CLI, operated a live model, executed
commands, authenticated an integration, resolved a real merge, or deployed a
service. Label every result from this path **simulated**. A facilitator or
assessor must not relabel it as live execution.

## Get oriented

Open the
[simulation artifact index](https://github.com/thetechhustle/learn_ai/tree/main/starter/simulation).
Start a document named `simulation-journal` with this header:

```text
Course version or commit:
Date:
Access constraint:
Evidence mode: SIMULATED
Artifacts inspected:
Decisions I made before opening outcomes:
Observed in supplied evidence:
Still unknown without a live run:
```

The distinction between your prediction and the prerecorded outcome matters.
Write your decision first; open the outcome second.

## Chapters 1 and 2: claims, constraints, and prediction

1. Read Chapters 1 and 2.
2. Open `starter/simulation/project-brief.md`.
3. Mark each statement as **goal**, **context**, **constraint**, **acceptance
   criterion**, or **unsupported claim**.
4. Predict which files an agent would need to inspect and which file it should
   change.
5. Write one sentence explaining why a plausible answer is not verified work.

**Save as evidence:** your annotated brief, file prediction, and verification
sentence. Complete the Chapter 1 and Chapter 2 checkpoints and mark the
execution field `simulated`.

## Chapters 3 and 4: first session and Builder Loop

Use these artifacts in order:

1. `before/task-data.json`
2. `session-transcript.md`, stopping at every `YOUR DECISION` marker
3. `permission-prompts.md`, writing approve/deny and a reason before the
   supplied disposition
4. `changes.patch`
5. `after/task-data.json` and `after/summary.json`
6. `verifier-transcript.txt`

Before opening the patch, write:

- the intended file and value change;
- one action you would approve;
- one action you would deny;
- the expected change to **Unassigned open**;
- the smallest recovery surface if the edit is wrong.

Then inspect the patch line by line. Confirm that `T-104` receives an owner,
the expected summary changes from `1` to `0`, and no network, credential, or
unrelated file change appears. The transcript includes a stale-expected-output
failure between the data edit and the corrected result; explain why that
failure is useful evidence.

**Save as evidence:** permission decisions, diff review, failure explanation,
and a path-specific recovery plan. Do not write that you ran Git, Node, or
Claude Code.

## Chapter 5: context engineering

Compare `project-brief.md` with `context/CLAUDE.md`.

1. Circle durable instructions that belong in project context.
2. Cross out anything that is merely a one-time task.
3. Identify the data classification and the prohibited inputs.
4. Write one missing fact the agent would need before changing production
   behavior.
5. Draft a five-line session handoff that refers to the supplied diff and
   unresolved uncertainty without copying the entire transcript.

**Save as evidence:** the context classification and handoff. The artifact is a
model to critique, not proof that a live agent loaded project memory.

## Chapter 6: workflow and debugging

Use the three stages in `verifier-transcript.txt`: clean baseline, stale
expected output, and corrected pass.

1. At the failure, name the first useful error.
2. Separate the root failure from any skipped dependent check.
3. Propose the smallest repair without opening the corrected outcome.
4. Compare your proposal with `changes.patch`.
5. Write a human acceptance pass for table content, combined filters, keyboard
   use, and narrow-screen reflow.

**Save as evidence:** a diagnosis, minimal repair proposal, and acceptance
checklist. A prerecorded verifier result is not a test you executed.

## Chapter 7: Skill review

Open `skill/SKILL.md` and `skill/example-output.md`.

1. Identify its trigger, required inputs, ordered procedure, stop conditions,
   and output contract.
2. Find one instruction that prevents scope creep.
3. Apply the Skill on paper to `changes.patch`.
4. Compare your result with `example-output.md`.
5. Suggest one improvement without adding a live dependency.

**Save as evidence:** your paper execution, comparison, and improvement. This
demonstrates specification reading, not Skill installation or invocation.

## Chapter 8: mock tool connection and trust boundary

Open `mcp/tool-manifest.json`, then review `mcp/tool-transcript.json` one event
at a time.

1. Inventory each proposed capability and its data direction.
2. Decide whether read access is necessary; decline write access.
3. Treat tool-returned task text as untrusted data, including text that looks
   like an instruction.
4. Identify which annotation is descriptive rather than an enforced security
   boundary.
5. Design a manual export fallback with less access.

**Save as evidence:** the capability inventory, approval decision, suspicious
content finding, and lower-access alternative. No MCP server is connected in
this path.

## Chapter 9: hooks and guardrails

Read `hooks/policy.json`, predict the outcome of each event in
`hooks/events.json`, then open `hooks/transcript.txt`.

Classify every result as **allow**, **block**, or **verify after action**.
Explain:

- why a path rule can block a known dangerous action;
- why a passing hook does not prove the result is correct;
- why a `Stop` check is not a `SessionEnd` event;
- what still needs human review.

**Save as evidence:** predictions, comparison with the supplied transcript, and
one proposed negative test. These are mock policy records, not an installed
hook.

## Chapter 10: agent-team review

Open `team/team-plan.md`. Before reading `team/reviewer-report.md`, identify:

- exclusive file ownership for each worker;
- shared resources that file isolation does not protect;
- the integration order and verification gate;
- the condition that should stop the merge.

Then read the reviewer report and decide whether to accept, revise, or reject
the proposed integration. Write the exact bounded follow-up you would send.

**Save as evidence:** risk inventory, disposition, and follow-up. The actors are
prerecorded roles; no subagents or worktrees ran on your machine.

## Chapter 11: release and capstone handoff

Review `release/release-checklist.md`.

1. Select a private, authenticated, recorded, or public review surface.
2. Mark every mechanism **used**, **simulated**, or **declined with reason**.
3. Separate repository rollback from service, data, credential, and
   communication recovery.
4. Write the disclosure that would accompany the artifact.
5. Name one current product, price, or policy claim that must be rechecked at
   decision time.

Use the synthetic dashboard as the capstone surface, or submit your completed
simulation journal as a private recorded walkthrough. Apply the course capstone
rubric, but mark live-operation dimensions as simulated. Never invent
credentials, customer records, deployment URLs, command output, or user
feedback.

## Scoring simulated evidence

Use the same answer-free
[Scoring Guide](assessment/scoring-guide.md) as the live lanes. A simulated
artifact can earn full credit for a sound brief, prediction, permission
decision, diff review, risk analysis, recovery design, and honest disclosure.
It cannot serve as evidence that you personally ran a command, exercised a live
permission boundary, authenticated a tool, observed nondeterministic model
behavior, or completed a deployment.

For each chapter checkpoint:

1. Save your first attempt before opening the supplied disposition or example.
2. Name the artifact and exact evidence supporting each score.
3. Record **live**, **delegated**, or **simulated** beside every execution
   claim.
4. Score an unobserved live behavior as unproven, not as a pass.
5. Record one revision after comparing with the supplied outcome or peer
   feedback.

## Completion packet

Submit:

1. The simulation journal with predictions recorded before outcomes.
2. Chapter checkpoint responses labeled `simulated`.
3. The Chapter 3/4 diff and permission review.
4. The Chapter 8 trust-boundary inventory.
5. The Chapter 9 hook predictions and negative test.
6. The Chapter 10 integration disposition.
7. The Chapter 11 release checklist and disclosure.
8. A final list titled **What remains unproven without live access**.

Score the reasoning, evidence use, scope control, and honest disclosure. Do not
award live-execution credit for prerecorded artifacts. When access later
becomes available, repeat one bounded Chapter 3/4 task in a disposable
workspace to convert simulation evidence into observed execution evidence.
