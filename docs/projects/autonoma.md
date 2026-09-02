[← Back to profile](../../README.md)

# Autonoma — Autonomous Web Security Crawler

![Repo](https://img.shields.io/badge/Repo-Private-red?style=for-the-badge&logo=github)

<a href="https://www.linkedin.com/in/daniel-shalom-13987a1a/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" /></a>
<a href="https://github.com/ponya5"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" /></a>
<a href="https://www.daniel-shalom.com"><img src="https://img.shields.io/badge/Website-www.daniel--shalom.com-green?style=for-the-badge&logo=googlechrome&logoColor=white" /></a>
<a href="https://www.instagram.com/daniel.shalom.ai/"><img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" /></a>

**An autonomous, state-aware agent that crawls a web application, maps every page and interactive element, and tests each one for functional bugs and OWASP security vulnerabilities.**

<a href="../../assets/autonoma-screenshot.png"><img src="../../assets/autonoma-screenshot.png" width="100%" /></a>

## Overview

Manual QA and pentest coverage rarely scales with how fast an application's pages and forms change. Autonoma maps a target app end-to-end — every page, every form, every button — then runs a coordinated set of agents against each element: a baseline pass to establish clean behavior, a chaos/abuse pass for functional bugs, an OWASP payload pass for security vulnerabilities, and an LLM-driven business-logic pass for the gaps rule-based testing misses. A React control console lets you start scans, watch progress live, and drill into every finding with reproduction steps and evidence.

## Goals

- Give QA and security teams continuous, automated coverage of an app's full page and form surface — not just the pages someone remembered to test.
- Separate "this looks broken" from "this is actually a regression" by testing against a clean baseline first.
- Make findings actionable: every issue ships with reproduction steps, HTTP evidence, screenshots, and a session video clip.
- Let generated automation (Playwright tests) come directly out of the crawl data instead of being written from scratch.

## Key Features

- **Autonomous crawl** — DFS traversal maps every reachable page and groups interactive elements (forms, navigation, action buttons).
- **Mixed public/auth scan** — public pages are crawled without cookies; once a login page is found, the crawler performs one authenticated login, then continues testing protected pages with that session.
- **Multi-agent testing** — Baseline (clean behavior), Abuser (functional chaos: empty/overlong inputs, Unicode, double submits), Security (SQL injection variants, XSS), and Analyst (LLM-driven business-logic testing).
- **Runs dashboard** — every crawl is a "run" with its own issues, tasks, logs, and topology (graph, tree, and network views).
- **Issues viewer** — full reproduction detail: HTTP evidence, console errors, screenshots, and a session video clip centered on the issue.
- **Live browser stream** — watch each crawl worker's browser live via MJPEG.
- **Story to Xray Tests** — generate Xray manual test cases from a Jira story using an LLM, review/edit, and push to Jira.
- **Automation Tests** — generate Playwright TypeScript tests from a manual test case and the crawl's site map, run them in-browser, and auto-heal failing tests by reading Playwright's accessibility snapshot at failure time.
- **Cross-run statistics** — KPI dashboard (pass rate, judge confidence, time-to-remediate) with CSV export and Slack reporting.
- **Demo mode** — three pre-recorded crawl runs load instantly with no backend, so you can explore the UI without a live target.

## Potential Use Cases

- QA teams needing continuous regression coverage across an evolving web app.
- Security teams running lightweight, repeatable OWASP checks between formal pentests.
- Teams wanting to bootstrap a Playwright test suite from real crawl data instead of writing it by hand.
- Engineering leads wanting an executive-level "AI risk summary" of an app's health after every scan.

## How to Use

```bash
# 1 — Clone
git clone https://github.com/ponya5/Autonoma.git
cd Autonoma

# 2 — Copy and fill in your API keys (optional — only needed for LLM-assisted grouping)
cp .env.example .env

# 3 — Launch (installs everything automatically on first run)
./launch.sh          # macOS / Linux
launch.bat           # Windows
```

Then either flip the **Demo** toggle to explore pre-recorded runs, or start a real scan:

```bash
crawler crawl --url https://your-target.com/app --username user@example.com --password secret
```

Frontend runs at `http://localhost:5173`, backend API at `http://localhost:8000`.

## Tech Stack

Python (FastAPI backend, Playwright browser automation, Pydantic models), React 19 + Vite 7 + Tailwind v4 + shadcn/ui frontend, SQLite for run metadata, and pluggable LLM providers (Claude, OpenAI, Ollama) for element grouping and business-logic testing.

---

This is a private repository. Reach out via any of the links above for a walkthrough or access.

[← Back to profile](../../README.md)
