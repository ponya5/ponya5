[← Back to profile](../../README.md)

# PathPilot Tutorial Generator

![Repo](https://img.shields.io/badge/Repo-Private-red?style=for-the-badge&logo=github)

<a href="https://www.linkedin.com/in/daniel-shalom-13987a1a/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" /></a>
<a href="https://github.com/ponya5"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" /></a>
<a href="https://www.daniel-shalom.com"><img src="https://img.shields.io/badge/Website-www.daniel--shalom.com-green?style=for-the-badge&logo=googlechrome&logoColor=white" /></a>
<a href="https://www.instagram.com/daniel.shalom.ai/"><img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" /></a>

**An end-to-end AI video pipeline that turns any topic into a fully produced, narrated tutorial video.**

<a href="../../assets/pathpilot-demo.gif"><img src="../../assets/pathpilot-demo.gif" width="100%" /></a>

## Overview

Producing a professional tutorial video normally means writing a script, sourcing or creating visuals, recording narration, adding subtitles, and editing it all together — hours of work per video. PathPilot Tutorial Generator chains GPT-4 (script), DALL-E 3 / Nano Banana Pro (visuals), Runway Gen-4 Turbo (motion), and ElevenLabs (narration) into a single pipeline, orchestrated through a Next.js review UI, so a topic goes in and a finished MP4 with subtitles comes out.

## Goals

- Collapse the tutorial-video production pipeline (script → visuals → motion → narration → subtitles → final cut) into a single guided flow.
- Let a non-video-editor produce a professional-looking narrated tutorial from just a topic description.
- Keep humans in the loop where it matters — the storyboard is reviewable and editable before final rendering, and every generation phase reports real-time cost.

## Key Features

- **Google SSO authentication** with a permitted-user allowlist.
- **AI script generation** — GPT-4 creates a structured tutorial script from a topic.
- **Image generation** — DALL-E 3 or Nano Banana Pro (via OpenRouter) generate the visuals for each slide.
- **Motion generation** — Runway Gen-4 Turbo adds realistic camera motion to static slides.
- **Voice synthesis** — ElevenLabs premium voices (8 options) with speed control, falling back to gTTS when not configured.
- **Subtitle generation** — automatic SRT file creation.
- **Video assembly** — MoviePy compiles the final video.
- **Real-time progress & cost tracking** — visibility into all 4 generation phases and per-service spend as it happens.

## Potential Use Cases

- Educators and course creators who want to turn written material into narrated video quickly.
- Internal L&D/training teams producing how-to videos at a fraction of normal production time.
- Marketing/dev-rel teams needing quick explainer videos for a feature or topic without a video team.

## How to Use

Enter a topic → review the generated storyboard → configure voice/speed/subtitles → watch progress across the 4 phases → download the finished video.

## Tech Stack

FastAPI backend with Google OAuth + JWT, GPT-4/DALL-E 3/Nano Banana Pro/ElevenLabs/Runway integrations, MoviePy + FFmpeg for video assembly; Next.js 14 + TypeScript + Tailwind + shadcn/ui frontend, optional InstantDB for real-time sync.

---

This is a private repository. Reach out via any of the links above for a walkthrough or access.

[← Back to profile](../../README.md)
