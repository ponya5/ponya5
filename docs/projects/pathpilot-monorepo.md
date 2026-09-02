[← Back to profile](../../README.md)

# PathPilot (Monorepo)

![Repo](https://img.shields.io/badge/Repo-Private-red?style=for-the-badge&logo=github)
[![Contact Me](https://img.shields.io/badge/Contact%20Me-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/daniel-shalom-13987a1a/)

**A unified ecosystem of AI apps for education, analytics, and automation, sharing a common auth/config/UI foundation.**

<a href="../../assets/pathpilot-monorepo-demo.gif"><img src="../../assets/pathpilot-monorepo-demo.gif" width="100%" /></a>

## Overview

PathPilot started as several separate learning-and-productivity tools and was consolidated into one monorepo so they could share authentication, configuration, and UI components instead of duplicating that plumbing across four codebases. The monorepo currently hosts the AI Course Analyzer, AI Feedz, Training Tracker, and Log Monitor, alongside the standalone [PathPilot Tutorial Generator](pathpilot-tutorial-generator.md).

## Goals

- Give a family of AI learning/productivity tools a shared, consistent foundation instead of reinventing auth/config/UI in each one.
- Make it cheap to add a new PathPilot app by inheriting the shared shell rather than starting from scratch.
- Keep each app's domain logic (course analysis, training tracking, log monitoring) independent while sharing infrastructure.

## What's Inside

- **AI Course Analyzer** — NLP pipelines that deconstruct educational curriculums with deep semantic analysis and automated summarization: evaluates course content, assesses difficulty levels, identifies knowledge gaps, and recommends the right course for a learner's level and goals.
- **AI Feedz** — content/feed intelligence tooling within the PathPilot ecosystem.
- **Training Tracker** — autonomous agents that monitor real-time training progress with predictive analytics for milestone completion, tracking progress across multiple courses/platforms and providing automated scheduling recommendations.
- **Log Monitor** — shared logging/monitoring tooling across the PathPilot apps.

## Potential Use Cases

- Learning & development teams wanting automated curriculum analysis and gap detection.
- Individuals or teams tracking training progress across multiple courses and platforms with predictive milestone alerts.
- Anyone maintaining a family of related internal tools who wants to see a working example of a shared-foundation monorepo (auth, config, UI) instead of copy-pasted infrastructure per app.

## Tech Stack

Monorepo architecture with a shared authentication/configuration/UI layer; individual apps built with AI/NLP pipelines for content analysis and predictive analytics for progress tracking.

---

This is a private repository. [Contact me on LinkedIn](https://www.linkedin.com/in/daniel-shalom-13987a1a/) for a walkthrough or access.

[← Back to profile](../../README.md)
