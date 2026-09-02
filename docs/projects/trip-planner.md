[← Back to profile](../../README.md)

# Trip Planner Dashboard

![Repo](https://img.shields.io/badge/Repo-Public-brightgreen?style=for-the-badge&logo=github)
[![View on GitHub](https://img.shields.io/badge/View%20on%20GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ponya5/trip-planner-dashboard)

**A Claude/Cursor AI skill that turns "plan me a trip" into one self-contained HTML dashboard with a live-routed map, itinerary, hotels, budget, and safety fallbacks.**

<a href="../../assets/trip-planner-demo.gif"><img src="../../assets/trip-planner-demo.gif" width="100%" /></a>

## Overview

Most AI trip-planning outputs are a wall of text you have to mentally reconstruct into an actual plan. This skill instead produces a single HTML file: a live-routed map with animated drive playback on one tab, and a full written plan (itinerary, hotels, budget, packing, safety fallbacks) on the other — with no server, no API key, and no build step required to view it.

It was built after a real 6-day jeep trip through Georgia, where the first versions had wrong turns, a fake 300km detour from bad map data, and no way to "drive" the route. The working pieces from fixing those issues became this reusable skill.

## Goals

- Make AI trip planning produce something immediately usable — a dashboard, not a transcript.
- Fix the specific failure modes real trip planning hit: bad routing detours, layout bugs, no visual sense of the drive.
- Keep the output completely self-contained: one HTML file, no server, no API key, works offline except for map tiles/live routing.

## Key Features

- **Live-routed map** — a dotted planned line plus a thick live-routed line on real roads, with distance and drive time.
- **Detour-safe routing** — falls back to the planned line if a live route looks implausible.
- **Drive-the-trip playback** — an animated marker with speed control, pause/resume.
- **Day-by-day itinerary** — color-coded by day, with stops, tips, and a Google Maps link per day.
- **Transport costs, hotels, and lodging** — price ranges and booking links.
- **Practical lists** — budget, food, packing, and a pre-trip checklist.
- **Safety and fallbacks** — guidance for road closures or weather changes.
- **Responsive layout** — day filters, a draggable split view, and tooltips at any screen size.

## Potential Use Cases

- Anyone using Claude or Cursor who wants a genuinely usable trip plan instead of a text dump.
- Multi-day road trips where seeing the route (not just reading turn-by-turn text) matters.
- Group trips needing a shared reference (map + itinerary + budget + hotels) in one file that's easy to send around.

## How to Use

1. Try the [demo](https://github.com/ponya5/trip-planner-dashboard/blob/main/examples/demo-trip.html) first — no install needed.
2. Put the skill folder where your tool looks for skills:
   - Claude: `~/.claude/skills/trip-dashboard/`
   - Cursor: `~/.cursor/skills/trip-dashboard/`
3. Ask for a trip in plain language, e.g. *"Plan a 7-day road trip through Scotland for 4 of us, renting one car."*
4. Answer any follow-up questions (dates, budget, group size).
5. Open the HTML file the AI creates in your browser.

## Tech Stack

A self-contained HTML/CSS/JS dashboard template (map + itinerary engine), packaged as a Claude/Cursor Agent Skill with example demos and an evaluation set (`evals/evals.json`) used during development.

---

⭐ [Star the repo](https://github.com/ponya5/trip-planner-dashboard) if you find it useful.

[← Back to profile](../../README.md)
