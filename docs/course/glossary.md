# Glossary

Use this glossary as a quick lookup while working through the lessons. Definitions favor plain language and practical use over academic precision. If a term in a lesson isn't clear from context, look it up here — vocabulary should never be the reason you stop.

---

**Access token**: A secret credential that lets software act on an account. A broad token grants many permissions or reaches a large scope of data.

**Agent**: An AI system that doesn't just answer — it acts. It can read files, run commands, use tools, check its own work, and keep going until the job is done or it needs you.

**Agentic engineering**: The practice of building with and around AI agents: designing their context, tools, guardrails, and workflows so they produce reliable work.

**Agentic loop**: The cycle an agent runs on every task — gather context, take action, verify the result — repeated until done. The core mental model of this course.

**API (Application Programming Interface)**: A way for programs to talk to each other. When Claude Code calls a weather service or your database, it's using an API.

**API key**: A secret password that identifies your account to a service. Treat it like a debit card number: never paste it into files you share or commit to Git.

**Artifact**: A concrete piece of work used as evidence, such as a file, screenshot, recording, test result, decision log, or deployed page.

**Authorization**: Permission from the person or organization responsible for data or a system. Access alone does not prove authorization.

**CLAUDE.md**: A file in your project that Claude Code reads at the start of every session. Your project's standing orders: what this project is, how it's organized, what the rules are.

**CLI (Command-Line Interface)**: A program you run by typing its name in the terminal, like `git` or `claude`. Agents can use CLIs as tools.

**Claude Code**: Anthropic's terminal-based AI coding agent, and the primary tool of this course. You describe outcomes; it plans, edits files, runs commands, and verifies.

**Commit**: A saved snapshot of tracked project files in Git, with a message describing what changed. It provides a comparison and recovery point within Git's documented boundary.

**Context**: Everything the model can currently see: your instructions, files it read, conversation history, memory files. Quality of context determines quality of output.

**Context engineering**: Deliberately shaping what the agent sees — briefs, CLAUDE.md, memory, examples, scoped tasks — so it performs at its best. The successor to "prompt engineering."

**Context window**: The maximum input/output budget for a model interaction, measured in tokens. Material can be summarized or dropped as it fills, and fitting does not guarantee perfect attention.

**Data classification**: A label for how sensitive data is and what handling rules apply to it.

**Data minimization**: Using, sharing, and retaining only the data necessary for a specific task.

**Deploy**: Delivering a project to an environment where its intended users or reviewers can access it. The surface may be public, private, authenticated, local, or recorded; platform terms and costs must be checked when chosen.

**Diff**: A view of exactly what changed between two versions of a file — lines added, lines removed. Reading diffs is how you review an agent's work.

**Fixture**: A known input or saved setup used to run a repeatable test.

**Git**: Version-control software that records snapshots of tracked files when you commit. It can restore committed content, but it does not recover every uncommitted or untracked file, undo external actions, or replace backups and service-specific recovery.

**GitHub**: A service that hosts Git repositories. It can hold a private or public remote copy of pushed commits and is where this course repository lives.

**Hallucination**: When a model states something false with full confidence. Not lying — predicting plausibly. The reason "verify" is a permanent step in the loop.

**Harness**: The environment around an agent — its tools, permissions, memory, and validation. A good harness is why the same model performs brilliantly in one setup and poorly in another.

**Hook**: An automatic action that fires at specific moments in an agent session — for example, running your tests after every file edit. Guardrails that don't depend on anyone remembering.

**Least privilege**: Giving a person or tool only the access needed for the current task, for only as long as it is needed.

**LLM (Large Language Model)**: The engine under every modern AI assistant. A neural network trained on enormous amounts of text to predict what comes next — which turns out to be enough to write, reason, and code.

**MCP (Model Context Protocol)**: An open standard that connects agents to outside tools and data — databases, browsers, design tools, your company's systems. Think USB-C for AI.

**MCP server**: A program that offers tools to an agent over MCP. Install a Postgres MCP server and your agent can query your database.

**Memory**: Files an agent keeps across sessions so it doesn't start from zero every time — project facts, your preferences, past decisions.

**Model**: A specific trained AI, like Claude Sonnet or Claude Opus. Different models trade off speed, cost, and capability.

**Monitoring**: Repeatedly observing a system after release so failures, misuse, cost changes, and unexpected behavior can be detected.

**Multi-agent orchestration**: Running several agents on one goal — splitting work, working in parallel, reviewing each other — with you as the director.

**Plan mode**: A Claude Code mode where the agent proposes an approach for your approval before touching anything. Think first, build second.

**Prompt**: What you say to a model. In agentic work, the prompt is just one ingredient — context, tools, and guardrails do the heavy lifting.

**Prompt injection**: Instructions hidden or embedded in content that try to make an AI system ignore its intended task or misuse its tools.

**Provenance**: A record of where information or an artifact came from and how it was produced or changed.

**Provider handling**: How an AI or cloud provider sends, stores, retains, reviews, and uses the data submitted to its service.

**Recourse**: A way for an affected person to question, correct, appeal, or obtain human review of a system's output or decision.

**Regression**: A behavior that used to work but breaks after a change.

**Repository (repo)**: A project folder tracked by Git. Everything in this course lives in repos.

**Revocation**: Removing access that was previously granted, such as disabling a credential or disconnecting a tool.

**Roll-forward**: Recovering by making and deploying a new corrective change instead of restoring an older version.

**Rubric**: A scoring guide that names the criteria and evidence used to judge work.

**Sandbox**: An enforced environment that limits which files, processes, networks, or other resources a program can reach. A project folder by itself is not a sandbox.

**Schema**: A description of a data structure: its fields, types, relationships, and rules.

**Second brain**: A structured set of notes and docs your agent can read — decisions, research, style guides — so its context survives beyond any single session.

**Skill**: A reusable instruction package that teaches Claude Code a specific capability or your specific way of doing something. Write once, invoke forever.

**Slash command**: A quick command inside a Claude Code session starting with `/`, like `/clear`, `/usage`, or a compatible custom command you create.

**Subagent**: An agent your main agent spawns to handle a piece of work in its own context — research, review, a parallel task — reporting back when done.

**Synthetic data**: Artificial examples created to resemble a useful pattern without containing real people's or organizations' confidential information.

**Terminal**: The text-based app where you type commands and run Claude Code. Less scary than it looks; Chapter 3 makes it home.

**Token**: The unit models read and write — roughly three-quarters of a word. Context windows and costs are measured in tokens.

**Vibe coding**: Building by describing outcomes in plain language and letting the agent write the code. Powerful, and safe exactly in proportion to how well you verify.

**Worktree**: A Git feature that gives you multiple working copies of one repository — the trick that lets several agents build different things in the same project at the same time.
