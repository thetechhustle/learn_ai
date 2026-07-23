# Competency Framework

The entry and exit diagnostics assess the same eight competencies on the same four-level scale. Chapter tasks provide repeated evidence along the way.

## Level scale

| Level | Meaning | Observable pattern |
| --- | --- | --- |
| 0 — Not yet evidenced | The response is missing, unsafe, or unrelated. | No usable decision or artifact; major risk is ignored. |
| 1 — Emerging | The learner names part of the idea but cannot yet apply it reliably. | Generic advice, incomplete steps, or verification by appearance alone. |
| 2 — Capable | The learner applies the competency to the stated situation with relevant evidence. | Bounded decision, workable artifact, appropriate check, and material risks addressed. |
| 3 — Adaptive | The learner applies it, explains tradeoffs, and adjusts for stakes or failure. | Multiple evidence types, explicit limitations, recovery or escalation, and a justified alternative. |

A polished artifact is not automatically Level 3. A plain artifact with strong judgment can be.

## Competencies and anchors

### C1 — Explain AI-agent behavior and limits

- **Level 1:** Distinguishes a chatbot from an agent or says AI can be wrong.
- **Level 2:** Explains model output, context, tools, and verification in practical terms; predicts a relevant failure.
- **Level 3:** Connects uncertainty and context limits to a proportionate verification strategy without claiming to know hidden model reasoning.

### C2 — Frame and delegate bounded work

- **Level 1:** States a goal.
- **Level 2:** Provides outcome, context, constraints, examples or inputs, and observable done-means.
- **Level 3:** Separates must-have from not-today work, identifies ambiguity, and defines decision or escalation points.

### C3 — Operate files, versions, and sessions safely

- **Level 1:** Names Git, backups, permissions, or secrets as safety concerns.
- **Level 2:** Uses an isolated project, inspects changes, makes recoverable checkpoints, and protects credentials and sensitive data.
- **Level 3:** Matches recovery to the failure type, explains what Git cannot recover, and treats unknown code, hooks, and configuration as untrusted until reviewed.

### C4 — Run the Builder Loop and verify results

- **Level 1:** Asks the agent to check its work.
- **Level 2:** Moves through vision, context, build, verify, and ship; uses an independent check tied to done-means.
- **Level 3:** Tests a failure path, records what was caught, and includes human acceptance or source verification where judgment is required.

### C5 — Design useful, maintainable context

- **Level 1:** Adds instructions or notes.
- **Level 2:** Places stable project facts, commands, conventions, and boundaries in the right persistent layer and keeps task-specific detail scoped.
- **Level 3:** Demonstrates a behavior change, removes stale or sensitive context, and preserves decisions across a fresh session.

### C6 — Select tools and manage trust boundaries

- **Level 1:** Chooses a tool because it is available or convenient.
- **Level 2:** Compares capability, permissions, data exposure, source trust, cost, and a simpler alternative.
- **Level 3:** Applies least privilege, tests with synthetic or read-only data, defines approval boundaries, and declines the connection when residual risk exceeds value.

### C7 — Mechanize quality and orchestrate work

- **Level 1:** Uses a checklist or divides work.
- **Level 2:** Creates a repeatable validator or guardrail and gives parallel work explicit ownership, inputs, outputs, and integration checks.
- **Level 3:** Proves the mechanism catches a seeded failure, identifies shared-resource risks, and justifies when sequential or single-agent work is better.

### C8 — Ship and operate a responsible, viable result

- **Level 1:** Publishes or proposes a result.
- **Level 2:** Chooses an appropriate public or private delivery, verifies accessibility and core operation, documents cost and handoff, and addresses data, provenance, disclosure, and recourse.
- **Level 3:** Uses monitoring plus recovery evidence, tests representative users and misuse cases, and makes calibrated value claims supported by observed evidence.

## Competency-to-course map

| Chapter | Primary competencies | Reinforced competencies |
| --- | --- | --- |
| 1 | C1, C2 | C8 |
| 2 | C1, C2 | C4, C6 |
| 3 | C3 | C4 |
| 4 | C4 | C2, C3 |
| 5 | C5 | C2, C4 |
| 6 | C4 | C2, C5, C8 |
| 7 | C5 | C4, C7 |
| 8 | C6 | C3, C8 |
| 9 | C7 | C3, C4, C6 |
| 10 | C7 | C2, C3, C4 |
| 11 | C8 | C4, C6, C7 |

## What scores mean

The diagnostic maximum is 24 points: eight competencies multiplied by three. Total score is useful for a broad snapshot, but the eight competency scores are the actionable result. Two learners with 15 points may need entirely different practice.

| Total | Interpretation |
| --- | --- |
| 0–7 | Start with Foundations. Use the supported starter path and seek review before connecting tools or publishing. |
| 8–14 | You have useful pieces but inconsistent execution. Follow the full course and focus first on any 0 or 1. |
| 15–19 | You can handle bounded, low-stakes work. Use chapter tasks to strengthen weak competencies and adaptive judgment. |
| 20–24 | You show broad readiness. Do not skip the tasks: use them to test transfer, current product knowledge, and higher-stakes judgment. |

Regardless of total, a **0 in C3, C6, or C8 is a stop signal** for unsupervised work with real credentials, external systems, sensitive data, or affected users. Practice with synthetic data and a reviewer first.

Growth is not just a higher total. Count as meaningful growth when:

- a 0 or 1 becomes a 2 with evidence;
- a 2 becomes a 3 through better tradeoff or failure reasoning;
- an exit answer is more specific, testable, and appropriately cautious; or
- you correctly decline automation or deployment that your entry answer would have accepted.
