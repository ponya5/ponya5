<div align="center">

# Stash

### Your Social Posts, Organized.

A private, AI-powered bookmark manager for social media. Save links from X, LinkedIn, Instagram, YouTube, TikTok, and more — Stash pulls in the preview, detects the platform, and files every post under the right category automatically.

<img src="src/assets/stash-logo.png" alt="Stash logo" width="120" />

</div>

---

## Why Stash?

Social media moves fast. The good stuff — the thread that broke down a fundraise, the YouTube talk that actually taught you something, the IG reel you swore you'd try later — scrolls past and disappears. Browser bookmarks are a dumping ground. Notes apps lose them. Stash is a quiet, private place to keep the posts worth remembering.

**It's strictly private.** No feeds. No followers. No sharing. No public lists. Your saved posts are visible only to you.

## Features

- **One-tap saving** — Copy a link, open Stash, and it's detected from your clipboard instantly. On Android the clipboard read is automatic; on iOS a gentle tap-to-check pill works around the platform's privacy restrictions.
- **AI categorization** — Each saved post is analyzed with a language model and sorted into Technology, Business, Career Growth, Marketing, Leadership, or Startups, plus a fine-grained sub-category. Posts are categorized in the source language of the content.
- **Smart scraping** — Supabase Edge Functions pull real previews via the FxTwitter API (X), oEmbed (YouTube / TikTok / Instagram), and URL-slug parsing (LinkedIn, which hides content behind a login wall).
- **Custom categories** — Create your own categories and sub-categories. Stash falls back to raw names so edits stay smooth.
- **Search & filter** — Find any post by keyword, platform, category, favorite, reviewed, or archived state. Global search overrides active filters.
- **Triage tools** — Star favorites, mark posts as reviewed, archive the noise. Bulk actions for moving, archiving, and deleting across many posts at once.
- **5-second undo** — Every destructive or move action shows an undo toast, so nothing is ever gone by accident.
- **Installable PWA** — Add Stash to your home screen on iPhone or Android for a native-feeling app. Web Share Target support means you can save a link from any app's share sheet straight into Stash.
- **Dark & light themes** — A minimalist, Apple-like aesthetic with a cyan-accented dark mode.
- **Guided onboarding** — A 3-slide interactive tutorial walks new users through saving their first post, with a highlight that guides them to the Add Post button.

## Tech Stack

| Layer | Technology |
| --- | --- |
| **Frontend** | React 18, TypeScript, Vite 5, Tailwind CSS v3 |
| **UI** | shadcn/ui (Radix primitives), Framer Motion, Lucide icons |
| **Data** | TanStack Query for server state |
| **Backend** | Supabase (Postgres, Auth, Edge Functions, Storage) with Row-Level Security |
| **Auth** | Google OAuth (managed), JWT sessions, server-side role checks |
| **AI** | Lovable AI Gateway (Gemini 2.5 Flash) for categorization |
| **PWA** | Web App Manifest, Web Share Target API, installable on iOS & Android |

## Architecture

```
┌───────────────┐     ┌─────────────────┐     ┌──────────────────┐
│   React SPA    │────▶│  Supabase Auth   │     │  Supabase RLS    │
│  (Vite + TS)   │     │  (Google OAuth)  │     │  (per-user posts) │
└───────┬───────┘     └─────────────────┘     └──────────────────┘
        │
        │ supabase.functions.invoke
        ▼
┌───────────────────────┐     ┌───────────────────────┐
│  Edge Function:        │────▶│  Lovable AI Gateway   │
│  categorize-post       │     │  (Gemini 2.5 Flash)    │
│  (scrape + categorize) │     └───────────────────────┘
└───────┬───────────────┘
        │ FxTwitter API / oEmbed / URL-slug parse
        ▼
   Social platforms (X, YouTube, TikTok, Instagram, LinkedIn)
```

### How a saved post works

1. User pastes a URL (or it's auto-detected from the clipboard).
2. The `categorize-post` Edge Function scrapes a preview using the platform-appropriate method — FxTwitter for X, oEmbed for YouTube/TikTok/Instagram, URL-slug parsing for LinkedIn's login-walled posts.
3. The scraped content is sent to the AI Gateway, which returns a JSON object: platform, content type, category, sub-category, title, excerpt, and author.
4. The result is validated against an allowlist of known categories/sub-categories and inserted into Postgres, protected by per-user RLS policies.

### Security

- **Row-Level Security** on every user table — users can only read and modify their own posts.
- **Server-side admin checks** via a `has_role` security-definer function on a `user_roles` table — admin status is never inferred from client-side storage.
- **JWT validation** in every Edge Function before any database or AI call.
- **Leaked-password protection** enabled on auth.
- **Account deletion** cascades through all user data and clears local `stash_*` storage keys.

## Project Structure

```
src/
├── components/        # UI components (PostCard, AddPostDialog, MobileNav, tutorials…)
├── hooks/             # usePosts, useAuth, useCategories, useClipboardUrl, useIosClipboardNudge…
├── pages/             # Index (dashboard), Auth, ShareHandler, NotFound
├── types/             # Post, Category, Platform type definitions
├── lib/               # utils, device detection, sanitization
└── integrations/      # Supabase client

supabase/
├── functions/
│   ├── categorize-post/        # Scrape + AI categorize a single URL
│   ├── recategorize-all-posts/ # Re-run categorization across a user's library
│   ├── delete-user/            # Account deletion + data cleanup
│   └── refresh-popular-posts/  # Refresh stale previews
└── migrations/                 # Schema, RLS policies, grants, role functions
```

## Getting Started

```sh
# Clone the repo
git clone <YOUR_GIT_URL>
cd stash

# Install dependencies
npm install

# Start the dev server
npm run dev
```

The app expects Supabase environment variables (`VITE_SUPABASE_URL`, `VITE_SUPABASE_PUBLISHABLE_KEY`) and an `LOVABLE_API_KEY` for the AI Gateway in the deployed Edge Functions.

## Live Demo

- **Published app:** [socialstash.me](https://socialstash.me)
- **Lovable preview:** [socialstash.lovable.app](https://socialstash.lovable.app)

## Screenshots

> Add screenshots here: the dashboard in grid view, the mobile install flow, the onboarding tutorial, and the bulk-actions bar.

---

<div align="center">

Built with [Lovable](https://lovable.dev) · React · TypeScript · Supabase · Tailwind CSS

</div>
