# SFS - Document Download Tool

A modern desktop application for downloading and managing financial documents. Built with FastAPI backend and React frontend, this professional tool provides document retrieval, file management, and cloud storage integration.

## Features

### 📥 Document Download
- **Document Categories**: Download fund and investor documents by year
- **Bulk Downloads**: Retrieve entire document sets for specific categories
- **Targeted Downloads**: Get documents for specific funds by name
- **Real-time Progress**: Visual feedback with notifications
- **Professional UI**: Clean, intuitive interface optimized for desktop

### 📁 File Management
- **Complete File Browser**: View all downloaded files and folders
- **Smart Search**: Search by filename, path, category, or year
- **Detailed Information**: File size, modification date, full path
- **Quick Actions**: Download files directly from the table
- **Recursive Scanning**: Automatically includes all subfolders
- **Enhanced UI**: Modern table design with hover effects and icons

### ⚙️ Settings
- **Local Storage Configuration**: Set custom download directory
- **AWS S3 Integration**: Optional cloud backup to S3 bucket
- **Secure Credentials**: Encrypted storage of AWS credentials
- **Flexible Options**: Enable/disable cloud backup as needed

### 🎨 User Experience
- **Desktop-Optimized**: Wide layout designed for desktop use (1600px)
- **Tabbed Interface**: Easy navigation between download, files, and settings
- **Modern Design**: Clean, professional interface with gradient backgrounds
- **Responsive Feedback**: Loading states, success/error notifications
- **Accessibility**: Proper labels, ARIA attributes, keyboard navigation

## Installation

### Prerequisites
- **Python 3.8+** - [Download Python](https://www.python.org/downloads/)
- **Node.js 16+** - [Download Node.js](https://nodejs.org/)
- **npm** (comes with Node.js)

### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd <project-directory>
```

### Step 2: Backend Setup

#### Windows
```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium
```

#### macOS/Linux
```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium
```

**Important**: The `playwright install chromium` command downloads the Chromium browser needed for web scraping. This is required for the application to function properly.

### Step 3: Frontend Setup
```bash
cd frontend
npm install
```

### Step 4: Environment Configuration (Optional)
Create a `backend/.env` file if you need custom configuration:
```env
# Add your environment variables here
# Example:
# DOWNLOAD_DIR=./downloads
# LOG_LEVEL=INFO
```

## Running the Application

### Quick Start (Windows)
```bash
start.bat
```
This will start both backend and frontend automatically.

### Manual Start

#### Terminal 1 - Backend
```bash
cd backend
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # macOS/Linux
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

#### Terminal 2 - Frontend
```bash
cd frontend
npm run dev
```

### Access Points
- **Web Interface**: http://localhost:5173
- **API Documentation**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000

## API Usage

### Download Documents by Category
```bash
GET /api/v1/documents/download/{category}/{year}
```
Categories: `fund`, `investor`

Example:
```bash
curl "http://localhost:8000/api/v1/documents/download/fund/2024"
```

### Download Specific Fund Documents
```bash
GET /api/v1/documents/download_fund/{fund_name}/{year}
```

Example:
```bash
curl "http://localhost:8000/api/v1/documents/download_fund/CMT%20II/2024"
```

### Get Document Count
```bash
GET /api/v1/documents/count/{category}/{year}
```

Example:
```bash
curl "http://localhost:8000/api/v1/documents/count/fund/2024"
```

## Project Structure

```
├── assets/                 # Application assets (logos, icons)
├── backend/                # FastAPI backend
│   ├── app/
│   │   ├── api/v1/        # API routes
│   │   ├── core/          # Configuration and logging
│   │   ├── schemas/       # Data models and constants
│   │   └── services/      # Business logic
│   ├── downloads/         # Downloaded documents storage
│   ├── data/              # SQLite database storage
│   ├── .env.example       # Environment variables template
│   └── requirements.txt   # Python dependencies
├── frontend/              # React frontend
│   ├── src/
│   │   ├── components/    # UI components
│   │   └── lib/          # Utilities and API client
│   └── package.json      # Node.js dependencies
├── scripts/               # Utility scripts for setup and testing
├── INSTALL.md            # Quick installation guide
├── README.md             # This file
└── start.bat             # Application launcher (Windows)
```

## Technology Stack

### Backend
- **FastAPI** - Modern Python web framework
- **Uvicorn** - ASGI server
- **Playwright** - Browser automation for web scraping
- **Pydantic** - Data validation
- **SQLite** - Local database for user management
- **Python-dotenv** - Environment configuration

### Frontend
- **React 18** - UI framework
- **Vite** - Build tool and dev server
- **TypeScript** - Type-safe JavaScript
- **Tailwind CSS** - Utility-first CSS framework
- **Radix UI** - Accessible component primitives
- **Lucide React** - Icon library
- **Sonner** - Toast notifications

## Development

### Backend Development
```bash
cd backend
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # macOS/Linux
uvicorn app.main:app --reload
```

The backend will automatically reload when you make changes to the code.

### Frontend Development
```bash
cd frontend
npm run dev
```

Vite provides hot module replacement (HMR) for instant updates during development.

### Testing
```bash
# Frontend tests
cd frontend
npm test

# Frontend tests with coverage
npm run test:coverage
```

## Utility Scripts

The `scripts/` folder contains helpful utilities:
- `setup-everything.bat` - Complete setup (backend + frontend + Playwright)
- `restart-backend.bat` - Restart backend server
- `quick-restart-backend.bat` - Quick backend restart
- `test-backend.bat` - Run backend tests
- `test-setup.bat` - Verify installation
- `verify-setup.py` - Python setup verification script

## Troubleshooting

### Playwright Installation Issues
If `playwright install chromium` fails:
```bash
# Install all browsers
playwright install

# Or install with dependencies (Linux)
playwright install --with-deps chromium

# Or use the provided script (Windows)
scripts\install-playwright.bat
```

### Port Already in Use
If port 8000 or 5173 is already in use:
```bash
# Backend - change port
uvicorn app.main:app --reload --port 8001

# Frontend - Vite will automatically suggest an alternative port
```

### Python Virtual Environment Issues
If you have trouble activating the virtual environment:
```bash
# Windows - try PowerShell
.venv\Scripts\Activate.ps1

# Or use Python directly
python -m venv .venv --clear
```

## Configuration

### Backend Configuration
Create `backend/.env` file (copy from `.env.example`):
```env
# Add your environment variables here
DOWNLOAD_DIR=./downloads
LOG_LEVEL=INFO
```

### Logging
Logs are written to:
- `backend/app.log` - File logging
- Console output - Real-time logging

### Static Files
Downloaded documents are served at `/static/` endpoint and stored in the `backend/downloads/` directory.

## Deployment

### Production Build

#### Frontend
```bash
cd frontend
npm run build
```
The production build will be in `frontend/dist/`.

#### Backend
The backend runs with Uvicorn. For production, consider using:
- **Gunicorn** with Uvicorn workers
- **Docker** containers
- **Systemd** service (Linux)

## License

[Add your license information here]

## Support

For issues and questions, please create an issue in the repository.