from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List, Dict, Any
from app.core.database import get_db
from app.models.models import (
    User, LessonProgress, CodingSubmission, SubmittedAnswer, InterviewSession
)
from app.api.deps import get_current_user

router = APIRouter(tags=["Personal Learning Roadmap"])

def build_stages_for_role(
    role: str,
    lang: str,
    completed_lessons: int,
    solved_coding: int,
    total_attempts: int,
    interviews_completed: int
) -> List[Dict[str, Any]]:
    normalized_role = role.lower()
    
    # 1. FRONTEND DEVELOPER
    if "frontend" in normalized_role or "ui" in normalized_role:
        return [
            {
                "stage_number": 1,
                "title": "Stage 1: HTML5 Semantics, Modern CSS3 & Responsive Layouts",
                "description": "Master semantic elements, CSS Grid, Flexbox, media queries, accessibility (a11y), and responsive mobile-first architecture.",
                "skills": ["HTML5 Semantics", "CSS Grid & Flexbox", "Tailwind CSS", "Responsive Design", "Accessibility"],
                "estimated_hours": 14,
                "status": "completed" if completed_lessons >= 1 else "in_progress",
                "recommended_practice": "/app/technical",
                "is_unlocked": True
            },
            {
                "stage_number": 2,
                "title": "Stage 2: Modern JavaScript (ES6+) & Asynchronous Architecture",
                "description": "Master closures, event loop, Promises, async/await, prototypes, ES modules, and DOM manipulation.",
                "skills": ["ES6+ Syntax", "Promises & Async/Await", "Event Loop", "Closures & Scope", "DOM Manipulation"],
                "estimated_hours": 18,
                "status": "completed" if solved_coding >= 2 else ("in_progress" if completed_lessons >= 1 else "upcoming"),
                "recommended_practice": "/app/coding",
                "is_unlocked": True
            },
            {
                "stage_number": 3,
                "title": "Stage 3: TypeScript Foundations & Type Safety",
                "description": "Interfaces, type aliases, generics, union types, utility types, and integrating TypeScript with modern web apps.",
                "skills": ["Interfaces & Generics", "Type Inference", "Union & Intersection", "Utility Types"],
                "estimated_hours": 15,
                "status": "completed" if solved_coding >= 4 else "upcoming",
                "recommended_practice": "/app/technical",
                "is_unlocked": True
            },
            {
                "stage_number": 4,
                "title": "Stage 4: React 18 Core Architecture & Hooks",
                "description": "Component lifecycle, useState, useEffect, useMemo, useCallback, custom hooks, and virtual DOM diffing.",
                "skills": ["Component Lifecycle", "Custom Hooks", "State Management", "Virtual DOM", "React DevTools"],
                "estimated_hours": 22,
                "status": "upcoming",
                "recommended_practice": "/app/technical",
                "is_unlocked": True
            },
            {
                "stage_number": 5,
                "title": "Stage 5: State Management & Client-Side Routing",
                "description": "Context API, Zustand/Redux Toolkit, React Router 6, protected routes, and navigation patterns.",
                "skills": ["Context API", "Zustand/Redux", "React Router", "Route Guards"],
                "estimated_hours": 16,
                "status": "upcoming",
                "recommended_practice": "/app/technical",
                "is_unlocked": True
            },
            {
                "stage_number": 6,
                "title": "Stage 6: API Integration, REST, Caching & Form Validation",
                "description": "Fetch API, Axios, React Query / TanStack Query, error boundaries, React Hook Form, and Zod validation.",
                "skills": ["RESTful Fetching", "React Query", "React Hook Form", "Zod Validation", "Error Boundaries"],
                "estimated_hours": 18,
                "status": "upcoming",
                "recommended_practice": "/app/technical",
                "is_unlocked": True
            },
            {
                "stage_number": 7,
                "title": "Stage 7: Web Performance, Bundling & Core Web Vitals",
                "description": "Vite bundling, code-splitting, lazy loading, LCP/FID/CLS optimization, and service workers.",
                "skills": ["Vite & Rollup", "Code Splitting", "Core Web Vitals", "Lighthouse Audits"],
                "estimated_hours": 14,
                "status": "upcoming",
                "recommended_practice": "/app/technical",
                "is_unlocked": True
            },
            {
                "stage_number": 8,
                "title": "Stage 8: Problem Solving & Linear Data Structures",
                "description": "Frontend algorithmic interviews: String parsing, Two-pointer techniques, Arrays, and Hash tables.",
                "skills": ["Array Transformations", "String Manipulation", "Two Pointers", "Hash Maps"],
                "estimated_hours": 18,
                "status": "upcoming",
                "recommended_practice": "/app/coding",
                "is_unlocked": True
            },
            {
                "stage_number": 9,
                "title": "Stage 9: Capstone Frontend Projects & Git Workflow",
                "description": "Build high-impact production web applications featuring interactive dashboards and clean UI component libraries.",
                "skills": ["Git Branching", "Component Library", "Production Deployment", "Vercel / Netlify"],
                "estimated_hours": 25,
                "status": "upcoming",
                "recommended_practice": "/app/resume",
                "is_unlocked": True
            },
            {
                "stage_number": 10,
                "title": "Stage 10: Quantitative Aptitude & Placement Reasoning",
                "description": "Percentages, Profit/Loss, Time & Work, Speed/Distance, and logical reasoning for campus placement tests.",
                "skills": ["Quantitative Aptitude", "Logical Reasoning", "Speed & Accuracy"],
                "estimated_hours": 16,
                "status": "completed" if total_attempts >= 5 else "upcoming",
                "recommended_practice": "/app/aptitude",
                "is_unlocked": True
            },
            {
                "stage_number": 11,
                "title": "Stage 11: Frontend Machine Coding & UI Live Interview",
                "description": "Live coding UI components under time pressure: Autocomplete, Infinite Scroll, Kanban Board, and Modal systems.",
                "skills": ["Machine Coding", "Component Design", "State Architecture", "Live Explanation"],
                "estimated_hours": 15,
                "status": "completed" if interviews_completed >= 1 else "upcoming",
                "recommended_practice": "/app/interview",
                "is_unlocked": True
            },
            {
                "stage_number": 12,
                "title": "Stage 12: Behavioral HR & STAR Storytelling",
                "description": "Articulate UI project challenges, cross-functional collaboration with designers and backend teams.",
                "skills": ["STAR Framework", "Project Articulation", "Cross-functional Collaboration"],
                "estimated_hours": 10,
                "status": "upcoming",
                "recommended_practice": "/app/communication",
                "is_unlocked": True
            },
            {
                "stage_number": 13,
                "title": "Stage 13: ATS-Optimized Frontend Resume & Portfolio",
                "description": "Quantify UI impact (reduced load time by 40%, built responsive components) and format single-page ATS resume.",
                "skills": ["ATS Optimization", "Action Verb Phrasing", "Live Demo Hosting", "Portfolio Verification"],
                "estimated_hours": 8,
                "status": "upcoming",
                "recommended_practice": "/app/resume",
                "is_unlocked": True
            }
        ]

    # 2. BACKEND DEVELOPER
    elif "backend" in normalized_role:
        return [
            {
                "stage_number": 1,
                "title": f"Stage 1: {lang} Advanced Syntax & Concurrency",
                "description": f"Master asynchronous I/O, OOP, memory management, closures, generators, and exception handling in {lang}.",
                "skills": [f"{lang} Core", "Async / Await", "OOP & Design Patterns", "Memory & Threading"],
                "estimated_hours": 15,
                "status": "completed" if completed_lessons >= 1 else "in_progress",
                "recommended_practice": "/app/technical",
                "is_unlocked": True
            },
            {
                "stage_number": 2,
                "title": "Stage 2: Relational Databases, Normalization & SQL",
                "description": "PostgreSQL & SQLite: 1NF to BCNF normalization, ACID transactions, B-Tree indexes, and complex JOIN queries.",
                "skills": ["SQL Queries", "JOINs & Subqueries", "Normalization", "B-Tree Indexing", "ACID Transactions"],
                "estimated_hours": 18,
                "status": "completed" if solved_coding >= 2 else ("in_progress" if completed_lessons >= 1 else "upcoming"),
                "recommended_practice": "/app/technical",
                "is_unlocked": True
            },
            {
                "stage_number": 3,
                "title": "Stage 3: RESTful API Architecture & Authentication",
                "description": "REST principles, OpenAPI/Swagger specifications, JWT authentication, HttpOnly cookies, and role-based access control.",
                "skills": ["RESTful Standards", "FastAPI / Node / Spring", "JWT & Sessions", "RBAC Security"],
                "estimated_hours": 20,
                "status": "completed" if solved_coding >= 4 else "upcoming",
                "recommended_practice": "/app/technical",
                "is_unlocked": True
            },
            {
                "stage_number": 4,
                "title": "Stage 4: Data Structures & Algorithmic Optimization",
                "description": "Arrays, HashMaps, Trees, Graphs, Stacks, Queues, and Priority Queues with time & space complexity.",
                "skills": ["Data Structures", "Big-O Analysis", "HashMaps", "Binary Trees", "Graphs"],
                "estimated_hours": 22,
                "status": "upcoming",
                "recommended_practice": "/app/coding",
                "is_unlocked": True
            },
            {
                "stage_number": 5,
                "title": "Stage 5: Caching Strategies & Key-Value Stores",
                "description": "In-memory caching with Redis, Cache-Aside, Write-Through, cache invalidation, and rate limiting.",
                "skills": ["Redis Caching", "Cache Invalidation", "Rate Limiting", "Connection Pooling"],
                "estimated_hours": 14,
                "status": "upcoming",
                "recommended_practice": "/app/technical",
                "is_unlocked": True
            },
            {
                "stage_number": 6,
                "title": "Stage 6: Operating Systems, Virtual Memory & Concurrency",
                "description": "Processes vs threads, CPU scheduling, race conditions, deadlocks, virtual memory, and inter-process communication.",
                "skills": ["Process Management", "Concurrency & Locks", "Virtual Memory", "Deadlocks"],
                "estimated_hours": 16,
                "status": "upcoming",
                "recommended_practice": "/app/technical",
                "is_unlocked": True
            },
            {
                "stage_number": 7,
                "title": "Stage 7: Computer Networks, Sockets & Protocols",
                "description": "TCP/IP 3-way handshake, UDP, HTTP/2 & HTTP/3, WebSockets, DNS, and TLS handshake security.",
                "skills": ["TCP vs UDP", "HTTP Protocols", "TLS/SSL", "DNS Resolution", "WebSockets"],
                "estimated_hours": 15,
                "status": "upcoming",
                "recommended_practice": "/app/technical",
                "is_unlocked": True
            },
            {
                "stage_number": 8,
                "title": "Stage 8: System Design & Scalable Microservices",
                "description": "Load balancers, database sharding, replication, horizontal scaling, message queues, and API gateways.",
                "skills": ["Load Balancing", "Database Sharding", "Message Queues", "CAP Theorem", "Microservices"],
                "estimated_hours": 24,
                "status": "upcoming",
                "recommended_practice": "/app/technical",
                "is_unlocked": True
            },
            {
                "stage_number": 9,
                "title": "Stage 9: Production Capstone Projects & Containerization",
                "description": "Build high-throughput backend services with Docker, automated unit tests (Pytest), and CI/CD pipelines.",
                "skills": ["Docker", "Pytest Suite", "CI/CD Actions", "Database Migrations"],
                "estimated_hours": 25,
                "status": "upcoming",
                "recommended_practice": "/app/resume",
                "is_unlocked": True
            },
            {
                "stage_number": 10,
                "title": "Stage 10: Quantitative Aptitude & Numerical Reasoning",
                "description": "Campus assessment round: Arithmetic, Algebra, Permutations, Probability, and Syllogisms.",
                "skills": ["Percentages", "Probability", "Time-Speed-Distance", "Permutations"],
                "estimated_hours": 16,
                "status": "completed" if total_attempts >= 5 else "upcoming",
                "recommended_practice": "/app/aptitude",
                "is_unlocked": True
            },
            {
                "stage_number": 11,
                "title": "Stage 11: Backend Live Coding & System Design Interviews",
                "description": "Live problem solving, API schema design, query optimization, and latency reduction defenses.",
                "skills": ["Live API Design", "Query Optimization", "System Architecture Defense"],
                "estimated_hours": 15,
                "status": "completed" if interviews_completed >= 1 else "upcoming",
                "recommended_practice": "/app/interview",
                "is_unlocked": True
            },
            {
                "stage_number": 12,
                "title": "Stage 12: Behavioral & Technical Communication Lab",
                "description": "STAR behavioral responses highlighting root cause analysis, resolving production outages, and team consensus.",
                "skills": ["STAR Technique", "Incident Post-Mortems", "Technical Ownership"],
                "estimated_hours": 10,
                "status": "upcoming",
                "recommended_practice": "/app/communication",
                "is_unlocked": True
            },
            {
                "stage_number": 13,
                "title": "Stage 13: ATS-Optimized Backend Resume & Deployment",
                "description": "Quantify backend wins (e.g. 35% latency drop, 99.9% uptime, 100% test coverage) and pass ATS scans.",
                "skills": ["ATS Verification", "Measurable Metrics", "GitHub Portfolio", "Production Links"],
                "estimated_hours": 8,
                "status": "upcoming",
                "recommended_practice": "/app/resume",
                "is_unlocked": True
            }
        ]

    # 3. DATA ANALYST / BI
    elif "data" in normalized_role or "analyst" in normalized_role or "bi" in normalized_role:
        return [
            {
                "stage_number": 1,
                "title": "Stage 1: Advanced Relational SQL for Data Analytics",
                "description": "Master Window functions (ROW_NUMBER, DENSE_RANK, LEAD, LAG), Common Table Expressions (CTEs), and aggregation.",
                "skills": ["Window Functions", "CTEs", "Subqueries", "GROUP BY & HAVING", "Complex JOINs"],
                "estimated_hours": 16,
                "status": "completed" if completed_lessons >= 1 else "in_progress",
                "recommended_practice": "/app/technical",
                "is_unlocked": True
            },
            {
                "stage_number": 2,
                "title": "Stage 2: Python for Data Science (NumPy & Pandas)",
                "description": "DataFrames, indexing, filtering, vectorized operations, series manipulation, and data transformation.",
                "skills": ["Pandas DataFrames", "NumPy Arrays", "Vectorization", "Data Aggregation"],
                "estimated_hours": 18,
                "status": "completed" if solved_coding >= 2 else ("in_progress" if completed_lessons >= 1 else "upcoming"),
                "recommended_practice": "/app/coding",
                "is_unlocked": True
            },
            {
                "stage_number": 3,
                "title": "Stage 3: Data Cleaning, Imputation & ETL Pipelines",
                "description": "Handling missing values, outlier detection, data normalization, regex text cleaning, and automated data pipelines.",
                "skills": ["Missing Value Imputation", "Outlier Detection", "Regex Text Cleaning", "ETL Pipelines"],
                "estimated_hours": 15,
                "status": "completed" if solved_coding >= 4 else "upcoming",
                "recommended_practice": "/app/technical",
                "is_unlocked": True
            },
            {
                "stage_number": 4,
                "title": "Stage 4: Statistical Analysis, Probability & Hypothesis Testing",
                "description": "Mean/Median/Mode, Standard Deviation, Normal Distributions, Confidence Intervals, Z-tests, and T-tests.",
                "skills": ["Descriptive Statistics", "Probability Distributions", "Hypothesis Testing", "A/B Testing Basics"],
                "estimated_hours": 18,
                "status": "upcoming",
                "recommended_practice": "/app/aptitude",
                "is_unlocked": True
            },
            {
                "stage_number": 5,
                "title": "Stage 5: Data Visualization & Dashboard Storytelling",
                "description": "Transform raw query outputs into actionable visual insights using charts, heatmaps, and dashboarding.",
                "skills": ["Data Storytelling", "KPI Dashboarding", "Cohort Analysis", "Bar/Line/Scatter Charts"],
                "estimated_hours": 15,
                "status": "upcoming",
                "recommended_practice": "/app/technical",
                "is_unlocked": True
            },
            {
                "stage_number": 6,
                "title": "Stage 6: Relational Schemas & Analytical Data Warehousing",
                "description": "Star schemas, snowflake schemas, dimensional modeling, OLTP vs OLAP, and analytical query execution.",
                "skills": ["Dimensional Modeling", "Star Schema", "OLAP vs OLTP", "Data Marts"],
                "estimated_hours": 14,
                "status": "upcoming",
                "recommended_practice": "/app/technical",
                "is_unlocked": True
            },
            {
                "stage_number": 7,
                "title": "Stage 7: Business Problem Solving & Root Cause Case Studies",
                "description": "Analyze churn rates, customer acquisition cost (CAC), revenue cohorts, and diagnostic placement scenarios.",
                "skills": ["Root Cause Analysis", "Cohort Retention", "Funnel Metrics", "Business Acumen"],
                "estimated_hours": 15,
                "status": "upcoming",
                "recommended_practice": "/app/technical",
                "is_unlocked": True
            },
            {
                "stage_number": 8,
                "title": "Stage 8: Quantitative Aptitude & Data Interpretation",
                "description": "Bar charts, pie charts, tabular analysis, percentages, ratios, and timed logical placement tests.",
                "skills": ["Data Interpretation", "Percentages & Ratios", "Logical Deduction", "Speed Drills"],
                "estimated_hours": 16,
                "status": "completed" if total_attempts >= 5 else "upcoming",
                "recommended_practice": "/app/aptitude",
                "is_unlocked": True
            },
            {
                "stage_number": 9,
                "title": "Stage 9: Capstone Analytical Projects & GitHub Showcase",
                "description": "Publish complete data case studies with reproducible notebooks, clean schemas, and business insights.",
                "skills": ["Jupyter Notebooks", "Clean Data Schemas", "Executive Summaries", "GitHub Portfolio"],
                "estimated_hours": 20,
                "status": "upcoming",
                "recommended_practice": "/app/resume",
                "is_unlocked": True
            },
            {
                "stage_number": 10,
                "title": "Stage 10: Technical SQL & Case Study Mock Interviews",
                "description": "Solve live multi-table SQL queries, explain trade-offs, and defend analytical assumptions.",
                "skills": ["Live SQL Coding", "Case Study Walkthrough", "Analytical Communication"],
                "estimated_hours": 14,
                "status": "completed" if interviews_completed >= 1 else "upcoming",
                "recommended_practice": "/app/interview",
                "is_unlocked": True
            },
            {
                "stage_number": 11,
                "title": "Stage 11: HR Behavioral & Stakeholder Communication",
                "description": "Communicate complex data insights to non-technical stakeholders using the STAR framework.",
                "skills": ["STAR Framework", "Stakeholder Communication", "Influence Without Authority"],
                "estimated_hours": 10,
                "status": "upcoming",
                "recommended_practice": "/app/communication",
                "is_unlocked": True
            },
            {
                "stage_number": 12,
                "title": "Stage 12: ATS-Optimized Data Analyst Resume",
                "description": "Highlight business value (e.g. identified $50k cost leakage, built SQL models) formatted for ATS engines.",
                "skills": ["ATS Keyword Matching", "Action Verbs", "Quantified ROI", "Portfolio Links"],
                "estimated_hours": 8,
                "status": "upcoming",
                "recommended_practice": "/app/resume",
                "is_unlocked": True
            }
        ]

    # 4. QA & TEST AUTOMATION
    elif "qa" in normalized_role or "test" in normalized_role:
        return [
            {
                "stage_number": 1,
                "title": "Stage 1: Software Testing Fundamentals & Test Case Design",
                "description": "Black-box, white-box, boundary value analysis, equivalence partitioning, defect life cycles, and test plans.",
                "skills": ["Test Case Design", "Boundary Value Analysis", "Defect Life Cycle", "Severity vs Priority"],
                "estimated_hours": 14,
                "status": "completed" if completed_lessons >= 1 else "in_progress",
                "recommended_practice": "/app/technical",
                "is_unlocked": True
            },
            {
                "stage_number": 2,
                "title": f"Stage 2: {lang} Programming for Automation Engineers",
                "description": f"Master OOP, strings, collections, file I/O, regex, and assertions in {lang}.",
                "skills": [f"{lang} Fundamentals", "Collections", "OOP Principles", "Exception Handling"],
                "estimated_hours": 16,
                "status": "completed" if solved_coding >= 2 else ("in_progress" if completed_lessons >= 1 else "upcoming"),
                "recommended_practice": "/app/coding",
                "is_unlocked": True
            },
            {
                "stage_number": 3,
                "title": "Stage 3: Automated Testing Frameworks (Pytest / Vitest)",
                "description": "Fixtures, parameterization, mock objects, test runners, coverage reports, and failure reporting.",
                "skills": ["Pytest / Vitest", "Test Fixtures", "Parametric Tests", "Code Coverage Reports"],
                "estimated_hours": 16,
                "status": "completed" if solved_coding >= 4 else "upcoming",
                "recommended_practice": "/app/technical",
                "is_unlocked": True
            },
            {
                "stage_number": 4,
                "title": "Stage 4: Web UI Automation with Playwright & Selenium",
                "description": "Page Object Model (POM), element selectors, handling dynamic waits, alerts, iframes, and cross-browser testing.",
                "skills": ["Playwright", "Page Object Model", "Dynamic Waits & Selectors", "Cross-browser Suites"],
                "estimated_hours": 20,
                "status": "upcoming",
                "recommended_practice": "/app/technical",
                "is_unlocked": True
            },
            {
                "stage_number": 5,
                "title": "Stage 5: API Automation & Contract Testing",
                "description": "Automating REST API checks with requests/supertest: Status codes, JSON schema validation, auth headers, and response latency.",
                "skills": ["REST API Testing", "JSON Schema Validation", "Postman Collections", "Auth Token Testing"],
                "estimated_hours": 16,
                "status": "upcoming",
                "recommended_practice": "/app/technical",
                "is_unlocked": True
            },
            {
                "stage_number": 6,
                "title": "Stage 6: SQL & Database Validation for QA",
                "description": "Verify database state changes following API or UI operations using SQL assertions and rollback tests.",
                "skills": ["SQL Assertions", "Data Integrity Verification", "Database Rollbacks"],
                "estimated_hours": 14,
                "status": "upcoming",
                "recommended_practice": "/app/technical",
                "is_unlocked": True
            },
            {
                "stage_number": 7,
                "title": "Stage 7: CI/CD Test Pipeline Integration",
                "description": "Run automated test suites on pull requests using GitHub Actions, generate HTML test reports, and alert on regression.",
                "skills": ["GitHub Actions", "Regression Suites", "Automated Artifact Reports"],
                "estimated_hours": 15,
                "status": "upcoming",
                "recommended_practice": "/app/technical",
                "is_unlocked": True
            },
            {
                "stage_number": 8,
                "title": "Stage 8: Quantitative Aptitude & Placement Reasoning",
                "description": "Logical reasoning, puzzles, percentages, series, and timed assessment drills.",
                "skills": ["Quantitative Aptitude", "Logical Reasoning", "Speed Drills"],
                "estimated_hours": 16,
                "status": "completed" if total_attempts >= 5 else "upcoming",
                "recommended_practice": "/app/aptitude",
                "is_unlocked": True
            },
            {
                "stage_number": 9,
                "title": "Stage 9: Capstone Test Automation Suite Project",
                "description": "Build an open-source test suite demonstrating automated E2E and API regression coverage with Dockerized runners.",
                "skills": ["End-to-End Suite", "Dockerized Test Runner", "Reporting Dashboard"],
                "estimated_hours": 20,
                "status": "upcoming",
                "recommended_practice": "/app/resume",
                "is_unlocked": True
            },
            {
                "stage_number": 10,
                "title": "Stage 10: Technical SDET & QA Mock Interviews",
                "description": "Live test scenario generation, edge case identification, bug reproduction steps, and automation architecture.",
                "skills": ["Edge Case Identification", "Bug Triage", "Automation Architecture Defense"],
                "estimated_hours": 14,
                "status": "completed" if interviews_completed >= 1 else "upcoming",
                "recommended_practice": "/app/interview",
                "is_unlocked": True
            },
            {
                "stage_number": 11,
                "title": "Stage 11: Behavioral HR & Quality Advocacy",
                "description": "Communicating quality blockers, collaborating with developers, and resolving release deadlines using STAR.",
                "skills": ["STAR Framework", "Quality Advocacy", "Collaborative Triage"],
                "estimated_hours": 10,
                "status": "upcoming",
                "recommended_practice": "/app/communication",
                "is_unlocked": True
            },
            {
                "stage_number": 12,
                "title": "Stage 12: ATS-Optimized SDET Resume & Job Search",
                "description": "Highlight test coverage percentage, regression time saved, and automated suites on single-page ATS resume.",
                "skills": ["ATS Optimization", "Test Automation Metrics", "GitHub Portfolio"],
                "estimated_hours": 8,
                "status": "upcoming",
                "recommended_practice": "/app/resume",
                "is_unlocked": True
            }
        ]

    # 5. GENERALIST SOFTWARE DEVELOPER / FULL-STACK (Default Gold Standard)
    else:
        return [
            {
                "stage_number": 1,
                "title": f"Stage 1: {lang} Programming Fundamentals",
                "description": f"Master core syntax, variables, data types, control structures, functions, and memory basics in {lang}.",
                "skills": [f"{lang} Syntax", "Control Flow", "Functions", "Scope & Memory"],
                "estimated_hours": 12,
                "status": "completed" if completed_lessons >= 1 else "in_progress",
                "recommended_practice": "/app/technical",
                "is_unlocked": True
            },
            {
                "stage_number": 2,
                "title": "Stage 2: Problem-Solving & Linear Data Structures",
                "description": "Deep dive into Arrays, Strings, Linked Lists, Stacks, and Queues with time & space complexity analysis.",
                "skills": ["Arrays", "Strings", "Linked Lists", "Stacks & Queues", "Big-O Notation"],
                "estimated_hours": 18,
                "status": "completed" if solved_coding >= 2 else ("in_progress" if completed_lessons >= 1 else "upcoming"),
                "recommended_practice": "/app/coding",
                "is_unlocked": True
            },
            {
                "stage_number": 3,
                "title": "Stage 3: Core Algorithms & Searching/Sorting",
                "description": "Binary search, two-pointer techniques, sliding windows, recursion, QuickSort, and MergeSort.",
                "skills": ["Binary Search", "Two Pointers", "Sliding Window", "MergeSort", "QuickSort"],
                "estimated_hours": 20,
                "status": "completed" if solved_coding >= 4 else "upcoming",
                "recommended_practice": "/app/coding",
                "is_unlocked": True
            },
            {
                "stage_number": 4,
                "title": "Stage 4: Object-Oriented Programming (OOP)",
                "description": "Encapsulation, Inheritance, Polymorphism, Abstraction, SOLID principles, and common design patterns.",
                "skills": ["Encapsulation", "Inheritance", "Polymorphism", "SOLID Principles", "Design Patterns"],
                "estimated_hours": 14,
                "status": "upcoming",
                "recommended_practice": "/app/technical",
                "is_unlocked": True
            },
            {
                "stage_number": 5,
                "title": "Stage 5: DBMS, SQL & Relational Schema Design",
                "description": "Relational schemas, normalization (1NF-BCNF), indexing with B-Trees, transactions, ACID properties, and complex JOINs.",
                "skills": ["SQL Queries", "JOINs", "Normalization", "Indexing", "ACID Transactions"],
                "estimated_hours": 16,
                "status": "upcoming",
                "recommended_practice": "/app/technical",
                "is_unlocked": True
            },
            {
                "stage_number": 6,
                "title": "Stage 6: Operating Systems & Concurrency",
                "description": "Processes vs threads, CPU scheduling algorithms, deadlocks, virtual memory, paging, and inter-process communication.",
                "skills": ["Processes & Threads", "CPU Scheduling", "Deadlocks", "Virtual Memory", "Paging"],
                "estimated_hours": 15,
                "status": "upcoming",
                "recommended_practice": "/app/technical",
                "is_unlocked": True
            },
            {
                "stage_number": 7,
                "title": "Stage 7: Computer Networks & Protocols",
                "description": "OSI 7-layer model, TCP/IP, 3-way handshakes, UDP, HTTP/HTTPS, DNS resolution, and REST architecture.",
                "skills": ["OSI Model", "TCP vs UDP", "HTTP/HTTPS", "DNS & Routing", "REST Fundamentals"],
                "estimated_hours": 14,
                "status": "upcoming",
                "recommended_practice": "/app/technical",
                "is_unlocked": True
            },
            {
                "stage_number": 8,
                "title": "Stage 8: Web Development Fundamentals & APIs",
                "description": "Client-server architecture, modern JavaScript/TypeScript, React state management, and backend RESTful endpoints.",
                "skills": ["React/Frontend", "Node/FastAPI Backend", "RESTful APIs", "Authentication/JWT"],
                "estimated_hours": 20,
                "status": "upcoming",
                "recommended_practice": "/app/technical",
                "is_unlocked": True
            },
            {
                "stage_number": 9,
                "title": "Stage 9: Production Projects & Git Version Control",
                "description": "Build 2 full-stack projects showcasing clean database architecture, automated tests, and deployment on cloud platforms.",
                "skills": ["Git Branching", "Full-Stack Project", "Database Migrations", "API Documentation"],
                "estimated_hours": 25,
                "status": "upcoming",
                "recommended_practice": "/app/resume",
                "is_unlocked": True
            },
            {
                "stage_number": 10,
                "title": "Stage 10: Quantitative Aptitude & Logical Assessment",
                "description": "Timed placement assessments: Percentages, Profit/Loss, Time & Work, Speed/Distance, Syllogisms, and Puzzles.",
                "skills": ["Quantitative Aptitude", "Logical Reasoning", "Speed & Accuracy", "Data Interpretation"],
                "estimated_hours": 16,
                "status": "completed" if total_attempts >= 5 else "upcoming",
                "recommended_practice": "/app/aptitude",
                "is_unlocked": True
            },
            {
                "stage_number": 11,
                "title": "Stage 11: Technical Interview Preparation & System Design",
                "description": "Mock interview practice with real-time feedback on architecture, edge cases, and algorithmic complexity.",
                "skills": ["Live Coding Explanation", "System Design Basics", "Complexity Justification"],
                "estimated_hours": 15,
                "status": "completed" if interviews_completed >= 1 else "upcoming",
                "recommended_practice": "/app/interview",
                "is_unlocked": True
            },
            {
                "stage_number": 12,
                "title": "Stage 12: HR & Behavioral Communication Lab",
                "description": "Mastering STAR framework responses for behavioral rounds, conflict resolution, leadership, and professional articulation.",
                "skills": ["STAR Framework", "Self Introduction", "Behavioral Scenarios", "Active Listening"],
                "estimated_hours": 10,
                "status": "upcoming",
                "recommended_practice": "/app/communication",
                "is_unlocked": True
            },
            {
                "stage_number": 13,
                "title": "Stage 13: ATS-Optimized Resume & Campus Placement",
                "description": "Tailor resume bullets with quantifiable achievements, verify ATS compliance, and prepare company-specific applications.",
                "skills": ["Resume ATS Optimization", "Action Verb Phrasing", "Application Tracking", "Offer Evaluation"],
                "estimated_hours": 8,
                "status": "upcoming",
                "recommended_practice": "/app/resume",
                "is_unlocked": True
            }
        ]

@router.get("/roadmap")
@router.get("/roadmap/my-roadmap")
def get_student_roadmap(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    profile = current_user.profile
    target_role = profile.target_role if profile and profile.target_role else "Software Developer"
    lang = profile.preferred_programming_language if (profile and profile.preferred_programming_language) else "Python"
    skill = profile.skill_level if profile and profile.skill_level else "Beginner"

    completed_lessons = db.query(LessonProgress).filter(
        LessonProgress.user_id == current_user.id,
        LessonProgress.status == "completed"
    ).count()

    solved_coding = db.query(CodingSubmission).filter(
        CodingSubmission.user_id == current_user.id,
        CodingSubmission.status.in_(["accepted", "preview_evaluated"])
    ).count()

    total_attempts = db.query(SubmittedAnswer).filter(
        SubmittedAnswer.user_id == current_user.id
    ).count()

    interviews_completed = db.query(InterviewSession).filter(
        InterviewSession.user_id == current_user.id,
        InterviewSession.status == "completed"
    ).count()

    stages = build_stages_for_role(
        role=target_role,
        lang=lang,
        completed_lessons=completed_lessons,
        solved_coding=solved_coding,
        total_attempts=total_attempts,
        interviews_completed=interviews_completed
    )

    return {
        "target_role": target_role,
        "preferred_language": lang,
        "skill_level": skill,
        "total_stages": len(stages),
        "stages": stages
    }
