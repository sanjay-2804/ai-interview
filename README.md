# InterviewAI — AI-Powered Career & Placement Preparation Platform

> **"Learn Smarter. Practice Better. Get Placement-Ready."**

InterviewAI is a comprehensive, production-oriented full-stack web application designed for college students preparing for campus recruitment drives, coding assessments, aptitude exams, technical interviews, and HR communication rounds.

---

## 1. Complete Application Architecture

The project features a decoupled, professional architecture:

- **Frontend**: Semantic HTML5, responsive modern CSS3, and vanilla JavaScript (Fetch API, Chart.js, Lucide Icons). Completely framework-free for maximum clarity, speed, and ease of inspection in VS Code.
- **Backend**: Python 3.10+ with FastAPI, Pydantic validation schemas, and RESTful endpoints under `/api/v1`.
- **Database**: SQLite for zero-configuration local development; structured with SQLAlchemy ORM and Alembic migrations for seamless PostgreSQL production deployment.
- **Content Banks**:
  - **548 fully validated aptitude questions** across Quantitative (41 topics), Logical Reasoning (24 topics), and Verbal Ability (21 topics).
  - **313 structured coding challenges** categorized across 9 difficulty tiers with multi-language starter code and test cases.
  - **Communication Speaking Studio** with real browser Web Audio / MediaRecorder capture, Web Speech transcription, and a 5-pillar evaluation rubric.

```
InterviewAI/
├── frontend/
│   ├── index.html            # Public landing page with features & FAQ
│   ├── login.html            # Secure student authentication
│   ├── register.html         # Student registration & password hashing
│   ├── career-setup.html     # 16-career personalization wizard
│   ├── dashboard.html        # Real-time statistics, streak, & Chart.js graph
│   ├── roadmap.html          # Dynamic milestone learning roadmaps
│   ├── coding.html           # 310+ coding problems & execution runner
│   ├── aptitude.html         # 540+ questions across 7 learning modes
│   ├── learning.html         # 16 technical CS tracks with lessons
│   ├── communication.html    # Speaking studio with live audio recording
│   ├── interviews.html       # Technical, HR & behavioral mock rounds
│   ├── projects.html         # Curated project blueprints & interview defense
│   ├── resume.html           # ATS resume builder & structured review
│   ├── progress.html         # Analytics, diagnostics, & data export
│   ├── profile.html          # Student preferences & target role settings
│   ├── admin.html            # Protected administrator management centre
│   ├── server.js             # Zero-dependency local web server
│   ├── css/
│   │   └── style.css         # Academic-professional stylesheet
│   ├── js/                   # Modular vanilla JS controllers
│   │   ├── api.js            # Centralized REST API client
│   │   ├── auth.js           # Session and authentication manager
│   │   ├── main.js           # Navigation shell injector
│   │   └── ...               # Page controllers
│   └── assets/
│       └── logo.svg          # Brand identity
├── backend/
│   ├── app/
│   │   ├── main.py           # FastAPI entrypoint & CORS config
│   │   ├── api/              # REST routers under /api/v1
│   │   ├── models/           # SQLAlchemy models
│   │   ├── schemas/          # Pydantic schemas
│   │   ├── services/         # Business logic & evaluators
│   │   └── seeds/            # Repeatable database seed pipelines
│   ├── tests/                # Automated pytest test suite
│   ├── requirements.txt      # Python dependencies
│   └── interviewai.db        # SQLite database
├── .env.example              # Environment variables template
└── README.md
```

---

## 2. Prerequisites & Version Requirements

Ensure the following runtimes are installed on your Windows system:

1. **Python**: Version `3.10` or higher (`python --version`)
2. **Node.js**: Version `18.0` or higher (`node -v`)
3. **VS Code**: Recommended editor

---

## 3. Exact Windows / PowerShell Launch Instructions

To run the complete full-stack website, open two separate PowerShell terminals inside the root project directory:

### Terminal 1 — Backend API (FastAPI)

```powershell
# 1. Navigate to the backend directory
cd backend

# 2. Create and activate a Python virtual environment (if not already created)
python -m venv venv
.\venv\Scripts\Activate.ps1

# If PowerShell script execution is restricted on your machine, run:
# Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

# 3. Install required Python dependencies
pip install -r requirements.txt

# 4. Start the FastAPI server on port 8000
.\venv\Scripts\uvicorn.exe app.main:app --host 127.0.0.1 --port 8000 --reload
```

The backend will start and log:
`Uvicorn running on http://127.0.0.1:8000`

---

### Terminal 2 — Frontend Web Server

```powershell
# 1. Navigate to the frontend directory
cd frontend

# 2. Launch the local static web server on port 3000
node server.js

# Alternative without Node:
# python -m http.server 3000
```

The frontend server will start and log:
`InterviewAI Frontend Server running at http://localhost:3000/`

---

## 4. Open in Your Web Browser

Once both servers are running:

- **Frontend Website**: [http://localhost:3000](http://localhost:3000)
- **Interactive API Documentation (Swagger)**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **API Health Check**: [http://localhost:8000/api/v1/health](http://localhost:8000/api/v1/health)

---

## 5. First-Time Setup & Student User Flow

1. Open [http://localhost:3000](http://localhost:3000) in your browser.
2. Click **Get Started** or navigate to `register.html`.
3. Create an account with your name, college email, and password.
4. Upon registration, you are automatically directed to the **Career Setup Wizard** (`career-setup.html`) to choose from 16 target roles (e.g. *Full-Stack Developer*, *Software Engineer*, *AI/ML Engineer*).
5. Saving preferences unlocks your personalized dashboard (`dashboard.html`), ordered milestones (`roadmap.html`), and practice recommendations.
6. Explore:
   - **Aptitude & Tests** (`aptitude.html`): Choose from 7 learning modes. Notice the strict answer locking, 14-point explanation breakdown, and absence of redo buttons in the same session.
   - **Coding Library** (`coding.html`): Filter through 313 problems, write solutions in Python/JS/Java/C++, and run test evaluations.
   - **Communication Lab** (`communication.html`): Grant microphone permissions, record an audio response, view live transcription, and inspect the 5-pillar rubric scorecard.

---

## 6. Running Automated Tests

To verify backend integrity, security rules, and data persistence:

```powershell
cd backend
.\venv\Scripts\pytest.exe -v
```

All 24 comprehensive test suites will execute and pass:
`======================= 24 passed in 7.39s (100% green) =======================`

---

## 7. Troubleshooting Common Issues

| Issue | Cause | Fix |
| :--- | :--- | :--- |
| `Port 8000 already in use` | Another process is using port 8000 | Run `Get-Process -Id (Get-NetTCPConnection -LocalPort 8000).OwningProcess \| Stop-Process -Force` |
| `Port 3000 already in use` | Another server is using port 3000 | In `frontend/server.js`, change `PORT = 3001` or terminate the conflicting process |
| `CORS error in browser console` | Frontend port not in backend whitelist | `backend/app/main.py` explicitly whitelists `http://localhost:3000`, `http://127.0.0.1:3000`, `http://localhost:5500`, and `http://localhost:5173` |
| `Microphone blocked` in Communication Lab | Browser permission denied | Click the camera/microphone icon in the browser address bar and choose "Allow" |
| `ExecutionPolicy` error in PowerShell | Windows default script restrictions | Run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` before activating venv |

---

## 8. Data Security & Integrity Commitments

- **No Plaintext Passwords**: Passwords hashed securely using bcrypt before storage.
- **Strict Role-Based Authorization**: Administrative operations (`/api/v1/admin/*`) require verified administrator roles on the backend; hiding buttons in the frontend is never relied upon.
- **Data Isolation**: Students cannot access, edit, or delete another student's practice attempts or profiles.
- **No Deceptive Simulations**: Third-party compilers and AI providers have transparent fallbacks that clearly state their operational mode instead of fabricating fake evaluations.
