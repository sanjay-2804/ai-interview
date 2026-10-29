import sys
import os
import json

sys.path.insert(0, r'e:\MINI 2.0\backend')
from app.services.company_interview_service import COMPANIES_DATA

# Deep catalog of authentic interview questions for all companies
NEW_QUESTIONS = {
    "tcs": {
        1: [
            {
                "question": "What is the output of the following C program?\n#include <stdio.h>\nint main() {\n  int x = 10, y = 20;\n  printf('%d', x = y == 20);\n  return 0;\n}",
                "options": ["1", "0", "10", "20"],
                "answer": "1",
                "explanation": "Equality operator (==) has higher precedence than assignment (=). 'y == 20' evaluates to 1 (True). Then x is assigned 1, and 1 is printed."
            },
            {
                "question": "In a competitive race, A gives B a start of 40 meters in a 1000-meter race, and A wins by 19 seconds. If A gives B a start of 30 seconds, B wins by 40 meters. Find the speed of A.",
                "options": ["5 m/s", "6.25 m/s", "7.5 m/s", "8 m/s"],
                "answer": "6.25 m/s",
                "explanation": "Let speed of A be Va and speed of B be Vb. Time taken by A = 1000/Va. In case 1: 960/Vb - 1000/Va = 19. In case 2: 1000/Va - 960/Vb + 30 gives distance difference. Solving the linear system yields Va = 6.25 m/s."
            },
            {
                "question": "What is the time complexity of building a Binary Heap from an unordered array of N elements using the bottom-up Heapify approach?",
                "options": ["O(N)", "O(N log N)", "O(log N)", "O(N^2)"],
                "answer": "O(N)",
                "explanation": "Although inserting N elements one by one takes O(N log N), bottom-up Heapify sums the series N/4*(1) + N/8*(2) + N/16*(3)... which converges mathematically to O(N)."
            }
        ],
        2: [
            {
                "question": "Given a string S containing lowercase English alphabets, find the length of the longest substring without repeating characters.\nInput: 'abcabcbb'\nOutput: 3 (The answer is 'abc').",
                "expected": ["Sliding Window technique", "Hash Map or frequency array of characters", "O(N) time complexity and O(min(N, M)) space complexity"],
                "model_answer": "Use a sliding window with left and right pointers. Maintain a hash map storing the most recent index of each character. When a repeated character is encountered within the current window, move the left pointer to last_seen_index + 1. Track max_length."
            },
            {
                "question": "Given an array of positive integers representing daily stock prices, find the maximum profit you can achieve by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.\nInput: [7,1,5,3,6,4]\nOutput: 5 (Buy on day 2 at price 1 and sell on day 5 at price 6).",
                "expected": ["Single-pass tracking of min_price", "Calculate potential profit = price[i] - min_price", "O(N) time and O(1) space"],
                "model_answer": "Maintain a running variable 'min_price_so_far' initialized to infinity. Iterate through the array: update min_price_so_far = min(min_price_so_far, price), and max_profit = max(max_profit, price - min_price_so_far). Returns max_profit in O(N) time and O(1) space."
            }
        ],
        3: [
            {
                "question": "Why does a C++ base class with virtual functions always require a virtual destructor, and what happens if you omit it?",
                "expected": ["Virtual destructor ensures derived class destructor is called", "Prevents memory leaks and resource dangling when deleting derived object via base pointer", "vtable stores destructor entry point"]
            },
            {
                "question": "Explain Database Normalization from 1NF to BCNF with real-world examples. Under what production circumstances would you intentionally denormalize a schema?",
                "expected": ["1NF: Atomic values", "2NF: No partial dependency on composite key", "3NF: No transitive dependencies", "BCNF: Every determinant is a candidate key", "Denormalization used in read-heavy analytics/warehousing to avoid expensive multi-table JOINs"]
            }
        ],
        4: [
            {
                "question": "How do you handle working with a team member who is not pulling their weight or missing deadlines on a client deliverable?",
                "expected": ["Non-accusatory direct communication first", "Understanding root causes (clarity, skill gap, personal emergency)", "Offering pairing or breaking down tasks", "Escalating transparently to project manager if unresolved"]
            }
        ]
    },
    "infosys": {
        1: [
            {
                "question": "What is the output of the following pseudocode?\nInteger p, q, r\nSet p = 5, q = 11, r = 7\nIf ((p & q) < (q ^ r))\n  p = (q >> 1) + (r << 1)\nEnd If\nPrint p + q + r",
                "options": ["37", "32", "29", "41"],
                "answer": "37",
                "explanation": "p & q = 5 & 11 = 1. q ^ r = 11 ^ 7 = 12. Since 1 < 12, the condition is True. p = (11 >> 1) + (7 << 1) = 5 + 14 = 19. Result = 19 + 11 + 7 = 37."
            },
            {
                "question": "Statements: (1) All algorithms are logic. (2) Some logic is mathematics. Conclusions: (I) Some mathematics is algorithms. (II) Some logic is algorithms.",
                "options": ["Only Conclusion II follows", "Only Conclusion I follows", "Both I and II follow", "Neither follows"],
                "answer": "Only Conclusion II follows",
                "explanation": "Since all algorithms are logic, the converse 'Some logic is algorithms' is always true. However, there is no direct definite overlap between mathematics and algorithms, so I does not necessarily follow."
            }
        ],
        2: [
            {
                "question": "Given an array of integers sorted in ascending order that has been rotated at an unknown pivot, find the index of a target value in O(log N) time.\nInput: nums = [4,5,6,7,0,1,2], target = 0\nOutput: 4",
                "expected": ["Modified Binary Search", "Determine which half (left or right) is sorted", "Check if target lies in sorted half", "O(log N) time and O(1) space"],
                "model_answer": "In a rotated sorted array, dividing at mid always leaves at least one half strictly sorted. If nums[left] <= nums[mid], the left half is sorted. If target is within nums[left] and nums[mid], search left; otherwise search right. If right half is sorted, apply symmetric logic. Time complexity is O(log N)."
            },
            {
                "question": "Given coins of different denominations and a total amount of money, compute the fewest number of coins that you need to make up that amount. If that amount cannot be made up, return -1.\nInput: coins = [1,2,5], amount = 11\nOutput: 3 (11 = 5 + 5 + 1)",
                "expected": ["Dynamic Programming (Unbounded Knapsack)", "dp[i] = min(dp[i], dp[i - coin] + 1)", "O(amount * number of coins) time", "O(amount) space"],
                "model_answer": "Initialize dp array of size amount + 1 with infinity, dp[0] = 0. For each coin, iterate from coin to amount: dp[i] = min(dp[i], dp[i - coin] + 1). Return dp[amount] if not infinity else -1."
            }
        ],
        3: [
            {
                "question": "What is the difference between Synchronous and Asynchronous programming in modern backend systems? How does the Node.js Event Loop or Python asyncio handle non-blocking I/O?",
                "expected": ["Synchronous blocks calling thread until I/O completes", "Asynchronous registers callback/coroutine and yields execution to event loop", "Single-threaded event loop utilizes OS polling (epoll/kqueue) for high concurrency"]
            }
        ]
    },
    "amazon": {
        1: [
            {
                "question": "In an Amazon fulfillment center, an automated rover starts at (0,0) facing North. It receives instructions: 'G' (go 1 unit), 'L' (turn 90 deg left), 'R' (turn 90 deg right). Determine if the rover moves in a bounded circle forever.",
                "expected": ["Vector coordinate tracking", "Rover is bounded if position returns to (0,0) OR direction changes from initial North after 1 sequence cycle", "O(N) time and O(1) space"],
                "model_answer": "Simulate one cycle of instructions with direction vectors (dx, dy). If the rover returns to (0,0) or does not face North at the end of the sequence, repeating the sequence 4 times will guarantee returning to the starting point. Thus the robot is bounded."
            },
            {
                "question": "You have N sticks with given positive lengths. You can connect any two sticks of lengths X and Y with cost X + Y. Find the minimum total cost to connect all sticks into one.",
                "expected": ["Min-Heap (Priority Queue)", "Greedy strategy: always connect two smallest sticks", "O(N log N) time complexity"],
                "model_answer": "Insert all stick lengths into a Min-Heap. While heap size > 1, extract the two smallest elements, sum them, add the sum to total cost, and insert the sum back into the heap. Returns optimal Huffman-like minimum cost."
            }
        ],
        2: [
            {
                "question": "Design and implement a Least Recently Used (LRU) Cache with get(key) and put(key, value) operations running in strictly O(1) average time complexity.",
                "expected": ["Doubly Linked List + Hash Map", "Hash Map maps key to node pointer", "Doubly Linked List maintains access recency with O(1) node relocation", "Capacity eviction removes tail node in O(1)"],
                "model_answer": "Use a Hash Map paired with a Doubly Linked List with dummy head and tail nodes. get(key): lookup node in map, move to head, return value. put(key, val): if key exists, update value and move to head. If new, create node, put in map and at head. If capacity exceeded, remove node before tail and delete from map."
            },
            {
                "question": "Given the root of a binary tree, find the Lowest Common Ancestor (LCA) of two given nodes p and q.",
                "expected": ["Recursive tree traversal", "Base cases: root is None, root == p, root == q", "If left and right recursive calls both return non-null, root is LCA", "O(N) time and O(H) space"],
                "model_answer": "Base case: if root is None, p, or q, return root. Recursively search left = LCA(root.left, p, q) and right = LCA(root.right, p, q). If both left and right are non-null, p and q are in separate subtrees, so root is LCA. If only one is non-null, propagate that node upward."
            }
        ],
        3: [
            {
                "question": "Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.\nInput: s = 'leetcode', wordDict = ['leet', 'code']\nOutput: true",
                "expected": ["Dynamic Programming with Hash Set", "dp[i] = true if s[0:i] can be segmented", "Check dp[j] and s[j:i] in wordDict for j in range 0..i", "O(N^2) time and O(N) space"],
                "model_answer": "Store wordDict in a Hash Set. Declare dp array of size len(s)+1 with dp[0] = True. For i from 1 to len(s), iterate j from 0 to i. If dp[j] is True and s[j:i] is in the word set, set dp[i] = True and break. Returns dp[len(s)]."
            }
        ],
        4: [
            {
                "question": "Tell me about a time you had a strong technical disagreement with your team lead or peer. How did you handle it and what was the outcome? (Amazon Leadership Principle: Have Backbone; Disagree and Commit)",
                "expected": ["STAR structure", "Objective data and benchmarks used instead of emotional debate", "Respectful listening and debate", "Fully committing to the agreed path regardless of personal preference", "Measurable positive result"]
            },
            {
                "question": "Give an example of a time you had to make a high-stakes technical decision without complete data or under severe time pressure. (Amazon Leadership Principle: Bias for Action)",
                "expected": ["Two-way door vs one-way door decision framework", "Risk assessment and rollback plan", "Speed of execution and bias for action", "Post-launch metrics tracking"]
            }
        ]
    },
    "zoho": {
        1: [
            {
                "question": "What is the output of the following C code snippet?\n#include <stdio.h>\nint main() {\n  int arr[] = {10, 20, 30, 40, 50};\n  int *ptr = arr;\n  printf('%d ', *ptr++);\n  printf('%d', *++ptr);\n  return 0;\n}",
                "options": ["10 30", "10 20", "20 30", "10 40"],
                "answer": "10 30",
                "explanation": "*ptr++ dereferences first (prints 10) then increments pointer to 20. Then *++ptr increments pointer first (to 30) then dereferences, printing 30."
            },
            {
                "question": "What will be printed by this C program?\n#include <stdio.h>\nvoid fun(int n) {\n  if (n <= 0) return;\n  printf('%d ', n);\n  fun(n - 2);\n  printf('%d ', n);\n}\nint main() {\n  fun(5);\n  return 0;\n}",
                "options": ["5 3 1 1 3 5", "5 3 1", "1 3 5 5 3 1", "5 4 3 2 1"],
                "answer": "5 3 1 1 3 5",
                "explanation": "Head recursion prints 5, then 3, then 1. As the call stack unwinds, tail prints 1, 3, 5."
            }
        ],
        2: [
            {
                "question": "Given an odd-length string, print the string in an 'X' pattern diagonally from both corners.\nInput: 'PROGRAM'\nOutput:\nP     M\n R   A \n  O R  \n   G   \n  O R  \n R   A \nP     M",
                "expected": ["Nested loops iterating row i and col j", "Print char at j when j == i or j == len - 1 - i", "Print space otherwise", "O(N^2) time and O(1) auxiliary space"],
                "model_answer": "Let N = len(string). Outer loop i from 0 to N-1, inner loop j from 0 to N-1. If j == i: print string[i]. Else if j == N - 1 - i: print string[N - 1 - i]. Else: print space. Print newline at end of inner loop."
            }
        ],
        3: [
            {
                "question": "Design a Low-Level Object-Oriented Railway Ticket Reservation System with Berths (Lower, Middle, Upper, RAC, Waiting List) and automatic berth allocation based on passenger age and gender preferences.",
                "expected": ["Class definitions: Passenger, Ticket, Train, ReservationSystem", "Allocation rules: Senior citizens & pregnant women get Lower berths", "RAC and WL queues management on cancellation", "Encapsulation, Modular design, and Clean separation of concerns"],
                "model_answer": "Design Passenger with attributes (id, name, age, gender, berth_preference). ReservationSystem maintains lists for Confirmed (63 berths), RAC (18 berths), and Waiting List (10). On booking, check preference: if senior/female with child, prefer lower. If full, allocate RAC; if RAC full, allocate WL. On cancellation, promote first RAC to confirmed and first WL to RAC."
            }
        ]
    },
    "walmart": {
        1: [
            {
                "question": "What is the optimal data structure to support Top-K search recommendations in Walmart's search bar with sub-millisecond query latency?",
                "options": ["Trie augmented with Min-Heaps at each node", "Unindexed SQLite database", "B+ Tree on disk", "Unsorted circular linked list"],
                "answer": "Trie augmented with Min-Heaps at each node",
                "explanation": "A Trie stores prefixes; storing top-K search frequencies directly at nodes allows O(L) prefix lookup without searching the entire sub-tree."
            }
        ],
        2: [
            {
                "question": "Given an array of integers nums and a sliding window of size k moving from left to right, return the max sliding window.\nInput: nums = [1,3,-1,-3,5,3,6,7], k = 3\nOutput: [3,3,5,5,6,7]",
                "expected": ["Monotonic Deque storing indices", "Maintain strictly decreasing elements in deque", "Evict out-of-window indices from front", "O(N) time and O(K) space"],
                "model_answer": "Use a Double-ended Queue (deque) that maintains indices in monotonically decreasing order of values. For each index i: remove indices from back whose values are <= nums[i]. Remove front index if it falls outside [i - k + 1, i]. Append i. When i >= k - 1, the front of the deque is the maximum for the current window."
            }
        ],
        3: [
            {
                "question": "How do you handle distributed transactions and event consistency across Order, Payment, and Stock services in Walmart's e-commerce backend during high-concurrency flash sales?",
                "expected": ["Saga Pattern (Orchestration with Kafka/Temporal)", "Compensating transactions on failure", "Outbox pattern for atomic DB write + Kafka message emission", "Idempotency keys on all payment webhooks"],
                "model_answer": "Avoid blocking Two-Phase Commit. Use the Saga pattern: an Order Orchestrator sends events via Kafka. Transactional Outbox pattern guarantees the DB commit and message dispatch occur atomically. If stock reservation fails, compensating events trigger payment refunds and order cancellation."
            }
        ]
    },
    "flipkart": {
        1: [
            {
                "question": "Design a low-level object-oriented Parking Lot System supporting multiple spot types (Motorcycle, Compact, Large), automated ticket generation, and fee calculation based on duration.",
                "expected": ["Clean classes: ParkingLot, Floor, ParkingSpot, Vehicle (Motorcycle, Car, Truck), Ticket", "Strategy pattern for pricing calculation", "Thread-safe spot assignment using locks", "Clean API: park_vehicle(), unpark_vehicle()"],
                "model_answer": "Define abstract Vehicle class with subclasses Car, Bike, Truck. ParkingSpot has SpotType and is_available. Floor contains list of spots. ParkingLot singleton manages floors. park(vehicle) finds first matching spot, marks occupied, generates Ticket with timestamp. unpark(ticket) calculates fee via PricingStrategy, frees spot."
            }
        ],
        2: [
            {
                "question": "Given n jobs where every job has a start time, end time, and profit, find the maximum profit you can achieve such that no two jobs overlap.\nInput: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]\nOutput: 120",
                "expected": ["Sort jobs by end time", "Dynamic programming: dp[i] = max(dp[i-1], job.profit + dp[latest_non_conflicting])", "Binary search (bisect) to find non-conflicting job in O(log N)", "O(N log N) total time"],
                "model_answer": "Sort jobs by end time. Define dp[i] as maximum profit using a subset of first i jobs. For job i, use binary search to find the latest job j whose end time <= job[i].start. dp[i] = max(dp[i-1], job[i].profit + dp[j]). Total runtime is O(N log N)."
            }
        ]
    },
    "freshworks": {
        1: [
            {
                "question": "In a multitenant SaaS CRM database like Freshsales, which architectural partitioning approach provides strong tenant data isolation while minimizing cloud infrastructure cost?",
                "options": ["Shared Database with Shared Schema and PostgreSQL Row-Level Security (RLS)", "Database per Tenant with dedicated EC2 instance for each customer", "Unindexed JSON files in an AWS S3 bucket", "Single flat CSV file"],
                "answer": "Shared Database with Shared Schema and PostgreSQL Row-Level Security (RLS)",
                "explanation": "Shared database + shared schema utilizes hardware resources efficiently while PostgreSQL Row-Level Security (RLS) automatically enforces 'WHERE tenant_id = current_tenant' at the database engine level."
            }
        ],
        2: [
            {
                "question": "Design an In-Memory Key-Value Cache with Time-to-Live (TTL) expiration in Python or Java.\nOperations: set(key, value, ttl_seconds), get(key) -> value or None.",
                "expected": ["Hash Map for O(1) key lookup", "Min-Heap or PriorityQueue for O(log N) expiration tracking", "Passive eviction on get() + Active background cleanup thread", "Thread-safe locking"],
                "model_answer": "Use a dictionary mapping key -> (value, expire_timestamp). On get(key): check if current_time > expire_timestamp; if expired, delete and return None. Maintain a background daemon thread that periodically checks a Min-Heap of (expire_timestamp, key) to purge stale keys actively without bloating RAM."
            }
        ]
    },
    "paypal": {
        1: [
            {
                "question": "Why must financial payment software strictly store monetary balances as integer cents or arbitrary-precision Decimal types instead of standard IEEE 754 float?",
                "options": ["IEEE 754 binary floating point cannot accurately represent base-10 fractions like 0.1, causing balance drift", "Floats cannot be stored in SQL tables", "Float calculations run 1000x slower on modern CPUs", "IEEE 754 is restricted to 3D gaming chips"],
                "answer": "IEEE 754 binary floating point cannot accurately represent base-10 fractions like 0.1, causing balance drift",
                "explanation": "Binary floating-point numbers represent fractions as powers of 2. For instance, 0.1 + 0.2 equals 0.30000000000000004 in IEEE 754, which accumulates into serious financial balance errors."
            }
        ],
        2: [
            {
                "question": "Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.\nInput: nums = [1,1,1], k = 2\nOutput: 2",
                "expected": ["Prefix Sum + Hash Map technique", "running_sum - k lookup in frequency map", "O(N) time and O(N) space", "Avoids O(N^2) brute force"],
                "model_answer": "Maintain a running prefix sum and a hash map storing the frequency of prefix sums encountered so far, initialized with {0: 1}. For each num: add to running sum. If (running_sum - k) is in the map, increment count by map[running_sum - k]. Add current running_sum to map. Runs in O(N) time."
            }
        ]
    },
    "microsoft": {
        1: [
            {
                "question": "Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum (Kadane's Algorithm).\nInput: nums = [-2,1,-3,4,-1,2,1,-5,4]\nOutput: 6 (Subarray [4,-1,2,1])",
                "expected": ["Kadane's Dynamic Programming Algorithm", "current_sum = max(num, current_sum + num)", "max_sum = max(max_sum, current_sum)", "O(N) time and O(1) space"],
                "model_answer": "Initialize current_sum = 0 and max_sum = -infinity. Iterate through each number: current_sum = max(num, current_sum + num), max_sum = max(max_sum, current_sum). Returns max_sum in a single pass of O(N) time and O(1) auxiliary space."
            }
        ],
        2: [
            {
                "question": "Design an algorithm to serialize and deserialize a binary tree into and from a string format.",
                "expected": ["Pre-order traversal with delimiter (comma) and null markers ('#')", "Queue-based iterative deserialization", "O(N) time and O(N) space"],
                "model_answer": "Serialization: Pre-order DFS traversal. If node is None, append '#'. Else append str(val) and recurse left and right. Deserialization: Split string by comma into a queue. Read next token: if '#', return None. Else create TreeNode(int(val)), node.left = deserialize(), node.right = deserialize(). Returns root in O(N)."
            }
        ]
    },
    "google": {
        1: [
            {
                "question": "Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.\nInput: height = [0,1,0,2,1,0,1,3,2,1,2,1]\nOutput: 6",
                "expected": ["Two Pointers approach from left and right", "Maintain left_max and right_max", "Water trapped at pointer is max - height", "O(N) time and O(1) auxiliary space"],
                "model_answer": "Use two pointers left = 0, right = n - 1 with left_max = 0, right_max = 0. While left < right: if height[left] < height[right]: if height[left] >= left_max, update left_max; else water += left_max - height[left]; left++. Else: if height[right] >= right_max, update right_max; else water += right_max - height[right]; right--. Returns total water in O(N) time and O(1) space."
            }
        ],
        2: [
            {
                "question": "There is a new alien language that uses the English alphabet. Given a list of words from the alien language dictionary sorted lexicographically, derive the order of letters in this language.\nInput: words = ['wrt','wrf','er','ett','rftt']\nOutput: 'wertf'",
                "expected": ["Directed Graph construction comparing adjacent words", "Topological Sort using Kahn's Algorithm (BFS) or DFS cycle detection", "O(V + E) time where V is unique characters"],
                "model_answer": "Build a directed graph where an edge u -> v means character u precedes v. Compare adjacent words: find the first differing character and add directed edge. Count in-degrees. Apply Kahn's BFS algorithm using a queue of nodes with in-degree 0. If result length == number of unique characters, return topological string; else cycle exists (invalid)."
            }
        ]
    }
}

# Merge new questions into COMPANIES_DATA
updated_companies_count = 0
added_questions_count = 0

for company in COMPANIES_DATA:
    slug = company["slug"].lower()
    if slug in NEW_QUESTIONS:
        rounds_dict = NEW_QUESTIONS[slug]
        for round_item in company["rounds"]:
            r_num = round_item["round_number"]
            if r_num in rounds_dict:
                existing_qs = round_item.setdefault("sample_questions", [])
                for new_q in rounds_dict[r_num]:
                    # Check for duplicates by question text
                    if not any(eq.get("question") == new_q["question"] for eq in existing_qs):
                        existing_qs.append(new_q)
                        added_questions_count += 1
        updated_companies_count += 1

print(f"Added {added_questions_count} new authentic questions across {updated_companies_count} companies.")

# Count total sample questions across all companies now
total_after = sum(len(r.get("sample_questions", [])) for c in COMPANIES_DATA for r in c["rounds"])
print(f"Total company sample questions is now: {total_after}")

# Now persist this expanded list back to company_interview_service.py
# Let's write the updated COMPANIES_DATA into company_interview_service.py safely
service_file_path = r'e:\MINI 2.0\backend\app\services\company_interview_service.py'

header = '''from typing import List, Dict, Any, Optional

COMPANIES_DATA = '''

footer = '''

class CompanyInterviewService:
    def list_companies(self) -> List[Dict[str, Any]]:
        return [
            {
                "id": c["id"],
                "name": c["name"],
                "slug": c["slug"],
                "badge": c["badge"],
                "package": c["package"],
                "hiring_season": c["hiring_season"],
                "eligibility": c["eligibility"],
                "description": c["description"],
                "rounds_count": len(c["rounds"]),
                "rounds_summary": [f"Round {r['round_number']}: {r['name']}" for r in c["rounds"]]
            }
            for c in COMPANIES_DATA
        ]

    def get_company(self, slug: str) -> Optional[Dict[str, Any]]:
        for c in COMPANIES_DATA:
            if c["slug"].lower() == slug.lower() or c["id"].lower() == slug.lower():
                return c
        return None

    def add_question(self, slug: str, round_number: int, question_data: Dict[str, Any]) -> bool:
        comp = self.get_company(slug)
        if not comp:
            return False
        for r in comp["rounds"]:
            if r["round_number"] == round_number:
                r.setdefault("sample_questions", []).append(question_data)
                return True
        return False

company_service = CompanyInterviewService()
'''

with open(service_file_path, 'w', encoding='utf-8') as f:
    f.write(header)
    json.dump(COMPANIES_DATA, f, indent=4, ensure_ascii=False)
    f.write(footer)

print(f"Successfully updated {service_file_path} with expanded question library!")

