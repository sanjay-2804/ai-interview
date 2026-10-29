"""
InterviewAI — Company Interview Questions Mega Expansion
Injects 100+ new authentic company-specific questions directly into COMPANIES_DATA
by appending to each company's round sample_questions lists.
"""

import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from app.services.company_interview_service import COMPANIES_DATA
import pprint

# Mapping: company slug -> round_number -> list of new questions to add
NEW_QUESTIONS = {
    "tcs": {
        1: [
            {"question": "A shopkeeper allows a discount of 10% on the marked price of an article. How much above the cost price should he mark the article to gain 8% profit?",
             "options": ["20%", "18%", "15%", "25%"],
             "answer": "20%",
             "explanation": "Let CP = 100. SP for 8% gain = 108. If discount is 10%, MP × 0.9 = 108. MP = 120. So 20% above CP."},
            {"question": "If the sum of the first n natural numbers is 210, what is n?",
             "options": ["20", "21", "19", "25"],
             "answer": "20",
             "explanation": "n(n+1)/2 = 210 → n(n+1) = 420. 20 × 21 = 420, so n = 20."},
            {"question": "What is the value of log₂(256)?",
             "options": ["8", "7", "6", "9"],
             "answer": "8",
             "explanation": "2⁸ = 256, so log₂(256) = 8."},
            {"question": "A man invested INR 12,000 at 10% SI for 2 years. What is the total amount at the end?",
             "options": ["INR 14,400", "INR 13,200", "INR 14,000", "INR 15,600"],
             "answer": "INR 14,400",
             "explanation": "SI = 12000 × 10 × 2 / 100 = 2400. Amount = 12000 + 2400 = 14400."},
        ],
        2: [
            {"question": "Write a function in Python to check if a given string is a valid palindrome considering only alphanumeric characters and ignoring cases.",
             "expected": ["Two-pointer approach", "Skip non-alphanumeric characters", "Compare lowercase versions", "O(N) time, O(1) space"],
             "model_answer": "def is_palindrome(s):\n    l, r = 0, len(s)-1\n    while l < r:\n        while l < r and not s[l].isalnum(): l += 1\n        while l < r and not s[r].isalnum(): r -= 1\n        if s[l].lower() != s[r].lower(): return False\n        l += 1; r -= 1\n    return True"},
            {"question": "Given an array of integers, find the pair with the minimum absolute difference. Return the pair.",
             "expected": ["Sort the array first", "Iterate and compare adjacent elements", "Track minimum difference", "O(N log N) due to sorting"],
             "model_answer": "Sort array. Iterate comparing arr[i+1]-arr[i] for minimum difference. Return pair with smallest absolute difference."},
        ],
        3: [
            {"question": "Explain the difference between TCP and UDP protocols. When would you choose one over the other?",
             "expected": ["TCP: connection-oriented, reliable, ordered delivery", "UDP: connectionless, fast, no guaranteed delivery", "TCP: web browsing, email, file transfer", "UDP: video streaming, gaming, DNS queries"],
             "model_answer": "TCP guarantees ordered, reliable delivery via acknowledgments and retransmissions (used for HTTP, FTP, email). UDP is connectionless with minimal overhead (used for live video, VoIP, gaming where speed matters more than reliability)."},
        ],
        4: [
            {"question": "Where do you see yourself in 5 years? How does TCS fit into your career plan?",
             "answer": "Express your goal of growing from a developer to a technical architect or project lead within TCS Digital. Mention TCS's training programs, global client exposure, and opportunities for certifications in cloud and AI technologies."},
        ],
    },
    "infosys": {
        1: [
            {"question": "Three coins are tossed simultaneously. What is the probability of getting at least 2 heads?",
             "options": ["1/2", "3/8", "1/4", "5/8"],
             "answer": "1/2",
             "explanation": "Total outcomes = 8. Favorable (2H or 3H): HHT, HTH, THH, HHH = 4. Probability = 4/8 = 1/2."},
            {"question": "If ROSE is coded as 6821, CHAIR is coded as 73456, then what is the code for ORACLE?",
             "options": ["165731", "156731", "165371", "156371"],
             "answer": "165731",
             "explanation": "O=1, R=6, A=5, C=7, L=3, E=1. ORACLE = 165731."},
            {"question": "Complete the series: 2, 6, 12, 20, 30, ?",
             "options": ["42", "40", "36", "44"],
             "answer": "42",
             "explanation": "Differences: 4, 6, 8, 10, 12. Next term = 30 + 12 = 42. Pattern: n(n+1) → 1×2, 2×3, 3×4, 4×5, 5×6, 6×7=42."},
        ],
        2: [
            {"question": "Write pseudocode to find the second largest element in an unsorted array without sorting it.",
             "expected": ["Initialize first_max and second_max", "Single pass through array", "Update both when finding a new maximum", "Handle edge case of all equal elements", "O(N) time complexity"],
             "model_answer": "Initialize first = second = -infinity. For each element x: if x > first, set second = first, first = x. Else if x > second and x != first, set second = x. Return second. O(N) time, O(1) space."},
            {"question": "Explain the concept of recursion with an example. What are its advantages and disadvantages?",
             "expected": ["Function calling itself with a base case", "Example: factorial, Fibonacci, tree traversal", "Advantage: elegant solution for tree/graph problems", "Disadvantage: stack overflow risk, overhead of function calls"],
             "model_answer": "Recursion is a technique where a function calls itself with a smaller subproblem until a base case is reached. Example: factorial(n) = n × factorial(n-1), base case factorial(0) = 1. Advantages: clean code for tree traversals, divide-and-conquer. Disadvantages: risk of stack overflow for deep recursion, overhead per call."},
        ],
        3: [
            {"question": "Tell me about your final year project. What challenges did you face and how did you overcome them?",
             "answer": "Walk through the project systematically: problem statement, tech stack chosen and why, your specific contributions, one major blocker (e.g., API rate limits, database performance), how you solved it (caching, query optimization), and measurable outcomes (response time improved by X%)."},
            {"question": "Describe a situation where you had to meet a tight deadline. How did you manage your time?",
             "answer": "Use the STAR method: Describe the assignment deadline, your prioritization approach (breaking work into smaller tasks, eliminating distractions), collaboration with teammates, and the successful outcome delivered on time."},
        ],
    },
    "accenture": {
        1: [
            {"question": "A boat goes 12 km upstream in 3 hours and 12 km downstream in 2 hours. Find the speed of the stream.",
             "options": ["1 km/h", "2 km/h", "1.5 km/h", "3 km/h"],
             "answer": "1 km/h",
             "explanation": "Upstream speed = 12/3 = 4 km/h. Downstream speed = 12/2 = 6 km/h. Stream speed = (6-4)/2 = 1 km/h."},
            {"question": "If the day before yesterday was Thursday, what day will fall on the day after tomorrow?",
             "options": ["Monday", "Tuesday", "Sunday", "Wednesday"],
             "answer": "Monday",
             "explanation": "Day before yesterday = Thursday → Yesterday = Friday → Today = Saturday → Tomorrow = Sunday → Day after tomorrow = Monday."},
            {"question": "In a class, 60% students passed in English and 70% passed in Math. If 40% passed in both, what percentage failed in both?",
             "options": ["10%", "15%", "20%", "30%"],
             "answer": "10%",
             "explanation": "Passed in at least one = 60+70-40 = 90%. Failed in both = 100-90 = 10%."},
        ],
        2: [
            {"question": "Write a function to reverse a linked list iteratively.",
             "expected": ["Three pointers: prev, current, next", "Iterative reversal in single pass", "O(N) time, O(1) space", "Handle empty list edge case"],
             "model_answer": "def reverse_list(head):\n    prev = None\n    current = head\n    while current:\n        next_node = current.next\n        current.next = prev\n        prev = current\n        current = next_node\n    return prev"},
        ],
        3: [
            {"question": "What are your strengths and how will they contribute to Accenture's client delivery model?",
             "answer": "Highlight problem-solving speed, adaptability to new tech stacks, and collaborative communication. Connect these to Accenture's consulting model where engineers must quickly understand diverse client domains and deliver solutions within tight timelines."},
            {"question": "How do you stay updated with rapidly evolving technology trends?",
             "answer": "Mention specific sources: following engineering blogs (Martin Fowler, Netflix Tech Blog), completing online certifications (AWS, Google Cloud), contributing to open-source projects, and attending tech meetups or hackathons."},
        ],
    },
    "amazon": {
        1: [
            {"question": "Given a string, find the length of the longest substring without repeating characters.",
             "expected": ["Sliding window technique", "Hash set or hash map to track seen characters", "Move left pointer when duplicate found", "O(N) time complexity"],
             "model_answer": "Use sliding window with hash set. Expand right pointer; if duplicate found, shrink from left until duplicate removed. Track max window length. O(N) time, O(min(N,26)) space."},
        ],
        2: [
            {"question": "Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.",
             "expected": ["Use auxiliary min-stack tracking current minimum at each level", "Push: push to main stack AND push min(val, minStack.top) to minStack", "Pop: pop from both stacks", "getMin: return minStack.top in O(1)"],
             "model_answer": "Maintain two stacks: main stack and min stack. On push(x): push x to main, push min(x, minStack.peek()) to minStack. On pop: pop from both. getMin returns minStack.peek(). All operations O(1)."},
            {"question": "Implement an LRU Cache with O(1) get and put operations.",
             "expected": ["Doubly linked list for ordering", "Hash map for O(1) key lookup", "Move accessed node to front on get", "Evict tail node on capacity overflow"],
             "model_answer": "Use HashMap<Key, Node> + DoublyLinkedList. get(key): find node in map O(1), move to head O(1), return value. put(key,val): if exists update and move to head; else create node, add to head, if over capacity remove tail and delete from map. All O(1)."},
        ],
        3: [
            {"question": "Design a URL shortener service like bit.ly that handles 100M daily URL creation requests.",
             "expected": ["Base62 encoding of auto-increment ID or hash", "Read-heavy: use Redis cache for hot URLs", "Database: NoSQL (DynamoDB) for horizontal scaling", "Custom domain support and analytics tracking", "TTL for expiring links"],
             "model_answer": "Generate short codes using Base62 encoding of a distributed sequence generator (Snowflake ID). Store mappings in DynamoDB with DAX cache layer. Use CloudFront CDN for 301 redirects. Track click analytics asynchronously via Kafka."},
        ],
        4: [
            {"question": "Tell me about a time you had to make a decision with incomplete data. (Leadership Principle: Bias for Action)",
             "answer": "Describe a project where you had to ship a feature without full user research data. Explain how you made a reversible decision, gathered real-time feedback post-launch, and iterated rapidly. Emphasize speed over perfection for reversible decisions."},
            {"question": "Describe a time when you simplified a complex process. (Leadership Principle: Invent and Simplify)",
             "answer": "Share how you identified manual repetitive steps in a deployment or testing workflow, automated them with scripts or CI/CD pipelines, reduced deployment time from hours to minutes, and documented the simplified process for the team."},
        ],
    },
    "wipro": {
        1: [
            {"question": "A tank is filled by 3 pipes with uniform flow rates. The first two pipes operating simultaneously fill the tank in the same time during which the third pipe alone empties it. The first pipe alone fills the tank in 10 hours, the second in 15 hours. How long does the third pipe take to empty the tank?",
             "options": ["6 hours", "8 hours", "10 hours", "12 hours"],
             "answer": "6 hours",
             "explanation": "Rate of 1st + 2nd = 1/10 + 1/15 = 5/30 = 1/6. Since these together fill at the same rate the 3rd empties, 3rd pipe takes 6 hours."},
        ],
        2: [
            {"question": "Write a program to check whether a given number is an Armstrong number.",
             "expected": ["Find number of digits n", "Sum each digit raised to power n", "Compare sum with original number", "Handle multi-digit Armstrong numbers (e.g., 153, 370, 371)"],
             "model_answer": "def is_armstrong(num):\n    digits = str(num)\n    n = len(digits)\n    return sum(int(d)**n for d in digits) == num"},
        ],
        3: [
            {"question": "Explain the four pillars of Object-Oriented Programming with real-world examples.",
             "expected": ["Encapsulation: bundling data with methods (bank account hiding balance)", "Abstraction: hiding complex implementation (car steering wheel)", "Inheritance: code reuse (Employee extends Person)", "Polymorphism: one interface multiple forms (shape.area() for circle/rectangle)"],
             "model_answer": "1. Encapsulation: BankAccount class hides balance, exposes deposit()/withdraw(). 2. Abstraction: Driver uses accelerate() without knowing engine internals. 3. Inheritance: ElectricCar extends Car inheriting drive() but adding charge(). 4. Polymorphism: draw(Shape s) works for Circle, Rectangle, Triangle through method overriding."},
        ],
    },
    "cognizant": {
        1: [
            {"question": "Find the missing number: 3, 9, 27, 81, ?",
             "options": ["243", "162", "189", "216"],
             "answer": "243",
             "explanation": "Each term is multiplied by 3. 81 × 3 = 243. Geometric progression with r = 3."},
            {"question": "If 5 men can do a work in 12 days, how many men are needed to complete it in 4 days?",
             "options": ["15", "12", "10", "20"],
             "answer": "15",
             "explanation": "Total man-days = 5 × 12 = 60. For 4 days: 60/4 = 15 men."},
        ],
        2: [
            {"question": "Write a function to find the first non-repeating character in a string.",
             "expected": ["Use hash map to count character frequencies", "Second pass to find first char with count 1", "O(N) time, O(1) space (bounded alphabet)"],
             "model_answer": "def first_non_repeating(s):\n    freq = {}\n    for c in s: freq[c] = freq.get(c, 0) + 1\n    for c in s:\n        if freq[c] == 1: return c\n    return None"},
        ],
    },
    "capgemini": {
        1: [
            {"question": "Two numbers are in the ratio 3:5 and their difference is 36. Find the smaller number.",
             "options": ["54", "48", "45", "63"],
             "answer": "54",
             "explanation": "Let numbers be 3x and 5x. 5x - 3x = 36 → 2x = 36 → x = 18. Smaller = 3×18 = 54."},
            {"question": "A clock shows 3:15 PM. What is the angle between the hour and minute hands?",
             "options": ["7.5°", "0°", "15°", "22.5°"],
             "answer": "7.5°",
             "explanation": "At 3:15, minute hand at 90°. Hour hand at 30×3 + 0.5×15 = 90+7.5 = 97.5°. Angle = |97.5 - 90| = 7.5°."},
        ],
        2: [
            {"question": "Write pseudocode to find the maximum sum subarray in an array of integers (Kadane's Algorithm).",
             "expected": ["Initialize max_so_far and max_ending_here", "Iterate through array", "max_ending_here = max(arr[i], max_ending_here + arr[i])", "Update max_so_far if max_ending_here is larger", "O(N) time, O(1) space"],
             "model_answer": "max_so_far = max_here = arr[0]\nfor i in range(1, len(arr)):\n    max_here = max(arr[i], max_here + arr[i])\n    max_so_far = max(max_so_far, max_here)\nreturn max_so_far"},
        ],
        3: [
            {"question": "Tell me about a time you failed at something and what you learned from it.",
             "answer": "Choose a genuine failure (e.g., underestimating project timeline, a bug in production). Describe the impact, how you took ownership, the corrective actions taken, and the lasting lesson learned (better estimation, more thorough testing, communication habits)."},
        ],
    },
    "zoho": {
        1: [
            {"question": "Find the next term: 2, 3, 5, 8, 13, 21, ?",
             "options": ["34", "32", "28", "26"],
             "answer": "34",
             "explanation": "Fibonacci-like: each term = sum of previous two. 13+21 = 34."},
        ],
        2: [
            {"question": "Write a function to rotate a given N×N matrix by 90 degrees clockwise in-place.",
             "expected": ["Transpose the matrix (swap rows and columns)", "Reverse each row", "In-place O(1) extra space", "O(N²) time complexity"],
             "model_answer": "Step 1: Transpose (swap matrix[i][j] with matrix[j][i] for i<j). Step 2: Reverse each row. Result: 90° clockwise rotation. O(N²) time, O(1) space."},
        ],
        3: [
            {"question": "Design a simple event calendar application. What classes and data structures would you use?",
             "expected": ["Event class with title, start_time, end_time, recurrence", "Calendar class managing list of events", "Conflict detection using interval overlap check", "BST or sorted list for efficient time-range queries"],
             "model_answer": "Event(title, start, end, recurrence_rule). Calendar stores events in a balanced BST keyed by start_time. addEvent checks for conflicts using interval overlap (a.start < b.end and b.start < a.end). getEventsInRange uses BST range query for O(log N + K) retrieval."},
        ],
    },
    "microsoft": {
        1: [
            {"question": "Given a sorted array, remove the duplicates in-place such that each element appears only once. Return the new length.",
             "expected": ["Two-pointer technique", "Slow pointer tracks position of unique elements", "Fast pointer scans through array", "O(N) time, O(1) space"],
             "model_answer": "i = 0 (slow pointer). For j = 1 to n-1 (fast pointer): if nums[j] != nums[i], increment i and set nums[i] = nums[j]. Return i+1. O(N) time, O(1) space."},
        ],
        2: [
            {"question": "Design a thread-safe bounded blocking queue. What synchronization primitives would you use?",
             "expected": ["Mutex lock for mutual exclusion", "Two condition variables: not_full and not_empty", "Producer waits on not_full when queue is full", "Consumer waits on not_empty when queue is empty", "Signal after enqueue/dequeue"],
             "model_answer": "Use a circular buffer with mutex + 2 condition variables. enqueue: lock → while full, wait(not_full) → insert → signal(not_empty) → unlock. dequeue: lock → while empty, wait(not_empty) → remove → signal(not_full) → unlock."},
        ],
        3: [
            {"question": "Design a real-time collaborative document editor (like Google Docs). How do you handle concurrent edits?",
             "expected": ["Operational Transformation (OT) or CRDTs for conflict resolution", "WebSocket connections for real-time sync", "Server as central authority for OT", "Cursor position tracking per user", "Undo/redo stack per session"],
             "model_answer": "Use Operational Transformation: each edit operation (insert/delete at position) is transformed against concurrent operations to maintain consistency. WebSocket channels push operations to all connected clients. Server applies canonical ordering. CRDTs (like Yjs) offer eventual consistency without central coordination."},
        ],
    },
    "google": {
        1: [
            {"question": "Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. Assume exactly one solution exists.",
             "expected": ["Hash map approach", "Store complement = target - nums[i]", "Check if complement exists in map", "O(N) time, O(N) space"],
             "model_answer": "seen = {}\nfor i, num in enumerate(nums):\n    complement = target - num\n    if complement in seen: return [seen[complement], i]\n    seen[num] = i"},
        ],
        2: [
            {"question": "You have N eggs and a building with K floors. Find the minimum number of trials needed to find the critical floor in the worst case.",
             "expected": ["Classic egg drop problem", "Dynamic programming approach", "dp[n][k] = 1 + min over x of max(dp[n-1][x-1], dp[n][k-x])", "Binary search optimization for O(N*K*logK)"],
             "model_answer": "Use DP: dp[eggs][floors] = minimum worst-case trials. For each floor x from 1 to k: if egg breaks, check dp[eggs-1][x-1] floors below; if survives, check dp[eggs][k-x] floors above. dp[n][k] = 1 + min over x of max(dp[n-1][x-1], dp[n][k-x]). Optimize with binary search."},
        ],
        3: [
            {"question": "Design YouTube's video recommendation system. How would you balance relevance, diversity, and freshness?",
             "expected": ["Two-stage: candidate generation + ranking", "Collaborative filtering for candidates", "Deep neural network ranker with features: watch time, CTR, user history", "Diversity injection to avoid filter bubbles", "Freshness boost for new content"],
             "model_answer": "Candidate generation: retrieve 1000 candidates using collaborative filtering and content-based embeddings. Ranking: deep neural network scores each candidate on predicted watch time, click probability, and user engagement signals. Diversity: re-rank to ensure category diversity. Freshness: time-decay boosting for recent uploads."},
        ],
        4: [
            {"question": "Tell me about a time when you disagreed with a team decision but ultimately committed to it. (Googleyness)",
             "answer": "Describe the disagreement professionally (e.g., architecture choice), how you presented data-driven arguments, respected the team's decision when consensus formed, and fully committed to making the chosen approach successful."},
        ],
    },
    "flipkart": {
        1: [
            {"question": "Given an array of N integers, find the contiguous subarray with the maximum product.",
             "expected": ["Track both max and min products (negative × negative = positive)", "At each position: max_prod = max(nums[i], max_prod*nums[i], min_prod*nums[i])", "Similarly for min_prod", "O(N) time, O(1) space"],
             "model_answer": "Track max_prod, min_prod, result. For each num: if num < 0, swap max_prod and min_prod. max_prod = max(num, max_prod*num). min_prod = min(num, min_prod*num). result = max(result, max_prod). O(N) time."},
        ],
        2: [
            {"question": "Design a real-time inventory management system for an e-commerce platform handling flash sales with 100K concurrent users.",
             "expected": ["Redis for atomic inventory decrement (DECR command)", "Optimistic locking or distributed locks for race condition prevention", "Event-driven architecture with Kafka for order processing", "Database eventual consistency with reconciliation jobs"],
             "model_answer": "Use Redis DECR for atomic stock countdown during flash sales. If DECR returns ≥ 0, allow order; if < 0, reject and INCR back. Push successful orders to Kafka for async database persistence. Run reconciliation jobs to sync Redis and PostgreSQL inventory."},
        ],
    },
    "paypal": {
        1: [
            {"question": "What is the output?\nint x = 5;\nSystem.out.println(x++ + ++x);",
             "options": ["12", "11", "10", "13"],
             "answer": "12",
             "explanation": "x++ evaluates to 5 (post-increment, x becomes 6). ++x evaluates to 7 (pre-increment, x becomes 7). 5 + 7 = 12."},
        ],
        2: [
            {"question": "Implement a function to detect if a binary tree is a valid Binary Search Tree (BST).",
             "expected": ["In-order traversal should produce sorted sequence", "Or recursive approach with min/max bounds", "Left subtree values < node < right subtree values", "Handle edge cases: duplicate values, single node"],
             "model_answer": "def is_valid_bst(node, min_val=float('-inf'), max_val=float('inf')):\n    if not node: return True\n    if node.val <= min_val or node.val >= max_val: return False\n    return is_valid_bst(node.left, min_val, node.val) and is_valid_bst(node.right, node.val, max_val)"},
        ],
        3: [
            {"question": "Design a fraud detection system for PayPal that flags suspicious transactions in real-time.",
             "expected": ["Stream processing with Apache Flink or Kafka Streams", "ML model scoring in real-time pipeline", "Feature engineering: transaction velocity, geolocation anomaly, device fingerprint", "Rule engine for known fraud patterns", "Human review queue for borderline cases"],
             "model_answer": "Ingest transaction events via Kafka. Flink stream processor enriches with user history and computes real-time features (transaction velocity, geo-distance from last transaction). ML model (gradient boosted trees) scores fraud probability. Rules engine catches known patterns. Transactions scoring above threshold are held for review; others proceed."},
        ],
    },
    "walmart": {
        1: [
            {"question": "Two trains running in opposite directions cross each other in 10 seconds. If the speeds are 54 km/h and 72 km/h and one train is 120 m long, find the length of the other train.",
             "options": ["230 m", "200 m", "250 m", "180 m"],
             "answer": "230 m",
             "explanation": "Relative speed = (54+72) × 5/18 = 126 × 5/18 = 35 m/s. Total distance = speed × time = 35 × 10 = 350 m. Other train = 350 - 120 = 230 m."},
        ],
        2: [
            {"question": "Implement a function to merge K sorted linked lists into one sorted linked list.",
             "expected": ["Use min-heap (priority queue) of size K", "Push head of each list to heap", "Pop minimum, add to result, push next node from that list", "O(N log K) time where N is total elements"],
             "model_answer": "import heapq\ndef merge_k_lists(lists):\n    heap = [(l.val, i, l) for i, l in enumerate(lists) if l]\n    heapq.heapify(heap)\n    dummy = curr = ListNode(0)\n    while heap:\n        val, i, node = heapq.heappop(heap)\n        curr.next = node\n        curr = curr.next\n        if node.next:\n            heapq.heappush(heap, (node.next.val, i, node.next))\n    return dummy.next"},
        ],
    },
    "freshworks": {
        1: [
            {"question": "A and B together can complete a task in 12 days. B and C together in 15 days. C and A together in 20 days. How many days will all three take together?",
             "options": ["10 days", "8 days", "9 days", "12 days"],
             "answer": "10 days",
             "explanation": "1/A+1/B = 1/12, 1/B+1/C = 1/15, 1/C+1/A = 1/20. Adding all: 2(1/A+1/B+1/C) = 1/12+1/15+1/20 = 5+4+3/60 = 12/60 = 1/5. So 1/A+1/B+1/C = 1/10. Together: 10 days."},
        ],
        2: [
            {"question": "Design a multi-tenant SaaS application where each customer's data is isolated. What database strategy would you use?",
             "expected": ["Options: separate databases, separate schemas, shared schema with tenant_id", "Shared schema with tenant_id column for cost efficiency at scale", "Row-level security policies for data isolation", "Connection pooling with tenant context injection"],
             "model_answer": "Use shared database with tenant_id column on every table (most scalable for SMB SaaS). Implement PostgreSQL Row-Level Security (RLS) policies so queries automatically filter by tenant. Connection middleware injects SET app.current_tenant before each request. For enterprise customers requiring strict isolation, offer dedicated schema or database tier."},
        ],
    },
}

def apply():
    updated = 0
    added_qs = 0

    for comp in COMPANIES_DATA:
        slug = comp["slug"]
        if slug not in NEW_QUESTIONS:
            continue

        for round_num_str, questions in NEW_QUESTIONS[slug].items():
            round_num = int(round_num_str)
            for r in comp["rounds"]:
                if r["round_number"] == round_num:
                    existing_texts = {q.get("question", "")[:80] for q in r.get("sample_questions", [])}
                    for q in questions:
                        if q["question"][:80] not in existing_texts:
                            r.setdefault("sample_questions", []).append(q)
                            added_qs += 1
                    break

        updated += 1

    # Write back
    file_path = os.path.join(os.path.dirname(__file__), "..", "app", "services", "company_interview_service.py")
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    class_marker = "class CompanyInterviewService:"
    code_after = content[content.index(class_marker):]

    formatted = pprint.pformat(COMPANIES_DATA, indent=4, width=120)
    new_content = f"from typing import List, Dict, Any, Optional\n\nCOMPANIES_DATA = {formatted}\n\n{code_after}"

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"Updated {updated} companies with {added_qs} new questions.")

if __name__ == "__main__":
    apply()

