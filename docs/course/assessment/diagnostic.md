# Paired Diagnostics

The entry and exit forms assess the same eight competencies through different situations. Complete the entry form before Chapter 1 and the exit form after Chapter 11. The matched design measures transfer without relying on memorized answers.

## Entry Diagnostic

Complete this before Chapter 1. It is a baseline, not an admissions test. Do not study for it, and do not ask an AI assistant to compose your judgment. You may use accessibility and language support.

Allow about 45–75 minutes. Short, concrete answers are enough.

### Entry instructions

1. Label a page or recording `Entry Diagnostic` and add the date.
2. Answer all eight situations. If you do not know a command or product, describe the process you would use.
3. Note any AI, person, or reference source that helped.
4. Self-score with the [Answer Key and Evidence Guide](answer-key.md#diagnostic-reference-patterns).
5. Record one evidence sentence and one next action for each competency.

### Entry situations

#### 1. What is the system doing? — C1

A writing assistant produces three confident citations for a policy memo. One link works but does not support the claim; two links do not exist.

Explain in plain language how a fluent system can produce this result. Identify what the model can and cannot establish by itself, then give a check proportionate to a low-stakes blog post and a check for a client compliance memo.

#### 2. Turn a wish into a brief — C2

Someone says, “Make me a great event website by tomorrow.”

Write the brief you would give an agent. Include the intended user, outcome, supplied inputs, constraints, observable done-means, what is not being built, and questions or decisions that should stop work.

#### 3. Make the work recoverable — C3

An agent is about to reorganize a folder containing the only copies of family photos and several unrelated documents. The folder is not under version control.

Describe what you would do before allowing any action, how you would inspect a small trial, what recovery evidence you need, and which risks Git would and would not solve.

#### 4. Prove a result — C4

An agent says a contact form is complete because the page looks correct and the submit button works once.

Define “done” and a verification pass. Include one normal path, one failure path, one check independent of the agent’s claim, and the evidence you would retain.

#### 5. Put context in the right place — C5

You repeatedly tell an agent: use the organization’s approved tone; never include client names in examples; run a link check before delivery; this week’s task is a July newsletter.

Decide what belongs in persistent project context, what belongs only in the current task, what should not be stored there, and how you would tell whether the context helped.

#### 6. Decide whether to connect a tool — C6

An unfamiliar community MCP server offers to read and update your real calendar. Its README asks for a broad account token and recommends approving all tool calls.

Write an accept, modify, or decline decision. Address source trust, permissions, data exposure, safer alternatives, test data, approval boundaries, and what new evidence could change your decision.

#### 7. Turn a rule into a mechanism — C7

A three-person project keeps shipping pages with broken links. The team’s checklist says “remember to check links,” but misses continue.

Propose a repeatable control and how you would prove it works. Then split investigation, implementation, and review between people or agents without letting parallel work overwrite or invalidate other work. You may also justify a sequential plan.

#### 8. Choose a responsible delivery — C8

You built a dashboard from a volunteer group’s membership spreadsheet. It includes names, contact details, attendance, and AI-written participation summaries. The group wants a public portfolio link.

Decide how to demonstrate or deliver the work. Address authorization, data minimization, provider handling, provenance, affected people, accessibility, disclosure, correction or appeal, misuse, monitoring, recovery, cost, and claims you can honestly make.

### Entry score sheet

| Competency | Score, 0–3 | Evidence for the score | Next action |
| --- | ---: | --- | --- |
| C1 — Behavior and limits |  |  |  |
| C2 — Framing and delegation |  |  |  |
| C3 — Safe operation |  |  |  |
| C4 — Builder Loop and verification |  |  |  |
| C5 — Context engineering |  |  |  |
| C6 — Tool and trust judgment |  |  |  |
| C7 — Mechanisms and orchestration |  |  |  |
| C8 — Responsible shipping |  |  |  |
| **Total / 24** |  |  |  |

Interpret your profile with [What scores mean](competency-framework.md#what-scores-mean). Save the original answers unchanged so the exit comparison is honest.

## Exit Diagnostic

Complete this after Chapter 11 and before or alongside the capstone. This form assesses the same competencies as the entry diagnostic through different situations, so improvement means transfer rather than memorizing an answer.

Allow about 60–90 minutes. Work independently on the judgment first. You may then use tools to produce evidence, but disclose their contribution.

### Exit instructions

1. Label a page or recording `Exit Diagnostic` and add the date.
2. Answer all eight situations. Include artifacts or demonstrations where requested.
3. Cite the current source for any product-specific behavior that materially affects your plan.
4. Self-score with the [Answer Key and Evidence Guide](answer-key.md#diagnostic-reference-patterns).
5. Ask a peer to score at least C3, C6, and C8 without seeing your self-score.

### Exit situations

#### 1. Explain and calibrate — C1

An agent summarizes a research folder and reports that “the evidence proves” a new workflow increases output by 40%. The folder contains one vendor case study, two opinion posts, and a small internal survey.

Explain how the system could produce that conclusion. Rewrite the claim at a supportable confidence level and design verification for an informal team note versus a decision that changes employee evaluation.

#### 2. Brief consequential work — C2

A community clinic asks for “an AI intake helper that tells patients what to do next.” You do not have enough information to know whether the tool would offer logistics, medical advice, or triage.

Create a bounded discovery and prototype brief. Include outcome, users, constraints, supplied evidence, observable done-means, not-today scope, unresolved decisions, expert review, and conditions that stop automation.

#### 3. Inspect an unfamiliar project — C3

You clone a public repository that contains source code, package scripts, hooks, agent instructions, an example environment file, and a database migration. You are asked to “run it and let the agent fix whatever breaks.”

Provide a safe preflight, checkpoint, execution, review, and recovery plan. Demonstrate the inspection commands or equivalent interface actions on a disposable project. Explain what version control, backups, a sandbox, and permissions each do not guarantee.

#### 4. Verify across evidence types — C4

An agent changes a small service so exported dates display in the user’s locale. Automated tests pass.

Define observable done-means and produce a verification matrix covering expected behavior, an edge or failure case, regression evidence, human acceptance, and any source that must be checked. Show how a failed check returns to the loop.

#### 5. Diagnose context quality — C5

A project’s persistent instructions have grown to twelve pages. They contain current commands, old launch plans, contradictory style rules, meeting notes, a client token, and task details for work finished last month. The agent sometimes follows the wrong rule.

Propose and demonstrate a context audit: retain, relocate, rewrite, or remove each class of content. Define the correct memory layer, remove the secret from all relevant exposure paths, and design a fresh-session comparison that can show improvement.

#### 6. Design least-privilege tool use — C6

A reporting workflow needs order totals from a production database and must send a weekly summary to a team channel. Available options include a broad write-capable MCP server, database and messaging CLIs, a read-only export, or manual handoff.

Choose and justify an architecture. Include data classification, credentials, least privilege, source or package trust, prompt-injection exposure, approval gates, synthetic testing, logging, revocation, and a simpler fallback.

#### 7. Build and test a harness — C7

Two agents could update documentation and application code in parallel for a release. Both need shared schema information; tests use the same local database and port.

Design the work allocation, isolation, integration order, and validation harness. Seed one safe failure and show the mechanism catching it. Explain shared-resource risks and when one agent or sequential work would be the better choice.

#### 8. Prepare an accountable launch — C8

A small business wants to launch an AI-assisted customer-support workflow. Draft replies use order history and are reviewed by staff before sending. The owner wants to advertise that it “eliminates support mistakes and cuts costs in half.”

Create a launch decision and evidence pack: appropriate deployment, authorization and provider handling, evaluation cases, accessibility, provenance, AI disclosure, human review, correction or escalation, abuse controls, monitoring, recovery, cost budget, handoff, and a calibrated claim supported by available evidence.

### Exit score and comparison

| Competency | Entry | Exit | Change | Best exit evidence | Next deliberate practice |
| --- | ---: | ---: | ---: | --- | --- |
| C1 — Behavior and limits |  |  |  |  |  |
| C2 — Framing and delegation |  |  |  |  |  |
| C3 — Safe operation |  |  |  |  |  |
| C4 — Builder Loop and verification |  |  |  |  |  |
| C5 — Context engineering |  |  |  |  |  |
| C6 — Tool and trust judgment |  |  |  |  |  |
| C7 — Mechanisms and orchestration |  |  |  |  |  |
| C8 — Responsible shipping |  |  |  |  |  |
| **Total / 24** |  |  |  |  |  |

Use [What scores mean](competency-framework.md#what-scores-mean), but review the evidence before the number. A lower score can reflect more accurate self-judgment. Resolve self/peer differences by pointing to evidence, not averaging automatically.

Choose one next project that exercises your lowest competency. If C3, C6, or C8 is below 2, keep the project isolated, synthetic, and supervised.
