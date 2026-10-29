from sqlalchemy.orm import Session
from app.core.database import SessionLocal, engine, Base
from app.core.security import get_password_hash
from app.models.models import (
    User, UserProfile, Subject, Topic, Lesson, LearningResource,
    Question, QuestionOption, CodingProblem, LearningPath, RoadmapStage,
    Resume, ActivityEvent, SubmittedAnswer, PracticeSession, SessionQuestion, utc_now
)

def seed_database():
    # Ensure tables exist
    Base.metadata.create_all(bind=engine)
    db: Session = SessionLocal()
    try:
        # 1. Admin User
        admin_user = db.query(User).filter(User.email == "admin@interviewai.dev").first()
        if not admin_user:
            admin_user = User(
                email="admin@interviewai.dev",
                hashed_password=get_password_hash("Admin@123456"),
                full_name="Platform Administrator",
                role="admin",
                is_active=True,
                is_verified=True
            )
            db.add(admin_user)
            db.flush()

        # 2. Demo Student User
        student_user = db.query(User).filter(User.email == "student@interviewai.dev").first()
        if not student_user:
            student_user = User(
                email="student@interviewai.dev",
                hashed_password=get_password_hash("Student@123456"),
                full_name="Aarav Sharma",
                role="student",
                is_active=True,
                is_verified=True
            )
            db.add(student_user)
            db.flush()

            student_profile = UserProfile(
                user_id=student_user.id,
                college="National Institute of Technology",
                course="B.Tech Computer Science & Engineering",
                study_year="2026",
                target_role="Software Developer",
                preferred_programming_language="Python",
                skill_level="Intermediate",
                study_availability=3.0,
                preferred_topics=["Data Structures", "Algorithms", "Quantitative Aptitude", "SQL"],
                prep_priorities=["Campus Placement", "Product Companies"],
                onboarding_completed=True
            )
            db.add(student_profile)

            resume = Resume(
                user_id=student_user.id,
                title="Aarav Sharma - Software Engineer Resume",
                full_name="Aarav Sharma",
                email="student@interviewai.dev",
                phone="+91 98765 43210",
                location="Bengaluru, Karnataka",
                target_role="Software Developer",
                summary="Passionate computer science undergraduate with strong foundations in algorithms, data structures, and web technologies. Proven track record building full-stack applications with FastAPI and React.",
                education_json=[{
                    "degree": "B.Tech in Computer Science & Engineering",
                    "institution": "National Institute of Technology",
                    "year": "2022 - 2026",
                    "score": "8.8 CGPA"
                }],
                skills_json=["Python", "JavaScript", "TypeScript", "React", "FastAPI", "SQL", "Git", "Docker", "Tailwind CSS"],
                projects_json=[
                    {
                        "title": "InterviewAI Placement Platform",
                        "description": "Full-stack placement preparation web app with interactive answer-learning loops, live test cases, and ATS resume analyzer.",
                        "tech_stack": "React, TypeScript, FastAPI, PostgreSQL",
                        "link": "https://github.com/aarav/interviewai"
                    },
                    {
                        "title": "Algorithmic Visualizer",
                        "description": "Interactive web visualization for sorting algorithms (QuickSort, MergeSort) and pathfinding algorithms (Dijkstra, A*).",
                        "tech_stack": "TypeScript, HTML5 Canvas",
                        "link": "https://github.com/aarav/algo-visualizer"
                    }
                ],
                experience_json=[{
                    "role": "Software Engineering Intern",
                    "company": "TechInnovate Solutions",
                    "period": "May 2025 - July 2025",
                    "description": "Optimized database queries decreasing page load latency by 35%. Implemented RESTful microservices with automated unit tests."
                }],
                certifications_json=[{
                    "name": "AWS Certified Cloud Practitioner",
                    "issuer": "Amazon Web Services",
                    "year": "2025"
                }],
                links_json={
                    "github": "https://github.com/aarav",
                    "linkedin": "https://linkedin.com/in/aarav-sharma",
                    "portfolio": "https://aaravsharma.dev"
                }
            )
            db.add(resume)
            db.commit()

        # 2.5 Subjects
        subjects_data = [
            ("Quantitative Aptitude", "quantitative-aptitude", "Master arithmetic, algebra, percentages, speed-time, and numbers for campus tests.", "Calculator"),
            ("Logical & Verbal Reasoning", "logical-verbal-reasoning", "Puzzles, syllogisms, blood relations, and grammar for aptitude clearance.", "Brain"),
            ("Core Computer Science", "core-cs", "Data structures, algorithms, DBMS, operating systems, and computer networks.", "Cpu"),
            ("Software Engineering & Development", "software-engineering", "Modern programming languages, web frameworks, Git, and architecture.", "Code2")
        ]
        subject_map = {}
        for s_name, s_slug, s_desc, s_icon in subjects_data:
            s = db.query(Subject).filter(Subject.slug == s_slug).first()
            if not s:
                s = Subject(name=s_name, slug=s_slug, description=s_desc, icon=s_icon)
                db.add(s)
                db.flush()
            subject_map[s_slug] = s
        db.commit()

        # 3. Topics with subject mappings
        topics_data = [
            # Aptitude Topics
            ("Percentages & Profit-Loss", "percentages-profit-loss", "aptitude", "quantitative", "Percentages, markup, discount, cost price, selling price, and margin calculations.", "Percent", "quantitative-aptitude"),
            ("Time, Speed & Distance", "time-speed-distance", "aptitude", "quantitative", "Relative speed, trains, boats and streams, average speed formulas.", "Zap", "quantitative-aptitude"),
            ("Time & Work", "time-work", "aptitude", "quantitative", "Man-days, efficiency ratios, pipes and cisterns problem solving.", "Clock", "quantitative-aptitude"),
            ("Logical Deductions & Syllogisms", "syllogisms", "aptitude", "logical", "Venn diagrams, categorical propositions, truth-table deductions.", "Brain", "logical-verbal-reasoning"),
            ("Blood Relations & Directions", "blood-relations", "aptitude", "logical", "Family trees, directional sense tests, coordinate displacements.", "Compass", "logical-verbal-reasoning"),
            ("Verbal Ability & Grammar", "verbal-grammar", "aptitude", "verbal", "Sentence correction, active-passive voice, idioms, reading comprehension.", "BookMarked", "logical-verbal-reasoning"),
            # Technical Topics
            ("Data Structures & Algorithms", "dsa", "technical", "cs", "Arrays, Linked Lists, Trees, Graphs, Sorting, Dynamic Programming.", "Binary", "core-cs"),
            ("Object-Oriented Programming", "oop", "technical", "cs", "Encapsulation, Inheritance, Polymorphism, Abstraction, SOLID principles.", "Boxes", "core-cs"),
            ("DBMS & SQL", "dbms-sql", "technical", "cs", "Relational modeling, Normalization, ACID transactions, B-Tree indexes, SQL joins.", "Database", "core-cs"),
            ("Operating Systems", "operating-systems", "technical", "cs", "Processes, Threads, Concurrency, Virtual Memory, CPU Scheduling, Deadlocks.", "Cpu", "core-cs"),
            ("Computer Networks", "computer-networks", "technical", "cs", "OSI & TCP/IP stack, Socket programming, HTTP/3, DNS, Transport protocols.", "Network", "core-cs"),
            ("Python Programming", "python-programming", "technical", "programming", "Python idioms, memory management, decorators, generators, GIL.", "Code", "software-engineering"),
            ("Web Development & React", "web-dev", "technical", "web_dev", "Component lifecycles, Hooks, Virtual DOM, RESTful API consumption.", "Globe", "software-engineering")
        ]

        topic_map = {}
        for name, slug, cat, subcat, desc, icon, subj_slug in topics_data:
            t = db.query(Topic).filter(Topic.slug == slug).first()
            s_obj = subject_map.get(subj_slug)
            if not t:
                t = Topic(name=name, slug=slug, category=cat, subcategory=subcat, description=desc, icon=icon, subject_id=s_obj.id if s_obj else None)
                db.add(t)
                db.flush()
            else:
                if s_obj and not t.subject_id:
                    t.subject_id = s_obj.id
            topic_map[slug] = t
        db.commit()

        # 4. Lessons with rich markdown content
        lessons_data = [
            (
                "percentages-profit-loss",
                "Mastering Percentages and Profit/Loss for Placement Exams",
                "percentages-profit-loss-guide",
                "Beginner",
                20,
                [
                    "Percentage change formula: `((New - Old) / Old) * 100`",
                    "Cost Price (CP), Selling Price (SP), Profit = SP - CP, Loss = CP - SP",
                    "Profit % = `(Profit / CP) * 100` (Always computed on Cost Price)",
                    "Successive discounts: `Net Discount = d1 + d2 - (d1 * d2) / 100`"
                ],
                """# Percentages and Profit & Loss Mastery

Percentages are the foundation for over 40% of quantitative aptitude questions in placement exams for TCS, Infosys, Cognizant, Wipro, and product companies.

## Core Formulae

1. **Fraction to Percentage Equivalents**:
   - 1/2 = 50%
   - 1/3 = 33.33%
   - 1/4 = 25%
   - 1/5 = 20%
   - 1/6 = 16.66%
   - 1/7 = 14.28%
   - 1/8 = 12.5%
   - 1/9 = 11.11%
   - 1/12 = 8.33%

Memorizing these equivalents allows you to compute answers in 15 seconds instead of 60 seconds.

## Profit & Loss Equations

- **Profit** = SP - CP
- **Loss** = CP - SP
- **Profit %** = (Profit / CP) * 100
- **Loss %** = (Loss / CP) * 100
- **Marked Price (MP)**: Price labeled on the item before discounts.
- **Discount %** = ((MP - SP) / MP) * 100

### Key Trap to Avoid
> Students frequently divide by Selling Price (SP) when calculating Profit Percentage. **Always divide by Cost Price (CP)** unless explicitly stated otherwise by the problem.
"""
            ),
            (
                "dsa",
                "Time and Space Complexity Analysis: Big-O Demystified",
                "big-o-complexity-guide",
                "Beginner",
                15,
                [
                    "Big-O represents the upper bound asymptotic growth rate.",
                    "Common hierarchy: O(1) < O(log N) < O(N) < O(N log N) < O(N^2) < O(2^N) < O(N!)",
                    "Drop constant factors and non-dominant terms for large N.",
                    "Auxiliary space measures additional memory beyond input storage."
                ],
                """# Asymptotic Complexity and Big-O Notation

In technical placement interviews, understanding Big-O notation is essential. Every coding question finishes with: *"What is the time and space complexity of your solution, and can we do better?"*

## Complexity Classes Hierarchy

1. **O(1) - Constant Time**: Hash map lookup, accessing an array element by index.
2. **O(log N) - Logarithmic Time**: Binary search, searching in a Balanced Binary Search Tree.
3. **O(N) - Linear Time**: Single traversal through an array or linked list.
4. **O(N log N) - Linearithmic Time**: MergeSort, QuickSort (average case), HeapSort.
5. **O(N^2) - Quadratic Time**: Nested loops over array elements (Bubble sort, Selection sort).
6. **O(2^N) - Exponential Time**: Recursive calculation of Fibonacci without memoization, generating all subsets.
7. **O(N!) - Factorial Time**: Generating all permutations of a string.

## Practical Interview Rule of Thumb
Given standard online coding assessment constraints (1 to 2 seconds CPU time limit):
- N <= 10^4: O(N^2) might pass, but O(N log N) is preferred.
- N <= 10^6: O(N) or O(N log N) required.
- N >= 10^8: Only O(log N) or O(1) will pass without timing out (TLE).
"""
            ),
            (
                "dbms-sql",
                "Database Indexing Internals: B-Trees & Query Optimization",
                "b-trees-and-indexing",
                "Intermediate",
                25,
                [
                    "An index is an auxiliary data structure that reduces disk I/O.",
                    "B-Trees maintain sorted order with balanced logarithmic search, insert, and delete operations.",
                    "Clustered Index determines physical storage order of rows (only one per table).",
                    "Secondary Indexes store search keys and pointers to row locators."
                ],
                """# Database Indexing & B-Trees

Without an index, finding a specific row requires a **Full Table Scan** (O(N) disk block reads). For a table with 10 million rows, this takes seconds. With a B-Tree index, it takes 3 to 4 block reads (O(log N)).

## Why B-Trees Over Binary Search Trees?
- Binary Search Trees (BSTs) have low branching factors (2 children), leading to high tree height and many disk seeks.
- B-Trees have huge branching factors (hundreds of keys per node), keeping tree height to 3-4 levels even for millions of rows.
- Each node matches disk block sizes (typically 4KB or 8KB) maximizing cache line efficiency.

## The Cost of Indexes
Indexes are not free. While they accelerate `SELECT` queries with `WHERE`, `JOIN`, or `ORDER BY` clauses:
1. They consume additional physical disk storage.
2. Every `INSERT`, `UPDATE`, and `DELETE` must also update all related index structures, slowing down write-heavy workloads.
"""
            ),
            (
                "operating-systems",
                "Process vs Thread & CPU Scheduling Fundamentals",
                "process-thread-cpu-scheduling",
                "Intermediate",
                20,
                [
                    "A process is an execution instance with its own virtual address space.",
                    "Threads share code, data, and heap within a process, but have private registers and stacks.",
                    "Thread context switching is significantly faster than process context switching.",
                    "Preemptive scheduling allows high-priority tasks to interrupt running tasks."
                ],
                """# Operating Systems: Processes and Threads

## Process vs Thread Architecture
- **Process**: Program in execution. Encapsulates text (code), data (globals), heap (dynamic allocation), stack (local variables, call frames), and OS resources (file descriptors).
- **Thread**: Lightweight unit of CPU execution within a process. Multiple threads in the same process share the heap and address space, enabling low-overhead communication.

## Context Switching Overhead
When switching between processes:
1. CPU registers and program counter are saved.
2. Page table base pointer (CR3 register in x86) is updated.
3. CPU Translation Lookaside Buffer (TLB) is invalidated, causing memory access cache misses.

When switching between threads of the same process:
- Memory space remains identical, so TLB does NOT need to be flushed, making thread context switches 5x to 10x faster.
"""
            )
        ]

        for topic_slug, title, slug, diff, mins, takeaways, content in lessons_data:
            t = topic_map.get(topic_slug)
            if t:
                l = db.query(Lesson).filter(Lesson.slug == slug).first()
                if not l:
                    l = Lesson(
                        topic_id=t.id,
                        title=title,
                        slug=slug,
                        difficulty=diff,
                        estimated_minutes=mins,
                        key_takeaways=takeaways,
                        content_markdown=content,
                        order_index=1,
                        is_published=True
                    )
                    db.add(l)
        db.commit()

        # 5. Learning Resources
        resources_data = [
            ("dsa", "GeeksforGeeks Data Structures", "https://www.geeksforgeeks.org/data-structures/", "documentation", "GeeksforGeeks", "English", "Comprehensive tutorial series on arrays, trees, heaps, and graphs with C++, Java, and Python examples."),
            ("dsa", "LeetCode Problem Set", "https://leetcode.com/problemset/", "practice", "LeetCode", "English", "Over 3,000 curated algorithmic interview problems categorized by pattern and difficulty."),
            ("percentages-profit-loss", "IndiaBIX Quantitative Aptitude", "https://www.indiabix.com/aptitude/questions-and-answers/", "practice", "IndiaBIX", "English", "Standard placement aptitude questions with step-by-step mathematical explanations."),
            ("dbms-sql", "W3Schools SQL Tutorial", "https://www.w3schools.com/sql/", "documentation", "W3Schools", "English", "Interactive SQL tutorial covering SELECT, JOIN, GROUP BY, and subqueries with live browser editor."),
            ("web-dev", "MDN Web Docs", "https://developer.mozilla.org/", "documentation", "MDN", "English", "Authoritative web development reference for JavaScript, HTML, CSS, and modern Web APIs.")
        ]

        for topic_slug, title, url, r_type, provider, lang, desc in resources_data:
            t = topic_map.get(topic_slug)
            if t:
                existing_r = db.query(LearningResource).filter(LearningResource.url == url).first()
                if not existing_r:
                    r = LearningResource(
                        topic_id=t.id,
                        title=title,
                        url=url,
                        resource_type=r_type,
                        provider_name=provider,
                        language=lang,
                        description=desc,
                        is_verified=True
                    )
                    db.add(r)
        db.commit()

        # 6. Questions & Detailed Feedback (Learn from Every Answer Central Feature)
        questions_data = [
            # Quantitative Aptitude
            {
                "topic_slug": "percentages-profit-loss",
                "type": "aptitude_mcq",
                "diff": "intermediate",
                "text": "A retailer buys an article for $400 and marks it 25% above cost price. If he offers a 10% discount on the marked price, what is his profit percentage?",
                "code": None,
                "explanation": "To determine the profit percentage, first calculate the Marked Price (MP), then compute the Selling Price (SP) after the 10% discount, and finally calculate profit over the original Cost Price.",
                "reasoning": "Step 1: Cost Price (CP) = $400.\nStep 2: Marked Price (MP) = 400 + (25% of 400) = 400 + 100 = $500.\nStep 3: Selling Price (SP) = 500 - (10% of 500) = 500 - 50 = $450.\nStep 4: Profit = SP - CP = $450 - $400 = $50.\nStep 5: Profit % = (Profit / CP) * 100 = (50 / 400) * 100 = 12.5%.",
                "example": "If a phone costs $800 wholesale, is marked up 25% to $1,000, and sold at a 10% holiday discount for $900, the net profit is $100 on an $800 base, which is exactly 12.5%.",
                "mistake": "A common mistake is subtracting the 10% discount directly from the 25% markup to guess '15%'. Discounts apply to Marked Price ($500), not Cost Price ($400).",
                "tip": "Net Multiplier Shortcut: SP = CP * 1.25 * 0.90 = CP * 1.125. The 0.125 increase translates directly to 12.5% profit!",
                "url": "https://www.geeksforgeeks.org/profit-and-loss-formulas/",
                "options": [
                    ("A", "15.0%", False, "Incorrect. You cannot simply subtract 10% from 25% because they apply to different base values ($500 vs $400)."),
                    ("B", "12.5%", True, "Correct! Marked price = $500, Selling price = $450, yielding a $50 profit on $400 (12.5%)."),
                    ("C", "10.0%", False, "Incorrect. A 10% profit on $400 would equal $440 SP, whereas the actual SP is $450."),
                    ("D", "14.2%", False, "Incorrect. 14.2% would correspond to approximately 1/7 ratio, which does not match the computed values.")
                ]
            },
            {
                "topic_slug": "percentages-profit-loss",
                "type": "aptitude_mcq",
                "diff": "beginner",
                "text": "If the price of sugar increases by 25%, by what percentage must a household reduce its consumption so that total expenditure remains unchanged?",
                "code": None,
                "explanation": "When the price of a commodity increases by R%, consumption must decrease by [R / (100 + R)] * 100% to keep expenditure constant.",
                "reasoning": "Formula: Reduction % = [R / (100 + R)] * 100\nSubstitute R = 25:\nReduction % = [25 / (100 + 25)] * 100 = [25 / 125] * 100 = (1 / 5) * 100 = 20%.",
                "example": "Assume original price was $10/kg and consumption was 10kg (Expenditure = $100). New price = $12.50/kg. For expenditure to stay $100, consumption = 100 / 12.5 = 8kg (a reduction of 2kg out of 10kg = 20%).",
                "mistake": "Assuming that a 25% increase in price requires a 25% decrease in consumption. A 25% decrease would actually lower total expenditure below the baseline.",
                "tip": "Fraction rule: If price increases by 1/4 (25%), consumption must decrease by 1/(4+1) = 1/5 (20%).",
                "url": "https://www.geeksforgeeks.org/percentages/",
                "options": [
                    ("A", "25%", False, "Incorrect. A 25% reduction would drop consumption to 7.5kg, causing expenditure to drop to $93.75."),
                    ("B", "20%", True, "Correct! Using [R / (100 + R)] * 100 gives 25/125 * 100 = 20%."),
                    ("C", "16.66%", False, "Incorrect. 16.66% corresponds to a 20% price increase, not a 25% increase."),
                    ("D", "15%", False, "Incorrect. 15% reduction leaves expenditure at $106.25, which violates the requirement.")
                ]
            },
            {
                "topic_slug": "time-work",
                "type": "aptitude_mcq",
                "diff": "intermediate",
                "text": "Pipe A can fill a tank in 12 hours, while Pipe B can empty the same tank in 18 hours. If both pipes are opened simultaneously into an empty tank, how many hours will it take to fill completely?",
                "code": None,
                "explanation": "Net rate of work per hour is the filling rate minus the emptying rate.",
                "reasoning": "Step 1: Pipe A fills 1/12 of the tank per hour.\nStep 2: Pipe B empties 1/18 of the tank per hour.\nStep 3: Net rate = (1/12) - (1/18) = (3 - 2) / 36 = 1/36 per hour.\nStep 4: Total time to fill = 1 / (1/36) = 36 hours.",
                "example": "Take total tank capacity as LCM(12, 18) = 36 liters. Pipe A fills 3 L/hr, Pipe B drains 2 L/hr. Net inflow = 1 L/hr. Filling 36 liters takes 36 / 1 = 36 hours.",
                "mistake": "Adding the rates instead of subtracting, forgetting that Pipe B empties rather than fills.",
                "tip": "Use the LCM method for Pipes and Cisterns to avoid messy fraction arithmetic!",
                "url": "https://www.geeksforgeeks.org/pipes-and-cisterns/",
                "options": [
                    ("A", "30 hours", False, "Incorrect. Does not match the net LCM rate calculation."),
                    ("B", "36 hours", True, "Correct! Net rate is 1/12 - 1/18 = 1/36, meaning 36 hours to fill."),
                    ("C", "24 hours", False, "Incorrect. 24 hours would require a net rate of 1/24 per hour."),
                    ("D", "15 hours", False, "Incorrect. If pipes worked together to fill, it would take ~7.2 hrs; with emptying, it must exceed 18 hrs.")
                ]
            },
            # Logical Reasoning
            {
                "topic_slug": "syllogisms",
                "type": "aptitude_mcq",
                "diff": "intermediate",
                "text": "Statements:\n1. All engineers are problem solvers.\n2. Some problem solvers are musicians.\nConclusions:\nI. Some engineers are musicians.\nII. Some problem solvers are engineers.\nWhich conclusion(s) logically follow?",
                "code": None,
                "explanation": "From 'All A are B', the immediate converse 'Some B are A' is always valid. However, no definite overlap between engineers and musicians is guaranteed.",
                "reasoning": "Statement 1: Engineers ⊆ Problem Solvers.\nStatement 2: Problem Solvers ∩ Musicians ≠ ∅.\nConclusion I: 'Some engineers are musicians' — Engineers and Musicians might be completely disjoint subsets inside Problem Solvers. Does not follow necessarily.\nConclusion II: 'Some problem solvers are engineers' — Since All engineers are problem solvers, the set of problem solvers definitely contains engineers. Follows definitely.",
                "example": "Let Engineers = {Alice, Bob}, Problem Solvers = {Alice, Bob, Charlie}, Musicians = {Charlie}. Here, all engineers are problem solvers, Charlie is both, but no engineer is a musician. Thus I is not guaranteed.",
                "mistake": "Assuming that because both groups share the category 'problem solvers', they must share elements with each other.",
                "tip": "Whenever you see 'All A are B', you can immediately validate 'Some B are A'.",
                "url": "https://www.geeksforgeeks.org/syllogism-reasoning-concepts-questions/",
                "options": [
                    ("A", "Only Conclusion I follows", False, "Incorrect. Engineers and musicians may have zero overlap."),
                    ("B", "Only Conclusion II follows", True, "Correct! Since All Engineers are Problem Solvers, Some Problem Solvers are guaranteed to be Engineers."),
                    ("C", "Both Conclusions I and II follow", False, "Incorrect. Conclusion I is merely possible, not logically necessary."),
                    ("D", "Neither Conclusion follows", False, "Incorrect. Conclusion II is a valid conversion of Statement 1.")
                ]
            },
            # Technical MCQs: DSA
            {
                "topic_slug": "dsa",
                "type": "technical_mcq",
                "diff": "intermediate",
                "text": "What is the worst-case time complexity of searching for an element in a Hash Table that handles collisions using separate chaining?",
                "code": None,
                "explanation": "In the worst case, every single key hashes to the exact same bucket, degrading the chain into a single linked list of N elements.",
                "reasoning": "Under a perfect hash function with uniform distribution, average lookup is O(1). However, if an adversarial input causes hash collisions for all N keys, they are placed in a single linked list bucket. Searching through this linked list takes O(N) operations in the worst case.",
                "example": "If hash(k) = 0 for all keys k1, k2, ... kN, finding kN requires traversing all N nodes in bucket 0.",
                "mistake": "Confusing the average case O(1) with the worst case O(N). Java 8 mitigated this by converting long linked lists (>= 8 nodes) into balanced red-black trees, improving worst case to O(log N).",
                "tip": "Always specify average case vs worst case when discussing Hash Tables in technical interviews!",
                "url": "https://www.geeksforgeeks.org/hashing-data-structure/",
                "options": [
                    ("A", "O(1)", False, "Incorrect. O(1) is the expected average case under the simple uniform hashing assumption, not the worst case."),
                    ("B", "O(log N)", False, "Incorrect. Standard separate chaining uses linked lists with O(N) traversal, unless treeified like Java 8."),
                    ("C", "O(N)", True, "Correct! When all elements collide into the same bucket, searching degrades to linked list traversal O(N)."),
                    ("D", "O(N log N)", False, "Incorrect. Hash table lookups never exceed O(N).")
                ]
            },
            # Technical MCQs: Operating Systems
            {
                "topic_slug": "operating-systems",
                "type": "technical_mcq",
                "diff": "intermediate",
                "text": "Which of the following is NOT one of Coffman's four necessary conditions for a Deadlock to occur?",
                "code": None,
                "explanation": "Coffman conditions are: Mutual Exclusion, Hold and Wait, No Preemption, and Circular Wait. Aging is a scheduling starvation prevention technique, not a deadlock condition.",
                "reasoning": "The 4 Coffman conditions required simultaneously for a deadlock are:\n1. Mutual Exclusion (at least one resource is non-shareable)\n2. Hold and Wait (processes holding resources request new ones)\n3. No Preemption (resources cannot be forcibly taken away)\n4. Circular Wait (P0 waits for P1, P1 waits for P2 ... Pn waits for P0)\nAging is a mechanism to gradually increase the priority of waiting processes to prevent starvation.",
                "example": "Traffic gridlock at a 4-way intersection without signals where each car holds the lane and waits for the car ahead to move represents Circular Wait.",
                "mistake": "Confusing deadlock conditions with CPU scheduling concepts like aging or starvation prevention.",
                "tip": "Remember the acronym MHNC: Mutual exclusion, Hold & wait, No preemption, Circular wait.",
                "url": "https://www.geeksforgeeks.org/deadlock-in-operating-system/",
                "options": [
                    ("A", "Mutual Exclusion", False, "Incorrect. Mutual exclusion is indeed one of the 4 Coffman conditions."),
                    ("B", "Hold and Wait", False, "Incorrect. Hold and wait is a required Coffman condition."),
                    ("C", "Aging", True, "Correct! Aging is a starvation-prevention technique in priority scheduling, NOT a deadlock condition."),
                    ("D", "Circular Wait", False, "Incorrect. Circular wait is the 4th fundamental Coffman condition.")
                ]
            },
            # Technical MCQs: DBMS
            {
                "topic_slug": "dbms-sql",
                "type": "technical_mcq",
                "diff": "intermediate",
                "text": "Consider a relational table with functional dependencies. A relation is in Third Normal Form (3NF) if and only if it is in 2NF and:",
                "code": None,
                "explanation": "3NF eliminates transitive functional dependencies on non-prime attributes.",
                "reasoning": "Definition: For every non-trivial functional dependency X -> Y in relation R:\nEither X is a superkey, OR Y is a prime attribute (part of any candidate key).\nThis ensures there are no transitive dependencies: non-key attributes must depend solely on the candidate key, not on another non-key attribute.",
                "example": "In Students(ID, DepartmentName, DepartmentHOD): ID -> DepartmentName and DepartmentName -> DepartmentHOD creates a transitive dependency ID -> DepartmentHOD. Splitting into Students and Departments resolves this to 3NF.",
                "mistake": "Thinking 3NF requires every determinant to be a candidate key — that stricter definition is Boyce-Codd Normal Form (BCNF).",
                "tip": "Mnemonic: 'Every attribute must depend on the key (1NF), the whole key (2NF), and nothing but the key (3NF), so help me Codd!'",
                "url": "https://www.geeksforgeeks.org/third-normal-form-3nf/",
                "options": [
                    ("A", "No non-prime attribute is transitively dependent on any candidate key", True, "Correct! 3NF strictly removes transitive functional dependencies."),
                    ("B", "Every determinant is a candidate key", False, "Incorrect. That is the definition of Boyce-Codd Normal Form (BCNF), which is strictly stronger than 3NF."),
                    ("C", "Multi-valued dependencies are eliminated", False, "Incorrect. Multi-valued dependencies are handled in 4NF."),
                    ("D", "Partial dependencies on composite keys are removed", False, "Incorrect. Removing partial dependencies is the requirement for 2NF, not 3NF.")
                ]
            }
        ]

        for q_data in questions_data:
            t = topic_map.get(q_data["topic_slug"])
            if t:
                existing_q = db.query(Question).filter(Question.question_text == q_data["text"]).first()
                if not existing_q:
                    q = Question(
                        topic_id=t.id,
                        question_type=q_data["type"],
                        difficulty=q_data["diff"],
                        question_text=q_data["text"],
                        code_snippet=q_data.get("code"),
                        explanation=q_data["explanation"],
                        step_by_step_reasoning=q_data["reasoning"],
                        practical_example=q_data["example"],
                        common_mistake=q_data["mistake"],
                        learning_tip=q_data["tip"],
                        related_concept_url=q_data["url"],
                        is_published=True
                    )
                    db.add(q)
                    db.flush()

                    for key, text, is_corr, why_wrong in q_data["options"]:
                        opt = QuestionOption(
                            question_id=q.id,
                            option_key=key,
                            option_text=text,
                            is_correct=is_corr,
                            why_wrong_explanation=why_wrong
                        )
                        db.add(opt)
        db.commit()

        # 7. Coding Problems
        coding_problems_data = [
            {
                "topic_slug": "dsa",
                "title": "Two Sum",
                "slug": "two-sum",
                "diff": "Easy",
                "category": "Arrays & Hashing",
                "desc": "Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.\n\nYou may assume that each input would have exactly one solution, and you may not use the same element twice.\n\nYou can return the answer in any order.",
                "input_format": "Array of integers `nums`, integer `target`",
                "output_format": "Array of two integer indices `[i, j]`",
                "constraints": "2 <= nums.length <= 10^4\n-10^9 <= nums[i] <= 10^9\n-10^9 <= target <= 10^9\nOnly one valid answer exists.",
                "sample_input": "nums = [2,7,11,15], target = 9",
                "sample_output": "[0, 1]",
                "test_cases": [
                    {"input": "nums = [2,7,11,15], target = 9", "output": "[0, 1]"},
                    {"input": "nums = [3,2,4], target = 6", "output": "[1, 2]"},
                    {"input": "nums = [3,3], target = 6", "output": "[0, 1]"}
                ],
                "time_comp": "O(N)",
                "space_comp": "O(N)",
                "hints": [
                    "A brute force approach checks all pairs in O(N^2) time. Can we do better with a Hash Map?",
                    "As you iterate, calculate complement = target - nums[i]. Check if complement already exists in the map."
                ],
                "explanation": "Use a hash map to store each number and its index. For each element `nums[i]`, compute `complement = target - nums[i]`. If `complement` is in the map, return `[map[complement], i]`. Otherwise, insert `nums[i]: i` into the map.",
                "ext_url": "https://leetcode.com/problems/two-sum/",
                "ext_platform": "LeetCode",
                "py": """def twoSum(nums: list[int], target: int) -> list[int]:
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
""",
                "js": """function twoSum(nums, target) {
    const seen = new Map();
    for (let i = 0; i < nums.length; i++) {
        const complement = target - nums[i];
        if (seen.has(complement)) {
            return [seen.get(complement), i];
        }
        seen.set(nums[i], i);
    }
    return [];
}
""",
                "java": """class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (map.containsKey(complement)) {
                return new int[] { map.get(complement), i };
            }
            map.put(nums[i], i);
        }
        return new int[] {};
    }
}
""",
                "cpp": """class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> seen;
        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            if (seen.find(complement) != seen.end()) {
                return {seen[complement], i};
            }
            seen[nums[i]] = i;
        }
        return {};
    }
};
"""
            },
            {
                "topic_slug": "dsa",
                "title": "Valid Parentheses",
                "slug": "valid-parentheses",
                "diff": "Easy",
                "category": "Stacks",
                "desc": "Given a string `s` containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.\n\nAn input string is valid if:\n1. Open brackets must be closed by the same type of brackets.\n2. Open brackets must be closed in the correct order.\n3. Every close bracket has a corresponding open bracket of the same type.",
                "input_format": "A single string `s` consisting of parentheses.",
                "output_format": "Boolean `true` or `false`",
                "constraints": "1 <= s.length <= 10^4\n`s` consists of parentheses only '()[]{}'.",
                "sample_input": "s = '()[]{}'",
                "sample_output": "true",
                "test_cases": [
                    {"input": "s = '()'", "output": "true"},
                    {"input": "s = '()[]{}'", "output": "true"},
                    {"input": "s = '(]'", "output": "false"}
                ],
                "time_comp": "O(N)",
                "space_comp": "O(N)",
                "hints": [
                    "Which data structure follows Last-In, First-Out (LIFO)?",
                    "Push opening brackets onto a stack. When a closing bracket arrives, verify if the top of the stack matches."
                ],
                "explanation": "Iterate through the string. If the character is an opening bracket, push it onto a stack. If it is a closing bracket, check if the stack is non-empty and the top matches. At the end, return true if the stack is completely empty.",
                "ext_url": "https://leetcode.com/problems/valid-parentheses/",
                "ext_platform": "LeetCode",
                "py": """def isValid(s: str) -> bool:
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack
""",
                "js": """function isValid(s) {
    const stack = [];
    const map = { ')': '(', '}': '{', ']': '[' };
    for (const char of s) {
        if (map[char]) {
            if (stack.pop() !== map[char]) return false;
        } else {
            stack.push(char);
        }
    }
    return stack.length === 0;
}
""",
                "java": """class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        for (char c : s.toCharArray()) {
            if (c == '(') stack.push(')');
            else if (c == '{') stack.push('}');
            else if (c == '[') stack.push(']');
            else if (stack.isEmpty() || stack.pop() != c) return false;
        }
        return stack.isEmpty();
    }
}
""",
                "cpp": """class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        for (char c : s) {
            if (c == '(' || c == '{' || c == '[') st.push(c);
            else {
                if (st.empty()) return false;
                if (c == ')' && st.top() != '(') return false;
                if (c == '}' && st.top() != '{') return false;
                if (c == ']' && st.top() != '[') return false;
                st.pop();
            }
        }
        return st.empty();
    }
};
"""
            },
            {
                "topic_slug": "dsa",
                "title": "Merge Intervals",
                "slug": "merge-intervals",
                "diff": "Medium",
                "category": "Sorting & Arrays",
                "desc": "Given an array of `intervals` where `intervals[i] = [start_i, end_i]`, merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.",
                "input_format": "2D array of integer intervals `[[start, end], ...]`",
                "output_format": "2D array of merged intervals",
                "constraints": "1 <= intervals.length <= 10^4\nintervals[i].length == 2\n0 <= start_i <= end_i <= 10^4",
                "sample_input": "intervals = [[1,3],[2,6],[8,10],[15,18]]",
                "sample_output": "[[1,6],[8,10],[15,18]]",
                "test_cases": [
                    {"input": "intervals = [[1,3],[2,6],[8,10],[15,18]]", "output": "[[1,6],[8,10],[15,18]]"},
                    {"input": "intervals = [[1,4],[4,5]]", "output": "[[1,5]]"}
                ],
                "time_comp": "O(N log N)",
                "space_comp": "O(N)",
                "hints": [
                    "If intervals are sorted by their start time, all overlapping intervals become contiguous in the list.",
                    "Compare current interval start time with previous merged interval end time."
                ],
                "explanation": "Sort intervals by start time. Iterate through sorted intervals: if current interval starts after previous interval ends, append it as a new interval. Otherwise, merge by setting previous end = max(previous end, current end).",
                "ext_url": "https://leetcode.com/problems/merge-intervals/",
                "ext_platform": "LeetCode",
                "py": """def merge(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged
""",
                "js": """function merge(intervals) {
    if (!intervals.length) return [];
    intervals.sort((a, b) => a[0] - b[0]);
    const merged = [intervals[0]];
    for (let i = 1; i < intervals.length; i++) {
        const prev = merged[merged.length - 1];
        const curr = intervals[i];
        if (curr[0] <= prev[1]) {
            prev[1] = Math.max(prev[1], curr[1]);
        } else {
            merged.push(curr);
        }
    }
    return merged;
}
""",
                "java": """class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
        List<int[]> merged = new ArrayList<>();
        for (int[] interval : intervals) {
            if (merged.isEmpty() || merged.get(merged.size() - 1)[1] < interval[0]) {
                merged.add(interval);
            } else {
                merged.get(merged.size() - 1)[1] = Math.max(merged.get(merged.size() - 1)[1], interval[1]);
            }
        }
        return merged.toArray(new int[merged.size()][]);
    }
}
""",
                "cpp": """class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end());
        vector<vector<int>> merged;
        for (auto& interval : intervals) {
            if (merged.empty() || merged.back()[1] < interval[0]) {
                merged.push_back(interval);
            } else {
                merged.back()[1] = max(merged.back()[1], interval[1]);
            }
        }
        return merged;
    }
};
"""
            }
        ]

        for p_data in coding_problems_data:
            t = topic_map.get(p_data["topic_slug"])
            if t:
                existing_p = db.query(CodingProblem).filter(CodingProblem.slug == p_data["slug"]).first()
                if not existing_p:
                    p = CodingProblem(
                        topic_id=t.id,
                        title=p_data["title"],
                        slug=p_data["slug"],
                        difficulty=p_data["diff"],
                        category=p_data["category"],
                        description=p_data["desc"],
                        input_format=p_data["input_format"],
                        output_format=p_data["output_format"],
                        constraints=p_data["constraints"],
                        sample_input=p_data["sample_input"],
                        sample_output=p_data["sample_output"],
                        test_cases_json=p_data["test_cases"],
                        time_complexity=p_data["time_comp"],
                        space_complexity=p_data["space_comp"],
                        hints=p_data["hints"],
                        solution_explanation=p_data["explanation"],
                        external_url=p_data["ext_url"],
                        external_platform=p_data["ext_platform"],
                        starter_code_python=p_data["py"],
                        starter_code_javascript=p_data["js"],
                        starter_code_java=p_data["java"],
                        starter_code_cpp=p_data["cpp"]
                    )
                    db.add(p)
        db.commit()

        # 8. Add sample activity event for demo student
        if student_user:
            act = db.query(ActivityEvent).filter(ActivityEvent.user_id == student_user.id).first()
            if not act:
                db.add(ActivityEvent(
                    user_id=student_user.id,
                    event_type="onboarding",
                    title="Completed Placement Onboarding",
                    details="Configured target role: Software Developer (Python)",
                    metadata_json={"role": "Software Developer"},
                    created_at=utc_now()
                ))
                db.commit()

        # 9. Seed the full 500+ Aptitude & 300+ Coding banks
        try:
            from app.seeds.seed_large_banks import seed_large_banks
            seed_large_banks()
        except Exception as e:
            print("[Seed] Note on large banks:", e)

        print("[Seed] Database seed completed successfully!")
    finally:
        db.close()

if __name__ == "__main__":
    seed_database()
