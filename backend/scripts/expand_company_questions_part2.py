import sys
import os
import json

sys.path.insert(0, r'e:\MINI 2.0\backend')
from app.services.company_interview_service import COMPANIES_DATA

PART2_QUESTIONS = {
    "accenture": {
        1: [
            {
                "question": "Given a password string S, check if it is valid: at least 4 characters, at least 1 numeric digit, at least 1 capital letter, and must not have space or slash. Starting character must not be a number.",
                "options": ["Valid if len >= 4, has digit, has uppercase, no space/slash, start != digit", "Valid if contains '@' and length > 8", "Valid if all lowercase", "Valid if ends with a period"],
                "answer": "Valid if len >= 4, has digit, has uppercase, no space/slash, start != digit",
                "explanation": "Standard Accenture cognitive & coding rule: length >= 4, starts with non-digit, contains at least one uppercase letter and one digit, with no whitespace or forward slash."
            },
            {
                "question": "A sum of money doubles itself in 5 years at simple interest. In how many years will it become 4 times of itself at the same rate of interest?",
                "options": ["15 years", "10 years", "20 years", "12 years"],
                "answer": "15 years",
                "explanation": "Doubling in 5 years means Simple Interest = Principal P in 5 years (Rate R = 20%). To become 4 times, Interest required = 3P. Time = (3P * 100) / (P * 20) = 15 years."
            }
        ],
        2: [
            {
                "question": "You are given an array of N integers. Return the count of pairs (nums[i], nums[j]) such that i < j and |nums[i] - nums[j]| equals a given difference k.\nInput: nums = [1,5,3,4,2], k = 2\nOutput: 3 (Pairs: (1,3), (5,3), (4,2))",
                "expected": ["Hash Set or frequency map for O(1) difference lookup", "For each num, check if (num - k) and (num + k) exist", "O(N) time and O(N) space"],
                "model_answer": "Store all unique numbers in a Hash Set. Iterate through each element num in the set: if (num + k) is in the set, increment pair count. This achieves O(N) time complexity and O(N) auxiliary space, avoiding O(N^2) nested loops."
            }
        ],
        3: [
            {
                "question": "Explain Cloud Computing service models: IaaS, PaaS, and SaaS with real-world examples. Which model would an engineering team select to rapidly deploy a full-stack containerized web app?",
                "expected": ["IaaS: Infrastructure (AWS EC2, Azure VMs)", "PaaS: Platform (Heroku, AWS Elastic Beanstalk)", "SaaS: Software (Gmail, Salesforce)", "PaaS or Container Service (ECS/GKE) chosen for rapid zero-ops deployment"]
            }
        ]
    },
    "wipro": {
        1: [
            {
                "question": "A boat travels 24 km upstream and 36 km downstream in 6 hours. It also travels 36 km upstream and 24 km downstream in 6.5 hours. Find the speed of the current.",
                "options": ["2 km/h", "3 km/h", "4 km/h", "1.5 km/h"],
                "answer": "2 km/h",
                "explanation": "Let upstream speed = u, downstream speed = v. 24/u + 36/v = 6 and 36/u + 24/v = 6.5. Solving gives u = 8 km/h, v = 12 km/h. Speed of current = (v - u)/2 = (12 - 8)/2 = 2 km/h."
            }
        ],
        2: [
            {
                "question": "Given a directed graph, write an algorithm to detect whether the graph contains a cycle.\nInput: 4 vertices, edges: 0->1, 1->2, 2->3, 3->1\nOutput: Cycle Detected (1->2->3->1)",
                "expected": ["DFS with recursion stack tracking (visited array + in_stack array)", "Or Kahn's Algorithm (in-degree count)", "O(V + E) time"],
                "model_answer": "Use DFS with two boolean arrays: 'visited' and 'in_recursion_stack'. For each unvisited node, perform DFS: mark visited and in_recursion_stack. For each neighbor: if not visited, recurse; if already in_recursion_stack, a back-edge and cycle is detected. When exiting DFS for node, unmark in_recursion_stack."
            }
        ],
        3: [
            {
                "question": "What is the 3-Way Handshake in TCP connection establishment, and why is a 2-Way Handshake insufficient?",
                "expected": ["SYN -> SYN-ACK -> ACK sequence", "Ensures both client and server can send and receive packets", "Prevents duplicate delayed historical connection requests from tying up server resources"]
            }
        ]
    },
    "cognizant": {
        1: [
            {
                "question": "What is the difference between synchronous execution and asynchronous execution in web backends? How does a thread pool handle concurrent socket requests?",
                "expected": ["Synchronous blocks waiting for I/O", "Asynchronous registers callbacks/promises and yields CPU", "Thread pool allocates fixed worker threads, queueing requests when saturated"]
            }
        ],
        2: [
            {
                "question": "Given an integer array nums and an integer k, find the k-th largest element in the array in O(N log K) time.\nInput: nums = [3,2,1,5,6,4], k = 2\nOutput: 5",
                "expected": ["Min-Heap of size k", "Insert elements; when size > k, pop smallest", "Root of Min-Heap holds k-th largest", "O(N log K) time and O(K) space"],
                "model_answer": "Maintain a Min-Heap of capacity k. Iterate through each number in nums and push into heap. If heap size exceeds k, pop the minimum element. After scanning all elements, the top of the Min-Heap is guaranteed to be the k-th largest element in O(N log K) time."
            }
        ],
        3: [
            {
                "question": "Explain the difference between SQL GROUP BY and HAVING clauses. Can an aggregate function (such as COUNT or SUM) be used in a WHERE clause?",
                "options": ["WHERE filters rows before grouping; HAVING filters aggregated groups after GROUP BY; aggregates cannot be used in WHERE", "HAVING and WHERE are completely interchangeable", "HAVING only works on integer primary keys", "WHERE can contain SUM() if wrapped in quotes"],
                "answer": "WHERE filters rows before grouping; HAVING filters aggregated groups after GROUP BY; aggregates cannot be used in WHERE",
                "explanation": "SQL query execution order: FROM -> WHERE (row filter) -> GROUP BY -> HAVING (group aggregate filter) -> SELECT -> ORDER BY. Aggregate functions compute over groups, so they cannot execute in the row-level WHERE phase."
            }
        ]
    },
    "capgemini": {
        1: [
            {
                "question": "Which of the following sorting algorithms is Stable and has a worst-case time complexity of O(N log N)?",
                "options": ["Merge Sort", "Quick Sort", "Heap Sort", "Selection Sort"],
                "answer": "Merge Sort",
                "explanation": "Merge Sort guarantees O(N log N) worst-case time and preserves the relative order of elements with equal keys (Stability). Quick Sort and Heap Sort are not stable in their standard implementations."
            }
        ],
        2: [
            {
                "question": "Given two sorted arrays nums1 and nums2, merge them into a single sorted array in-place without allocating extra space.\nInput: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3\nOutput: [1,2,2,3,5,6]",
                "expected": ["Three pointers starting from the back (m - 1, n - 1, m + n - 1)", "Fill largest element from the end of nums1", "O(M + N) time and O(1) extra space"],
                "model_answer": "Set pointer p1 = m - 1, p2 = n - 1, and write pointer p = m + n - 1. While p2 >= 0: if p1 >= 0 and nums1[p1] > nums2[p2], nums1[p] = nums1[p1], p1--; else nums1[p] = nums2[p2], p2--; p--. Runs in O(M + N) time with zero extra memory."
            }
        ]
    },
    "oracle": {
        1: [
            {
                "question": "Why do relational database engines (like Oracle and MySQL InnoDB) use B+ Trees rather than standard Binary Search Trees (BST) or B-Trees for disk storage indexing?",
                "options": ["B+ Trees store all actual records in leaf nodes connected as a doubly linked list, optimizing range scans and maximizing disk block fan-out", "B+ Trees consume 0 bytes of RAM", "Binary Search Trees are mathematically un-indexable", "B+ Trees are only compatible with Oracle Linux"],
                "answer": "B+ Trees store all actual records in leaf nodes connected as a doubly linked list, optimizing range scans and maximizing disk block fan-out",
                "explanation": "B+ Tree nodes have high fan-out (hundreds of keys per disk page), minimizing disk I/O depth (height <= 3-4 for millions of rows). Linked leaf nodes enable fast O(1) sequential range scans."
            }
        ],
        2: [
            {
                "question": "Implement a Trie (Prefix Tree) with insert(word), search(word), and startsWith(prefix) operations.",
                "expected": ["TrieNode class with children dict and is_end_of_word boolean", "insert: traverse/create nodes for each char, mark end", "search: verify full word and is_end_of_word == True", "startsWith: verify prefix traversal completes", "All operations run in O(L) time where L is word length"],
                "model_answer": "Define TrieNode with children = {} and is_end = False. insert(word): node = root; for c in word: node = node.children.setdefault(c, TrieNode()); node.is_end = True. search(word): traverse; return node is not None and node.is_end. startsWith(prefix): traverse; return node is not None. Time complexity is O(L) per operation."
            }
        ]
    },
    "cisco": {
        1: [
            {
                "question": "In computer networking, what is the fundamental purpose of the Address Resolution Protocol (ARP)?",
                "options": ["To resolve an IP address (Network Layer) to a physical MAC address (Data Link Layer) on a local LAN", "To assign dynamic IP addresses to newly connected devices", "To encrypt HTTP payloads using TLS", "To convert domain names into IP addresses"],
                "answer": "To resolve an IP address (Network Layer) to a physical MAC address (Data Link Layer) on a local LAN",
                "explanation": "ARP broadcasts on Layer 2 asking 'Who has IP X.X.X.X?' and receives a unicast reply with the corresponding hardware MAC address."
            }
        ],
        2: [
            {
                "question": "Given a network of N nodes connected by directed weighted edges, find the minimum time it takes for a signal sent from node K to reach all nodes. If impossible, return -1 (Network Delay Time).",
                "expected": ["Dijkstra's Algorithm using Min-Heap", "Distance array initialized to infinity", "O((V + E) log V) time", "Return max(dist) if all visited else -1"],
                "model_answer": "Build adjacency list. Use a Min-Heap initialized with (0, K). Maintain dist array initialized to infinity with dist[K] = 0. Pop (d, u): if d > dist[u], continue. For each neighbor (v, w): if d + w < dist[v], dist[v] = d + w, push (dist[v], v). After heap is empty, if max(dist) is infinity return -1; else return max(dist)."
            }
        ]
    },
    "adobe": {
        1: [
            {
                "question": "In graphic processing and document rendering engines, why are Bezier Curves preferred over raster pixel grids for scalable font glyphs and vector art?",
                "options": ["Bezier curves are parametric polynomial curves that scale infinitely without pixelation or quality loss", "Raster pixels run faster on CPU", "Bezier curves only work in black and white", "Vector art requires 100x more memory than bitmap images"],
                "answer": "Bezier curves are parametric polynomial curves that scale infinitely without pixelation or quality loss",
                "explanation": "Parametric Bernstein polynomial formulas allow glyphs and paths to be mathematically re-rasterized at any DPI or zoom level with crisp edges."
            }
        ],
        2: [
            {
                "question": "Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands (connected components 4-directionally).\nInput: grid with 1s and 0s\nOutput: Number of islands",
                "expected": ["BFS or DFS traversal", "Sink visited land cells (set grid[r][c] = '0')", "O(M * N) time and O(M * N) space", "Handle 4-directional boundary conditions"],
                "model_answer": "Iterate through each cell (r, c). When a '1' is encountered, increment island count and trigger DFS/BFS to visit and flip all connected '1's (up, down, left, right) to '0'. Continue scanning. Returns total island count in O(M * N) time."
            }
        ]
    }
}

for company in COMPANIES_DATA:
    slug = company["slug"].lower()
    if slug in PART2_QUESTIONS:
        rounds_dict = PART2_QUESTIONS[slug]
        for round_item in company["rounds"]:
            r_num = round_item["round_number"]
            if r_num in rounds_dict:
                existing_qs = round_item.setdefault("sample_questions", [])
                for new_q in rounds_dict[r_num]:
                    if not any(eq.get("question") == new_q["question"] for eq in existing_qs):
                        existing_qs.append(new_q)

total_after = sum(len(r.get("sample_questions", [])) for c in COMPANIES_DATA for r in c["rounds"])
print(f"Total company sample questions is now: {total_after}")

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

print(f"Successfully updated {service_file_path} with Part 2 expanded questions!")

