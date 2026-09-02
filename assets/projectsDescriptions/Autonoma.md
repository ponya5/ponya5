# Autonoma — Autonomous Web Security Crawler

An autonomous, state-aware agent that crawls a web application, maps every page and interactive element, and tests each one for functional bugs and OWASP security vulnerabilities. A React control console lets you start scans, monitor live progress, review findings per crawl run, and export reports — all from the browser.

---

## Quick Start

**Prerequisites:** Python 3.11+, Node.js 18+, Git

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

That's it. The script creates a Python venv, installs all dependencies, starts the API on `:8000`, and opens the UI at **http://localhost:5173** automatically.

> **Want to explore without a live target?** Flip the **Demo** toggle in the top bar. Three pre-recorded crawl runs load instantly — no setup required.

---

## Features

| Area | What it does |
|------|--------------|
| **Autonomous crawl** | DFS traversal maps every reachable page and groups interactive elements (forms, navigation, action buttons) |
| **Mixed public/auth scan** | Public pages are crawled without cookies; when a login page is discovered the crawler first captures `auth.json` with one successful login, then tests the login page publicly and revisits protected pages with authenticated browser state |
| **Baseline agent** | Fills forms with LLM-generated realistic values (cached), clicks standalone buttons once — establishes a clean baseline to suppress false positives |
| **Abuser agent** | Chaos tests on forms only: empty/overlong inputs, Unicode/emoji, double submissions, partial fills, radio combinations |
| **Security agent** | OWASP payloads: SQL injection (auth bypass, error, union, blind, time-based), reflected XSS (5 vectors) |
| **Analyst agent** | LLM-based business-logic testing: generates a per-page test plan, executes via constrained actions, evaluates results — targets semantic and workflow gaps the catalog agents miss |
| **LLM-assisted grouping** | Optionally use Claude, OpenAI, or local Ollama to improve element group labels |
| **Runs dashboard** | Every crawl is a "run" — issues, tasks, logs, and topology per run or aggregated across all runs |
| **Graph topology** | Three views: Graphic (ReactFlow with depth floor lanes), Tree (indented with depth badges, connecting lines, issue counts), and Network (force-directed graph) |
| **Issues viewer** | Full issue detail with reproduction steps, HTTP evidence, console errors, screenshots, and a session video clip (±5 seconds around issue detection, scrubber pre-positioned) |
| **Artifacts labeling** | Artifacts tab shows which screenshot belongs to which issue; navigator/session screenshots labeled as generic artifacts |
| **Agent log expansion** | Expanding a log row shows a human-readable sentence ("Navigator captured snapshot of Login (/login)") and resolves `node_xxx` IDs to page names |
| **System status** | Built-in self-check for API, Playwright, state directories, auth file, and all LLM providers |
| **Live UI** | Real-time log stream, draggable stat cards, task queue, issues drill-down, and report generation |
| **Live browser stream** | MJPEG feed of each crawl worker's browser at `/api/stream/browser?worker=N`; togglable at runtime without restarting the crawl |
| **Run export / import** | Download runs + findings as a JSON bundle; import to restore on another instance |
| **Page performance** | Per-page timing metrics (FCP, DOM Loaded, Load Complete, Network Idle) with slow-page highlighting in the Performance view |
| **Demo mode** | Pre-recorded runs, no backend needed — toggle from the top bar |
| **Story to Xray Tests** | Load a Jira story, generate Xray manual test cases with an LLM, review/edit them, and push them to Jira/Xray — all from the browser. Runs without real Jira/Xray credentials using stub mode (`JIRA_XRAY_MODE=stub`). |
| **Automation Tests** | Generate Playwright TypeScript page objects and spec files from a selected manual test case and a persistent site map. Edit, run, and debug generated tests in the browser. **Stabilize** button automatically heals failing tests: runs the test, reads Playwright's `error-context.md` (the live accessibility snapshot at failure time), calls the LLM with real page data, applies the fix, and retries — up to `STABILIZE_MAX_ATTEMPTS` times. |
| **Module-based navigation** | Sidebar organised into four sections — Crawler, Site Maps, Test Management, General. Root `/` shows a neutral module launcher; the Dashboard is at `/dashboard`. Non-crawler routes show a `Module / Page` breadcrumb in the top bar instead of the run-context UI; crawler polling is suppressed on Test Management and General routes. |

---

## Prerequisites

| Tool | Minimum version | Purpose |
|------|----------------|---------|
| Python | **3.11** | Backend crawler + API server |
| Node.js | **18** | React frontend |
| npm | **9** | Frontend package manager (comes with Node) |
| Git | any | Clone the repo |

Python LLM packages and the Playwright browser binary are installed automatically during setup.

---

## Detailed Installation

### Step 1 — Python environment

```bash
python -m venv .venv

# Activate (macOS / Linux)
source .venv/bin/activate

# Activate (Windows PowerShell)
.venv\Scripts\Activate.ps1

# Option A — editable install (recommended for development)
pip install -e ".[all,api]"

# Option B — pinned install from requirements.txt (recommended for CI / Docker)
pip install -r requirements.txt

# For tests, also install dev dependencies
pip install -r requirements-dev.txt

# Install Playwright's Chromium browser
playwright install chromium
```

> `[all]` includes the `anthropic` and `openai` packages.  
> `[api]` includes `fastapi`, `uvicorn`, `sse-starlette`, and `httpx`.  
> `requirements.txt` contains all pinned production dependencies.  
> `requirements-dev.txt` extends it with `pytest`, `pytest-asyncio`, and `pytest-mock`.

### Step 2 — Frontend

```bash
cd frontend
npm install
```

### Step 3 — Environment variables

Copy the example file and add your keys:

```bash
cp .env.example .env
```

Open `.env` and fill in whichever LLM providers you want to use:

```bash
# Claude (Anthropic) — https://console.anthropic.com
ANTHROPIC_API_KEY=sk-ant-...

# OpenAI — https://platform.openai.com/api-keys
OPENAI_API_KEY=sk-...

# Ollama (local, no key needed by default)
# Just run: ollama serve
# Optionally set a custom base URL:
# OLLAMA_BASE_URL=http://localhost:11434
```

LLM providers are **optional**. Without one, element grouping uses rule-based heuristics. At least one provider is recommended for best results.

### Step 4 — Launch

```bash
# macOS / Linux (starts both servers, opens browser)
./launch.sh

# Windows
launch.bat
```

| Service | URL |
|---------|-----|
| Frontend UI | http://localhost:5173 |
| Backend API | http://localhost:8000 |
| API docs | http://localhost:8000/docs |

---

## Typical Workflow

```bash
# 1. Start a mixed public/auth scan
#    Public pages (including login/signup) are mapped first.
#    When a login page is discovered, the crawler first performs one successful login,
#    writes auth.json, then tests the login page publicly and continues on protected pages with that storage state.
crawler crawl --url https://your-target.com/app --username user@example.com --password secret

# 2. Review findings in the UI, or generate a report from the CLI
crawler report
```

When starting from the frontend New Run modal, fill **Authenticator secret** only for targets whose login flow asks for an authenticator-app OTP code. Leave it blank for normal username/password logins. The secret is used only for the one successful login that captures `auth.json`; saved run snapshots record only whether OTP was enabled, not the secret value.

For SSO, MFA, CAPTCHA, or flows the automated login helper cannot handle, use the manual fallback:

```bash
crawler auth --url https://your-target.com/login
crawler crawl --url https://your-target.com/app --resume
```

Alternatively, use the **Dashboard** in the UI to start/stop scans, set options, and monitor everything live.

---

## CLI Reference

All commands require the virtual environment to be active (`source .venv/bin/activate`).

### `crawler crawl` — run a scan

```bash
crawler crawl --url <target-url> [options]
```

| Flag | Default | Description |
|------|---------|-------------|
| `--url` | *(required)* | Target URL to crawl |
| `--resume` | false | Continue from existing state instead of starting fresh |
| `--headless` / `--no-headless` | headless | Run browser headlessly or visibly |
| `--max-depth` | 50 | Maximum DFS traversal depth |
| `--username` | none | Credentials for the one successful login performed when the crawler discovers a login page |
| `--password` | none | Password for the automated successful login |
| `--login-url` | none | Optional legacy hint for the login page URL; normally the crawler discovers the login page during the crawl |
| `--llm-provider` | none | LLM for element grouping: `claude`, `openai`, or `ollama` |
| `--llm-model` | provider default | Model name override |

```bash
# Basic scan
crawler crawl --url https://example.com/login

# Mixed public/auth scan with automated successful login
crawler crawl --url https://example.com/app --username user@example.com --password secret

# LLM-assisted, visible browser
crawler crawl --url https://example.com/login --no-headless --llm-provider claude

# Resume an interrupted scan
crawler crawl --url https://example.com/login --resume
```

### `crawler auth` — manual auth fallback

```bash
crawler auth --url <login-url> [--output auth.json]
```

Opens a visible Chromium window at `--url`. Log in manually, then press Enter in the terminal. The session (cookies, localStorage) is saved to `auth.json` and then reused for `auth_required=true` pages during the crawl.

### `crawler report` — export a findings report

```bash
crawler report [--format markdown|json] [--output <file>]
```

```bash
crawler report                          # Markdown to stdout
crawler report --format json -o r.json  # JSON to file
```

---

## System Status Check

The Dashboard includes a **System Status** card that checks all components before you start a scan:

| Check | What it verifies |
|-------|-----------------|
| API Server | Backend is reachable |
| Playwright Browser | Chromium is installed |
| State Directories | `state/`, `knowledge_base/`, `logs/` exist |
| Auth File | `auth.json` is present when protected pages need authenticated browser state |
| Claude | `ANTHROPIC_API_KEY` is set |
| OpenAI | `OPENAI_API_KEY` is set |
| Ollama | Local Ollama server is reachable |

Hit **Re-check** after updating your `.env` or running `playwright install chromium`.

---

## Output Files

| Path | Contents |
|------|----------|
| `runs/<run-id>/` | Isolated per-run directory: findings, state, screenshots, logs |
| `runs/<run-id>/knowledge_base/findings/` | One JSON file per finding — severity, reproduction steps, HTTP evidence |
| `runs/<run-id>/knowledge_base/screenshots/` | Evidence PNGs |
| `runs/<run-id>/knowledge_base/pages/` | Accessibility snapshots per page |
| `runs/<run-id>/state/graph.json` | DFS graph: nodes, edges, traversal state |
| `runs/<run-id>/state/task_queue.json` | Task queue with dependencies |
| `runs/<run-id>/logs/agent_log.jsonl` | Structured append-only log (JSON Lines) |
| `llm_cache/` | Shared at repo root — on-disk LLM form-value cache (all runs and the CLI) |
| `state/graph.json` | Symlinked to the active run's state (live crawl) |
| `logs/agent_log.jsonl` | Symlinked to the active run's log (live crawl) |

> Starting a new scan (without `--resume`) creates a fresh run directory. Previous run data is always preserved and browsable from the **Runs** page in the UI.

### Dashboard stat definitions

| Stat | UI label | Meaning |
|------|----------|---------|
| `issues_count` | Issues | Total issues found by agents (Abuser + Security + Analyst) |
| `tasks_failed` | Tasks errored | Tasks that raised an exception or crashed during execution |
| `tasks_pending` | Not started | Tasks that were queued but never executed before the run stopped |

---

## What Gets Tested

### Navigator — Page Discovery & Performance
- Extracts ordinary in-page links from the DOM and adds same-site pages to the DFS crawl graph
- Clicks links that open in a secondary tab, captures the popup URL, closes the new tab, and returns to the original tab before continuing
- Treats only the exact original hostname as in-scope, so the crawl stays on the same domain + subdomain as the starting URL
- Ignores links on any other host, including sibling subdomains, and logs that they were skipped
- **Measures page load performance** after each navigation using the browser's native Performance API (Navigation Timing + Paint Timing): First Paint, First Contentful Paint (FCP), DOM Content Loaded, Load Complete, and Time to Network Idle. Results are written to `runs/{slug}/performance.json`. Pages where any key metric exceeds 3 s are flagged as slow and highlighted in the Performance view.

### Baseline — Benign Interaction
- Uses LLM to generate realistic, context-aware values for each form field (e.g. real names, valid email addresses). Falls back to hardcoded lookup tables when LLM is unavailable. LLM results are cached per unique field set so the same form never triggers a second LLM call.
- Submits each form once with those values and clicks standalone action buttons once
- Records the baseline response so Abuser and Security can suppress findings that were already present before negative testing

### Abuser — Functional Chaos (forms only)
- Empty and overlong submissions (10 000 characters)
- Unicode, emoji, zero-width characters
- HTML tags and special characters in input fields
- Repeated form submissions, double submit
- Mismatched input types, partial form fills
- Each radio button option tested independently
- **Standalone action buttons are not chaos-tested** — a single baseline click is sufficient; errors on buttons are ignored (happy flow)

### Security — OWASP
- **SQL Injection (auth bypass)**: `OR 1=1` patterns targeting login forms
- **SQL Injection (error-based)**: single quote, stacked queries, DROP TABLE
- **SQL Injection (union-based)**: 1–3 NULL column enumeration
- **SQL Injection (boolean-blind)**: true/false condition diffing
- **SQL Injection (time-blind)**: `SLEEP`, `WAITFOR DELAY`, `pg_sleep` across MySQL / MSSQL / PostgreSQL
- **XSS**: script tag, img onerror, attribute breakout, javascript protocol, event handler injection

### Analyst — LLM-Based Business Logic
Runs after Abuser + Security complete on each node. Focuses on gaps the catalog-driven agents miss.
- Receives page summary, element groups with baseline results, and existing findings as context
- LLM generates a structured test plan targeting business logic, semantic validation, and workflow edge cases
- Executes tests via a constrained action vocabulary (`fill`, `click`, `submit`, `check_response`, `screenshot`, `read_text`, `get_url`, `navigate`, `trigger_dynamic_region`)
- A second LLM call evaluates each result and decides whether it represents a real issue
- Findings recorded with `agent: "analyst"` alongside standard evidence (screenshots, HTTP evidence)
- Includes dynamic region context (modals, dropdowns) — can trigger and test them
- Configurable via `analyst_enabled` (default `true`), `analyst_max_actions` (default `10`), and `analyst_model` (default: same provider as other agents)

### LLM Finding Judge — Value & Severity Review
After all agents finish (and before the run summary), an LLM reviews every finding as a triage lead.
- For each finding it decides whether the issue is genuinely valuable (filtering noise and expected behaviour) and assigns a corrected severity, a confidence score (0–1), and a one-sentence rationale
- The verdict is stored **non-destructively** in a `judgment` block on each finding; the agent-assigned severity and the severity-distribution counts are left unchanged
- Judgments are cached so identical findings across pages cost one LLM call; the pass is gated by `finding_judge_enabled` (default `true`) and skipped when no LLM is configured
- Non-blocking: a per-finding judge failure is logged and never affects run completion; if the LLM was unavailable, the finding gets a neutral fallback judgment that is automatically retried on the next resume (rather than being treated as already judged)
- Crawled page content sent to the judge (title, description, response snippet, console errors) is length-capped and delimited as untrusted data, and the judge is instructed to never follow instructions embedded in it

### LLM Run Summary — AI Insights
After all agents complete on a run, the orchestrator generates a business-level summary of all findings.
- Synthesizes findings into an executive-facing analysis: what kind of application it is, overall risk posture, recurring patterns, top issues, and prioritized remediation recommendations
- Assigns a risk score (1–10) and groups findings by severity distribution
- Written to `runs/{slug}/summary.json` alongside `stats.json`
- Non-blocking: if the LLM fails or is not configured, the run still completes normally
- For stopped/aborted runs: the Issues page shows a "Generate AI Insights" button that triggers on-demand generation via `POST /api/runs/{run_id}/summary`
- Displayed in the `RunSummaryPanel` on the Issues page when a specific run is selected

### Persistent Site Map — Cross-Run Accumulation
A per-hostname site map (`sites/<site_id>/`) that accumulates pages, edges, and issues across many crawl runs.
- When a crawl completes or is stopped, it enters a **pending-merge** queue instead of being discarded
- The **Merge Review** screen (`/runs/:runId/merge`) shows every crawled page with its screenshot, URL, status, and health-warning badges (console errors, failed XHRs, navigation failures) so the user can spot empty or error renders from SPAs before committing
- Per-page selection: check only the pages that rendered correctly; the rest are left untouched in the site map
- **Issue lifecycle**: `open` → re-tested and gone → `resolved`; reappears → `regressed`; page deselected or only partially tested → issue stays `open` (no false resolutions)
- Merge records store reversible deltas (prior page state and issue state) for future undo support
- Site views: **Site Maps** page lists all sites; each site has Map / Issues / Performance / Runs tabs
- Sidebar shows a badge on Site Maps when runs are awaiting review; Runs page shows a "Review & Merge" button on pending runs
- On-disk: `sites/<site_id>/{site_map.json, issues.json, merges.json}` + `sites` SQLite table

### Cross-Run Statistics Dashboard — KPIs & Slack Export
A "Statistics" tab on the Report page (`/monitor`) shows aggregated health KPIs across all recorded crawl runs.
- **KPI cards**: Runs analysed, task pass rate (`tasks_completed / total`), average LLM judge confidence (excluding `provider_error` fallbacks), and average time-to-remediate (from resolved `SiteIssue` records in `sites/*/issues.json`)
- **Cross-run trend chart**: Issues found, pages tested, and tasks failed plotted as an area chart over all runs — oldest to newest
- **CSV export**: `GET /api/statistics/export?format=csv` — one row per run + a trailing KPI summary block
- **Slack integration**: "Send to Slack" button on both the Statistics tab and the existing Report download area. Posts a structured summary (title + bullet KPIs + fields) via an incoming webhook. Requires `SLACK_WEBHOOK_URL` env var. Both buttons are disabled with a tooltip when the webhook is not configured. `GET /api/integrations/slack/health` reports configured / unconfigured.
- Data is computed on-the-fly from existing on-disk artifacts — no new persistence layer
- Demo mode reads a static `DEMO_STATISTICS` snapshot (6-run securebank scenario)

### Story to Xray Tests — LLM-Assisted Test Case Generation
A standalone screen for QA teams to generate Xray manual test cases from a Jira story using an LLM.
- Enter a Jira story key; the backend retrieves the story and any already-linked Xray manual tests
- Choose generation options (happy-path, negative, edge cases, permission/role, API-level, UI-level) and click **Generate test cases** — the LLM returns structured, validated test cases. Each option has an editable count field next to its checkbox controlling the maximum tests to generate for that category (default: 1 for happy-path, 3 for every other category; max 20 per category — the LLM may return fewer than the maximum)
- Click the chevron next to **Generate test cases** for **Generate with instructions** — add free-text instructions (e.g. "focus negative tests on the payment step") that are given priority over the default generation rules
- Review, edit (title, description, prerequisites, steps with action / test data / expected result), reorder steps, add manual tests, or delete drafts
- **Add to Jira** saves a new test and links it to the story; **Save changes** updates an existing Xray test (with a confirmation prompt warning about shared usage)
- Saved tests display their Jira key as a direct link; unsaved drafts are clearly badged (LLM / Manual / Modified)
- No Jira access? Click **Create test case without Jira** next to the story loader to seed a blank manual test case and skip straight to editing + **Automate**, without loading any story. The Jira-only panels (story card, Generate, Save/Test Set) are hidden in this mode; the ad-hoc test case is not persisted, only handed off to Automation Tests.
- Runs without real Jira/Xray credentials using `JIRA_XRAY_MODE=stub` (default). Set global `LLM_PROVIDER` / `LLM_MODEL` in `.env`, or override this feature with `JIRA_LLM_PROVIDER` / `JIRA_LLM_MODEL`. Jira generation defaults to a 300 second timeout; override with `JIRA_LLM_TIMEOUT`.

### Automation Tests — Generate and Stabilize Playwright Tests
A screen for QA teams to generate Playwright TypeScript automation from a selected manual test case and a persistent site map, then run and maintain those tests directly from the browser.

**Test repo:** by default, Generate/Run/Stabilize/Refactor/Remediate all operate on the bundled `generated-tests/` folder. Use the **Test repo** field in the left panel to point them at an external git repo instead (an absolute path to an already-bootstrapped Playwright/TypeScript project — its own `package.json`, `tsconfig.json`, `playwright.config.ts`, and `node_modules` with `tsc`/`playwright` installed). The path is validated and persisted server-side, so it's remembered across sessions and backend restarts.

**Generate:** pick a test case from Story to Xray and a crawl run, click **Generate**. The backend reads the crawl graph and page snapshots, calls the LLM, writes TypeScript page objects and a spec file, runs `tsc --noEmit` and `playwright test`, and lands validated files in `generated-tests/`.

**Run:** select a `.spec.ts` file in the file tree and click **Run**. Playwright output streams to the resizable terminal pane in real time; click **Stop** to terminate. The file/config panel and terminal pane are both resizable, and Generation, Run, Stabilize, and Refactor output tabs stay available once they have appeared in the session. Once the run finishes, click **View Report** next to the status badge to open Playwright's HTML report in a new tab — screenshots, video, and the trace viewer for that run are all browsable from there.

**Stabilize:** if a test fails after a UI change, click **Stabilize**. The heal loop runs the test, reads Playwright's automatically generated `error-context.md` (which contains the live page accessibility snapshot at the moment of failure), builds a prompt with real page data, asks the LLM for a fix, applies changed files through the same locator-policy lint as generation, and retries. Repeats up to `STABILIZE_MAX_ATTEMPTS` times (default `5`). A full session log is written to `generated-tests/.stabilize-logs/` after every stabilization run.

**Fix Test (Remediate):** if a test run fails and you want an automated root-cause triage before healing, click **Fix Test**. The remediation loop first calls an LLM judge to classify the failure as `test_defect`, `app_bug`, or `flaky`. Only `test_defect` proceeds to the heal loop (same as Stabilize); `app_bug` and `flaky` short-circuit immediately — the test source is never modified. An `app_bug` verdict shows a red banner in the **Remediate** output tab so developers can act on the real issue. Each remediation run is logged to `generated-tests/.remediation-logs/`. Optionally, a successful heal can push the updated spec back to Xray by setting `push_to_xray` and providing an Xray test key.

**Edit safely:** Cmd/Ctrl+S saves from the editor. Delete requires modal confirmation, rename commits only on Enter, and Run/Stabilize/Refactor share the same unsaved-changes dialog. Non-spec files show an inline hint because only `.spec.ts` files can run, stabilize, or refactor.

**Git controls:** a toolbar between the Test repo field and the file tree shows the current branch, ahead/behind counts, and a change count; use it to fetch/pull/push, switch or create a branch, and view diffs, commit, or discard changes — all without leaving the browser. Only available for an external repo (the bundled `generated-tests/` default has no `.git` of its own, so git controls are disabled there to avoid ever touching Autonoma's own repository). Push/pull use your own system git credentials (ssh-agent, `~/.gitconfig`, OS credential helpers) — Autonoma stores no secret. Checkout and pull are blocked while you have uncommitted changes (commit or discard first — there's no auto-stash), and every git action is blocked while a generation/run/stabilize/refactor/remediation job is in flight.

**Bootstrap** (first time only):
```bash
cd generated-tests && npm ci && npx playwright install chromium
```

**Key env vars:** `AUTOMATION_LLM_PROVIDER`, `AUTOMATION_LLM_MODEL`, `AUTOMATION_LLM_TIMEOUT`, `AUTOMATION_HEADED` (`true`/`false`), `STABILIZE_MAX_ATTEMPTS`, `E2E_EMAIL`, `E2E_PASSWORD`.

---

## How It Works

Six agents coordinate through shared JSON state files (`state/graph.json`, `state/task_queue.json`):

| Agent | Role |
|-------|------|
| **Orchestrator** | Drives the DFS loop; sequences Baseline → Abuser → Security → Analyst on each node |
| **Navigator** | Maps pages — takes accessibility snapshots, groups elements, discovers links, generates a page summary |
| **Baseline** | One benign interaction per group to establish a clean response baseline |
| **Abuser** | Chaos tests every element group (runs after Baseline, before Security) |
| **Security** | OWASP payload injection on every element group |
| **Analyst** | LLM-driven business-logic tests — runs after Security, targets semantic and workflow gaps |

Node status flow: `unmapped → mapped → partially_tested → tested → fully_tested`
- `partially_tested` is set after all Abuser groups complete on a node
- `tested` is set after all Security groups complete
- `fully_tested` is set after the Analyst completes (skipped if `analyst_enabled: false`)

Mixed public/auth scan:
- **Public pages** — crawled and tested without `auth.json`, including login, signup, forgot-password, and other unauthenticated routes
- **Login page** — once mapped, the crawler first performs one successful login with the supplied credentials in a fresh public context to capture `auth.json`; when the New Run modal includes an authenticator secret, it generates and submits the OTP before saving state. The login page is then tested without using that saved auth state
- **Protected pages** — preserved as `auth_required=true` and mapped/tested only after `auth.json` exists

---

## Project Structure

```
Autonoma/
├── crawler/                    # Python package — all agent logic
│   ├── agents/                 # Orchestrator, Navigator, Baseline, Abuser, Security
│   │   ├── orchestrator.py
│   │   ├── navigator.py
│   │   ├── baseline.py         # Benign-interaction baseline agent
│   │   ├── abuser.py
│   │   ├── security.py
│   │   └── _helpers.py         # Shared helpers (radio groups, submit locator, etc.)
│   ├── browser/                # Playwright wrapper + auth capture
│   ├── models/                 # Pydantic models (graph, tasks, findings)
│   ├── payloads/               # Abuse and security test catalogs
│   ├── state/                  # GraphStore, TaskStore
│   ├── detection/              # Response analyzer
│   ├── llm/                    # LLM provider abstraction (Claude, OpenAI, Ollama)
│   ├── config.py               # Config dataclass
│   ├── cli.py                  # CLI entry point (`crawler` command)
│   ├── log.py                  # Structured logging helpers (CrawlerLogger)
│   └── report.py               # Report generator
├── backend/                    # FastAPI server
│   ├── main.py                 # App factory, CORS, static mounts
│   ├── routers/                # crawl, graph, tasks, findings, logs, report, auth,
│   │                           # health, runs, performance, images, stream, system_logs
│   ├── schemas.py              # Pydantic request/response models
│   ├── crawler_service.py      # Async crawl task management
│   ├── run_paths.py            # Per-run path resolution helpers
│   ├── deps.py                 # FastAPI dependency injection
│   └── db/                     # SQLite run repository
├── frontend/                   # React 19 + Vite 7 + Tailwind v4 + shadcn/ui
│   └── src/
│       ├── pages/              # Dashboard, Findings, FindingDetail, Evidence,
│       │                       # Graph, Tasks, Logs, SystemLogs, Report, Runs, Help,
│       │                       # runs/Performance (per-run page load timing)
│       ├── components/
│       │   ├── dashboard/      # DraggableCardGrid and stat card components
│       │   ├── graph/          # Graphic / Tree / Table topology components
│       │   ├── monitor/        # Live monitor components
│       │   ├── layout/         # Sidebar, TopBar
│       │   └── ui/             # shadcn/ui primitives
│       ├── api/                # Typed API client wrappers
│       ├── hooks/              # useCrawlStatus, useFindings, useTasks, useLogStream, usePerformance, ...
│       ├── contexts/           # DemoContext, RunContext, ThemeContext
│       ├── types/              # Shared TypeScript type definitions
│       ├── lib/                # Utility functions
│       └── demo/               # Static demo data (pre-recorded runs)
├── runs/                       # Per-run scan output (state, findings, logs, screenshots)
├── demo/                       # Pre-built demo run data served by the backend
├── state/                      # Runtime state — gitignored
├── knowledge_base/             # Scan output — gitignored
├── logs/                       # agent_log.jsonl — gitignored
├── llm_cache/                  # LLM response cache — gitignored
├── tests/
│   ├── unit/                   # Fast unit tests (no browser required)
│   ├── browser/                # Browser-level integration tests
│   └── e2e/                    # End-to-end tests (require a running target)
├── scripts/                    # Developer utilities (demo data generation, debug helpers)
├── design-log/                 # Architecture decision records
├── docs/
│   ├── architecture.md         # System design
│   └── schemas.md              # JSON schemas for all data files
├── pyproject.toml              # Python project + dependency groups
├── requirements.txt            # Pinned production dependencies
├── requirements-dev.txt        # Pinned dev/test dependencies
├── run.py                      # Backend entry point (python run.py)
├── launch.sh                   # One-command launch (macOS / Linux)
├── launch.bat                  # One-command launch (Windows)
└── .env.example                # Environment variable template
```

---

## Running Tests

```bash
source .venv/bin/activate
pytest tests/unit/             # Fast unit tests (no browser required)
pytest tests/browser/          # Browser-level integration tests
pytest tests/e2e/ -m e2e       # End-to-end tests (requires a running target)
```

---

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| `playwright: command not found` | Run `pip install playwright && playwright install chromium` inside the venv |
| `Cannot connect to API` | Make sure the backend is running: `python run.py` (or use `launch.bat` / `launch.sh`) |
| Ollama shows "Not reachable" | Run `ollama serve` in a separate terminal |
| `auth.json` warning in System Status | If automated login is not possible, run `crawler auth --url <your-login-url>` to provide manual authenticated state |
| Frontend build errors | Delete `frontend/node_modules` and re-run `npm install` |
| Port already in use | Kill the existing process or change the port in `launch.sh` / `launch.bat` |
