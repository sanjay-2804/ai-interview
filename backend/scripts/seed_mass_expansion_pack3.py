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

PACK3 = [
    # ------------------ PERCENTAGES & PROFIT-LOSS ------------------
    {
        "topic_slug": "percentages-profit-loss",
        "type": "technical_mcq",
        "difficulty": "intermediate",
        "text": "A shopkeeper marks an article 40% above the cost price and allows a discount of 25% on the marked price. If he makes a profit of Rs. 140, what is the cost price of the article?",
        "explanation": "Let Cost Price (CP) = 100x. Marked Price (MP) = 140x. Selling Price (SP) after 25% discount = 140x * 0.75 = 105x. Profit = 105x - 100x = 5x. Given 5x = 140 => x = 28. CP = 100x = Rs. 2,800.",
        "steps": "1. Let CP = 100.\n2. MP = 140.\n3. SP = 140 - (25% of 140) = 140 - 35 = 105.\n4. Net profit percentage = 5%.\n5. If 5% = Rs. 140, then 100% = (140 / 5) * 100 = Rs. 2,800.",
        "example": "Standard placement markup and discount problem.",
        "mistake": "Calculating the 25% discount on the cost price instead of marked price.",
        "tip": "Discount is always calculated on Marked Price; Profit or Loss is always calculated on Cost Price.",
        "options": [
            ("A", "Rs. 2,800", True, "Correct: 5% net gain = Rs. 140 => Cost Price = Rs. 2,800."),
            ("B", "Rs. 2,400", False, "Incorrect calculation of markup."),
            ("C", "Rs. 3,200", False, "Overestimated markup multiplier."),
            ("D", "Rs. 3,500", False, "Computed on selling price directly.")
        ]
    },
    {
        "topic_slug": "percentages-profit-loss",
        "type": "technical_mcq",
        "difficulty": "intermediate",
        "text": "By selling 33 meters of cloth, a merchant gains the selling price of 11 meters. Find the merchant's gain percentage.",
        "explanation": "Let SP of 1 meter = Re. 1. Total SP of 33 meters = Rs. 33. Profit = SP of 11 meters = Rs. 11. Cost Price (CP) = SP - Profit = 33 - 11 = Rs. 22. Gain % = (Profit / CP) * 100 = (11 / 22) * 100 = 50%.",
        "steps": "1. Profit = SP(33) - CP(33) = SP(11).\n2. CP(33) = SP(33) - SP(11) = SP(22).\n3. Profit % = [Profit / CP] * 100 = [11 / 22] * 100 = 50%.",
        "example": "Classic campus quantitative aptitude problem.",
        "mistake": "Calculating gain % as (11 / 33) * 100 = 33.33% by dividing by SP instead of CP.",
        "tip": "Always divide by the Cost Price to calculate profit percentage, never by Selling Price.",
        "options": [
            ("A", "50%", True, "Correct: Gain percentage is based on Cost Price (CP = 22, Profit = 11 => 50%)."),
            ("B", "33.33%", False, "Common error: Divided by selling price instead of cost price."),
            ("C", "25%", False, "Incorrect formula."),
            ("D", "40%", False, "Arithmetic mistake.")
        ]
    },

    # ------------------ TIME, SPEED & DISTANCE ------------------
    {
        "topic_slug": "time-speed-distance",
        "type": "technical_mcq",
        "difficulty": "intermediate",
        "text": "Two trains running in opposite directions on parallel tracks cross a pole in 27 seconds and 17 seconds respectively, and they cross each other completely in 23 seconds. What is the ratio of their speeds?",
        "explanation": "Let speeds be u and v. Length of train 1 = 27u, length of train 2 = 17v. Total distance = 27u + 17v. Relative speed in opposite directions = u + v. Time = (27u + 17v) / (u + v) = 23. 27u + 17v = 23u + 23v => 4u = 6v => u / v = 3 / 2.",
        "steps": "1. Distance = Speed * Time.\n2. L1 = 27u, L2 = 17v.\n3. Relative speed = u + v.\n4. (27u + 17v) / (u + v) = 23.\n5. 4u = 6v => u:v = 3:2.",
        "example": "Using alligation: 27 and 17 with mean 23 gives (23 - 17) : (27 - 23) = 6 : 4 = 3 : 2.",
        "mistake": "Subtracting speeds in opposite directions instead of adding them.",
        "tip": "Opposite directions: Add speeds (u + v); Same direction: Subtract speeds (u - v).",
        "options": [
            ("A", "3 : 2", True, "Correct: 4u = 6v simplifies to ratio 3 : 2."),
            ("B", "2 : 3", False, "Inverted ratio."),
            ("C", "5 : 4", False, "Incorrect alligation difference."),
            ("D", "4 : 3", False, "Arithmetic error.")
        ]
    },
    {
        "topic_slug": "time-speed-distance",
        "type": "technical_mcq",
        "difficulty": "advanced",
        "text": "A man walks at 4 km/h and reaches his office 10 minutes late. Next day, he walks at 5 km/h and reaches his office 5 minutes early. What is the distance between his home and his office?",
        "explanation": "Let distance be D km. Time difference = 10 min late to 5 min early = 15 minutes = 1/4 hour. D/4 - D/5 = 1/4 => D/20 = 1/4 => D = 5 km.",
        "steps": "1. Total time difference = 10 + 5 = 15 minutes = 15/60 = 1/4 hour.\n2. Equation: D/4 - D/5 = 1/4.\n3. (5D - 4D) / 20 = 1/4 => D/20 = 1/4.\n4. D = 5 km.",
        "example": "Formula: Distance = (S1 * S2 / |S1 - S2|) * (Total Time Difference). (4 * 5 / 1) * (15/60) = 20 * (1/4) = 5 km.",
        "mistake": "Subtracting the late and early times (10 - 5 = 5 min). Late and early are on opposite sides of schedule, so add them (10 + 5 = 15 min).",
        "tip": "Late + Early: Add times; Late + Late or Early + Early: Subtract times.",
        "options": [
            ("A", "5 km", True, "Correct: (4 * 5 / 1) * (15/60) = 5 km."),
            ("B", "4 km", False, "Result if time difference was miscalculated as 5 minutes."),
            ("C", "6.25 km", False, "Multiplied by incorrect speed difference."),
            ("D", "7.5 km", False, "Formula applied with inverse speeds.")
        ]
    },

    # ------------------ PERMUTATIONS & PROBABILITY ------------------
    {
        "topic_slug": "permutations-probability",
        "type": "technical_mcq",
        "difficulty": "intermediate",
        "text": "In how many different ways can the letters of the word 'CORPORATION' be arranged so that the vowels always come together?",
        "explanation": "In 'CORPORATION': Total 11 letters. Vowels are O, O, A, I, O (5 vowels: 3 O's, 1 A, 1 I). Consonants are C, R, P, R, T, N (6 consonants: 2 R's). Treat the 5 vowels as 1 single block. Total units to arrange = 6 consonants + 1 block = 7 units with 2 R's: 7! / 2! = 2,520 ways. Inside the vowel block, 5 vowels with 3 O's: 5! / 3! = 20 ways. Total arrangements = 2,520 * 20 = 50,400.",
        "steps": "1. Vowels = O, O, A, I, O (5 vowels, with 3 identical O's).\n2. Consonants = C, R, P, R, T, N (6 consonants, with 2 identical R's).\n3. Units = 6 + 1 = 7. Ways = 7! / 2! = 2,520.\n4. Internal vowel arrangements = 5! / 3! = 20.\n5. Total ways = 2,520 * 20 = 50,400.",
        "example": "Grouping/block method for permutation problems.",
        "mistake": "Forgetting to divide by repeated letters (2! for R's and 3! for O's).",
        "tip": "Always divide by the factorials of identical repeated letters to eliminate duplicate permutations.",
        "options": [
            ("A", "50,400", True, "Correct: (7! / 2!) * (5! / 3!) = 2,520 * 20 = 50,400."),
            ("B", "25,200", False, "Forgot to divide by 2! for R's."),
            ("C", "42,000", False, "Arithmetic error."),
            ("D", "5,040", False, "Missed the internal vowel permutation multiplier.")
        ]
    },
    {
        "topic_slug": "permutations-probability",
        "type": "technical_mcq",
        "difficulty": "intermediate",
        "text": "Two fair six-sided dice are rolled simultaneously. What is the probability that the sum of the numbers appearing on top is a prime number?",
        "explanation": "Total possible outcomes = 6 * 6 = 36. Prime sums possible between 2 and 12 are {2, 3, 5, 7, 11}. Sum=2: (1,1) [1]. Sum=3: (1,2),(2,1) [2]. Sum=5: (1,4),(2,3),(3,2),(4,1) [4]. Sum=7: (1,6),(2,5),(3,4),(4,3),(5,2),(6,1) [6]. Sum=11: (5,6),(6,5) [2]. Total favorable = 1 + 2 + 4 + 6 + 2 = 15. Probability = 15 / 36 = 5 / 12.",
        "steps": "1. Total outcomes = 36.\n2. Prime sums: 2, 3, 5, 7, 11.\n3. Count pairs for each: 1 + 2 + 4 + 6 + 2 = 15 favorable pairs.\n4. Probability = 15/36 = 5/12.",
        "example": "Standard dice probability distribution.",
        "mistake": "Counting 9 as a prime number (9 is composite: 3 * 3).",
        "tip": "Sum 7 is always the most frequent outcome when rolling two six-sided dice (6 out of 36).",
        "options": [
            ("A", "5 / 12", True, "Correct: 15 favorable outcomes / 36 total = 5 / 12."),
            ("B", "7 / 18", False, "Missed sum=11 outcomes."),
            ("C", "1 / 2", False, "Counted composite sums."),
            ("D", "13 / 36", False, "Omitted sum=2.")
        ]
    },

    # ------------------ OBJECT-ORIENTED PROGRAMMING (OOP) ------------------
    {
        "topic_slug": "oop",
        "type": "technical_mcq",
        "difficulty": "intermediate",
        "text": "What is the Liskov Substitution Principle (LSP) in SOLID object-oriented design?",
        "explanation": "LSP states that objects of a superclass should be replaceable with objects of a subclass without affecting the correctness or expected behavior of the program. Subtypes must honor the behavioral contracts and invariants established by their parent types.",
        "steps": "1. Superclass T defines behavior and invariants.\n2. Subclass S extends T.\n3. Any function expecting T must work correctly when passed an instance of S.\n4. Classic violation: Square subclassing Rectangle where setWidth() changes height, breaking area calculations.",
        "example": "If Bird has fly(), Penguin subclassing Bird and throwing CannotFlyException violates LSP.",
        "mistake": "Thinking LSP just means inheritance compiles. It requires behavioral compatibility.",
        "tip": "Favor composition over inheritance when subclass cannot fulfill parent contract.",
        "options": [
            ("A", "Subtypes must be substitutable for their base types without altering program correctness", True, "Correct: Subclasses must fulfill the contract and invariants of base classes."),
            ("B", "Every class must have only one public method", False, "This confuses LSP with Single Responsibility."),
            ("C", "All objects must inherit from a single god class", False, "God objects are an antipattern."),
            ("D", "Classes cannot contain private variables", False, "Encapsulation requires private variables.")
        ]
    },
    {
        "topic_slug": "oop",
        "type": "technical_mcq",
        "difficulty": "intermediate",
        "text": "What design pattern decouples the abstraction from its implementation so that both can vary independently?",
        "explanation": "The Bridge Pattern decouples an abstraction from its implementation by replacing class inheritance with object composition, allowing client interfaces and concrete platform implementations to evolve in separate class hierarchies.",
        "steps": "1. Abstraction defines the high-level control logic.\n2. Implementor defines the platform-specific primitive operations.\n3. Abstraction holds a reference to Implementor (the Bridge).\n4. Prevents Cartesian product class explosion (e.g., WindowsCircle, MacCircle, WindowsSquare, MacSquare).",
        "example": "GUI toolkits separating Shape (Circle, Square) from DrawingAPI (DirectX, OpenGL).",
        "mistake": "Confusing Bridge with Adapter. Adapter makes unrelated interfaces work together after design; Bridge separates abstraction upfront.",
        "tip": "Bridge = Upfront structural decoupling; Adapter = Retroactive interface conversion.",
        "options": [
            ("A", "Bridge Pattern", True, "Correct: Uses composition over inheritance to decouple abstraction from implementation."),
            ("B", "Singleton Pattern", False, "Singleton enforces a single instance, not abstraction decoupling."),
            ("C", "Observer Pattern", False, "Observer is a publish-subscribe behavioral event pattern."),
            ("D", "Memento Pattern", False, "Memento is for state snapshot and undo operations.")
        ]
    },

    # ------------------ SYSTEM DESIGN & CLOUD ------------------
    {
        "topic_slug": "system-design-cloud",
        "type": "technical_mcq",
        "difficulty": "advanced",
        "text": "What is the Circuit Breaker Pattern in distributed microservices architecture?",
        "explanation": "The Circuit Breaker pattern prevents an application from repeatedly attempting to execute an operation that is likely to fail (such as a slow or dead third-party service). When failures exceed a threshold, the circuit trips to 'Open', failing fast immediately and allowing the downstream system time to recover before transitioning to 'Half-Open'.",
        "steps": "1. Closed State: Normal operation. Requests pass through.\n2. Failure threshold reached (e.g. 50% timeouts): Circuit transitions to Open.\n3. Open State: All calls fail fast immediately or return fallback responses without network calls.\n4. Timeout expires: Transitions to Half-Open. Lets small probe traffic through.\n5. If probes succeed: Circuit resets to Closed; if probes fail: resets to Open.",
        "example": "Netflix Hystrix and Resilience4j protecting checkout services from crashing when recommendations service times out.",
        "mistake": "Confusing Circuit Breaker with Retry. Retries hammer a failing system; Circuit Breaker shields it.",
        "tip": "Pair Circuit Breakers with exponential backoff and jittered retries.",
        "options": [
            ("A", "Fails fast when downstream dependencies fail, shielding services from cascade failures and allowing recovery", True, "Correct: Transitions between Closed, Open, and Half-Open states to prevent cascading microservice outages."),
            ("B", "Physically cuts server electrical wiring during high voltage spikes", False, "Software pattern, not an electrical hardware fuse."),
            ("C", "Compresses JSON into binary Protobuf format", False, "Serialization format, not fault tolerance."),
            ("D", "Automatically scales Kubernetes pods to 1000 replicas", False, "Horizontal Pod Autoscaling (HPA) handles autoscaling.")
        ]
    },
    {
        "topic_slug": "system-design-cloud",
        "type": "technical_mcq",
        "difficulty": "advanced",
        "text": "In distributed caching systems, what is the 'Cache-Aside' (Lazy Loading) pattern?",
        "explanation": "In Cache-Aside, the application code directly coordinates between the cache and database: (1) Check cache. If hit, return data. (2) If miss, read from DB, write into cache with TTL, and return data. (3) On update, mutate DB and invalidate/evict the cache key.",
        "steps": "1. Client requests data.\n2. App queries Redis (Cache).\n3. Cache Miss: App queries MySQL (DB).\n4. App populates Redis with retrieved record + TTL.\n5. App returns data to client.\n6. Update: App writes to MySQL, evicts key from Redis.",
        "example": "Standard web application caching pattern with Redis/Memcached.",
        "mistake": "Thinking the cache automatically queries the database in Cache-Aside. That is 'Read-Through' caching.",
        "tip": "Cache-Aside gives developers full control over cache eviction and TTL management.",
        "options": [
            ("A", "Application checks cache first, queries DB on miss, writes result back to cache, and evicts cache on data updates", True, "Correct: Application manages both cache lookups and DB sync."),
            ("B", "Cache writes all updates directly to tape backup drives", False, "Not an archival tape pattern."),
            ("C", "Database completely disables all memory caches", False, "Database buffer pools continue operating independently."),
            ("D", "Cache only stores user login passwords in plain text", False, "Unsafe and unrelated.")
        ]
    }
]

print(f"Adding {len(PACK3)} high-yield questions to database...")

added = 0
for q in PACK3:
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

print(f"Successfully added {added} questions and {added * 4} options to interviewai.db!")

