# Beacon

[![Live Demo](https://img.shields.io/badge/Live%20Demo-beacon--ai.me-blue?style=flat-square)](https://beacon-ai.me)
[![Built with](https://img.shields.io/badge/Built%20with-React%20%7C%20Vite%20%7C%20TypeScript%20%7C%20Tailwind%20CSS%20%7C%20Supabase-6366f1?style=flat-square)](https://beacon-ai.me)

> **Beacon** is a free, open-source event-discovery platform that aggregates technology, AI, and developer events from multiple curated sources into one Hebrew-friendly, easy-to-use dashboard.

---

## What is Beacon?

Beacon helps Israeli tech professionals discover their next conference, meetup, workshop, or webinar without jumping between dozens of websites and newsletters.

The platform automatically scrapes public event pages from trusted sources, normalizes the data, and presents it in a clean list or calendar view. Events are always upcoming — past events are completely purged, so you never waste time on stale listings.

---

## Key Features

### Event Discovery
- **Aggregated feed** of tech, AI, and developer events from multiple curated sources
- **List view** with smart search, filters, and sort options
- **Calendar view** with monthly and free-scroll browsing modes
- **Source logos** shown subtly on every event card for quick brand recognition

### Smart Calendar
- **Monthly calendar** with visual indicators for:
  - Today
  - Selected date
  - Events you're attending
  - Recommended / highlighted events
- **Free-scroll mode** that syncs the calendar indicator with your scroll position
- **One-click date selection** that jumps directly to that day's events

### Personalization
- **Attend / Register** actions on every event card
- **Recommended events** highlighted in bright orange by admins
- **Event type badges** (conference, meetup, webinar, workshop, etc.)
- **Location normalization** — online events and major cities prioritized

### Admin & Automation
- **Admin panel** for managing event sources, monitoring sync health, and marking recommended events
- **Automated scraper** with timeout protection, retry logic, and graceful stop support
- **Manual sync** with real-time progress indication
- **URL validation** that preserves events when sites temporarily block bots

### Design & UX
- **Luxury glass-morphism UI** with a flowing WebGL color-bend background
- **Full Hebrew RTL support** — mirrored layouts and right-to-left text flow
- **Responsive design** optimized for desktop and mobile
- **Onboarding help modal** that opens automatically on first login

---

## Benefits

| For Tech Professionals | For Event Organizers | For Developers |
|---|---|---|
| One place to find all upcoming tech events | Easy path to get events discovered by the community | Open-source architecture to learn from and extend |
| No more stale or past events cluttering the feed | Contact form to submit events for inclusion | Modern React + Supabase + Edge Functions stack |
| Calendar + list views fit different planning styles | Source management dashboard | Automated scraping pipeline with real-world resilience |
| Fast, mobile-friendly Hebrew interface | Sync health monitoring and logs | Security-first with RLS, role-based access, and audits |

---

## Tech Stack

- **Frontend:** React 18, TypeScript, Vite, Tailwind CSS, shadcn/ui
- **Backend / Data:** Supabase (Postgres, Auth, Row Level Security, Edge Functions)
- **Automation:** Supabase Edge Functions, pg_cron scheduling
- **Scraping:** Firecrawl + intelligent fallback scraper
- **AI / Normalization:** OpenAI GPT-4o-mini for location normalization and topic detection
- **Styling:** Custom glass-morphism design system, Heebo font, WebGL animated background

---

## Pages

| Page | Description |
|---|---|
| `/` | Landing page with overview, live stats, and feature highlights |
| `/explore` | Browse, search, and filter all upcoming tech events in list or calendar view |
| `/admin` | Administration panel for sources, sync status, and recommendations |
| `/settings` | User settings |
| `/add-event` | Submit a new event |

---

## Getting Started

> This is a client-side React application. The backend is handled by Supabase (managed service).

### Prerequisites

- Node.js (LTS recommended)
- A Supabase project
- A Firecrawl API key (for scraping)
- An OpenAI API key (for AI normalization)

### Installation

```bash
# 1. Clone the repository
git clone <YOUR_GIT_URL>
cd <YOUR_PROJECT_NAME>

# 2. Install dependencies
npm install

# 3. Start the development server
npm run dev
```

### Environment Variables

Create a `.env` file based on the provided `.env.example`:

```env
VITE_SUPABASE_URL=your_supabase_url
VITE_SUPABASE_ANON_KEY=your_supabase_anon_key
VITE_FIRECRAWL_API_KEY=your_firecrawl_key
VITE_OPENAI_API_KEY=your_openai_key
```

---

## Architecture Overview

```text
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│   React Client  │────▶│  Supabase Auth   │────▶│  Supabase DB    │
│  (Vite + TS)    │     │  + Edge Functions│     │  (RLS secured)  │
└─────────────────┘     └──────────────────┘     └─────────────────┘
                               │
                               ▼
                        ┌──────────────────┐
                        │  Firecrawl / AI  │
                        │  Scraper Pipeline│
                        └──────────────────┘
```

---

## Security

- **Row Level Security (RLS)** on all user-facing tables
- **Role-based admin access** via a separate `user_roles` table
- **Edge function authentication** with admin JWT and scheduler secrets
- **No secrets in client code** — API keys live in Supabase secrets / environment variables
- Regular security scans and dependency checks

---

## Contributing

Contributions are welcome! Whether it's fixing a bug, adding a new event source, improving the UI, or translating content — feel free to open an issue or pull request.

Please keep the code style consistent and ensure the build passes before submitting.

---

## License

This project is open source and available under the [MIT License](LICENSE).

---

## Author

Built and maintained by **Daniel Shalom**.

- Website: [beacon-ai.me](https://beacon-ai.me)
- Support the project: [Buy Me a Coffee ☕](https://ko-fi.com/T6T61VOIV8)

---

*Stay ahead of the curve — never miss your next tech event with Beacon.*
