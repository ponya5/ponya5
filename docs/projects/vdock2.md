[← Back to profile](../../README.md)

# VDock2 | Virtual Stream Deck

![Repo](https://img.shields.io/badge/Repo-Private-red?style=for-the-badge&logo=github)
[![Contact Me](https://img.shields.io/badge/Contact%20Me-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/daniel-shalom-13987a1a/)

**A customizable control deck for your computer — buttons, scenes, system actions, widgets, and animated backgrounds in one interface.**

<a href="../../assets/vdock2-demo.gif"><img src="../../assets/vdock2-demo.gif" width="100%" /></a>

## Overview

Dedicated hardware stream decks are expensive and locked to whatever buttons the manufacturer designed. VDock is a software stream deck instead — build your own button grids for launching apps, running hotkeys, controlling volume, switching OBS scenes, monitoring system stats, and more. Use it as a desktop Electron app or straight in the browser, with 26+ animated dashboard backgrounds included.

## Goals

- Give people the stream-deck workflow (one-click access to frequent actions) without proprietary hardware.
- Make every part of the deck editable — layouts, scenes, pages, icons, backgrounds, actions — instead of a fixed set of buttons.
- Keep setup to a single interactive menu so non-technical users can get running without manually wiring up a Python + Node dev environment.

## Key Features

- **Custom grids, scenes & pages** — drag, resize, and arrange buttons freely across multiple layouts per profile.
- **Hotkeys & macros, system control** — keyboard shortcuts, chained actions, volume/brightness/media/power/window management.
- **Apps, URLs & OBS integration** — launch programs, open sites, run commands, control OBS scenes and sources.
- **Live widgets** — CPU/RAM/GPU/disk/network metrics, weather, world clock, timers, and countdowns.
- **26+ animated backgrounds** — aurora, light rays, silk, iridescence, plus custom wallpaper uploads.
- **Touch modes** — normal, touch-friendly, and tablet sizing for different device setups.
- **One setup menu** — `setup.bat`/`setup.sh` handles dependency install, Electron packaging, and desktop shortcut creation, interactively or via flags (`--full`, `--deps`, `--shortcut`, `--launch`).

## Potential Use Cases

- Streamers and content creators wanting a free, fully custom stream-deck alternative.
- Power users who want one-click access to system controls, app launches, and OBS scenes without dedicated hardware.
- Home office setups wanting a live system-metrics + weather + quick-launch dashboard on a spare monitor or tablet.

## How to Use

```bash
git clone https://github.com/ponya5/VDock2.git
cd VDock2
setup.bat        # Windows — or ./setup.sh on macOS/Linux
```

Then launch via the desktop shortcut, or `launch.bat` / `./launch.sh`. VDock opens at `http://localhost:3000` after a 5–10 second startup.

## Tech Stack

Python Flask backend, Vue 3 + TypeScript frontend, Electron for the desktop shell — cross-platform on Windows, macOS, and Linux.

---

This is a private repository. [Contact me on LinkedIn](https://www.linkedin.com/in/daniel-shalom-13987a1a/) for a walkthrough or access.

[← Back to profile](../../README.md)
