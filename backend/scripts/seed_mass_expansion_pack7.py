"""
InterviewAI — Massive Question Expansion Pack 7
Elevates all remaining topics to 15+ questions each across Aptitude, Logical Reasoning,
Verbal Ability, and Core Computer Science.
"""

import sqlite3
import os
from datetime import datetime, timezone

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "interviewai.db")

QUESTIONS = [
    # -------------------------------------------------------------
    # Topic 56: C & C++ Programming (needs 9+ -> currently 6)
    # -------------------------------------------------------------
    {
        "topic_id": 56, "difficulty": "medium",
        "question_text": "What is the output of the following C code snippet?\n#include <stdio.h>\nint main() {\n  int x = 10;\n  int *p = &x;\n  int **pp = &p;\n  printf('%d', **pp + 5);\n  return 0;\n}",
        "explanation": "`*pp` dereferences `pp` to obtain pointer `p`. `**pp` dereferences `p` to obtain the value of `x` (10). Therefore, `**pp + 5` evaluates to 10 + 5 = 15.",
        "options": [
            ("A", "15", True, "Correct: Double dereference yields 10; 10 + 5 = 15."),
            ("B", "20", False, "Incorrect: Value is 10, not 15."),
            ("C", "Address of x + 5", False, "Incorrect: Double dereference yields the integer value, not pointer address."),
            ("D", "Segmentation fault", False, "Incorrect: All pointers are properly initialized.")
        ]
    },
    {
        "topic_id": 56, "difficulty": "hard",
        "question_text": "In C++, what is RAII (Resource Acquisition Is Initialization)?",
        "explanation": "RAII is an idiom where resource lifecycle is bound to object lifetime: resources (heap memory, file handles, sockets, mutexes) are acquired in the constructor and automatically released in the destructor when the object goes out of scope.",
        "options": [
            ("A", "An idiom where resource holding is tied to object lifetime, guaranteeing automatic cleanup via destructors.", True, "Correct: Constructors acquire resources, destructors release them deterministically."),
            ("B", "A compiler flag that enables multi-threaded compilation in GCC.", False, "Incorrect: RAII is a design paradigm, not a compiler flag."),
            ("C", "A database transaction isolation protocol.", False, "Incorrect: RAII belongs to C++ systems programming."),
            ("D", "An initialization list syntax required for all struct definitions.", False, "Incorrect: Member initialization list is separate from RAII.")
        ]
    },
    {
        "topic_id": 56, "difficulty": "medium",
        "question_text": "What is the size of an empty class in C++ and why?",
        "explanation": "In C++, an empty class has a size of 1 byte so that distinct object instances always have unique memory addresses.",
        "options": [
            ("A", "1 byte, ensuring distinct object instances have unique addresses in memory.", True, "Correct: Standard C++ mandates non-zero size for unique object addressing."),
            ("B", "0 bytes, because it contains no data members or virtual functions.", False, "Incorrect: Size cannot be zero in standard C++."),
            ("C", "4 bytes, aligned with the default CPU register size.", False, "Incorrect: Only 1 byte is allocated."),
            ("D", "8 bytes, reserving pointer space for a hidden vptr.", False, "Incorrect: No vptr exists unless virtual functions are declared.")
        ]
    },
    {
        "topic_id": 56, "difficulty": "medium",
        "question_text": "What does the `volatile` qualifier tell the C/C++ compiler about a variable?",
        "explanation": "`volatile` informs the compiler that the variable's value can be modified by external factors outside the program's control (such as hardware registers, interrupt service routines, or concurrent threads), preventing unwanted compiler optimizations like caching in registers.",
        "options": [
            ("A", "The variable may be changed unexpectedly by hardware or external threads, preventing compiler register-caching optimizations.", True, "Correct: Forces read/write directly from memory every time."),
            ("B", "The variable is stored in flash ROM memory permanently.", False, "Incorrect: volatile variables reside in standard RAM."),
            ("C", "The variable cannot be modified once initialized (read-only).", False, "Incorrect: That describes `const`, not `volatile`."),
            ("D", "The variable is automatically deleted when CPU usage exceeds 90%.", False, "Incorrect: Completely fabricated.")
        ]
    },
    {
        "topic_id": 56, "difficulty": "hard",
        "question_text": "What is the purpose of `std::move` in modern C++?",
        "explanation": "`std::move` does not move anything by itself; it unconditionally casts an expression to an rvalue reference (`T&&`), enabling move constructors or move assignment operators to transfer ownership of resources without expensive deep copying.",
        "options": [
            ("A", "It unconditionally casts an expression to an rvalue reference, enabling resource theft via move semantics without deep copies.", True, "Correct: static_cast<std::remove_reference_t<T>&&>(t)."),
            ("B", "It physically relocates data blocks in computer RAM from stack to heap.", False, "Incorrect: It does not move memory directly, only alters value category."),
            ("C", "It pauses program execution for 10 milliseconds.", False, "Incorrect: That is std::this_thread::sleep_for."),
            ("D", "It deletes pointers and sets them to nullptr.", False, "Incorrect: std::move does not delete anything.")
        ]
    },
    {
        "topic_id": 56, "difficulty": "medium",
        "question_text": "Which bitwise operation can be used to check whether an integer $N > 0$ is a power of 2?",
        "explanation": "If $N$ is a power of 2, its binary representation has exactly one bit set (e.g. $8 = 1000_2$, $7 = 0111_2$). The expression `(N & (N - 1)) == 0` clears the lowest set bit; if the result is 0, $N$ is a power of 2.",
        "options": [
            ("A", "`(N & (N - 1)) == 0`", True, "Correct: Powers of 2 have a single set bit which is cleared by subtracting 1."),
            ("B", "`(N | (N - 1)) == 0`", False, "Incorrect: Bitwise OR combines bits, never yielding 0 for positive N."),
            ("C", "`(N ^ (N - 1)) == 0`", False, "Incorrect: XOR yields 0 only if both operands are identical."),
            ("D", "`(N >> 1) == 0`", False, "Incorrect: Only true for N = 1.")
        ]
    },

    # -------------------------------------------------------------
    # Topic 58: Software Engineering & Testing (needs 9+ -> currently 6)
    # -------------------------------------------------------------
    {
        "topic_id": 58, "difficulty": "medium",
        "question_text": "In software testing, what is the key difference between Black-Box and White-Box testing?",
        "explanation": "Black-Box testing evaluates functionality against requirements without knowledge of internal code or logic structures. White-Box testing examines internal code paths, control flows, loops, and conditions with full source code visibility.",
        "options": [
            ("A", "Black-box tests functionality without internal code knowledge; white-box tests internal code logic and paths.", True, "Correct: External specifications vs internal code paths."),
            ("B", "Black-box is for frontend only; white-box is for backend only.", False, "Incorrect: Both methodologies apply to all layers."),
            ("C", "White-box testing is conducted solely by end users in production.", False, "Incorrect: End users perform User Acceptance Testing (black-box)."),
            ("D", "Black-box testing requires root server administrative privileges.", False, "Incorrect: Black-box requires no server privileges.")
        ]
    },
    {
        "topic_id": 58, "difficulty": "medium",
        "question_text": "What does the 'Red, Green, Refactor' cycle represent in Test-Driven Development (TDD)?",
        "explanation": "1. Red: Write a failing unit test for the desired feature. 2. Green: Write minimal implementation code to make the test pass. 3. Refactor: Clean up code and eliminate duplication while keeping all tests green.",
        "options": [
            ("A", "Write a failing test (Red), implement code to pass it (Green), and optimize design while retaining green status (Refactor).", True, "Correct: The foundational loop of TDD."),
            ("B", "Red status means server crash, Green means reboot, Refactor means rebuild database.", False, "Incorrect: TDD is an automated coding practice."),
            ("C", "Code reviews where bugs are redlined, approved green, and merged.", False, "Incorrect: That describes Git review workflows."),
            ("D", "Traffic light algorithm for managing microservice rate limits.", False, "Incorrect: Completely unrelated.")
        ]
    },
    {
        "topic_id": 58, "difficulty": "hard",
        "question_text": "What is 'Code Coverage' versus 'Branch Coverage' in software quality engineering?",
        "explanation": "Line/Code coverage measures the percentage of code lines executed by tests. Branch coverage is stricter, ensuring that every decision branch (both `true` and `false` evaluations of every `if` or `switch` condition) has been tested.",
        "options": [
            ("A", "Line coverage checks if statements were executed; branch coverage ensures all decision paths (true and false) were traversed.", True, "Correct: 100% line coverage does not guarantee 100% branch coverage."),
            ("B", "Branch coverage tests Git branches while code coverage tests pull requests.", False, "Incorrect: Branch coverage refers to control-flow decision branches."),
            ("C", "Code coverage is for compiled languages; branch coverage is for interpreted languages.", False, "Incorrect: Both apply universally across languages."),
            ("D", "Line coverage is impossible to automate in CI/CD pipelines.", False, "Incorrect: Tools like Istanbul, JaCoCo, and Coverage.py automate it.")
        ]
    },
    {
        "topic_id": 58, "difficulty": "medium",
        "question_text": "What is 'Regression Testing' and when is it performed?",
        "explanation": "Regression testing re-runs existing test suites after code modifications, bug fixes, or new feature additions to ensure previously working functionality has not broken.",
        "options": [
            ("A", "Re-testing existing features after code modifications to confirm no new bugs were introduced into working modules.", True, "Correct: Guards against unintended side-effects."),
            ("B", "Testing how software behaves when CPU temperature decreases.", False, "Incorrect: That would be environmental stress testing."),
            ("C", "Testing only deprecated legacy features before deletion.", False, "Incorrect: Verifies the entire active codebase."),
            ("D", "Testing beta features exclusively with external paying customers.", False, "Incorrect: That describes Beta testing.")
        ]
    },

    # -------------------------------------------------------------
    # Topic 8: Object-Oriented Programming (needs 8+ -> currently 7)
    # -------------------------------------------------------------
    {
        "topic_id": 8, "difficulty": "medium",
        "question_text": "What is the Diamond Problem in object-oriented programming, and how do languages like C++ and Java address it?",
        "explanation": "The Diamond Problem arises in multiple inheritance when a class inherits from two classes that both inherit from a common base class, causing ambiguity regarding which superclass implementation to execute. C++ resolves it using `virtual` inheritance; Java avoids it by disallowing multiple class inheritance and using interfaces with default methods.",
        "options": [
            ("A", "Ambiguity from multiple inheritance of a shared base class; resolved by C++ virtual inheritance and Java interface contracts.", True, "Correct: Prevents duplicated base instances and ambiguous method dispatch."),
            ("B", "A security vulnerability involving encryption keys shaped like diamonds.", False, "Incorrect: It is a class hierarchy design ambiguity."),
            ("C", "A database deadlock between four simultaneous transactions.", False, "Incorrect: It belongs to OOP inheritance, not database locking."),
            ("D", "A memory leak caused by allocating dynamic arrays inside a loop.", False, "Incorrect: Memory leaks are unrelated to diamond hierarchies.")
        ]
    },
    {
        "topic_id": 8, "difficulty": "medium",
        "question_text": "What is the primary characteristic of the Singleton Design Pattern?",
        "explanation": "The Singleton pattern ensures that a class has only one instance throughout the application lifecycle and provides a global access point to that instance, typically using a private constructor and static factory method.",
        "options": [
            ("A", "Guarantees a class has only one instance and provides a global point of access to it.", True, "Correct: Enforces single-instance constraint with private constructor."),
            ("B", "Allows an object to create up to 10 instances dynamically.", False, "Incorrect: Singleton strictly limits to one instance."),
            ("C", "Separates object creation from its representation using a builder.", False, "Incorrect: That describes the Builder pattern."),
            ("D", "Converts the interface of a class into another interface clients expect.", False, "Incorrect: That describes the Adapter pattern.")
        ]
    },
    {
        "topic_id": 8, "difficulty": "hard",
        "question_text": "What is the difference between Method Overloading and Method Overriding?",
        "explanation": "Method Overloading is compile-time (static) polymorphism where methods in the same class share the same name but have different parameter lists. Method Overriding is runtime (dynamic) polymorphism where a subclass provides a specific implementation of a method already declared in its superclass.",
        "options": [
            ("A", "Overloading is compile-time with different parameter signatures; Overriding is runtime where subclass replaces superclass implementation.", True, "Correct: Static vs Dynamic polymorphism distinction."),
            ("B", "Overloading requires the `virtual` keyword while Overriding forbids it.", False, "Incorrect: Overriding uses virtual in C++."),
            ("C", "Overriding only works with private methods, while Overloading requires public methods.", False, "Incorrect: Private methods cannot be overridden."),
            ("D", "Overloading is supported only in Python, not in Java or C++.", False, "Incorrect: Java and C++ natively support method overloading.")
        ]
    },

    # -------------------------------------------------------------
    # Topic 12: Python Programming (needs 8+ -> currently 7)
    # -------------------------------------------------------------
    {
        "topic_id": 12, "difficulty": "medium",
        "question_text": "In Python, how does a shallow copy (`copy.copy`) differ from a deep copy (`copy.deepcopy`) for nested data structures?",
        "explanation": "A shallow copy creates a new compound object and inserts references to the objects found in the original. A deep copy recursively duplicates all nested objects, ensuring that modifying a nested object in the copy does not alter the original.",
        "options": [
            ("A", "Shallow copy copies the outer container while referencing nested items; deep copy recursively duplicates all nested objects.", True, "Correct: Modifying nested lists in a shallow copy affects the original."),
            ("B", "Shallow copy saves memory to disk while deep copy saves to CPU cache.", False, "Incorrect: Both operate in application heap memory."),
            ("C", "Deep copy converts all numbers into floating point values.", False, "Incorrect: Deep copy preserves data types intact."),
            ("D", "Python does not support deep copying of lists or dictionaries.", False, "Incorrect: `copy.deepcopy` is standard library functionality.")
        ]
    },
    {
        "topic_id": 12, "difficulty": "hard",
        "question_text": "What is the purpose of Python's `__slots__` attribute in class definitions?",
        "explanation": "By default, Python stores instance attributes in a dictionary (`__dict__`). Defining `__slots__` tells Python not to use `__dict__`, allocating a fixed amount of space for a static set of attributes. This significantly reduces memory footprint and accelerates attribute access for millions of instances.",
        "options": [
            ("A", "It replaces the dynamic `__dict__` with a fixed-size memory array, drastically reducing memory usage for many instances.", True, "Correct: Eliminates __dict__ overhead per instance."),
            ("B", "It automatically connects the class to a PostgreSQL database table.", False, "Incorrect: __slots__ is pure Python memory optimization."),
            ("C", "It enables multi-threading on GPUs natively.", False, "Incorrect: Unrelated to GPU acceleration."),
            ("D", "It forbids subclasses from inheriting from the parent class.", False, "Incorrect: Subclasses can still inherit from slotted classes.")
        ]
    },
    {
        "topic_id": 12, "difficulty": "medium",
        "question_text": "What is a Python decorator and what is its syntactic equivalent?",
        "explanation": "A decorator is a callable that takes a function as input, extends its behavior without modifying the function itself, and returns a callable. The `@decorator` syntax above `def func():` is syntactic sugar for `func = decorator(func)`.",
        "options": [
            ("A", "A function that wraps another function to extend behavior; `@my_dec def f()` is equivalent to `f = my_dec(f)`.", True, "Correct: Standard closure-based higher-order function pattern."),
            ("B", "A GUI widget used to add border styling to Tkinter desktop apps.", False, "Incorrect: Decorator is a language metaprogramming feature."),
            ("C", "A command line argument parser for terminal scripts.", False, "Incorrect: That is argparse."),
            ("D", "A compiler directive that converts Python bytecodes into C++ binaries.", False, "Incorrect: That describes tools like Cython or Nuitka.")
        ]
    },

    # -------------------------------------------------------------
    # Topic 55: Java Programming (needs 8+ -> currently 7)
    # -------------------------------------------------------------
    {
        "topic_id": 55, "difficulty": "medium",
        "question_text": "What is the difference between `final`, `finally`, and `finalize()` in Java?",
        "explanation": "- `final`: keyword to declare constants, prevent method overriding, or forbid class inheritance.\n- `finally`: block in exception handling that executes regardless of whether an exception occurred.\n- `finalize()`: deprecated method on `Object` called by Garbage Collector before reclaiming memory.",
        "options": [
            ("A", "`final` is an immutability/inheritance modifier, `finally` is a guaranteed cleanup block in try-catch, `finalize()` is a GC hook.", True, "Correct: Core Java distinctions frequently examined in campus interviews."),
            ("B", "All three are exact synonyms introduced in Java 17 for thread synchronization.", False, "Incorrect: They serve entirely distinct language roles."),
            ("C", "`finally` creates constants while `final` executes cleanup code.", False, "Incorrect: Reversed definitions."),
            ("D", "`finalize()` is used to terminate the JVM with an exit code.", False, "Incorrect: That is System.exit().")
        ]
    },
    {
        "topic_id": 55, "difficulty": "hard",
        "question_text": "In Java's Garbage Collection, what is the Generational Hypothesis?",
        "explanation": "The Weak Generational Hypothesis observes that most objects survive for only a short time after allocation (die young). Java divides the heap into Young Generation (Eden, Survivor) and Old Generation (Tenured), collecting the Young Generation frequently with lightweight Minor GCs.",
        "options": [
            ("A", "Most allocated objects die young; separating heap into Young and Old generations allows frequent, fast minor garbage collections.", True, "Correct: Basis for HotSpot collectors (G1, CMS, ZGC)."),
            ("B", "Garbage collection takes twice as long for each new major Java version release.", False, "Incorrect: GC algorithms have become significantly faster."),
            ("C", "Objects must exist for at least 1 hour before garbage collection can inspect them.", False, "Incorrect: Objects die in milliseconds."),
            ("D", "All objects are permanently stored in RAM and never collected until application exit.", False, "Incorrect: That would cause rapid OutOfMemoryErrors.")
        ]
    },
    {
        "topic_id": 55, "difficulty": "medium",
        "question_text": "What is the difference between `ArrayList` and `LinkedList` in Java Collections?",
        "explanation": "`ArrayList` uses a resizable array providing $O(1)$ random access by index, but $O(N)$ insertion/deletion in the middle due to element shifting. `LinkedList` uses a doubly linked list providing $O(1)$ insertions/deletions at known nodes, but $O(N)$ random access.",
        "options": [
            ("A", "`ArrayList` has $O(1)$ indexed access and $O(N)$ middle insertions; `LinkedList` has $O(N)$ indexed access and $O(1)$ pointer insertion.", True, "Correct: Array-backed vs Node-pointer backed collections."),
            ("B", "`ArrayList` can only store strings while `LinkedList` stores primitives.", False, "Incorrect: Both store any object type using generics."),
            ("C", "`LinkedList` is stored on GPU while `ArrayList` is stored on CPU.", False, "Incorrect: Both reside in JVM heap memory."),
            ("D", "`ArrayList` is synchronized by default while `LinkedList` is not.", False, "Incorrect: Neither is synchronized by default (Vector is).")
        ]
    },

    # -------------------------------------------------------------
    # Topic 57: JavaScript & TypeScript (needs 8+ -> currently 7)
    # -------------------------------------------------------------
    {
        "topic_id": 57, "difficulty": "medium",
        "question_text": "What is 'hoisting' in JavaScript, and how do `var`, `let`, and `const` differ regarding it?",
        "explanation": "Hoisting is JavaScript's behavior of moving declarations to the top of their scope during compilation. `var` declarations are hoisted and initialized to `undefined`. `let` and `const` are hoisted but remain uninitialized in the 'Temporal Dead Zone' (TDZ), throwing a `ReferenceError` if accessed before declaration.",
        "options": [
            ("A", "Declarations are hoisted; `var` initializes to `undefined`, while `let`/`const` enter the Temporal Dead Zone throwing ReferenceError if accessed early.", True, "Correct: TDZ prevents accessing let/const before initialization."),
            ("B", "Hoisting only occurs when running in Node.js, not in web browsers.", False, "Incorrect: Hoisting is a fundamental ECMAScript standard behavior."),
            ("C", "`let` and `const` are completely ignored by the JavaScript engine until script end.", False, "Incorrect: They are parsed in the lexical declaration phase."),
            ("D", "Hoisting converts all variables to global window object properties.", False, "Incorrect: Block and function scopes are respected.")
        ]
    },
    {
        "topic_id": 57, "difficulty": "hard",
        "question_text": "What is the purpose of the `Promise.allSettled()` method compared to `Promise.all()` in modern JavaScript?",
        "explanation": "`Promise.all()` rejects immediately as soon as ANY promise in the iterable rejects (short-circuiting). `Promise.allSettled()` waits for ALL promises to complete regardless of whether they fulfilled or rejected, returning an array of outcome objects with their status and value/reason.",
        "options": [
            ("A", "`Promise.all()` short-circuits on the first rejection; `Promise.allSettled()` waits for all promises to resolve or reject.", True, "Correct: allSettled provides comprehensive resolution tracking."),
            ("B", "`Promise.allSettled()` executes promises sequentially on the server.", False, "Incorrect: Execution remains concurrent."),
            ("C", "`Promise.all()` only accepts arrays of numbers.", False, "Incorrect: Accepts iterables of promises of any type."),
            ("D", "`Promise.allSettled()` deletes rejected promises from browser cache.", False, "Incorrect: Promises are in-memory async primitives.")
        ]
    },

    # -------------------------------------------------------------
    # Topic 60: AI & Machine Learning Foundations (needs 7+ -> currently 8)
    # -------------------------------------------------------------
    {
        "topic_id": 60, "difficulty": "medium",
        "question_text": "What is the Bias-Variance Tradeoff in machine learning?",
        "explanation": "High bias leads to underfitting (the model is too simplistic to capture underlying patterns, high error on both train and test data). High variance leads to overfitting (the model memorizes noise in the training data, high error on unseen test data). The goal is to find an optimal balance minimizing total generalization error.",
        "options": [
            ("A", "High bias causes underfitting (oversimplified model); high variance causes overfitting (memorizing noise); the goal is minimizing total error.", True, "Correct: Fundamental ML model complexity tradeoff."),
            ("B", "Bias refers to ethical discrimination; variance refers to database replication delay.", False, "Incorrect: In statistics/ML, bias and variance are mathematical properties."),
            ("C", "Bias is measured only in unsupervised clustering algorithms.", False, "Incorrect: Applies across supervised regression and classification."),
            ("D", "Variance can be completely eliminated by deleting half the dataset.", False, "Incorrect: Deleting data typically increases variance and degrades model quality.")
        ]
    },
    {
        "topic_id": 60, "difficulty": "hard",
        "question_text": "In Transformer architectures, what is the core mechanism that allows modeling long-range token dependencies in parallel?",
        "explanation": "The Multi-Head Self-Attention mechanism computes attention weights between every pair of tokens in a sequence using Query ($Q$), Key ($K$), and Value ($V$) matrix multiplications ($Attention(Q, K, V) = \\text{softmax}(\\frac{QK^T}{\\sqrt{d_k}})V$), allowing tokens to attend to all other tokens simultaneously without sequential recurrence.",
        "options": [
            ("A", "Scaled Dot-Product Self-Attention, which calculates contextual relationships across all token pairs simultaneously.", True, "Correct: QK^T / sqrt(d_k) eliminates sequential RNN bottlenecks."),
            ("B", "Convolutional max-pooling filters applied over audio waveforms.", False, "Incorrect: That describes CNNs for audio/vision."),
            ("C", "A single-threaded while loop that scans text backwards.", False, "Incorrect: Transformers run highly parallel matrix multiplications on GPUs."),
            ("D", "Random forest bagging across decision trees.", False, "Incorrect: Unrelated to neural attention models.")
        ]
    },

    # -------------------------------------------------------------
    # Topic 7: Data Structures & Algorithms (needs 6+ -> currently 9)
    # -------------------------------------------------------------
    {
        "topic_id": 7, "difficulty": "medium",
        "question_text": "What is the time complexity of searching for a word of length $L$ in a Trie (Prefix Tree) containing $N$ total words?",
        "explanation": "Searching in a Trie traverses one node per character of the query word. Thus, lookup time depends solely on the length of the word $L$, running in $O(L)$ time, completely independent of the total number of words $N$ stored in the tree.",
        "options": [
            ("A", "$O(L)$ where $L$ is the length of the query string, completely independent of $N$.", True, "Correct: One transition per character."),
            ("B", "$O(\\log N)$ because the Trie is a binary search tree.", False, "Incorrect: A Trie is an M-ary tree where transitions take constant time per character."),
            ("C", "$O(N \\times L)$ because every word must be scanned.", False, "Incorrect: Prefix sharing eliminates scanning all words."),
            ("D", "$O(1)$ instant hash lookup.", False, "Incorrect: Each character requires a tree link traversal.")
        ]
    },
    {
        "topic_id": 7, "difficulty": "hard",
        "question_text": "Dijkstra's Algorithm finds shortest paths from a single source in a weighted graph. Why does it fail when negative edge weights are present?",
        "explanation": "Dijkstra's algorithm is greedy: once a vertex is marked visited (extracted from the priority queue), its calculated distance is assumed to be finalized and optimal. A negative edge encountered later could provide a shorter path to an already finalized vertex, breaking the greedy invariant. Bellman-Ford must be used instead.",
        "options": [
            ("A", "Its greedy assumption fails: once a node's distance is marked finalized, negative edges could offer shorter paths retroactively.", True, "Correct: Greedy choice property is violated by negative weights."),
            ("B", "It triggers a division by zero error in the priority queue.", False, "Incorrect: Priority queue does not perform division."),
            ("C", "Negative edges convert the graph into an undirected cycle automatically.", False, "Incorrect: Graph topology does not change based on weight sign."),
            ("D", "It runs forever in an infinite loop on any negative number.", False, "Incorrect: Only negative weight cycles cause infinite loops in Bellman-Ford, but Dijkstra simply produces wrong outputs.")
        ]
    },

    # -------------------------------------------------------------
    # Topic 11: Computer Networks (needs 6+ -> currently 9)
    # -------------------------------------------------------------
    {
        "topic_id": 11, "difficulty": "medium",
        "question_text": "What is the difference between Symmetric and Asymmetric encryption?",
        "explanation": "Symmetric encryption uses the SAME single secret key for both encryption and decryption (fast, e.g. AES-256). Asymmetric encryption uses a public-private key pair: data encrypted with the public key can only be decrypted by the matching private key (slower, e.g. RSA, ECC).",
        "options": [
            ("A", "Symmetric uses one shared secret key for encryption and decryption; Asymmetric uses a public-private key pair.", True, "Correct: Foundation of modern TLS hybrid encryption."),
            ("B", "Symmetric encryption only works on wireless networks.", False, "Incorrect: Encryption algorithms are transport-independent."),
            ("C", "Asymmetric encryption is 1,000 times faster than symmetric encryption.", False, "Incorrect: Asymmetric encryption is significantly slower due to modular arithmetic."),
            ("D", "Symmetric encryption does not require keys.", False, "Incorrect: Requires a secret shared key.")
        ]
    },
    {
        "topic_id": 11, "difficulty": "medium",
        "question_text": "What is a Reverse Proxy, and how does it differ from a Forward Proxy?",
        "explanation": "A Forward Proxy sits in front of clients, protecting client identities and mediating outbound internet requests. A Reverse Proxy sits in front of origin web/app servers, intercepting inbound client requests to perform load balancing, SSL termination, and caching.",
        "options": [
            ("A", "A forward proxy protects clients accessing the internet; a reverse proxy protects web servers handling incoming client traffic.", True, "Correct: Nginx/HAProxy act as reverse proxies in server architectures."),
            ("B", "A reverse proxy reverses the bytes in network packets for security.", False, "Incorrect: Unrelated to packet byte order."),
            ("C", "Forward proxies cannot cache HTTP responses.", False, "Incorrect: Forward proxies frequently cache outbound web assets."),
            ("D", "Reverse proxies can only handle UDP DNS traffic.", False, "Incorrect: Reverse proxies primarily handle HTTP/HTTPS/TCP traffic.")
        ]
    },

    # -------------------------------------------------------------
    # Topic 59: System Design & Cloud Computing (needs 6+ -> currently 9)
    # -------------------------------------------------------------
    {
        "topic_id": 59, "difficulty": "medium",
        "question_text": "What is Consistent Hashing, and why is it preferred over simple modulo hashing (`hash(key) % N`) in distributed caching systems?",
        "explanation": "With `hash(key) % N`, when a cache server is added or removed ($N$ changes), almost ALL keys map to new servers, causing a catastrophic cache miss storm. Consistent Hashing maps keys and servers onto a virtual 360-degree ring; when a server joins or leaves, only $K/N$ keys need to be remapped on average.",
        "options": [
            ("A", "It maps keys and nodes to a circular hash ring, so adding or removing a node only remaps $K/N$ keys, avoiding cache stampedes.", True, "Correct: Foundation of DynamoDB, Cassandra, and Memcached clusters."),
            ("B", "It ensures all user passwords are encrypted with consistent salt lengths.", False, "Incorrect: Belongs to cryptographic hashing, not consistent hashing rings."),
            ("C", "It eliminates the need for database storage completely.", False, "Incorrect: Caching supplements databases, not replaces persistent storage."),
            ("D", "It forces all web requests to route through a single master server.", False, "Incorrect: Consistent hashing enables decentralized distribution.")
        ]
    },
    {
        "topic_id": 59, "difficulty": "hard",
        "question_text": "What is the difference between Horizontal Scaling (Scale-Out) and Vertical Scaling (Scale-Up)?",
        "explanation": "Vertical scaling upgrades existing single-machine hardware (adding more RAM, faster CPU cores, larger SSDs), which has a hard physical ceiling and introduces a single point of failure. Horizontal scaling adds more independent server nodes to the distributed cluster, enabling near-linear elasticity and high availability.",
        "options": [
            ("A", "Vertical scaling adds more CPU/RAM to a single machine (hardware ceiling); Horizontal scaling adds more machines to a cluster (higher fault tolerance).", True, "Correct: Scale-up vs Scale-out architectural principle."),
            ("B", "Horizontal scaling means rotating monitors horizontally on developer desks.", False, "Incorrect: Completely fabricated joke distractor."),
            ("C", "Vertical scaling is free in all cloud providers while horizontal scaling is paid.", False, "Incorrect: Upgrading machine instances incurs significant cloud costs."),
            ("D", "Horizontal scaling is impossible with relational SQL databases.", False, "Incorrect: Distributed SQL (CockroachDB, Spanner, read replicas, sharding) scales horizontally.")
        ]
    },

    # -------------------------------------------------------------
    # Topic 62: Walmart-Style Placement Assessment (needs 9+ -> currently 6)
    # -------------------------------------------------------------
    {
        "topic_id": 62, "difficulty": "medium",
        "question_text": "A retail supercenter purchases an inventory of 500 laptops at INR 40,000 each. It sells 300 of them at a 25% profit and the remaining 200 at a 10% loss. What is the net overall percentage profit or loss on the entire inventory?",
        "explanation": "Total Cost Price = 500 * 40,000 = 2,00,00,000 (INR 2 Cr).\nRevenue from 300 laptops = 300 * (40,000 * 1.25) = 300 * 50,000 = 1,50,00,000.\nRevenue from 200 laptops = 200 * (40,000 * 0.90) = 200 * 36,000 = 72,00,000.\nTotal Revenue = 1,50,00,000 + 72,00,000 = 2,22,00,000.\nNet Profit = 22,00,000.\nPercentage Profit = (22,00,000 / 2,00,00,000) * 100 = 11% overall profit.",
        "options": [
            ("A", "11% Profit", True, "Correct: 300(25%) + 200(-10%) / 500 = (7500 - 2000)/500 = 5500/500 = 11%."),
            ("B", "15% Profit", False, "Incorrect: Overestimates revenue."),
            ("C", "7.5% Loss", False, "Incorrect: The higher volume at 25% profit outweighs the 10% loss."),
            ("D", "12.5% Profit", False, "Incorrect: Unweighted average (25 - 10)/2 = 7.5%, not 12.5%.")
        ]
    },
    {
        "topic_id": 62, "difficulty": "hard",
        "question_text": "Walmart Global Tech OA Question: In an automated warehouse, packages are stored in a conveyor belt with weights represented as an array. You can load packages into trucks of capacity $C$. What is the minimum truck capacity required to ship all packages within $D$ days without splitting packages across trucks?",
        "explanation": "This is the classic Capacity To Ship Packages Within D Days problem. The answer space for capacity $C$ ranges from $\\max(\\text{weights})$ to $\\sum(\\text{weights})$. We binary search over this capacity range, verifying feasibility in $O(N)$ for each midpoint. Total time complexity is $O(N \\log(\\sum W - \\max W))$.",
        "options": [
            ("A", "Binary search on the answer space between $\\max(\\text{weights})$ and $\\sum(\\text{weights})$ with $O(N)$ greedy feasibility checks.", True, "Correct: Optimal O(N log(Sum - Max)) approach."),
            ("B", "Dynamic programming with $O(N^3)$ memoization matrix.", False, "Incorrect: Inefficient and unnecessary when binary search on monotone space works."),
            ("C", "Breadth-First Search on a state transition graph.", False, "Incorrect: BFS would blow up the state space exponentially."),
            ("D", "Sorting the package array in ascending order before shipping.", False, "Incorrect: Problem requires maintaining conveyor belt sequence.")
        ]
    },

    # -------------------------------------------------------------
    # Topic 63: Freshworks-Style Placement Assessment (needs 10+ -> currently 5)
    # -------------------------------------------------------------
    {
        "topic_id": 63, "difficulty": "medium",
        "question_text": "Freshworks Campus Assessment: A customer support ticketing dashboard receives incoming tickets. Each ticket has a priority from 1 to 5. Which data structure guarantees $O(1)$ retrieval of the highest priority ticket and $O(\\log N)$ insertion of new tickets?",
        "explanation": "A Max-Heap (or Priority Queue) allows $O(1)$ inspection of the maximum priority ticket at the root, and $O(\\log N)$ insertion and extraction of tickets via heapify bubbling operations.",
        "options": [
            ("A", "Max-Heap (Priority Queue)", True, "Correct: Peak max priority in O(1), insert/extract in O(log N)."),
            ("B", "Standard FIFO Queue", False, "Incorrect: FIFO ignores ticket priority weights."),
            ("C", "Unsorted Linked List", False, "Incorrect: Finding the max priority ticket would take O(N) scan."),
            ("D", "Hash Map with ticket ID keys", False, "Incorrect: Hash map does not maintain order or max priority.")
        ]
    },
    {
        "topic_id": 63, "difficulty": "medium",
        "question_text": "Freshworks Quantitative OA: A sales rep makes a phone call to a client every 15 minutes, while an email automation runs every 25 minutes. If both trigger simultaneously at 9:00 AM, at what time will they next trigger at the exact same moment?",
        "explanation": "We find the Least Common Multiple (LCM) of 15 and 25 minutes.\n$15 = 3 \\times 5$\n$25 = 5^2$\n$\\text{LCM}(15, 25) = 3 \\times 5^2 = 75$ minutes = 1 hour and 15 minutes.\n9:00 AM + 1 hr 15 min = 10:15 AM.",
        "options": [
            ("A", "10:15 AM", True, "Correct: LCM(15, 25) = 75 minutes; 9:00 AM + 75 min = 10:15 AM."),
            ("B", "10:30 AM", False, "Incorrect: 90 minutes is not a multiple of 25."),
            ("C", "10:00 AM", False, "Incorrect: 60 minutes is not a multiple of 25."),
            ("D", "11:15 AM", False, "Incorrect: 135 minutes is not the first occurrence.")
        ]
    },

    # -------------------------------------------------------------
    # Topic 64: Flipkart-Style Placement Assessment (needs 10+ -> currently 5)
    # -------------------------------------------------------------
    {
        "topic_id": 64, "difficulty": "medium",
        "question_text": "Flipkart Grid Assessment: An e-commerce warehouse has an array of delivery times for packages. A delivery partner wants to deliver to the maximum number of houses in a single contiguous stretch such that the total delivery time does not exceed $K$ minutes. What technique solves this in $O(N)$ time?",
        "explanation": "Because all delivery times are non-negative, the window sum is monotonic. A Sliding Window (Two Pointers) technique maintains a running sum, expanding the right pointer and contracting the left pointer when the sum exceeds $K$, tracking the maximum window width in $O(N)$ time and $O(1)$ space.",
        "options": [
            ("A", "Sliding Window with two pointers expanding right and contracting left.", True, "Correct: O(N) time with O(1) space."),
            ("B", "Nested loops computing all possible subarray sums in $O(N^2)$.", False, "Incorrect: Quadratic time is too slow and causes TLE."),
            ("C", "Dijkstra's shortest path algorithm.", False, "Incorrect: Not a graph path-finding problem."),
            ("D", "Merge Sort on the array.", False, "Incorrect: Sorting destroys the contiguous house stretch order.")
        ]
    },
    {
        "topic_id": 64, "difficulty": "hard",
        "question_text": "Flipkart Machine Coding: What design pattern is most appropriate when implementing a dynamic discounts pricing engine (e.g. FestivalDiscount, CouponDiscount, FirstTimeBuyerDiscount) that can be mixed and applied dynamically to an order total?",
        "explanation": "The Strategy Pattern (or Decorator Pattern) allows discount algorithms to be defined as interchangeable strategies or layered cumulatively on top of an order, following the Open/Closed Principle without modifying core order processing logic.",
        "options": [
            ("A", "Strategy Pattern (or Decorator Pattern for cumulative layered discounts).", True, "Correct: Encapsulates discount rules and enables runtime switching."),
            ("B", "Singleton Pattern", False, "Incorrect: Singleton does not facilitate polymorphic algorithm substitution."),
            ("C", "Flyweight Pattern", False, "Incorrect: Flyweight minimizes memory sharing, unrelated to discount calculation logic."),
            ("D", "Proxy Pattern", False, "Incorrect: Proxy controls access rather than computing prices.")
        ]
    },

    # -------------------------------------------------------------
    # Topic 65: PayPal-Style Placement Assessment (needs 10+ -> currently 5)
    # -------------------------------------------------------------
    {
        "topic_id": 65, "difficulty": "medium",
        "question_text": "PayPal Online Assessment: In financial systems, why is it dangerous to use 64-bit IEEE 754 floating-point numbers (`double` or `float`) for monetary transactions?",
        "explanation": "Binary floating-point types cannot represent many decimal fractions (like 0.1 or 0.01) exactly, leading to cumulative rounding errors (e.g., `0.1 + 0.2 = 0.30000000000000004`). Financial systems must use arbitrary-precision decimal representations (like Java's `BigDecimal` or Python's `decimal.Decimal`) or store integer cents.",
        "options": [
            ("A", "Binary floating-point cannot represent base-10 decimals precisely, accumulating rounding discrepancies in balance calculations.", True, "Correct: Financial systems mandate BigDecimal or integer cents."),
            ("B", "Float values cannot be stored in SQL database columns.", False, "Incorrect: SQL supports FLOAT and DOUBLE PRECISION."),
            ("C", "Float numbers can only represent positive amounts, not refunds.", False, "Incorrect: Floating-point supports signed values."),
            ("D", "Float numbers consume 10 times more memory than strings.", False, "Incorrect: Doubles are only 8 bytes.")
        ]
    },
    {
        "topic_id": 65, "difficulty": "hard",
        "question_text": "PayPal Engineering Question: When designing a payment processing webhook, how should the receiver endpoint ensure idempotency against duplicate delivery attempts from payment gateways?",
        "explanation": "Payment gateways include a unique `Idempotency-Key` or `event_id` in webhook payloads. The receiver checks whether the `event_id` has already been processed in a distributed cache (e.g. Redis) or database with a unique constraint. If already processed, it returns HTTP 200 OK without re-crediting the account.",
        "options": [
            ("A", "Verify a unique idempotency key or event ID against a processed transactions store before executing payment updates.", True, "Correct: Prevents double-charging and duplicate balance credits."),
            ("B", "Reject all HTTP POST requests and accept only GET requests.", False, "Incorrect: Webhooks deliver state changes via POST payloads."),
            ("C", "Restart the web server after every incoming transaction.", False, "Incorrect: Catastrophic anti-pattern."),
            ("D", "Store the transaction in browser local storage.", False, "Incorrect: Webhooks communicate server-to-server, with no browser involved.")
        ]
    }
]

def seed_pack7():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    now_iso = datetime.now(timezone.utc).isoformat()

    added_q = 0
    added_opt = 0

    for item in QUESTIONS:
        cursor.execute("SELECT id FROM questions WHERE question_text = ?", (item["question_text"],))
        if cursor.fetchone():
            continue

        cursor.execute("""
            INSERT INTO questions (
                topic_id, question_type, difficulty, question_text,
                explanation, step_by_step_reasoning, practical_example,
                common_mistake, learning_tip, is_published, created_at
            ) VALUES (?, 'mcq', ?, ?, ?, ?, ?, ?, ?, 1, ?)
        """, (
            item["topic_id"],
            item["difficulty"],
            item["question_text"],
            item["explanation"],
            "Apply rigorous computational and engineering reasoning.",
            "Standard high-volume placement benchmark.",
            "Falling for deceptive distractor options or misreading constraints.",
            "Break down problem premises step by step.",
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

    print(f"Pack 7: Successfully added {added_q} questions and {added_opt} options.")

if __name__ == "__main__":
    seed_pack7()

