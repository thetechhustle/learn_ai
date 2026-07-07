# Setup

Everything you need to run the labs in this course, in about 30 minutes. Do this before Chapter 3. If a step fails, don't push through blind — the [Glossary](glossary.md) and the troubleshooting notes below cover the common snags.

## What you're setting up

1. A **terminal** you're comfortable opening.
2. **Node.js** (the runtime Claude Code ships on).
3. **Git** and a free **GitHub** account (your safety net and your portfolio).
4. **Claude Code** and a Claude account.
5. A dedicated **projects folder** so agent work never touches your personal files.

## 1. Open your terminal

=== "🌱 No-code lane"

    **Mac:** Press ++cmd+space++, type `Terminal`, press ++enter++. That window is your new office.

    **Windows:** Install [Windows Terminal](https://aka.ms/terminal) from the Microsoft Store, then install WSL by opening it and running `wsl --install`. Restart when asked. The course assumes the Linux (WSL) environment on Windows — it's the industry default and everything in the lessons will match.

    Type this and press ++enter++ to prove you're alive:

    ```console
    $ echo "I'm here"
    ```

    If the terminal repeats it back, you're in business.

=== "⚙️ Engineer lane"

    Use whatever you already run — iTerm2, Ghostty, Windows Terminal + WSL2, or a native Linux shell. Claude Code works best in a real terminal rather than an IDE-embedded one for the first sessions, so you see exactly what it does.

## 2. Install Node.js

=== "🌱 No-code lane"

    Download the **LTS** installer from [nodejs.org](https://nodejs.org) and run it like any other app. Then confirm in your terminal:

    ```console
    $ node --version
    ```

    Any version 18 or higher is fine.

=== "⚙️ Engineer lane"

    Use your version manager of choice:

    ```console
    $ fnm install --lts   # or: nvm install --lts / mise use -g node@lts
    $ node --version
    ```

## 3. Install Git and create a GitHub account

Git is the undo button for everything you'll build. Non-negotiable, both lanes.

```console
$ git --version
```

If that fails: on Mac, run `xcode-select --install`; on WSL/Linux, run `sudo apt install git`.

Then create a free account at [github.com](https://github.com) and set your identity:

```console
$ git config --global user.name "Your Name"
$ git config --global user.email "you@example.com"
```

!!! example "Watch: Git in one sitting"
    New to Git? Watch freeCodeCamp's [Git and GitHub for Beginners — Crash Course](https://www.youtube.com/watch?v=RGOj5yH7evk) (1 hr). You don't need all of it yet — the first 30 minutes covers everything Chapter 3 uses.

## 4. Install Claude Code

```console
$ npm install -g @anthropic-ai/claude-code
```

Then start it once to log in:

```console
$ claude
```

Follow the login prompt in your browser. When you see the Claude Code prompt in your terminal, you're connected. Type `/exit` to leave.

Official install docs, including native installers: [code.claude.com/docs](https://code.claude.com/docs/en/overview).

!!! warning "Plans and cost"
    Claude Code runs on your Claude subscription or API credits. Start with a Pro plan or a small API budget and watch usage with `/cost` during sessions. Chapter 11 covers cost strategy properly — until then, small sessions, small projects.

## 5. Create your projects folder

Give every agent session a home that is **not** your Desktop, Documents, or anything precious:

```console
$ mkdir -p ~/builds
$ cd ~/builds
```

Every lab in this course starts from `~/builds`. Agents act on real files — a dedicated folder plus Git means every experiment is reversible.

## Verify the full setup

Run each line. Every one should answer without an error:

```console
$ node --version
$ git --version
$ claude --version
$ ls ~/builds
```

All green? You're ready. Head to [Chapter 1](../lessons/01_the_shift/README.md) if you haven't read it, or straight to [Chapter 3](../lessons/03_command_center/README.md) to put the setup to work.

## Troubleshooting

- **`command not found: claude`** — your npm global bin isn't on PATH. Run `npm config get prefix`; add its `bin` folder to your shell profile, or reinstall Node via the LTS installer which wires this up for you.
- **Windows without WSL** — Claude Code supports native Windows, but lessons show Unix-style commands. WSL keeps you on the happy path.
- **Corporate machine** — if installs are blocked, use a personal machine. You need an environment you're allowed to experiment in.
