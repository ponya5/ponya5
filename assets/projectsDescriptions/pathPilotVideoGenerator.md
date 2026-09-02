# PathPilot Tutorial Generator

A professional AI-powered platform that transforms text topics into complete narrated tutorial videos with images, audio, and subtitles.

## ✨ Features

- 🔐 **Google SSO Authentication** - Secure login with permitted user management
- 🤖 **AI Script Generation** - GPT-4 creates structured tutorial scripts
- 🖼️ **Image Generation** - DALL-E 3 and Nano Banana Pro (via OpenRouter) generate relevant visuals
- 🎥 **Motion Generation** - Runway Gen-4 Turbo annotates slides with realistic camera motion
- 🎵 **Voice Synthesis** - ElevenLabs premium voices (8 options) with speed control
- 📝 **Subtitle Generation** - Automatic SRT file creation
- 🎬 **Video Assembly** - Professional video compilation with MoviePy
- 📊 **Real-time Progress** - Track generation across 4 phases
- 🎨 **Modern UI** - Professional interface with PathPilot branding
- 💰 **Cost Tracking** - Real-time cost monitoring for all AI services

## 📋 Prerequisites

### Required Software
- **Python 3.8+** - [Download](https://www.python.org/downloads/)
- **Node.js 18+** - [Download](https://nodejs.org/)
- **FFmpeg** - [Download](https://ffmpeg.org/download.html) (must be in PATH)
  - Windows: Download, extract, add to PATH
  - macOS: `brew install ffmpeg`
  - Linux: `sudo apt-get install ffmpeg`

### Required API Keys
- **Google OAuth Credentials** - [Get here](https://console.cloud.google.com/)
  - Required for user authentication
  - Free to set up
- **OpenAI API Key** - [Get here](https://platform.openai.com/api-keys)
  - Required for script generation (GPT-4) and image generation (DALL-E 3)
  - Pay-as-you-go pricing: ~$0.05-0.10 per video

### Optional API Keys (Recommended)
- **ElevenLabs API Key** - [Get here](https://elevenlabs.io/)
  - Premium voice synthesis (8 voice options)
  - Free tier: 10,000 characters/month
  - Fallback: gTTS (free, lower quality)
- **OpenRouter API Key** - [Get here](https://openrouter.ai/)
  - Alternative image generation (Nano Banana Pro)
  - Free tier available
  - Fallback: DALL-E 3

### Optional API Keys (Advanced Features)
- **RunwayML API Secret** - [Get here](https://runwayml.com/)
  - Gen-4 Turbo video motion from static images
  - ~$0.05 per second of video
  - Fallback: Static images used
- **InstantDB App ID** - [Get here](https://instantdb.com/)
  - Real-time project synchronization
  - Fallback: Local JSON storage


## 🚀 Quick Start

### Windows

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd PathPilot-Tutorial-Generator
   ```

2. **Run automated setup**
   ```bash
   setup.bat
   ```

3. **Configure API keys**
   - Copy `.env.preview` to `.env` in the root directory
   - Edit `.env` with your API keys (see Configuration section below)
   - Add permitted user emails to `backend/db/permitted_users.json`

4. **Start the application**
   ```bash
   start.bat
   ```
   This will open:
   - Backend server at http://localhost:8000
   - Frontend at http://localhost:3000
   - Browser automatically opens to the app

### Linux/macOS

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd PathPilot-Tutorial-Generator
   ```

2. **Run automated setup**
   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```

3. **Configure API keys**
   - Copy `.env.preview` to `.env` in the root directory
   - Edit `.env` with your API keys (see Configuration section below)
   - Add permitted user emails to `backend/db/permitted_users.json`

4. **Start the application**
   ```bash
   # Terminal 1 - Backend
   cd backend
   source venv/bin/activate
   uvicorn main:app --reload

   # Terminal 2 - Frontend
   cd frontend
   npm run dev
   ```
   
5. **Access the application**
   - Open http://localhost:3000
   - Sign in with a permitted Google account

## 📁 Project Structure

```
PathPilot-Tutorial-Generator/
├── backend/                 # FastAPI backend
│   ├── services/           # Core services
│   │   ├── auth.py         # Google OAuth & JWT authentication
│   │   ├── script_gen.py   # GPT-4 script generation
│   │   ├── image_gen.py    # DALL-E 3 / Nano Banana Pro
│   │   ├── tts.py          # ElevenLabs / gTTS audio
│   │   ├── runway_service.py # Runway Gen-4 Turbo video
│   │   ├── video_editor.py # MoviePy video assembly
│   │   ├── subtitle_gen.py # SRT subtitle generation
│   │   ├── billing_tracker.py # Cost tracking
│   │   ├── cost_tracker.py # Usage monitoring
│   │   └── db.py           # State management
│   ├── db/                 # JSON database files
│   │   ├── permitted_users.json
│   │   ├── projects_db.json
│   │   ├── budget_config.json
│   │   └── usage_events.json
│   ├── tests/              # Backend tests
│   ├── utils/              # Utility functions
│   ├── main.py             # API endpoints
│   ├── requirements.txt    # Python dependencies
│   └── .env.example        # Environment template
├── frontend/               # Next.js frontend
│   ├── app/               # Next.js app directory
│   │   ├── page.tsx       # Main application
│   │   ├── login/         # Authentication page
│   │   └── billing/       # Billing dashboard
│   ├── components/        # React components
│   │   ├── AuthGuard.tsx  # Route protection
│   │   ├── Header.tsx     # Navigation & user menu
│   │   ├── InputForm.tsx  # Topic input
│   │   ├── Storyboard.tsx # Slide editor
│   │   ├── ProgressTracker.tsx # Generation progress
│   │   ├── VideoPlayer.tsx # Video playback
│   │   ├── CostTracker.tsx # Cost monitoring
│   │   └── ui/            # Reusable UI components
│   ├── lib/               # Utilities
│   │   ├── auth.ts        # Auth utilities
│   │   ├── db.ts          # InstantDB integration
│   │   └── utils.ts       # Helper functions
│   ├── types/             # TypeScript types
│   ├── public/            # Static files
│   └── package.json       # Node dependencies
├── generated/             # Output videos (gitignored)
│   └── [project-id]/      # Per-project folders
│       ├── audio/         # Generated audio files
│       ├── images/        # Generated images
│       ├── videos/        # Generated video clips
│       ├── uploadedFiles/ # User-uploaded assets
│       ├── final_video.mp4
│       └── subtitles.srt
├── docs/                  # Documentation
│   ├── PROJECT_STRUCTURE.md
│   ├── CLEANUP_SUMMARY_2025.md
│   ├── guides/
│   ├── fixes/
│   └── implementation/
├── assets/                # Branding assets
├── logs/                  # Application logs
├── scripts/               # Utility scripts
├── tools/                 # Development tools
├── .env                   # Environment configuration
├── .env.preview           # Environment template
├── README.md              # This file
├── QUICK_START.md         # Quick start guide
├── setup.bat              # Windows setup
├── setup.sh               # Linux/macOS setup
├── start.bat              # Windows launcher
└── start.ps1              # PowerShell launcher
```

## 🏗️ Technology Stack

### Backend
- **Framework**: FastAPI 0.115.6 (Python async web framework)
- **Server**: Uvicorn 0.34.0 (ASGI server)
- **Authentication**: Google OAuth 2.0 + JWT
- **AI Services**:
  - OpenAI GPT-4 (script generation)
  - OpenAI DALL-E 3 (image generation)
  - OpenRouter Nano Banana Pro (alternative images)
  - ElevenLabs (premium voice synthesis)
  - gTTS (fallback voice synthesis)
  - RunwayML Gen-4 Turbo (video motion)
- **Video Processing**: MoviePy 2.1.1 + FFmpeg
- **Image Processing**: Pillow 11.0.0
- **Database**: JSON file storage
- **Real-time**: WebSockets 14.1

### Frontend
- **Framework**: Next.js 14 (React framework)
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **UI Components**: shadcn/ui
- **State Management**: React hooks
- **Real-time Sync**: InstantDB (optional)
- **Authentication**: Google Sign-In

### Infrastructure
- **Development**: Local (localhost:3000, localhost:8000)
- **Production**: Deployable to Vercel (frontend) + any Python host (backend)
- **Storage**: Local filesystem (generated videos)
- **Logs**: File-based logging (logs/backend.log)

## 🎯 Usage

1. **Enter a topic** - Describe what you want to teach
2. **Review storyboard** - Edit generated slides if needed
3. **Configure settings** - Choose voice, speed, and subtitle options
4. **Watch progress** - Real-time tracking across 4 phases
5. **Download video** - Get your final video with subtitles

## 🔧 Configuration

### Environment Variables (`.env` in root directory)

Create a `.env` file in the project root by copying `.env.preview`:

```bash
# Windows
copy .env.preview .env

# Linux/macOS
cp .env.preview .env
```

Then edit `.env` with your API keys:

```env
# ============================================
# REQUIRED - Authentication
# ============================================
GOOGLE_CLIENT_ID=your-client-id.apps.googleusercontent.com
GOOGLE_CLIENT_SECRET=your-client-secret
NEXT_PUBLIC_GOOGLE_CLIENT_ID=your-client-id.apps.googleusercontent.com
JWT_SECRET=your-secure-random-secret

# ============================================
# REQUIRED - AI Services
# ============================================
OPENAI_API_KEY=sk-your-openai-api-key

# ============================================
# OPTIONAL - AI Services
# ============================================
OPENROUTER_API_KEY=sk-or-v1-your-openrouter-api-key
ELEVENLABS_API_KEY=sk_your-elevenlabs-api-key
RUNWAYML_API_SECRET=your-runwayml-api-secret

# ============================================
# OPTIONAL - Database & Sync
# ============================================
NEXT_PUBLIC_INSTANTDB_APP_ID=your-instantdb-app-id
```

### Detailed Setup Instructions

#### 1. Google OAuth Setup (Required)

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing
3. Enable Google+ API
4. Create OAuth 2.0 credentials:
   - Application type: Web application
   - Authorized JavaScript origins: `http://localhost:3000`
   - Authorized redirect URIs: `http://localhost:3000`, `http://localhost:3000/login`
5. Copy Client ID and Client Secret to `.env`
6. Copy Client ID to `NEXT_PUBLIC_GOOGLE_CLIENT_ID`

#### 2. JWT Secret Generation (Required)

Generate a secure random secret:

```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

Copy the output to `JWT_SECRET` in `.env`

#### 3. OpenAI API Key (Required)

1. Go to [OpenAI Platform](https://platform.openai.com/api-keys)
2. Create new API key
3. Copy to `OPENAI_API_KEY` in `.env`

#### 4. Permitted Users Configuration (Required)

Edit `backend/db/permitted_users.json`:

```json
{
  "permitted_emails": [
    "your-email@gmail.com",
    "team-member@company.com"
  ]
}
```

Only emails in this list can access the application.

#### 5. Optional Services

**ElevenLabs (Premium Voices):**
- Sign up at [elevenlabs.io](https://elevenlabs.io/)
- Get API key from dashboard
- Free tier: 10,000 characters/month
- Fallback: gTTS (free, lower quality)

**OpenRouter (Alternative Image Generation):**
- Sign up at [openrouter.ai](https://openrouter.ai/)
- Get API key from dashboard
- Free tier available for Nano Banana Pro
- Fallback: DALL-E 3

**RunwayML (Video Motion):**
- Sign up at [runwayml.com](https://runwayml.com/)
- Get API secret from dashboard
- Cost: ~$0.05 per second of video
- Fallback: Static images used

**InstantDB (Real-time Sync):**
- Sign up at [instantdb.com](https://instantdb.com/)
- Create app and get App ID
- Fallback: Local JSON storage

### Image Generation Models

The application supports two image generation models:

1. **DALL-E 3** (Default)
   - High-quality image generation from OpenAI
   - Requires: `OPENAI_API_KEY`
   - Cost: ~$0.04 per image

2. **Nano Banana Pro** (via OpenRouter)
   - Alternative image generation model through OpenRouter
   - Requires: `OPENROUTER_API_KEY`
   - Cost: Free tier available
   - Automatic fallback to DALL-E 3 if unavailable

**Sequential vs Parallel Generation:**
- When using the same model for all slides: Parallel generation (faster)
- When using different models (e.g., DALL-E for some slides, Nano Banana for others): Sequential generation (more reliable)
- Visual styles are applied consistently across all slides regardless of model

### Available Voices (ElevenLabs)

When ElevenLabs API key is configured:
- **Rachel** - Female, Calm, Professional
- **Adam** - Male, Deep, Authoritative
- **Domi** - Female, Strong, Confident
- **Elli** - Female, Emotional, Expressive
- **Josh** - Male, Young, Energetic
- **Arnold** - Male, Crisp, Clear
- **Antoni** - Male, Well-Rounded, Versatile
- **Sam** - Male, Raspy, Distinctive

When ElevenLabs is not configured, the system automatically falls back to gTTS (Google Text-to-Speech) which provides basic voice synthesis for free.

### Cost Estimates

**Per Video (Typical 5-slide tutorial):**

| Service | Cost | Required |
|---------|------|----------|
| Script Generation (GPT-4) | ~$0.01 | ✅ Required |
| Images - DALL-E 3 | ~$0.20 (5 × $0.04) | ✅ Required |
| Images - Nano Banana Pro | Free tier | Optional |
| Audio - ElevenLabs | ~$0.005 | Optional |
| Audio - gTTS | Free | Fallback |
| Video Motion - Runway | ~$1.25 (5 × $0.25) | Optional |
| **Total (Minimal)** | **~$0.21** | DALL-E + gTTS |
| **Total (Recommended)** | **~$0.22** | DALL-E + ElevenLabs |
| **Total (Full Features)** | **~$1.46** | All services |

**Monthly Estimates (20 videos):**
- Minimal: ~$4.20/month
- Recommended: ~$4.40/month
- Full Features: ~$29.20/month

## 📊 Progress Phases

1. **Images (0-33%)** - Generating visuals with DALL-E 3 or Nano Banana Pro
2. **Audio (33-66%)** - Creating narration with ElevenLabs/gTTS
3. **Video (66-90%)** - Assembling video with MoviePy
4. **Subtitles (90-100%)** - Generating SRT files

## 🛠️ Manual Installation

If you prefer manual setup:

### Backend

```bash
cd backend
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate

pip install -r requirements.txt
cp .env.example .env
# Edit .env with your API keys
```

### Frontend

```bash
cd frontend
npm install
```

## 🧪 Testing

### Frontend Build Test

The project includes automated build testing to catch syntax and type errors early:

```bash
cd frontend
npm test
```

This runs a full Next.js build to verify:
- ✅ No JSX syntax errors
- ✅ No TypeScript type errors
- ✅ All imports are valid
- ✅ Build completes successfully

### Pre-commit Hook

A Git pre-commit hook is configured to automatically run the build test before each commit:

- Located at: `.git/hooks/pre-commit`
- Runs: `npm run build` in the frontend directory
- Prevents commits if the build fails
- Helps catch errors before they reach the repository

To bypass the hook temporarily (not recommended):
```bash
git commit --no-verify -m "your message"
```

## 📝 API Endpoints

- `POST /generate-script` - Generate tutorial script from topic
- `POST /generate-video` - Start video generation (async)
- `GET /status/{project_id}` - Check generation progress
- `GET /generated/{project_id}/final_video.mp4` - Download video
- `GET /generated/{project_id}/subtitles.srt` - Download subtitles

## 🐛 Troubleshooting

### Installation Issues

**FFmpeg not found:**
```bash
# Windows
# Download from https://ffmpeg.org/, extract, and add to PATH
# Verify: ffmpeg -version

# macOS
brew install ffmpeg

# Linux
sudo apt-get install ffmpeg
```

**Python dependencies fail to install:**
```bash
cd backend
pip install --upgrade pip
pip install -r requirements.txt
```

**Node modules fail to install:**
```bash
cd frontend
npm cache clean --force
npm install
```

### Configuration Issues

**Backend can't find .env file:**
- Ensure `.env` is in the project root (not in `backend/`)
- Check file is named exactly `.env` (not `.env.txt`)
- Verify file has proper line endings (LF, not CRLF)

**Google OAuth not working:**
- Verify `GOOGLE_CLIENT_ID` matches in Google Cloud Console
- Check authorized origins include `http://localhost:3000`
- Wait 5-10 minutes after changing Google Cloud Console settings
- Clear browser cache and cookies

**Can't login / Access denied:**
- Check your email is in `backend/db/permitted_users.json`
- Verify email matches exactly (case-sensitive)
- Check backend logs: `logs/backend.log`

### Runtime Issues

**MoviePy errors:**
```bash
# Verify FFmpeg is installed and in PATH
python -c "from moviepy import *"

# Check FFmpeg version
ffmpeg -version
```

**OpenRouter / Nano Banana Pro not working:**
- Check `OPENROUTER_API_KEY` in `.env`
- System will automatically fallback to DALL-E 3
- Check logs for "OpenRouter not configured" messages
- Verify API key is valid at [openrouter.ai](https://openrouter.ai/)

**ElevenLabs not working:**
- Check API key in `.env`
- Verify you have credits remaining
- System will fallback to gTTS automatically
- Check logs for "ElevenLabs" error messages

**Runway video generation fails:**
- Check `RUNWAYML_API_SECRET` in `.env`
- Verify you have credits remaining
- Check image file exists and is valid
- System will use static images if Runway fails

**Port already in use:**
```bash
# Backend (8000)
# Windows: netstat -ano | findstr :8000
# Linux/Mac: lsof -i :8000

# Frontend (3000)
# Windows: netstat -ano | findstr :3000
# Linux/Mac: lsof -i :3000

# Kill process and restart
```

### Performance Issues

**Video generation is slow:**
- Image generation: 10-30 seconds per image (DALL-E 3)
- Audio generation: 5-10 seconds per slide (ElevenLabs)
- Video assembly: 30-60 seconds (MoviePy)
- Total: 3-5 minutes for a 5-slide video

**Out of memory errors:**
- Close other applications
- Reduce number of slides
- Use lower resolution images (configured in code)

### Debugging

**Check backend logs:**
```bash
# View logs
cat logs/backend.log

# Follow logs in real-time
tail -f logs/backend.log  # Linux/Mac
Get-Content logs/backend.log -Wait  # Windows PowerShell
```

**Check frontend logs:**
- Open browser console (F12)
- Check Network tab for API errors
- Look for red error messages

**Test API directly:**
- Visit http://localhost:8000/docs
- Try individual endpoints
- Check response codes and messages

**Verify setup:**
```bash
.\verify_setup.ps1
```

### Common Error Messages

**"Invalid Google token":**
- Token expired (Google tokens are short-lived)
- Wrong `GOOGLE_CLIENT_ID` in `.env`
- Try logging out and back in

**"Access denied. Email not authorized":**
- Add your email to `backend/db/permitted_users.json`
- Restart backend server

**"OpenAI API key not found":**
- Check `OPENAI_API_KEY` in `.env`
- Verify key starts with `sk-`
- Check key is valid at OpenAI dashboard

**"FFmpeg not found":**
- Install FFmpeg and add to PATH
- Restart terminal/command prompt
- Verify: `ffmpeg -version`

**"Module not found":**
```bash
# Backend
cd backend
pip install <module-name>

# Frontend
cd frontend
npm install <package-name>
```

## 📄 License

MIT License - See LICENSE file for details

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🙏 Acknowledgments

### AI Services
- **OpenAI** - GPT-4 for script generation, DALL-E 3 for image generation
- **OpenRouter** - Access to Nano Banana Pro model
- **Nous Research** - Nano Banana Pro image generation model
- **ElevenLabs** - Premium voice synthesis technology
- **RunwayML** - Gen-4 Turbo video motion generation
- **Google** - Text-to-Speech (gTTS) fallback service

### Frameworks & Libraries
- **FastAPI** - Modern Python web framework
- **Next.js** - React framework for production
- **MoviePy** - Video editing and processing
- **Pillow** - Python image processing
- **shadcn/ui** - Beautiful UI components
- **Tailwind CSS** - Utility-first CSS framework

### Infrastructure
- **Vercel** - Frontend hosting platform
- **InstantDB** - Real-time database synchronization
- **Google Cloud** - OAuth authentication services

### Community
- All contributors and users who provide feedback
- Open source community for amazing tools and libraries

## 📞 Support

- **Documentation**: Check [README.md](README.md) and [docs/](docs/)
- **Quick Start**: See [QUICK_START.md](QUICK_START.md)
- **Issues**: Open an issue on GitHub
- **Logs**: Check `logs/backend.log` for detailed error messages

## 🗺️ Roadmap

### Planned Features
- [ ] Multi-language support (Spanish, French, German, etc.)
- [ ] Custom voice cloning (ElevenLabs)
- [ ] Advanced video transitions and effects
- [ ] Background music integration
- [ ] Batch video generation
- [ ] Video templates and themes
- [ ] LMS integrations (Canvas, Moodle, etc.)
- [ ] Analytics and engagement tracking
- [ ] Team collaboration features
- [ ] API for programmatic access
- [ ] Mobile app (iOS/Android)

### Recent Updates
- ✅ Google SSO authentication
- ✅ Real-time cost tracking
- ✅ Runway Gen-4 Turbo video motion
- ✅ Multiple image generation models
- ✅ Asset upload and management
- ✅ Comprehensive documentation
- ✅ Repository cleanup and organization

## 📊 Project Stats

- **Languages**: Python, TypeScript, JavaScript
- **Backend**: FastAPI + 15+ services
- **Frontend**: Next.js + 20+ components
- **AI Models**: 5+ integrated services
- **Documentation**: 10+ comprehensive guides
- **Tests**: 40+ test files
- **Active Development**: Regular updates and improvements

---

**Made with ❤️ by the PathPilot Team**

*Transform your ideas into professional tutorial videos in minutes!*
