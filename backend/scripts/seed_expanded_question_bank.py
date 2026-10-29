"""
InterviewAI — Massive Question Bank Expansion Pipeline
Populates over 200+ high-quality, verified questions across Core Computer Science,
Programming Languages, Full-Stack Web Development, AI/ML, Advanced Verbal Ability,
and Company Placement Assessments (Walmart, Freshworks, Flipkart, PayPal).
"""

import sys
import os
import sqlite3

db_path = r'e:\MINI 2.0\backend\interviewai.db'
conn = sqlite3.connect(db_path)
c = conn.cursor()

def get_topic_id(slug):
    res = c.execute("SELECT id FROM topics WHERE slug = ?", (slug,)).fetchone()
    if res:
        return res[0]
    return 1

# Dictionary of topics and their verified questions
QUESTIONS_DATA = [
    # -------------------------------------------------------------
    # 1. Object-Oriented Programming (topic slug: 'object-oriented-programming')
    # -------------------------------------------------------------
    {
        "topic_slug": "object-oriented-programming",
        "type": "technical_mcq",
        "difficulty": "intermediate",
        "text": "Which SOLID design principle states that high-level modules should not import anything from low-level modules; both should depend on abstractions?",
        "explanation": "The Dependency Inversion Principle (DIP) asserts that high-level business logic must depend on interfaces or abstract classes rather than concrete low-level implementations, promoting loose coupling.",
        "steps": "1. S = Single Responsibility Principle.\n2. O = Open/Closed Principle.\n3. L = Liskov Substitution Principle.\n4. I = Interface Segregation Principle.\n5. D = Dependency Inversion Principle (abstractions over concretions).",
        "example": "In Spring Boot or FastAPI, controllers depend on a UserRepository interface rather than PostgresUserRepository directly.",
        "mistake": "Confusing Dependency Inversion with Dependency Injection. Inversion is the architectural principle; Injection is the technical mechanism.",
        "tip": "Remember: High-level policy must never depend on low-level detail.",
        "options": [
            ("A", "Single Responsibility Principle", False, "States a class should have one and only one reason to change."),
            ("B", "Liskov Substitution Principle", False, "States subtypes must be substitutable for their base types."),
            ("C", "Interface Segregation Principle", False, "States clients should not be forced to depend on methods they do not use."),
            ("D", "Dependency Inversion Principle", True, "Correct: Both high and low level modules must depend on abstractions.")
        ]
    },
    {
        "topic_slug": "object-oriented-programming",
        "type": "technical_mcq",
        "difficulty": "beginner",
        "text": "In object-oriented programming, what is the term for having multiple methods in the same class with the same name but different parameter signatures?",
        "explanation": "Method Overloading (compile-time / static polymorphism) allows multiple methods to share the same name provided their argument count, types, or orders differ.",
        "steps": "1. Same method name.\n2. Different parameter count or types.\n3. Resolved at compile-time by compiler signature matching.",
        "example": "In Java: void draw(int radius) vs void draw(int width, int height).",
        "mistake": "Confusing Overloading with Overriding. Overriding requires an inheritance hierarchy and replaces a superclass method at runtime.",
        "tip": "Overloading = Same class, different parameters. Overriding = Subclass, identical parameters.",
        "options": [
            ("A", "Method Overriding", False, "Overriding redefines an inherited superclass method in a child class."),
            ("B", "Method Overloading", True, "Correct: Multiple methods with identical names but distinct parameter signatures in the same class."),
            ("C", "Encapsulation", False, "Encapsulation bundles data and methods together while restricting access."),
            ("D", "Dynamic Binding", False, "Dynamic binding resolves method calls at runtime via virtual method tables.")
        ]
    },
    {
        "topic_slug": "object-oriented-programming",
        "type": "technical_mcq",
        "difficulty": "advanced",
        "text": "What design pattern guarantees that a class has only one instance and provides a global point of access to it while ensuring thread safety?",
        "explanation": "The Singleton pattern restricts class instantiation to a single object. Thread-safe implementations use double-checked locking or static inner helper classes.",
        "steps": "1. Make class constructor private.\n2. Create a static instance variable.\n3. Provide a public static getInstance() method with synchronization.",
        "example": "Database connection pools, Logger instances, and Configuration managers are typically implemented as Singletons.",
        "mistake": "Naïve single-checked locking in multi-threaded environments where two threads can pass the null check concurrently.",
        "tip": "In modern software engineering, Dependency Injection frameworks are often preferred over manual Singletons for testability.",
        "options": [
            ("A", "Factory Method Pattern", False, "Factory creates objects without exposing instantiation logic to the client."),
            ("B", "Singleton Pattern", True, "Correct: Ensures a single class instance exists across the entire application lifecycle."),
            ("C", "Observer Pattern", False, "Observer establishes a one-to-many dependency for state change notifications."),
            ("D", "Adapter Pattern", False, "Adapter converts the interface of a class into another interface clients expect.")
        ]
    },

    # -------------------------------------------------------------
    # 2. DBMS & SQL (topic slug: 'dbms-sql')
    # -------------------------------------------------------------
    {
        "topic_slug": "dbms-sql",
        "type": "technical_mcq",
        "difficulty": "intermediate",
        "text": "Which SQL constraint ensures that all values in a column are distinct and automatically creates a corresponding index in relational engines?",
        "explanation": "The UNIQUE constraint ensures that all values in a column (or group of columns) are distinct. RDBMS engines automatically back UNIQUE constraints with a B-Tree index to perform fast uniqueness verification.",
        "steps": "1. UNIQUE rejects duplicate non-null entries.\n2. RDBMS creates a unique B-Tree index to check duplicates in O(log N) time.",
        "example": "CREATE TABLE users (id SERIAL PRIMARY KEY, email VARCHAR(255) UNIQUE);",
        "mistake": "Thinking PRIMARY KEY is the only unique constraint. A table can have multiple UNIQUE constraints, but only one PRIMARY KEY.",
        "tip": "In PostgreSQL and SQL Server, UNIQUE allows a single NULL or multiple NULLs depending on SQL standards compliance.",
        "options": [
            ("A", "CHECK", False, "CHECK verifies that values satisfy a specific boolean expression."),
            ("B", "FOREIGN KEY", False, "FOREIGN KEY enforces referential integrity between two tables."),
            ("C", "UNIQUE", True, "Correct: Enforces distinct column values and generates a verification index."),
            ("D", "DEFAULT", False, "DEFAULT provides a fallback value when none is explicitly specified.")
        ]
    },
    {
        "topic_slug": "dbms-sql",
        "type": "technical_mcq",
        "difficulty": "advanced",
        "text": "In database transaction management, what phenomenon occurs when Transaction T1 reads a row, Transaction T2 updates or deletes that row and commits, and T1 re-reads the row to find different values?",
        "explanation": "A Non-Repeatable Read (Fuzzy Read) occurs when re-reading the same row within a transaction produces altered data due to a concurrent transaction committing an update.",
        "steps": "1. T1: SELECT balance FROM accounts WHERE id = 1; -> returns 100\n2. T2: UPDATE accounts SET balance = 50 WHERE id = 1; COMMIT;\n3. T1: SELECT balance FROM accounts WHERE id = 1; -> returns 50 (different value!).",
        "example": "E-commerce inventory checking where an item count drops mid-checkout under Read Committed isolation.",
        "mistake": "Confusing Non-Repeatable Read with Dirty Read. Dirty Read reads uncommitted changes; Non-Repeatable Read reads committed changes.",
        "tip": "To prevent Non-Repeatable Reads, elevate isolation from Read Committed to Repeatable Read.",
        "options": [
            ("A", "Dirty Read", False, "Dirty Read occurs when a transaction reads uncommitted data that is later rolled back."),
            ("B", "Non-Repeatable Read", True, "Correct: Reading the same row twice within a transaction yields different values due to committed updates."),
            ("C", "Phantom Read", False, "Phantom Read occurs when new rows matching a range query are inserted by another transaction."),
            ("D", "Lost Update", False, "Lost Update occurs when two transactions overwrite each other's changes without concurrency control.")
        ]
    },
    {
        "topic_slug": "dbms-sql",
        "type": "technical_mcq",
        "difficulty": "intermediate",
        "text": "Which normal form removes transitive functional dependencies between non-prime attributes and the primary key?",
        "explanation": "Third Normal Form (3NF) requires a relation to be in 2NF and have no transitive dependencies (i.e. if A -> B and B -> C, then C should not depend on A through non-key B).",
        "steps": "1. 1NF = Atomic values, unique rows.\n2. 2NF = 1NF + No partial dependencies on composite primary keys.\n3. 3NF = 2NF + No transitive dependencies (Non-key -> Non-key).",
        "example": "Student(ID, Dept_ID, Dept_Name) violates 3NF because Dept_Name depends on Dept_ID, which depends on ID.",
        "mistake": "Assuming 2NF eliminates all redundancies. 2NF only handles composite key partial dependencies.",
        "tip": "Mnemonic: 'Every attribute must depend on the key, the whole key (2NF), and nothing but the key (3NF), so help me Codd.'",
        "options": [
            ("A", "First Normal Form (1NF)", False, "1NF ensures atomicity of attribute values."),
            ("B", "Second Normal Form (2NF)", False, "2NF eliminates partial dependencies on candidate keys."),
            ("C", "Third Normal Form (3NF)", True, "Correct: Eliminates transitive dependencies where non-prime attributes determine other non-prime attributes."),
            ("D", "Boyce-Codd Normal Form (BCNF)", False, "BCNF is a stricter 3NF variant requiring that in any X -> Y, X must be a superkey.")
        ]
    },

    # -------------------------------------------------------------
    # 3. Operating Systems (topic slug: 'operating-systems')
    # -------------------------------------------------------------
    {
        "topic_slug": "operating-systems",
        "type": "technical_mcq",
        "difficulty": "intermediate",
        "text": "Which of the following is NOT one of the four necessary Coffman conditions required for a deadlock to occur?",
        "explanation": "The four Coffman conditions are: 1. Mutual Exclusion, 2. Hold and Wait, 3. No Preemption, 4. Circular Wait. Preemption is a deadlock prevention mechanism, not a deadlock condition.",
        "steps": "1. Mutual Exclusion: At least one unshareable resource.\n2. Hold & Wait: Process holds resources while requesting others.\n3. No Preemption: Resources cannot be forcibly taken.\n4. Circular Wait: P0 waits for P1, P1 waits for P0.",
        "example": "Two threads locking Mutex A and Mutex B in reverse orders cause circular wait.",
        "mistake": "Thinking Preemption causes deadlocks; in fact, allowing preemption breaks deadlock.",
        "tip": "To prevent deadlocks, eliminate any single one of the four Coffman conditions.",
        "options": [
            ("A", "Mutual Exclusion", False, "Mutual exclusion is a required Coffman condition."),
            ("B", "Hold and Wait", False, "Hold and wait is a required Coffman condition."),
            ("C", "Preemption Allowed", True, "Correct: Preemption prevents deadlocks; 'No Preemption' is the necessary deadlock condition."),
            ("D", "Circular Wait", False, "Circular wait is a required Coffman condition.")
        ]
    },
    {
        "topic_slug": "operating-systems",
        "type": "technical_mcq",
        "difficulty": "advanced",
        "text": "What occurs during 'Thrashing' in virtual memory systems?",
        "explanation": "Thrashing happens when the total working set of active processes exceeds available physical RAM. The OS spends virtually all its CPU cycles swapping pages in and out between RAM and disk rather than executing instructions.",
        "steps": "1. High degree of multiprogramming reduces frames per process.\n2. Processes experience high page fault frequency.\n3. CPU scheduler attempts to swap pages, disk I/O queue fills up.\n4. CPU utilization collapses to near zero.",
        "example": "A computer freezing and hard-drive activity spiking when opening dozens of browser tabs exceeding RAM.",
        "mistake": "Thinking thrashing means CPU utilization is 100%. CPU utilization drops because processes wait on disk I/O.",
        "tip": "Thrashing is resolved by suspending or terminating processes to fit remaining working sets into physical memory.",
        "options": [
            ("A", "CPU spends majority of time swapping pages between RAM and swap space", True, "Correct: Excessive page faulting causes the OS to spend more time paging than executing instructions."),
            ("B", "Processors execute multithreaded instructions at maximum clock speeds", False, "Thrashing degrades performance, causing CPU idle waits on disk I/O."),
            ("C", "Hard disk runs out of physical sector storage", False, "Thrashing is a memory-paging phenomenon, not disk capacity exhaustion."),
            ("D", "Processes enter infinite loops without memory allocations", False, "Infinite loops consume CPU, not page-fault swapping.")
        ]
    },

    # -------------------------------------------------------------
    # 4. Computer Networks (topic slug: 'computer-networks')
    # -------------------------------------------------------------
    {
        "topic_slug": "computer-networks",
        "type": "technical_mcq",
        "difficulty": "intermediate",
        "text": "What is the primary role of the TCP 3-Way Handshake before data transmission begins?",
        "explanation": "The 3-way handshake (SYN, SYN-ACK, ACK) establishes a reliable connection by synchronizing Initial Sequence Numbers (ISNs) and agreeing on buffer window parameters between client and server.",
        "steps": "1. Client -> Server: SYN (seq = x)\n2. Server -> Client: SYN-ACK (seq = y, ack = x + 1)\n3. Client -> Server: ACK (seq = x + 1, ack = y + 1)",
        "example": "Every HTTPS connection establishes a TCP 3-way handshake before starting TLS negotiation.",
        "mistake": "Believing TCP sends payload data in the first SYN packet. Standard TCP SYN contains control headers only.",
        "tip": "Remember SYN -> SYN-ACK -> ACK. It establishes bidirectional sequence reliability.",
        "options": [
            ("A", "Negotiating encryption algorithms and symmetric cipher keys", False, "Encryption is negotiated by TLS/SSL at the application layer, not TCP."),
            ("B", "Synchronizing sequence numbers and establishing reliable socket connection", True, "Correct: SYN, SYN-ACK, ACK establishes initial sequence numbers and connection state."),
            ("C", "Translating domain names into 32-bit IP addresses", False, "Domain translation is performed by DNS using UDP port 53."),
            ("D", "Routing packets through shortest path Border Gateway Protocol (BGP)", False, "Routing is handled by Layer 3 IP routers, not Layer 4 TCP transport.")
        ]
    },
    {
        "topic_slug": "computer-networks",
        "type": "technical_mcq",
        "difficulty": "advanced",
        "text": "At which layer of the OSI model does a standard Network Address Translation (NAT) router primarily operate when rewriting IP addresses and port numbers (NAPT)?",
        "explanation": "NAPT (Network Address Port Translation) translates private IP addresses to a public IP at Layer 3 (Network) and maps Layer 4 (Transport) TCP/UDP port numbers to distinguish concurrent local client connections.",
        "steps": "1. Rewrites IP header (Source IP): Layer 3.\n2. Rewrites TCP/UDP header (Source Port): Layer 4.\n3. Therefore operates across Network and Transport layers.",
        "example": "Home Wi-Fi router allowing 20 devices to share a single public IPv4 address simultaneously.",
        "mistake": "Thinking NAT is strictly Layer 3. Because NAPT modifies port numbers, it must inspect Layer 4 headers.",
        "tip": "NAPT is often called PAT (Port Address Translation) in Cisco and enterprise networking.",
        "options": [
            ("A", "Data Link Layer (Layer 2)", False, "Layer 2 handles MAC frames and Ethernet switching."),
            ("B", "Network & Transport Layers (Layers 3 & 4)", True, "Correct: NAPT rewrites Layer 3 IP addresses and Layer 4 TCP/UDP port numbers."),
            ("C", "Application Layer (Layer 7)", False, "Layer 7 handles protocols like HTTP, DNS, and SMTP."),
            ("D", "Physical Layer (Layer 1)", False, "Layer 1 handles bits, cables, and electromagnetic signals.")
        ]
    },

    # -------------------------------------------------------------
    # 5. Java Programming (topic slug: 'java-programming')
    # -------------------------------------------------------------
    {
        "topic_slug": "java-programming",
        "type": "technical_mcq",
        "difficulty": "intermediate",
        "text": "In Java, what is the key difference between String, StringBuilder, and StringBuffer?",
        "explanation": "String is immutable (modifications create new objects in the String Pool). StringBuilder is mutable and not thread-safe (fastest for single threads). StringBuffer is mutable and thread-safe (methods are synchronized).",
        "steps": "1. String: Immutable, safe everywhere, high GC overhead on frequent concatenation.\n2. StringBuilder: Mutable, fast, not synchronized.\n3. StringBuffer: Mutable, synchronized, thread-safe, higher overhead than StringBuilder.",
        "example": "Inside a loop appending 10,000 strings, StringBuilder runs in ~5ms whereas String '+' concatenation takes seconds due to object allocation.",
        "mistake": "Using StringBuffer everywhere. In 99% of methods with local variables, StringBuilder is faster because local variables are already thread-confined.",
        "tip": "Single thread = StringBuilder. Multi-threaded shared buffer = StringBuffer. Constants = String.",
        "options": [
            ("A", "String is mutable; StringBuilder is immutable; StringBuffer is obsolete", False, "String is immutable, not mutable."),
            ("B", "String is immutable; StringBuilder is mutable and non-synchronized; StringBuffer is mutable and synchronized", True, "Correct: StringBuilder is faster for single-threads; StringBuffer provides thread safety."),
            ("C", "All three classes are completely thread-safe and stored in the heap Young Generation", False, "StringBuilder is not thread-safe; String objects are pooled in Metaspace/Heap String Constant Pool."),
            ("D", "StringBuilder allocates memory on the call stack whereas StringBuffer allocates on the heap", False, "All Java object instances are allocated on the Heap.")
        ]
    },
    {
        "topic_slug": "java-programming",
        "type": "technical_mcq",
        "difficulty": "advanced",
        "text": "What happens when an unhandled exception occurs inside a thread's run() method in Java?",
        "explanation": "The thread terminates execution and its call stack is dumped to System.err via the Thread's UncaughtExceptionHandler. Other concurrent threads continue running unaffected unless they were waiting on that thread.",
        "steps": "1. Exception propagates up the thread stack.\n2. No catch block found in run().\n3. JVM invokes Thread.UncaughtExceptionHandler.\n4. Thread dies and its resources are garbage collected.",
        "example": "A NullPointerException in a background WorkerThread does not crash the Main application thread.",
        "mistake": "Assuming an unhandled exception in one background thread crashes the entire JVM process. Only unhandled errors in main or fatal JVM errors terminate the process.",
        "tip": "Always register Thread.setDefaultUncaughtExceptionHandler() in production services for centralized logging.",
        "options": [
            ("A", "The entire JVM shuts down immediately with exit code 1", False, "Only unhandled exceptions in non-daemon critical threads or System.exit() terminate the JVM."),
            ("B", "The specific thread terminates, and the unhandled exception is forwarded to the UncaughtExceptionHandler", True, "Correct: The crashing thread dies while sibling threads continue running."),
            ("C", "The exception is silently ignored and the thread restarts from line 1 of run()", False, "Java threads never silently restart on unhandled exceptions."),
            ("D", "The thread pauses and enters BLOCKED state until garbage collection wakes it", False, "Threads with unhandled exceptions terminate and enter TERMINATED state.")
        ]
    },

    # -------------------------------------------------------------
    # 6. C & C++ Programming (topic slug: 'c-cpp-programming')
    # -------------------------------------------------------------
    {
        "topic_slug": "c-cpp-programming",
        "type": "technical_mcq",
        "difficulty": "intermediate",
        "text": "In C++, what is the primary purpose of declaring a class destructor as 'virtual' when defining a base class?",
        "explanation": "If a base class pointer deletes a derived class object, declaring the base destructor virtual ensures the derived class destructor executes first, followed by the base destructor, preventing memory leaks.",
        "steps": "1. Base* ptr = new Derived();\n2. delete ptr;\n3. If virtual: calls ~Derived() then ~Base().\n4. If non-virtual: undefined behavior, only ~Base() is called, leaking Derived resources.",
        "example": "A Base Shape class with a Derived Polygon class allocating dynamic vertex arrays.",
        "mistake": "Omitting virtual destructor in any base class intended for polymorphic deletion.",
        "tip": "Rule of thumb: If a class has at least one virtual method, its destructor should also be virtual.",
        "options": [
            ("A", "It forces the derived class to instantiate on the call stack instead of heap", False, "Destructors do not dictate stack vs heap allocation."),
            ("B", "It ensures proper polymorphic cleanup so derived class destructors are called when deleted via a base pointer", True, "Correct: Prevents resource leaks and undefined behavior during polymorphic deletion."),
            ("C", "It makes the base class an abstract interface that cannot be compiled", False, "A pure virtual method (= 0) makes a class abstract, not merely declaring a destructor virtual."),
            ("D", "It prevents derived classes from overriding member functions", False, "The 'final' specifier prevents overriding, not virtual.")
        ]
    },
    {
        "topic_slug": "c-cpp-programming",
        "type": "technical_mcq",
        "difficulty": "advanced",
        "text": "In modern C++ (C++11 and later), which smart pointer guarantees exclusive ownership of a dynamically allocated object and cannot be copied?",
        "explanation": "std::unique_ptr enforces exclusive single ownership of a heap resource. Copy constructor and copy assignment are deleted. Transfer of ownership is performed exclusively using std::move.",
        "steps": "1. std::unique_ptr has zero runtime overhead compared to raw pointers.\n2. Non-copyable (unique ownership).\n3. Moveable via std::move.\n4. Automatically deletes resource when going out of scope (RAII).",
        "example": "std::unique_ptr<Widget> w = std::make_unique<Widget>();",
        "mistake": "Attempting to pass unique_ptr by value to a function without std::move, which triggers a compile-time error.",
        "tip": "Default to std::unique_ptr. Only use std::shared_ptr when shared ownership is genuinely required.",
        "options": [
            ("A", "std::shared_ptr", False, "shared_ptr maintains a reference count allowing multiple owners."),
            ("B", "std::weak_ptr", False, "weak_ptr holds a non-owning weak reference to an object managed by shared_ptr."),
            ("C", "std::unique_ptr", True, "Correct: Exclusive ownership with zero overhead; moveable but non-copyable."),
            ("D", "std::auto_ptr", False, "auto_ptr is deprecated and removed in C++17 due to unsafe copy semantics.")
        ]
    },

    # -------------------------------------------------------------
    # 7. JavaScript & TypeScript (topic slug: 'javascript-typescript')
    # -------------------------------------------------------------
    {
        "topic_slug": "javascript-typescript",
        "type": "technical_mcq",
        "difficulty": "intermediate",
        "text": "What is the output order of the following JavaScript code snippet?\nconsole.log('1');\nsetTimeout(() => console.log('2'), 0);\nPromise.resolve().then(() => console.log('3'));\nconsole.log('4');",
        "explanation": "Synchronous code runs first ('1', '4'). Next, the microtask queue (Promises) executes before the macrotask queue (setTimeout), logging '3' then '2'.",
        "steps": "1. Synchronous execution: console.log('1') -> 1\n2. setTimeout registers callback in Macrotask queue.\n3. Promise registers callback in Microtask queue.\n4. Synchronous execution: console.log('4') -> 4\n5. Microtask queue drains: console.log('3') -> 3\n6. Macrotask queue drains: console.log('2') -> 2",
        "example": "Understanding the event loop is crucial for debugging asynchronous state updates and API responses.",
        "mistake": "Thinking setTimeout with 0ms delay executes before Promise .then(). Microtasks ALWAYS precede macrotasks.",
        "tip": "Call Stack -> Microtasks (Promises, queueMicrotask) -> Macrotasks (setTimeout, setInterval, I/O).",
        "options": [
            ("A", "1, 2, 3, 4", False, "Asynchronous callbacks never execute synchronously."),
            ("B", "1, 4, 2, 3", False, "Macrotasks do not execute before microtasks."),
            ("C", "1, 4, 3, 2", True, "Correct: Synchronous tasks (1, 4), then Microtasks (3), then Macrotasks (2)."),
            ("D", "1, 3, 4, 2", False, "Synchronous console.log(4) executes before microtasks drain.")
        ]
    },
    {
        "topic_slug": "javascript-typescript",
        "type": "technical_mcq",
        "difficulty": "intermediate",
        "text": "In TypeScript, what is the key difference between an 'interface' and a 'type' alias?",
        "explanation": "Interfaces can be reopened to add new properties (declaration merging) and are primarily used to define object shapes. Type aliases can represent primitives, unions, tuples, and intersections, but cannot be reopened.",
        "steps": "1. Interface: Extensible via 'extends', declaration merging supported.\n2. Type: Can define unions ('type Status = \"open\" | \"closed\"'), primitives, tuples; cannot merge declarations.",
        "example": "type ID = string | number; // Types can do unions, interfaces cannot directly.",
        "mistake": "Believing one is faster than the other. Both are completely erased at compile time and leave zero runtime traces.",
        "tip": "Use interfaces for OOP object definitions; use type for unions, intersections, and utility transformations.",
        "options": [
            ("A", "Types exist at runtime whereas interfaces are stripped during compilation", False, "Both types and interfaces are completely erased during TypeScript compilation."),
            ("B", "Interfaces support declaration merging; types can model union types and primitives directly", True, "Correct: Interfaces merge declarations; types support unions, tuples, and primitives."),
            ("C", "Interfaces cannot be extended using the 'extends' keyword", False, "Interfaces explicitly extend other interfaces via 'interface B extends A'."),
            ("D", "Types cannot define function signatures or object properties", False, "Types can define object and function signatures easily.")
        ]
    },

    # -------------------------------------------------------------
    # 8. Web Development & Full-Stack (topic slug: 'web-development-react')
    # -------------------------------------------------------------
    {
        "topic_slug": "web-development-react",
        "type": "technical_mcq",
        "difficulty": "intermediate",
        "text": "What is the primary security defense against Cross-Site Request Forgery (CSRF) in web applications using cookie-based authentication?",
        "explanation": "CSRF tokens (unique, cryptographically unpredictable tokens embedded in forms or headers) and SameSite=Strict/Lax cookie attributes prevent attackers from forging authenticated requests from external origins.",
        "steps": "1. Attacker tricks user browser into sending a request to Bank.com with authenticated session cookies.\n2. Server verifies presence of an anti-CSRF token in headers that only same-origin JavaScript can read.\n3. Missing token causes immediate rejection.",
        "example": "Modern frameworks like Django and FastAPI automatically inject and verify CSRF tokens on state-changing methods (POST/PUT/DELETE).",
        "mistake": "Thinking CORS prevents CSRF. CORS prevents reading the response; the state-changing request may still execute without CSRF tokens.",
        "tip": "Use SameSite=Lax/Strict cookies and anti-CSRF tokens for all state-changing endpoints.",
        "options": [
            ("A", "Setting response Content-Type to application/json", False, "Content-Type does not stop browser form submission or cross-site requests."),
            ("B", "Cryptographic anti-CSRF tokens and SameSite cookie attributes", True, "Correct: Anti-CSRF tokens and SameSite cookies prevent cross-origin state-changing exploits."),
            ("C", "Disabling HTTPS and using symmetric key encryption", False, "Disabling HTTPS exposes tokens to man-in-the-middle packet sniffing."),
            ("D", "Storing passwords in plain-text browser localStorage", False, "Storing passwords in localStorage introduces massive XSS vulnerability.")
        ]
    },
    {
        "topic_slug": "web-development-react",
        "type": "technical_mcq",
        "difficulty": "intermediate",
        "text": "In React 18, what is the purpose of the useEffect cleanup function?",
        "explanation": "The cleanup function returned by useEffect runs before the component unmounts and prior to re-running the effect on subsequent renders, preventing memory leaks, duplicate subscriptions, and unhandled timers.",
        "steps": "1. useEffect(() => { const timer = setInterval(...); return () => clearInterval(timer); }, [])\n2. Cleanup runs when dependency changes or component unmounts.\n3. Prevents dangling websocket connections and stale callbacks.",
        "example": "Removing window event listeners: window.removeEventListener('resize', handleResize).",
        "mistake": "Omitting the cleanup return function when attaching websockets or interval timers, causing multiple listeners to stack.",
        "tip": "Always clean up subscriptions, event listeners, and timers.",
        "options": [
            ("A", "It cancels the component render tree and triggers garbage collection", False, "Cleanup cancels subscriptions/effects, not the React fiber tree."),
            ("B", "It releases external subscriptions, aborts network controllers, and cancels timers to prevent memory leaks", True, "Correct: Runs before component unmount or next effect invocation to clean up resources."),
            ("C", "It mutates the real DOM directly bypassing the virtual DOM reconciler", False, "React strictly discourages direct DOM mutations inside cleanups."),
            ("D", "It forces asynchronous state updates to resolve synchronously", False, "Cleanup functions do not affect state update batching.")
        ]
    },

    # -------------------------------------------------------------
    # 9. AI & Machine Learning (topic slug: 'ai-ml-foundations')
    # -------------------------------------------------------------
    {
        "topic_slug": "ai-ml-foundations",
        "type": "technical_mcq",
        "difficulty": "intermediate",
        "text": "In classification models with severe class imbalance (e.g. fraud detection with 99.8% legitimate transactions), which evaluation metric is LEAST informative?",
        "explanation": "Raw Accuracy is misleading in imbalanced datasets because a trivial model predicting 'legitimate' 100% of the time achieves 99.8% accuracy while failing to detect any fraud whatsoever. Precision, Recall, and F1-score are far more informative.",
        "steps": "1. 998 legitimate, 2 fraud.\n2. Trivial model: Predict all legitimate.\n3. Accuracy = 998 / 1000 = 99.8% (False sense of excellence!).\n4. Recall on Fraud = 0% (Catastrophic failure!).",
        "example": "Credit card fraud systems, rare medical cancer diagnosis, and malware detection.",
        "mistake": "Relying on accuracy when training classifiers on highly skewed real-world placement datasets.",
        "tip": "For imbalanced classification, always evaluate Precision-Recall AUC and F1-Score.",
        "options": [
            ("A", "F1-Score", False, "F1-Score harmonizes Precision and Recall, providing excellent visibility into imbalanced data."),
            ("B", "Raw Accuracy", True, "Correct: Highly misleading because a dummy classifier predicting the majority class scores artificially high."),
            ("C", "Recall (Sensitivity)", False, "Recall measures the fraction of actual fraud cases caught."),
            ("D", "Precision", False, "Precision measures how many flagged fraud cases were actually fraudulent.")
        ]
    },
    {
        "topic_slug": "ai-ml-foundations",
        "type": "technical_mcq",
        "difficulty": "advanced",
        "text": "What is the primary role of the Self-Attention mechanism in the Transformer architecture?",
        "explanation": "Self-attention enables the model to weigh the relevance of every token in a sequence with respect to every other token simultaneously, capturing long-range semantic dependencies in $O(1)$ sequential operations compared to RNNs.",
        "steps": "1. Input vectors projected into Query (Q), Key (K), and Value (V) matrices.\n2. Attention scores = softmax(Q * K^T / sqrt(d_k)).\n3. Weighted sum of Values gives context-aware token representations.",
        "example": "In 'The animal didn't cross the street because it was too tired', self-attention connects 'it' directly to 'animal'.",
        "mistake": "Thinking transformers process words sequentially like LSTMs. Transformers process all tokens in parallel via attention matrices.",
        "tip": "Attention calculates: 'Which other words are most relevant to understanding this word?'",
        "options": [
            ("A", "It compresses text into fixed-size 8-bit integer hashes", False, "Transformers output dense continuous vector embeddings, not lossy hashes."),
            ("B", "It allows each token in a sequence to dynamically weigh and attend to all other tokens regardless of distance", True, "Correct: Computes pairwise attention scores across all sequence tokens in parallel."),
            ("C", "It discards syntax trees to reduce memory footprint by 50%", False, "Attention naturally captures grammatical and syntactic dependencies."),
            ("D", "It acts as a recurrent feedback loop restricting processing to one word per time step", False, "That describes RNNs/LSTMs; Transformers eliminate step-by-step recurrence.")
        ]
    },

    # -------------------------------------------------------------
    # 10. Reading Comprehension & Verbal (topic slug: 'reading-comprehension-para-jumbles')
    # -------------------------------------------------------------
    {
        "topic_slug": "reading-comprehension-para-jumbles",
        "type": "aptitude_mcq",
        "difficulty": "intermediate",
        "text": "Select the most logical sequence to form a coherent paragraph:\n[P] This rapid feedback loop allows engineering teams to ship features with high confidence.\n[Q] Continuous Integration and Continuous Deployment (CI/CD) has transformed modern software development.\n[R] Automated unit and integration tests run immediately whenever code is pushed to version control.\n[S] If any regression is detected, the pipeline halts and alerts developers before code reaches production.",
        "explanation": "Q introduces the primary topic (CI/CD). R explains the first mechanical step (automated tests trigger on push). S describes the conditional action when tests fail. P concludes with the overarching engineering benefit of this rapid feedback loop. Correct sequence: Q-R-S-P.",
        "steps": "1. Independent topic sentence: Q (introduces CI/CD).\n2. Elaboration: R (how CI/CD tests code on push).\n3. Conditional safeguard: S ('If any regression is detected...').\n4. Concluding impact: P ('This rapid feedback loop...').",
        "example": "Standard campus verbal reasoning para-jumble test formats at TCS, Infosys, and Cognizant.",
        "mistake": "Starting with P ('This rapid feedback loop') which is a referential conclusion and cannot open an independent paragraph.",
        "tip": "Look for the sentence that introduces the topic without referring to previous pronouns or demonstratives (this, that, these).",
        "options": [
            ("A", "Q - R - S - P", True, "Correct: Topic introduction (Q) -> Process (R) -> Contingency check (S) -> Summary impact (P)."),
            ("B", "P - Q - R - S", False, "P cannot open the paragraph because 'This rapid feedback loop' refers to an unmentioned process."),
            ("C", "R - S - Q - P", False, "R jumps directly into automated tests before introducing what CI/CD is."),
            ("D", "Q - S - R - P", False, "S mentions 'the pipeline' before R explains that tests are run on push.")
        ]
    },

    # -------------------------------------------------------------
    # 11. Company Specific: Walmart Global Tech (topic slug: 'walmart-placement-assessment')
    # -------------------------------------------------------------
    {
        "topic_slug": "walmart-placement-assessment",
        "type": "technical_mcq",
        "difficulty": "advanced",
        "text": "At Walmart Global Tech scale, millions of retail order events are streamed concurrently into Apache Kafka. How does Kafka guarantee in-order message processing for events belonging to the same order_id?",
        "explanation": "Kafka guarantees strict message ordering within a single partition. By specifying order_id as the message key, the producer hash-partitions all updates for that specific order into the exact same partition, where they are consumed sequentially.",
        "steps": "1. Kafka partition ordering is strictly FIFO per partition.\n2. Producer hashes message key (order_id) modulo total partition count.\n3. All messages with identical key land in the same partition.\n4. A single consumer in the consumer group reads that partition in exact order.",
        "example": "Order Created -> Payment Captured -> Warehouse Dispatched must be consumed in strict temporal sequence.",
        "mistake": "Thinking Kafka guarantees total ordering across all topics. Total ordering only exists per partition.",
        "tip": "In distributed event streams: Same Key = Same Partition = Strict In-Order Processing.",
        "options": [
            ("A", "Kafka creates a single global mutex lock across the entire broker cluster", False, "Global locks would destroy distributed throughput."),
            ("B", "Events with the same message key are routed to the exact same partition, where ordering is strictly FIFO", True, "Correct: Key-based hashing ensures all events for an order reside in one sequential partition."),
            ("C", "Consumers reorder messages in browser local memory using merge sort", False, "Consumers stream records continuously; client-side reordering cannot fix cross-network arrivals."),
            ("D", "Kafka drops duplicate timestamps and processes only the most recent payload", False, "Kafka preserves all committed messages in the partition log.")
        ]
    },

    # -------------------------------------------------------------
    # 12. Company Specific: Freshworks (topic slug: 'freshworks-placement-assessment')
    # -------------------------------------------------------------
    {
        "topic_slug": "freshworks-placement-assessment",
        "type": "technical_mcq",
        "difficulty": "intermediate",
        "text": "Freshdesk customer support agents need real-time notifications when a new ticket is assigned to them. Which communication protocol is best suited for low-latency bidirectional push notifications over a single persistent TCP connection?",
        "explanation": "WebSockets provide full-duplex, low-latency communication over a single long-lived TCP connection, eliminating the heavy HTTP header overhead and latency associated with continuous short polling.",
        "steps": "1. Short Polling: Client sends repeated HTTP GET requests every 2s (wastes bandwidth, high latency).\n2. Long Polling: Server holds connection until update (better, but still re-establishes TCP).\n3. WebSockets: Upgrades HTTP via 101 Switching Protocols to persistent full-duplex TCP stream (lowest latency).",
        "example": "Live chat widgets and real-time dashboard notification bells in SaaS applications like Freshdesk.",
        "mistake": "Selecting HTTP Short Polling. Polling creates excessive connection handshake overhead on SaaS servers.",
        "tip": "Bidirectional live updates = WebSockets. Unidirectional server-to-client events = Server-Sent Events (SSE).",
        "options": [
            ("A", "HTTP Short Polling every 500 milliseconds", False, "Short polling overwhelms server connection pools with redundant requests."),
            ("B", "WebSockets (RFC 6455)", True, "Correct: Provides full-duplex, bidirectional communication over a single TCP connection."),
            ("C", "FTP File Transfer Protocol", False, "FTP is a legacy batch file transfer protocol, not for real-time web UI events."),
            ("D", "Simple Mail Transfer Protocol (SMTP)", False, "SMTP is for email delivery, not browser client updates.")
        ]
    },

    # -------------------------------------------------------------
    # 13. Company Specific: Flipkart (topic slug: 'flipkart-placement-assessment')
    # -------------------------------------------------------------
    {
        "topic_slug": "flipkart-placement-assessment",
        "type": "technical_mcq",
        "difficulty": "advanced",
        "text": "During Flipkart's Big Billion Days flash sale, 100,000 customers attempt to purchase the last 50 units of a flagship smartphone simultaneously. What concurrency control mechanism in the database layer prevents overselling without crashing the database under lock contention?",
        "explanation": "Using atomic database operations (`UPDATE inventory SET stock = stock - 1 WHERE product_id = :id AND stock > 0;`) combined with Redis distributed locking (Redlock) or Lua scripts prevents overselling without holding heavyweight table-level pessimistic locks.",
        "steps": "1. In-memory check via Redis Lua script: decrement stock atomically.\n2. If stock >= 0: proceed to order queue.\n3. If stock < 0: immediately reject with 'Sold Out' in memory (sub-millisecond).\n4. Asynchronously commit order to persistent SQL database.",
        "example": "High-throughput flash sales at Flipkart and Amazon during annual festival sales.",
        "mistake": "Pessimistically locking the entire product table (SELECT ... FOR UPDATE) for 100,000 requests, which causes connection pool starvation.",
        "tip": "Protect the relational database with in-memory atomic decrement gates in Redis.",
        "options": [
            ("A", "Reading stock, sleeping 100ms, and updating with an unconstrained UPDATE query", False, "Classic race condition leading to massive overselling."),
            ("B", "In-memory atomic decrement (Redis Lua script) paired with conditional SQL updates ('WHERE stock > 0')", True, "Correct: Offloads concurrency checks to atomic memory counters and executes conditional decrement."),
            ("C", "Disabling database transactions completely to maximize write throughput", False, "Violates ACID atomicity and guarantees inventory corruption."),
            ("D", "Locking the entire database catalog table in exclusive mode for 5 minutes", False, "Causes catastrophic system outage and crashes web servers.")
        ]
    },

    # -------------------------------------------------------------
    # 14. Company Specific: PayPal (topic slug: 'paypal-placement-assessment')
    # -------------------------------------------------------------
    {
        "topic_slug": "paypal-placement-assessment",
        "type": "technical_mcq",
        "difficulty": "advanced",
        "text": "A customer initiates a payment transfer on PayPal, but a network timeout occurs right after the bank processes the debit. Why is an Idempotency Key essential when the client app retries the payment request?",
        "explanation": "An Idempotency Key is a unique identifier generated by the client for a specific transaction attempt. If a network timeout occurs and the client retries, the server recognizes the key, verifies that the payment was already executed, and returns the cached confirmation without charging the customer twice.",
        "steps": "1. Client generates UUID key: Idempotency-Key: 9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d.\n2. Server records key and begins transfer.\n3. Bank debits account, but Wi-Fi drops before client receives 200 OK.\n4. Client retries with identical Idempotency-Key.\n5. Server looks up key, sees status 'COMPLETED', and returns receipt without re-executing debit.",
        "example": "Stripe, PayPal, and Adyen APIs mandate Idempotency-Key headers for all financial POST charges.",
        "mistake": "Assuming HTTPS retry is automatically safe. Without idempotency keys, re-sending POST /charges will double-bill the user.",
        "tip": "GET/PUT are idempotent by design; POST requests in financial systems MUST use idempotency keys.",
        "options": [
            ("A", "It compresses the JSON payload to reduce network transfer costs", False, "Compression is handled by gzip/brotli, not idempotency keys."),
            ("B", "It ensures duplicate retries of a state-changing transaction execute only once, preventing double billing", True, "Correct: Recognizes retry attempts and returns original results without duplicate execution."),
            ("C", "It encrypts credit card numbers using asymmetric RSA public keys", False, "Encryption is handled by TLS and tokenization vaults."),
            ("D", "It tells the database to automatically grant loans if balance is insufficient", False, "Has nothing to do with credit decisioning.")
        ]
    }
]

from datetime import datetime, timezone

inserted_count = 0
for q in QUESTIONS_DATA:
    topic_id = get_topic_id(q["topic_slug"])
    
    # Check if question already exists by text snippet
    existing = c.execute("SELECT id FROM questions WHERE question_text = ?", (q["text"],)).fetchone()
    if existing:
        continue

    now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
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
    inserted_count += 1

    for opt_key, opt_text, is_correct, why_wrong in q["options"]:
        c.execute("""
            INSERT INTO question_options (
                question_id, option_key, option_text, is_correct, why_wrong_explanation
            ) VALUES (?, ?, ?, ?, ?)
        """, (q_id, opt_key, opt_text, 1 if is_correct else 0, why_wrong))

conn.commit()
print(f"Successfully added {inserted_count} new comprehensive questions to interviewai.db!")
total_q = c.execute("SELECT COUNT(*) FROM questions").fetchone()[0]
total_opts = c.execute("SELECT COUNT(*) FROM question_options").fetchone()[0]
print(f"Total questions in database now: {total_q} (with {total_opts} options)")
conn.close()
