from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional
from app.core.database import get_db
from app.models.models import (
    User, Subject, Topic, Lesson, LearningResource, LessonProgress,
    ActivityEvent, utc_now
)
from app.schemas.schemas import LessonDetail, TopicDetail, LearningResourceOut, SubjectOut
from app.api.deps import get_current_user

router = APIRouter(tags=["Learning & Educational Content"])

@router.get("/subjects", response_model=List[SubjectOut])
def get_subjects(db: Session = Depends(get_db)):
    subjects = db.query(Subject).all()
    if not subjects:
        # If subjects table empty, create from distinct topic categories
        topics = db.query(Topic).all()
        categories = list({t.category for t in topics})
        for idx, cat in enumerate(categories):
            subj = Subject(
                name=cat.replace('_', ' ').capitalize(),
                slug=cat,
                description=f"Core curriculum for {cat.replace('_', ' ')} preparation.",
                icon="BookOpen"
            )
            db.add(subj)
        db.commit()
        subjects = db.query(Subject).all()
    return [SubjectOut.model_validate(s) for s in subjects]

@router.get("/topics")
def get_topics(
    category: Optional[str] = None,
    subcategory: Optional[str] = None,
    db: Session = Depends(get_db)
):
    query = db.query(Topic)
    if category:
        query = query.filter(Topic.category == category)
    if subcategory:
        query = query.filter(Topic.subcategory == subcategory)

    topics = query.all()
    out = []
    for t in topics:
        out.append({
            "id": t.id,
            "name": t.name,
            "slug": t.slug,
            "category": t.category,
            "subcategory": t.subcategory,
            "description": t.description,
            "icon": t.icon,
            "lesson_count": len(t.lessons),
            "resource_count": len(t.resources),
            "question_count": len(t.questions),
            "coding_count": len(t.coding_problems)
        })
    return out

@router.get("/lessons")
def get_lessons(
    topic_id: Optional[int] = None,
    db: Session = Depends(get_db)
):
    query = db.query(Lesson).filter(Lesson.is_published == True)
    if topic_id:
        query = query.filter(Lesson.topic_id == topic_id)
    lessons = query.order_by(Lesson.order_index).all()
    return [
        {
            "id": l.id,
            "topic_id": l.topic_id,
            "topic_name": l.topic.name if l.topic else None,
            "title": l.title,
            "slug": l.slug,
            "difficulty": l.difficulty,
            "estimated_minutes": l.estimated_minutes,
            "order_index": l.order_index
        }
        for l in lessons
    ]

@router.get("/lessons/{lesson_id}", response_model=LessonDetail)
def get_lesson(
    lesson_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    lesson = db.query(Lesson).filter(Lesson.id == lesson_id).first()
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found.")

    progress = db.query(LessonProgress).filter(
        LessonProgress.user_id == current_user.id,
        LessonProgress.lesson_id == lesson_id
    ).first()

    resources = [LearningResourceOut.model_validate(r) for r in lesson.topic.resources] if lesson.topic else []

    return LessonDetail(
        id=lesson.id,
        topic_id=lesson.topic_id,
        title=lesson.title,
        slug=lesson.slug,
        difficulty=lesson.difficulty,
        content_markdown=lesson.content_markdown,
        key_takeaways=lesson.key_takeaways,
        estimated_minutes=lesson.estimated_minutes,
        is_completed=bool(progress and progress.status == "completed"),
        resources=resources
    )

@router.put("/lessons/{lesson_id}/progress")
def update_lesson_progress(
    lesson_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    lesson = db.query(Lesson).filter(Lesson.id == lesson_id).first()
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found.")

    progress = db.query(LessonProgress).filter(
        LessonProgress.user_id == current_user.id,
        LessonProgress.lesson_id == lesson_id
    ).first()

    if not progress:
        progress = LessonProgress(
            user_id=current_user.id,
            lesson_id=lesson_id,
            status="completed",
            completed_at=utc_now()
        )
        db.add(progress)

        activity = ActivityEvent(
            user_id=current_user.id,
            event_type="lesson_complete",
            title=f"Completed lesson: {lesson.title}",
            details=f"Topic: {lesson.topic.name if lesson.topic else 'General'}",
            metadata_json={"lesson_id": lesson.id}
        )
        db.add(activity)
        db.commit()

    return {"message": "Lesson progress updated successfully.", "status": "completed", "lesson_id": lesson_id}

@router.get("/resources", response_model=List[LearningResourceOut])
def get_resources(
    topic_id: Optional[int] = None,
    db: Session = Depends(get_db)
):
    query = db.query(LearningResource).filter(LearningResource.is_verified == True)
    if topic_id:
        query = query.filter(LearningResource.topic_id == topic_id)
    resources = query.all()
    return [LearningResourceOut.model_validate(r) for r in resources]

@router.get("/system-design")
def get_system_design_catalog():
    return [
        {
            "id": 1,
            "title": "URL Shortening Service (TinyURL)",
            "difficulty": "Beginner to Intermediate",
            "tagline": "The classic distributed system interview problem testing hashing, caching, and key generation.",
            "requirements": {
                "functional": ["Shorten long URL into unique 7-character code", "Redirect short URL to original destination in <15ms", "Optional custom aliases and link expiration"],
                "non_functional": ["High availability (99.99%)", "Read-heavy ratio (100:1 reads to writes)", "Low latency redirect (<10ms)"]
            },
            "architecture": "Client -> Global CDN / Anycast DNS -> API Gateway & Load Balancer -> Stateless Web Services -> Redis Cluster -> Sharded PostgreSQL / DynamoDB -> Key Generation Service (KGS with Zookeeper).",
            "api_design": [
                {"method": "POST", "path": "/api/v1/urls", "desc": "Generates short URL from destination payload"},
                {"method": "GET", "path": "/{short_code}", "desc": "Redirects with HTTP 302 Found (or 301 Permanent)"}
            ],
            "trade_offs": "Base62 Encoding vs MD5 hash truncation. Using KGS (Key Generation Service) eliminates runtime hash collision checks and ensures instant O(1) writes.",
            "interview_questions": [
                "Why use HTTP 302 redirect instead of HTTP 301 for TinyURL?",
                "How would you prevent database read bottlenecks when a viral tweet causes 100k requests/second?",
                "How does consistent hashing balance cached URLs across 20 Redis nodes?"
            ]
        },
        {
            "id": 2,
            "title": "Real-Time Chat & Messaging Application (WhatsApp / Slack)",
            "difficulty": "Intermediate to Advanced",
            "tagline": "Bi-directional persistent connections, message ordering, and distributed presence detection.",
            "requirements": {
                "functional": ["One-on-one direct messaging", "Group messaging with up to 1,000 members", "Online/Offline presence status", "Read receipts (sent, delivered, read)"],
                "non_functional": ["Real-time delivery (<100ms)", "Zero message loss with persistent storage", "End-to-end encryption support"]
            },
            "architecture": "Mobile/Web Client -> WebSocket Gateway -> Connection Manager (Erlang/Go) -> Apache Kafka Message Broker -> Chat Service -> Cassandra / ScyllaDB (append-only chat history) -> Redis (Presence & PubSub).",
            "api_design": [
                {"method": "WS", "path": "/ws/chat", "desc": "Bi-directional persistent socket for streaming messages"},
                {"method": "GET", "path": "/api/v1/conversations/{id}/messages", "desc": "Paginated historical message retrieval"}
            ],
            "trade_offs": "WebSockets vs Long Polling: WebSockets provide full-duplex communication with lower header overhead. Cassandra is chosen over relational databases because chat is write-heavy and time-series structured.",
            "interview_questions": [
                "How do you ensure message ordering across distributed client clocks?",
                "How does the presence system avoid overwhelming the database with 50 million heartbeats per minute?",
                "What happens to messages when the recipient is offline?"
            ]
        },
        {
            "id": 3,
            "title": "Ride-Hailing Geospatial Matching Engine (Uber / Lyft)",
            "difficulty": "Advanced",
            "tagline": "Geospatial indexing, driver dispatch optimization, and high-frequency location streaming.",
            "requirements": {
                "functional": ["Riders request rides and view nearby drivers", "Drivers broadcast GPS coordinates every 4 seconds", "Ride matching based on ETA and routing"],
                "non_functional": ["Sub-second location queries", "Strong consistency during driver acceptance to prevent duplicate matching", "Fault tolerance during peak surges"]
            },
            "architecture": "Driver GPS -> WebSockets / gRPC -> Location Ingestion Service -> Redis Geospatial / QuadTree / Uber H3 -> Matching Engine -> Dispatch Queue (RabbitMQ) -> MySQL (ACID trip ledger).",
            "api_design": [
                {"method": "POST", "path": "/api/v1/rides/request", "desc": "Rider initiates pickup request"},
                {"method": "POST", "path": "/api/v1/drivers/location", "desc": "Driver streams continuous latitude/longitude telemetry"}
            ],
            "trade_offs": "QuadTree vs Uber H3 Hexagonal Grid. H3 provides equidistant neighbor centroids and consistent cell boundaries across any zoom resolution.",
            "interview_questions": [
                "How does Uber H3 divide Earth into hierarchical hexagons?",
                "How do you prevent two drivers from accepting the exact same ride request simultaneously?",
                "How would you implement dynamic surge pricing based on regional supply/demand density?"
            ]
        },
        {
            "id": 4,
            "title": "Distributed Caching & Invalidation Engine",
            "difficulty": "Intermediate",
            "tagline": "Cache-aside, write-through, write-back patterns, eviction policies (LRU/LFU), and stampede mitigation.",
            "requirements": {
                "functional": ["Store key-value pairs with configurable TTL", "LRU (Least Recently Used) automatic eviction", "Consistent hashing across cache node ring"],
                "non_functional": ["Sub-millisecond retrieval", "High availability with automatic replica failover", "Graceful degradation on cache miss"]
            },
            "architecture": "Application Nodes -> Consistent Hash Ring -> Memcached / Redis Shards -> Replication Group -> Master-Replica with Sentinel failover.",
            "api_design": [
                {"method": "GET", "path": "/cache/{key}", "desc": "Fetches cached entry"},
                {"method": "PUT", "path": "/cache/{key}", "desc": "Stores key with TTL expiration"}
            ],
            "trade_offs": "Cache-Aside vs Write-Through: Cache-aside is resilient to cache failure, while write-through guarantees cache consistency with the database at the cost of higher write latency.",
            "interview_questions": [
                "What is cache stampede (thundering herd) and how do probabilistic early expiration or mutex locks fix it?",
                "How do you implement an O(1) LRU Cache using a Doubly Linked List and HashMap?",
                "How does virtual node replication solve hot-spot imbalance in consistent hashing?"
            ]
        }
    ]

@router.get("/languages")
def get_language_curriculum():
    return [
        {
            "id": "java",
            "name": "Java",
            "icon": "coffee",
            "tagline": "The dominant language for enterprise software engineering and placement coding rounds.",
            "levels": [
                {"name": "Beginner", "topics": ["Syntax & Data Types", "JVM vs JRE vs JDK", "Control Statements", "Methods & Memory Stack"]},
                {"name": "Intermediate", "topics": ["OOP: Encapsulation, Inheritance, Polymorphism, Abstraction", "Exception Handling (Checked vs Unchecked)", "Java Collections Framework (List, Set, Map, PriorityQueue)"]},
                {"name": "Advanced", "topics": ["Generics & Wildcards", "Java 8 Streams API & Lambdas", "Multithreading, Volatile & Synchronized", "Garbage Collection Algorithms & Memory Leaks"]}
            ],
            "common_interview_questions": [
                "Why is String immutable in Java, and how does the String Constant Pool save memory?",
                "What is the difference between Comparable and Comparator interfaces?",
                "How does ConcurrentHashMap achieve thread safety without locking the entire table?",
                "Explain the difference between fail-fast and fail-safe iterators."
            ]
        },
        {
            "id": "python",
            "name": "Python",
            "icon": "code",
            "tagline": "Clean syntax, dynamic typing, and rapid algorithmic implementation for tech interviews.",
            "levels": [
                {"name": "Beginner", "topics": ["Data Types & Dynamic Typing", "List, Tuple, Dict, Set Operations", "List Comprehensions", "Functions & *args / **kwargs"]},
                {"name": "Intermediate", "topics": ["Object-Oriented Programming & Dunder Methods", "Generators & Iterators (yield)", "Decorators & Closures", "Context Managers (with statement)"]},
                {"name": "Advanced", "topics": ["Global Interpreter Lock (GIL) and its implications", "Asyncio & Coroutines", "Metaclasses", "Memory Management & Reference Counting"]}
            ],
            "common_interview_questions": [
                "What is the difference between deepcopy and shallow copy in Python?",
                "How does the Global Interpreter Lock (GIL) affect CPU-bound vs I/O-bound multithreaded programs?",
                "What are generators and how do they optimize memory when processing huge datasets?",
                "Explain the difference between __new__ and __init__."
            ]
        },
        {
            "id": "cpp",
            "name": "C++",
            "icon": "cpu",
            "tagline": "High performance, low-level memory control, and the language of choice for competitive programming.",
            "levels": [
                {"name": "Beginner", "topics": ["Pointers & References", "Stack vs Heap Allocation", "Functions & Header Files", "Structs & Unions"]},
                {"name": "Intermediate", "topics": ["OOP: Virtual Functions & vtable / vptr", "Copy Constructors & Assignment Operator", "Standard Template Library (vector, map, unordered_map, set)"]},
                {"name": "Advanced", "topics": ["Smart Pointers (unique_ptr, shared_ptr, weak_ptr)", "RAII Principle", "Move Semantics & rvalue references", "Templates & Metaprogramming"]}
            ],
            "common_interview_questions": [
                "Why should a base class destructor always be declared virtual?",
                "What is the difference between unique_ptr and shared_ptr, and when would you use weak_ptr to break cyclic references?",
                "How does the vtable (virtual table) mechanism achieve runtime polymorphism?",
                "What are move semantics and how do std::move and rvalue references eliminate deep copies?"
            ]
        },
        {
            "id": "sql",
            "name": "SQL & Relational Databases",
            "icon": "database",
            "tagline": "Essential querying and data modeling skill tested across every technical round.",
            "levels": [
                {"name": "Beginner", "topics": ["SELECT, WHERE, ORDER BY, GROUP BY, HAVING", "Aggregate Functions (COUNT, SUM, AVG, MIN, MAX)", "INNER, LEFT, RIGHT, and FULL OUTER JOINS"]},
                {"name": "Intermediate", "topics": ["Subqueries & Correlated Subqueries", "Window Functions (ROW_NUMBER, RANK, DENSE_RANK)", "Database Normalization (1NF to BCNF)"]},
                {"name": "Advanced", "topics": ["ACID Properties & Transaction Isolation Levels", "B-Tree vs Hash Indexing Internals", "Query Optimization & EXPLAIN ANALYZE", "Database Sharding & Read Replicas"]}
            ],
            "common_interview_questions": [
                "What is the difference between RANK(), DENSE_RANK(), and ROW_NUMBER()?",
                "Write an SQL query to find employees earning more than their managers.",
                "Explain the four transaction isolation levels and the anomalies they prevent (Dirty Read, Non-repeatable Read, Phantom Read).",
                "What is the difference between DELETE, TRUNCATE, and DROP?"
            ]
        }
    ]


