[← Back to profile](../../README.md)

# Social Stash

![Repo](https://img.shields.io/badge/Repo-Private-red?style=for-the-badge&logo=github)
[![Live Demo](https://img.shields.io/badge/Live-socialstash.me-blue?style=for-the-badge&logo=googlechrome&logoColor=white)](https://socialstash.me)

<a href="https://www.linkedin.com/in/daniel-shalom-13987a1a/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" /></a>
<a href="https://github.com/ponya5"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" /></a>
<a href="https://www.daniel-shalom.com"><img src="https://img.shields.io/badge/Website-www.daniel--shalom.com-green?style=for-the-badge&logo=googlechrome&logoColor=white" /></a>
<a href="https://www.instagram.com/daniel.shalom.ai/"><img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" /></a>

**Your social posts, organized. A private, AI-powered bookmark manager for social media.**

<a href="../../assets/socialstash-demo.gif"><img src="../../assets/socialstash-demo.gif" width="100%" /></a>

## Overview

Social media moves fast. The good stuff — the thread that broke down a fundraise, the YouTube talk that actually taught you something, the IG reel you swore you'd try later — scrolls past and disappears. Browser bookmarks turn into a dumping ground and notes apps lose the context. Social Stash is a quiet, private place to save and organize posts across X, LinkedIn, Instagram, YouTube, TikTok, and Facebook, with AI doing the categorization work for you. It's strictly private — no feeds, no followers, no public lists.

## Goals

- Give people one place to reliably re-find valuable social content instead of losing it to the scroll.
- Automate the categorization work (technology, business, career growth, marketing, leadership, startups) so saving is a one-tap action, not a filing chore.
- Keep the whole experience private by design — no social layer at all.

## Key Features

- **One-tap saving** — paste a link and it's detected from your clipboard instantly (automatic on Android, tap-to-check on iOS due to platform restrictions).
- **AI categorization** — each saved post is analyzed by an LLM and sorted into a category and sub-category, in the source language of the content.
- **Smart scraping** — pulls real previews via the FxTwitter API (X), oEmbed (YouTube/TikTok/Instagram), and URL-slug parsing for LinkedIn's login-walled posts.
- **Custom categories** — create your own categories and sub-categories.
- **Search & filter** — by keyword, platform, category, favorite, reviewed, or archived state.
- **Triage tools** — star favorites, mark reviewed, archive noise, bulk move/archive/delete with a 5-second undo on every destructive action.
- **Installable PWA** — add to your home screen on iOS or Android, with Web Share Target support so you can save straight from any app's share sheet.
- **Guided onboarding** — a 3-slide interactive tutorial for new users.

## Potential Use Cases

- Knowledge workers and researchers who save a lot of social content and need to actually find it again later.
- Content creators building a swipe file of reference posts across platforms.
- Anyone who wants a private, ad-free alternative to platform-native bookmarking.

## How to Use

1. Sign in with Google at [socialstash.me](https://socialstash.me).
2. Copy a link from any supported platform, open Social Stash — the URL is detected automatically (or tap the clipboard pill on iOS).
3. The post is scraped, categorized by AI, and filed automatically.
4. Use search, filters, favorites, and archiving to keep your library organized. 1,000+ users are already saving posts this way.

## Tech Stack

React 18 + TypeScript + Vite 5 + Tailwind CSS, shadcn/ui + Framer Motion, TanStack Query, Supabase (Postgres, Auth, Edge Functions, Storage with Row-Level Security), Google OAuth, and the Lovable AI Gateway (Gemini 2.5 Flash) for categorization. Installable as a PWA on iOS and Android.

---

This is a private repository. Reach out via any of the links above for a walkthrough or access. You can try the live app at [socialstash.me](https://socialstash.me).

[← Back to profile](../../README.md)
