[← Back to profile](../../README.md)

# Beacon

![Repo](https://img.shields.io/badge/Repo-Private-red?style=for-the-badge&logo=github)
[![Live Demo](https://img.shields.io/badge/Live-beacon--ai.me-blue?style=for-the-badge&logo=googlechrome&logoColor=white)](https://beacon-ai.me)

<a href="https://www.linkedin.com/in/daniel-shalom-13987a1a/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" /></a>
<a href="https://github.com/ponya5"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" /></a>
<a href="https://www.daniel-shalom.com"><img src="https://img.shields.io/badge/Website-www.daniel--shalom.com-green?style=for-the-badge&logo=googlechrome&logoColor=white" /></a>
<a href="https://www.instagram.com/daniel.shalom.ai/"><img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" /></a>

**A free, open-source event-discovery platform that aggregates tech, AI, and developer events into one Hebrew-friendly dashboard.**

<a href="../../assets/beacon-demo.gif"><img src="../../assets/beacon-demo.gif" width="100%" /></a>

## Overview

Finding the next relevant conference, meetup, or workshop usually means checking dozens of sites and newsletters. Beacon aggregates events from multiple curated sources, normalizes the data, and presents everything in one clean list or calendar view. Past events are purged automatically, so the feed never fills up with stale listings — and the UI has full Hebrew RTL support for the Israeli tech community it was originally built for.

## Goals

- Give tech professionals one place to discover upcoming conferences, meetups, and webinars instead of checking many sources.
- Keep the feed always current — no expired or past events cluttering the view.
- Make discovery genuinely usable for a Hebrew-speaking audience with proper RTL support, not just a translated English UI.

## Key Features

- **Aggregated feed** of tech, AI, and developer events from multiple curated sources, with a searchable/filterable list view and a monthly or free-scroll calendar view.
- **Smart calendar** — visual indicators for today, selected date, events you're attending, and admin-highlighted recommended events.
- **Personalization** — Attend/Register actions on event cards, event-type badges, and location normalization (online events and major cities prioritized).
- **Admin & automation** — an admin panel for managing sources and monitoring sync health, an automated scraper with retry/timeout protection, and manual sync with real-time progress.
- **Design & UX** — a glass-morphism UI with a flowing WebGL background, full Hebrew RTL support, and responsive design for desktop and mobile.

## Potential Use Cases

- Tech professionals wanting a single, always-current view of upcoming events instead of tracking multiple newsletters.
- Event organizers wanting their events discovered by the community without extra promotion overhead.
- Developers looking for a real-world example of a Supabase + Edge Functions + automated scraping architecture.

## How to Use

Visit [beacon-ai.me](https://beacon-ai.me) directly — browse the `/explore` page for the list or calendar view, or submit your own event via `/add-event`.

## Tech Stack

React 18 + TypeScript + Vite + Tailwind CSS + shadcn/ui, Supabase (Postgres, Auth, Row-Level Security, Edge Functions, pg_cron), Firecrawl with an intelligent fallback scraper, and OpenAI GPT-4o-mini for location/topic normalization.

---

This is a private repository. Reach out via any of the links above for a walkthrough or access. Try the live app at [beacon-ai.me](https://beacon-ai.me).

[← Back to profile](../../README.md)
