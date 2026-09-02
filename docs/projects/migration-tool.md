[← Back to profile](../../README.md)

# Large-Scale Document Migration Tool

![Repo](https://img.shields.io/badge/Repo-Private-red?style=for-the-badge&logo=github)
[![Contact Me](https://img.shields.io/badge/Contact%20Me-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/daniel-shalom-13987a1a/)

**A desktop application for bulk-downloading and managing financial documents from web portals.**

<a href="../../assets/sfs-migration-screenshot.png"><img src="../../assets/sfs-migration-screenshot.png" width="100%" /></a>

## Overview

Retrieving fund and investor documents from a web portal one-by-one doesn't scale when you need thousands of them for a migration or archive project. This tool automates that retrieval with Playwright-driven browser downloads, gives you a full file browser over what's been downloaded, and optionally pushes everything to AWS S3 for cloud backup.

## Goals

- Turn a manual, click-through document retrieval process into a bulk, scriptable operation.
- Give the person running the migration a clear view of what's been downloaded, by category, year, and fund.
- Support both local storage and optional cloud (S3) backup without hardcoding either choice.

## Key Features

- **Document download** — retrieve fund/investor documents by category and year, in bulk or targeted to a specific fund.
- **Real-time progress** — visual feedback and notifications during downloads.
- **File management** — a full file browser with smart search (filename, path, category, year), file details, and quick re-download actions.
- **Recursive scanning** — automatically picks up all subfolders.
- **AWS S3 integration** — optional, encrypted-credential cloud backup alongside local storage.
- **Desktop-optimized UI** — a wide, tabbed interface built for this specific workflow rather than a generic file manager.

## Potential Use Cases

- Fund administrators migrating large volumes of investor/fund documents off a legacy portal.
- Compliance/records teams needing a searchable local + cloud archive of financial documents.
- Any team doing a one-time or recurring bulk document retrieval from a web-based document portal.

## How to Use

```bash
# Backend
cd backend
python -m venv .venv && .venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium
uvicorn app.main:app --reload --port 8000

# Frontend
cd frontend
npm install
npm run dev
```

Or on Windows, just run `start.bat` to launch both. Web UI at `http://localhost:5173`, API docs at `http://localhost:8000/docs`.

```bash
# Example: download all fund documents for 2024
curl "http://localhost:8000/api/v1/documents/download/fund/2024"
```

## Tech Stack

FastAPI + Uvicorn backend with Playwright for browser automation and SQLite for local state; React 18 + Vite + TypeScript + Tailwind + Radix UI frontend; optional AWS S3 integration for cloud backup.

---

This is a private repository. [Contact me on LinkedIn](https://www.linkedin.com/in/daniel-shalom-13987a1a/) for a walkthrough or access.

[← Back to profile](../../README.md)
