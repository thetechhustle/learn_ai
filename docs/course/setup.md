# Setup

Everything you need to run the labs in this course, usually in 45–60 minutes. Account, operating-system, or corporate controls can take longer. Do this before Chapter 3. If a step fails, don't push through blind — use the linked official guidance and troubleshooting notes.

## What you're setting up

1. A **terminal** you're comfortable opening.
2. **Claude Code** and an account that includes access.
3. **Git** and a free **GitHub** account (one layer of your safety net and portfolio).
4. **Node.js LTS** for the `npx`-based MCP labs in Chapter 8.
5. A dedicated **projects folder** so agent work stays away from personal files.

## 1. Open your terminal

=== "🌱 No-code lane"

    **Mac:** Press ++cmd+space++, type `Terminal`, press ++enter++. That window is your new office.

    **Windows:** Open PowerShell or Windows Terminal. Claude Code supports native Windows, so WSL is optional. Use WSL 2 if you want a Linux toolchain or Claude Code's Bash sandbox; native Windows is the simpler start for Windows-native projects.

    Type this and press ++enter++ to prove you're alive:

    ```console
    $ echo "I'm here"
    ```

    If the terminal repeats it back, you're in business.

=== "⚙️ Engineer lane"

    Use whatever you already run — iTerm2, Ghostty, PowerShell, Windows Terminal + WSL2, or a Linux shell. A standalone terminal makes the first sessions easier to follow, but native Windows and IDE integrations are supported.

## 2. Install Claude Code

The [official setup guide](https://code.claude.com/docs/en/setup) recommends the native installer. Claude Code runs as a native binary; Node.js is not its runtime or a prerequisite for this installation.

=== "Mac, Linux, or WSL"

    ```console
    $ curl -fsSL https://claude.ai/install.sh | bash
    ```

=== "Windows PowerShell"

    ```powershell
    irm https://claude.ai/install.ps1 | iex
    ```

=== "Windows CMD"

    ```bat
    curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
    ```

Then verify the installation:

```console
$ claude --version
$ claude doctor
```

!!! note "npm is an alternative"
    If you manage tools through npm, `npm install -g @anthropic-ai/claude-code` is still supported, but the current package requires **Node.js 22 or later**. The installed Claude Code binary does not use Node at runtime. Do not use `sudo npm install -g`.

Start Claude Code once to log in:

```console
$ claude
```

Follow the browser prompt. Claude Code requires a Pro, Max, Team, Enterprise, or Console account; the free Claude.ai plan does not include Claude Code. Type `/exit` after you connect.

## 3. Install Node.js for Chapter 8

Chapter 8 uses `npx` to run some MCP servers, so install the current **Node.js LTS** release from [nodejs.org](https://nodejs.org). It is a lab dependency, not Claude Code's runtime.

```console
$ node --version
$ npx --version
```

If you use a version manager, `fnm install --lts`, `nvm install --lts`, or the equivalent is fine.

## 4. Install Git and create a GitHub account

Git gives tracked project files recoverable checkpoints. It does not back up untracked or ignored files, undo changes in databases or remote services, or replace a real backup.

```console
$ git --version
```

If that fails: on Mac, run `xcode-select --install`; on WSL/Linux, run `sudo apt install git`.

Then create a free account at [github.com](https://github.com) and set your identity:

```console
$ git config --global user.name "Your Name"
$ git config --global user.email "you@example.com"
```

Authenticate before the first push. The GitHub CLI is the course's later workflow, so install it from the [official `gh` instructions](https://cli.github.com/) and run:

```console
$ gh auth login
$ gh auth status
```

Choose HTTPS and follow the browser flow. If you cannot use `gh`, use GitHub's official HTTPS credential-manager or SSH-key guidance; do not put a personal access token directly in a remote URL or project file.

!!! example "Watch: Git in one sitting"
    New to Git? Watch freeCodeCamp's [Git and GitHub for Beginners — Crash Course](https://www.youtube.com/watch?v=RGOj5yH7evk) (1 hr). You don't need all of it yet — the first 30 minutes covers everything Chapter 3 uses.

!!! warning "Plans and cost"
    Claude Code runs through an eligible subscription or API-backed Console account. Use `/usage` to watch plan allowance or API token use. Subscription users see plan usage, not a billable per-session charge. API dollar figures are local estimates; the [Claude Console usage page](https://console.anthropic.com/settings/usage) is authoritative for billing. Chapter 11 covers budgeting in detail.

## 5. Create your projects folder

Give every agent session a home that is **not** your Desktop, Documents, or anything precious:

```console
$ mkdir -p ~/builds
$ cd ~/builds
```

Every lab in this course starts from `~/builds`. A dedicated folder plus Git narrows the workspace and checkpoints tracked files; it does not make external actions or untracked/ignored state automatically reversible.

## Verify the full setup

Run each line. Every one should answer without an error:

```console
$ node --version
$ npx --version
$ git --version
$ gh auth status
$ claude --version
$ ls ~/builds
```

All green? You're ready. Head to [Chapter 1](../lessons/01_the_shift/README.md) if you haven't read it, or straight to [Chapter 3](../lessons/03_command_center/README.md) to put the setup to work.

## Troubleshooting

- **`command not found: claude`** — run `claude doctor` if available, then use the [official install troubleshooting guide](https://code.claude.com/docs/en/setup). For an npm installation, confirm Node 22+ and that npm's global bin directory is on `PATH`.
- **Native Windows command differences** — the course examples use Unix-style commands. Git for Windows adds Git Bash; WSL 2 provides a fuller Linux environment and supports Bash sandboxing. Native PowerShell remains supported.
- **Corporate machine** — if installs are blocked, use a personal machine. You need an environment you're allowed to experiment in.
