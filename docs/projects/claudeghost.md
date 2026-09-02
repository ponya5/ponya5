[← Back to profile](../../README.md)

# ClaudeGhost

![Repo](https://img.shields.io/badge/Repo-Public-brightgreen?style=for-the-badge&logo=github)
[![View on GitHub](https://img.shields.io/badge/View%20on%20GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ponya5/ClaudeGhost)

**Headless Supervisor for the Anthropic Claude CLI — run Claude Code autonomously while staying in control via Telegram.**

<a href="../../assets/claudeghost-demo.gif"><img src="../../assets/claudeghost-demo.gif" width="100%" /></a>

## Overview

Running an AI coding agent unattended is risky if it can execute anything without oversight, but babysitting every command defeats the point of autonomy. ClaudeGhost wraps the `claude` CLI in a supervised shell: it classifies every command by risk, auto-approves what's safe for your configured autonomy level, and escalates anything risky to your phone for a one-tap approve/block via the Telegram Bot API — free, unlimited, and instant.

## Goals

- Let Claude Code run autonomously on real tasks without requiring you to sit at the terminal.
- Give you a tunable trust dial (5 autonomy levels) instead of an all-or-nothing choice between "ask everything" and "full auto."
- Keep a full audit trail of every session — files modified, commands executed, cost, duration — without cluttering chat with long messages.

## Key Features

- **AFK Autonomy Levels (1–5)** — from Paranoid (asks everything) to God Mode (full auto), with Read-Only/Write/Execute tiers in between.
- **Telegram Bot API approvals** — approve, block, redirect with an alternative instruction, or kill the process, all from your phone.
- **Risk classification** — every command is categorized as Read-Only, Write, Execute, or Critical before it runs.
- **Budget control** — set a spending limit; the session pauses automatically if it's exceeded.
- **Session loop** — run multiple tasks back-to-back without restarting the tool.
- **Changelog tracking** — every session writes a detailed log (files modified, commands run, cost, duration) with a short Telegram summary linking to the full log.
- **Live Rich terminal dashboard** and stall detection for when the CLI hangs.
- **Auto-update checker** — compares your local repo against the remote on startup, no GitHub Releases required.

## Potential Use Cases

- Developers who want to kick off a Claude Code task and step away, checking in only when something risky needs a decision.
- Teams running longer autonomous coding sessions overnight or during meetings, with Telegram as the only interruption channel.
- Anyone who wants graduated trust in an AI coding agent instead of binary "supervised" vs "fully autonomous" modes.

## How to Use

```bash
git clone https://github.com/ponya5/ClaudeGhost.git
cd ClaudeGhost
pip install -r requirements.txt

python setup_interactive.py     # sets up your Telegram bot
python -m src.cli config test   # verify the connection

python claudeghost.py "Create a hello world app" --level 3
```

You'll get a Telegram notification whenever approval is needed. Reply `A` to approve, `B` to block, `C <text>` to redirect, or `D` to kill the process.

## Tech Stack

Python 3.10+, PTY/subprocess wrapping around the Claude CLI, Telegram Bot API, Rich for the terminal dashboard, and pydantic for config.

---

⭐ [Star the repo](https://github.com/ponya5/ClaudeGhost) if you find it useful.

[← Back to profile](../../README.md)
