import os

company_file = r'e:\MINI 2.0\backend\app\services\company_interview_service.py'
with open(company_file, 'r', encoding='utf-8') as f:
    text = f.read()

target = "        'slug': 'adobe'}\n]"
if target not in text:
    target = "        'slug': 'adobe'}\r\n]"

new_companies = """        'slug': 'adobe'},
    {
        'id': 'walmart',
        'slug': 'walmart',
        'name': 'Walmart Global Tech',
        'badge': 'Walmart CodeHers / Campus SDE',
        'package': 'INR 18.0 LPA - INR 28.0 LPA',
        'hiring_season': 'July - October (On-Campus & CodeHers)',
        'eligibility': 'B.Tech / M.Tech in CS / IT / ECE with 7.0+ CGPA and zero active backlogs.',
        'description': 'Walmart Global Tech India builds high-scale retail software, distributed supply-chain microservices, and omnichannel checkout infrastructure processing billions of transactions.',
        'rounds': [
            {
                'round_number': 1,
                'name': 'Online Technical Assessment (DSA & Core CS)',
                'type': 'Coding & Technical MCQ',
                'duration_minutes': 90,
                'questions_count': 22,
                'cutoff_percentage': 75,
                'sections': ['Data Structures', 'Algorithms', 'Operating Systems', 'DBMS & SQL'],
                'tips': 'Solve both algorithmic coding problems with optimal time complexity and brush up on indexing and transaction isolation levels.',
                'sample_questions': [
                    {
                        'question': 'Which database isolation level prevents both Dirty Reads and Non-Repeatable Reads, but may still permit Phantom Reads under the ANSI SQL standard?',
                        'options': ['Read Uncommitted', 'Read Committed', 'Repeatable Read', 'Serializable'],
                        'answer': 'Repeatable Read',
                        'explanation': 'Under ANSI SQL standards, Repeatable Read holds shared read locks until the transaction ends, preventing Dirty Reads and Non-Repeatable Reads. Phantom Reads can only occur if range locks are not acquired, which requires Serializable isolation.'
                    },
                    {
                        'question': 'Given an array of product prices and an integer target, describe an optimal algorithm to find the maximum sub-array sum with at most k elements.',
                        'answer': 'Use a deque to maintain a sliding window of prefix sums of length up to k, keeping elements monotonically increasing so the minimum prefix sum is available at the front in O(1) amortized time, yielding O(N) overall time complexity.'
                    }
                ]
            },
            {
                'round_number': 2,
                'name': 'Technical Interview 1: Data Structures & Problem Solving',
                'type': 'Live Coding & Algorithms',
                'duration_minutes': 60,
                'questions_count': 2,
                'cutoff_percentage': 75,
                'sections': ['Dynamic Programming', 'Trees & Graphs', 'Edge Case Analysis'],
                'tips': 'Communicate your thought process before writing code. Clarify constraints like negative weights and integer overflow.',
                'sample_questions': [
                    {
                        'question': 'Given a directed acyclic graph (DAG) representing store inventory dependencies, find the longest path from any source to any sink node in O(V + E) time.',
                        'answer': 'Compute topological ordering using Kahn algorithm (in-degrees) or DFS post-order. Initialize distances to negative infinity, then relax outgoing edges in topological order in O(V + E) time.'
                    }
                ]
            },
            {
                'round_number': 3,
                'name': 'Technical Interview 2: Low-Level Design & Concurrency',
                'type': 'LLD & System Architecture',
                'duration_minutes': 60,
                'questions_count': 2,
                'cutoff_percentage': 75,
                'sections': ['Object-Oriented Design', 'Multithreading', 'Design Patterns'],
                'tips': 'Apply SOLID principles, explain thread synchronization mechanisms (synchronized, ReentrantLock), and draw clean class diagrams.',
                'sample_questions': [
                    {
                        'question': 'Design an in-memory thread-safe LRU Cache with O(1) get and put operations in Java or Python.',
                        'answer': 'Combine a doubly linked list with a hash map. The hash map maps keys to list nodes for O(1) lookup. When accessed or updated, move node to the head. When capacity is exceeded, evict from tail. Protect mutations with a ReadWriteLock or concurrent primitives.'
                    }
                ]
            },
            {
                'round_number': 4,
                'name': 'Managerial & Cultural Fit',
                'type': 'Behavioral & Leadership',
                'duration_minutes': 45,
                'questions_count': 3,
                'cutoff_percentage': 70,
                'sections': ['Customer Obsession', 'Ownership Mindset', 'Team Collaboration'],
                'tips': 'Use the STAR method and emphasize customer-centric engineering decisions you made in college projects.',
                'sample_questions': [
                    {
                        'question': 'Tell me about a time when you identified a critical flaw in your software architecture right before a project deadline. How did you prioritize and address it?',
                        'answer': 'Explain with Situation, Task, Action, and quantifiable Result, focusing on rapid risk triage, communication with stakeholders, and implementing a resilient solution under tight constraints.'
                    }
                ]
            }
        ]
    },
    {
        'id': 'freshworks',
        'slug': 'freshworks',
        'name': 'Freshworks',
        'badge': 'Freshworks Campus SDE',
        'package': 'INR 12.0 LPA - INR 18.0 LPA',
        'hiring_season': 'August - November',
        'eligibility': 'B.Tech / BE / MCA with 65% or 6.5+ CGPA and strong programming skills.',
        'description': 'Leading SaaS enterprise product company providing intuitive CRM, IT service management (Freshservice), and customer support software (Freshdesk) serving over 65,000 businesses globally.',
        'rounds': [
            {
                'round_number': 1,
                'name': 'Online Aptitude & Coding Assessment',
                'type': 'Aptitude & DSA Coding',
                'duration_minutes': 90,
                'questions_count': 30,
                'cutoff_percentage': 70,
                'sections': ['Quantitative Aptitude', 'Verbal Reasoning', 'Coding Problems'],
                'tips': 'Practice string manipulation, array hashing, and clean code formatting in modern programming languages.',
                'sample_questions': [
                    {
                        'question': 'In a RESTful API design, which HTTP method should be used for idempotent updates that replace the entire resource state?',
                        'options': ['POST', 'PUT', 'PATCH', 'CONNECT'],
                        'answer': 'PUT',
                        'explanation': 'PUT is defined by RFC 7231 as an idempotent method intended to replace the entire target resource with the requested payload, whereas PATCH is non-idempotent and updates partial fields.'
                    },
                    {
                        'question': 'Given a stream of incoming customer support tickets with timestamps, write a function to calculate the 95th percentile resolution time over a sliding 1-hour window.',
                        'answer': 'Maintain a balanced binary search tree or two heaps (max-heap for lower 95% and min-heap for upper 5%) while pruning expired timestamps outside the 1-hour window.'
                    }
                ]
            },
            {
                'round_number': 2,
                'name': 'Machine Coding / Modular Design Round',
                'type': 'Machine Coding & Implementation',
                'duration_minutes': 90,
                'questions_count': 1,
                'cutoff_percentage': 75,
                'sections': ['Clean Code', 'OOP Design', 'Extensibility', 'Unit Testing'],
                'tips': 'Write modular code with proper separation of concerns (controller, service, repository, models). Do not cram all logic in a single main function.',
                'sample_questions': [
                    {
                        'question': 'Design and code a command-line Issue Tracking and Escalation System with priority levels, assignment rules, and SLA breach notifications.',
                        'answer': 'Create Ticket, User, SLAStrategy, and NotificationObserver models. Use the Strategy pattern for escalation routing and Observer pattern for alerts. Ensure all inputs are validated cleanly.'
                    }
                ]
            },
            {
                'round_number': 3,
                'name': 'Technical Architecture & Deep Dive',
                'type': 'Technical Interview',
                'duration_minutes': 60,
                'questions_count': 2,
                'cutoff_percentage': 75,
                'sections': ['Database Optimization', 'WebSockets', 'Caching Strategies'],
                'tips': 'Demonstrate knowledge of Redis caching, database indexes, connection pooling, and multi-tenant architectures.',
                'sample_questions': [
                    {
                        'question': 'How does multi-tenant database architecture differ between shared-database shared-schema vs schema-per-tenant, and how do you prevent data leaks between tenants?',
                        'answer': 'Shared-schema isolates data via tenant_id column and row-level security policies, requiring minimal infrastructure overhead. Schema-per-tenant isolates data via separate Postgres schemas, offering higher compliance at higher migration cost. Data leaks are prevented using parameterized ORM filters and mandatory session tenant contexts.'
                    }
                ]
            },
            {
                'round_number': 4,
                'name': 'HR & Values Alignment',
                'type': 'Culture & Career Goals',
                'duration_minutes': 45,
                'questions_count': 3,
                'cutoff_percentage': 70,
                'sections': ['Craftsmanship', 'Empathy', 'Growth Mindset'],
                'tips': 'Demonstrate genuine interest in SaaS product usability and explain how you prioritize customer happiness in engineering.',
                'sample_questions': [
                    {
                        'question': 'Why are you passionate about working at a SaaS product company like Freshworks compared to traditional IT services?',
                        'answer': 'Emphasize your desire to have continuous ownership of product features, measuring real user adoption metrics, and iterating rapidly based on customer telemetry and feedback.'
                    }
                ]
            }
        ]
    },
    {
        'id': 'flipkart',
        'slug': 'flipkart',
        'name': 'Flipkart',
        'badge': 'Flipkart GRiD / SDE-1 Campus',
        'package': 'INR 26.0 LPA - INR 34.0 LPA',
        'hiring_season': 'July - October',
        'eligibility': 'B.Tech / M.Tech in CS / IT / Circuital branches with 7.0+ CGPA.',
        'description': 'India leading homegrown e-commerce pioneer, part of Walmart Inc. Renowned for its challenging 90-minute Machine Coding round and rigorous problem-solving standards.',
        'rounds': [
            {
                'round_number': 1,
                'name': 'Online Assessment (Algorithms & Problem Solving)',
                'type': 'HackerRank Coding',
                'duration_minutes': 90,
                'questions_count': 3,
                'cutoff_percentage': 80,
                'sections': ['Dynamic Programming', 'Graph Algorithms', 'Greedy Techniques'],
                'tips': 'All 3 algorithmic problems must pass 100% of hidden test cases with strict time limits (1.0s).',
                'sample_questions': [
                    {
                        'question': 'What is the time complexity of finding the shortest path in a weighted graph with non-negative edge weights using a Fibonacci heap implementation of Dijkstra algorithm?',
                        'options': ['O(V^2)', 'O(E + V log V)', 'O(E log V)', 'O(V * E)'],
                        'answer': 'O(E + V log V)',
                        'explanation': 'With a Fibonacci heap, decrease-key operations take O(1) amortized time, leading to O(E) for all edge relaxations, while extract-min takes O(log V) amortized time across V vertices, totaling O(E + V log V).'
                    },
                    {
                        'question': 'Given delivery hubs and transit times, find the minimum time to deliver all orders using at most k delivery executives.',
                        'answer': 'Model as binary search on answer combined with a greedy verification function or dynamic programming with bitmask states for constrained path routing.'
                    }
                ]
            },
            {
                'round_number': 2,
                'name': 'Machine Coding Round (The Flipkart Signature Round)',
                'type': 'Live Modular Coding & OOP',
                'duration_minutes': 90,
                'questions_count': 1,
                'cutoff_percentage': 80,
                'sections': ['Object-Oriented Design', 'Design Patterns', 'Executable Driver Code'],
                'tips': 'Focus on writing clean, working, extensible code with in-memory data structures. Implement demo driver code in main() to demonstrate all functional requirements.',
                'sample_questions': [
                    {
                        'question': 'Design and implement an in-memory Flash Sale Inventory Booking System that handles concurrent reservations, cart timeouts (10 mins), and stock replenishment.',
                        'answer': 'Create Product, Inventory, Reservation, and User models. Implement concurrency control using synchronized blocks or ConcurrentHashMap with lock striping. Apply State pattern for reservation lifecycles and Strategy pattern for discount engines.'
                    }
                ]
            },
            {
                'round_number': 3,
                'name': 'Problem Solving & Data Structures Deep Dive',
                'type': 'Live Coding Interview',
                'duration_minutes': 60,
                'questions_count': 2,
                'cutoff_percentage': 75,
                'sections': ['Binary Search Trees', 'Tries', 'Sub-array DP'],
                'tips': 'Write production-grade code on a shared whiteboard or editor without syntax errors and verify boundary inputs.',
                'sample_questions': [
                    {
                        'question': 'Design an autocomplete search engine prefix query system that returns the top 5 most frequently searched product keywords in O(K) time where K is prefix length.',
                        'answer': 'Use a Trie where each node stores a min-heap or sorted list of the top 5 keywords passing through that node. Looking up a prefix takes O(K) to reach the prefix node, and reading the precomputed top 5 takes O(1).'
                    }
                ]
            },
            {
                'round_number': 4,
                'name': 'Hiring Manager & Bar Raiser Round',
                'type': 'Behavioral & System Intuition',
                'duration_minutes': 45,
                'questions_count': 3,
                'cutoff_percentage': 70,
                'sections': ['Customer Centricity', 'Bias for Action', 'Engineering Ownership'],
                'tips': 'Demonstrate resilience when dealing with failed experiments and articulate clear technical trade-offs.',
                'sample_questions': [
                    {
                        'question': 'Describe a scenario where you faced conflicting deadlines across two critical software modules. How did you negotiate and deliver?',
                        'answer': 'Discuss how you assessed critical path impact, communicated transparently with team members, and delivered a high-quality MVP on time followed by iterative improvements.'
                    }
                ]
            }
        ]
    },
    {
        'id': 'paypal',
        'slug': 'paypal',
        'name': 'PayPal',
        'badge': 'PayPal Campus SDE-1',
        'package': 'INR 24.0 LPA - INR 32.0 LPA',
        'hiring_season': 'August - November',
        'eligibility': 'B.Tech / M.Tech in CS / IT / ECE with 7.5+ CGPA and strong fundamentals in algorithms and computer systems.',
        'description': 'Global financial technology giant powering digital payments, digital wallets, and payment gateways for over 430 million active accounts globally.',
        'rounds': [
            {
                'round_number': 1,
                'name': 'Online Coding & Technical Assessment',
                'type': 'HackerRank Test',
                'duration_minutes': 90,
                'questions_count': 24,
                'cutoff_percentage': 75,
                'sections': ['Data Structures', 'Algorithms', 'Bit Manipulation', 'Operating Systems'],
                'tips': 'Solve algorithmic challenges with focus on memory efficiency and edge cases like overflow and negative integers.',
                'sample_questions': [
                    {
                        'question': 'Which property of database transactions guarantees that once a payment transaction commits, its updates survive system crashes and power failures?',
                        'options': ['Atomicity', 'Consistency', 'Isolation', 'Durability'],
                        'answer': 'Durability',
                        'explanation': 'Durability guarantees that once a transaction has committed, its changes are written to non-volatile storage (such as write-ahead transaction logs) and will survive any subsequent system crash.'
                    },
                    {
                        'question': 'Given an array of integer account balances, find the longest contiguous subarray whose sum is divisible by k in O(N) time.',
                        'answer': 'Use prefix sum modulo k with a hash map storing the earliest occurrence of each remainder. If (prefix_sum % k) repeats at index i and j, subarray between i+1 and j has sum divisible by k.'
                    }
                ]
            },
            {
                'round_number': 2,
                'name': 'Technical Interview 1: Data Structures & System Algorithms',
                'type': 'Live Coding Interview',
                'duration_minutes': 60,
                'questions_count': 2,
                'cutoff_percentage': 75,
                'sections': ['Linked Lists', 'Binary Trees', 'Two Pointers', 'Complexity Analysis'],
                'tips': 'State time and space complexities explicitly before writing code. Handle null and empty inputs cleanly.',
                'sample_questions': [
                    {
                        'question': 'Implement an algorithm to detect and remove a cycle in a singly linked list in O(N) time and O(1) auxiliary space.',
                        'answer': 'Use Floyd Cycle Detection (slow and fast pointers moving at 1x and 2x speed). When they meet, reset slow to head and advance both at 1x until they meet at the cycle start. Traverse to find the last node in the cycle and set its next pointer to null.'
                    }
                ]
            },
            {
                'round_number': 3,
                'name': 'Technical Interview 2: Concurrency, Multithreading & Transactions',
                'type': 'Core Engineering & Concurrency',
                'duration_minutes': 60,
                'questions_count': 2,
                'cutoff_percentage': 75,
                'sections': ['Thread Safety', 'Deadlocks', 'Distributed Transactions', 'Idempotency'],
                'tips': 'Explain the difference between optimistic and pessimistic locking in financial transfer systems and define idempotency keys.',
                'sample_questions': [
                    {
                        'question': 'How do you design a payment transfer endpoint between two accounts (Account A to Account B) that prevents deadlocks under high concurrent bidirectional transfers?',
                        'answer': 'Always acquire account locks in a globally deterministic order (e.g., lock the account with the smaller account ID first, then lock the larger ID). This eliminates circular wait conditions, completely preventing deadlocks. Combine with transactional balance verification and idempotency keys.'
                    }
                ]
            },
            {
                'round_number': 4,
                'name': 'Managerial & Core Cultural Values',
                'type': 'Behavioral & Leadership',
                'duration_minutes': 45,
                'questions_count': 3,
                'cutoff_percentage': 70,
                'sections': ['Integrity', 'Collaboration', 'Innovation', 'Inclusion'],
                'tips': 'Highlight your commitment to ethical engineering, data privacy, and attention to detail when dealing with sensitive user information.',
                'sample_questions': [
                    {
                        'question': 'Why do you want to build fintech software at PayPal, and how do you ensure high reliability in critical software systems?',
                        'answer': 'Articulate the responsibility of building systems where errors directly impact livelihoods. Discuss unit testing, regression testing, automated canary deployments, and observability as essential engineering habits.'
                    }
                ]
            }
        ]
    }\n]"""

if target in text:
    updated = text.replace(target, new_companies)
    with open(company_file, 'w', encoding='utf-8') as f:
        f.write(updated)
    print("SUCCESS: 4 companies added to company_interview_service.py!")
else:
    print("ERROR: Target anchor not found in file!")

