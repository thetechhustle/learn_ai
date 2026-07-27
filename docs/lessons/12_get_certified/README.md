# Chapter 12: Get Certified — Turn Agentic Skill into Defensible Proof

You have learned how agents work, how to give them context and tools, how to
verify their work, and how to ship responsibly. This chapter answers the next
question:

> How do I turn that practice into a certification plan, a body of evidence, and
> a workshop someone else can actually use?

This is not a promise that a certificate guarantees a job, a client, or a salary.
It is a repeatable way to prepare for a technical certification while building
the judgment that the exam, a hiring manager, a client, or a teammate can inspect.
The credential is one signal. Your lab evidence, design decisions, failure
analysis, and ability to explain tradeoffs are the receipt.

!!! abstract "What you will learn"
    - Separate course completion, certification, project evidence, and job readiness.
    - Read a certification outline as a set of performance demands instead of a list of vocabulary.
    - Build and explain an agent loop using an SDK, tools, context, and verification.
    - Make least-privilege decisions around MCP, permissions, data, and external effects.
    - Produce a certification lab evidence pack with a failed path and a reviewable correction.
    - Defend architecture choices in scenario form and turn the material into a workshop or video lesson.

!!! success "Builder principle"
    A certification plan is strongest when every study block leaves evidence: a decision,
    a working or simulated lab, a failure you caught, or an explanation you can give
    without reading the answer back.

## The certification this chapter uses as a case study

The companion course is built around Anthropic's **Claude Certified Architect —
Foundations**, commonly abbreviated CCA-F. Anthropic announced the certification
for Claude Partner Network partners on March 12, 2026. Access, exam delivery,
eligibility, scoring, and availability can change, so treat provider documentation
as authoritative at the moment you schedule an exam.

The linked video reports the following exam shape at the time it was recorded:

| Video-reported detail | How to use it in this course |
| --- | --- |
| Five broad domains: agentic architecture and orchestration; tool design and MCP; Claude Code configuration and workflows; prompt engineering and structured output; context management and reliability | Build a study matrix and attach a lab or explanation to every domain. |
| 60 multiple-choice questions | Practice reading long scenarios for the decision being tested, not memorizing isolated terms. |
| 720/1000 passing score | Use the score as a planning target only; confirm the current exam page before relying on it. |
| About two hours of exam time | Practice deliberate reading and elimination, but do not turn study into speed typing. |
| Hands-on implementation is emphasized | Run or simulate the systems. A fluent explanation is not proof that you can operate the design. |

These are **video-reported facts**, not permanent guarantees. The video also says
the certification was initially limited to the Claude Partner Network. Anthropic's
current partner and academy pages must be checked before a learner pays, applies,
or represents themselves as eligible.

## Watch map for the companion video

Use the published chapter markers as the beginning of each viewing block. The
timestamps are a starting point for a lesson, not a replacement for the written
lab or the current primary documentation.

| Watch block | Video timestamp | Use it for |
| --- | ---: | --- |
| Introduction and exam overview | [00:00:47](https://youtu.be/reDRM0tqhNs?t=47) | Eligibility questions, study posture, domain map, and exam format. |
| SDK environment setup | [00:10:17](https://youtu.be/reDRM0tqhNs?t=617) | Claude Code and Agent SDK setup decisions; separate account access from local setup. |
| Agentic loop foundations | [00:47:36](https://youtu.be/reDRM0tqhNs?t=2856) | Gather, act, verify; tool use; stop reasons; state transitions. |
| Multi-agent orchestration | [01:52:53](https://youtu.be/reDRM0tqhNs?t=6773) | Delegation, roles, coordination, and when one agent is enough. |
| Advanced agent patterns | [04:15:46](https://youtu.be/reDRM0tqhNs?t=15346) | Pattern selection under constraints and failure analysis. |
| Sessions, context, and state | [06:47:52](https://youtu.be/reDRM0tqhNs?t=24472) | Context windows, resumable work, state boundaries, and stale context. |
| Claude Code configuration, permissions, and safety | [07:31:50](https://youtu.be/reDRM0tqhNs?t=27110) | Permission gates, configuration, approvals, and safer defaults. |
| Built-in tooling | [08:58:52](https://youtu.be/reDRM0tqhNs?t=32332) | Tool capability, tool choice, and observable tool behavior. |
| Reliability, evaluation, and output quality | [09:39:03](https://youtu.be/reDRM0tqhNs?t=34743) | False positives, evaluation design, and quality beyond “it ran.” |
| Scaling and real-world constraints | [10:43:59](https://youtu.be/reDRM0tqhNs?t=38639) | Context, cost, latency, reliability, and operational tradeoffs. |
| MCP ecosystem integration | [11:29:51](https://youtu.be/reDRM0tqhNs?t=41391) | MCP clients, servers, tools, resources, trust, and integration choices. |
| Claude Code in CI/CD automation | [11:41:19](https://youtu.be/reDRM0tqhNs?t=42079) | Automation boundaries, review gates, and machine-assisted delivery. |
| Scenario-based architect patterns | [12:14:57](https://youtu.be/reDRM0tqhNs?t=44097) | Final synthesis: choose, explain, verify, and defend an architecture. |

## The six-lesson path

1. **[12.1 Why Certification Is a Learning System](12.1_why_certification_is_a_learning_system.md)** — choose a credential for a reason and define evidence before studying.
2. **[12.2 Read the Blueprint and Build a Study Plan](12.2_read_the_blueprint_and_build_a_study_plan.md)** — turn domains and performance verbs into a practical schedule.
3. **[12.3 Build the Core: Agent Loops, SDKs, and Tools](12.3_build_the_core_agent_loops_sdks_and_tools.md)** — practice the mechanics behind the scenario questions.
4. **[12.4 Architect Trust: MCP, Context, Permissions, and Safety](12.4_architect_trust_mcp_context_permissions_and_safety.md)** — make the security and reliability tradeoffs visible.
5. **[12.5 The Certification Lab: Build the Evidence Pack](12.5_the_certification_lab_build_the_evidence_pack.md)** — complete an end-to-end lab with a seeded failure and a reviewer.
6. **[12.6 Scenario Defense, Workshops, and the Capstone Bridge](12.6_scenario_defense_workshops_and_the_capstone_bridge.md)** — explain choices under pressure and convert the work into teaching and portfolio evidence.

## Routes through the chapter

=== "🌱 No-code lane"

    Use the supplied simulations, decision tables, synthetic task fixtures, and
    recorded explanations. You are practicing architecture judgment and evidence
    quality without being blocked by an account, paid plan, local install, or
    programming language.

=== "⚙️ Engineer lane"

    Run the labs in a disposable repository with synthetic data. Use the current
    Agent SDK and MCP documentation for syntax, pin reviewed dependencies where
    appropriate, and record what you actually executed versus what you simulated.

The lanes are not a ranking. A no-code learner who identifies a trust boundary and
tests a failure path has stronger evidence than an engineer who runs a command but
cannot explain what it proved.

## Chapter checkpoint

Complete the [Chapter 12 checkpoint](../../course/assessment/chapter-checkpoints.md#chapter-12-certification-readiness-with-evidence), then save:

- a certification readiness brief and domain study matrix;
- a timestamped video/source map with access and “verify before scheduling” notes;
- one lab evidence pack with a failed path and corrected path;
- three scenario defenses, including one case where the safest answer is to decline or narrow the automation;
- a claim ledger distinguishing **certified**, **course completed**, **project evidence**, **simulated**, and **unknown**.

No live exam is required for this chapter. Do not describe completion of this
chapter as holding an Anthropic certification.

## References to keep current

- [Anthropic: Claude Partner Network and Claude Certified Architect announcement](https://www.anthropic.com/news/claude-partner-network)
- [Anthropic Claude Code overview](https://docs.anthropic.com/en/docs/claude-code/overview)
- [Anthropic Agent SDK overview](https://docs.anthropic.com/en/docs/claude-code/sdk)
- [Anthropic Agent SDK Python reference](https://docs.anthropic.com/en/docs/claude-code/sdk/sdk-python)
- [Model Context Protocol introduction](https://modelcontextprotocol.io/docs/getting-started/intro)
- [MCP architecture](https://modelcontextprotocol.io/docs/learn/architecture)
- [MCP security best practices](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices)
- [Certification source log](../../course/certification-source-log.md)
- [Companion video: Claude Certified Architect — Foundations](https://www.youtube.com/watch?v=reDRM0tqhNs)

The [course maintenance guide](../../course/maintenance.md) explains how to
recheck moving product behavior, commands, terms, and source records. Revisit this
chapter before a new cohort or workshop run.
