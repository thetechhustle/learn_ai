# Glossary

Use this glossary as a quick lookup while working through the lessons. Definitions favor plain language and practical use over academic precision. If a term in a lesson isn't clear from context, look it up here — vocabulary should never be the reason you stop.

---

**Agent**: An AI system that doesn't just answer — it acts. It can read files, run commands, use tools, check its own work, and keep going until the job is done or it needs you.

**Agentic engineering**: The practice of building with and around AI agents: designing their context, tools, guardrails, and workflows so they produce reliable work.

**Agentic loop**: The cycle an agent runs on every task — gather context, take action, verify the result — repeated until done. The core mental model of this course.

**API (Application Programming Interface)**: A way for programs to talk to each other. When Claude Code calls a weather service or your database, it's using an API.

**API key**: A secret password that identifies your account to a service. Treat it like a debit card number: never paste it into files you share or commit to Git.

**CLAUDE.md**: A file in your project that Claude Code reads at the start of every session. Your project's standing orders: what this project is, how it's organized, what the rules are.

**CLI (Command-Line Interface)**: A program you run by typing its name in the terminal, like `git` or `claude`. Agents can use CLIs as tools.

**Claude Code**: Anthropic's terminal-based AI coding agent, and the primary tool of this course. You describe outcomes; it plans, edits files, runs commands, and verifies.

**Commit**: A saved snapshot of your project in Git, with a message describing what changed. Your undo button and your receipts.

**Context**: Everything the model can currently see: your instructions, files it read, conversation history, memory files. Quality of context determines quality of output.

**Context engineering**: Deliberately shaping what the agent sees — briefs, CLAUDE.md, memory, examples, scoped tasks — so it performs at its best. The successor to "prompt engineering."

**Context window**: The maximum input/output budget for a model interaction, measured in tokens. Material can be summarized or dropped as it fills, and fitting does not guarantee perfect attention.

**Deploy**: Putting your project on the public internet so anyone can reach it. GitHub Pages, Vercel, and Netlify make this nearly free.

**Diff**: A view of exactly what changed between two versions of a file — lines added, lines removed. Reading diffs is how you review an agent's work.

**Git**: Version-control software that tracks every change to your project. Lets you experiment fearlessly, because you can always roll back.

**GitHub**: A website that hosts Git repositories. Your backup, your portfolio, and where this course itself lives.

**Hallucination**: When a model states something false with full confidence. Not lying — predicting plausibly. The reason "verify" is a permanent step in the loop.

**Harness**: The environment around an agent — its tools, permissions, memory, and validation. A good harness is why the same model performs brilliantly in one setup and poorly in another.

**Hook**: An automatic action that fires at specific moments in an agent session — for example, running your tests after every file edit. Guardrails that don't depend on anyone remembering.

**LLM (Large Language Model)**: The engine under every modern AI assistant. A neural network trained on enormous amounts of text to predict what comes next — which turns out to be enough to write, reason, and code.

**MCP (Model Context Protocol)**: An open standard that connects agents to outside tools and data — databases, browsers, design tools, your company's systems. Think USB-C for AI.

**MCP server**: A program that offers tools to an agent over MCP. Install a Postgres MCP server and your agent can query your database.

**Memory**: Files an agent keeps across sessions so it doesn't start from zero every time — project facts, your preferences, past decisions.

**Model**: A specific trained AI, like Claude Sonnet or Claude Opus. Different models trade off speed, cost, and capability.

**Multi-agent orchestration**: Running several agents on one goal — splitting work, working in parallel, reviewing each other — with you as the director.

**Plan mode**: A Claude Code mode where the agent proposes an approach for your approval before touching anything. Think first, build second.

**Prompt**: What you say to a model. In agentic work, the prompt is just one ingredient — context, tools, and guardrails do the heavy lifting.

**Repository (repo)**: A project folder tracked by Git. Everything in this course lives in repos.

**Second brain**: A structured set of notes and docs your agent can read — decisions, research, style guides — so its context survives beyond any single session.

**Skill**: A reusable instruction package that teaches Claude Code a specific capability or your specific way of doing something. Write once, invoke forever.

**Slash command**: A quick command inside a Claude Code session starting with `/`, like `/clear`, `/usage`, or a compatible custom command you create.

**Subagent**: An agent your main agent spawns to handle a piece of work in its own context — research, review, a parallel task — reporting back when done.

**Terminal**: The text-based app where you type commands and run Claude Code. Less scary than it looks; Chapter 3 makes it home.

**Token**: The unit models read and write — roughly three-quarters of a word. Context windows and costs are measured in tokens.

**Vibe coding**: Building by describing outcomes in plain language and letting the agent write the code. Powerful, and safe exactly in proportion to how well you verify.

**Worktree**: A Git feature that gives you multiple working copies of one repository — the trick that lets several agents build different things in the same project at the same time.
