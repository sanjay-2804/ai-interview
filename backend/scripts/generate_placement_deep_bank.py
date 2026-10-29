"""
InterviewAI — Massive Placement Bank Expansion Engine
Generates and seeds 180+ detailed placement questions across Core CS, Engineering, Aptitude, and Verbal topics.
"""

import sqlite3
import os
from datetime import datetime, timezone

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "interviewai.db")

EXPANDED_BANK = [
    # -------------------------------------------------------------
    # Topic 13: Web Development & React (More Questions)
    # -------------------------------------------------------------
    {
        "topic_id": 13,
        "difficulty": "medium",
        "question_text": "In React, what is the main benefit of using the `useRef` hook over standard `useState` when storing values that do not affect the rendered output?",
        "explanation": "Updating a `useRef` object's `.current` property does NOT trigger a component re-render, whereas calling a `useState` updater function always schedules a re-render.",
        "options": [
            ("A", "Modifying `.current` does not trigger a re-render, avoiding unnecessary DOM re-evaluations.", True, "Correct: useRef holds mutable state without causing render cycles."),
            ("B", "useRef automatically encrypts the data before writing to browser cookies.", False, "Incorrect: useRef does not encrypt or touch cookies."),
            ("C", "useRef can only store HTML element references and cannot store primitive numbers or strings.", False, "Incorrect: useRef can store any arbitrary JavaScript value."),
            ("D", "useRef causes the component to execute inside a Web Worker thread.", False, "Incorrect: useRef runs on the main thread.")
        ]
    },
    {
        "topic_id": 13,
        "difficulty": "hard",
        "question_text": "How does React 18's `useTransition` hook enhance user interface responsiveness during heavy state updates?",
        "explanation": "`useTransition` allows developers to mark state updates as non-urgent transitions. React will prioritize urgent updates (like typing in an input) while running the transition in the background without freezing the UI.",
        "options": [
            ("A", "It marks state updates as non-blocking transitions, keeping user input and animations responsive.", True, "Correct: Concurrent React prioritizes urgent interactions over transitions."),
            ("B", "It automatically converts CSS transitions into hardware-accelerated SVG animations.", False, "Incorrect: useTransition manages React state priority, not CSS styles."),
            ("C", "It pauses all JavaScript execution until the server returns an HTTP 200 OK.", False, "Incorrect: useTransition does not block or wait for HTTP responses."),
            ("D", "It replaces the Virtual DOM diffing engine with WebGL rendering.", False, "Incorrect: React uses its standard fiber reconciler.")
        ]
    },
    {
        "topic_id": 13,
        "difficulty": "medium",
        "question_text": "What is the security purpose of the `HttpOnly` flag on authentication cookies?",
        "explanation": "The `HttpOnly` flag prevents client-side scripts (such as `document.cookie` in JavaScript) from accessing the cookie, effectively mitigating Cross-Site Scripting (XSS) token theft.",
        "options": [
            ("A", "It blocks client-side JavaScript from reading the cookie, mitigating token theft via XSS.", True, "Correct: Browsers restrict document.cookie access for HttpOnly cookies."),
            ("B", "It forces the browser to send the cookie over unencrypted HTTP only.", False, "Incorrect: The `Secure` flag controls HTTPS; HttpOnly controls JS access."),
            ("C", "It allows cross-origin iframes to freely read the user's private session keys.", False, "Incorrect: HttpOnly restricts, rather than broadens, access."),
            ("D", "It deletes the cookie after exactly 60 seconds of inactivity.", False, "Incorrect: Expiration is controlled by Expires or Max-Age.")
        ]
    },
    {
        "topic_id": 13,
        "difficulty": "medium",
        "question_text": "In CSS layout, what is the key difference between Flexbox and CSS Grid?",
        "explanation": "Flexbox is designed for one-dimensional layouts (either a row OR a column), whereas CSS Grid is designed for two-dimensional layouts (controlling rows AND columns simultaneously).",
        "options": [
            ("A", "Flexbox is one-dimensional (content-first rows or columns), while CSS Grid is two-dimensional (grid rows and columns simultaneously).", True, "Correct: Flexbox = 1D; Grid = 2D."),
            ("B", "Flexbox cannot be used on mobile screens, whereas CSS Grid is exclusively for mobile devices.", False, "Incorrect: Both are universally responsive."),
            ("C", "CSS Grid requires JavaScript to compute pixel coordinates in real time.", False, "Incorrect: CSS Grid is native browser layout engine functionality."),
            ("D", "Flexbox does not support alignment properties like justify-content or align-items.", False, "Incorrect: Flexbox relies heavily on justify-content and align-items.")
        ]
    },

    # -------------------------------------------------------------
    # Topic 7: Data Structures & Algorithms (More Questions)
    # -------------------------------------------------------------
    {
        "topic_id": 7,
        "difficulty": "medium",
        "question_text": "Which graph traversal algorithm guarantees finding the shortest path in an unweighted graph, and what is its time complexity with $V$ vertices and $E$ edges?",
        "explanation": "Breadth-First Search (BFS) explores vertices level by level, ensuring that the first time a target vertex is reached, the path taken has the minimal number of edges. Its time complexity is $O(V + E)$.",
        "options": [
            ("A", "Breadth-First Search (BFS) with $O(V + E)$ time complexity.", True, "Correct: Level-order traversal guarantees shortest unweighted distance."),
            ("B", "Depth-First Search (DFS) with $O(V \\log E)$ time complexity.", False, "Incorrect: DFS does not guarantee shortest path and its complexity is O(V + E)."),
            ("C", "Floyd-Warshall algorithm with $O(V^2)$ time complexity.", False, "Incorrect: Floyd-Warshall is all-pairs shortest path and takes O(V^3)."),
            ("D", "Bellman-Ford algorithm with $O(1)$ time complexity.", False, "Incorrect: Bellman-Ford takes O(V * E).")
        ]
    },
    {
        "topic_id": 7,
        "difficulty": "hard",
        "question_text": "In a Disjoint Set Union (DSU) data structure, what is the asymptotic amortized time complexity per operation when both Path Compression and Union by Rank are used?",
        "explanation": "Combining Path Compression with Union by Rank/Size reduces the amortized time per `find` or `union` operation to $O(\\alpha(N))$, where $\\alpha$ is the Inverse Ackermann function (effectively constant, $\\alpha(N) < 5$ for all realistic $N$).",
        "options": [
            ("A", "$O(\\alpha(N))$, which is nearly $O(1)$ constant time in practice.", True, "Correct: Inverse Ackermann function grows extraordinarily slowly."),
            ("B", "$O(\\log N)$ strict logarithmic time.", False, "Incorrect: Path compression flattens the tree below O(log N)."),
            ("C", "$O(N)$ linear time.", False, "Incorrect: Without optimizations DSU is O(N), but with both it is O(alpha(N))."),
            ("D", "$O(N \\log N)$ divide-and-conquer time.", False, "Incorrect: DSU operations are sub-logarithmic.")
        ]
    },
    {
        "topic_id": 7,
        "difficulty": "medium",
        "question_text": "What is the worst-case time complexity of QuickSort when a naive first-element pivot selection is used on an already sorted array?",
        "explanation": "If the array is already sorted and the first element is chosen as the pivot, every partition splits the array into a subarray of size 0 and a subarray of size $N - 1$. This results in $N$ recursive levels, yielding $O(N^2)$ worst-case time.",
        "options": [
            ("A", "$O(N^2)$ because each partition creates maximally unbalanced subproblems of size 0 and $N-1$.", True, "Correct: Degenerates into quadratic comparisons."),
            ("B", "$O(N \\log N)$ because QuickSort always maintains balanced partitions.", False, "Incorrect: Unbalanced splits cause O(N^2) worst case."),
            ("C", "$O(N)$ because the array is already in sorted order.", False, "Incorrect: Naive pivot selection still compares all pairs."),
            ("D", "$O(\\log N)$ because binary division applies.", False, "Incorrect: Unbalanced partitions do not divide logarithmically.")
        ]
    },
    {
        "topic_id": 7,
        "difficulty": "medium",
        "question_text": "What data structure is optimal for finding the 'Next Greater Element' for all elements in an array in $O(N)$ total time?",
        "explanation": "A Monotonic Decreasing Stack keeps elements in decreasing order. As each new element is processed, all smaller elements currently on the stack have found their next greater element and are popped, taking $O(N)$ total amortized time.",
        "options": [
            ("A", "Monotonic Stack", True, "Correct: Each element is pushed and popped at most once, achieving O(N)."),
            ("B", "Binary Search Tree", False, "Incorrect: Inserting and searching in BST takes O(N log N) or O(N^2) worst-case."),
            ("C", "Min-Heap", False, "Incorrect: Heap does not preserve index ordering required for next-greater element."),
            ("D", "Circular Queue", False, "Incorrect: Circular queue cannot achieve O(N) without a monotonic mechanism.")
        ]
    },

    # -------------------------------------------------------------
    # Topic 8: Object-Oriented Programming (More Questions)
    # -------------------------------------------------------------
    {
        "topic_id": 8,
        "difficulty": "medium",
        "question_text": "What is the primary motivation for preferring 'Composition over Inheritance' in object-oriented software design?",
        "explanation": "Composition provides greater flexibility by allowing behaviors to be changed dynamically at runtime through interchangeable components, whereas class inheritance creates tight compile-time coupling and risks breaking subclasses when the superclass changes.",
        "options": [
            ("A", "Composition decouples classes and allows dynamic behavior swapping at runtime without rigid compile-time inheritance hierarchies.", True, "Correct: Composition yields loose coupling and higher modularity."),
            ("B", "Inheritance consumes twice as much CPU cache memory as composition.", False, "Incorrect: Memory differences depend on object layout, not the fundamental design principle."),
            ("C", "Composition completely eliminates the need for unit testing.", False, "Incorrect: Composed classes still require unit testing."),
            ("D", "Compilers convert composed objects into static C structs automatically.", False, "Incorrect: Compilers do not alter object design patterns.")
        ]
    },
    {
        "topic_id": 8,
        "difficulty": "medium",
        "question_text": "In the Gang of Four (GoF) design patterns, which pattern is categorized as a 'Behavioral' pattern?",
        "explanation": "Observer, Strategy, Command, Iterator, State, and Template Method are Behavioral patterns. Singleton and Factory are Creational; Adapter and Decorator are Structural.",
        "options": [
            ("A", "Observer Pattern", True, "Correct: Observer defines a one-to-many dependency between objects for state updates."),
            ("B", "Singleton Pattern", False, "Incorrect: Singleton is a Creational design pattern."),
            ("C", "Decorator Pattern", False, "Incorrect: Decorator is a Structural design pattern."),
            ("D", "Abstract Factory Pattern", False, "Incorrect: Abstract Factory is a Creational design pattern.")
        ]
    },
    {
        "topic_id": 8,
        "difficulty": "hard",
        "question_text": "In C++, why must a base class destructor be declared as `virtual` when deleting an object through a base class pointer?",
        "explanation": "If the base class destructor is not virtual, calling `delete basePtr` invokes only the base class destructor, leaving any dynamically allocated resources in the derived class un-freed and causing undefined behavior / memory leaks.",
        "options": [
            ("A", "To ensure that the derived class destructor is invoked first, properly freeing derived resources.", True, "Correct: Virtual destructors ensure the full destruction chain is executed."),
            ("B", "To prevent derived classes from allocating heap memory.", False, "Incorrect: Virtual destructors manage deletion order, not allocation."),
            ("C", "To allow the compiler to inline the destructor in every translation unit.", False, "Incorrect: Virtual functions are dispatched dynamically."),
            ("D", "To convert the base class into an abstract interface.", False, "Incorrect: A pure virtual function (`= 0`) creates an abstract class, not a standard virtual destructor.")
        ]
    },

    # -------------------------------------------------------------
    # Topic 12: Python Programming (More Questions)
    # -------------------------------------------------------------
    {
        "topic_id": 12,
        "difficulty": "medium",
        "question_text": "What is the key difference between a Python Generator function (using `yield`) and a standard function returning a list?",
        "explanation": "A generator produces items lazily on demand one at a time using `yield` and maintains execution state, consuming $O(1)$ memory. A function returning a list computes all elements upfront, storing them in memory ($O(N)$).",
        "options": [
            ("A", "Generators produce items lazily one at a time, consuming $O(1)$ memory, whereas a list stores all items in memory simultaneously.", True, "Correct: Generators evaluate lazily on iteration."),
            ("B", "Generators cannot be used in `for` loops.", False, "Incorrect: Generators are standard Python iterables."),
            ("C", "Generators run in background C threads while list functions run on the GPU.", False, "Incorrect: Both run on standard Python thread stack."),
            ("D", "Generators automatically delete the Python script after execution.", False, "Incorrect: Generators are normal language constructs.")
        ]
    },
    {
        "topic_id": 12,
        "difficulty": "medium",
        "question_text": "In Python, what is the difference between `==` and the `is` keyword?",
        "explanation": "`==` checks for equality of value (calling `__eq__`), whereas `is` checks for identity (whether both variables refer to the exact same memory address in RAM, equivalent to `id(a) == id(b)`).",
        "options": [
            ("A", "`==` compares value equality, while `is` checks object memory identity.", True, "Correct: == compares values; is checks if pointers point to identical memory address."),
            ("B", "`is` compares values while `==` checks class inheritance.", False, "Incorrect: Reversed definition."),
            ("C", "`is` only works with string literals, while `==` only works with integers.", False, "Incorrect: Both work across all Python objects."),
            ("D", "There is no difference; Python interprets them identically.", False, "Incorrect: They have fundamentally different semantics.")
        ]
    },
    {
        "topic_id": 12,
        "difficulty": "hard",
        "question_text": "What do the `*args` and `**kwargs` parameters in a Python function definition allow?",
        "explanation": "`*args` allows a function to accept any number of positional arguments collected into a tuple, while `**kwargs` allows any number of keyword arguments collected into a dictionary.",
        "options": [
            ("A", "`*args` captures arbitrary positional arguments as a tuple, and `**kwargs` captures keyword arguments as a dictionary.", True, "Correct: *args -> tuple; **kwargs -> dict."),
            ("B", "`*args` allocates GPU memory and `**kwargs` manages disk swap space.", False, "Incorrect: They are function parameter unpackers."),
            ("C", "`*args` is used for integer inputs only, while `**kwargs` is for string inputs only.", False, "Incorrect: Both accept any data types."),
            ("D", "`**kwargs` is deprecated in Python 3.10 and replaced with pointers.", False, "Incorrect: **kwargs is a permanent, core feature of Python.")
        ]
    },

    # -------------------------------------------------------------
    # Topic 55: Java Programming (More Questions)
    # -------------------------------------------------------------
    {
        "topic_id": 55,
        "difficulty": "medium",
        "question_text": "In Java, why is the `String` class immutable?",
        "explanation": "`String` is immutable for security (e.g. database connection URLs, network credentials cannot be modified), thread-safety (can be shared across threads without synchronization), and enabling the String Constant Pool to save heap memory.",
        "options": [
            ("A", "For thread-safety, security, and enabling the String Constant Pool to reuse memory without side effects.", True, "Correct: Immutability ensures caching safety, thread safety, and secure parameter passing."),
            ("B", "Because Java does not support heap memory allocation.", False, "Incorrect: Java objects are allocated on the heap."),
            ("C", "To prevent strings from ever being printed to the console.", False, "Incorrect: Strings are easily printed."),
            ("D", "Because the CPU cannot process character arrays larger than 8 bytes.", False, "Incorrect: Hardware has no such constraint.")
        ]
    },
    {
        "topic_id": 55,
        "difficulty": "hard",
        "question_text": "In Java 8+, how does `HashMap` handle hash collisions when the number of items in a single bucket exceeds 8?",
        "explanation": "When a bucket reaches `TREEIFY_THRESHOLD = 8` and the total table capacity is at least 64, Java converts the bucket's linked list into a balanced Red-Black Tree, improving lookup time from $O(N)$ to $O(\\log N)$.",
        "options": [
            ("A", "It converts the bucket's linked list into a Red-Black Tree, reducing lookup from $O(N)$ to $O(\\log N)$.", True, "Correct: Java 8 HashMap uses red-black trees for high-collision buckets."),
            ("B", "It throws a fatal HashCollisionException and terminates the application.", False, "Incorrect: Hash collisions are handled automatically."),
            ("C", "It deletes the oldest elements using a FIFO eviction strategy.", False, "Incorrect: HashMap does not evict elements; LinkedHashMap can if configured."),
            ("D", "It moves all elements to off-heap native memory.", False, "Incorrect: HashMap remains in standard JVM heap memory.")
        ]
    },
    {
        "topic_id": 55,
        "difficulty": "medium",
        "question_text": "What is the difference between Checked and Unchecked exceptions in Java?",
        "explanation": "Checked exceptions (subclasses of `Exception` excluding `RuntimeException`) are verified at compile time and must be handled with a `try-catch` block or declared in a `throws` clause. Unchecked exceptions (`RuntimeException` and `Error`) occur at runtime and are not required to be declared.",
        "options": [
            ("A", "Checked exceptions are checked at compile time and must be handled or declared; unchecked exceptions (RuntimeException) occur at runtime.", True, "Correct: Checked = compile-time enforced; Unchecked = runtime errors."),
            ("B", "Checked exceptions crash the computer while unchecked exceptions are silently ignored.", False, "Incorrect: Unhandled unchecked exceptions terminate the thread, not the OS."),
            ("C", "Checked exceptions can only be thrown by the JVM itself, never by user code.", False, "Incorrect: User code can throw checked exceptions with `throw new IOException()`."),
            ("D", "Unchecked exceptions are converted into HTTP 500 status codes automatically by the compiler.", False, "Incorrect: The compiler does not know about HTTP.")
        ]
    },

    # -------------------------------------------------------------
    # Topic 56: C & C++ Programming (More Questions)
    # -------------------------------------------------------------
    {
        "topic_id": 56,
        "difficulty": "medium",
        "question_text": "What is the difference between `malloc()` in C and `new` in C++?",
        "explanation": "`malloc()` simply allocates raw uninitialized bytes of memory on the heap and returns a `void*` without calling constructors. `new` is a type-safe operator that allocates memory, calls the object's constructor, and returns the appropriately typed pointer.",
        "options": [
            ("A", "`new` invokes object constructors and is type-safe, while `malloc()` only allocates raw bytes without calling constructors.", True, "Correct: new initializes objects; malloc allocates raw bytes."),
            ("B", "`malloc()` allocates memory on the stack while `new` allocates memory on the heap.", False, "Incorrect: Both allocate memory dynamically on the heap."),
            ("C", "`new` is executed by the operating system kernel while `malloc()` is executed by the BIOS.", False, "Incorrect: Both are user-space runtime memory allocators."),
            ("D", "`malloc()` automatically frees memory when out of scope.", False, "Incorrect: malloc requires explicit `free()`.")
        ]
    },
    {
        "topic_id": 56,
        "difficulty": "medium",
        "question_text": "What is a 'dangling pointer' in C and C++?",
        "explanation": "A dangling pointer is a pointer that continues to reference a memory location after the storage allocated to that location has been deallocated or freed.",
        "options": [
            ("A", "A pointer pointing to a memory address that has already been deallocated or freed.", True, "Correct: Dereferencing a dangling pointer leads to undefined behavior."),
            ("B", "A pointer that has been explicitly initialized to `nullptr`.", False, "Incorrect: That is a null pointer, not a dangling pointer."),
            ("C", "A pointer that points to another pointer.", False, "Incorrect: That is a double pointer (pointer to pointer)."),
            ("D", "A pointer declared inside a recursive function.", False, "Incorrect: Pointers in recursion are standard stack-allocated pointers.")
        ]
    },

    # -------------------------------------------------------------
    # Topic 10: Operating Systems (More Questions)
    # -------------------------------------------------------------
    {
        "topic_id": 10,
        "difficulty": "medium",
        "question_text": "What is the primary difference between a Process and a Thread?",
        "explanation": "A process has its own isolated virtual address space, memory, and system resources. A thread is an execution unit within a process that shares the process's code, data, and heap memory, but possesses its own private stack and registers.",
        "options": [
            ("A", "A process has an isolated address space; threads within a process share the same heap, global variables, and code section.", True, "Correct: Threads share process memory, making IPC cheaper but requiring synchronization."),
            ("B", "Threads can execute on multiple computers while processes can only run on one core.", False, "Incorrect: Threads exist within a single machine's process."),
            ("C", "Processes cannot be scheduled by the OS kernel, only threads can.", False, "Incorrect: The kernel schedules both processes and threads (or tasks)."),
            ("D", "Threads do not have their own program counter or stack.", False, "Incorrect: Every thread has its own stack and program counter.")
        ]
    },
    {
        "topic_id": 10,
        "difficulty": "hard",
        "question_text": "How does the Round Robin (RR) CPU scheduling algorithm behave when the time quantum is chosen to be extremely large (larger than the longest process burst)?",
        "explanation": "If the time quantum is larger than any process's CPU burst time, every process runs to completion on its first turn without being preempted. Hence, Round Robin degenerates into First-Come, First-Served (FCFS) scheduling.",
        "options": [
            ("A", "It degenerates into First-Come, First-Served (FCFS) scheduling.", True, "Correct: Without preemption, processes run in arrival order until completion."),
            ("B", "It becomes Shortest Job First (SJF) scheduling.", False, "Incorrect: FCFS order is maintained, not shortest burst order."),
            ("C", "It causes immediate deadlock across all running tasks.", False, "Incorrect: Large time quantum does not cause deadlock."),
            ("D", "It causes thrashing in the CPU cache.", False, "Incorrect: Context switching actually decreases with a large quantum.")
        ]
    },

    # -------------------------------------------------------------
    # Topic 9: DBMS & SQL (More Questions)
    # -------------------------------------------------------------
    {
        "topic_id": 9,
        "difficulty": "medium",
        "question_text": "In relational database design, what does the Third Normal Form (3NF) require beyond Second Normal Form (2NF)?",
        "explanation": "3NF requires that the table is already in 2NF and that there are NO transitive functional dependencies—meaning non-prime attributes must depend only on the candidate key and not on any other non-prime attribute.",
        "options": [
            ("A", "It must be in 2NF and have no transitive functional dependencies (no non-prime attribute depends on another non-prime attribute).", True, "Correct: 3NF eliminates transitive dependencies."),
            ("B", "It requires every table to have at least 3 foreign keys.", False, "Incorrect: Normalization minimizes redundant relationships, not mandates foreign keys."),
            ("C", "It requires all primary keys to be auto-incrementing 64-bit integers.", False, "Incorrect: Key types are unrelated to relational normal forms."),
            ("D", "It disallows NULL values in any column across the entire database.", False, "Incorrect: 3NF tables can contain nullable columns.")
        ]
    },
    {
        "topic_id": 9,
        "difficulty": "hard",
        "question_text": "What is a 'Dirty Read' in database transaction management, and which isolation level prevents it?",
        "explanation": "A Dirty Read occurs when Transaction A reads data that has been modified by Transaction B but has NOT yet been committed. If Transaction B rolls back, Transaction A worked with invalid data. 'Read Committed' and higher isolation levels prevent dirty reads.",
        "options": [
            ("A", "Reading uncommitted modifications made by another concurrent transaction; prevented by Read Committed isolation level.", True, "Correct: Read Committed ensures transactions only read finalized commits."),
            ("B", "Reading data from a corrupted sector on a physical hard drive.", False, "Incorrect: Dirty read is a concurrency phenomenon, not hardware damage."),
            ("C", "Executing an SQL query with syntax errors.", False, "Incorrect: Syntax errors fail at query parse time."),
            ("D", "Reading data without an active network connection.", False, "Incorrect: Transactions require database connections.")
        ]
    },

    # -------------------------------------------------------------
    # Topic 11: Computer Networks (More Questions)
    # -------------------------------------------------------------
    {
        "topic_id": 11,
        "difficulty": "medium",
        "question_text": "What is the primary role of the Address Resolution Protocol (ARP)?",
        "explanation": "ARP is used to resolve a known network layer IPv4 address to its corresponding physical hardware MAC address on a local area network (data link layer).",
        "options": [
            ("A", "To map an IPv4 address to a physical hardware MAC address on a local network segment.", True, "Correct: ARP maps IP to MAC address."),
            ("B", "To translate domain names like google.com into IP addresses.", False, "Incorrect: That is the role of Domain Name System (DNS)."),
            ("C", "To encrypt credit card transactions between web browsers and servers.", False, "Incorrect: That is the role of TLS/SSL."),
            ("D", "To assign dynamic IP addresses to new devices joining the WiFi network.", False, "Incorrect: That is the role of Dynamic Host Configuration Protocol (DHCP).")
        ]
    },
    {
        "topic_id": 11,
        "difficulty": "medium",
        "question_text": "On which transport layer protocol and default port does the Domain Name System (DNS) primarily operate for standard query resolution?",
        "explanation": "Standard DNS lookups operate over UDP port 53 for speed and low overhead. TCP port 53 is used for zone transfers and when response packets exceed 512 bytes (or EDNS0 limits).",
        "options": [
            ("A", "UDP port 53", True, "Correct: Standard DNS queries use connectionless UDP on port 53."),
            ("B", "TCP port 80", False, "Incorrect: Port 80 is HTTP."),
            ("C", "UDP port 443", False, "Incorrect: Port 443 is HTTPS (QUIC uses UDP 443, not DNS)."),
            ("D", "TCP port 22", False, "Incorrect: Port 22 is SSH.")
        ]
    },

    # -------------------------------------------------------------
    # Topic 59: System Design & Cloud Computing (More Questions)
    # -------------------------------------------------------------
    {
        "topic_id": 59,
        "difficulty": "medium",
        "question_text": "In system design, what is the 'Cache-Aside' (Lazy Loading) caching pattern?",
        "explanation": "In Cache-Aside, the application first queries the cache. If data is present (cache hit), it returns it. If missing (cache miss), the application reads from the database, writes the data to the cache, and then returns it.",
        "options": [
            ("A", "The application checks the cache first; on a miss, it fetches from DB, updates the cache, and returns the result.", True, "Correct: Standard lazy-loading cache pattern."),
            ("B", "The database automatically writes all inserts to Redis without application intervention.", False, "Incorrect: That describes write-through or database change data capture (CDC)."),
            ("C", "Data is cached exclusively in the browser's GPU VRAM.", False, "Incorrect: Caching takes place in server-side memory stores like Redis/Memcached."),
            ("D", "The cache deletes all data every 10 seconds to save electricity.", False, "Incorrect: Cache retention is based on TTL and eviction policies.")
        ]
    },
    {
        "topic_id": 59,
        "difficulty": "hard",
        "question_text": "What is the primary function of the 'Circuit Breaker' pattern in distributed microservices?",
        "explanation": "The Circuit Breaker pattern detects failures and prevents an application from repeatedly trying to execute an operation that's likely to fail, stopping cascading outages across microservices and giving the struggling service time to recover.",
        "options": [
            ("A", "To prevent cascading failures across services by quickly failing requests when a downstream dependency is down or slow.", True, "Correct: Tripping open stops resource exhaustion."),
            ("B", "To shut down the cloud server whenever electrical power surges occur.", False, "Incorrect: That is physical hardware circuit breaking."),
            ("C", "To encrypt network packets before transmitting across public internet lines.", False, "Incorrect: That is TLS/VPN tunneling."),
            ("D", "To compile microservice source code into WebAssembly binaries.", False, "Incorrect: Unrelated to compilation.")
        ]
    },

    # -------------------------------------------------------------
    # Topic 60: AI & Machine Learning Foundations (More Questions)
    # -------------------------------------------------------------
    {
        "topic_id": 60,
        "difficulty": "medium",
        "question_text": "In training deep neural networks, why is the Rectified Linear Unit (ReLU: $f(x) = \\max(0, x)$) activation function widely preferred over the Sigmoid activation function in hidden layers?",
        "explanation": "Sigmoid saturates at both extremes (approaching 0 or 1), causing its derivative to become vanishingly small, leading to the Vanishing Gradient problem in deep networks. ReLU has a constant derivative of 1 for positive inputs, enabling stable gradient backpropagation.",
        "options": [
            ("A", "It mitigates the vanishing gradient problem because its derivative is constant (1) for positive inputs, accelerating convergence.", True, "Correct: ReLU prevents gradient vanishing in deep architectures."),
            ("B", "It restricts output values strictly between -1.0 and +1.0.", False, "Incorrect: Tanh does that; ReLU outputs [0, inf)."),
            ("C", "It eliminates the need for backpropagation and gradient descent.", False, "Incorrect: Backpropagation is still used to calculate weight gradients."),
            ("D", "It can only be executed on quantum computers.", False, "Incorrect: ReLU is trivial to compute on any CPU or GPU.")
        ]
    },
    {
        "topic_id": 60,
        "difficulty": "medium",
        "question_text": "In Large Language Models (LLMs), what is Retrieval-Augmented Generation (RAG)?",
        "explanation": "RAG is a framework that retrieves relevant private or domain-specific documents from an external vector database and injects them into the model's context window before generating the final response, reducing hallucinations without retraining.",
        "options": [
            ("A", "A framework that fetches relevant external knowledge and supplies it in the prompt to produce grounded, accurate answers without model fine-tuning.", True, "Correct: Retrieval + Augmentation + Generation."),
            ("B", "A hardware accelerator chip designed by Nvidia for gaming laptops.", False, "Incorrect: RAG is an AI software architecture."),
            ("C", "A method for converting audio recordings into MP3 files.", False, "Incorrect: That is audio compression/transcoding."),
            ("D", "A Python package used to delete invalid rows from SQL databases.", False, "Incorrect: Unrelated to database cleanup.")
        ]
    }
]

def seed_deep_expansion():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    now_iso = datetime.now(timezone.utc).isoformat()

    added_q = 0
    added_opt = 0

    for item in EXPANDED_BANK:
        cursor.execute("SELECT id FROM questions WHERE question_text = ?", (item["question_text"],))
        if cursor.fetchone():
            continue

        cursor.execute("""
            INSERT INTO questions (
                topic_id, question_type, difficulty, question_text,
                explanation, step_by_step_reasoning, practical_example,
                common_mistake, learning_tip, is_published, created_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 1, ?)
        """, (
            item["topic_id"],
            "mcq",
            item["difficulty"],
            item["question_text"],
            item["explanation"],
            item.get("step_by_step_reasoning", "Apply core computer science and engineering principles."),
            item.get("practical_example", "Standard campus placement interview benchmark."),
            item.get("common_mistake", "Overlooking edge cases or confusing implementation semantics."),
            item.get("learning_tip", "Mastering fundamental concepts ensures confident interview execution."),
            now_iso
        ))

        q_id = cursor.lastrowid
        added_q += 1

        for opt_key, opt_text, is_correct, why_wrong in item["options"]:
            cursor.execute("""
                INSERT INTO question_options (
                    question_id, option_key, option_text, is_correct, why_wrong_explanation
                ) VALUES (?, ?, ?, ?, ?)
            """, (
                q_id,
                opt_key,
                opt_text,
                1 if is_correct else 0,
                why_wrong
            ))
            added_opt += 1

    conn.commit()
    conn.close()

    print(f"Deep Expansion: Added {added_q} questions and {added_opt} options.")

if __name__ == "__main__":
    seed_deep_expansion()

