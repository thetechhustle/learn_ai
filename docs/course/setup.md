# Setup

Everything you need to run the labs in this course, usually in 45–60 minutes. Account, operating-system, or corporate controls can take longer. Do this before Chapter 3. If a step fails, don't push through blind — use the linked official guidance and troubleshooting notes.

## What you're setting up

1. A **terminal** you're comfortable opening.
2. **Claude Code** and an account that includes access.
3. **Git** and a free **GitHub** account (one layer of your safety net and portfolio).
4. **Node.js LTS** for the `npx`-based MCP labs in Chapter 8.
5. A dedicated **projects folder** so the intended workspace is easy to identify.
6. A local copy of this course and its synthetic starter project.

!!! info "No install or paid access?"
    You can complete the course's [Simulation Path](simulation-path.md) in a
    browser from the supplied artifacts. It requires no Claude account, Git,
    Node.js, or terminal. The simulation is a real analysis and decision-making
    path, but it does not prove that you operated a live agent or integration.

## 1. Open your terminal

=== "🌱 No-code lane"

    **Mac:** Press ++cmd+space++, type `Terminal`, press ++enter++. That window is your new office.

    **Windows:** Open PowerShell or Windows Terminal. Claude Code supports native Windows, so WSL is optional. Use WSL 2 if you want a Linux toolchain or Claude Code's Bash sandbox; native Windows is the simpler start for Windows-native projects.

    Type the command for your terminal and press ++enter++:

    === "Mac, Linux, or WSL"

        ```console
        $ echo "I'm here"
        ```

    === "Windows PowerShell"

        ```powershell
        Write-Output "I'm here"
        ```

    If the terminal repeats it back, it is ready.

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

=== "Mac, Linux, or WSL"

    ```console
    $ mkdir -p ~/builds
    $ cd ~/builds
    ```

=== "Windows PowerShell"

    ```powershell
    New-Item -ItemType Directory -Force -Path (Join-Path $HOME "builds")
    Set-Location (Join-Path $HOME "builds")
    ```

Every lab starts from the `builds` folder in your home directory. A dedicated
folder plus Git narrows the intended workspace and checkpoints tracked files;
the folder is not an operating-system sandbox, and it does not make external
actions or untracked/ignored state automatically reversible.

## 6. Get the course files

Choose **Git clone** if Git works on your machine. Choose **Download ZIP** if
you cannot or do not want to use Git yet. Both routes produce a `learn_ai`
folder inside `builds`.

### Option A: clone with Git

=== "Mac, Linux, or WSL"

    ```console
    $ cd ~/builds
    $ git clone https://github.com/thetechhustle/learn_ai.git
    $ cd learn_ai
    ```

=== "Windows PowerShell"

    ```powershell
    Set-Location (Join-Path $HOME "builds")
    git clone https://github.com/thetechhustle/learn_ai.git
    Set-Location .\learn_ai
    ```

### Option B: download a ZIP

1. Open the [course repository](https://github.com/thetechhustle/learn_ai).
2. Select **Code**, then **Download ZIP**.
3. Use the commands for your operating system:

=== "Mac"

    Safari may expand the download automatically. If
    `~/Downloads/learn_ai-main` exists, run:

    ```console
    $ mv ~/Downloads/learn_ai-main ~/builds/learn_ai
    $ cd ~/builds/learn_ai
    ```

    If the `.zip` is still present, double-click it in Finder first.

=== "Linux or WSL"

    ```console
    $ cd ~/builds
    $ unzip ~/Downloads/learn_ai-main.zip
    $ mv learn_ai-main learn_ai
    $ cd learn_ai
    ```

    In WSL, a browser download may instead be under
    `/mnt/c/Users/YOURNAME/Downloads`; replace the ZIP path accordingly.

=== "Windows PowerShell"

    ```powershell
    Set-Location (Join-Path $HOME "builds")
    Expand-Archive -LiteralPath (Join-Path $HOME "Downloads\learn_ai-main.zip") -DestinationPath . -Force
    Rename-Item -Path .\learn_ai-main -NewName learn_ai
    Set-Location .\learn_ai
    ```

### Prove you are at the repository root

Do not continue until the current folder contains both `mkdocs.yml` and
`starter/verify.js`.

=== "Mac, Linux, or WSL"

    ```console
    $ pwd
    $ ls -l mkdocs.yml starter/verify.js
    $ ls starter
    ```

    The first `ls` command must print both named files.

=== "Windows PowerShell"

    ```powershell
    Get-Location
    Test-Path .\mkdocs.yml
    Test-Path .\starter\verify.js
    Get-ChildItem .\starter -Name
    ```

    Both `Test-Path` commands must print `True`.

For a Git clone, `git rev-parse --show-toplevel` should also print a path ending
in `learn_ai`. A ZIP has no Git history, so use the file checks instead.

### Open the course and starter

If Visual Studio Code is installed, run `code .` at the repository root on any
platform. Otherwise:

=== "Mac"

    ```console
    $ open starter/index.html
    $ nano starter/index.html
    ```

    In `nano`, edit the text, press ++ctrl+o++ then ++enter++ to save, and
    ++ctrl+x++ to exit.

=== "Linux"

    ```console
    $ xdg-open starter/index.html
    $ nano starter/index.html
    ```

    Use ++ctrl+o++, ++enter++, and ++ctrl+x++ to save and exit `nano`.

=== "WSL"

    ```console
    $ explorer.exe starter/index.html
    $ nano starter/index.html
    ```

    Use ++ctrl+o++, ++enter++, and ++ctrl+x++ to save and exit `nano`.

=== "Windows PowerShell"

    ```powershell
    Invoke-Item .\starter\index.html
    Start-Process notepad.exe .\starter\index.html
    ```

The browser should show the synthetic **Build With AI Task Dashboard**. Keep the
editor and browser open, then continue to the [Starter Project](starter-project.md).

## Verify the full setup

Run the block for your operating system. Every installed tool should answer
without an error:

=== "Mac, Linux, or WSL"

    ```console
    $ node --version
    $ npx --version
    $ git --version
    $ gh auth status
    $ claude --version
    $ ls ~/builds/learn_ai/starter
    ```

=== "Windows PowerShell"

    ```powershell
    node --version
    npx --version
    git --version
    gh auth status
    claude --version
    Get-ChildItem (Join-Path $HOME "builds\learn_ai\starter") -Name
    ```

All green? You're ready. If a paid account or install is unavailable, use the
[Simulation Path](simulation-path.md) instead of treating setup as failed. Head
to [Chapter 1](../lessons/01_the_shift/README.md) if you haven't read it, or
straight to [Chapter 3](../lessons/03_command_center/README.md) to put the setup
to work.

## Troubleshooting

- **`command not found: claude`** — run `claude doctor` if available, then use the [official install troubleshooting guide](https://code.claude.com/docs/en/setup). For an npm installation, confirm Node 22+ and that npm's global bin directory is on `PATH`.
- **Native Windows command differences** — use the Windows PowerShell tabs in
  Setup and Chapter 3. They work in Windows PowerShell 5.1 and do not rely on
  Bash chaining. A lesson that requires Bash will say so explicitly; Git Bash
  or WSL 2 are optional, not silent prerequisites.
- **Corporate machine** — do not bypass organizational controls. If installs,
  accounts, or payment are unavailable, complete the
  [Simulation Path](simulation-path.md) with the supplied synthetic artifacts.
