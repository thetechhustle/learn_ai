# Answer Key and Evidence Guide

These are reference patterns, not single correct answers. Open-ended work can be
effective in many forms. Score only what the learner’s evidence supports.

Open this page after completing the
[Finish and Save Before Review](review-after-attempt.md) steps. If patterns were
viewed early, disclose that exposure; do not claim an unexposed baseline.

## How to review fairly

1. Read the task, required evidence, and competency anchor before judging polish.
2. Locate evidence. Do not infer a test, safety decision, or user check that is not shown.
3. Score each criterion independently. Cite a file, line, screenshot, output, or timestamp.
4. Treat a justified refusal, manual path, private demo, or sequential workflow as a strong answer when it fits the risk and evidence.
5. Give one observed strength, one unsupported claim, one risk or accessibility concern, and one highest-value revision.
6. Let the learner respond with accept, modify, or decline plus a reason. The reviewer need not agree, but the disposition must be recorded.

Lane, visual production value, English fluency, typing speed, and paid-tool access are not scoring criteria.

## Diagnostic reference patterns

Use the [Competency Framework](competency-framework.md#competencies-and-anchors) for 0–3 levels. The patterns below show what relevant evidence may contain.

### C1 — Behavior and limits

**Strong evidence may include:**

- Output is generated from learned patterns and current context; fluency is not source validation.
- Tool results, retrieved text, and user-provided context can also be incomplete, stale, or malicious.
- The system cannot establish a citation or causal claim without checking authoritative evidence.
- Verification scales from opening cited sources for a low-stakes draft to expert review, independent data, and documented controls for consequential use.
- Claims are calibrated to evidence: “suggests,” “observed in this sample,” or “not established,” as appropriate.

**Insufficient or risky:** “AI lies,” “the temperature was too high,” asking the same model whether it is correct, or presenting hidden chain-of-thought as a reliable causal explanation.

### C2 — Framing and delegation

**Strong evidence may include:** intended user and outcome, supplied sources, scope and constraints, examples, observable acceptance criteria, exclusions, ambiguity questions, and a stop/escalation rule. High-stakes prototypes limit the model’s role and name qualified human oversight.

**Insufficient or risky:** adjectives such as “great” or “professional” standing in for done-means, silent assumptions about users, or automating clinical, legal, financial, employment, or safety decisions before authority and review are established.

### C3 — Safe operation

**Strong evidence may include:** disposable copy or verified backup, isolated directory, review of repository instructions/scripts/hooks/dependencies, secret and data classification, explicit file scope, checkpoint, diff, small trial, recovery demonstration, and careful execution. It distinguishes:

- Git recovery of tracked history from backup recovery of untracked or external state;
- permission prompts from sandbox or operating-system isolation;
- source review from trust in a popular repository; and
- `.gitignore` protection against commits from protection against processes, tools, transcripts, or providers.

**Insufficient or risky:** working on irreplaceable originals, broad approval, running install scripts before inspection, or claiming Git can always undo an action.

### C4 — Builder Loop and verification

**Strong evidence may include:** observable done-means, reviewed plan, exact change review, deterministic checks, realistic behavior tests, independent source checks, human acceptance, failure-path evidence, and a recorded correction loop.

**Insufficient or risky:** agent self-report, a screenshot of one happy path, “tests pass” without relevant coverage, or visual inspection as proof of backend behavior.

### C5 — Context engineering

**Strong evidence may include:** stable purpose, map, conventions, commands/process, and boundaries in project context; task detail in the current brief; durable decisions in a decision record; no secrets; removal of contradictions and stale plans; and a controlled fresh-session comparison.

**Insufficient or risky:** putting everything in one growing file, storing credentials or client data, judging improvement from vibes, or assuming persistence is accurate memory.

### C6 — Tool and trust judgment

**Strong evidence may include:** data-flow map, source and maintainer review, pinned or reviewed version, narrow credentials, read-only or synthetic pilot, explicit approval for external writes, output/log review, prompt-injection analysis, revocation, and manual or export fallback.

**Insufficient or risky:** equating read-only with confidential, putting secrets in prompts or committed files, approving every action, or choosing a connection only because it is easy.

### C7 — Mechanisms and orchestration

**Strong evidence may include:** a deterministic control tied to a failure, known-good and known-bad fixtures, pass/fail/corrected-pass output, scoped work ownership, dependency and shared-resource map, integration checks, and a reasoned choice between parallel and sequential work.

**Insufficient or risky:** a checklist relabeled as automation, a validator never observed failing, overlapping ownership, or assuming worktrees isolate databases, ports, caches, credentials, or untracked files.

### C8 — Responsible shipping

**Strong evidence may include:** authorization, data minimization and provider terms, private or synthetic delivery where needed, provenance, representative and accessible testing, material AI disclosure, human correction or appeal, misuse controls, monitoring, recovery, cost evidence, handoff, and calibrated value claims.

**Insufficient or risky:** public exposure as proof of shipping, publishing personal data, claiming error elimination, treating a free tier as permanent, or promising savings or income without measured evidence.

The public [Scoring Guide](scoring-guide.md) contains the universal checkpoint
rubric, score interpretation, and safety gate.

## Chapter answer and evidence patterns

Use these to resolve scoring questions. They do not replace the requirements in [Chapter Checkpoints](chapter-checkpoints.md).

### Chapter 1

- **Credible pattern:** a narrow user problem, a tool-mediated action loop, an observable seven-day test, and claims labeled by evidence status.
- **Valid variation:** choosing not to use an agent because a template or manual process is simpler.
- **Common miss:** repeating anecdotes, market numbers, or income claims without a primary source and date.

### Chapter 2

- **Credible pattern:** the low-stakes path checks source support; the higher-stakes path adds qualified review, representative evaluation, logging, and limits or refusal.
- **Valid variation:** selecting a smaller or cheaper model after the task is narrowed and evaluation shows it is adequate.
- **Common miss:** more detailed prompting presented as a substitute for verification.

### Chapter 3

- **Credible pattern:** disposable scope, inspected configuration, explicit checkpoint, exact diff, safe seeded change, and observed restore.
- **Valid variation:** file copies plus a graphical version-history interface when Git is not yet accessible.
- **Common miss:** a successful final file with no proof of initial state or recovery.

### Chapter 4

- **Credible pattern:** acceptance criteria map directly to checks; a bad link, missing field, style regression, or failing test is caught and corrected.
- **Valid variation:** a peer introduces the fault so the learner does not know where it is.
- **Common miss:** asking the building agent to provide both the only implementation and the only verdict.

### Chapter 5

- **Credible pattern:** the comparison holds the task mostly constant and records criteria such as rule adherence, unnecessary questions, command accuracy, or boundary violations.
- **Valid variation:** context produces no improvement; a strong analysis identifies why and removes it.
- **Common miss:** assuming a larger context file is a better context file.

### Chapter 6

- **Credible pattern:** two comparable runs, observed baseline, reusable routine, approval before external action, and a narrow statement such as “saved 12 minutes on the second run.”
- **Valid variation:** deciding repetition is too rare or variable to automate, then documenting a reusable checklist instead.
- **Common miss:** projecting two-run results into annual savings or universal productivity.

### Chapter 7

- **Credible pattern:** invocation description matches positive cases, stays inactive on a negative case, handles missing input, and improves after a recorded failure.
- **Valid variation:** a Skill containing only instructions and references because a script would add no value.
- **Common miss:** hiding side effects or relying on an author-specific absolute path.

### Chapter 8

- **Credible pattern:** a read-only export or narrowly scoped credential wins over a broad server, an attempted write is denied, and revocation is documented.
- **Valid variation:** declining all live connections and using a manual handoff.
- **Common miss:** ignoring that retrieved content can carry hostile instructions or sensitive output can leak through logs and model context.

### Chapter 9

- **Credible pattern:** the same mechanism produces a pass, blocks a known violation, then passes after correction; event names and settings are checked against current documentation.
- **Valid variation:** a human approval gate is mechanized for a decision that should not be automated.
- **Common miss:** treating a hook, deny pattern, or permission prompt as an operating-system security boundary.

### Chapter 10

- **Credible pattern:** independent ownership, explicit output contracts, separate mutable resources, and integration tests; measured coordination cost supports the parallelism decision.
- **Valid variation:** a dependency graph shows parallel work would add risk, so the learner runs sequentially.
- **Common miss:** counting agents or terminals instead of evaluating integrated quality.

### Chapter 11

- **Credible pattern:** a public-safe or private delivery, external acceptance, accessibility evidence, current cost/terms evidence, monitoring, recovery test, handoff, and a claim limited to observed results.
- **Valid variation:** a recorded synthetic-data demonstration when public or live deployment would expose people or create unsupported operations burden.
- **Common miss:** a live URL with no ownership, recovery, responsible-use, or evidence-backed value story.

## Peer feedback form

```text
Task and lane:
Evidence reviewed:

Scores:
- Judgment and framing: __ / 3 because ...
- Execution and artifact: __ / 3 because ...
- Verification and safety: __ / 3 because ...
- Reflection and transfer: __ / 3 because ...

Observed strength:
Unsupported claim:
Risk or accessibility concern:
Highest-value revision:
Question I could not resolve from the evidence:
```

The learner adds:

```text
Disposition: accept / modify / decline
Revision or reason:
New evidence:
```
