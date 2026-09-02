# AI License Manager

**An internal platform for tracking, requesting, and governing AI tool access across an organization.**

## The problem

As companies adopt more AI tools (Claude, ChatGPT, Copilot, Cursor, and others), license sprawl becomes a real cost and compliance problem: nobody has a single view of who has access to what, how much the company is paying for idle seats, which departments are actually adopting the tools they're paying for, or how fast access requests get resolved. Spend tracking and access decisions end up scattered across spreadsheets, Slack threads, and vendor invoices.

## What it does

AI License Manager centralizes all of that into one dashboard:

- **Dashboard Overview** — real-time view of AI coverage across the org (% of employees with at least one licence), total monthly AI spend, pending requests needing a decision, and rollups by department and tool.
- **License Requests** — a structured request/approval workflow: employees submit a tool + justification, admins approve/deny/confirm access, and every decision is logged with a reviewer and timestamp. Supports bulk import via CSV/Excel.
- **Metrics & Goals (AI Scorecard)** — a quarterly executive scorecard that goes beyond raw counts to answer "is the AI investment working?" It tracks leading and lagging indicators (activation rate, department penetration, adoption depth, cost per adopted user, renewal exposure) and explicitly shows which lever moves which headline metric — plus a built-in "AI Advisor" and data-quality caveats so leadership doesn't over-read noisy numbers.
- **Inventory & Billing** — tracks paid seats, idle/reclaimable spend by tool, and renewal exposure.
- **Users & Departments** — full roster view with license assignment, adoption gaps, deactivated users, and department-level penetration.
- **Activity log** — audit trail of every access change.

## Why it matters

- **Cost control**: surfaces idle seats and reclaimable spend down to the dollar and the specific tool, turning "we probably have some waste" into an actionable list.
- **Governance & compliance**: every access grant has a requester, reviewer, and justification on record — useful for security reviews and audits.
- **Executive visibility**: the AI Scorecard reframes tool adoption as a business metric (ROI, coverage, exposure) instead of a raw usage report, so leadership can make investment decisions instead of guessing.
- **Faster access**: a self-service request flow with clear SLAs on pending decisions, instead of ad hoc Slack DMs to IT.

## Stack & approach

Built as a full-stack internal web application with a dashboard-first UX (card-based KPIs, filterable tables, CSV import/export) and a lightweight "beta" analytics layer (the Scorecard) designed to evolve as data quality improves — the app is transparent about which numbers aren't trustworthy yet rather than presenting false precision.

---

*Screenshots show the app with all data anonymized/fabricated for portfolio purposes.*
