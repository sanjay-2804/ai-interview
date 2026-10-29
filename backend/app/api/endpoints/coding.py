from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app.core.database import get_db
from app.models.models import User, CodingProblem, CodingSubmission
from app.schemas.schemas import (
    CodingProblemListOut, CodingProblemDetail, CodeRunRequest, CodeRunResult
)
from app.api.deps import get_current_user
from app.services.coding_service import coding_service

router = APIRouter(prefix="/coding", tags=["Coding Practice"])

@router.get("/problems", response_model=List[CodingProblemListOut])
def list_coding_problems(
    difficulty: Optional[str] = None,
    category: Optional[str] = None,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    query = db.query(CodingProblem)
    if difficulty and difficulty.lower() != "all":
        query = query.filter(CodingProblem.difficulty.ilike(difficulty))
    if category and category.lower() != "all":
        query = query.filter(CodingProblem.category.ilike(category))

    problems = query.all()
    user_submissions = db.query(CodingSubmission).filter(CodingSubmission.user_id == current_user.id).all()
    attempted_ids = {s.problem_id for s in user_submissions}
    solved_ids = {s.problem_id for s in user_submissions if s.status == "accepted"}

    out = []
    for p in problems:
        out.append(CodingProblemListOut(
            id=p.id,
            title=p.title,
            slug=p.slug,
            difficulty=p.difficulty,
            category=p.category,
            time_complexity=p.time_complexity,
            space_complexity=p.space_complexity,
            external_url=p.external_url,
            external_platform=p.external_platform,
            has_attempted=(p.id in attempted_ids),
            is_solved=(p.id in solved_ids)
        ))
    return out

@router.get("/problems/{problem_id}", response_model=CodingProblemDetail)
def get_coding_problem(
    problem_id: int,
    db: Session = Depends(get_db)
):
    problem = db.query(CodingProblem).filter(CodingProblem.id == problem_id).first()
    if not problem:
        raise HTTPException(status_code=404, detail="Coding problem not found.")
    return CodingProblemDetail.model_validate(problem)

@router.post("/submissions", response_model=CodeRunResult)
@router.post("/run", response_model=CodeRunResult)
def run_and_submit_code(
    payload: CodeRunRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return coding_service.submit_code(
        db=db,
        user_id=current_user.id,
        problem_id=payload.problem_id,
        language=payload.language,
        code=payload.code
    )

@router.get("/submissions")
def get_all_user_submissions(
    problem_id: Optional[int] = None,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    query = db.query(CodingSubmission).filter(CodingSubmission.user_id == current_user.id)
    if problem_id:
        query = query.filter(CodingSubmission.problem_id == problem_id)
    submissions = query.order_by(CodingSubmission.submitted_at.desc()).all()
    return [
        {
            "id": s.id,
            "problem_id": s.problem_id,
            "problem_title": s.problem.title if s.problem else None,
            "language": s.language,
            "status": s.status,
            "runtime_ms": s.runtime_ms,
            "memory_kb": s.memory_kb,
            "output_log": s.output_log,
            "submitted_at": s.submitted_at.strftime("%Y-%m-%d %H:%M:%S")
        } for s in submissions
    ]

@router.get("/problems/{problem_id}/submissions")
def get_problem_submissions(
    problem_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    submissions = db.query(CodingSubmission).filter(
        CodingSubmission.user_id == current_user.id,
        CodingSubmission.problem_id == problem_id
    ).order_by(CodingSubmission.submitted_at.desc()).all()
    return [
        {
            "id": s.id,
            "language": s.language,
            "status": s.status,
            "runtime_ms": s.runtime_ms,
            "memory_kb": s.memory_kb,
            "output_log": s.output_log,
            "submitted_at": s.submitted_at.strftime("%Y-%m-%d %H:%M:%S")
        } for s in submissions
    ]

@router.get("/dsa-roadmap")
def get_dsa_roadmap():
    return [
        {
            "level": 1,
            "title": "Level 1: Programming Foundations",
            "tagline": "Syntax fundamentals, memory allocation basics, and recursive call stacks.",
            "topics": [
                {"name": "Variables & Primitive Types", "desc": "Integer ranges, floating point precision, and character encoding (ASCII/Unicode)."},
                {"name": "Conditionals & Flow Control", "desc": "Branching, switch statements, and short-circuit boolean evaluation."},
                {"name": "Loops & Iteration", "desc": "Nested loop invariants, break/continue semantics, and iteration boundaries."},
                {"name": "Functions & Pointers", "desc": "Pass-by-value vs pass-by-reference, activation records, and call stacks."},
                {"name": "Recursion Foundations", "desc": "Base case identification, recursion trees, and avoiding StackOverflowError."}
            ]
        },
        {
            "level": 2,
            "title": "Level 2: Time & Space Complexity",
            "tagline": "Rigorous Big-O asymptotic analysis for interview problem solving.",
            "topics": [
                {"name": "Big-O, Omega & Theta Notations", "desc": "Upper bound, lower bound, and tight asymptotic complexity bounds."},
                {"name": "Common Complexity Classes", "desc": "O(1) constant, O(log N) logarithmic, O(N) linear, O(N log N) linearithmic, O(N^2) quadratic, O(2^N) exponential."},
                {"name": "Master Theorem", "desc": "Solving divide-and-conquer recurrence relations T(N) = aT(N/b) + f(N)."},
                {"name": "Auxiliary Space Complexity", "desc": "Distinguishing input storage from heap/stack auxiliary memory consumption."}
            ]
        },
        {
            "level": 3,
            "title": "Level 3: Linear Data Structures",
            "tagline": "Sequential memory layouts and dynamic pointer structures.",
            "topics": [
                {"name": "Static & Dynamic Arrays", "desc": "Contiguous memory, geometric resizing amortized O(1), and cache locality."},
                {"name": "Singly & Doubly Linked Lists", "desc": "Pointer manipulation, cycle detection (Floyd's Tortoise & Hare), and reverse traversal."},
                {"name": "Stacks (LIFO)", "desc": "Call stacks, parenthesis matching, and monotonic stack optimizations."},
                {"name": "Queues & Deques (FIFO)", "desc": "Circular buffers, breadth-first traversal queues, and double-ended queues."},
                {"name": "Hash Tables & Collision Resolution", "desc": "Chaining vs open addressing (linear/quadratic probing), load factors, and hash function properties."}
            ]
        },
        {
            "level": 4,
            "title": "Level 4: Searching & Sorting Algorithms",
            "tagline": "Foundational comparison and non-comparison ordering paradigms.",
            "topics": [
                {"name": "Binary Search", "desc": "Search space division, lower_bound, upper_bound, and binary search on monotonic answer spaces."},
                {"name": "Merge Sort", "desc": "Stable O(N log N) divide-and-conquer sorting with auxiliary array merging."},
                {"name": "Quick Sort", "desc": "In-place partitioning (Lomuto vs Hoare), pivot selection, and randomized quickselect O(N)."},
                {"name": "Counting & Radix Sort", "desc": "Non-comparison linear time O(N + K) sorting for integers and fixed-length strings."}
            ]
        },
        {
            "level": 5,
            "title": "Level 5: Core Problem-Solving Patterns",
            "tagline": "The 6 recurring patterns that solve 80% of placement coding questions.",
            "topics": [
                {"name": "Two Pointers Technique", "desc": "Opposite ends convergence and same-direction pacing for sorted arrays."},
                {"name": "Sliding Window Pattern", "desc": "Fixed vs dynamic window sizing for substring and subarray aggregation."},
                {"name": "Prefix Sums & Difference Arrays", "desc": "O(1) range sum queries and O(1) range increment updates."},
                {"name": "Fast & Slow Pointers", "desc": "Finding list middle nodes, cycle entry detection, and palindrome lists."},
                {"name": "Monotonic Stack / Queue", "desc": "Next Greater Element (NGE), Largest Rectangle in Histogram, and sliding window maximum."}
            ]
        },
        {
            "level": 6,
            "title": "Level 6: Nonlinear Hierarchical Structures",
            "tagline": "Trees, balanced search trees, binary heaps, and trie structures.",
            "topics": [
                {"name": "Binary Trees", "desc": "In-order, Pre-order, Post-order, and Level-order traversals; Lowest Common Ancestor (LCA)."},
                {"name": "Binary Search Trees (BST)", "desc": "BST property, search/insert/delete in O(H), in-order successor, and validation."},
                {"name": "Binary Heaps & Priority Queues", "desc": "Min-heap/Max-heap array representations, heapify in O(N), top-K element patterns."},
                {"name": "Tries (Prefix Trees)", "desc": "Efficient string prefix storage, auto-complete lookup, and XOR maximum pair queries."},
                {"name": "Graph Representations", "desc": "Adjacency matrix vs adjacency list, Breadth-First Search (BFS), and Depth-First Search (DFS)."}
            ]
        },
        {
            "level": 7,
            "title": "Level 7: Advanced Algorithmic Paradigms",
            "tagline": "Dynamic programming, greedy choices, shortest paths, and disjoint sets.",
            "topics": [
                {"name": "Dynamic Programming (DP)", "desc": "Overlapping subproblems, optimal substructure, memoization (top-down) vs tabulation (bottom-up), 0/1 Knapsack, LCS, and LIS."},
                {"name": "Greedy Algorithms", "desc": "Activity selection, fractional knapsack, interval scheduling, and Huffman coding."},
                {"name": "Shortest Paths (Dijkstra & Bellman-Ford)", "desc": "Weighted graph pathfinding with priority queues and negative weight cycle detection."},
                {"name": "Disjoint Set Union (DSU / Union-Find)", "desc": "Union by rank, path compression near O(1), and Kruskal's Minimum Spanning Tree."},
                {"name": "Topological Sorting", "desc": "Kahn's in-degree algorithm and DFS post-order reversal for course schedules and build dependencies."}
            ]
        }
    ]
