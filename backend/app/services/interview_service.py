from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from typing import Dict, Any, List, Optional
import datetime
from app.models.models import InterviewSession, InterviewResponse, ActivityEvent, utc_now
from app.schemas.schemas import (
    MockInterviewStart, MockInterviewDetail, MockInterviewResponseOut
)
from app.services.ai_service import ai_service

# Predefined curated question bank for interviews
INTERVIEW_QUESTIONS_BANK = {
    "Technical": [
        {
            "question": "Can you explain the differences between Process and Thread in Operating Systems, and how context switching differs between them?",
            "expected": ["Process has independent address space", "Threads share heap and memory of parent process", "Thread context switch is lighter and faster", "Inter-process communication (IPC) vs shared memory"]
        },
        {
            "question": "What is Database Indexing, how do B-Trees work under the hood, and what are the trade-offs of having too many indexes?",
            "expected": ["B-Tree data structure keeps data sorted for log(N) search", "Speeds up SELECT queries", "Slows down INSERT, UPDATE, and DELETE", "Consumes extra storage space"]
        },
        {
            "question": "Explain the concept of RESTful APIs and the key differences between PUT and PATCH HTTP methods.",
            "expected": ["Stateless client-server architecture", "PUT replaces the entire resource representation", "PATCH applies partial modifications", "Idempotence properties (PUT is idempotent)"]
        },
        {
            "question": "How does Garbage Collection work in modern runtimes (such as the JVM or V8), and what is a memory leak in a garbage-collected language?",
            "expected": ["Mark-and-sweep algorithm", "Generational hypothesis (young vs old generation)", "Memory leaks occur when unintended object references prevent reclamation"]
        },
        {
            "question": "What is the CAP Theorem in distributed systems, and why can't a distributed database guarantee both Consistency and Availability during network partitions?",
            "expected": ["Consistency, Availability, and Partition Tolerance", "Network partitions are unavoidable across network links", "Choice between CP (strict consistency, reject writes) and AP (high availability, eventual consistency)"]
        },
        {
            "question": "Explain the ACID properties in relational database management systems and how isolation levels prevent phantom reads and dirty reads.",
            "expected": ["Atomicity, Consistency, Isolation, Durability", "Dirty reads: reading uncommitted data", "Non-repeatable reads: reading modified data in same transaction", "Phantom reads: new rows inserted matching predicate", "Serializable vs Read Committed isolation"]
        },
        {
            "question": "How do WebSockets differ from standard HTTP polling and Server-Sent Events (SSE) for real-time web applications?",
            "expected": ["Full-duplex bidirectional persistent TCP channel", "HTTP handshake with 101 Switching Protocols", "SSE is unidirectional server-to-client", "Polling incurs HTTP request/response overhead"]
        },
        {
            "question": "What are microservices, and how does the Saga Pattern manage distributed transactions without Two-Phase Commit?",
            "expected": ["Independently deployable domain-bounded services", "Saga coordinates choreography or orchestration", "Compensating transactions reverse partial failures", "Eventual consistency"]
        }
    ],
    "HR": [
        {
            "question": "Tell me about yourself, your academic background, and what inspired you to pursue a career in technology.",
            "expected": ["Concise professional summary", "Key academic achievements and relevant coursework", "Passion for problem-solving and software development", "Future career alignment"]
        },
        {
            "question": "Describe a challenging situation in a group project where you faced a conflict or disagreement. How did you resolve it?",
            "expected": ["STAR framework (Situation, Task, Action, Result)", "Active listening and understanding differing perspectives", "Objective evaluation of technical trade-offs", "Positive team outcome"]
        },
        {
            "question": "Where do you see yourself in 3 to 5 years, and how does this role align with your long-term career aspirations?",
            "expected": ["Technical growth and mastery of system design or architecture", "Mentorship or project ownership", "Continuous learning mindset", "Commitment to engineering excellence"]
        },
        {
            "question": "Tell me about a time you missed a project deadline or made a critical mistake in your code. How did you handle it?",
            "expected": ["Taking immediate ownership without blaming teammates", "Transparent communication with stakeholders", "Root cause analysis and corrective action", "Implemented tests or linting to prevent recurrence"]
        },
        {
            "question": "Why do you want to join our company specifically, and what unique value do you bring to our engineering team?",
            "expected": ["Knowledge of company products, culture, and engineering values", "Alignment of personal technical skills with team roadmap", "High curiosity and drive to deliver impact from Day 1"]
        },
        {
            "question": "How do you handle working under tight deadlines or ambiguous project requirements?",
            "expected": ["Breaking down ambiguous problems into verifiable milestones", "Proactive communication and asking clarifying questions", "Ruthless prioritization of MVP features", "Maintaining composure under pressure"]
        }
    ],
    "DSA": [
        {
            "question": "How does a Hash Map handle collisions, and what is the difference between Chaining and Open Addressing?",
            "expected": ["Hash function maps keys to buckets", "Chaining uses linked lists or balanced trees at each bucket", "Open addressing probes for the next available slot (linear, quadratic, double hashing)", "Worst-case time complexity O(N) vs average O(1)"]
        },
        {
            "question": "Explain QuickSort vs MergeSort. When would you prefer one over the other in real-world software?",
            "expected": ["QuickSort is in-place with O(N log N) average and O(N^2) worst case", "MergeSort is stable with guaranteed O(N log N) but O(N) auxiliary space", "MergeSort preferred for linked lists and external sorting; QuickSort for cache locality"]
        },
        {
            "question": "How would you detect a cycle in a Singly Linked List, and what is the optimal time and space complexity?",
            "expected": ["Floyd's Cycle Finding Algorithm (Tortoise and Hare)", "Slow pointer advances 1 step, fast pointer advances 2 steps", "If they meet, cycle exists", "O(N) time and O(1) auxiliary space"]
        },
        {
            "question": "What is the difference between Depth-First Search (DFS) and Breadth-First Search (BFS) in graph traversal, and when would you use each?",
            "expected": ["BFS uses a FIFO Queue and explores level-by-level (finds shortest path in unweighted graphs)", "DFS uses recursion / LIFO Stack and explores paths deeply (topological sort, cycle detection)", "Both run in O(V + E) time"]
        }
    ],
    "Mixed": [
        {
            "question": "Walk me through the architecture and design trade-offs of the most technically challenging project you have built.",
            "expected": ["Clear problem statement and target users", "Architecture diagram and tech stack justification", "Tough technical bug or scale bottleneck overcome", "Quantifiable impact and future improvements"]
        },
        {
            "question": "How does an inverted index work in search engines like Elasticsearch to achieve sub-second full-text retrieval?",
            "expected": ["Tokenization and stemming of document text", "Mapping terms to posting lists of document IDs and term frequencies", "Skip lists for rapid intersection of multi-word queries"]
        },
        {
            "question": "Describe a scenario where you had to learn an unfamiliar programming language or framework under tight deadline pressure.",
            "expected": ["Structured learning path (official docs, minimal toy prototype)", "Seeking mentorship or reading existing codebases", "Applying software engineering fundamentals", "Delivered feature successfully"]
        },
        {
            "question": "What is the difference between SQL and NoSQL databases, and how do you decide which one to use for a new product?",
            "expected": ["Relational ACID vs horizontal scalability and flexible schema", "Use SQL for financial, transactional, and relational joined data", "Use NoSQL (Document/KV/Columnar) for massive scale, append-only events, or unstructured payloads"]
        },
        {
            "question": "Explain the Two-Pointer technique in array manipulation and how it reduces O(N^2) brute force to O(N).",
            "expected": ["In sorted arrays, left pointer starts at 0, right at N-1", "Shrink search space monotonically based on comparison", "O(N) time complexity with O(1) space"]
        },
        {
            "question": "How do you approach writing clean, maintainable, and testable code in a collaborative git-based team environment?",
            "expected": ["SOLID principles and meaningful naming", "Writing unit and integration tests", "Small atomic git commits and thorough pull request reviews", "Continuous integration and automated linting"]
        },
        {
            "question": "What is rate limiting, and how would you implement a distributed Token Bucket rate limiter using Redis?",
            "expected": ["Throttling client request rate to prevent abuse", "Token bucket refills tokens at steady rate R up to capacity B", "Redis Lua script executes atomic get-decrement-refill operations in O(1)"]
        },
        {
            "question": "Do you have any questions for the engineering team about our technical stack, culture, or placement expectations?",
            "expected": ["Thoughtful questions regarding tech stack challenges", "Team engineering culture, CI/CD, and deployment practices", "Onboarding expectations and mentorship programs"]
        }
    ]
}

class InterviewService:
    def start_interview(
        self,
        db: Session,
        user_id: int,
        category: str,
        target_role: str,
        difficulty: str,
        question_count: int
    ) -> MockInterviewDetail:
        category_clean = category if category in INTERVIEW_QUESTIONS_BANK else "Technical"
        q_pool = INTERVIEW_QUESTIONS_BANK.get(category_clean, INTERVIEW_QUESTIONS_BANK["Technical"])
        total_q = min(question_count, len(q_pool))

        session = InterviewSession(
            user_id=user_id,
            category=category,
            target_role=target_role,
            difficulty=difficulty,
            total_questions=total_q,
            completed_questions=0,
            status="in_progress",
            created_at=utc_now()
        )
        db.add(session)
        db.commit()
        db.refresh(session)

        first_q = q_pool[0]["question"] if q_pool else "Tell me about your technical journey."
        q_list = [{"id": i + 1, "question_text": q["question"], "category": category} for i, q in enumerate(q_pool[:total_q])]

        return MockInterviewDetail(
            id=session.id,
            category=session.category,
            target_role=session.target_role,
            difficulty=session.difficulty,
            total_questions=session.total_questions,
            completed_questions=0,
            status=session.status,
            current_question_text=first_q,
            questions=q_list,
            responses=[]
        )

    def get_interview(self, db: Session, session_id: int, user_id: int) -> MockInterviewDetail:
        session = db.query(InterviewSession).filter(
            InterviewSession.id == session_id,
            InterviewSession.user_id == user_id
        ).first()

        if not session:
            raise HTTPException(status_code=404, detail="Interview session not found.")

        category_clean = session.category if session.category in INTERVIEW_QUESTIONS_BANK else "Technical"
        q_pool = INTERVIEW_QUESTIONS_BANK.get(category_clean, INTERVIEW_QUESTIONS_BANK["Technical"])

        current_q = None
        if session.completed_questions < session.total_questions and session.completed_questions < len(q_pool):
            current_q = q_pool[session.completed_questions]["question"]

        resp_items = [
            MockInterviewResponseOut(
                id=r.id,
                question_text=r.question_text,
                category=r.category,
                student_response=r.student_response,
                score=r.score,
                evaluation_status=r.evaluation_status,
                strengths=r.strengths,
                missing_concepts=r.missing_concepts,
                improvement_suggestions=r.improvement_suggestions,
                sample_answer=r.sample_answer,
                ai_engine=r.ai_engine
            ) for r in session.responses
        ]

        q_list = [{"id": i + 1, "question_text": q["question"], "category": session.category} for i, q in enumerate(q_pool[:session.total_questions])]

        return MockInterviewDetail(
            id=session.id,
            category=session.category,
            target_role=session.target_role,
            difficulty=session.difficulty,
            total_questions=session.total_questions,
            completed_questions=session.completed_questions,
            status=session.status,
            current_question_text=current_q,
            questions=q_list,
            responses=resp_items,
            overall_score=session.overall_score,
            feedback_summary=session.feedback_summary
        )

    async def submit_response(
        self,
        db: Session,
        session_id: int,
        user_id: int,
        response_text: str
    ) -> MockInterviewDetail:
        session = db.query(InterviewSession).filter(
            InterviewSession.id == session_id,
            InterviewSession.user_id == user_id
        ).first()

        if not session or session.status == "completed":
            raise HTTPException(status_code=400, detail="Interview session is inactive or completed.")

        category_clean = session.category if session.category in INTERVIEW_QUESTIONS_BANK else "Technical"
        q_pool = INTERVIEW_QUESTIONS_BANK.get(category_clean, INTERVIEW_QUESTIONS_BANK["Technical"])

        current_idx = session.completed_questions
        if current_idx >= len(q_pool):
            current_q_item = {"question": "Describe your approach to learning new technologies quickly.", "expected": ["Structured learning", "Hands-on projects", "Reading documentation"]}
        else:
            current_q_item = q_pool[current_idx]

        eval_result = await ai_service.evaluate_interview_response(
            question=current_q_item["question"],
            expected_aspects=current_q_item["expected"],
            student_response=response_text,
            category=session.category,
            target_role=session.target_role
        )

        resp = InterviewResponse(
            session_id=session.id,
            question_text=current_q_item["question"],
            category=session.category,
            expected_aspects=current_q_item["expected"],
            student_response=response_text,
            score=eval_result.get("score", 7.0),
            evaluation_status=eval_result.get("evaluation_status", "evaluated"),
            strengths=eval_result.get("strengths", []),
            missing_concepts=eval_result.get("missing_concepts", []),
            improvement_suggestions=eval_result.get("improvement_suggestions", []),
            sample_answer=eval_result.get("sample_answer", ""),
            ai_engine=eval_result.get("ai_engine", "Deterministic Placement Rubric"),
            created_at=utc_now()
        )
        db.add(resp)

        session.completed_questions += 1
        if session.completed_questions >= session.total_questions:
            session.status = "completed"
            # Calculate overall score
            all_scores = [r.score for r in session.responses if r.score] + [resp.score]
            avg_score = round(sum(all_scores) / len(all_scores), 1) if all_scores else 7.5
            session.overall_score = avg_score
            session.feedback_summary = (
                f"Completed {session.total_questions} interview questions. "
                f"Overall readiness score: {avg_score}/10. Continue practicing technical depth and STAR behavioral storytelling."
            )

            act = ActivityEvent(
                user_id=user_id,
                event_type="mock_interview",
                title=f"Completed {session.category} Mock Interview",
                details=f"Average Score: {avg_score}/10 ({session.total_questions} questions)",
                metadata_json={"session_id": session.id, "score": avg_score}
            )
            db.add(act)

        db.commit()
        return self.get_interview(db, session.id, user_id)

interview_service = InterviewService()

