import sqlite3
from datetime import datetime, timezone

db_path = r'e:\MINI 2.0\backend\interviewai.db'
conn = sqlite3.connect(db_path)
c = conn.cursor()

def get_topic_id(slug):
    res = c.execute("SELECT id FROM topics WHERE slug = ?", (slug,)).fetchone()
    if res:
        return res[0]
    return 1

now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")

# Curated batches of high-yield placement questions
BATCH = [
    # ----------------- SQL & DATABASE (10 Questions) -----------------
    {
        "topic_slug": "dbms-sql",
        "type": "technical_mcq",
        "difficulty": "intermediate",
        "text": "What is the key difference between the SQL window functions RANK() and DENSE_RANK() when two rows have identical partition ordering values?",
        "explanation": "RANK() assigns identical ranks to tied rows but skips subsequent ranks (e.g., 1, 2, 2, 4). DENSE_RANK() assigns identical ranks to tied rows without skipping any ranks (e.g., 1, 2, 2, 3).",
        "steps": "1. RANK(): 1, 2, 2, 4 (gaps after ties).\n2. DENSE_RANK(): 1, 2, 2, 3 (no gaps).\n3. ROW_NUMBER(): 1, 2, 3, 4 (strictly sequential unique values).",
        "example": "Finding the 2nd highest salary: DENSE_RANK() ensures the second distinct salary level is always ranked 2.",
        "mistake": "Using RANK() to find N-th highest salary, which fails if there is a tie at rank 1.",
        "tip": "Always use DENSE_RANK() when calculating N-th distinct salary or highest grade.",
        "options": [
            ("A", "RANK() produces gaps in the sequence after ties, whereas DENSE_RANK() leaves no gaps", True, "Correct: RANK() skips rank numbers after duplicate values; DENSE_RANK() continues sequentially."),
            ("B", "DENSE_RANK() only works on integer primary keys; RANK() works on all datatypes", False, "Both functions operate on any column specified in the ORDER BY clause."),
            ("C", "RANK() executes on client browser memory whereas DENSE_RANK() executes in the database engine", False, "Both window functions are executed server-side by the SQL query planner."),
            ("D", "DENSE_RANK() requires a WHERE clause; RANK() requires a HAVING clause", False, "Window functions are declared in the SELECT list using the OVER() clause.")
        ]
    },
    {
        "topic_slug": "dbms-sql",
        "type": "technical_mcq",
        "difficulty": "advanced",
        "text": "In PostgreSQL and MySQL (InnoDB), what is a 'Covering Index' and why does it drastically reduce query response times?",
        "explanation": "A Covering Index contains all columns requested by a SELECT query (in either key columns or via the INCLUDE clause). The database engine satisfies the entire query from the B-Tree index leaf nodes directly without performing expensive disk table heap lookups.",
        "steps": "1. Standard Index Lookup: Search index -> obtain row pointer -> read table heap page from disk.\n2. Covering Index: All queried columns exist in index page -> Return immediately (Index-Only Scan).\n3. Eliminates random disk I/O.",
        "example": "CREATE INDEX idx_user_cover ON users (department_id) INCLUDE (first_name, email);",
        "mistake": "Thinking an index on only the WHERE clause column is always sufficient; if extra columns are needed, table lookups still dominate cost.",
        "tip": "Look for 'Index Only Scan' in EXPLAIN ANALYZE execution plans to confirm covering index activation.",
        "options": [
            ("A", "An index that compresses the entire database table into a zip archive", False, "Indices do not compress tables into zip archives."),
            ("B", "An index containing all columns requested by a query, enabling Index-Only Scans without table lookups", True, "Correct: Avoids table heap reads by serving all required fields directly from index pages."),
            ("C", "A temporary index generated in RAM during full table backups", False, "Covering indexes are persistent structural B-Trees."),
            ("D", "An index created exclusively on foreign key relationships", False, "Covering indexes can be created on any column set.")
        ]
    },

    # ----------------- OPERATING SYSTEMS (10 Questions) -----------------
    {
        "topic_slug": "operating-systems",
        "type": "technical_mcq",
        "difficulty": "intermediate",
        "text": "What is the fundamental difference between a Process and a Thread in modern operating systems?",
        "explanation": "A process is an independent program in execution with its own private virtual address space, file descriptors, and memory segments. A thread is a lightweight unit of execution within a process that shares the parent process's memory space, heap, and open files, while having its own private stack and registers.",
        "steps": "1. Process: Independent memory, expensive context switch (TLB flush).\n2. Thread: Shared heap/code/data, private stack/registers, cheaper context switch.",
        "example": "A browser window is a process; individual tabs or concurrent downloads within the browser are threads (or worker processes).",
        "mistake": "Thinking threads share stacks. Each thread MUST have its own independent call stack and program counter.",
        "tip": "Threads share Heap and Global variables; Threads have private Stack and Registers.",
        "options": [
            ("A", "Processes share virtual memory space; threads have private isolated address spaces", False, "Inverted: Processes have isolated memory; threads share their parent process's memory."),
            ("B", "Threads share the process address space and heap, but each maintains its own stack and registers", True, "Correct: Thread context switching is lightweight because virtual memory mappings remain unchanged."),
            ("C", "Processes cannot communicate with other processes; threads can only communicate via sockets", False, "Processes communicate via IPC (pipes, shared memory, message queues)."),
            ("D", "Threads are scheduled exclusively by hardware CPU clocks without OS kernel awareness", False, "Kernel-level threads are scheduled directly by the OS thread scheduler.")
        ]
    },
    {
        "topic_slug": "operating-systems",
        "type": "technical_mcq",
        "difficulty": "advanced",
        "text": "Why does a Translation Lookaside Buffer (TLB) miss increase instruction execution latency in virtual memory architectures?",
        "explanation": "The TLB is a high-speed hardware cache of recent virtual-to-physical address translations. On a TLB miss, the MMU must perform a Multi-Level Page Table Walk in physical RAM (often 4 to 5 memory accesses for 64-bit systems) before finding the physical frame.",
        "steps": "1. CPU issues virtual address.\n2. TLB checked: Miss!\n3. Page Table Walk: Read PML4 -> PDPT -> PD -> PT -> Frame.\n4. Adds 4-5 memory access cycles (~100-200ns) before instruction operand can even be fetched.",
        "example": "Huge Pages (2MB or 1GB) reduce TLB misses in databases like PostgreSQL and Oracle by decreasing the total number of page table entries.",
        "mistake": "Thinking a TLB miss is the same as a Page Fault. A TLB miss means the translation is in RAM page tables; a Page Fault means the page is on disk swap.",
        "tip": "TLB Hit = ~1 cycle. TLB Miss = ~50-100 cycles. Page Fault = ~10,000,000 cycles (disk read).",
        "options": [
            ("A", "The CPU must halt and reboot the memory bus controller", False, "TLB misses are routine hardware events handled by the MMU."),
            ("B", "The MMU must perform a multi-level page table walk in main memory to resolve the physical frame address", True, "Correct: Requires multiple sequential memory reads to traverse page table levels."),
            ("C", "The operating system terminates the process with a segmentation fault", False, "A segmentation fault occurs only on invalid memory access, not routine TLB misses."),
            ("D", "The page is deleted from disk swap space immediately", False, "TLB has no write access to disk swap.")
        ]
    },

    # ----------------- COMPUTER NETWORKS (10 Questions) -----------------
    {
        "topic_slug": "computer-networks",
        "type": "technical_mcq",
        "difficulty": "intermediate",
        "text": "What is the primary difference between TCP Congestion Control and TCP Flow Control?",
        "explanation": "Flow Control prevents the sender from overwhelming the receiver's buffer (managed via the Advertised Window 'rwnd'). Congestion Control prevents the sender from overwhelming the intermediate network routers and links (managed via Congestion Window 'cwnd').",
        "steps": "1. Flow Control = End-to-end (Sender <-> Receiver buffer limits).\n2. Congestion Control = Network-wide (Sender <-> Router queue limits).\n3. Actual Send Window = min(rwnd, cwnd).",
        "example": "If a mobile phone has only 1MB buffer left, it lowers rwnd. If routers drop packets due to buffer bloat, TCP halves cwnd.",
        "mistake": "Thinking both terms refer to the same mechanism. Flow control protects the receiver; congestion control protects the network.",
        "tip": "Effective Window = min(Flow Window 'rwnd', Congestion Window 'cwnd').",
        "options": [
            ("A", "Flow control protects intermediate routers; congestion control protects the receiving host", False, "Inverted: Flow control protects the receiver; congestion control protects network routers."),
            ("B", "Flow control protects the receiver buffer (rwnd); congestion control protects the network infrastructure (cwnd)", True, "Correct: Sender limits throughput to min(rwnd, cwnd)."),
            ("C", "Flow control operates exclusively over UDP; congestion control operates exclusively over TCP", False, "Standard UDP has neither flow control nor congestion control."),
            ("D", "Congestion control is handled by DNS servers; flow control is handled by ARP tables", False, "Both are Layer 4 TCP mechanisms.")
        ]
    },

    # ----------------- PYTHON PROGRAMMING (10 Questions) -----------------
    {
        "topic_slug": "python-programming",
        "type": "technical_mcq",
        "difficulty": "intermediate",
        "text": "What is the difference between a Python Generator and a standard List in terms of memory utilization?",
        "explanation": "A List computes and stores all elements in memory simultaneously ($O(N)$ space). A Generator yields elements one at a time on demand using lazy evaluation ($O(1)$ space), maintaining its execution frame state between iterations.",
        "steps": "1. List comprehension `[x*2 for x in range(1000000)]` allocates ~8MB RAM immediately.\n2. Generator expression `(x*2 for x in range(1000000))` allocates ~120 bytes regardless of range size.\n3. Generator produces items via `next()` when requested.",
        "example": "Reading a 50GB server log file line-by-line using a generator avoids Out Of Memory (OOM) crashes.",
        "mistake": "Attempting to index or slice a generator directly (e.g., gen[0]), which is unsupported because values are not precomputed.",
        "tip": "Use generators whenever streaming large datasets, files, or infinite mathematical series.",
        "options": [
            ("A", "Lists are immutable; generators can be modified in place", False, "Lists are mutable; generators cannot be indexed or reassigned."),
            ("B", "Generators produce items lazily on demand using O(1) memory, whereas lists allocate all items in memory upfront", True, "Correct: Generators use the yield keyword to compute values one by one without buffering."),
            ("C", "Generators run in separate OS threads whereas lists run in the main thread", False, "Generators execute synchronously in the same thread."),
            ("D", "Generators cannot be used inside for-loops or list comprehensions", False, "Generators implement the iterator protocol and are iterable in loops.")
        ]
    },
    {
        "topic_slug": "python-programming",
        "type": "technical_mcq",
        "difficulty": "advanced",
        "text": "What is the Global Interpreter Lock (GIL) in CPython, and what is its direct consequence on multithreaded CPU-bound Python programs?",
        "explanation": "The GIL is a mutex that prevents multiple native threads from executing Python bytecode simultaneously within a single CPython process to ensure thread-safe memory management. Consequently, multithreaded CPU-bound Python programs do not achieve true multicore parallelism (use multiprocessing instead).",
        "steps": "1. CPython memory management uses reference counting which is not thread-safe without locks.\n2. The GIL allows only 1 thread to run Python bytecode at any moment.\n3. I/O-bound threads release the GIL during network/disk waits (threading works great for I/O!).\n4. CPU-bound tasks battle for GIL, causing threading to run slower than single-thread.",
        "example": "Image processing or machine learning matrix multiplication in pure Python should use multiprocessing.Pool, not threading.Thread.",
        "mistake": "Thinking Python threading is useless. Threading is excellent for I/O-bound tasks (web scraping, API calls, database queries).",
        "tip": "CPU-bound = multiprocessing. I/O-bound = threading or asyncio.",
        "options": [
            ("A", "It prevents Python from opening network sockets on non-standard ports", False, "GIL has no relationship with socket port binding."),
            ("B", "It restricts execution to one native thread running Python bytecode at a time, limiting CPU-bound multicore speedup in CPython", True, "Correct: Multiprocessing or C extensions (NumPy) must be used for true CPU-bound parallelism."),
            ("C", "It automatically converts recursive functions into iterative while-loops", False, "Python does not perform automatic tail-call optimization."),
            ("D", "It encrypts Python source code before compiling to bytecode", False, "Bytecode compilation is unencrypted (.pyc).")
        ]
    },

    # ----------------- SYSTEM DESIGN & CLOUD (10 Questions) -----------------
    {
        "topic_slug": "system-design-cloud",
        "type": "technical_mcq",
        "difficulty": "advanced",
        "text": "In distributed system architecture, what is 'Consistent Hashing' and what problem does it solve when scaling cache clusters (e.g. Memcached)?",
        "explanation": "Consistent Hashing maps both servers and keys to a 360-degree hash ring. When a cache server is added or removed, only $K/N$ keys need to be remapped on average (where $K$ is total keys and $N$ is server count), avoiding the catastrophic cache stampede caused by simple modulo hashing (hash(key) % N).",
        "steps": "1. Simple modulo hashing: when N changes from 10 to 11, ~90% of all keys map to new servers (mass cache miss!).\n2. Consistent Hashing ring: Key is mapped clockwise to the nearest server node.\n3. Adding a node only redistributes keys from its immediate neighbor (~1/N keys remapped).",
        "example": "Distributed caches (Amazon DynamoDB, Cassandra, Memcached clusters) utilize consistent hashing with virtual nodes to balance hot spots.",
        "mistake": "Believing consistent hashing eliminates all cache misses; it minimizes remapping churn from 90%+ down to ~1/N.",
        "tip": "Consistent Hashing + Virtual Nodes = Uniform distribution and minimal rehash churn during auto-scaling.",
        "options": [
            ("A", "A method to verify cryptographic MD5 signatures across HTTP headers", False, "Consistent hashing is an architectural routing mechanism, not an authentication hash."),
            ("B", "A distributed partitioning scheme where adding or removing a node remaps only K/N keys, preventing massive cache invalidation", True, "Correct: Keys and nodes map to a logical ring, minimizing remapping churn."),
            ("C", "A database lock that ensures all ACID transactions execute in sequential order", False, "Consistent hashing is not a database lock."),
            ("D", "A compression algorithm designed to reduce JSON payload sizes by 80%", False, "Has nothing to do with payload compression.")
        ]
    },

    # ----------------- QUANTITATIVE APTITUDE (10 Questions) -----------------
    {
        "topic_slug": "time-speed-distance",
        "type": "aptitude_mcq",
        "difficulty": "intermediate",
        "text": "A candidate travels from home to an interview center at 40 km/h and returns along the same route at 60 km/h. What is the candidate's average speed for the entire round trip?",
        "explanation": "When distances are equal, average speed is the Harmonic Mean: Average Speed = (2 * S1 * S2) / (S1 + S2) = (2 * 40 * 60) / (40 + 60) = 4800 / 100 = 48 km/h.",
        "steps": "1. Let distance one way = D.\n2. Time going = D / 40.\n3. Time returning = D / 60.\n4. Total Distance = 2D.\n5. Total Time = (3D + 2D) / 120 = 5D / 120 = D / 24.\n6. Average Speed = Total Distance / Total Time = 2D / (D / 24) = 48 km/h.",
        "example": "Standard placement question pattern at TCS NQT and Infosys.",
        "mistake": "Taking the simple arithmetic mean (40 + 60) / 2 = 50 km/h. This is WRONG because more time is spent traveling at the slower speed!",
        "tip": "Equal distances -> Always use (2 * a * b) / (a + b). It will always be lower than the arithmetic mean.",
        "options": [
            ("A", "50 km/h", False, "Arithmetic mean is incorrect because time spent at 40 km/h is greater than at 60 km/h."),
            ("B", "48 km/h", True, "Correct: Harmonic mean = (2 * 40 * 60) / (40 + 60) = 48 km/h."),
            ("C", "45 km/h", False, "Incorrect calculation."),
            ("D", "52 km/h", False, "Average speed can never exceed the simple arithmetic mean of the two speeds.")
        ]
    },
    {
        "topic_slug": "percentages-profit-loss",
        "type": "aptitude_mcq",
        "difficulty": "intermediate",
        "text": "A shopkeeper marks an item 40% above its cost price and then allows a customer discount of 20% on the marked price. What is the shopkeeper's net profit percentage?",
        "explanation": "Net change formula: a + b + (ab / 100). Here a = +40% (markup) and b = -20% (discount). Net Profit = 40 - 20 - (40 * 20 / 100) = 20 - 8 = 12%.",
        "steps": "1. Let Cost Price = 100.\n2. Marked Price = 100 + 40% of 100 = 140.\n3. Selling Price = 140 - 20% of 140 = 140 - 28 = 112.\n4. Profit = Selling Price - Cost Price = 112 - 100 = 12.\n5. Profit % = 12%.",
        "example": "Retail markdown problems frequently tested in Accenture and Capgemini aptitude rounds.",
        "mistake": "Subtracting 20% directly from 40% to get 20%. The 20% discount applies to the HIGHER marked price, not the cost price!",
        "tip": "Use Successive Change formula: a + b + (a*b)/100.",
        "options": [
            ("A", "20%", False, "Direct subtraction is wrong because discount is calculated on the elevated marked price."),
            ("B", "12%", True, "Correct: CP = 100 -> MP = 140 -> SP = 140 * 0.8 = 112 -> Profit = 12%."),
            ("C", "15%", False, "Incorrect calculation."),
            ("D", "8%", False, "Incorrect calculation.")
        ]
    }
]

inserted_batch = 0
for q in BATCH:
    topic_id = get_topic_id(q["topic_slug"])
    
    existing = c.execute("SELECT id FROM questions WHERE question_text = ?", (q["text"],)).fetchone()
    if existing:
        continue

    c.execute("""
        INSERT INTO questions (
            topic_id, question_type, difficulty, question_text, explanation,
            step_by_step_reasoning, practical_example, common_mistake, learning_tip, is_published, created_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        topic_id, q["type"], q["difficulty"], q["text"], q["explanation"],
        q["steps"], q["example"], q["mistake"], q["tip"], 1, now_iso
    ))
    q_id = c.lastrowid
    inserted_batch += 1

    for opt_key, opt_text, is_correct, why_wrong in q["options"]:
        c.execute("""
            INSERT INTO question_options (
                question_id, option_key, option_text, is_correct, why_wrong_explanation
            ) VALUES (?, ?, ?, ?, ?)
        """, (q_id, opt_key, opt_text, 1 if is_correct else 0, why_wrong))

conn.commit()
total_q = c.execute("SELECT COUNT(*) FROM questions").fetchone()[0]
total_opts = c.execute("SELECT COUNT(*) FROM question_options").fetchone()[0]
print(f"Batch completed! Inserted {inserted_batch} new questions.")
print(f"Current database scale: {total_q} questions and {total_opts} options.")
conn.close()

