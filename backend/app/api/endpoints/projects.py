from fastapi import APIRouter
from typing import List, Dict, Any

router = APIRouter(prefix="/projects", tags=["Project Blueprints"])

PROJECT_BLUEPRINTS = [
    {
        "id": 1,
        "title": "InterviewAI — Placement Assessment & Learning Platform",
        "role": "Full-Stack Developer",
        "difficulty": "Advanced",
        "problem_statement": "College students lack personalized, concept-first placement preparation that systematically pinpoints weaknesses, enforces honest retrieval practice, and provides actionable code complexity feedback.",
        "objectives": [
            "Architect a decoupled React + FastAPI system with relational database integrity.",
            "Enforce strict submission locking and prevent duplicate scoring.",
            "Integrate both live AI models and fallback deterministic rubrics.",
            "Implement role-based authorization for students and administrators."
        ],
        "tech_stack": ["React", "TypeScript", "Tailwind CSS", "FastAPI", "SQLAlchemy", "PostgreSQL/SQLite"],
        "main_features": [
            "Learn From Every Answer quiz engine with locked submissions",
            "Code problem sandbox with complexity analysis",
            "Mock technical interview evaluator",
            "Live ATS resume builder with printable export"
        ],
        "milestones": [
            "Milestone 1: Database ER design, Alembic migrations, and JWT auth.",
            "Milestone 2: Practice session state machine and feedback engine.",
            "Milestone 3: Coding practice runner and interview evaluation pipeline.",
            "Milestone 4: Responsive UI with Recharts analytics and accessibility audit."
        ],
        "database_schema": """users (id, email, password_hash, role)
practice_sessions (id, user_id, category, score, status)
session_questions (id, session_id, question_id, submitted_answer, is_correct)
coding_problems (id, title, test_cases_json, time_complexity)
interview_sessions (id, user_id, overall_score, feedback)""",
        "testing_requirements": "Pytest for session locking & duplicate scoring prevention; Vitest for feedback rendering.",
        "github_guidance": "Include clear architecture diagrams in README, clean Git commit messages, CI workflow, and environment templates.",
        "interview_questions": [
            "How did you prevent race conditions or duplicate submissions in the quiz scoring system?",
            "How does your database handle session question ordering and relational cascading?",
            "Why did you choose FastAPI over Flask or Django for this architecture?"
        ]
    },
    {
        "id": 2,
        "title": "Distributed Task Scheduler & Job Queue",
        "role": "Backend / Systems Developer",
        "difficulty": "Intermediate",
        "problem_statement": "Handling asynchronous background operations (email notifications, report generation, video processing) reliably without blocking API worker threads.",
        "objectives": [
            "Build a lightweight worker-queue model with Redis and Python/Go.",
            "Implement exponential backoff retry mechanisms and dead-letter queues.",
            "Design idempotent task execution handlers."
        ],
        "tech_stack": ["Python", "FastAPI", "Redis", "Celery / RQ", "Docker"],
        "main_features": [
            "Delayed execution and recurring cron scheduling",
            "Worker heartbeat monitoring and failure recovery",
            "Web dashboard for real-time queue metrics and retry triggering"
        ],
        "milestones": [
            "Milestone 1: Producer API and Redis list queue integration.",
            "Milestone 2: Worker pool daemon with signal handling (SIGTERM).",
            "Milestone 3: Dead-letter queue and retry backoff logic.",
            "Milestone 4: Metrics export to Prometheus/Grafana."
        ],
        "database_schema": """tasks (id, task_name, payload_json, status, retries, created_at)
worker_nodes (id, hostname, last_heartbeat, status)
task_logs (id, task_id, execution_time_ms, error_message)""",
        "testing_requirements": "Unit tests for retry math; integration tests verifying worker picks tasks off Redis FIFO queue.",
        "github_guidance": "Include a docker-compose.yml file that launches Redis and 2 worker containers with a single command.",
        "interview_questions": [
            "What happens if a worker crashes midway through executing a task? How do you ensure at-least-once delivery?",
            "How do you prevent duplicate task processing (idempotency)?",
            "What is the difference between Redis Lists (LPUSH/RPOP) and Redis Streams?"
        ]
    },
    {
        "id": 3,
        "title": "Real-Time Collaborative Code Editor",
        "role": "Frontend / Full-Stack Developer",
        "difficulty": "Advanced",
        "problem_statement": "Remote technical interviews require simultaneous code editing without overwriting peer inputs or suffering high latency.",
        "objectives": [
            "Implement WebSocket communication for bi-directional state synchronization.",
            "Apply conflict resolution algorithms (Operational Transformation or CRDTs).",
            "Integrate Monaco Editor with multi-cursor indicator support."
        ],
        "tech_stack": ["React", "TypeScript", "WebSockets", "Node.js / FastAPI", "Yjs / Automerge"],
        "main_features": [
            "Multiplayer cursor presence and color coding",
            "Room-based access control and sharable invite links",
            "Syntax highlighting for 10+ programming languages",
            "In-editor chat and session recording replay"
        ],
        "milestones": [
            "Milestone 1: WebSocket server with room connection management.",
            "Milestone 2: Monaco editor binding and local change event listeners.",
            "Milestone 3: CRDT text binding for collision-free concurrent edits.",
            "Milestone 4: Presence awareness (user active positions and labels)."
        ],
        "database_schema": """rooms (id, slug, owner_id, language, created_at)
room_participants (id, room_id, user_name, color_hex, joined_at)
code_snapshots (id, room_id, content, version, saved_at)""",
        "testing_requirements": "Simulate simultaneous WebSocket edits from 3 virtual clients and verify convergence on the exact same string.",
        "github_guidance": "Host a live demo on Vercel/Render, embed a 30-second screen capture gif of live multi-cursor editing in your README.",
        "interview_questions": [
            "Explain how Conflict-Free Replicated Data Types (CRDTs) differ from Operational Transformation (OT).",
            "How do you handle WebSocket connection drops and automatic reconnection without losing local edits?",
            "How did you minimize latency and bandwidth for typing events?"
        ]
    },
    {
        "id": 4,
        "title": "E-Commerce Microservices & Inventory Management",
        "role": "Backend / Cloud Developer",
        "difficulty": "Intermediate",
        "problem_statement": "Flash sale scenarios cause database race conditions, inventory overselling, and cascading service outages in monolithic systems.",
        "objectives": [
            "Decouple Order, Catalog, and Inventory into independent bounded contexts.",
            "Implement optimistic locking or Redis atomic decrements for flash sales.",
            "Handle eventual consistency with Saga pattern or event publishing."
        ],
        "tech_stack": ["Java / Spring Boot or Python FastAPI", "PostgreSQL", "Redis", "Kafka / RabbitMQ", "Docker"],
        "main_features": [
            "Inventory reservation with TTL timeouts",
            "Idempotent order checkout pipeline",
            "Distributed tracing with correlation IDs"
        ],
        "milestones": [
            "Milestone 1: Relational schemas with row versioning for optimistic concurrency.",
            "Milestone 2: Redis atomic decrement (DECRBY) with Lua script verification.",
            "Milestone 3: Order cancellation compensation transaction (Saga).",
            "Milestone 4: Load testing with Locust/k6 demonstrating zero overselling under 1,000 req/sec."
        ],
        "database_schema": """products (id, sku, title, price, stock_quantity, version)
orders (id, user_id, total_amount, status, created_at)
order_items (id, order_id, product_id, quantity, unit_price)
inventory_reservations (id, order_id, product_id, expires_at)""",
        "testing_requirements": "Automated concurrency test asserting stock never drops below 0 when 50 concurrent threads purchase 1 item.",
        "github_guidance": "Include benchmark charts (k6/Locust) showing throughput and p99 latency in your repository documentation.",
        "interview_questions": [
            "How did you prevent dirty reads and lost updates during high-concurrency checkout?",
            "What is the difference between Optimistic Locking and Pessimistic Locking?",
            "How would you handle a payment gateway timeout when the user's card was charged but your webhook was missed?"
        ]
    }
]

@router.get("/")
def get_project_blueprints():
    return PROJECT_BLUEPRINTS

