[← Back to profile](../../README.md)

# Take Your Time (IDE Arcade)

![Repo](https://img.shields.io/badge/Repo-Public-brightgreen?style=for-the-badge&logo=github)
[![View on GitHub](https://img.shields.io/badge/View%20on%20GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ponya5/TakeYourTime_IDE_Arcade)

**A VS Code extension that lets you play arcade games while waiting for AI agents, builds, or long-running tasks to complete.**

<a href="../../assets/takeyourtime-demo.gif"><img src="../../assets/takeyourtime-demo.gif" width="100%" /></a>

## Overview

AI agents, builds, and CI runs create a lot of small dead-air moments — long enough to be annoying, short enough that switching apps feels wasteful. Take Your Time turns that idle time into a quick arcade break, launched right inside a sandboxed VS Code webview tab, without ever blocking or interfering with the task actually running in the background.

## Goals

- Give developers a low-friction way to use unavoidable wait time instead of just staring at a progress bar.
- Keep it completely non-blocking — games run independently and never interfere with the build/agent/task underneath.
- Make it configurable (which game sites, fallback URLs) rather than hardcoding one arcade site.

## Key Features

- **Quick access** via an activity bar icon for instant game launch.
- **Multiple game sites** — switch between OnlineGames.io, CrazyGames, Playpager, and SMB Games (or add your own).
- **Non-blocking gameplay** — runs in a sandboxed webview tab, independent of your actual work.
- **Configurable settings** — primary game URL, fallback URL, custom game site list, and error-reporting toggle.
- **Type-safe configuration** via Zod validation.

## Potential Use Cases

- Developers who spend meaningful chunks of the day waiting on AI agents (Claude Code, Copilot, etc.) or long builds.
- Teams wanting a shared, curated list of game sites configured via workspace settings.
- Anyone who wants a five-minute mental reset without leaving the IDE.

## How to Use

1. Download the `.vsix` from [Releases](https://github.com/ponya5/TakeYourTime_IDE_Arcade/releases), then in VS Code: `Ctrl+Shift+P` → "Install from VSIX..." → select the file → reload.
2. Click the game controller icon (🎮) in the Activity Bar, or run "Take Your Time: Open Game" from the Command Palette.
3. A new editor tab opens with the game site — play while your task finishes in the background.

Configure game sites and fallback URLs under **Settings → Take Your Time**.

## Tech Stack

TypeScript 5.3+, the VS Code Extension API, Node.js 20.x, and Zod for configuration validation.

---

⭐ [Star the repo](https://github.com/ponya5/TakeYourTime_IDE_Arcade) if you find it useful.

[← Back to profile](../../README.md)
