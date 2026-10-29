import sqlite3
from datetime import datetime, timezone

db_path = r'e:\MINI 2.0\backend\interviewai.db'
conn = sqlite3.connect(db_path)
c = conn.cursor()

def get_topic_id(slug):
    res = c.execute("SELECT id FROM topics WHERE slug = ?", (slug,)).fetchone()
    if res:
        return res[0]
    res_fallback = c.execute("SELECT id FROM topics LIMIT 1").fetchone()
    return res_fallback[0] if res_fallback else 1

now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")

QUESTIONS = [
    # ------------------ DBMS & SQL ------------------
    {
        "topic_slug": "dbms-sql",
        "type": "technical_mcq",
        "difficulty": "intermediate",
        "text": "What is the primary difference between Clustered Index and Non-Clustered Index in relational databases like SQL Server and MySQL?",
        "explanation": "A Clustered Index dictates the physical ordering of data rows on the storage disk; a table can only have one clustered index. A Non-Clustered Index is a separate secondary B-Tree structure storing index keys and row pointers back to the clustered index/data page.",
        "steps": "1. Clustered: Physical table order = Index order. Only 1 per table (typically Primary Key).\n2. Non-Clustered: Separate structure pointing to data rows. A table can have multiple non-clustered indexes.\n3. Clustered index searches don't need secondary lookups.",
        "example": "Primary key 'employee_id' creates a clustered index; non-clustered index on 'email' speeds up user login lookups.",
        "mistake": "Believing a table can have multiple clustered indexes. Physical rows can only be ordered on disk in one physical sequence.",
        "tip": "Always place clustered index on columns used in frequent range scans (e.g., date ranges or auto-increment IDs).",
        "options": [
            ("A", "Clustered index defines the physical order of data rows on disk (max 1 per table); Non-Clustered is a separate index pointing to data rows", True, "Correct: Physical disk row layout matches the clustered index."),
            ("B", "Non-clustered indexes are stored in RAM; Clustered indexes are stored on disk", False, "Both index types reside on disk and are cached into buffer pool RAM."),
            ("C", "A table can have up to 10 clustered indexes but only 1 non-clustered index", False, "Inverted: Maximum 1 clustered index, multiple non-clustered indexes."),
            ("D", "Clustered indexes are exclusively used for JSON data types", False, "Clustered indexes apply to relational column datatypes.")
        ]
    },
    {
        "topic_slug": "dbms-sql",
        "type": "technical_mcq",
        "difficulty": "advanced",
        "text": "In database concurrency control, what is a 'Dirty Read' and at which SQL ANSI transaction isolation level is it permitted?",
        "explanation": "A Dirty Read occurs when Transaction A reads data that has been modified by Transaction B but NOT yet committed. If Transaction B rolls back, Transaction A worked with data that technically never existed. It is permitted only in Read Uncommitted.",
        "steps": "1. Tx 1 updates account balance from $100 to $500 (uncommitted).\n2. Tx 2 reads balance as $500 (Dirty Read!).\n3. Tx 1 encounters error and issues ROLLBACK.\n4. Real balance is still $100, but Tx 2 made business decisions on $500.",
        "example": "Read Uncommitted isolation level permits dirty reads.",
        "mistake": "Confusing Dirty Read with Non-Repeatable Read. Dirty Read involves uncommitted data; Non-Repeatable Read involves data changed and committed by another transaction.",
        "tip": "Production OLTP systems should use at least Read Committed or Repeatable Read.",
        "options": [
            ("A", "Reading uncommitted modifications made by another concurrent transaction; allowed under Read Uncommitted", True, "Correct: Reading uncommitted, rollback-vulnerable state."),
            ("B", "Reading corrupted hard drive sectors; allowed under Serializable", False, "Hardware corruption is not an ANSI isolation level concept."),
            ("C", "A query reading two different primary keys simultaneously; allowed under Snapshot", False, "Reading multiple primary keys is normal relational behavior."),
            ("D", "Reading data after a database crash; allowed under Repeatable Read", False, "Crash recovery is handled by the WAL/redo log, not dirty reads.")
        ]
    },
    {
        "topic_slug": "dbms-sql",
        "type": "technical_mcq",
        "difficulty": "intermediate",
        "text": "What does the SQL command 'TRUNCATE TABLE' do differently compared to 'DELETE FROM' without a WHERE clause?",
        "explanation": "TRUNCATE is a DDL command that deallocates all data pages in one operation, resets auto-increment sequences, cannot be rolled back in some engines (like MySQL outside transactions), and is significantly faster because it does not log row-by-row deletions.",
        "steps": "1. DELETE: DML command. Logs every deleted row in the redo/transaction log. Fires DELETE triggers. Slower.\n2. TRUNCATE: DDL command. Deallocates data pages. Resets identity counters. Does not fire row triggers. High performance.",
        "example": "TRUNCATE TABLE audit_logs; frees megabytes of disk pages instantly.",
        "mistake": "Thinking TRUNCATE fires AFTER DELETE triggers. Triggers are bypassed because pages are deallocated en masse.",
        "tip": "Use TRUNCATE when clearing an entire staging table quickly; use DELETE when triggers or row-level logging are required.",
        "options": [
            ("A", "TRUNCATE is a DDL operation that deallocates data pages without logging individual rows, running much faster than DELETE", True, "Correct: Deallocates pages and resets auto-increment counters efficiently."),
            ("B", "DELETE removes the table schema from the database, while TRUNCATE preserves the table", False, "DROP removes table schema; DELETE removes table rows."),
            ("C", "TRUNCATE only deletes the first 100 rows", False, "TRUNCATE empties the entire table."),
            ("D", "DELETE cannot be rolled back under any circumstances", False, "DELETE statements inside transactions can be rolled back.")
        ]
    },

    # ------------------ OPERATING SYSTEMS ------------------
    {
        "topic_slug": "operating-systems",
        "type": "technical_mcq",
        "difficulty": "intermediate",
        "text": "What is the difference between a Mutex and a Counting Semaphore in multi-threaded programming?",
        "explanation": "A Mutex (Mutual Exclusion) has ownership semantics: only the thread that acquired (locked) the mutex can release (unlock) it. A Semaphore is a signaling mechanism with an integer counter where any thread can post (signal/increment) or wait (decrement).",
        "steps": "1. Mutex: Binary lock (0 or 1). Thread that locks MUST unlock. Used for mutual exclusion around critical sections.\n2. Semaphore: Counter >= 0. Used for signaling (e.g. Producer-Consumer buffer count) or resource pool limiting.\n3. A semaphore can be signaled by a thread that did not wait on it.",
        "example": "Mutex protects shared bank account balance variable; Counting Semaphore limits concurrent active database connections to 10.",
        "mistake": "Calling a Mutex 'just a binary semaphore'. Mutex has strict ownership and priority inheritance to prevent priority inversion.",
        "tip": "Mutex = Ownership & Mutual exclusion; Semaphore = Signaling & Resource counter.",
        "options": [
            ("A", "A Mutex has thread ownership (only the locking thread can unlock it); a Semaphore is a counter/signaling mechanism that any thread can signal", True, "Correct: Mutex requires ownership; semaphores facilitate signaling between different threads."),
            ("B", "Semaphores run only in hardware; Mutexes run in user software", False, "Both synchronization primitives are provided by OS kernels and threading libraries."),
            ("C", "A Mutex can allow up to 100 threads in the critical section at the same time", False, "A Mutex only permits exactly 1 thread at a time."),
            ("D", "Counting Semaphores do not work on multi-core processors", False, "Semaphores utilize hardware atomic instructions (CMPXCHG) on multi-core CPUs.")
        ]
    },
    {
        "topic_slug": "operating-systems",
        "type": "technical_mcq",
        "difficulty": "advanced",
        "text": "What four Coffman Conditions must hold simultaneously for a Deadlock to occur in an operating system?",
        "explanation": "Deadlock requires all 4 Coffman conditions: (1) Mutual Exclusion, (2) Hold and Wait, (3) No Preemption, and (4) Circular Wait. Breaking any one of these four conditions prevents deadlock.",
        "steps": "1. Mutual Exclusion: Resource held exclusively by one process.\n2. Hold and Wait: Process holds resource A while waiting for resource B.\n3. No Preemption: Resources cannot be forcibly seized; only released voluntarily.\n4. Circular Wait: P0 waits for P1, P1 waits for P2... Pn waits for P0.\n5. Eliminating any one condition (e.g., ordering resource acquisition to break Circular Wait) guarantees no deadlock.",
        "example": "Banker's Algorithm ensures safe resource allocation states to avoid deadlocks.",
        "mistake": "Thinking 3 conditions are enough for deadlock. All four MUST hold simultaneously.",
        "tip": "Enforcing a global linear order on lock acquisition breaks Circular Wait.",
        "options": [
            ("A", "Mutual Exclusion, Hold and Wait, No Preemption, and Circular Wait", True, "Correct: The four Coffman conditions necessary and sufficient for deadlock."),
            ("B", "High CPU, Low RAM, Network Partition, and Disk Full", False, "Resource exhaustion causes slowness or crashes, not formal deadlock."),
            ("C", "Paging, Segmentation, Swapping, and Thrashing", False, "These are virtual memory management concepts."),
            ("D", "First In First Out, Round Robin, Priority Scheduling, and SJF", False, "These are CPU scheduling algorithms.")
        ]
    },
    {
        "topic_slug": "operating-systems",
        "type": "technical_mcq",
        "difficulty": "intermediate",
        "text": "What is 'Thrashing' in virtual memory systems and what causes it?",
        "explanation": "Thrashing occurs when the operating system spends more time swapping virtual memory pages between RAM and swap disk than executing actual CPU instructions. It is caused when the sum of working sets of all running processes exceeds total physical RAM.",
        "steps": "1. Too many processes active in memory.\n2. Physical RAM fills up completely.\n3. Process A faults: OS reads page from disk, evicting Process B's page.\n4. Process B immediately faults: OS reads B, evicting Process A's page.\n5. CPU utilization drops near zero while disk queue stays at 100%.",
        "example": "Computer freezes and hard drive light blinks solid when opening 50 memory-intensive browser tabs.",
        "mistake": "Thinking thrashing means the CPU is calculating too fast. Thrashing means CPU is idle waiting for disk I/O.",
        "tip": "Fix thrashing by reducing degree of multiprogramming or adding physical RAM.",
        "options": [
            ("A", "When the OS spends excessive time swapping pages in/out of disk rather than executing instructions, caused by RAM oversubscription", True, "Correct: Working set sizes exceed physical memory causing constant page faults."),
            ("B", "When the CPU clock speed exceeds the motherboard bus frequency", False, "Clock multipliers handle CPU frequency; not related to thrashing."),
            ("C", "When network bandwidth drops to zero during a DDoS attack", False, "Thrashing is a memory/disk swap phenomenon."),
            ("D", "When two processes write to the same register simultaneously", False, "Registers are thread-private.")
        ]
    },

    # ------------------ COMPUTER NETWORKS ------------------
    {
        "topic_slug": "computer-networks",
        "type": "technical_mcq",
        "difficulty": "intermediate",
        "text": "How does HTTP/2 achieve significantly lower latency compared to HTTP/1.1?",
        "explanation": "HTTP/2 introduces binary framing and multiplexing over a single persistent TCP connection, allowing multiple concurrent bidirectional requests and responses without Head-of-Line (HoL) blocking at the HTTP layer, along with HPACK header compression and Server Push.",
        "steps": "1. HTTP/1.1: 1 request-response per TCP connection (or max 6 connections per domain in browsers). Causes Head-of-Line blocking.\n2. HTTP/2: Single TCP connection broken into binary frames tagged with stream IDs.\n3. Streams interleave simultaneously without waiting for previous responses.\n4. HPACK compresses redundant HTTP headers (cookies, user-agents).",
        "example": "Loading a webpage with 100 images requires only 1 TCP connection in HTTP/2 versus dozens of TCP handshakes in HTTP/1.1.",
        "mistake": "Thinking HTTP/2 switches to UDP. HTTP/2 still uses TCP; HTTP/3 (QUIC) is what switched to UDP.",
        "tip": "HTTP/2 = Multiplexed streams over single TCP + HPACK; HTTP/3 = QUIC over UDP.",
        "options": [
            ("A", "Binary framing and multiplexed concurrent streams over a single TCP connection, eliminating application Head-of-Line blocking", True, "Correct: Interleaves streams over a single socket and compresses headers with HPACK."),
            ("B", "Replaces IP addresses with domain name hashes", False, "IP addresses remain standard Layer 3 addressing."),
            ("C", "Eliminates all TLS encryption overhead by transmitting plain text", False, "HTTP/2 mandates TLS (HTTPS) in all major modern browsers."),
            ("D", "Sends all web pages via satellite radio signals", False, "HTTP/2 operates over standard internet transport infrastructure.")
        ]
    },
    {
        "topic_slug": "computer-networks",
        "type": "technical_mcq",
        "difficulty": "intermediate",
        "text": "What is the difference between TCP and UDP at the Transport Layer (Layer 4)?",
        "explanation": "TCP is connection-oriented, provides guaranteed reliable delivery, error checking, in-order sequencing, flow control (Sliding Window), and congestion control. UDP is connectionless, lightweight, and transmits datagrams without guarantees of delivery or ordering, prioritizing minimal latency.",
        "steps": "1. TCP: 3-way handshake, retransmission of lost packets (ACKs), sequence numbers, flow control. Used in HTTP, SSH, FTP, SQL.\n2. UDP: No handshake, fire-and-forget, header size only 8 bytes (vs TCP 20+ bytes). Used in DNS, VoIP, Video Streaming, Gaming.",
        "example": "Online multiplayer games use UDP so player positions update with zero buffering delay even if a single packet drops.",
        "mistake": "Assuming UDP does not have checksums. UDP has an optional 16-bit checksum for error detection, but does NOT retransmit.",
        "tip": "Need reliability & ordered data? Use TCP. Need lowest latency & can tolerate packet drops? Use UDP.",
        "options": [
            ("A", "TCP provides reliable, ordered, error-checked delivery with flow control; UDP provides fast, connectionless delivery without delivery guarantees", True, "Correct: Core architectural distinction between Transport Layer protocols."),
            ("B", "TCP operates on Layer 7; UDP operates on Layer 2", False, "Both TCP and UDP operate strictly at Layer 4 (Transport Layer)."),
            ("C", "UDP packets can never be sent over Wi-Fi networks", False, "Wi-Fi carries both TCP and UDP frames seamlessly."),
            ("D", "TCP cannot transmit text characters", False, "TCP carries any arbitrary binary payload including text.")
        ]
    },

    # ------------------ DSA & ALGORITHMS ------------------
    {
        "topic_slug": "dsa-arrays-strings",
        "type": "technical_mcq",
        "difficulty": "advanced",
        "text": "What is the primary advantage of the Knuth-Morris-Pratt (KMP) pattern searching algorithm over naive string matching?",
        "explanation": "KMP searches for occurrences of a pattern P of length M in text T of length N in strictly O(N + M) worst-case time by preprocessing the pattern into a Longest Prefix which is also Suffix (LPS) array, avoiding backtracking in the main text string.",
        "steps": "1. Naive string match: When a mismatch occurs after K characters, backtracks text pointer by K-1. Worst case O(N * M).\n2. KMP: Precomputes LPS array for pattern P in O(M).\n3. When mismatch occurs at P[j], LPS[j-1] indicates the next position in pattern to compare without rewinding text index i.\n4. Text index i strictly moves forward: O(N + M) total time.",
        "example": "Matching 'AAAB' inside 'AAAAAAAB' runs in linear time with KMP, whereas naive search re-compares redundant prefixes.",
        "mistake": "Thinking KMP sorts the string. KMP finds exact substring matches via prefix-suffix automata.",
        "tip": "LPS array stores the length of the longest proper prefix of pattern[0..i] that is also a suffix of pattern[0..i].",
        "options": [
            ("A", "Precomputes an LPS array to avoid backtracking the text pointer, guaranteeing linear O(N + M) time", True, "Correct: Eliminates redundant backtracking comparisons using prefix-suffix table."),
            ("B", "Sorts all characters alphabetically before searching", False, "Sorting destroys character positional sequence."),
            ("C", "Compresses the text into a zip archive before pattern matching", False, "KMP is a pattern matching algorithm, not compression."),
            ("D", "Requires O(N^3) memory storage", False, "Auxiliary space is only O(M) for the LPS array.")
        ]
    },
    {
        "topic_slug": "dsa-trees-graphs",
        "type": "technical_mcq",
        "difficulty": "intermediate",
        "text": "In a Red-Black Tree (Self-Balancing Binary Search Tree), what property guarantees that the tree remains balanced with height O(log N)?",
        "explanation": "Every path from a node to any of its descendant null leaves contains the exact same number of black nodes (Black-Height invariant), and no two red nodes can appear consecutively, guaranteeing the longest path is at most twice the length of the shortest path.",
        "steps": "1. Every node is either Red or Black.\n2. Root is always Black.\n3. Red nodes cannot have Red children (No two consecutive Reds).\n4. Every path from root to null has identical count of Black nodes.\n5. Longest path (alternating Red-Black) <= 2 * Shortest path (all Black). Max height <= 2 * log2(N+1).",
        "example": "C++ std::map, Java TreeMap, and Linux Completely Fair Scheduler (CFS) use Red-Black Trees.",
        "mistake": "Thinking Red-Black Trees are strictly balanced like AVL trees. AVL is more strictly balanced; Red-Black allows slight height imbalance to optimize faster O(1) amortized insertion rotations.",
        "tip": "Red-Black trees require fewer rotations on insert/delete than AVL trees, making them preferred for general-purpose maps.",
        "options": [
            ("A", "No two red nodes appear in sequence and every root-to-leaf path contains the same number of black nodes", True, "Correct: Ensures maximum path length is never more than twice the minimum path length."),
            ("B", "All leaf nodes must store prime numbers", False, "Values in Red-Black trees can be any comparable data type."),
            ("C", "Every node must have exactly 3 children", False, "Red-Black tree is a binary search tree (max 2 children)."),
            ("D", "Nodes alternate between RAM and disk cache", False, "Coloring is a structural algorithmic flag.")
        ]
    },

    # ------------------ FULL STACK & JAVASCRIPT ------------------
    {
        "topic_slug": "javascript-typescript",
        "type": "technical_mcq",
        "difficulty": "intermediate",
        "text": "In React 18, what is the crucial difference between the useMemo hook and the useCallback hook?",
        "explanation": "useMemo caches the result of a calculation (memoizes a value): useMemo(() => computeValue(a, b), [a, b]). useCallback caches the function definition itself between renders: useCallback(() => handleClick(), [deps]), preventing unnecessary re-renders of memoized child components.",
        "steps": "1. useMemo: 'useMemo(fn, deps)' -> executes fn and returns its computed VALUE.\n2. useCallback: 'useCallback(fn, deps)' -> returns the memoized FUNCTION reference without calling it.\n3. useCallback(fn, deps) is syntactically equivalent to useMemo(() => fn, deps).",
        "example": "Pass useCallback to child props wrapped in React.memo to prevent child re-rendering on parent state changes.",
        "mistake": "Using useMemo for every single trivial variable calculation. The hook invocation and dependency array check has its own small overhead.",
        "tip": "useMemo is for expensive computed values; useCallback is for stable callback references passed to child components.",
        "options": [
            ("A", "useMemo memoizes the returned value of a function; useCallback memoizes the function reference itself", True, "Correct: useMemo caches computed return values; useCallback caches callback function identities."),
            ("B", "useCallback runs on server side only; useMemo runs on client browser only", False, "Both are React hooks that execute identically in client or SSR environments."),
            ("C", "useMemo modifies the database table directly", False, "React hooks are client-side rendering primitives."),
            ("D", "useCallback is deprecated in React 18", False, "useCallback is a core production React hook.")
        ]
    },
    {
        "topic_slug": "javascript-typescript",
        "type": "technical_mcq",
        "difficulty": "intermediate",
        "text": "What is the 'Event Loop' in JavaScript and in what order are the Microtask Queue and Macrotask Queue processed?",
        "explanation": "JavaScript is single-threaded. Synchronous code executes first on the Call Stack. When the stack is empty, the Event Loop empties the entire Microtask Queue (Promises, queueMicrotask, MutationObserver) before processing the next single task from the Macrotask Queue (setTimeout, setInterval, setImmediate, I/O).",
        "steps": "1. Execute synchronous script on Call Stack.\n2. Call Stack becomes empty.\n3. Process ALL pending microtasks in Microtask Queue until queue is completely empty.\n4. Render UI updates.\n5. Pick ONE macrotask from Macrotask Queue (e.g. setTimeout callback) and execute.\n6. Repeat loop.",
        "example": "Promise.resolve().then(() => console.log('Promise')) always logs BEFORE setTimeout(() => console.log('Timeout'), 0).",
        "mistake": "Thinking setTimeout(fn, 0) executes immediately. It is placed into the macrotask queue and must wait for all current microtasks to finish.",
        "tip": "Promises and async/await are Microtasks (higher priority); setTimeout and setInterval are Macrotasks.",
        "options": [
            ("A", "The Microtask Queue (Promises) is completely drained before the next task from the Macrotask Queue (setTimeout) is executed", True, "Correct: Microtasks possess strict scheduling priority over macrotasks."),
            ("B", "setTimeout callbacks always execute before resolved Promise .then() callbacks", False, "Inverted: Promises are microtasks and execute before setTimeout macrotasks."),
            ("C", "The event loop spawns 10 OS threads for every console.log() statement", False, "JavaScript runtime execution is single-threaded on the main thread."),
            ("D", "Macrotasks and Microtasks run simultaneously in parallel without any queue order", False, "Execution follows deterministic queue ordering.")
        ]
    },

    # ------------------ APTITUDE & REASONING ------------------
    {
        "topic_slug": "aptitude-numerical",
        "type": "technical_mcq",
        "difficulty": "intermediate",
        "text": "Pipe A can fill a tank in 12 hours, Pipe B can fill it in 15 hours, and Pipe C can empty the full tank in 20 hours. If all three pipes are opened simultaneously, in how many hours will the tank be full?",
        "explanation": "Let total capacity be LCM(12, 15, 20) = 60 units. Efficiency of A = +5 units/hr. Efficiency of B = +4 units/hr. Efficiency of C = -3 units/hr. Combined net efficiency = 5 + 4 - 3 = 6 units/hr. Time required = 60 / 6 = 10 hours.",
        "steps": "1. Capacity = LCM(12, 15, 20) = 60 liters.\n2. Rate A = 60/12 = +5 l/h.\n3. Rate B = 60/15 = +4 l/h.\n4. Rate C = 60/20 = -3 l/h (emptying).\n5. Net Rate = 5 + 4 - 3 = 6 l/h.\n6. Time = 60 / 6 = 10 hours.",
        "example": "Classic placement pipe and cistern problem with positive filling rates and negative drain rate.",
        "mistake": "Adding the emptying rate instead of subtracting it.",
        "tip": "Use the LCM method instead of fractions to compute pipe efficiency with simple integers.",
        "options": [
            ("A", "10 hours", True, "Correct: Net filling rate is 6 units/hour for 60 units total = 10 hours."),
            ("B", "8 hours", False, "Calculated without subtracting pipe C drainage rate."),
            ("C", "12 hours", False, "Incorrect arithmetic on combined efficiency."),
            ("D", "15 hours", False, "Pipe A alone takes 12 hours; with pipe B helping it must be faster than 12 hours.")
        ]
    },
    {
        "topic_slug": "aptitude-logical",
        "type": "technical_mcq",
        "difficulty": "intermediate",
        "text": "At what time between 4 o'clock and 5 o'clock will the minute hand and the hour hand of a clock coincide (overlap at 0 degrees)?",
        "explanation": "At 4 o'clock, the hour hand is at 120 degrees (4 * 30 deg). The minute hand gains 5.5 degrees per minute relative to the hour hand (6 deg/min - 0.5 deg/min). Time = 120 / 5.5 = 240/11 = 21 and 9/11 minutes past 4.",
        "steps": "1. Initial angle at 4:00 = 4 * 30 = 120 degrees.\n2. Relative speed of minute hand over hour hand = 6 - 0.5 = 5.5 deg/min = 11/2 deg/min.\n3. Time to cover 120 deg = 120 / (11/2) = 240/11 minutes.\n4. 240/11 = 21 integers and remainder 9/11 minutes.",
        "example": "Hands coincide at: 21 9/11 minutes past 4 o'clock.",
        "mistake": "Assuming hands coincide exactly at 4:20. At 4:20, the hour hand has already moved 10 degrees past the 4 marker.",
        "tip": "Formula for coincidence: Time M = (Initial Angle) / (11/2).",
        "options": [
            ("A", "21 9/11 minutes past 4 o'clock", True, "Correct: 120 degrees / 5.5 degrees per minute = 240/11 = 21 9/11 minutes."),
            ("B", "20 minutes past 4 o'clock exactly", False, "Hour hand advances 0.5 degrees every minute, so it is at 130 deg at 4:20."),
            ("C", "22 5/11 minutes past 4 o'clock", False, "Incorrect division of relative angle."),
            ("D", "25 minutes past 4 o'clock", False, "At 4:25 minute hand is at 150 deg, past the hour hand.")
        ]
    }
]

print(f"Adding {len(QUESTIONS)} curated placement questions to SQLite database...")

added = 0
for q in QUESTIONS:
    topic_id = get_topic_id(q["topic_slug"])
    c.execute("""
        INSERT INTO questions (
            topic_id, question_type, difficulty, question_text, explanation,
            step_by_step_reasoning, practical_example, common_mistake,
            learning_tip, is_published, created_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 1, ?)
    """, (
        topic_id, q["type"], q["difficulty"], q["text"],
        q["explanation"], q["steps"], q["example"],
        q["mistake"], q["tip"], now_iso
    ))
    q_id = c.lastrowid
    added += 1

    for opt in q["options"]:
        c.execute("""
            INSERT INTO question_options (
                question_id, option_key, option_text, is_correct, why_wrong_explanation
            ) VALUES (?, ?, ?, ?, ?)
        """, (q_id, opt[0], opt[1], 1 if opt[2] else 0, opt[3]))

conn.commit()
conn.close()

print(f"Successfully added {added} questions and {added * 4} options to the core question bank!")

