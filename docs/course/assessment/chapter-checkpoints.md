# Chapter Checkpoints

Complete one task after every chapter. Each task should leave a small artifact that another person can inspect. Aim for 30–90 minutes; Chapters 6, 10, 11, and 12 may take longer.

## How to complete a task

1. Choose the no-code or engineer lane. You may switch lanes between chapters.
2. Use only public, synthetic, or explicitly authorized data.
3. Save the required evidence in the matching assessment folder.
4. Use the public [Scoring Guide](scoring-guide.md) criteria, then save the first attempt before opening worked chapter patterns.
5. Record whether worked patterns were viewed before the attempt: `yes / no / unsure`.
6. Continue through [Finish and Save Before Review](review-after-attempt.md), self-score, and ask a peer to review at least one task per track: Chapters 1–3, 4–6, 7–9, and 10–12.
7. Record one revision made because of a failed check or feedback.

No live service is required. A local artifact, screen recording, annotated mockup, or written simulation is valid when it shows the requested competency.

## Chapter 1 — Opportunity without hype

**Primary competencies:** C1, C2
**Reinforced competencies:** C8
**Task:** Select one possible build from your life or work. Produce a one-page opportunity brief that distinguishes a chatbot response from agentic work and narrows the idea to a seven-day experiment.

=== "No-code lane"

    Choose a website, personal workflow, research aid, dashboard, or content process. Use plain language and a sketch, checklist, or sample input/output.

=== "Engineer lane"

    Choose a small feature, maintenance task, internal tool, or development workflow. Include the likely repository or system boundary, but do not design the architecture yet.

**Required evidence**

- Named user and current problem, based on an observation or conversation rather than an invented market claim.
- A sequence showing where the agent would gather, act, and verify.
- One thing a chatbot answer could do and one additional capability or permission agentic execution would require.
- Must-have, not-today, observable done-means, and one reason not to build it.
- A claim ledger labeling important statements as observed, sourced, assumed, or unknown.

**Evidence standard:** A capable artifact distinguishes conversation from tool-mediated action, makes no unsupported productivity or income promise, and ends with a testable experiment. A list of exciting ideas without a user, limit, or evidence is insufficient.

## Chapter 2 — Predict the failure

**Primary competencies:** C1, C2
**Reinforced competencies:** C4, C6
**Task:** Design two delegations for the same outcome: one low-stakes and one higher-stakes. Predict how model behavior, context, and tools could create errors, then scale verification accordingly.

=== "No-code lane"

    Use a public-information task such as a local-event digest, comparison table, or factual newsletter draft. For the higher-stakes version, imagine the output informs eligibility, health, legal, financial, employment, or safety decisions; do not use real personal data.

=== "Engineer lane"

    Use a code task such as dependency research, data transformation, or a configuration change. Raise the stakes by placing it on a production, security, privacy, or billing path in a written simulation.

**Required evidence**

- Two five-element briefs: outcome, context, constraints, examples or inputs, and done-means.
- A context budget: what the model must see, what it does not need, and what may become stale.
- Three predicted failure modes, including a plausible fabricated or unsupported claim.
- Verification for each version and a sentence explaining why the checks differ.
- A justified model/tool choice that separates transferable concepts from current product details.

**Evidence standard:** A capable answer connects failure predictions to specific checks and does not treat fluent output, citations supplied by the model, or model self-explanation as proof.

## Chapter 3 — Recoverable first session

**Primary competencies:** C3
**Reinforced competencies:** C4
**Task:** Run or simulate a small agent-assisted edit inside a disposable project and produce a preflight-to-recovery record.

=== "No-code lane"

    Use a folder containing a simple text, Markdown, CSV, or HTML artifact. You may use a graphical Git client and file browser; record equivalent checkpoints and inspections.

=== "Engineer lane"

    Use a tiny repository and a scoped code or documentation change. Inspect configuration and scripts before installing dependencies or running code.

**Required evidence**

- Project boundary, backup or version-control state, data classification, and secret check.
- Before snapshot or commit; a list of specifically intended files.
- The brief, permission decisions, and the diff or before/after comparison.
- A successful checkpoint plus one demonstrated recovery on a harmless seeded edit.
- An explanation of one loss Git cannot recover and one risk permissions do not prevent.

**Evidence standard:** A capable run occurs only in a disposable or backed-up location, reviews exact changes, and demonstrates recovery. Saying “Git is my backup” or approving an unknown project wholesale is insufficient.

## Chapter 4 — Builder Loop with a caught failure

**Primary competencies:** C4
**Reinforced competencies:** C2, C3
**Task:** Take a small artifact through vision, context, build, verify, and ship to a review surface. Intentionally include or ask a peer to introduce one harmless defect, then catch it.

=== "No-code lane"

    Build or revise a one-page site, structured document, form, tracker, or public-data summary.

=== "Engineer lane"

    Implement a small behavior change with a testable interface. Keep the change narrow enough to review completely.

**Required evidence**

- Vision brief with observable done-means and not-today scope.
- Reviewed plan for work expected to take more than ten minutes.
- Change comparison or diff and notes on any surprising action.
- Verification pyramid: cheap checks, realistic behavior check, and human acceptance.
- Failure evidence, correction evidence, and a reviewable final surface.

**Evidence standard:** A capable submission shows the failed check, not only the final success, and uses evidence independent of the agent’s declaration.

## Chapter 5 — Context experiment

**Primary competencies:** C5
**Reinforced competencies:** C2, C4
**Task:** Run the same bounded request twice: first without project-specific persistent context, then in a fresh session with a deliberately designed context file. Compare behavior.

=== "No-code lane"

    Use a writing, planning, research, or simple site project. Persistent context may be a project instruction file supported by your agent.

=== "Engineer lane"

    Use a small repository with real commands, layout, conventions, and boundaries. Keep task-only implementation detail out of persistent context.

**Required evidence**

- Original request held substantially constant across both trials.
- Persistent context covering purpose, layout or sources, conventions, commands or process, and boundaries.
- A decision record stored separately from transient session detail.
- Before/after comparison against at least three observable criteria.
- Context hygiene note: stale, duplicate, sensitive, or over-specific information removed or relocated.

**Evidence standard:** A capable submission demonstrates a behavior difference without claiming one trial proves universal improvement. A long instruction file with no comparison or maintenance decision is insufficient.

## Chapter 6 — Reusable real-work workflow

**Primary competencies:** C4
**Reinforced competencies:** C2, C5, C8
**Task:** Build one useful workflow and run it twice on different inputs. The second run should require less re-explanation while preserving human review.

=== "No-code lane"

    Choose a research digest, document transformation, content preparation, file triage simulation, tracker update, or simple web publish. Keep external actions in draft or approval mode.

=== "Engineer lane"

    Choose a debug routine, small site workflow, release-note generator, data transformation, or maintenance automation with tests.

**Required evidence**

- Repetition/value filter: frequency, time or error baseline, and why automation is warranted.
- A reusable brief, command, template, or documented routine.
- Two run records with different inputs and comparable done-means.
- Human acceptance and source checks; approval before any external write or send.
- Measured result stated narrowly: observed time, defects, or steps for these two runs, not a universal promise.

**Evidence standard:** A capable workflow is reproducible and keeps consequential judgment or external action under appropriate human control. A one-off generated artifact is insufficient.

## Chapter 7 — Skill that earns reuse

**Primary competencies:** C5
**Reinforced competencies:** C4, C7
**Task:** Package a repeated workflow as a Skill or equivalent reusable agent instruction, test invocation and non-invocation cases, and revise it.

=== "No-code lane"

    Package a content check, meeting-prep routine, research format, accessibility review, or file-naming workflow. Scripts are optional.

=== "Engineer lane"

    Package a repository-specific review, migration check, test triage, documentation routine, or scaffold. Include a script only if it removes real ambiguity or repetition.

**Required evidence**

- Purpose and description that make invocation conditions clear.
- Instructions, references, examples, boundaries, and portable path handling where relevant.
- Two positive cases, one should-not-run case, and one malformed or incomplete input.
- Expected results defined before running tests.
- A failure or weakness, revision, and version note.

**Evidence standard:** A capable Skill improves repeatability and avoids unexpected side effects. Merely storing a long prompt, or testing only the happy path with the author coaching it, is insufficient.

## Chapter 8 — Least-privilege connection decision

**Primary competencies:** C6
**Reinforced competencies:** C3, C8
**Task:** Compare an MCP server, a CLI or API, and a manual/export approach for one workflow. Safely test the chosen approach or produce an executable test plan.

=== "No-code lane"

    Use a synthetic calendar, public web data, a disposable file set, or a read-only export. A paper threat model plus recorded mock approval flow is valid.

=== "Engineer lane"

    Use a local fixture, test account, read-only token, or mocked service. Pin and inspect third-party dependencies where practical.

**Required evidence**

- Data classification and a diagram of data, instruction, credential, and output flow.
- Comparison of capability, source trust, permissions, prompt-injection exposure, cost, and operational burden.
- Least-privilege permissions, secret handling, approval gates, logging, and revocation plan.
- Synthetic or read-only test with an attempted disallowed action.
- Accept, modify, or decline decision plus the evidence that would trigger reevaluation.

**Evidence standard:** A capable decision treats read-only as an integrity control, not a confidentiality guarantee, and considers a simpler alternative. “It is popular” or “the agent asked permission” is insufficient.

## Chapter 9 — Guardrail that proves itself

**Primary competencies:** C7
**Reinforced competencies:** C3, C4, C6
**Task:** Replace one remembered quality or safety rule with an automatic mechanism, then prove both pass and fail behavior.

=== "No-code lane"

    Use a link checker, accessibility checker, schema or required-field validator, naming check, spreadsheet validation, or an approval gate. A local script generated with assistance is acceptable if you can run and interpret it.

=== "Engineer lane"

    Use a test, formatter, linter, policy, hook, CI job, or permission configuration appropriate to a disposable repository.

**Required evidence**

- The failure the control targets, its consequence, and when the control runs.
- Current product documentation checked for event names or settings.
- A known-good fixture and a safely seeded bad fixture.
- Output showing pass, fail, and corrected pass.
- Bypass and limitation analysis, including why the mechanism is not a complete security boundary.

**Evidence standard:** A capable mechanism deterministically catches the seeded failure and fails clearly enough to act on. A configuration screenshot without execution evidence is insufficient.

## Chapter 10 — Parallel only when justified

**Primary competencies:** C7
**Reinforced competencies:** C2, C3, C4
**Task:** Plan and run a two-lane agent or human-plus-agent workflow, or demonstrate through dependency analysis that sequential work is the better design.

=== "No-code lane"

    Split a small launch pack, research package, or content system into independent artifacts with an integration review. Use separate folders or documents and synthetic/public data.

=== "Engineer lane"

    Use separate Git worktrees or equivalent isolated branches for two bounded changes. Inventory shared ports, databases, caches, credentials, generated files, and memory.

**Required evidence**

- Dependency graph and parallelism decision.
- Brief for each lane: ownership, allowed files or surfaces, inputs, output contract, done-means, and stop conditions.
- Isolation plan for tracked work and shared resources.
- Integration order, conflict handling, validation, and final human review.
- Comparison with a single-agent or sequential approach, including coordination overhead.

**Evidence standard:** A capable run has truly separable ownership and validates the integrated result. More simultaneous agents is not evidence of better orchestration.

## Chapter 11 — Evidence-backed launch

**Primary competencies:** C8
**Reinforced competencies:** C4, C6, C7
**Task:** Prepare and execute a low-risk launch or private demonstration with an operations and value evidence pack.

=== "No-code lane"

    Deliver a public-safe site, private workflow demonstration, synthetic-data dashboard, or sanitized case study. Use a platform you can operate and export from.

=== "Engineer lane"

    Deploy a small tested service or demonstrate it in a private environment. Include monitoring and a recovery or roll-forward exercise proportional to the stakes.

**Required evidence**

- Delivery decision, audience, public/private classification, authorization, and data/provider handling.
- Accessibility and representative-use checks; provenance, disclosure, correction or escalation, and abuse analysis.
- Current platform terms, actual usage and cost evidence, budget threshold, ownership, monitoring, and handoff.
- A safe recovery or roll-forward demonstration and one external acceptance pass.
- A value statement separating observed result, assumption, and future hypothesis; no guaranteed income, savings, accuracy, or career outcome.

**Evidence standard:** A capable launch is reviewable by its intended user, supportable after handoff, and honest about evidence and limits. A live URL by itself is insufficient.

## Chapter 12 — Certification readiness with evidence

**Primary competencies:** C1, C4, C6, C8
**Reinforced competencies:** C2, C5, C7
**Task:** Build a certification readiness and evidence pack using the Chapter 12 lab. Translate the current provider blueprint and companion-video timestamps into a study matrix, complete or simulate the Community Workshop Digest lab, defend three architecture scenarios, and record what is certified, completed, evidenced, simulated, or unknown.

=== "No-code lane"

    Use the supplied synthetic fixtures, architecture cards, decision tables, and recorded explanations. You do not need a paid account, live SDK, MCP server, or exam appointment. Your evidence must still show the data boundary, tool choice, failure path, and reviewer disposition.

=== "Engineer lane"

    Use a disposable repository with synthetic data. Run the deterministic fixture/evaluator path before adding any model or SDK integration. If you use the Agent SDK or MCP, record the current documentation, package/runtime versions, permissions, and what you actually executed.

**Required evidence**

- A dated certification readiness brief with the official source checked for access, format, cost, accommodations, and renewal questions.
- A domain study matrix with video timestamps, current primary references, performance verbs, labs, evidence of done, confidence, and review dates.
- A lab evidence pack with vision, context, tool/trust decisions, evaluation set, seeded failure, correction, and independent review.
- Three scenario defenses, including one case where the strongest answer is to decline, narrow, or escalate automation.
- A claim ledger that distinguishes provider-issued certification, course completion, project evidence, live execution, simulation, delegation, and unknowns.
- One workshop or video-lesson outline with timestamp, source date, learner objective, lab, failure drill, accessibility support, and current-doc recheck note.

**Evidence standard:** A capable submission uses the certification as a learning target without calling the course a credential, makes no unsupported eligibility or career claim, chooses the narrowest justified capability, catches a seeded failure, and leaves another person enough evidence to reproduce or challenge the decision. A polished study schedule with no lab or a passing-looking transcript with no independent check is insufficient.

## Chapter score sheet

Use one copy for every chapter.

| Dimension | Score, 0–3 | Evidence link or timestamp |
| --- | ---: | --- |
| Judgment and framing |  |  |
| Execution and artifact |  |  |
| Verification and safety |  |  |
| Reflection and transfer |  |  |
| **Total / 12** |  |  |

Record:

- **Failed check or feedback:**
- **Revision made:**
- **What I can now do without coaching:**
- **What still requires a reference or reviewer:**
- **Worked patterns viewed before first attempt:** yes / no / unsure
- **Primary competency evidence recorded:**
- **Reinforced competency evidence recorded, if directly observed:**
