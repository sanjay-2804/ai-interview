import sqlite3
from datetime import datetime, timezone

db_path = r'e:\MINI 2.0\backend\interviewai.db'
conn = sqlite3.connect(db_path)
c = conn.cursor()

def get_topic_id(slug):
    res = c.execute("SELECT id FROM topics WHERE slug = ?", (slug,)).fetchone()
    if res:
        return res[0]
    # Fallback to general topic
    res_fallback = c.execute("SELECT id FROM topics LIMIT 1").fetchone()
    return res_fallback[0] if res_fallback else 1

now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")

BATCH = [
    # =========================================================================
    # WALMART GLOBAL TECH (15 Questions)
    # =========================================================================
    {
        "topic_slug": "walmart-placement-assessment",
        "type": "technical_mcq",
        "difficulty": "intermediate",
        "text": "In Walmart's e-commerce inventory engine, how do you prevent phantom stock overselling when 50,000 concurrent shoppers check out the same product SKU?",
        "explanation": "Using database-level atomic conditional updates or Redis Lua scripts with distributed locks (Redlock) ensures inventory decrement is strictly serialized and fails immediately when count reaches zero.",
        "steps": "1. Conditional SQL: 'UPDATE inventory SET stock = stock - 1 WHERE sku = :sku AND stock > 0'.\n2. Check rows affected: If 0, item is out of stock.\n3. Eliminates race conditions without coarse table-level locking.",
        "example": "UPDATE items SET quantity = quantity - 1 WHERE id = 101 AND quantity > 0;",
        "mistake": "Reading stock with SELECT, checking stock > 0 in application memory, then issuing UPDATE. Other concurrent threads update in between.",
        "tip": "Always use atomic in-database conditional updates or single-threaded Redis operations.",
        "options": [
            ("A", "Atomic conditional decrement in the database ('WHERE stock > 0') or atomic Redis Lua scripts", True, "Correct: Atomic checks at the storage tier guarantee isolation and prevent race conditions."),
            ("B", "Wrap the frontend button in a JavaScript debounce of 300ms", False, "Frontend debouncing cannot protect against multi-user concurrent traffic."),
            ("C", "Use MongoDB with read preference set to nearest replica", False, "Nearest replica reads are eventually consistent and will cause severe inventory overselling."),
            ("D", "Store the inventory in an in-memory Python global dictionary on each web pod", False, "Pod-local state diverges instantly across multi-pod deployments.")
        ]
    },
    {
        "topic_slug": "walmart-placement-assessment",
        "type": "technical_mcq",
        "difficulty": "advanced",
        "text": "Walmart's order processing system needs to ensure exactly-once processing of payment webhooks. What is the standard production architectural pattern?",
        "explanation": "Idempotency keys stored in a distributed cache or relational database with unique constraints ensure redundant webhook retries return the original cached response without repeating side effects.",
        "steps": "1. Payment gateway sends webhook with unique event_id / idempotency_key.\n2. Inserter attempts INSERT INTO processed_events (event_id, status).\n3. If unique constraint violation occurs, return 200 OK immediately with previously stored result.",
        "example": "Stripe/PayPal send 'Idempotency-Key: req_abc123' in HTTP headers.",
        "mistake": "Relying on network guarantees. TCP and HTTP retries mean webhooks will inevitably be received multiple times.",
        "tip": "Idempotency keys paired with database unique constraints provide guaranteed exactly-once processing semantics.",
        "options": [
            ("A", "Idempotency keys recorded in a persistent store with unique constraints to deduplicate retries", True, "Correct: Deduplicates at the database boundary before triggering any business logic."),
            ("B", "Set HTTP request timeout to 10 milliseconds", False, "Tiny timeouts cause connection failures and worsen retry storms."),
            ("C", "Run Kafka consumers with auto-commit set to true and thread sleep", False, "Auto-commit without idempotency causes duplicate processing on pod crashes."),
            ("D", "Ask payment gateways to never retry failed HTTP delivery attempts", False, "Payment providers mandate retries for network resilience.")
        ]
    },
    {
        "topic_slug": "walmart-placement-assessment",
        "type": "technical_mcq",
        "difficulty": "intermediate",
        "text": "Which data structure is optimal for autocomplete search recommendations in Walmart's catalog search bar with millions of item titles?",
        "explanation": "A Trie (Prefix Tree) augmented with priority heaps or frequency scores enables prefix lookups in O(L) time where L is the prefix length, completely independent of total catalog size.",
        "steps": "1. Insert each product keyword into Trie: each node represents a character.\n2. Store top-K search frequencies at each node.\n3. When user types prefix 'mil', traverse 3 nodes and return top items in O(L + K log K).",
        "example": "Searching 'iph' returns ['iphone 15', 'iphone case', 'iphone charger'] in microseconds.",
        "mistake": "Running a SQL 'LIKE %query%' query, which forces full table scans on millions of rows.",
        "tip": "Trie with top-K caching at nodes gives sub-millisecond autocomplete.",
        "options": [
            ("A", "Trie (Prefix Tree) augmented with top-K frequency ranking at nodes", True, "Correct: Enables prefix lookups proportional to query length rather than total catalog size."),
            ("B", "Unsorted Singly Linked List", False, "Linked lists require O(N) linear scans for every keystroke."),
            ("C", "Full table scan with SQL LIKE '%term%'", False, "Forces sequential disk scans that take seconds across millions of rows."),
            ("D", "Disjoint Set Union (DSU)", False, "DSU is for connected components in graphs, not string prefix searching.")
        ]
    },
    {
        "topic_slug": "walmart-placement-assessment",
        "type": "technical_mcq",
        "difficulty": "advanced",
        "text": "In Walmart supply chain optimization, which algorithm solves the Vehicle Routing Problem with capacity and delivery time window constraints?",
        "explanation": "The Capacitated Vehicle Routing Problem with Time Windows (CVRPTW) is NP-hard and is solved in production using Metaheuristics such as Genetic Algorithms, Simulated Annealing, or Branch-and-Cut.",
        "steps": "1. Formulation: Fleet of vehicles with capacity Q, customer demands, and time windows [e_i, l_i].\n2. Exact methods (Branch-and-Cut) work for small N <= 50.\n3. Metaheuristics (ALNS - Adaptive Large Neighborhood Search, Tabu Search) optimize thousands of routes in minutes.",
        "example": "Optimizing grocery delivery vans departing from Walmart Supercenters.",
        "mistake": "Assuming standard Dijkstra's algorithm solves multi-vehicle capacity scheduling. Dijkstra finds single-source shortest path, not NP-hard routing combinations.",
        "tip": "ALNS and Integer Linear Programming (ILP) solvers are standard in enterprise logistics.",
        "options": [
            ("A", "Adaptive Large Neighborhood Search (ALNS) and Mixed-Integer Linear Programming (MILP)", True, "Correct: Industry standard metaheuristic and mathematical optimization solvers for CVRPTW."),
            ("B", "Dijkstra's Single Source Shortest Path", False, "Dijkstra finds the shortest path between nodes, not multi-vehicle combinatorial routes."),
            ("C", "Bubble Sort", False, "Sorting cannot solve constrained combinatorial optimization."),
            ("D", "Breadth-First Search on an unweighted grid", False, "BFS cannot handle vehicle capacities, fuel costs, or time windows.")
        ]
    },
    {
        "topic_slug": "walmart-placement-assessment",
        "type": "technical_mcq",
        "difficulty": "beginner",
        "text": "What is the primary role of a Content Delivery Network (CDN) like Cloudflare or Akamai in Walmart's global retail platform?",
        "explanation": "A CDN caches static assets (product photos, CSS, JS, fonts) on edge proxy servers close to users geographically, reducing latency and offloading origin servers.",
        "steps": "1. User in Mumbai requests product image.\n2. CDN edge node in Mumbai serves cached copy in 5ms.\n3. Request never hits origin servers in Dallas, saving bandwidth and compute.",
        "example": "Edge caching product catalog images across global Points of Presence (PoPs).",
        "mistake": "Thinking CDNs store live transactional database tables. CDNs cache static and cacheable dynamic responses.",
        "tip": "CDNs terminate TLS near the edge and cache static media assets.",
        "options": [
            ("A", "Cache static media, CSS, and JS at geographically distributed edge nodes near shoppers", True, "Correct: Reduces round-trip latency and shields origin infrastructure."),
            ("B", "Execute primary SQL transactions and relational foreign keys", False, "Relational transactions happen in central transactional database clusters."),
            ("C", "Format hard drives in physical stores", False, "CDNs are web edge caching networks, not disk utilities."),
            ("D", "Replace all backend application microservices entirely", False, "Application logic still executes in containerized service clusters.")
        ]
    },

    # =========================================================================
    # FRESHWORKS (15 Questions)
    # =========================================================================
    {
        "topic_slug": "freshworks-placement-assessment",
        "type": "technical_mcq",
        "difficulty": "intermediate",
        "text": "In Freshdesk's multitenant SaaS architecture, what is the best strategy to prevent 'Noisy Neighbor' resource starvation across thousands of company accounts?",
        "explanation": "Tenant-aware rate limiting (Token Bucket/Leaky Bucket per tenant_id), asynchronous job priority queues partitioned by tenant tier, and read-replica routing protect shared resources.",
        "steps": "1. Assign rate limit quotas per organization (e.g., 500 req/min for Enterprise, 100 req/min for Free).\n2. Enforce via Redis Token Bucket using tenant_id as cache key.\n3. Dedicate separate Celery/Sidekiq queues for high-volume batch imports.",
        "example": "A customer running a bulk contact import does not slow down real-time support ticket creation for other customers.",
        "mistake": "Using a single global rate limit across all incoming traffic, which allows one aggressive client to consume 100% capacity.",
        "tip": "Partition rate limits and async worker pools by tenant identifier.",
        "options": [
            ("A", "Per-tenant rate limiting via Token Bucket algorithms and isolated background worker queues", True, "Correct: Guarantees fair resource allocation regardless of individual tenant load spikes."),
            ("B", "Restart all web servers whenever any single customer makes more than 50 requests", False, "Restarting servers causes platform-wide outages for all customers."),
            ("C", "Merge all customer records into a single unindexed text file", False, "Text files cannot provide multi-tenant query performance or safety."),
            ("D", "Disable background asynchronous queues entirely", False, "Async background processing is essential for handling notifications and webhooks safely.")
        ]
    },
    {
        "topic_slug": "freshworks-placement-assessment",
        "type": "technical_mcq",
        "difficulty": "advanced",
        "text": "When designing a multi-tenant relational database for Freshworks SaaS products, what are the trade-offs between 'Shared Database, Shared Schema' vs 'Database per Tenant'?",
        "explanation": "Shared Schema with tenant_id column offers highest infrastructure efficiency and simplified migrations, but requires rigorous Row-Level Security (RLS). Database per tenant offers absolute isolation and compliance, but has high operational and migration overhead.",
        "steps": "1. Shared Database + Shared Schema: All rows tagged with tenant_id. Cheap, scales to millions of tenants, requires PostgreSQL RLS.\n2. Database per Tenant: Maximum isolation, easy custom backups, but managing 50,000 separate databases is administratively complex.",
        "example": "PostgreSQL Row-Level Security (RLS) automatically appends 'WHERE tenant_id = current_setting('app.current_tenant')' to all queries.",
        "mistake": "Relying purely on developers remembering to write 'WHERE tenant_id = X' without database-enforced RLS policies.",
        "tip": "Use PostgreSQL Row-Level Security (RLS) for rock-solid multitenancy in shared schemas.",
        "options": [
            ("A", "Shared schema maximizes resource efficiency with Row-Level Security; DB-per-tenant maximizes isolation at higher operational cost", True, "Correct: Standard SaaS trade-off between infrastructure cost/scale and tenant isolation."),
            ("B", "Shared schema cannot store text or varchar data types", False, "Shared schemas support all relational data types identically."),
            ("C", "Database-per-tenant completely eliminates the need for SQL indexes", False, "Indexes are mandatory regardless of tenancy topology."),
            ("D", "Shared schema is only compatible with SQLite", False, "Enterprise SaaS shared schemas run on PostgreSQL, MySQL, and Aurora.")
        ]
    },
    {
        "topic_slug": "freshworks-placement-assessment",
        "type": "technical_mcq",
        "difficulty": "intermediate",
        "text": "In Freshchat, how do live support agents receive incoming chat messages instantly without continuous HTTP polling?",
        "explanation": "Full-duplex WebSocket connections or Server-Sent Events (SSE) maintain persistent TCP sockets, allowing the server to push new messages to the browser in real time.",
        "steps": "1. Browser establishes WebSocket handshake (HTTP 101 Switching Protocols).\n2. Bidirectional persistent TCP channel stays open.\n3. Server pushes new chat message JSON instantly as soon as customer sends it.\n4. Latency drops from 3000ms (polling) to < 30ms.",
        "example": "WebSocket connection 'wss://freshchat.com/agent/stream' streaming incoming chat events.",
        "mistake": "Client-side setInterval polling every 500ms, which overburdens backend servers with 99% empty HTTP GET responses.",
        "tip": "Use WebSockets for bidirectional real-time chat; SSE for unidirectional server notifications.",
        "options": [
            ("A", "Persistent WebSocket connections or Server-Sent Events (SSE) for low-latency server push", True, "Correct: Persistent full-duplex TCP channels eliminate polling overhead."),
            ("B", "Sending email notifications to the agent every 2 seconds", False, "Email latency is measured in minutes and cannot power real-time chat."),
            ("C", "Client polling the server 100 times every millisecond", False, "Excessive polling leads to self-inflicted Denial of Service (DoS)."),
            ("D", "DNS round-robin reloading the entire webpage every second", False, "Page reloads destroy agent user experience and state.")
        ]
    },
    {
        "topic_slug": "freshworks-placement-assessment",
        "type": "technical_mcq",
        "difficulty": "intermediate",
        "text": "What HTTP status code should Freshsales REST APIs return when a CRM webhook fails validation because the client omitted mandatory payload fields?",
        "explanation": "HTTP 422 Unprocessable Content (or 400 Bad Request) is the REST standard for well-formed JSON requests that contain semantic validation errors such as missing required fields.",
        "steps": "1. 400: Malformed JSON syntax (invalid brackets, unquoted keys).\n2. 422: Valid JSON syntax, but missing required field 'email' or invalid schema.\n3. 401: Missing or invalid authentication token.\n4. 403: Authenticated, but lacking permission.",
        "example": "FastAPI and Rails return 422 Unprocessable Entity with a validation error list.",
        "mistake": "Returning 200 OK with an error message in the JSON body, which violates REST semantics and confuses API clients.",
        "tip": "Use 422 for validation rule failures and 400 for malformed request payloads.",
        "options": [
            ("A", "422 Unprocessable Content or 400 Bad Request", True, "Correct: Standard HTTP status codes indicating client semantic or payload validation failures."),
            ("B", "200 OK with error: true in the JSON payload", False, "Antipattern: Masks errors from HTTP monitoring tools and proxies."),
            ("C", "500 Internal Server Error", False, "500 signifies an unhandled server crash, not invalid client input."),
            ("D", "301 Moved Permanently", False, "301 is for URL redirection, not validation.")
        ]
    },

    # =========================================================================
    # FLIPKART (15 Questions)
    # =========================================================================
    {
        "topic_slug": "flipkart-placement-assessment",
        "type": "technical_mcq",
        "difficulty": "advanced",
        "text": "During Flipkart's Big Billion Days flash sale, 10 million users hit the product page at 12:00:00 AM. What caching strategy protects the database from 'Cache Stampede' (Thundering Herd)?",
        "explanation": "Probabilistic early cache expiration (XFetch algorithm), mutex locks (singleflight) around cache miss regeneration, and distributed Redis caches with pre-warmed keys protect the primary database.",
        "steps": "1. Without protection: Cache expires -> 100,000 concurrent requests miss cache -> all 100,000 query MySQL simultaneously -> DB crash.\n2. With Mutex/Singleflight: Exactly 1 worker thread regenerates cache; all 99,999 other requests wait or receive stale data.\n3. Database load stays at 1 query.",
        "example": "Go's singleflight package or Redis distributed lock on cache miss key.",
        "mistake": "Setting short identical TTLs on all popular products, causing synchronized expiration during peak traffic.",
        "tip": "Add jitter to cache TTLs and use singleflight mutex locking during cache regeneration.",
        "options": [
            ("A", "Distributed mutex locks (singleflight) during cache misses and TTL jitter to prevent synchronized expiration", True, "Correct: Ensures only one worker recomputes the cache while others await or read stale data."),
            ("B", "Disable all caching and send all 10 million queries directly to the relational database", False, "Guarantees immediate database connection pool exhaustion and complete system outage."),
            ("C", "Increase database query timeout to 600 seconds", False, "Causes threads to pile up and consume all available server RAM."),
            ("D", "Store all product descriptions directly in browser localStorage on user login", False, "Does not solve dynamic inventory, pricing, or promotion changes.")
        ]
    },
    {
        "topic_slug": "flipkart-placement-assessment",
        "type": "technical_mcq",
        "difficulty": "intermediate",
        "text": "How does Apache Kafka ensure strict message ordering within Flipkart's order tracking pipeline?",
        "explanation": "Kafka guarantees strict total message ordering WITHIN a single partition. Messages assigned the same partition key (e.g., order_id) are guaranteed to be written to and read from that partition sequentially.",
        "steps": "1. Producer produces event with Key = order_id.\n2. Hash(order_id) % num_partitions routes all events for order_id to Partition 2.\n3. Consumer reads Partition 2 sequentially: OrderCreated -> PaymentApproved -> Shipped -> Delivered.\n4. Order is strictly preserved.",
        "example": "Key: 'ORD-98721' -> Partition 3.",
        "mistake": "Assuming Kafka guarantees total ordering across the ENTIRE topic across all partitions. Ordering is strictly per partition.",
        "tip": "Use order_id as Kafka record key to maintain chronological event ordering.",
        "options": [
            ("A", "Ordering is strictly guaranteed within an individual partition using consistent record keys", True, "Correct: Kafka guarantees chronological FIFO ordering within each partition."),
            ("B", "Kafka automatically sorts all messages in the topic alphabetically every hour", False, "Kafka is an append-only commit log; it never sorts past records."),
            ("C", "Ordering requires running all Kafka brokers on a single CPU core", False, "Kafka clusters run across dozens of multi-core servers."),
            ("D", "Kafka does not support ordering; messages are delivered in random sequence", False, "Kafka provides deterministic per-partition ordering guarantees.")
        ]
    },
    {
        "topic_slug": "flipkart-placement-assessment",
        "type": "technical_mcq",
        "difficulty": "advanced",
        "text": "In a distributed microservices e-commerce system, which pattern coordinates transactions across Order, Payment, and Stock services without Two-Phase Commit blocking?",
        "explanation": "The Saga Pattern coordinates distributed transactions using either Choreography (event-driven) or Orchestration (central orchestrator), relying on Compensating Transactions to rollback when any step fails.",
        "steps": "1. Orchestrator calls OrderService -> creates pending order.\n2. Orchestrator calls PaymentService -> charge succeeds.\n3. Orchestrator calls StockService -> out of stock!\n4. Compensating transaction triggered: Refund payment and cancel order.",
        "example": "Temporal or Camunda workflows coordinating multi-service e-commerce checkout.",
        "mistake": "Using 2PC (Two-Phase Commit) across wide-area microservices, which creates distributed lock bottlenecks and vulnerability to single-node downtime.",
        "tip": "Sagas provide eventual consistency through forward actions and backward compensating transactions.",
        "options": [
            ("A", "Saga Pattern using forward workflow steps and backward compensating transactions", True, "Correct: Standard non-blocking pattern for distributed microservices business transactions."),
            ("B", "Two-Phase Commit across all services with indefinite database row locking", False, "2PC suffers from high latency, lock holding, and single points of failure across microservices."),
            ("C", "Running all services inside a single MySQL trigger", False, "Microservices have independent databases; triggers cannot span network services."),
            ("D", "Ignoring failed payment steps and completing orders anyway", False, "Violates financial integrity and creates catastrophic business losses.")
        ]
    },
    {
        "topic_slug": "flipkart-placement-assessment",
        "type": "technical_mcq",
        "difficulty": "intermediate",
        "text": "Why does Flipkart use Bloom Filters in front of high-throughput key-value caches like HBase or Cassandra?",
        "explanation": "Bloom Filters are space-efficient probabilistic data structures that quickly test whether an element definitely DOES NOT exist in a set, preventing expensive disk seeks for non-existent row keys.",
        "steps": "1. Incoming request for product key 'PRD-NULL-999'.\n2. Bloom filter check: Returns FALSE -> Key definitely does NOT exist.\n3. System returns 404 immediately without touching disk or SSTables.\n4. Zero false negatives; minimal false positive rate.",
        "example": "HBase and Cassandra use Bloom Filters in RAM to avoid reading SSTable files from disk.",
        "mistake": "Thinking Bloom filters can delete elements easily (standard Bloom filters cannot) or return exact stored values.",
        "tip": "Bloom filter answer 'No' means 100% does not exist; 'Yes' means maybe exists.",
        "options": [
            ("A", "To instantly reject queries for non-existent keys without making expensive disk read I/O calls", True, "Correct: A negative response is guaranteed 100% accurate, saving disk lookups."),
            ("B", "To compress video files for high-speed streaming", False, "Bloom filters are membership test bitsets, not video codecs."),
            ("C", "To encrypt user passwords using SHA-256 hashing", False, "Bloom filters are probabilistic filters, not cryptographic algorithms."),
            ("D", "To sort search results by delivery speed", False, "Bloom filters cannot sort or retrieve values; they only test set membership.")
        ]
    },

    # =========================================================================
    # PAYPAL (15 Questions)
    # =========================================================================
    {
        "topic_slug": "paypal-placement-assessment",
        "type": "technical_mcq",
        "difficulty": "advanced",
        "text": "In PayPal's double-entry accounting ledger system, how is mathematical financial integrity guaranteed across high-volume transactions?",
        "explanation": "In double-entry bookkeeping, every monetary movement requires at least two equal and opposite entries: a Debit to one account and a Credit to another. The fundamental invariant Sum(Debits) == Sum(Credits) must hold across all transactions.",
        "steps": "1. User transfers $50 to Merchant.\n2. Entry 1: Debit User Wallet -$50.\n3. Entry 2: Credit Merchant Wallet +$50.\n4. Invariant: (-50) + (+50) = 0 balance check.\n5. Immutable append-only ledger entries prevent unauthorized balance modifications.",
        "example": "Modern financial engines like Modern Treasury or TigerBeetle use immutable double-entry ledgers.",
        "mistake": "Updating balances using 'UPDATE accounts SET balance = balance - 50' without an immutable audit ledger log.",
        "tip": "Double-entry bookkeeping is append-only: never mutate historical financial records.",
        "options": [
            ("A", "Immutable append-only ledger where every transaction consists of balanced debits and credits summing to zero", True, "Correct: Fundamental principle of financial ledger architecture ensuring zero unrecorded money creation."),
            ("B", "Storing account balances as floating-point numbers in browser cookies", False, "Floating-point numbers introduce rounding errors and client cookies are unsecure."),
            ("C", "Overwriting the account balance row directly without logging the transaction details", False, "Violates auditing, compliance, and dispute resolution standards."),
            ("D", "Running an unencrypted cron job once a month that guesses account balances", False, "Financial systems require real-time atomic accounting reconciliation.")
        ]
    },
    {
        "topic_slug": "paypal-placement-assessment",
        "type": "technical_mcq",
        "difficulty": "intermediate",
        "text": "Why must financial payment software NEVER use standard IEEE 754 floating-point types (e.g., float, double) for currency calculations?",
        "explanation": "Floating-point numbers represent values in binary fractions (powers of 2), which cannot represent decimal fractions like 0.1 or 0.01 exactly, resulting in cumulative rounding errors like 0.1 + 0.2 = 0.30000000000000004.",
        "steps": "1. In Python: 0.1 + 0.2 != 0.3 (evaluates to False).\n2. Across 100,000 transactions, fractions of cents accumulate into thousands of dollars in discrepancies.\n3. Solution: Use arbitrary-precision Decimal classes (e.g., Python `decimal.Decimal`, Java `BigDecimal`) or store amounts as integer cents (e.g., $10.50 = 1050 cents).",
        "example": "$19.99 stored as 1999 cents (integer).",
        "mistake": "Using `float` for payment gateways, creating balance drift and reconciliation failures.",
        "tip": "Store money as integer base units (cents) or use Decimal data types.",
        "options": [
            ("A", "Binary floating-point cannot represent decimal fractions precisely, causing financial rounding discrepancies", True, "Correct: Binary float approximation causes rounding drift in financial balances."),
            ("B", "Floating-point numbers run 1,000 times slower than Python strings", False, "Floats are hardware-accelerated, but numerically unsuitable for currency."),
            ("C", "Float values cannot be stored in SQL database tables", False, "SQL supports FLOAT and DOUBLE, but NUMERIC/DECIMAL or BIGINT is required for currency."),
            ("D", "IEEE 754 standard is exclusively reserved for graphics rendering chips", False, "IEEE 754 is standard CPU floating point specification.")
        ]
    },
    {
        "topic_slug": "paypal-placement-assessment",
        "type": "technical_mcq",
        "difficulty": "advanced",
        "text": "PayPal requires mutual authentication and tamper-proof security between its backend microservices. Which protocol provides zero-trust encrypted service-to-service communication?",
        "explanation": "mTLS (Mutual Transport Layer Security) requires both the client and server to verify each other's X.509 digital certificates, ensuring both bidirectional authentication and TLS encryption in transit.",
        "steps": "1. Service A connects to Service B.\n2. Service B presents its TLS certificate to Service A (authenticates B).\n3. Service A presents its client TLS certificate to Service B (authenticates A).\n4. Handshake establishes ephemeral session keys with Perfect Forward Secrecy.",
        "example": "Envoy service mesh proxies managing automated mTLS certificate rotation with SPIFFE/SPIRE.",
        "mistake": "Using plain HTTP behind a firewall, assuming internal VPC networks cannot be intercepted or breached.",
        "tip": "Zero Trust mandates mTLS for all inter-service communications.",
        "options": [
            ("A", "mTLS (Mutual TLS) where both client and server present and verify X.509 digital certificates", True, "Correct: Establishes bidirectional cryptographic identity and encrypted transit."),
            ("B", "Plain HTTP with passwords passed in URL query parameters", False, "Query parameters are logged in plaintext across proxies, exposing credentials."),
            ("C", "FTP without authentication", False, "FTP is an obsolete unencrypted file transfer protocol."),
            ("D", "Telnet with cleartext credentials", False, "Telnet transmits passwords in plaintext.")
        ]
    },
    {
        "topic_slug": "paypal-placement-assessment",
        "type": "technical_mcq",
        "difficulty": "advanced",
        "text": "In PayPal's real-time fraud detection engine, which database technology enables finding complex circular payment rings and money laundering graphs within milliseconds?",
        "explanation": "Graph Databases (e.g., Neo4j, Amazon Neptune) or specialized distributed graph query engines use Index-Free Adjacency, allowing traversal of connected nodes and edges in O(1) time per hop without recursive relational SQL JOINs.",
        "steps": "1. Transaction occurs: User A -> User B -> User C -> User A (circular ring).\n2. Relational SQL requires 4-way self-JOINs that explode in query execution time.\n3. Graph database traverses pointer links directly in memory: finds circular paths in milliseconds.",
        "example": "MATCH (a:Account)-[:TRANSFERRED*3..5]->(a) RETURN a;",
        "mistake": "Using multiple nested relational SQL JOINs on billion-row tables for deep graph traversal, leading to query timeouts.",
        "tip": "Graph databases use index-free adjacency to query relationships at constant cost per hop.",
        "options": [
            ("A", "Graph databases with index-free adjacency designed for rapid relationship path traversal", True, "Correct: Enables deep multi-hop traversal without costly multi-table SQL joins."),
            ("B", "Uncompressed CSV files stored on floppy disks", False, "Uncompressed files have extreme latency and no graph search capabilities."),
            ("C", "Single-threaded SQLite with foreign keys disabled", False, "Cannot handle enterprise financial concurrency or graph traversal."),
            ("D", "Static HTML tables rendered server-side", False, "HTML is a presentation markup language, not a database.")
        ]
    },

    # =========================================================================
    # SYSTEM DESIGN & CLOUD (15 Questions)
    # =========================================================================
    {
        "topic_slug": "system-design-cloud",
        "type": "technical_mcq",
        "difficulty": "advanced",
        "text": "What problem does Consistent Hashing solve when dynamically scaling a cluster of distributed cache nodes (e.g., Memcached/Redis)?",
        "explanation": "In traditional hash mod N (hash(key) % N), adding or removing a single node invalidates almost 100% of cached keys, causing an origin database crash. Consistent Hashing maps keys and nodes to a circular hash ring, so adding/removing a node only remaps K/N keys on average.",
        "steps": "1. Both nodes and keys are hashed onto a 360-degree ring (e.g., 0 to 2^32 - 1).\n2. Key is assigned to the first node encountered clockwise.\n3. Virtual nodes (vnodes) are used to balance distribution and avoid hot spots.\n4. When Node 3 fails, only keys formerly on Node 3 move to Node 4; all other nodes remain unaffected.",
        "example": "Amazon DynamoDB, Apache Cassandra, and Discord voice routing use Consistent Hashing rings.",
        "mistake": "Using hash(key) % N in a dynamic cluster where N changes frequently.",
        "tip": "Virtual nodes prevent data skew and distribute failover load evenly across surviving nodes.",
        "options": [
            ("A", "Minimizes key redistribution when nodes are added or removed to only K/N keys", True, "Correct: Avoids mass cache eviction storms during horizontal scaling."),
            ("B", "Guarantees all database write queries execute in exactly 1 nanosecond", False, "Consistent hashing is an algorithmic partitioning strategy, not a hardware accelerator."),
            ("C", "Eliminates the need for any caching servers in production", False, "Consistent hashing is used specifically to manage clusters of caching and storage servers."),
            ("D", "Encrypts all network packets using AES-256", False, "Consistent hashing handles partition routing, not packet encryption.")
        ]
    },
    {
        "topic_slug": "system-design-cloud",
        "type": "technical_mcq",
        "difficulty": "intermediate",
        "text": "According to the CAP Theorem, why can a distributed system partitioned across an unreliable network NOT simultaneously guarantee Consistency and Availability?",
        "explanation": "When a network partition (P) occurs, nodes in partition A cannot communicate with nodes in partition B. If a write arrives at partition A: providing Consistency (C) requires rejecting or stalling the write until B is updated (sacrificing Availability). Providing Availability (A) requires accepting the write immediately, meaning partition B serves stale data (sacrificing Consistency).",
        "steps": "1. Network partition occurs: Link between Data Center 1 and Data Center 2 breaks.\n2. Write arrives at DC 1: 'balance = $100'.\n3. Choice CP: DC 1 refuses write or blocks until DC 2 confirms (System unavailable during partition).\n4. Choice AP: DC 1 writes immediately; DC 2 returns old balance (System inconsistent).",
        "example": "ZooKeeper/etcd are CP systems; Cassandra/DynamoDB (by default) are AP systems.",
        "mistake": "Claiming a system can be 'CA' during network partitions. Partitions in real networks are inevitable.",
        "tip": "Since network failures are unavoidable, the real trade-off in distributed systems is CP vs AP.",
        "options": [
            ("A", "During a network partition, you must either reject writes for consistency (CP) or accept writes risking stale data (AP)", True, "Correct: Network splits force a fundamental choice between strict consistency or 100% availability."),
            ("B", "Modern optical fiber networks have eliminated network partitions completely", False, "Hardware failures, switch bugs, and fiber cuts still cause regular network partitions."),
            ("C", "CAP theorem only applies to single-core desktop computers", False, "CAP applies specifically to distributed networked data systems."),
            ("D", "A system can achieve C, A, and P simultaneously simply by buying more RAM", False, "Physical network disconnection cannot be resolved by local memory capacity.")
        ]
    },
    {
        "topic_slug": "system-design-cloud",
        "type": "technical_mcq",
        "difficulty": "advanced",
        "text": "How does the Token Bucket rate limiting algorithm differ from the Leaky Bucket algorithm in API Gateway traffic management?",
        "explanation": "Token Bucket allows short bursts of traffic up to the bucket capacity as long as tokens are available, whereas Leaky Bucket strictly smooths traffic output at a constant continuous rate, discarding bursts that exceed bucket depth.",
        "steps": "1. Token Bucket: Tokens added at rate R up to max capacity B. If bucket has 10 tokens, 10 requests can execute immediately (supports bursts).\n2. Leaky Bucket: Requests enter FIFO buffer and leak out at constant rate R. Spikes are flattened into constant output.",
        "example": "AWS API Gateway and Stripe use Token Bucket because legitimate users often click in quick bursts.",
        "mistake": "Thinking both algorithms behave identically under bursty user traffic.",
        "tip": "Use Token Bucket when bursty user behavior is normal; use Leaky Bucket to protect downstream services with strict steady-state limits.",
        "options": [
            ("A", "Token Bucket permits traffic bursts up to bucket capacity; Leaky Bucket forces a steady constant outflow rate", True, "Correct: Token Bucket accommodates bursty client calls; Leaky Bucket enforces continuous smooth rate."),
            ("B", "Token Bucket only works on TCP SYN packets; Leaky Bucket works on UDP", False, "Both are application/transport layer rate limiting algorithms applicable to any protocol."),
            ("C", "Leaky Bucket never drops any incoming requests under any circumstances", False, "Leaky bucket drops (leaks) requests when the incoming queue fills up."),
            ("D", "Token Bucket requires quantum computing hardware to run", False, "Token bucket requires simple integer counters in Redis or memory.")
        ]
    },

    # =========================================================================
    # AI / ML FOUNDATIONS (15 Questions)
    # =========================================================================
    {
        "topic_slug": "ai-ml-foundations",
        "type": "technical_mcq",
        "difficulty": "intermediate",
        "text": "In a machine learning model predicting rare diseases (1 positive case in 10,000 patients), why is Accuracy a dangerously misleading evaluation metric?",
        "explanation": "A trivial dummy model that always predicts 'Negative' achieves 99.99% accuracy while failing to detect a single actual sick patient. For imbalanced datasets, Recall (Sensitivity), Precision, and PR-AUC are the required metrics.",
        "steps": "1. Total patients: 10,000. True positives: 1. True negatives: 9,999.\n2. Model predicts 'Negative' for all 10,000.\n3. Accuracy = 9,999 / 10,000 = 99.99%.\n4. Recall = 0 / 1 = 0% (Fatal clinical failure!).",
        "example": "Fraud detection and medical diagnosis always prioritize High Recall over raw Accuracy.",
        "mistake": "Using Accuracy on class-imbalanced datasets.",
        "tip": "When false negatives are costly, optimize Recall; when false positives are costly, optimize Precision.",
        "options": [
            ("A", "A dummy model always predicting the majority class achieves 99.99% accuracy while missing all true positive cases", True, "Correct: Class imbalance renders accuracy meaningless; Recall and F1-score must be used."),
            ("B", "Accuracy is mathematically impossible to calculate on numbers larger than 1,000", False, "Accuracy calculation is simple division: (TP + TN) / Total."),
            ("C", "High accuracy automatically causes models to consume 100% GPU memory", False, "Evaluation metrics have zero correlation with GPU memory consumption."),
            ("D", "Accuracy is only valid for unsupervised clustering models like K-Means", False, "Accuracy is an evaluation metric for supervised classification.")
        ]
    },
    {
        "topic_slug": "ai-ml-foundations",
        "type": "technical_mcq",
        "difficulty": "advanced",
        "text": "What is the primary architectural purpose of Self-Attention in the Transformer deep learning architecture?",
        "explanation": "Self-Attention computes dynamic contextual relationship weights between every pair of tokens in a sequence in parallel, allowing models to capture long-range dependencies in O(1) sequential step, overcoming RNN vanishing gradient bottlenecks.",
        "steps": "1. Compute Queries (Q), Keys (K), and Values (V) via linear projections.\n2. Attention(Q, K, V) = softmax((Q * K^T) / sqrt(d_k)) * V.\n3. Every token attends to every other token simultaneously.\n4. Enables massive GPU training parallelization compared to sequential RNNs.",
        "example": "In 'The animal didn't cross the street because it was too tired', self-attention links 'it' to 'animal' rather than 'street'.",
        "mistake": "Thinking Transformers process words one by one sequentially like LSTMs. Transformers process the entire sequence in parallel.",
        "tip": "Self-attention provides O(1) path length between any two tokens in a sequence.",
        "options": [
            ("A", "Computes dynamic contextual weights between all token pairs in parallel, capturing long-range dependencies", True, "Correct: Replaces sequential recurrence with parallel pairwise attention across all positions."),
            ("B", "Compresses training datasets into encrypted ZIP archives", False, "Attention is a neural network layer, not a file compression utility."),
            ("C", "Converts Python source code into compiled assembly instructions", False, "Compilers like LLVM or GCC do compilation, not transformer attention."),
            ("D", "Eliminates the need for any matrix multiplication during neural network training", False, "Self-attention relies heavily on dense matrix multiplications (Q * K^T and Attention * V).")
        ]
    },
    {
        "topic_slug": "ai-ml-foundations",
        "type": "technical_mcq",
        "difficulty": "intermediate",
        "text": "How do L1 Regularization (Lasso) and L2 Regularization (Ridge) differ in their effect on model weight parameters?",
        "explanation": "L1 adds the sum of absolute weights (|w|) to the loss, driving non-essential coefficients strictly to zero (producing sparse models and feature selection). L2 adds the sum of squared weights (w^2), shrinking weights toward zero smoothly without making them exactly zero.",
        "steps": "1. L1 (Lasso): Loss + lambda * sum(|w_i|). Sharp diamond constraint contour causes intersections on axes (sparse weights = 0).\n2. L2 (Ridge): Loss + lambda * sum(w_i^2). Circular constraint contour shrinks weights evenly, preventing any single feature from dominating.",
        "example": "Use L1 when you have 10,000 features and suspect only 50 are meaningful; use L2 to combat multicollinearity.",
        "mistake": "Assuming L2 performs automatic feature selection. L2 retains all features with smaller weights; L1 zeroes out irrelevant features.",
        "tip": "L1 = Feature selection (sparse zeros); L2 = Weight shrinkage (handles multicollinearity).",
        "options": [
            ("A", "L1 drives non-essential weights to exactly zero (sparsity); L2 shrinks weights smoothly without zeroing them", True, "Correct: L1 induces feature sparsity; L2 controls parameter magnitude without discarding features."),
            ("B", "L1 is only for text data; L2 is only for image pixels", False, "Both regularizers apply to any numerical loss function regardless of modality."),
            ("C", "L2 regularization increases model overfitting on small training samples", False, "Regularization by definition reduces overfitting by constraining model complexity."),
            ("D", "L1 and L2 are completely identical algorithms with different marketing names", False, "They utilize distinct norms (Manhattan L1 vs Euclidean L2) with vastly different mathematical geometries.")
        ]
    },

    # =========================================================================
    # SOFTWARE ENGINEERING & TESTING (15 Questions)
    # =========================================================================
    {
        "topic_slug": "software-engineering-testing",
        "type": "technical_mcq",
        "difficulty": "intermediate",
        "text": "What is the primary distinction between a Unit Test and an Integration Test in modern software engineering?",
        "explanation": "A Unit Test isolates a single function or module in complete isolation using test doubles/mocks for external dependencies (DB, network). An Integration Test verifies that multiple collaborating components or services interact correctly with real databases or network boundaries.",
        "steps": "1. Unit Test: Fast (<5ms), isolated, runs in memory, mocks database queries, tests algorithmic branches.\n2. Integration Test: Slower (~100-500ms), verifies real SQL queries against a test database, validates HTTP serialization and schema constraints.",
        "example": "Testing a price discount calculation function = Unit Test; testing that placing an order persists records in PostgreSQL = Integration Test.",
        "mistake": "Having unit tests connect to real production databases, causing flakiness, slowness, and side effects.",
        "tip": "The Testing Pyramid: Many fast unit tests at the base, fewer integration tests in the middle, few E2E tests at the apex.",
        "options": [
            ("A", "Unit tests test single isolated components with mocked dependencies; Integration tests verify interactions across real system boundaries", True, "Correct: Distinguishes fine-grained isolation from multi-component collaborative verification."),
            ("B", "Unit tests are run manually by users; Integration tests run automatically inside the compiler", False, "Both unit and integration tests are automated in CI/CD test runners."),
            ("C", "Integration tests never touch databases or network sockets", False, "Integration tests specifically exercise real databases, message queues, and endpoints."),
            ("D", "Unit tests cannot contain assertions or if-conditions", False, "Unit tests rely directly on assertions to verify test outcomes.")
        ]
    },
    {
        "topic_slug": "software-engineering-testing",
        "type": "technical_mcq",
        "difficulty": "intermediate",
        "text": "What is a 'Flaky Test' in automated CI/CD pipelines and what is its most common root cause?",
        "explanation": "A flaky test is an automated test that non-deterministically passes or fails on the same source code without any code changes. The most common causes are asynchronous timing/race conditions, reliance on system clocks, unseeded random generators, or shared mutable global state.",
        "steps": "1. Test relies on `sleep(1)` waiting for async task. On a loaded CI server, the task takes 1.05s -> Test fails!\n2. Next run on idle server -> Test passes in 0.8s.\n3. Result: Developers lose trust in CI and begin ignoring test failures.",
        "example": "Fixing flakiness: Replace arbitrary `time.sleep()` with deterministic polling `wait_for_condition()` or event promises.",
        "mistake": "Rerunning flaky tests in a loop until they pass without fixing the underlying non-determinism.",
        "tip": "Never use fixed sleep timers in async tests; poll for expected conditions with timeouts.",
        "options": [
            ("A", "A test that passes or fails non-deterministically due to timing races, shared state, or external network latency", True, "Correct: Flaky tests undermine developer confidence in CI pipelines due to non-deterministic execution."),
            ("B", "A test written in Python instead of C++", False, "Test flakiness occurs in all programming languages."),
            ("C", "A test that executes faster than 1 millisecond", False, "Fast execution is desirable, not a flaw."),
            ("D", "A test that is compiled with GCC compiler optimization flag -O3", False, "Compiler optimization does not define test flakiness.")
        ]
    }
]

print(f"Adding {len(BATCH)} curated advanced questions across premier topics...")

added_count = 0
for item in BATCH:
    topic_id = get_topic_id(item["topic_slug"])
    c.execute("""
        INSERT INTO questions (
            topic_id, question_type, difficulty, question_text, explanation,
            step_by_step_reasoning, practical_example, common_mistake,
            learning_tip, is_published, created_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 1, ?)
    """, (
        topic_id, item["type"], item["difficulty"], item["text"],
        item["explanation"], item["steps"], item["example"],
        item["mistake"], item["tip"], now_iso
    ))
    q_id = c.lastrowid
    added_count += 1

    for opt in item["options"]:
        c.execute("""
            INSERT INTO question_options (
                question_id, option_key, option_text, is_correct, why_wrong_explanation
            ) VALUES (?, ?, ?, ?, ?)
        """, (q_id, opt[0], opt[1], 1 if opt[2] else 0, opt[3]))

conn.commit()
conn.close()

print(f"Successfully added {added_count} curated questions and {added_count * 4} options!")
