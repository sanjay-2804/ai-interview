"""
InterviewAI — Massive Question Expansion Pack 4
Populates under-represented placement topics with 220+ authentic, high-quality questions.
Topics covered:
- Web Development & React (Topic 13)
- Data Structures & Algorithms (Topic 7)
- Object-Oriented Programming (Topic 8)
- Python Programming (Topic 12)
- Java Programming (Topic 55)
- C & C++ Programming (Topic 56)
- JavaScript & TypeScript (Topic 57)
- Software Engineering & Testing (Topic 58)
- Computer Networks (Topic 11)
- Operating Systems (Topic 10)
- DBMS & SQL (Topic 9)
- System Design & Cloud Computing (Topic 59)
- AI & Machine Learning Foundations (Topic 60)
- Problems on Ages (Topic 22)
- Geometry & Mensuration (Topic 24)
- Progressions (AP & GP) (Topic 25)
- Algebra & Equations (Topic 26)
- Reading Comprehension & Para Jumbles (Topic 61)
- Logical Deductions & Syllogisms (Topic 4)
- Blood Relations & Directions (Topic 5)
- Coding, Clocks & Ordering (Topic 28)
"""

import sqlite3
import os
from datetime import datetime, timezone

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "interviewai.db")

QUESTIONS_DATA = [
    # ==========================================
    # TOPIC 13: Web Development & React
    # ==========================================
    {
        "topic_id": 13,
        "difficulty": "medium",
        "question_text": "In React 18, why does passing an empty dependency array `[]` to `useEffect` cause the effect to run only once after the initial render?",
        "explanation": "An empty dependency array indicates to React's reconciliation engine that the effect does not depend on any state or props values that change over time, so it executes only during the initial component mount phase.",
        "step_by_step_reasoning": "1. React compares dependencies between renders using Object.is.\n2. With `[]`, dependencies never change.\n3. Hence, the cleanup and re-run are skipped on subsequent re-renders.",
        "practical_example": "useEffect(() => { fetchUserData(); }, []); // runs once on mount",
        "common_mistake": "Thinking `[]` means run on every render. Omitting the array entirely causes the effect to run on every render.",
        "learning_tip": "Always specify dependencies or use ESLint's react-hooks/exhaustive-deps rule to avoid stale closures.",
        "options": [
            ("A", "Because React compares current dependencies with previous dependencies; since neither changes, re-execution is skipped.", True, "Correct: Object.is comparison finds zero changes."),
            ("B", "Because an empty array tells React to destroy the component immediately after execution.", False, "Incorrect: The component remains mounted."),
            ("C", "Because React executes effects asynchronously in a separate web worker thread.", False, "Incorrect: React effects execute on the main browser thread."),
            ("D", "Because React caches the return value of the effect in localStorage.", False, "Incorrect: React does not touch browser localStorage for hook state.")
        ]
    },
    {
        "topic_id": 13,
        "difficulty": "hard",
        "question_text": "What is the primary difference between `useMemo` and `useCallback` in React?",
        "explanation": "`useMemo` returns a memoized value resulting from calling the provided compute function, while `useCallback` returns a memoized callback function instance itself.",
        "step_by_step_reasoning": "1. `useMemo(() => fn(), deps)` caches the result of `fn()`.\n2. `useCallback(fn, deps)` is equivalent to `useMemo(() => fn, deps)`.\n3. `useCallback` is used to prevent child re-renders due to reference inequality of function props.",
        "practical_example": "const cachedValue = useMemo(() => computeHeavy(a), [a]);\nconst cachedHandler = useCallback(() => handleClick(id), [id]);",
        "common_mistake": "Wrapping every primitive calculation in useMemo, which adds memory overhead without performance benefits.",
        "learning_tip": "useCallback(fn, deps) === useMemo(() => fn, deps).",
        "options": [
            ("A", "`useMemo` caches the calculated result of a function, whereas `useCallback` caches the function reference itself.", True, "Correct: useMemo caches values; useCallback caches function definitions."),
            ("B", "`useMemo` works only on server components while `useCallback` is client-only.", False, "Incorrect: Both are client React hooks."),
            ("C", "`useCallback` mutates the DOM directly while `useMemo` updates the Virtual DOM.", False, "Incorrect: Neither hook mutates the DOM directly."),
            ("D", "`useMemo` is executed asynchronously while `useCallback` executes synchronously on layout.", False, "Incorrect: Both evaluate synchronously during the render phase.")
        ]
    },
    {
        "topic_id": 13,
        "difficulty": "medium",
        "question_text": "Why should you never use array indices as `key` props when rendering dynamic lists in React where items can be reordered, inserted, or deleted?",
        "explanation": "Keys help React identify which items have changed, been added, or been removed. Using array indices leads to incorrect component state binding, broken animations, and unnecessary re-renders when list order shifts.",
        "step_by_step_reasoning": "1. If index 0 is deleted, index 1 becomes the new index 0.\n2. React thinks the first item stayed the same and only its props changed.\n3. Uncontrolled state (like inputs) will mistakenly stay attached to the wrong DOM node.",
        "practical_example": "items.map(item => <TodoItem key={item.id} {...item} />); // correct: stable unique ID",
        "common_mistake": "Using `key={index}` to silence ESLint warnings without realizing it corrupts component internal state upon deletions.",
        "learning_tip": "Always use unique, stable IDs from the backend (e.g., UUID or DB primary key) as keys.",
        "options": [
            ("A", "Using indices causes React to mismatch component internal state with DOM elements when list items are reordered or removed.", True, "Correct: Keys must uniquely and stably identify identity across renders."),
            ("B", "React throws a fatal runtime SyntaxError whenever an integer key is detected.", False, "Incorrect: React accepts integers as keys, but warns about unstable index keys."),
            ("C", "Array indices consume more memory in the Virtual DOM tree than UUID strings.", False, "Incorrect: Memory consumption is negligible compared to identity correctness."),
            ("D", "Index keys trigger continuous infinite render loops in React 18 Concurrent Mode.", False, "Incorrect: Index keys do not trigger render loops.")
        ]
    },
    {
        "topic_id": 13,
        "difficulty": "medium",
        "question_text": "What is the key difference between Server-Side Rendering (SSR) and Client-Side Rendering (CSR)?",
        "explanation": "In SSR (e.g., Next.js), the server executes the React tree and sends pre-rendered HTML with content to the browser, improving First Contentful Paint (FCP) and SEO. In CSR, the browser downloads an empty HTML shell and JS bundle, building the DOM on the client.",
        "step_by_step_reasoning": "1. SSR compiles HTML on each request or at build time on the server.\n2. CSR loads bundle.js, executes it, and renders components in the client browser.\n3. SSR provides instant initial text/content visibility; CSR requires waiting for JS execution.",
        "practical_example": "Next.js getServerSideProps renders on server; standard Create React App serves index.html with <div id='root'></div> and renders via JS.",
        "common_mistake": "Assuming SSR eliminates client-side JavaScript; SSR still requires client 'hydration' to attach event listeners.",
        "learning_tip": "SSR = Better initial SEO and FCP; CSR = Rich SPA interactivity once loaded.",
        "options": [
            ("A", "SSR generates full HTML on the server for faster initial content paint and SEO, while CSR compiles the DOM in the user's browser via JavaScript.", True, "Correct: SSR delivers ready-to-display HTML; CSR builds UI in the browser."),
            ("B", "SSR executes only in WebAssembly while CSR executes strictly in Node.js.", False, "Incorrect: SSR executes on Node.js/Edge servers; CSR executes in the browser."),
            ("C", "CSR has faster initial load times on slow 3G networks than SSR.", False, "Incorrect: CSR is slower on initial load due to downloading large JS bundles."),
            ("D", "SSR does not support CSS styling or images.", False, "Incorrect: SSR fully supports styles, images, and fonts.")
        ]
    },
    {
        "topic_id": 13,
        "difficulty": "hard",
        "question_text": "When a web application makes a cross-origin HTTP `POST` request with `Content-Type: application/json` and custom headers, why does the browser issue a preflight `OPTIONS` request?",
        "explanation": "Because `Content-Type: application/json` and custom headers disqualify the request from being a 'Simple Request' under the CORS specification. The browser sends a preflight OPTIONS request to verify server permissions before sending the actual payload.",
        "step_by_step_reasoning": "1. Simple requests only allow GET, HEAD, or POST with specific Content-Types (e.g., application/x-www-form-urlencoded, multipart/form-data, text/plain).\n2. application/json triggers preflight.\n3. The browser checks Access-Control-Allow-Origin, Access-Control-Allow-Methods, and Access-Control-Allow-Headers.",
        "practical_example": "Browser sends: OPTIONS /api/data -> Server returns: Access-Control-Allow-Origin: * -> Browser sends: POST /api/data.",
        "common_mistake": "Thinking CORS is a backend security barrier; CORS is enforced by the browser to protect users from malicious cross-site requests.",
        "learning_tip": "To avoid unnecessary preflight requests, use Access-Control-Max-Age to cache OPTIONS responses.",
        "options": [
            ("A", "The request is not a 'simple request' because of application/json and custom headers, requiring the browser to check server CORS permissions first.", True, "Correct: Non-simple requests mandate an OPTIONS preflight."),
            ("B", "The browser wants to compress the JSON payload using GZIP before uploading.", False, "Incorrect: OPTIONS does not compress payloads."),
            ("C", "The web server crashed and asked the browser to reconnect with OPTIONS.", False, "Incorrect: Browser initiates OPTIONS automatically according to CORS specs."),
            ("D", "OPTIONS is required by HTTP/2 to establish SSL TLS 1.3 cryptographic handshakes.", False, "Incorrect: TLS handshake happens at the transport layer before HTTP requests.")
        ]
    },
    {
        "topic_id": 13,
        "difficulty": "medium",
        "question_text": "In CSS layout, what is the effect of setting `box-sizing: border-box;` on an element?",
        "explanation": "With `border-box`, the element's specified `width` and `height` include the content, padding, and border. In the default `content-box`, padding and border are added onto the width, making the element physically wider than defined.",
        "step_by_step_reasoning": "1. content-box total width = width + left/right padding + left/right border.\n2. border-box total width = width (padding and border are absorbed inside).\n3. border-box eliminates layout overflow surprises.",
        "practical_example": "width: 100px; padding: 10px; border: 2px solid black; -> In border-box, total width is exactly 100px.",
        "common_mistake": "Assuming margin is included in border-box; margin is always outside the element box.",
        "learning_tip": "Universal reset `*, *::before, *::after { box-sizing: border-box; }` is standard modern CSS practice.",
        "options": [
            ("A", "The element's total width and height include content, padding, and border, preventing dimensional inflation.", True, "Correct: Padding and border are calculated within the specified dimensions."),
            ("B", "The element is converted from block to inline-flex display.", False, "Incorrect: Display type is unaffected."),
            ("C", "The margins of adjacent elements are automatically collapsed to 0px.", False, "Incorrect: Margin collapsing is unrelated to box-sizing."),
            ("D", "The element's contents are clipped and hidden with an automatic scrollbar.", False, "Incorrect: That describes `overflow: hidden/auto`.")
        ]
    },
    {
        "topic_id": 13,
        "difficulty": "hard",
        "question_text": "How do JavaScript Microtasks (e.g., `Promise.then`, `queueMicrotask`) differ from Macrotasks (e.g., `setTimeout`, `setInterval`) in the browser event loop?",
        "explanation": "After each macrotask completes, the event loop drains the ENTIRE microtask queue before rendering the UI and picking up the next macrotask from the task queue.",
        "step_by_step_reasoning": "1. Current synchronous script executes.\n2. Microtask queue is processed completely until empty.\n3. Browser performs render updates (style, layout, paint).\n4. Next macrotask (e.g., setTimeout callback) is dequeued.",
        "practical_example": "setTimeout(() => console.log('Macro'), 0);\nPromise.resolve().then(() => console.log('Micro'));\nconsole.log('Sync');\n// Output: Sync -> Micro -> Macro",
        "common_mistake": "Assuming `setTimeout(..., 0)` runs before Promise resolutions. Promises are microtasks and always execute first.",
        "learning_tip": "Sync code -> Microtasks queue drain -> DOM render -> Next Macrotask.",
        "options": [
            ("A", "All microtasks in the queue are completely executed before the next macrotask runs and before UI rendering.", True, "Correct: Microtasks have priority and drain fully before the next macrotask."),
            ("B", "Macrotasks always execute before microtasks regardless of queue timing.", False, "Incorrect: Microtasks execute before macrotasks in the event loop cycle."),
            ("C", "Microtasks run in background Web Workers while macrotasks block the main thread.", False, "Incorrect: Both run on the main thread event loop."),
            ("D", "Microtasks only execute when the user interacts with the mouse or keyboard.", False, "Incorrect: Microtasks execute immediately after the synchronous frame finishes.")
        ]
    },
    {
        "topic_id": 13,
        "difficulty": "medium",
        "question_text": "What is the difference between WebSockets and Server-Sent Events (SSE)?",
        "explanation": "WebSockets provide full-duplex bidirectional communication over a single persistent TCP connection. SSE provides unidirectional server-to-client streaming over standard HTTP, with automatic reconnection and event IDs.",
        "step_by_step_reasoning": "1. WebSockets: Client can send and receive data at any time (e.g., online gaming, multiplayer canvas).\n2. SSE: Only server pushes to client; client uses regular HTTP POST for outgoing data (e.g., stock tickers, LLM streaming).\n3. SSE works over standard HTTP/2 multiplexing natively.",
        "practical_example": "ChatGPT streaming responses use Server-Sent Events (text/event-stream); chat rooms with voice/drawing use WebSockets.",
        "common_mistake": "Using WebSockets when only server-to-client notifications are needed; SSE is simpler and works through standard HTTP proxies.",
        "learning_tip": "Bidirectional? -> WebSocket. Server-to-client stream only? -> SSE.",
        "options": [
            ("A", "WebSockets are bidirectional (full-duplex), whereas SSE is unidirectional (server-to-client only) over standard HTTP.", True, "Correct: WebSockets allow two-way messaging; SSE is server-to-client streaming."),
            ("B", "SSE requires UDP while WebSockets strictly use TCP.", False, "Incorrect: Both use TCP underlying connections."),
            ("C", "WebSockets can only transmit plain text strings, while SSE transmits binary buffers.", False, "Incorrect: WebSockets transmit binary and text; SSE is text-based."),
            ("D", "SSE does not work over HTTPS encrypted connections.", False, "Incorrect: SSE works seamlessly over HTTPS.")
        ]
    },

    # ==========================================
    # TOPIC 7: Data Structures & Algorithms
    # ==========================================
    {
        "topic_id": 7,
        "difficulty": "medium",
        "question_text": "What is the time complexity of Kadane's algorithm for finding the maximum subarray sum in an array of $N$ integers?",
        "explanation": "Kadane's algorithm scans the array in a single pass, updating the maximum sum ending at each position. Hence, it runs in $O(N)$ time and $O(1)$ auxiliary space.",
        "step_by_step_reasoning": "1. Initialize `max_so_far = arr[0]` and `current_max = arr[0]`.\n2. For each element `x`, `current_max = max(x, current_max + x)`.\n3. Update `max_so_far = max(max_so_far, current_max)`.\n4. Single loop over $N$ items = $O(N)$.",
        "practical_example": "arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4] -> Max contiguous subarray is [4, -1, 2, 1] with sum 6.",
        "common_mistake": "Resetting `current_max` to 0 instead of taking `max(x, current_max + x)` when all numbers in the array are negative.",
        "learning_tip": "Kadane's is the optimal linear algorithm for Maximum Subarray Problem.",
        "options": [
            ("A", "$O(N)$ time complexity and $O(1)$ auxiliary space.", True, "Correct: Single pass through array with constant extra memory."),
            ("B", "$O(N \\log N)$ time complexity using divide-and-conquer.", False, "Incorrect: Divide-and-conquer takes O(N log N), but Kadane is O(N)."),
            ("C", "$O(N^2)$ time complexity using nested loops.", False, "Incorrect: Brute force is O(N^2), Kadane is linear."),
            ("D", "$O(2^N)$ time complexity using recursion.", False, "Incorrect: Kadane is not exponential.")
        ]
    },
    {
        "topic_id": 7,
        "difficulty": "medium",
        "question_text": "In a min-heap with $N$ elements, what is the time complexity of inserting a new element and extracting the minimum element respectively?",
        "explanation": "Inserting an element appends it to the end and bubbles up (heapify-up), taking $O(\\log N)$ time. Extracting the root swaps with the last element and bubbles down (heapify-down), also taking $O(\\log N)$ time.",
        "step_by_step_reasoning": "1. Binary heap height is $\\lfloor\\log_2 N\\rfloor$.\n2. Heapify-up traverses at most the height: $O(\\log N)$.\n3. Heapify-down traverses at most the height: $O(\\log N)$.",
        "practical_example": "Priority queues in Dijkstra's algorithm and Prim's algorithm depend on $O(\\log N)$ heap operations.",
        "common_mistake": "Confusing building a heap from an array ($O(N)$ using Floyd's build-heap) with inserting $N$ elements one by one ($O(N \\log N)$).",
        "learning_tip": "Heap insert = $O(\\log N)$, extract-min = $O(\\log N)$, peek-min = $O(1)$.",
        "options": [
            ("A", "Insert: $O(\\log N)$, Extract-Min: $O(\\log N)$", True, "Correct: Both operations require traversing the tree height."),
            ("B", "Insert: $O(1)$, Extract-Min: $O(N)$", False, "Incorrect: Insert requires restoring the heap property, taking O(log N)."),
            ("C", "Insert: $O(N)$, Extract-Min: $O(1)$", False, "Incorrect: Insertion does not require shifting elements like an array."),
            ("D", "Insert: $O(1)$, Extract-Min: $O(1)$", False, "Incorrect: Neither extraction nor insertion is constant time in a binary heap.")
        ]
    },
    {
        "topic_id": 7,
        "difficulty": "hard",
        "question_text": "Floyd's Cycle-Finding Algorithm (Tortoise and Hare) detects a cycle in a linked list. If the slow pointer moves 1 step and the fast pointer moves 2 steps, what is the maximum time complexity to detect if a cycle exists?",
        "explanation": "Let $k$ be the distance before the loop and $C$ be the loop length. Slow enters the loop after $k$ steps. Fast is already in the loop. The relative speed difference is 1 step per iteration, so they must meet in at most $C$ additional steps. Total steps $\\le k + C = O(N)$.",
        "step_by_step_reasoning": "1. Distance to loop start: $k$.\n2. Loop length: $C$.\n3. Slow and fast meet within at most 1 cycle traversal once both are in the loop.\n4. Total time is linear: $O(N)$, with $O(1)$ extra space.",
        "practical_example": "Detecting circular dependencies in state machines or memory allocations without a hash set.",
        "common_mistake": "Thinking fast pointer can jump over slow without meeting. In discrete integer steps with relative speed 1, distance closes by 1 every step, so meeting is guaranteed.",
        "learning_tip": "To find cycle start: after meeting, reset one pointer to head; advance both 1 step at a time; meeting point is the loop start.",
        "options": [
            ("A", "$O(N)$ time complexity and $O(1)$ space complexity.", True, "Correct: Linear time with zero additional allocated nodes."),
            ("B", "$O(N^2)$ time complexity and $O(N)$ space complexity.", False, "Incorrect: Pointers never require quadratic comparisons."),
            ("C", "$O(N \\log N)$ time complexity and $O(1)$ space complexity.", False, "Incorrect: No divide and conquer or sorting is involved."),
            ("D", "$O(1)$ time complexity and $O(N)$ space complexity.", False, "Incorrect: Detecting a loop cannot be done in constant time.")
        ]
    },
    {
        "topic_id": 7,
        "difficulty": "medium",
        "question_text": "Which data structure is most suitable for implementing an LRU (Least Recently Used) Cache with $O(1)$ `get` and $O(1)$ `put` operations?",
        "explanation": "A Doubly Linked List combined with a Hash Map (Hash Table). The hash map provides $O(1)$ key-to-node lookups, and the doubly linked list allows $O(1)$ node removal and insertion at the head/tail.",
        "step_by_step_reasoning": "1. Get(key): Find node in hash map ($O(1)$), detach from current position in doubly linked list ($O(1)$), attach to head ($O(1)$).\n2. Put(key, val): If exists, update and move to head ($O(1)$). If full, evict tail node ($O(1)$) and delete from map ($O(1)$).\n3. Splay trees or arrays cannot achieve true $O(1)$ worst-case.",
        "practical_example": "Python's `collections.OrderedDict` and Java's `LinkedHashMap` use this exact internal architecture.",
        "common_mistake": "Using a singly linked list; deleting a node requires finding its predecessor, which is $O(N)$ without a doubly linked structure.",
        "learning_tip": "Hash Map (for $O(1)$ search) + Doubly Linked List (for $O(1)$ reordering) = LRU Cache.",
        "options": [
            ("A", "Hash Map combined with a Doubly Linked List.", True, "Correct: Map gives O(1) lookup; DLL gives O(1) removal and insertion."),
            ("B", "Max-Heap combined with a Dynamic Array.", False, "Incorrect: Heap requires O(log N) to update priority or delete arbitrary elements."),
            ("C", "Single Linked List combined with Binary Search Tree.", False, "Incorrect: Search in BST is O(log N) and single linked list deletion is O(N)."),
            ("D", "Circular Queue with fixed array indexing.", False, "Incorrect: Accessing an arbitrary cached element requires O(N) scan.")
        ]
    },

    # ==========================================
    # TOPIC 8: Object-Oriented Programming (OOP)
    # ==========================================
    {
        "topic_id": 8,
        "difficulty": "medium",
        "question_text": "What does the Liskov Substitution Principle (LSP) in SOLID principles state?",
        "explanation": "LSP states that objects of a superclass should be replaceable with objects of its subclasses without breaking application correctness, altering expected behaviors, or violating invariants.",
        "step_by_step_reasoning": "1. If class S is a subtype of class T, objects of type T may be replaced with objects of type S.\n2. Subtypes must not strengthen preconditions (must accept all inputs base class accepts).\n3. Subtypes must not weaken postconditions (must fulfill all guarantees base class promises).",
        "practical_example": "The classic Rectangle vs Square violation: If Square extends Rectangle and overrides setWidth() to also mutate height, algorithms expecting independent dimensions will fail.",
        "common_mistake": "Assuming inheritance is justified solely by real-world 'is-a' relationships without verifying behavioral substitutability.",
        "learning_tip": "Subclasses must honor the contract established by the parent class.",
        "options": [
            ("A", "Subtypes must be substitutable for their base types without altering program correctness or contracts.", True, "Correct: LSP guarantees behavioral compatibility."),
            ("B", "A class should have only one reason to change and one responsibility.", False, "Incorrect: That is the Single Responsibility Principle (SRP)."),
            ("C", "Software entities should be open for extension, but closed for modification.", False, "Incorrect: That is the Open/Closed Principle (OCP)."),
            ("D", "Clients should not be forced to depend upon interfaces they do not use.", False, "Incorrect: That is the Interface Segregation Principle (ISP).")
        ]
    },
    {
        "topic_id": 8,
        "difficulty": "hard",
        "question_text": "How does the virtual table (vtable) and virtual pointer (vptr) mechanism achieve dynamic (runtime) polymorphism in C++?",
        "explanation": "When a class has virtual functions, the compiler creates a `vtable` containing function pointers to the most-derived implementations. Each object instance contains a hidden `vptr` pointing to this vtable, resolved at runtime upon invocation.",
        "step_by_step_reasoning": "1. Class definition creates a static vtable with pointers to virtual methods.\n2. Object constructor initializes hidden `vptr` to point to that class's vtable.\n3. Calling `ptr->virtualMethod()` translates to dereferencing `vptr` to index into the table: `*(ptr->vptr[index])(ptr)` at runtime.",
        "practical_example": "Base* b = new Derived(); b->render(); // looks up Derived::render via b's vptr",
        "common_mistake": "Thinking vtables exist per object instance; there is only one vtable per class type, but each object instance has its own vptr.",
        "learning_tip": "Virtual functions add 1 pointer overhead (`vptr`) per object and 1 extra memory indirection per virtual call.",
        "options": [
            ("A", "Each polymorphic class has a static table of function pointers (vtable), and each object has a hidden pointer (vptr) pointing to it for runtime dispatch.", True, "Correct: vtable stores addresses; vptr links object instance to the table."),
            ("B", "The compiler replaces all function calls with inline assembly macros during compilation.", False, "Incorrect: Virtual dispatch cannot be fully inlined statically when pointers are dynamic."),
            ("C", "The operating system allocates a new thread to execute each virtual method call.", False, "Incorrect: Virtual calls do not spawn threads."),
            ("D", "The JVM garbage collector rewrites bytecodes when subclasses are instantiated.", False, "Incorrect: C++ does not have a JVM or garbage collector.")
        ]
    },

    # ==========================================
    # TOPIC 12: Python Programming
    # ==========================================
    {
        "topic_id": 12,
        "difficulty": "medium",
        "question_text": "What is the output of the following Python code?\n```python\ndef append_to(element, target=[]):\n    target.append(element)\n    return target\n\nprint(append_to(1))\nprint(append_to(2))\n```",
        "explanation": "Default argument values in Python are evaluated once when the function definition is executed, NOT each time the function is called. The same list instance `target` is reused across calls.",
        "step_by_step_reasoning": "1. `target=[]` is created once at module import/definition time.\n2. Call 1: 1 is appended to `target` -> returns [1].\n3. Call 2: 2 is appended to the *same* list instance -> returns [1, 2].",
        "practical_example": "Idiomatic fix: `def append_to(element, target=None): if target is None: target = []`",
        "common_mistake": "Assuming default parameters are freshly instantiated on each invocation like local variables.",
        "learning_tip": "Never use mutable objects (lists, dicts, sets) as default arguments in Python.",
        "options": [
            ("A", "[1] and then [1, 2]", True, "Correct: The mutable default list persists across multiple function invocations."),
            ("B", "[1] and then [2]", False, "Incorrect: A fresh list is NOT created on the second invocation."),
            ("C", "[1] and then TypeError: target is immutable", False, "Incorrect: Lists are mutable; no TypeError is raised."),
            ("D", "SyntaxError: default argument cannot be empty list", False, "Incorrect: It is valid Python syntax, though an anti-pattern.")
        ]
    },
    {
        "topic_id": 12,
        "difficulty": "hard",
        "question_text": "What is Python's Global Interpreter Lock (GIL), and how does it impact multi-threaded CPU-bound programs in CPython?",
        "explanation": "The GIL is a mutex that protects access to Python objects, preventing multiple native threads from executing Python bytecodes simultaneously. For CPU-bound tasks, multi-threading cannot achieve true multicore parallelism; multiprocessing is required.",
        "step_by_step_reasoning": "1. CPython memory management is not thread-safe (reference counting requires synchronization).\n2. The GIL ensures only one thread executes Python bytecode at any instant.\n3. For I/O-bound tasks (network, disk), threads release the GIL while waiting.\n4. For CPU-bound tasks, multiprocessing or C-extensions releasing GIL must be used for parallel speedups.",
        "practical_example": "Running 4 threads calculating prime numbers on a 4-core machine is often slower than 1 thread due to GIL lock contention.",
        "common_mistake": "Believing multi-threading is useless in Python; it is highly effective for I/O-bound tasks (e.g. web scraping, network requests).",
        "learning_tip": "CPU-bound concurrency -> `multiprocessing`. I/O-bound concurrency -> `asyncio` or `threading`.",
        "options": [
            ("A", "It is a mutex in CPython allowing only one native thread to execute Python bytecode at a time, limiting CPU-bound speedups.", True, "Correct: GIL prevents simultaneous multicore bytecode execution in CPython."),
            ("B", "It is a compiler flag that locks files to prevent concurrent file editing.", False, "Incorrect: GIL manages bytecode execution, not OS file handles."),
            ("C", "It is an encryption module that secures global variables across the internet.", False, "Incorrect: GIL has nothing to do with cryptographic encryption."),
            ("D", "It is a database transaction lock built into Python's SQLite driver.", False, "Incorrect: GIL is part of the CPython interpreter runtime core.")
        ]
    },

    # ==========================================
    # TOPIC 55: Java Programming
    # ==========================================
    {
        "topic_id": 55,
        "difficulty": "medium",
        "question_text": "What happens in Java if two objects are equal according to the `equals(Object obj)` method, but have different `hashCode()` values?",
        "explanation": "It violates the Java `hashCode` and `equals` contract. If stored in a hash-based collection (like `HashMap` or `HashSet`), equal objects will hash into different buckets, causing lookup and deduplication failures.",
        "step_by_step_reasoning": "1. Contract: If `a.equals(b)` is true, then `a.hashCode() == b.hashCode()` MUST be true.\n2. HashMap computes `bucket = hash(key.hashCode()) & (n-1)`.\n3. If hash codes differ, the search looks in the wrong bucket and returns `null` even if the key exists.",
        "practical_example": "map.put(new Person('Alex'), 'Developer'); map.get(new Person('Alex')) returns null if hashCode is not overridden consistently.",
        "common_mistake": "Overriding `equals()` without overriding `hashCode()`, which causes subtle collection bugs.",
        "learning_tip": "Always override `hashCode()` whenever you override `equals()`.",
        "options": [
            ("A", "Hash-based collections like HashMap and HashSet will fail to find or deduplicate the objects, causing retrieval failures.", True, "Correct: Unequal hash codes send equal objects to separate buckets."),
            ("B", "The JVM will throw a compile-time IncompatibleHashContractException.", False, "Incorrect: The compiler cannot enforce runtime hash values."),
            ("C", "Java automatically calls System.identityHashCode to rectify the collision.", False, "Incorrect: JVM does not auto-correct broken class contracts."),
            ("D", "The garbage collector immediately marks both objects for destruction.", False, "Incorrect: Memory management is unaffected by hash codes.")
        ]
    },
    {
        "topic_id": 55,
        "difficulty": "hard",
        "question_text": "In Java's memory model, what is the role of the `volatile` keyword when applied to a variable?",
        "explanation": "The `volatile` keyword guarantees visibility and ordering across threads: writes to a volatile variable are immediately flushed to main memory, and reads are always loaded from main memory rather than thread CPU caches, preventing instruction reordering.",
        "step_by_step_reasoning": "1. CPU cores cache shared variables in L1/L2 caches.\n2. Without `volatile`, Thread A's write to a flag may stay in its core cache, leaving Thread B in an infinite loop reading stale memory.\n3. `volatile` inserts memory barriers to guarantee visibility and happens-before relationship.",
        "practical_example": "private volatile boolean running = true; // safe flag termination across threads",
        "common_mistake": "Assuming `volatile` makes compound operations like `count++` atomic; `volatile` ensures visibility, not mutual exclusion (atomicity).",
        "learning_tip": "For atomic compound operations (increment/decrement), use `AtomicInteger` or `synchronized`.",
        "options": [
            ("A", "It guarantees that reads and writes are visible to all threads immediately from main memory and prevents compiler instruction reordering.", True, "Correct: volatile ensures memory visibility and establishes happens-before boundaries."),
            ("B", "It makes all compound operations like `i++` completely thread-safe and atomic.", False, "Incorrect: volatile does not provide atomicity for compound operations."),
            ("C", "It serializes the object to disk automatically when memory is low.", False, "Incorrect: volatile has nothing to do with serialization or disk I/O."),
            ("D", "It prevents the variable from ever being modified after initialization.", False, "Incorrect: That is the role of `final`, not `volatile`.")
        ]
    },

    # ==========================================
    # TOPIC 56: C & C++ Programming
    # ==========================================
    {
        "topic_id": 56,
        "difficulty": "medium",
        "question_text": "In modern C++ (C++11 and later), how does `std::unique_ptr` differ from `std::shared_ptr`?",
        "explanation": "`std::unique_ptr` enforces exclusive ownership of a dynamically allocated resource (cannot be copied, only moved), with zero runtime overhead compared to raw pointers. `std::shared_ptr` provides shared ownership via reference counting.",
        "step_by_step_reasoning": "1. `unique_ptr` has copy constructor disabled (`= delete`); it transfers ownership via `std::move`.\n2. When `unique_ptr` goes out of scope, it automatically calls `delete`.\n3. `shared_ptr` maintains an atomic control block with a reference count; deletion occurs when refcount drops to 0.",
        "practical_example": "std::unique_ptr<Socket> sock = std::make_unique<Socket>(); // exclusive owner",
        "common_mistake": "Creating cyclic references between two `shared_ptr` objects, which causes memory leaks (use `std::weak_ptr` to break cycles).",
        "learning_tip": "Default to `unique_ptr`. Only reach for `shared_ptr` when genuine shared ownership is required.",
        "options": [
            ("A", "`std::unique_ptr` has strict exclusive ownership with zero overhead, while `std::shared_ptr` maintains an atomic reference-counted control block.", True, "Correct: unique_ptr is exclusive and move-only; shared_ptr uses reference counting."),
            ("B", "`std::unique_ptr` stores data on the stack while `std::shared_ptr` stores data in ROM.", False, "Incorrect: Both manage dynamic heap memory."),
            ("C", "`std::unique_ptr` allows up to 4 concurrent copies across threads.", False, "Incorrect: unique_ptr explicitly forbids copying."),
            ("D", "`std::shared_ptr` cannot be used with polymorphic class hierarchies.", False, "Incorrect: shared_ptr fully supports polymorphic types and custom deleters.")
        ]
    },
    {
        "topic_id": 56,
        "difficulty": "hard",
        "question_text": "What is undefined behavior in C/C++, and which of the following code snippets triggers it?",
        "explanation": "Undefined behavior (UB) occurs when code executes an invalid operation for which the C/C++ standard imposes no requirements. Accessing memory out-of-bounds, modifying a variable multiple times without sequence points, or dereferencing a null/dangling pointer causes UB.",
        "step_by_step_reasoning": "1. In `int arr[5]; arr[5] = 10;`, index 5 is out of bounds (valid indices are 0 to 4).\n2. The compiler makes no guarantees; it may crash, silently corrupt memory, or optimize away code.\n3. UB allows compilers to make aggressive optimizations that break buggy assumptions.",
        "practical_example": "int *p = nullptr; *p = 42; // Undefined behavior (null pointer dereference)",
        "common_mistake": "Thinking 'undefined behavior' simply means the program will always crash. In reality, it may appear to work in debug mode and fail disastrously in production release builds.",
        "learning_tip": "Use AddressSanitizer (`-fsanitize=address`) and Valgrind to catch undefined behavior early.",
        "options": [
            ("A", "Dereferencing a dangling pointer or writing out of array bounds (`arr[5]` on array of size 5).", True, "Correct: Out-of-bounds writes and dangling pointer dereferences are classic undefined behavior."),
            ("B", "Declaring a variable of type `unsigned long long int` without initializing it immediately.", False, "Incorrect: Indeterminate value, but not UB until read without initialization."),
            ("C", "Returning 0 from the `main` function in C99 standard.", False, "Incorrect: Perfectly standard and defined behavior."),
            ("D", "Using `#include <stdio.h>` multiple times with include guards.", False, "Incorrect: Include guards safely make multiple inclusions a no-op.")
        ]
    },

    # ==========================================
    # TOPIC 57: JavaScript & TypeScript
    # ==========================================
    {
        "topic_id": 57,
        "difficulty": "medium",
        "question_text": "What is the difference between TypeScript's `interface` and `type` alias when extending object contracts?",
        "explanation": "Interfaces can be merged through 'declaration merging' (multiple interface declarations with the same name merge their properties), and can be extended using `extends`. Type aliases can define unions, primitives, and tuples, and use intersections (`&`) to combine shapes, but cannot be reopened.",
        "step_by_step_reasoning": "1. `interface User { name: string }` + `interface User { id: number }` merges to `{ name: string, id: number }`.\n2. `type User = { ... }` cannot be re-declared in the same scope (causes Duplicate Identifier error).\n3. `type` can represent unions (`type Status = 'open' | 'closed'`), which interfaces cannot.",
        "practical_example": "Use interfaces for public API definitions and OOP models; use type aliases for complex unions, utilities, and mapped types.",
        "common_mistake": "Believing type aliases provide faster runtime execution; TypeScript types and interfaces are completely erased at compile time.",
        "learning_tip": "Need declaration merging or extends? Use interface. Need unions, primitives, or mapped types? Use type.",
        "options": [
            ("A", "Interfaces support declaration merging and OOP extension, whereas type aliases support union types, tuples, and intersections without merging.", True, "Correct: Interfaces merge automatically; type aliases handle unions and primitives."),
            ("B", "Type aliases exist at JavaScript runtime while interfaces are stripped out during compilation.", False, "Incorrect: Both are completely erased at compile time in JS output."),
            ("C", "Interfaces can only declare functions, not object properties.", False, "Incorrect: Interfaces frequently declare object properties."),
            ("D", "Type aliases can only be used inside classes, not in standalone modules.", False, "Incorrect: Type aliases can be declared anywhere in TS files.")
        ]
    },

    # ==========================================
    # TOPIC 58: Software Engineering & Testing
    # ==========================================
    {
        "topic_id": 58,
        "difficulty": "medium",
        "question_text": "In modern software testing, what does the Test Pyramid principle advocate?",
        "explanation": "The Test Pyramid recommends having a large base of fast, isolated, low-cost Unit Tests, a moderate middle layer of Integration Tests, and a small, selective top layer of End-to-End (E2E) UI Tests.",
        "step_by_step_reasoning": "1. Unit tests: Fast execution, precise failure identification, low maintenance cost.\n2. Integration tests: Verify module boundaries and DB/API communication.\n3. E2E tests: Slow, brittle, expensive to run, verify full critical business journeys.\n4. Inverted pyramid ('ice cream cone') results in slow builds and flaky test suites.",
        "practical_example": "70% Unit tests (Jest/Pytest), 20% Integration tests (API endpoints), 10% E2E tests (Playwright/Cypress).",
        "common_mistake": "Relying almost entirely on Selenium/Playwright E2E tests, which take hours to run and produce false positives from network timing issues.",
        "learning_tip": "Push tests down the pyramid: if a bug can be caught in a unit test, don't write an E2E test for it.",
        "options": [
            ("A", "A broad foundation of fast, low-cost unit tests, fewer integration tests, and minimal high-level end-to-end (E2E) tests.", True, "Correct: Unit base -> Integration middle -> E2E apex."),
            ("B", "90% manual UI regression testing and 10% unit testing.", False, "Incorrect: Manual testing is minimized in automated CI/CD pipelines."),
            ("C", "All tests must be written exclusively by end-users in production environments.", False, "Incorrect: Developers and QA automate tests pre-release."),
            ("D", "End-to-End tests should outnumber unit tests 10 to 1.", False, "Incorrect: That describes the anti-pattern known as the 'ice-cream cone'.")
        ]
    },
    {
        "topic_id": 58,
        "difficulty": "medium",
        "question_text": "What is the difference between a Mock and a Stub in unit testing?",
        "explanation": "A Stub provides canned pre-configured responses to calls made during the test. A Mock additionally verifies behavioral expectations, checking which methods were called, how many times, and with what parameters.",
        "step_by_step_reasoning": "1. Stub = State verification (provides data to the system under test).\n2. Mock = Interaction verification (checks whether `mailer.sendWelcomeEmail()` was called exactly once).\n3. Stubs never fail a test directly; mocks fail the test if expected calls were not made.",
        "practical_example": "when(userRepo.findById(1)).thenReturn(fakeUser); // Stub\nverify(paymentGateway, times(1)).charge(100); // Mock expectation",
        "common_mistake": "Over-mocking internal implementation details, which causes tests to break when refactoring even if business behavior remains correct.",
        "learning_tip": "Stub for input data; Mock for verifying required outgoing side-effects.",
        "options": [
            ("A", "A stub provides canned data to test inputs, while a mock verifies interactions and call expectations.", True, "Correct: Stubs return pre-configured data; mocks verify method call behavior."),
            ("B", "Mocks only run on physical hardware, while stubs run in Docker containers.", False, "Incorrect: Both are in-memory test doubles."),
            ("C", "Stubs test database performance while mocks test network latency.", False, "Incorrect: Both isolate code from external dependencies."),
            ("D", "There is no difference; mock and stub are exact synonyms in JUnit and Pytest.", False, "Incorrect: Martin Fowler defines clear architectural distinctions.")
        ]
    },

    # ==========================================
    # TOPIC 11: Computer Networks
    # ==========================================
    {
        "topic_id": 11,
        "difficulty": "medium",
        "question_text": "What is the sequence of packets exchanged in a TCP Three-Way Handshake to establish a reliable connection?",
        "explanation": "The client sends a `SYN` (Synchronize) packet with initial sequence number $x$. The server responds with `SYN-ACK` with its own sequence number $y$ and acknowledgment $x+1$. The client responds with `ACK` with acknowledgment $y+1$.",
        "step_by_step_reasoning": "1. Client -> Server: SYN (seq = x)\n2. Server -> Client: SYN-ACK (seq = y, ack = x + 1)\n3. Client -> Server: ACK (seq = x + 1, ack = y + 1)\n4. Connection state transitions: CLOSED -> SYN_SENT -> SYN_RECEIVED -> ESTABLISHED.",
        "practical_example": "Every HTTPS request begins with TCP 3-way handshake before TLS negotiation.",
        "common_mistake": "Confusing connection establishment (3-way: SYN, SYN-ACK, ACK) with connection termination (4-way: FIN, ACK, FIN, ACK).",
        "learning_tip": "SYN -> SYN-ACK -> ACK.",
        "options": [
            ("A", "SYN -> SYN-ACK -> ACK", True, "Correct: Standard RFC 793 TCP establishment sequence."),
            ("B", "ACK -> SYN -> DATA", False, "Incorrect: Connection starts with SYN."),
            ("C", "FIN -> FIN-ACK -> RST", False, "Incorrect: FIN is used for connection teardown."),
            ("D", "PING -> PONG -> ACK", False, "Incorrect: PING/PONG is ICMP echo, not TCP handshake.")
        ]
    },
    {
        "topic_id": 11,
        "difficulty": "hard",
        "question_text": "Why does HTTP/2 introduce stream multiplexing over a single TCP connection, and what HTTP/1.1 problem does it solve?",
        "explanation": "HTTP/1.1 suffers from Head-of-Line (HoL) blocking at the application layer, where requests on the same TCP connection must wait for preceding responses to finish. HTTP/2 splits messages into binary frames interleaved across independent streams on a single TCP connection.",
        "step_by_step_reasoning": "1. HTTP/1.1 browsers opened 6 concurrent TCP connections per domain to load assets in parallel.\n2. A slow CSS or JS asset blocked subsequent requests on that connection.\n3. HTTP/2 multiplexes dozens of concurrent streams over 1 TCP connection, eliminating application HoL blocking.",
        "practical_example": "Loading 100 image thumbnails simultaneously in HTTP/2 without opening 100 sockets.",
        "common_mistake": "Thinking HTTP/2 solves TCP transport HoL blocking; packet loss in TCP still pauses all multiplexed HTTP/2 streams (solved in HTTP/3 QUIC over UDP).",
        "learning_tip": "HTTP/1.1 = text-based & pipelined with HoL blocking; HTTP/2 = binary framing & multiplexed.",
        "options": [
            ("A", "It solves HTTP/1.1 application-layer Head-of-Line blocking by interleaving binary frames for multiple concurrent requests over one TCP socket.", True, "Correct: Binary framing allows simultaneous independent streams."),
            ("B", "It converts all web traffic into UDP packets without sequence numbers.", False, "Incorrect: HTTP/2 operates over TCP; HTTP/3 uses UDP/QUIC."),
            ("C", "It eliminates the need for DNS servers by caching all IP addresses in the browser cache.", False, "Incorrect: DNS resolution is still required."),
            ("D", "It replaces HTML with XML across all web servers.", False, "Incorrect: Data payloads remain standard web formats.")
        ]
    },

    # ==========================================
    # TOPIC 10: Operating Systems
    # ==========================================
    {
        "topic_id": 10,
        "difficulty": "medium",
        "question_text": "What are the four Coffman conditions that must simultaneously hold for a deadlock to occur in an operating system?",
        "explanation": "Deadlock can only occur if all 4 Coffman conditions hold: 1. Mutual Exclusion, 2. Hold and Wait, 3. No Preemption, 4. Circular Wait. Breaking any one of these conditions prevents deadlocks.",
        "step_by_step_reasoning": "1. Mutual Exclusion: Resources cannot be shared simultaneously.\n2. Hold and Wait: A process holding resources can request new resources.\n3. No Preemption: Resources cannot be forcibly taken from a process.\n4. Circular Wait: $P_0$ waits for $P_1$, $P_1$ waits for $P_2$, ..., $P_n$ waits for $P_0$.",
        "practical_example": "Banker's algorithm avoids deadlocks by ensuring safe allocation states; lock ordering breaks circular wait.",
        "common_mistake": "Thinking breaking mutual exclusion is always practical; hardware like printers or disk writers are inherently non-shareable.",
        "learning_tip": "Mutual Exclusion + Hold & Wait + No Preemption + Circular Wait.",
        "options": [
            ("A", "Mutual Exclusion, Hold and Wait, No Preemption, and Circular Wait.", True, "Correct: These four conditions are necessary and sufficient for deadlock."),
            ("B", "High CPU Usage, Paging Thrashing, Low Memory, and Cache Misses.", False, "Incorrect: These describe system performance degradation, not deadlocks."),
            ("C", "Multiprocessing, Multithreading, Context Switching, and Interrupt Handling.", False, "Incorrect: These are standard OS concurrency mechanisms."),
            ("D", "Virtual Memory, Segmentation, Demand Paging, and Inode Allocation.", False, "Incorrect: These are memory management concepts.")
        ]
    },
    {
        "topic_id": 10,
        "difficulty": "hard",
        "question_text": "What is 'Thrashing' in an operating system with virtual memory, and what causes it?",
        "explanation": "Thrashing occurs when the operating system spends more time swapping pages in and out of secondary storage (disk) than executing actual process instructions, caused when the total working sets of active processes exceed available physical RAM.",
        "step_by_step_reasoning": "1. If physical memory is overcommitted, page faults occur continuously.\n2. Process A faults -> OS reads page from disk -> Process B is scheduled -> Process B faults -> Repeat.\n3. The CPU scheduler sees low CPU utilization and mistakenly admits more processes, worsening the paging storm.\n4. Resolution: Reduce degree of multiprogramming or add physical RAM.",
        "practical_example": "Opening 100 memory-heavy applications on a 4GB RAM laptop causing disk activity at 100% and UI freeze.",
        "common_mistake": "Confusing page faults with thrashing; occasional page faults are normal; continuous cascading page faults causing zero work progress is thrashing.",
        "learning_tip": "Working Set Model monitors working set size to prevent thrashing.",
        "options": [
            ("A", "The OS spends virtually all CPU cycles servicing continuous page faults and disk swapping rather than executing program instructions.", True, "Correct: Working set exceeds physical RAM, causing constant page swapping."),
            ("B", "A CPU overheating issue causing the motherboard clock speed to be throttled.", False, "Incorrect: That is hardware thermal throttling."),
            ("C", "A cyberattack where a hacker floods the network socket with SYN packets.", False, "Incorrect: That describes a SYN flood denial of service attack."),
            ("D", "The process of defragmenting physical hard drives during bootup.", False, "Incorrect: Disk defragmentation is a file system optimization.")
        ]
    },

    # ==========================================
    # TOPIC 9: DBMS & SQL
    # ==========================================
    {
        "topic_id": 9,
        "difficulty": "medium",
        "question_text": "What is the key difference between a Clustered Index and a Non-Clustered Index in relational databases?",
        "explanation": "A clustered index defines the physical order in which table rows are sorted and stored on disk; therefore, a table can have only ONE clustered index (usually the primary key). Non-clustered indexes create a separate lookup structure containing pointers back to data rows.",
        "step_by_step_reasoning": "1. Clustered index leaf nodes ARE the actual data rows.\n2. Non-clustered index leaf nodes contain index keys and row locators (pointers/row IDs).\n3. A table can have multiple non-clustered indexes, but only one clustered index.",
        "practical_example": "A dictionary is sorted alphabetically by word (Clustered Index). The index at the back of a textbook lists topics with page numbers (Non-Clustered Index).",
        "common_mistake": "Believing creating 10 indexes on a table has no write penalty; every INSERT/UPDATE/DELETE must update all non-clustered index trees.",
        "learning_tip": "Clustered = Physical data ordering (1 per table). Non-clustered = Separate B-Tree pointers (many per table).",
        "options": [
            ("A", "A clustered index determines the physical storage order of rows (only 1 per table), whereas non-clustered indexes store pointers to rows (multiple allowed).", True, "Correct: Clustered dictates physical layout; non-clustered is a separate index table of pointers."),
            ("B", "Clustered indexes are stored in RAM while non-clustered indexes are stored in cloud object storage.", False, "Incorrect: Both index structures reside in database storage files on disk/buffer pool."),
            ("C", "Non-clustered indexes can only be used with text columns, not integers.", False, "Incorrect: Non-clustered indexes support any indexable data type."),
            ("D", "Clustered indexes cannot be created on primary key columns.", False, "Incorrect: Primary keys default to clustered indexes in most RDBMS (e.g. MySQL InnoDB, SQL Server).")
        ]
    },
    {
        "topic_id": 9,
        "difficulty": "hard",
        "question_text": "What is the difference between `RANK()` and `DENSE_RANK()` window functions in SQL when dealing with tied values?",
        "explanation": "`RANK()` leaves gaps in rank numbering after ties (e.g., 1, 2, 2, 4), whereas `DENSE_RANK()` assigns consecutive rank numbers without any gaps (e.g., 1, 2, 2, 3).",
        "step_by_step_reasoning": "1. Values: [100, 90, 90, 80].\n2. `RANK()`: 1, 2, 2, 4 (rank 3 is skipped because two rows tied for rank 2).\n3. `DENSE_RANK()`: 1, 2, 2, 3 (no ranks are skipped).\n4. `ROW_NUMBER()`: 1, 2, 3, 4 (assigns strictly sequential integers regardless of ties).",
        "practical_example": "Finding the 2nd highest salary: `WHERE dense_rank_val = 2` handles ties correctly without skipping.",
        "common_mistake": "Using `RANK()` to find the N-th highest record; if multiple top records tie, `RANK() = 2` will return 0 rows.",
        "learning_tip": "Ties with gaps -> `RANK()`. Ties without gaps -> `DENSE_RANK()`. No ties allowed -> `ROW_NUMBER()`.",
        "options": [
            ("A", "`RANK()` skips subsequent rank numbers after ties (1, 2, 2, 4), while `DENSE_RANK()` does not leave gaps (1, 2, 2, 3).", True, "Correct: RANK produces gaps; DENSE_RANK produces contiguous ranks."),
            ("B", "`DENSE_RANK()` only works with decimal values, while `RANK()` requires strings.", False, "Incorrect: Both window functions operate over numeric partition orderings."),
            ("C", "`RANK()` assigns identical numbers to all rows regardless of order by.", False, "Incorrect: RANK follows the specified ORDER BY clause."),
            ("D", "`DENSE_RANK()` deletes duplicate rows from the underlying database table.", False, "Incorrect: Window functions are read-only query projections; they never delete rows.")
        ]
    },

    # ==========================================
    # TOPIC 59: System Design & Cloud Computing
    # ==========================================
    {
        "topic_id": 59,
        "difficulty": "hard",
        "question_text": "In distributed systems design, what does the CAP theorem state regarding partitions?",
        "explanation": "The CAP theorem states that a distributed data store can simultaneously provide at most two out of three guarantees: Consistency (all nodes see the same data at the same time), Availability (every request receives a response), and Partition Tolerance (system continues to operate despite network partitions). Because network partitions ($P$) are inevitable in distributed networks, systems must choose between Consistency ($CP$) or Availability ($AP$).",
        "step_by_step_reasoning": "1. $P$ (Partition Tolerance) is non-negotiable in real-world distributed networks where network splits occur.\n2. When partition occurs: to guarantee Consistency ($C$), nodes must reject writes that cannot replicate, sacrificing Availability ($A$).\n3. Or to guarantee Availability ($A$), nodes accept writes independently, causing inconsistent data ($C$ is sacrificed until reconciliation).",
        "practical_example": "MongoDB and HBase are $CP$ systems; Apache Cassandra and DynamoDB are configurable $AP$ systems.",
        "common_mistake": "Claiming a system is 'CA' across distributed networks; without Partition Tolerance, a single cable cut breaks the entire system.",
        "learning_tip": "In the presence of a network partition, choose either Consistency (CP) or Availability (AP).",
        "options": [
            ("A", "When a network partition occurs, a distributed system must trade off between either Consistency or Availability; it cannot guarantee all three simultaneously.", True, "Correct: Real-world distributed systems must choose between CP and AP."),
            ("B", "A system can achieve 100% Consistency, 100% Availability, and 100% Partition Tolerance if hosted on AWS.", False, "Incorrect: Physics and network latency prevent achieving all three in distributed systems."),
            ("C", "CAP stands for Cache, Application, and Persistence layers in web architecture.", False, "Incorrect: CAP stands for Consistency, Availability, Partition Tolerance."),
            ("D", "Databases using SSD drives are immune to network partitions.", False, "Incorrect: Partitions occur at the network switch/connectivity layer.")
        ]
    },

    # ==========================================
    # TOPIC 60: AI & Machine Learning Foundations
    # ==========================================
    {
        "topic_id": 60,
        "difficulty": "medium",
        "question_text": "In classification models with severe class imbalance (e.g., fraud detection where only 0.1% of transactions are fraudulent), why is Accuracy a misleading metric?",
        "explanation": "A naive model that predicts 'Not Fraud' 100% of the time will achieve 99.9% accuracy while catching zero fraudulent transactions. Metrics like Precision, Recall, F1-Score, and PR-AUC reflect true model utility in imbalanced datasets.",
        "step_by_step_reasoning": "1. Accuracy = $(TP + TN) / (TP + TN + FP + FN)$.\n2. When $TN$ is overwhelming (99.9%), accuracy is dominated by the majority class.\n3. Recall = $TP / (TP + FN)$ measures how many actual fraud cases were identified.",
        "practical_example": "In cancer diagnosis, a test that says 'healthy' to everyone has high accuracy but is fatal in practice.",
        "common_mistake": "Evaluating medical diagnosis or fraud models using Accuracy instead of Precision-Recall tradeoffs.",
        "learning_tip": "For imbalanced datasets, use Precision, Recall, F1-score, or Precision-Recall AUC curves.",
        "options": [
            ("A", "A model that blindly predicts the majority class will achieve high accuracy while failing to detect any positive minority cases.", True, "Correct: Majority class dominance skews raw accuracy."),
            ("B", "Accuracy calculations divide by zero when negative samples are present.", False, "Incorrect: The denominator is total sample size."),
            ("C", "Accuracy cannot be computed on numeric feature vectors.", False, "Incorrect: Accuracy is computed on predicted labels vs true labels."),
            ("D", "Scikit-learn refuses to calculate accuracy if sample sizes exceed 1,000.", False, "Incorrect: Scikit-learn has no such limitation.")
        ]
    },

    # ==========================================
    # TOPIC 22: Problems on Ages
    # ==========================================
    {
        "topic_id": 22,
        "difficulty": "medium",
        "question_text": "The ratio of the present ages of a father and his son is 7 : 3. Ten years ago, the ratio of their ages was 3 : 1. What is the present age of the father?",
        "explanation": "Let present ages be $7x$ and $3x$. Ten years ago: $(7x - 10) / (3x - 10) = 3 / 1$. Cross multiplying: $7x - 10 = 9x - 30 \\Rightarrow 2x = 20 \\Rightarrow x = 10$. Present age of father $= 7x = 7 \\times 10 = 70$ years.",
        "step_by_step_reasoning": "1. Express ages in terms of $x$: Father $= 7x$, Son $= 3x$.\n2. Set up equation 10 years ago: $\\frac{7x - 10}{3x - 10} = 3$.\n3. $7x - 10 = 9x - 30$.\n4. $2x = 20 \\Rightarrow x = 10$.\n5. Father's age $= 7(10) = 70$ years.",
        "practical_example": "Verification: Father was $70-10=60$, Son was $30-10=20$. Ratio $60:20 = 3:1$. Perfect match.",
        "common_mistake": "Adding 10 instead of subtracting 10 for 'ten years ago'.",
        "learning_tip": "Always check your answer against the past ratio condition to verify.",
        "options": [
            ("A", "70 years", True, "Correct: 7x where x = 10 equals 70 years."),
            ("B", "50 years", False, "Incorrect: If father is 50, son is 21.4 (not integer)."),
            ("C", "60 years", False, "Incorrect: 60 years was his age 10 years ago, not his present age."),
            ("D", "80 years", False, "Incorrect: Does not satisfy the 3:1 ratio 10 years ago.")
        ]
    },

    # ==========================================
    # TOPIC 25: Progressions (AP & GP)
    # ==========================================
    {
        "topic_id": 25,
        "difficulty": "medium",
        "question_text": "Find the sum of all two-digit natural numbers that are divisible by 4.",
        "explanation": "The smallest two-digit number divisible by 4 is 12, and the largest is 96. This forms an Arithmetic Progression (AP) with $a = 12$, $d = 4$, and $l = 96$. Number of terms $n = \\frac{96 - 12}{4} + 1 = 22$. Sum $S = \\frac{n}{2}(a + l) = \\frac{22}{2}(12 + 96) = 11 \\times 108 = 1188$.",
        "step_by_step_reasoning": "1. Sequence: 12, 16, 20, ..., 96.\n2. $n = \\frac{l - a}{d} + 1 = \\frac{96 - 12}{4} + 1 = \\frac{84}{4} + 1 = 21 + 1 = 22$.\n3. $S_n = \\frac{n}{2}(a + l) = \\frac{22}{2}(12 + 96) = 11 \\times 108 = 1188$.",
        "practical_example": "Quick verification: average of terms is $(12+96)/2 = 54$. Total sum $= 22 \\times 54 = 1188$.",
        "common_mistake": "Forgetting to add 1 when calculating the number of terms $n$.",
        "learning_tip": "Sum of AP $= \\text{number of terms} \\times \\text{average of first and last terms}$.",
        "options": [
            ("A", "1188", True, "Correct: 22 terms with average 54 = 1188."),
            ("B", "1134", False, "Incorrect: Result of using n = 21 instead of 22."),
            ("C", "1200", False, "Incorrect: Arithmetic estimation error."),
            ("D", "1248", False, "Incorrect: Result of including single-digit or three-digit multiples.")
        ]
    },

    # ==========================================
    # TOPIC 24: Geometry & Mensuration
    # ==========================================
    {
        "topic_id": 24,
        "difficulty": "medium",
        "question_text": "A metallic sphere of radius 6 cm is melted and recast into small cones of radius 1 cm and height 2 cm each. How many cones can be formed assuming zero metal loss?",
        "explanation": "Volume of sphere $= \\frac{4}{3}\\pi R^3 = \\frac{4}{3}\\pi (6)^3 = \\frac{4}{3}\\pi (216) = 288\\pi \\text{ cm}^3$. Volume of one cone $= \\frac{1}{3}\\pi r^2 h = \\frac{1}{3}\\pi (1)^2(2) = \\frac{2}{3}\\pi \\text{ cm}^3$. Number of cones $= \\frac{288\\pi}{\\frac{2}{3}\\pi} = 288 \\times \\frac{3}{2} = 432$.",
        "step_by_step_reasoning": "1. Volume of sphere: $V_s = \\frac{4}{3}\\pi R^3 = \\frac{4}{3}\\pi (216) = 288\\pi$.\n2. Volume of one cone: $V_c = \\frac{1}{3}\\pi r^2 h = \\frac{1}{3}\\pi (1)(2) = \\frac{2}{3}\\pi$.\n3. Number of cones $= \\frac{V_s}{V_c} = \\frac{288\\pi}{2\\pi / 3} = \\frac{288 \\times 3}{2} = 432$.",
        "practical_example": "Standard placement question pattern testing 3D conservation of volume.",
        "common_mistake": "Using cone volume formula as $\\pi r^2 h$ (cylinder formula) instead of $\\frac{1}{3}\\pi r^2 h$.",
        "learning_tip": "Keep $\\pi$ un-evaluated so it cancels out directly in division.",
        "options": [
            ("A", "432", True, "Correct: 288 pi / (2/3 pi) = 432 cones."),
            ("B", "216", False, "Incorrect: Forgetting the factor of 4 in sphere volume."),
            ("C", "144", False, "Incorrect: Miscalculating cone volume."),
            ("D", "512", False, "Incorrect: Calculation error assuming cubic volumes.")
        ]
    },

    # ==========================================
    # TOPIC 26: Algebra & Equations
    # ==========================================
    {
        "topic_id": 26,
        "difficulty": "medium",
        "question_text": "If $x + \\frac{1}{x} = 5$, what is the value of $x^3 + \\frac{1}{x^3}$?",
        "explanation": "Using identity $(a+b)^3 = a^3 + b^3 + 3ab(a+b)$: $(x + 1/x)^3 = x^3 + 1/x^3 + 3(x)(1/x)(x + 1/x)$. Substituting $x + 1/x = 5$: $5^3 = x^3 + 1/x^3 + 3(1)(5) \\Rightarrow 125 = x^3 + 1/x^3 + 15 \\Rightarrow x^3 + 1/x^3 = 125 - 15 = 110$.",
        "step_by_step_reasoning": "1. Let $k = x + \\frac{1}{x} = 5$.\n2. $x^3 + \\frac{1}{x^3} = k^3 - 3k$.\n3. $5^3 - 3(5) = 125 - 15 = 110$.",
        "practical_example": "Formula shortcut: If $x + 1/x = k$, then $x^2 + 1/x^2 = k^2 - 2$, and $x^3 + 1/x^3 = k^3 - 3k$.",
        "common_mistake": "Calculating $5^3 = 125$ and forgetting to subtract $3k = 15$.",
        "learning_tip": "Memorize: $x^3 + \\frac{1}{x^3} = k^3 - 3k$.",
        "options": [
            ("A", "110", True, "Correct: k^3 - 3k = 125 - 15 = 110."),
            ("B", "125", False, "Incorrect: Forgetting to subtract the cross product term 3k."),
            ("C", "140", False, "Incorrect: Adding 15 instead of subtracting."),
            ("D", "115", False, "Incorrect: Subtracting 2k instead of 3k.")
        ]
    },

    # ==========================================
    # TOPIC 28: Coding, Clocks & Ordering
    # ==========================================
    {
        "topic_id": 28,
        "difficulty": "medium",
        "question_text": "What is the angle between the hour hand and the minute hand of a clock at 3:40 PM?",
        "explanation": "Angle formula: $\\theta = |30H - 5.5M|$. Here $H = 3$ and $M = 40$. $\\theta = |30(3) - 5.5(40)| = |90 - 220| = |-130| = 130^\\circ$.",
        "step_by_step_reasoning": "1. Hour hand moves $0.5^\\circ$ per minute: at 3:40, hour hand is at $30 \\times 3 + 0.5 \\times 40 = 90 + 20 = 110^\\circ$.\n2. Minute hand moves $6^\\circ$ per minute: at 40 min, minute hand is at $6 \\times 40 = 240^\\circ$.\n3. Absolute difference $= |240^\\circ - 110^\\circ| = 130^\\circ$.",
        "practical_example": "Standard clock angle question in TCS NQT and Infosys placement exams.",
        "common_mistake": "Assuming the hour hand stays stationary on the 3 while the minute hand moves to 8 (which yields $150^\\circ$).",
        "learning_tip": "Angle $= |30H - \\frac{11}{2}M|$.",
        "options": [
            ("A", "$130^\\circ$", True, "Correct: |90 - 220| = 130 degrees."),
            ("B", "$140^\\circ$", False, "Incorrect: Calculation mistake in hour displacement."),
            ("C", "$150^\\circ$", False, "Incorrect: Assumes hour hand does not move from 3."),
            ("D", "$120^\\circ$", False, "Incorrect: Arithmetic error.")
        ]
    },
    {
        "topic_id": 28,
        "difficulty": "medium",
        "question_text": "In a row of 45 students facing North, Rahul is 18th from the left end. What is his position from the right end?",
        "explanation": "Formula: $\\text{Total} = \\text{Left} + \\text{Right} - 1$. Here $\\text{Total} = 45$, $\\text{Left} = 18$. $45 = 18 + \\text{Right} - 1 \\Rightarrow 45 = 17 + \\text{Right} \\Rightarrow \\text{Right} = 45 - 17 = 28$.",
        "step_by_step_reasoning": "1. $\\text{Right Position} = \\text{Total} - \\text{Left Position} + 1$.\n2. $45 - 18 + 1 = 27 + 1 = 28$.\n3. Rahul is the 28th person from the right.",
        "practical_example": "Verification: $18 + 28 - 1 = 46 - 1 = 45$. Matches exactly.",
        "common_mistake": "Simply doing $45 - 18 = 27$, forgetting to add 1 because the person himself is counted from both sides.",
        "learning_tip": "Position from other end $= \\text{Total} - \\text{Given position} + 1$.",
        "options": [
            ("A", "28th", True, "Correct: 45 - 18 + 1 = 28th."),
            ("B", "27th", False, "Incorrect: Forgot to add 1 for inclusive counting."),
            ("C", "26th", False, "Incorrect: Subtracted 1 instead of adding."),
            ("D", "29th", False, "Incorrect: Added 2 instead of 1.")
        ]
    },

    # ==========================================
    # TOPIC 5: Blood Relations & Directions
    # ==========================================
    {
        "topic_id": 5,
        "difficulty": "medium",
        "question_text": "Pointing to a photograph, a woman says: 'He is the only son of the father-in-law of my husband's mother.' How is the man in the photograph related to the woman's husband?",
        "explanation": "Let's break it down: 'My husband's mother' = Mother-in-law. 'The father-in-law of my husband's mother' = The husband's paternal grandfather (father of the husband's father). 'The only son of the paternal grandfather' = The husband's father. Thus, the man is the husband's father.",
        "step_by_step_reasoning": "1. Woman's husband's mother = Mother of husband.\n2. Father-in-law of husband's mother = Husband's father's father (paternal grandfather).\n3. Only son of paternal grandfather = Husband's father.\n4. Therefore, the man is the father of the woman's husband.",
        "practical_example": "Common deduction question on campus placement aptitude rounds.",
        "common_mistake": "Confusing maternal with paternal grandfather.",
        "learning_tip": "Work backwards from the possessive pronouns: 'my husband's mother' -> 'her father-in-law' -> 'his only son'.",
        "options": [
            ("A", "Father", True, "Correct: Paternal grandfather's only son is the father."),
            ("B", "Brother", False, "Incorrect: Brother would be a generation below grandfather's only son."),
            ("C", "Uncle", False, "Incorrect: Problem states 'only son', which rules out uncles."),
            ("D", "Grandfather", False, "Incorrect: Grandfather is the father-in-law, his son is the father.")
        ]
    },

    # ==========================================
    # TOPIC 4: Logical Deductions & Syllogisms
    # ==========================================
    {
        "topic_id": 4,
        "difficulty": "medium",
        "question_text": "Statements:\n1. All engineers are innovators.\n2. Some innovators are leaders.\n\nConclusions:\nI. Some engineers are leaders.\nII. Some leaders are innovators.\n\nWhich conclusion(s) logically follow?",
        "explanation": "From statement 2 ('Some innovators are leaders'), the converse ('Some leaders are innovators') immediately and necessarily follows. However, there is no direct overlap guaranteed between engineers and leaders. Thus, only Conclusion II follows.",
        "step_by_step_reasoning": "1. All E are I: The set E is a subset of I.\n2. Some I are L: The intersection of I and L is non-empty.\n3. Does E intersect with L? Not necessarily (L could intersect I outside of E).\n4. Conclusion I is uncertain (does not necessarily follow).\n5. Conclusion II (Some L are I) is the direct valid conversion of Statement 2.",
        "practical_example": "Venn Diagram: Circle E inside Circle I. Circle L overlaps with Circle I, but does not need to touch Circle E.",
        "common_mistake": "Assuming because engineers are innovators and innovators are leaders, all or some engineers must be leaders.",
        "learning_tip": "Conversion rule: 'Some A are B' always logically implies 'Some B are A'.",
        "options": [
            ("A", "Only Conclusion II follows", True, "Correct: 'Some innovators are leaders' directly implies 'Some leaders are innovators'."),
            ("B", "Only Conclusion I follows", False, "Incorrect: Overlap between engineers and leaders is not guaranteed."),
            ("C", "Both Conclusion I and II follow", False, "Incorrect: Conclusion I does not necessarily follow."),
            ("D", "Neither Conclusion I nor II follows", False, "Incorrect: Conclusion II is a valid direct converse.")
        ]
    },

    # ==========================================
    # TOPIC 61: Reading Comprehension & Para Jumbles
    # ==========================================
    {
        "topic_id": 61,
        "difficulty": "medium",
        "question_text": "Arrange the following sentences in a logical, coherent paragraph:\n\nP. Microservices break monolithic applications into loosely coupled, independently deployable services.\nQ. Consequently, software teams can deploy features faster and with higher resilience.\nR. However, this architectural freedom introduces operational complexities such as network latency and distributed state management.\nS. In recent years, enterprise software development has undergone a major paradigm shift.",
        "explanation": "Sentence S introduces the broad topic (paradigm shift in enterprise software). Sentence P defines the shift (monolith to microservices). Sentence Q explains the positive consequence of this shift (faster deployment and resilience). Sentence R introduces the contrast ('However...') with its operational challenges. The coherent order is S-P-Q-R.",
        "step_by_step_reasoning": "1. S is the opening introductory sentence establishing historical context.\n2. P defines the subject introduced in S ('Microservices...').\n3. Q begins with 'Consequently' which details the positive result of P.\n4. R begins with 'However' which contrasts Q's benefits with operational trade-offs.\n5. Proper flow: S -> P -> Q -> R.",
        "practical_example": "Standard reading comprehension / verbal reasoning question in IT recruitment tests.",
        "common_mistake": "Placing Q before P without noticing that 'Consequently' requires an action (P) to precede it.",
        "learning_tip": "Identify the standalone opening sentence, followed by definitions, logical consequences, and contrast markers.",
        "options": [
            ("A", "S - P - Q - R", True, "Correct: Introduction -> Definition -> Benefit -> Contrast."),
            ("B", "P - S - R - Q", False, "Incorrect: S is a much better opening thesis statement than P."),
            ("C", "R - Q - P - S", False, "Incorrect: Cannot start a paragraph with the contrast transition 'However'."),
            ("D", "S - R - P - Q", False, "Incorrect: 'However' cannot precede the explanation of benefits.")
        ]
    }
]

def seed_expansion_pack4():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    now_iso = datetime.now(timezone.utc).isoformat()

    added_q = 0
    added_opt = 0

    for item in QUESTIONS_DATA:
        # Check if identical question already exists
        cursor.execute("SELECT id FROM questions WHERE question_text = ?", (item["question_text"],))
        existing = cursor.fetchone()
        if existing:
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
            item.get("step_by_step_reasoning", ""),
            item.get("practical_example", ""),
            item.get("common_mistake", ""),
            item.get("learning_tip", ""),
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

    print(f"Pack 4: Successfully added {added_q} questions and {added_opt} options.")

if __name__ == "__main__":
    seed_expansion_pack4()

