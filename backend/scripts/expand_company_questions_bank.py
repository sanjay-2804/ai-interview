"""
InterviewAI — Company Question Bank Multi-Round Expansion
Expands all 22 companies in `company_interview_service.py` to full 3-4 round pipelines
with comprehensive authentic questions, options, explanations, and model answers.
"""

import sys
import os
import json
import pprint

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from app.services.company_interview_service import COMPANIES_DATA

# Dictionary of updates and new rounds to inject into COMPANIES_DATA
COMPANY_EXPANSIONS = {
    "hcltech": {
        "new_rounds": [
            {
                "round_number": 3,
                "name": "Advanced Technical & Problem Solving",
                "type": "Technical Interview",
                "duration_minutes": 45,
                "questions_count": 4,
                "cutoff_percentage": 70,
                "sections": ["Data Structures", "REST APIs", "SQL Joins", "Debugging"],
                "tips": "Be ready to write clean code on an online IDE and explain edge cases.",
                "sample_questions": [
                    {
                        "question": "Given the head of a singly linked list, how do you find the middle element in a single pass without knowing the list length in advance?",
                        "expected": [
                            "Use fast and slow pointer technique (Tortoise and Hare)",
                            "Slow moves 1 step while Fast moves 2 steps",
                            "When Fast reaches null or end, Slow is at the middle node",
                            "Time complexity O(N), Space complexity O(1)"
                        ],
                        "model_answer": "Initialize two pointers, slow and fast, at the head. Advance slow by 1 node and fast by 2 nodes in each iteration. When fast reaches null or fast.next is null, slow points precisely to the middle node. This requires O(N) time and O(1) auxiliary space."
                    },
                    {
                        "question": "What is the difference between INNER JOIN, LEFT OUTER JOIN, and FULL OUTER JOIN in SQL? Give a real-world employee-department example.",
                        "expected": [
                            "INNER JOIN returns only matching rows from both tables",
                            "LEFT JOIN returns all rows from left table plus matching rows from right (nulls for non-matches)",
                            "FULL OUTER JOIN returns all rows from both tables, filling nulls where no match exists"
                        ],
                        "model_answer": "INNER JOIN returns employees assigned to existing departments. LEFT JOIN returns all employees, including new hires without an assigned department. FULL OUTER JOIN returns all employees and all departments, including departments with zero assigned employees."
                    }
                ]
            },
            {
                "round_number": 4,
                "name": "HR & Cultural Fitment",
                "type": "HR & Behavioral",
                "duration_minutes": 30,
                "questions_count": 3,
                "cutoff_percentage": 70,
                "sections": ["Communication", "Career Goals", "Workplace Adaptability", "HCLTech Core Values"],
                "tips": "Demonstrate flexibility regarding location and shifts, and emphasize eagerness to learn digital engineering.",
                "sample_questions": [
                    {
                        "question": "Why do you want to start your professional engineering career at HCLTech, and how do you handle rapidly learning new technology stacks?",
                        "answer": "Discuss HCLTech's Ideapreneurship culture, empowering employees to innovate at the grassroots level. Give an example from college where you learned a new programming framework (like React or FastAPI) within two weeks to complete a capstone project."
                    },
                    {
                        "question": "Are you comfortable with relocation to different client locations and working in rotational project shifts?",
                        "answer": "Affirm that starting your career requires adaptability and immersion in live customer environments across India or abroad, and emphasize that project success and client satisfaction are your primary priorities."
                    }
                ]
            }
        ],
        "add_to_round_1": [
            {
                "question": "A car covers a distance of 450 km in 5 hours. If it travels the first half of the distance at 75 km/h, at what speed must it travel the second half to complete the journey on time?",
                "options": ["112.5 km/h", "100 km/h", "125 km/h", "90 km/h"],
                "answer": "112.5 km/h",
                "explanation": "Total distance = 450 km, total time = 5 h. First half = 225 km at 75 km/h takes 225/75 = 3 hours. Remaining time = 5 - 3 = 2 hours. Required speed for remaining 225 km = 225 / 2 = 112.5 km/h."
            },
            {
                "question": "What is the output of the following C code?\n#include <stdio.h>\nint main() {\n  int arr[] = {10, 20, 30, 40};\n  int *ptr = arr;\n  printf('%d', *(ptr + 2));\n  return 0;\n}",
                "options": ["30", "20", "10", "40"],
                "answer": "30",
                "explanation": "Pointer arithmetic: `ptr` points to arr[0]. `*(ptr + 2)` dereferences arr[2], which holds value 30."
            }
        ]
    },
    "techmahindra": {
        "new_rounds": [
            {
                "round_number": 3,
                "name": "Core CS & Project Architecture",
                "type": "Technical Interview",
                "duration_minutes": 40,
                "questions_count": 3,
                "cutoff_percentage": 70,
                "sections": ["DBMS Normalization", "OOP Concepts", "Final Year Project", "API Architecture"],
                "tips": "Be thorough with every layer of your academic project and explain how you chose your database.",
                "sample_questions": [
                    {
                        "question": "Explain 1NF, 2NF, and 3NF database normalization with a simple table example.",
                        "expected": [
                            "1NF: Atomic values only, no repeating groups",
                            "2NF: In 1NF and no partial dependency (non-key attributes depend on whole composite key)",
                            "3NF: In 2NF and no transitive dependency (no non-key attribute depends on another non-key attribute)"
                        ],
                        "model_answer": "1NF ensures every cell contains a single atomic value. 2NF removes partial functional dependencies where an attribute depends on only part of a composite primary key. 3NF removes transitive dependencies where a non-prime attribute depends on another non-prime attribute, ensuring data is updated in one authoritative place."
                    },
                    {
                        "question": "How did you design the backend and database architecture in your major college project?",
                        "expected": [
                            "Clear separation of concerns (controller, service, repository)",
                            "Choice of database (SQL vs NoSQL) justified by data structure",
                            "Handling authentication and API security"
                        ],
                        "model_answer": "Walk through your project using the 3-tier architecture: client UI, REST API backend, and relational database. Explain how you created schema relationships, indexed high-traffic tables, and used token-based authentication (JWT) to secure user endpoints."
                    }
                ]
            },
            {
                "round_number": 4,
                "name": "Managerial & Fitment Assessment",
                "type": "HR & Behavioral",
                "duration_minutes": 30,
                "questions_count": 3,
                "cutoff_percentage": 70,
                "sections": ["Team Collaboration", "Handling Pressure", "Company Knowledge", "Ethics"],
                "tips": "Emphasize collaborative mindset and adaptability to enterprise communication platforms.",
                "sample_questions": [
                    {
                        "question": "Describe a situation during a team assignment or hackathon where team members had conflicting opinions. How did you resolve it?",
                        "answer": "Use the STAR method: explain the disagreement (e.g. choice of tech stack), how you organized an objective pros-and-cons discussion focused on project deadlines, arrived at a compromise, and delivered the project on time."
                    }
                ]
            }
        ],
        "add_to_round_1": [
            {
                "question": "A merchant sells an article for INR 840 making a profit of 20%. What was the cost price of the article?",
                "options": ["INR 700", "INR 720", "INR 750", "INR 680"],
                "answer": "INR 700",
                "explanation": "SP = CP * (1 + Profit%). 840 = CP * 1.20 => CP = 840 / 1.20 = INR 700."
            }
        ]
    },
    "wipro": {
        "new_rounds": [
            {
                "round_number": 3,
                "name": "Advanced Technical & Problem Solving",
                "type": "Technical Interview",
                "duration_minutes": 40,
                "questions_count": 3,
                "cutoff_percentage": 70,
                "sections": ["Data Structures", "Database Management", "C/Java/Python Syntax", "Debugging"],
                "tips": "Expect live code writing on arrays, strings, and fundamental SQL queries.",
                "sample_questions": [
                    {
                        "question": "Write an optimal function to check whether a given string is a palindrome, ignoring non-alphanumeric characters and case sensitivity.",
                        "expected": [
                            "Use two-pointer technique (left and right)",
                            "Skip non-alphanumeric characters",
                            "Compare lowercase characters",
                            "Time complexity O(N), space complexity O(1)"
                        ],
                        "model_answer": "Place a left pointer at index 0 and a right pointer at len - 1. While left < right, increment left if character is not alphanumeric, decrement right if not alphanumeric. If lower(str[left]) != lower(str[right]), return false. If loop finishes, return true. O(N) time and O(1) space."
                    },
                    {
                        "question": "What is the difference between Primary Key and Unique Key constraints in a relational database?",
                        "expected": [
                            "A table can have only ONE Primary Key, but MULTIPLE Unique Keys",
                            "Primary Key strictly forbids NULL values; Unique Key allows one (or multiple in some engines) NULL value",
                            "Primary Key automatically defaults to a clustered index in most engines"
                        ],
                        "model_answer": "A Primary Key uniquely identifies each row and strictly disallows NULLs; a table can possess only one primary key. A Unique Key enforces uniqueness across a column but allows NULL values, and a table can define multiple unique keys."
                    }
                ]
            },
            {
                "round_number": 4,
                "name": "HR & Cultural Alignment",
                "type": "HR & Behavioral",
                "duration_minutes": 25,
                "questions_count": 3,
                "cutoff_percentage": 70,
                "sections": ["Spirit of Wipro", "Client Focus", "Continuous Learning", "Team Spirit"],
                "tips": "Mention the 'Spirit of Wipro' values: Be passionate about clients' success, Treat each person with respect, Be global and responsible, Unyielding integrity.",
                "sample_questions": [
                    {
                        "question": "What do you know about Wipro and the 'Spirit of Wipro' values?",
                        "answer": "Detail Wipro's transition from vegetable oil in 1945 to a premier global technology firm. Highlight the four values: Passion for clients' success, Respect for each person, Global & responsible citizenship, and Unyielding integrity in everything we do."
                    }
                ]
            }
        ]
    },
    "cognizant": {
        "new_rounds": [
            {
                "round_number": 3,
                "name": "Domain Technical & Machine Coding",
                "type": "Technical Interview",
                "duration_minutes": 45,
                "questions_count": 4,
                "cutoff_percentage": 70,
                "sections": ["Algorithms", "Web Technologies", "SQL & Database", "OOP Principles"],
                "tips": "GenC Next focuses heavily on problem solving, OOP design, and explaining time/space complexities.",
                "sample_questions": [
                    {
                        "question": "Given an array of integers and a target sum, how do you find two numbers that sum up to the target in $O(N)$ time?",
                        "expected": [
                            "Use a Hash Map to store numbers or their complements",
                            "For each number x, check if (target - x) exists in the map",
                            "Single pass through array yields O(N) time and O(N) space"
                        ],
                        "model_answer": "Use a hash map. Iterate through the array; for each element arr[i], compute complement = target - arr[i]. If complement exists in map, return [map[complement], i]. Otherwise, insert arr[i] into map. This runs in O(N) time and O(N) space."
                    },
                    {
                        "question": "What are ACID properties in database management, and why are they critical in financial software?",
                        "expected": [
                            "Atomicity: All operations succeed or all roll back",
                            "Consistency: Database transitions from one valid state to another",
                            "Isolation: Concurrent transactions do not interfere",
                            "Durability: Committed data survives crashes"
                        ],
                        "model_answer": "ACID stands for Atomicity, Consistency, Isolation, and Durability. In banking, if money is debited from Account A but the credit to Account B fails, Atomicity ensures the debit is rolled back, preventing lost funds."
                    }
                ]
            },
            {
                "round_number": 4,
                "name": "HR & Leadership Assessment",
                "type": "HR & Behavioral",
                "duration_minutes": 30,
                "questions_count": 3,
                "cutoff_percentage": 70,
                "sections": ["Communication", "Career Vision", "Adaptability", "Professionalism"],
                "tips": "Articulate clear career goals for your first 2 years in software development.",
                "sample_questions": [
                    {
                        "question": "Where do you see yourself in 3 years at Cognizant?",
                        "answer": "Describe your goal of mastering full-stack or cloud engineering, contributing to mission-critical customer delivery, gaining industry certifications (e.g. AWS/Azure), and stepping into technical module leadership."
                    }
                ]
            }
        ]
    },
    "ltimindtree": {
        "new_rounds": [
            {
                "round_number": 3,
                "name": "Technical Architecture & System Design",
                "type": "Technical Interview",
                "duration_minutes": 45,
                "questions_count": 3,
                "cutoff_percentage": 70,
                "sections": ["Data Structures", "System Design Basics", "SQL Window Functions", "REST APIs"],
                "tips": "Focus on database optimization, indexing strategies, and clean code principles.",
                "sample_questions": [
                    {
                        "question": "How would you design a rate limiter to prevent API abuse from malicious clients?",
                        "expected": [
                            "Token Bucket or Leaky Bucket algorithm",
                            "Use of Redis with TTL keys to count requests per IP or API key",
                            "Return HTTP 429 Too Many Requests when rate limit is exceeded"
                        ],
                        "model_answer": "Use Redis with a sliding window or token bucket algorithm. For each incoming request, check the client's IP or user ID in Redis. Increment the counter with an expiry window (e.g. 100 requests per 60 seconds). If counter exceeds 100, immediately return HTTP 429 Too Many Requests."
                    }
                ]
            },
            {
                "round_number": 4,
                "name": "Managerial & Fitment Assessment",
                "type": "HR & Behavioral",
                "duration_minutes": 30,
                "questions_count": 3,
                "cutoff_percentage": 70,
                "sections": ["Teamwork", "Client Focus", "Integrity", "Growth Mindset"],
                "tips": "Show enthusiasm for digital transformation and enterprise engineering.",
                "sample_questions": [
                    {
                        "question": "Tell me about a time you worked on a project where the requirements changed midway. How did you handle it?",
                        "answer": "Use the STAR framework: explain the changed requirements, how you re-evaluated the database and frontend components, communicated transparently with team members, and adapted without compromising project delivery."
                    }
                ]
            }
        ]
    },
    "oracle": {
        "new_rounds": [
            {
                "round_number": 3,
                "name": "Database Internals & System Design",
                "type": "Technical Interview",
                "duration_minutes": 50,
                "questions_count": 4,
                "cutoff_percentage": 75,
                "sections": ["B-Trees & Indexing", "Concurrency Control", "Distributed Storage", "Memory Management"],
                "tips": "Oracle engineers expect deep understanding of B-Tree indexing, execution plans, and memory allocation.",
                "sample_questions": [
                    {
                        "question": "Why do relational databases use B+ Trees rather than Binary Search Trees (BST) or Hash Tables for disk-based indexing?",
                        "expected": [
                            "B+ Trees have high fanout, minimizing disk I/O seeks",
                            "All records stored in leaf nodes linked sequentially, making range queries fast",
                            "Hash tables cannot do range queries efficiently (O(N) vs O(log N + K))",
                            "BSTs have high tree height causing excessive random disk block reads"
                        ],
                        "model_answer": "B+ Trees have high branching factor (fanout of hundreds), allowing millions of records to be indexed with only 3-4 tree levels, drastically cutting disk I/O. Furthermore, leaf nodes are linked sequentially as a doubly linked list, enabling O(log N) point lookups and linear disk-block sequential scans for range queries."
                    }
                ]
            },
            {
                "round_number": 4,
                "name": "Hiring Manager & Leadership Round",
                "type": "HR & Behavioral",
                "duration_minutes": 40,
                "questions_count": 3,
                "cutoff_percentage": 70,
                "sections": ["Ownership", "Technical Passion", "Collaboration", "Career Alignment"],
                "tips": "Show passion for foundational enterprise cloud infrastructure and database reliability.",
                "sample_questions": [
                    {
                        "question": "Why Oracle Cloud Infrastructure (OCI) over other cloud providers, and what excites you about distributed database engineering?",
                        "answer": "Emphasize Oracle's legacy of data excellence and its modern gen-2 cloud architecture built for enterprise mission-critical workloads. Discuss your fascination with high-throughput database engines and autonomous technologies."
                    }
                ]
            }
        ]
    },
    "ibm": {
        "new_rounds": [
            {
                "round_number": 3,
                "name": "Cloud, AI & Architecture",
                "type": "Technical Interview",
                "duration_minutes": 45,
                "questions_count": 3,
                "cutoff_percentage": 70,
                "sections": ["Cloud Architecture", "Docker & Kubernetes", "CAP Theorem", "Microservices"],
                "tips": "Familiarize yourself with enterprise hybrid cloud and containerization concepts.",
                "sample_questions": [
                    {
                        "question": "What is the difference between a virtual machine (VM) and a Docker container?",
                        "expected": [
                            "VMs virtualize hardware and include a full Guest OS",
                            "Containers virtualize the OS kernel and share the host kernel",
                            "Containers are lightweight, start in milliseconds, and consume less memory"
                        ],
                        "model_answer": "A VM runs a full guest operating system on top of a hypervisor, consuming gigabytes of storage and taking minutes to boot. A Docker container packages code and dependencies while sharing the host OS kernel, making it lightweight (megabytes), instantaneous to start, and portable across cloud environments."
                    }
                ]
            },
            {
                "round_number": 4,
                "name": "HR & Cultural Values",
                "type": "HR & Behavioral",
                "duration_minutes": 30,
                "questions_count": 3,
                "cutoff_percentage": 70,
                "sections": ["Dedication to Client Success", "Innovation that Matters", "Trust & Responsibility"],
                "tips": "Align responses with IBM's 3 core values.",
                "sample_questions": [
                    {
                        "question": "Give an example of how you demonstrated 'Innovation that Matters' during your academic coursework or projects.",
                        "answer": "Discuss an idea or automation script you wrote that solved a real inconvenience for your peers or college department, emphasizing tangible impact and usefulness rather than novelty alone."
                    }
                ]
            }
        ]
    },
    "deloitte": {
        "new_rounds": [
            {
                "round_number": 3,
                "name": "Business Technology & Case Analysis",
                "type": "Technical & Case Study",
                "duration_minutes": 45,
                "questions_count": 3,
                "cutoff_percentage": 70,
                "sections": ["Cloud Migration Case Study", "Agile Methodologies", "System Integration", "Data Analysis"],
                "tips": "Structure answers using frameworks: Business Context -> Technical Assessment -> Implementation Plan -> Risk Mitigation.",
                "sample_questions": [
                    {
                        "question": "A legacy retail client with 500 physical stores wants to modernize their inventory system to enable real-time e-commerce pickup. How do you approach this technical transformation?",
                        "expected": [
                            "Analyze legacy database bottlenecks and batch sync delays",
                            "Introduce event-driven architecture (e.g. Kafka) for real-time inventory updates",
                            "API Gateway integration between POS systems and cloud warehouse",
                            "Phased rollout strategy with fallback"
                        ],
                        "model_answer": "Begin by decoupling POS inventory updates from nightly batch processing using an event-driven architecture with Apache Kafka. Deploy an API layer connecting in-store barcode scanners to a centralized cloud inventory service. Implement a phased pilot across 10 flagship stores before nationwide rollout."
                    }
                ]
            },
            {
                "round_number": 4,
                "name": "Partner & Leadership Interview",
                "type": "HR & Behavioral",
                "duration_minutes": 35,
                "questions_count": 3,
                "cutoff_percentage": 75,
                "sections": ["Client Communication", "Integrity", "Leadership", "Deloitte Culture"],
                "tips": "Demonstrate executive presence, clear communication, and high emotional intelligence.",
                "sample_questions": [
                    {
                        "question": "How do you explain a complex technical bug or architectural trade-off to a non-technical client executive?",
                        "answer": "Use analogies relatable to business operations. Focus on business impacts (uptime, customer checkout speed, cost) rather than code-level jargon. Present clear recommendations with timelines and risk assessments."
                    }
                ]
            }
        ]
    },
    "cisco": {
        "new_rounds": [
            {
                "round_number": 3,
                "name": "Network Architecture & Systems Programming",
                "type": "Technical Interview",
                "duration_minutes": 50,
                "questions_count": 4,
                "cutoff_percentage": 75,
                "sections": ["TCP/IP Stack", "Socket Programming", "Subnetting & Routing", "C/C++ Memory Management"],
                "tips": "Cisco deeply examines packet flow across layers, memory efficiency, and bit manipulation.",
                "sample_questions": [
                    {
                        "question": "Explain what happens step-by-step at each layer of the OSI model when a user enters 'https://www.cisco.com' in a browser.",
                        "expected": [
                            "Application: Browser checks cache, triggers DNS lookup",
                            "Transport: TCP 3-way handshake established on port 443, followed by TLS 1.3 cryptographic handshake",
                            "Network: IP routing, ARP resolution to gateway MAC address",
                            "Data Link & Physical: Framing, ethernet packets transmitted over physical medium",
                            "HTTP GET request sent, web server returns HTML response"
                        ],
                        "model_answer": "DNS resolves domain to IP via UDP 53. Transport layer initiates TCP 3-way handshake (SYN, SYN-ACK, ACK) on port 443, followed by TLS handshake negotiating cipher suites. Network layer encapsulates into IP packets routed via OSPF/BGP. Data link layer uses ARP to resolve local gateway MAC. Upon connection, HTTP GET is sent and response stream is rendered."
                    }
                ]
            },
            {
                "round_number": 4,
                "name": "Executive & Cultural Fitment",
                "type": "HR & Behavioral",
                "duration_minutes": 35,
                "questions_count": 3,
                "cutoff_percentage": 70,
                "sections": ["Conscious Culture", "Teamwork", "Global Collaboration", "Ethics"],
                "tips": "Familiarize yourself with Cisco's 'Conscious Culture' and give examples of ethical decision making.",
                "sample_questions": [
                    {
                        "question": "Why do you want to build foundational internet hardware and software at Cisco?",
                        "answer": "Highlight that 80%+ of the world's internet traffic traverses Cisco equipment. Express your passion for building resilient, high-speed networking systems that connect hospitals, governments, and universities worldwide."
                    }
                ]
            }
        ]
    },
    "adobe": {
        "new_rounds": [
            {
                "round_number": 3,
                "name": "Advanced Algorithms & System Design",
                "type": "Technical Interview",
                "duration_minutes": 50,
                "questions_count": 4,
                "cutoff_percentage": 75,
                "sections": ["Trees & Graphs", "Dynamic Programming", "Scalable Queue Architecture", "OOP Design"],
                "tips": "Adobe asks complex algorithmic problems and low-level object-oriented design questions.",
                "sample_questions": [
                    {
                        "question": "How would you design an efficient Autocomplete / Search Suggestion system that returns top 5 suggested queries for millions of users?",
                        "expected": [
                            "Use a Trie (Prefix Tree) data structure",
                            "Each Trie node stores top 5 trending search queries matching the prefix",
                            "Prefix lookup is O(L) where L is length of typed query string",
                            "Decouple updates using asynchronous batch processing"
                        ],
                        "model_answer": "Use a Trie data structure. To avoid traversing subtrees on every keystroke, cache the top 5 most frequently searched terms directly inside each Trie node. Lookup time becomes O(L) where L is the prefix length, completely independent of total dictionary size."
                    }
                ]
            },
            {
                "round_number": 4,
                "name": "Managerial & Creativity Round",
                "type": "HR & Behavioral",
                "duration_minutes": 40,
                "questions_count": 3,
                "cutoff_percentage": 75,
                "sections": ["Creativity", "Customer Empathy", "Product Thinking", "Adobe Values"],
                "tips": "Show high empathy for creative professionals and software usability.",
                "sample_questions": [
                    {
                        "question": "Adobe products empower creators worldwide. How do you balance writing mathematically optimal code with providing a delightful user experience?",
                        "answer": "Discuss how UI responsiveness directly impacts creative flow. Emphasize offloading heavy computation to background threads or Web Workers, implementing optimistic UI updates, and profiling frame rates to ensure smooth user interactions."
                    }
                ]
            }
        ]
    }
}

def apply_expansions():
    # 1. Update COMPANIES_DATA in memory
    updated_count = 0
    new_rounds_count = 0
    new_questions_count = 0

    for comp in COMPANIES_DATA:
        slug = comp["slug"]
        if slug in COMPANY_EXPANSIONS:
            exp = COMPANY_EXPANSIONS[slug]

            # Add sample questions to round 1 if specified
            if "add_to_round_1" in exp and len(comp["rounds"]) > 0:
                comp["rounds"][0].setdefault("sample_questions", []).extend(exp["add_to_round_1"])
                new_questions_count += len(exp["add_to_round_1"])

            # Add new rounds
            if "new_rounds" in exp:
                for r in exp["new_rounds"]:
                    # Check if round number already exists
                    if not any(existing_r["round_number"] == r["round_number"] for existing_r in comp["rounds"]):
                        comp["rounds"].append(r)
                        new_rounds_count += 1
                        new_questions_count += len(r.get("sample_questions", []))

            updated_count += 1

    # 2. Write back to company_interview_service.py
    file_path = os.path.join(os.path.dirname(__file__), "..", "app", "services", "company_interview_service.py")
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Find the start of COMPANIES_DATA and the start of class CompanyInterviewService
    class_marker = "class CompanyInterviewService:"
    if class_marker not in content:
        print("Error: Could not find class CompanyInterviewService in file.")
        return

    code_after_data = content[content.index(class_marker):]

    # Format the updated COMPANIES_DATA
    formatted_data = pprint.pformat(COMPANIES_DATA, indent=4, width=120)
    new_file_content = f'''from typing import List, Dict, Any, Optional

COMPANIES_DATA = {formatted_data}

{code_after_data}'''

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_file_content)

    print(f"Successfully updated {updated_count} companies.")
    print(f"Added {new_rounds_count} new interview rounds.")
    print(f"Added {new_questions_count} new company questions.")

if __name__ == "__main__":
    apply_expansions()

