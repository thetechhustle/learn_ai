# Capstone: Ship Something Real

The capstone turns eleven chapters into one receipt. You will take a project from vision to a reviewable deployment or demonstration, selecting the context, tool, guardrail, and orchestration mechanisms the project actually warrants. Treat it like a real product launch: plan first, work in version control, verify everything, review who could be affected, and finish with proof.

## Scenario

Someone in your circle — a friend's business, your side hustle, a community org, or you — needs something real: a website, a tool, an automation, or an app. You're the builder now. Deliver it.

## Operating constraints

- Work inside a fresh Git repository under your `~/builds` folder — never on files you can't afford to lose.
- Commit at every meaningful checkpoint. Your Git history is part of the deliverable.
- Keep a running `BUILD_LOG.md` as you work: decisions, prompts that worked, dead ends, costs.
- Do not put real secrets or API keys in the repository. `.env` and `.gitignore` reduce source-control leakage; they do not prevent exposure to local processes, transcripts, hooks, MCP servers, models, or providers.
- Classify data as public, internal, confidential, or regulated. Confirm authorization and current provider retention/training controls; minimize, redact, or use synthetic demo data. Do not use regulated or client-confidential data without approved organizational controls.
- Set a usage budget before you start and monitor it with `/usage`. Subscription allowance is not a per-session bill; API dollar figures shown locally are estimates, with authoritative billing in the Console.

## Pick your build

Choose one path and keep the scope honest — shipped and small beats ambitious and unfinished:

=== "🌱 No-code lane"

    - A complete website for a real person or business — landing page, about, contact, deployed live.
    - A personal dashboard or tracker (habits, budget, content calendar) you actually use.
    - An automation that saves you real time weekly — research digests, content drafts, file organization.

=== "⚙️ Engineer lane"

    - A full-stack app with tests, CI, and deployment — front to back directed through your agent.
    - An agentic harness for a real codebase: CLAUDE.md, custom Skills, MCP connections, hooks, and validation, with before/after evidence of the difference it makes.
    - A multi-agent workflow that ships a feature in parallel across worktrees, documented end to end.

## Requirements

Whatever you build, the capstone must include:

- A written **vision brief** before any agent session: what you're building, for whom, and what "done" means.
- A **persistent context mechanism** — `CLAUDE.md` or the equivalent in another agent — with evidence you iterated on it.
- A **tool-selection note** covering reusable Skills/workflows, MCP/CLI connections, hooks/guardrails, and agent teams. Use each only when its value exceeds its risk and overhead; a justified decline is valid evidence of judgment.
- At least one **mechanized verification control** appropriate to the project: a test, validator, hook, policy, accessibility check, or equivalent that demonstrably catches a failure.
- A **verification pass** you ran yourself: the thing works, on a device that isn't yours, for a person that isn't you.
- A **reviewable delivery surface**: public deployment for public-safe work; otherwise a private/authenticated deployment, synthetic-data demo, recorded walkthrough, or public marketing shell that exposes no sensitive system or data.
- A **handoff document**: what it is, how it works, how to change it, what you'd do next.

## Responsible-build gate

Answer these in `RESPONSIBLE_BUILD.md` before launch:

1. **Data:** What data is used, who authorized it, how was it minimized, and what do the selected providers retain or use for training?
2. **Rights and provenance:** Where did code, claims, text, and media come from? What license, permission, attribution, or disclosure applies?
3. **People and access:** Who could be excluded or harmed? Test representative cases plus keyboard access, readable contrast, alt text, and an automated accessibility scan where applicable.
4. **Disclosure and recourse:** Where would AI involvement materially affect trust? Who can correct, appeal, or escalate an outcome?
5. **Abuse and failure:** How could the tool be misused, and what limits, monitoring, shutdown, rollback, or roll-forward plan reduces that risk?

## Evidence to capture

1. The vision brief and final persistent-context mechanism.
2. Screenshots or recordings of the working product.
3. Your Git log (`git log --oneline`) showing the build progression.
4. One story of something the agent got wrong — and how your loop caught it.
5. Usage evidence, authoritative billed cost where applicable, your hours, and what you'd budget next time.
6. The tool-selection note, `RESPONSIBLE_BUILD.md`, and one portability reflection: what concept would transfer to another agent, and what implementation detail would need re-verification?

## Self and peer review rubric

Score each row **0 = missing, 1 = partial, 2 = evidenced**. A strong capstone has no zero and explains every score with a link, file, screenshot, recording, or test result.

| Dimension | Evidence the reviewer should inspect |
| --- | --- |
| Problem and scope | Named user, observable done-means, explicit not-today list |
| Context and decisions | Persistent instructions, decision log, meaningful iteration |
| Tool judgment | Mechanisms chosen or declined with value, risk, and portability rationale |
| Verification | Reproducible checks, human acceptance pass, failure caught and corrected |
| Responsible build | Data/consent, provenance, representative and accessible testing, disclosure/recourse, misuse controls |
| Delivery and operations | Appropriate public/private demo, handoff, monitoring/recovery proportional to stakes |
| Reflection | Honest usage, cost, and time evidence plus a specific next improvement |

Ask a peer to run one main path and one failure path without coaching, review the evidence above, and leave: one observed strength, one unsupported claim, one responsible-use concern, and one highest-value next change. The builder responds to each item in `BUILD_LOG.md`; agreement is not required, disposition is.

## Done means done

No central submission is required. The rubric and peer pass turn the capstone into evidence you can inspect, improve, and selectively show a client, employer, or community without exposing sensitive work.

When it is safe to share: publish the public artifact or a sanitized case study. Private delivery is still shipped work.
