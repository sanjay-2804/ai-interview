from typing import List, Dict, Any, Optional

COMPANIES_DATA = [   {   'badge': 'TCS NQT / Digital / Prime',
        'description': "India's largest IT recruiter. TCS National Qualifier Test (NQT) screens for Ninja (3.36LPA), "
                       'Digital (7.0LPA), and Prime (9.0LPA) roles.',
        'eligibility': 'B.Tech / MCA / M.Tech with 60% or 6.0 CGPA throughout 10th, 12th, and UG with max 1 active '
                       'backlog.',
        'hiring_season': 'Year-round / National Qualifier Test',
        'id': 'tcs',
        'name': 'Tata Consultancy Services (TCS)',
        'package': 'INR 3.36 LPA - INR 9.0 LPA',
        'rounds': [   {   'cutoff_percentage': 65,
                          'duration_minutes': 75,
                          'name': 'Foundation Cognitive Assessment',
                          'questions_count': 65,
                          'round_number': 1,
                          'sample_questions': [   {   'answer': '200 m',
                                                      'explanation': 'Let train length be L and speed be S. S = (800 + '
                                                                     'L)/100 = (400 + L)/60. 60(800 + L) = 100(400 + '
                                                                     'L) => 48000 + 60L = 40000 + 100L => 40L = 8000 '
                                                                     '=> L = 200 m.',
                                                      'options': ['100 m', '200 m', '300 m', '400 m'],
                                                      'question': 'A train passes two bridges of lengths 800 m and 400 '
                                                                  'm in 100 seconds and 60 seconds respectively. What '
                                                                  'is the length of the train?'},
                                                  {   'answer': 'Undefined behavior (compiler dependent)',
                                                      'explanation': 'Modifying a variable multiple times without a '
                                                                     'sequence point causes undefined behavior in '
                                                                     'standard C/C++.',
                                                      'options': [   'Undefined behavior (compiler dependent)',
                                                                     '5 6 6',
                                                                     '7 7 5',
                                                                     '7 6 5'],
                                                      'question': 'What is the output of the following C code?\n'
                                                                  'int a = 5;\n'
                                                                  "printf('%d %d %d', a, ++a, a++);"},
                                                  {   'answer': '1',
                                                      'explanation': 'Equality operator (==) has higher precedence '
                                                                     "than assignment (=). 'y == 20' evaluates to 1 "
                                                                     '(True). Then x is assigned 1, and 1 is printed.',
                                                      'options': ['1', '0', '10', '20'],
                                                      'question': 'What is the output of the following C program?\n'
                                                                  '#include <stdio.h>\n'
                                                                  'int main() {\n'
                                                                  '  int x = 10, y = 20;\n'
                                                                  "  printf('%d', x = y == 20);\n"
                                                                  '  return 0;\n'
                                                                  '}'},
                                                  {   'answer': '6.25 m/s',
                                                      'explanation': 'Let speed of A be Va and speed of B be Vb. Time '
                                                                     'taken by A = 1000/Va. In case 1: 960/Vb - '
                                                                     '1000/Va = 19. In case 2: 1000/Va - 960/Vb + 30 '
                                                                     'gives distance difference. Solving the linear '
                                                                     'system yields Va = 6.25 m/s.',
                                                      'options': ['5 m/s', '6.25 m/s', '7.5 m/s', '8 m/s'],
                                                      'question': 'In a competitive race, A gives B a start of 40 '
                                                                  'meters in a 1000-meter race, and A wins by 19 '
                                                                  'seconds. If A gives B a start of 30 seconds, B wins '
                                                                  'by 40 meters. Find the speed of A.'},
                                                  {   'answer': 'O(N)',
                                                      'explanation': 'Although inserting N elements one by one takes '
                                                                     'O(N log N), bottom-up Heapify sums the series '
                                                                     'N/4*(1) + N/8*(2) + N/16*(3)... which converges '
                                                                     'mathematically to O(N).',
                                                      'options': ['O(N)', 'O(N log N)', 'O(log N)', 'O(N^2)'],
                                                      'question': 'What is the time complexity of building a Binary '
                                                                  'Heap from an unordered array of N elements using '
                                                                  'the bottom-up Heapify approach?'},
                                                  {   'answer': '20%',
                                                      'explanation': 'Let CP = 100. SP for 8% gain = 108. If discount '
                                                                     'is 10%, MP × 0.9 = 108. MP = 120. So 20% above '
                                                                     'CP.',
                                                      'options': ['20%', '18%', '15%', '25%'],
                                                      'question': 'A shopkeeper allows a discount of 10% on the marked '
                                                                  'price of an article. How much above the cost price '
                                                                  'should he mark the article to gain 8% profit?'},
                                                  {   'answer': '20',
                                                      'explanation': 'n(n+1)/2 = 210 → n(n+1) = 420. 20 × 21 = 420, so '
                                                                     'n = 20.',
                                                      'options': ['20', '21', '19', '25'],
                                                      'question': 'If the sum of the first n natural numbers is 210, '
                                                                  'what is n?'},
                                                  {   'answer': '8',
                                                      'explanation': '2⁸ = 256, so log₂(256) = 8.',
                                                      'options': ['8', '7', '6', '9'],
                                                      'question': 'What is the value of log₂(256)?'},
                                                  {   'answer': 'INR 14,400',
                                                      'explanation': 'SI = 12000 × 10 × 2 / 100 = 2400. Amount = 12000 '
                                                                     '+ 2400 = 14400.',
                                                      'options': [   'INR 14,400',
                                                                     'INR 13,200',
                                                                     'INR 14,000',
                                                                     'INR 15,600'],
                                                      'question': 'A man invested INR 12,000 at 10% SI for 2 years. '
                                                                  'What is the total amount at the end?'}],
                          'sections': [   'Numerical Ability (20 Qs)',
                                          'Verbal Ability (25 Qs)',
                                          'Reasoning Ability (20 Qs)'],
                          'tips': 'No negative marking in foundation round. Time management is critical.',
                          'type': 'Aptitude & Technical MCQ'},
                      {   'cutoff_percentage': 50,
                          'duration_minutes': 90,
                          'name': 'Advanced Quantitative & Hands-on Coding',
                          'questions_count': 2,
                          'round_number': 2,
                          'sample_questions': [   {   'expected': [   'Greedy jump tracking',
                                                                      'O(N) time complexity',
                                                                      'O(1) space complexity'],
                                                      'question': 'Given an integer array of size N, find the minimum '
                                                                  'number of jumps required to reach the end of the '
                                                                  'array, where each element represents the max steps '
                                                                  'you can jump forward.'},
                                                  {   'expected': [   'Sliding Window technique',
                                                                      'Hash Map or frequency array of characters',
                                                                      'O(N) time complexity and O(min(N, M)) space '
                                                                      'complexity'],
                                                      'model_answer': 'Use a sliding window with left and right '
                                                                      'pointers. Maintain a hash map storing the most '
                                                                      'recent index of each character. When a repeated '
                                                                      'character is encountered within the current '
                                                                      'window, move the left pointer to '
                                                                      'last_seen_index + 1. Track max_length.',
                                                      'question': 'Given a string S containing lowercase English '
                                                                  'alphabets, find the length of the longest substring '
                                                                  'without repeating characters.\n'
                                                                  "Input: 'abcabcbb'\n"
                                                                  "Output: 3 (The answer is 'abc')."},
                                                  {   'expected': [   'Single-pass tracking of min_price',
                                                                      'Calculate potential profit = price[i] - '
                                                                      'min_price',
                                                                      'O(N) time and O(1) space'],
                                                      'model_answer': "Maintain a running variable 'min_price_so_far' "
                                                                      'initialized to infinity. Iterate through the '
                                                                      'array: update min_price_so_far = '
                                                                      'min(min_price_so_far, price), and max_profit = '
                                                                      'max(max_profit, price - min_price_so_far). '
                                                                      'Returns max_profit in O(N) time and O(1) space.',
                                                      'question': 'Given an array of positive integers representing '
                                                                  'daily stock prices, find the maximum profit you can '
                                                                  'achieve by choosing a single day to buy one stock '
                                                                  'and choosing a different day in the future to sell '
                                                                  'that stock.\n'
                                                                  'Input: [7,1,5,3,6,4]\n'
                                                                  'Output: 5 (Buy on day 2 at price 1 and sell on day '
                                                                  '5 at price 6).'},
                                                  {   'expected': [   'Two-pointer approach',
                                                                      'Skip non-alphanumeric characters',
                                                                      'Compare lowercase versions',
                                                                      'O(N) time, O(1) space'],
                                                      'model_answer': 'def is_palindrome(s):\n'
                                                                      '    l, r = 0, len(s)-1\n'
                                                                      '    while l < r:\n'
                                                                      '        while l < r and not s[l].isalnum(): l '
                                                                      '+= 1\n'
                                                                      '        while l < r and not s[r].isalnum(): r '
                                                                      '-= 1\n'
                                                                      '        if s[l].lower() != s[r].lower(): return '
                                                                      'False\n'
                                                                      '        l += 1; r -= 1\n'
                                                                      '    return True',
                                                      'question': 'Write a function in Python to check if a given '
                                                                  'string is a valid palindrome considering only '
                                                                  'alphanumeric characters and ignoring cases.'},
                                                  {   'expected': [   'Sort the array first',
                                                                      'Iterate and compare adjacent elements',
                                                                      'Track minimum difference',
                                                                      'O(N log N) due to sorting'],
                                                      'model_answer': 'Sort array. Iterate comparing arr[i+1]-arr[i] '
                                                                      'for minimum difference. Return pair with '
                                                                      'smallest absolute difference.',
                                                      'question': 'Given an array of integers, find the pair with the '
                                                                  'minimum absolute difference. Return the pair.'}],
                          'sections': ['Advanced Quantitative (15 Qs)', 'Hands-on Coding (2 Problems)'],
                          'tips': 'Problem 1 is typically Array/String manipulation. Problem 2 is Dynamic Programming '
                                  'or Matrix traversal.',
                          'type': 'Advanced Coding'},
                      {   'cutoff_percentage': 70,
                          'duration_minutes': 45,
                          'name': 'Technical Interview (TR)',
                          'questions_count': 4,
                          'round_number': 3,
                          'sample_questions': [   {   'expected': [   'Encapsulation, Abstraction, Inheritance, '
                                                                      'Polymorphism',
                                                                      'Virtual functions & vtable in C++',
                                                                      'Method overriding & dynamic method dispatch in '
                                                                      'Java'],
                                                      'question': 'Explain the 4 pillars of OOPs with real-world '
                                                                  'examples. How is Runtime Polymorphism achieved in '
                                                                  'C++ vs Java?'},
                                                  {   'expected': [   'Super key uniquely identifies row',
                                                                      'Candidate key is minimal super key',
                                                                      'Primary key is chosen candidate key',
                                                                      'Foreign key refers to primary key of another '
                                                                      'relation'],
                                                      'question': 'Explain the difference between primary key, foreign '
                                                                  'key, candidate key, and super key in DBMS.'},
                                                  {   'expected': [   'Virtual destructor ensures derived class '
                                                                      'destructor is called',
                                                                      'Prevents memory leaks and resource dangling '
                                                                      'when deleting derived object via base pointer',
                                                                      'vtable stores destructor entry point'],
                                                      'question': 'Why does a C++ base class with virtual functions '
                                                                  'always require a virtual destructor, and what '
                                                                  'happens if you omit it?'},
                                                  {   'expected': [   '1NF: Atomic values',
                                                                      '2NF: No partial dependency on composite key',
                                                                      '3NF: No transitive dependencies',
                                                                      'BCNF: Every determinant is a candidate key',
                                                                      'Denormalization used in read-heavy '
                                                                      'analytics/warehousing to avoid expensive '
                                                                      'multi-table JOINs'],
                                                      'question': 'Explain Database Normalization from 1NF to BCNF '
                                                                  'with real-world examples. Under what production '
                                                                  'circumstances would you intentionally denormalize a '
                                                                  'schema?'},
                                                  {   'expected': [   'TCP: connection-oriented, reliable, ordered '
                                                                      'delivery',
                                                                      'UDP: connectionless, fast, no guaranteed '
                                                                      'delivery',
                                                                      'TCP: web browsing, email, file transfer',
                                                                      'UDP: video streaming, gaming, DNS queries'],
                                                      'model_answer': 'TCP guarantees ordered, reliable delivery via '
                                                                      'acknowledgments and retransmissions (used for '
                                                                      'HTTP, FTP, email). UDP is connectionless with '
                                                                      'minimal overhead (used for live video, VoIP, '
                                                                      'gaming where speed matters more than '
                                                                      'reliability).',
                                                      'question': 'Explain the difference between TCP and UDP '
                                                                  'protocols. When would you choose one over the '
                                                                  'other?'}],
                          'sections': [   'OOPs Concepts',
                                          'DBMS & SQL Normalization',
                                          'Final Year Project Defense',
                                          'Pointers and Memory'],
                          'tips': 'Be thorough with your resume projects. Interviewers frequently ask to write SQL '
                                  'queries with GROUP BY and HAVING on paper.',
                          'type': 'Technical Interview'},
                      {   'cutoff_percentage': 75,
                          'duration_minutes': 30,
                          'name': 'Managerial & HR Interview (MR/HR)',
                          'questions_count': 3,
                          'round_number': 4,
                          'sample_questions': [   {   'expected': [   'Clear positive affirmation of relocation '
                                                                      'willingness',
                                                                      'Adaptability evidence from college '
                                                                      'hostelling/internship',
                                                                      'Enthusiasm for global client exposure'],
                                                      'question': 'TCS operates in global client timezones requiring '
                                                                  'shift rotations and relocation across delivery '
                                                                  'centres in India. Are you comfortable with this, '
                                                                  'and how do you adapt to new environments?'},
                                                  {   'expected': [   'Non-accusatory direct communication first',
                                                                      'Understanding root causes (clarity, skill gap, '
                                                                      'personal emergency)',
                                                                      'Offering pairing or breaking down tasks',
                                                                      'Escalating transparently to project manager if '
                                                                      'unresolved'],
                                                      'question': 'How do you handle working with a team member who is '
                                                                  'not pulling their weight or missing deadlines on a '
                                                                  'client deliverable?'},
                                                  {   'answer': 'Express your goal of growing from a developer to a '
                                                                'technical architect or project lead within TCS '
                                                                "Digital. Mention TCS's training programs, global "
                                                                'client exposure, and opportunities for certifications '
                                                                'in cloud and AI technologies.',
                                                      'question': 'Where do you see yourself in 5 years? How does TCS '
                                                                  'fit into your career plan?'}],
                          'sections': [   'Willingness to Relocate',
                                          'Rotational Shifts & Night Shifts',
                                          'TCS Core Values & Integrity',
                                          'Handling Work Deadlines'],
                          'tips': 'Show flexibility with relocation and working in shifts. TCS values reliability and '
                                  'loyalty.',
                          'type': 'HR & Behavioral'}],
        'slug': 'tcs'},
    {   'badge': 'SE / DSE / Specialist Programmer',
        'description': 'Known for the Mysuru training campus. Offers Systems Engineer (3.6LPA), Digital Specialist '
                       'Engineer (DSE - 6.25LPA), and Specialist Programmer (SP - 9.5LPA).',
        'eligibility': '60% or 6.0 CGPA throughout 10th, 12th, and Diploma/B.Tech with all branches eligible.',
        'hiring_season': 'On-Campus & InfyTQ',
        'id': 'infosys',
        'name': 'Infosys',
        'package': 'INR 3.6 LPA - INR 9.5 LPA',
        'rounds': [   {   'cutoff_percentage': 70,
                          'duration_minutes': 100,
                          'name': 'Online Test (Reasoning, Technical & Verbal)',
                          'questions_count': 54,
                          'round_number': 1,
                          'sample_questions': [   {   'answer': '7',
                                                      'explanation': 'Identity: (a ^ b) + 2*(a & b) = a + b. Here 4 + '
                                                                     '3 = 7. Bitwise XOR is addition without carry, '
                                                                     'and AND*2 adds the carry back.',
                                                      'options': ['7', '11', '14', '9'],
                                                      'question': 'What is the output of the following pseudocode?\n'
                                                                  'Integer a, b, c\n'
                                                                  'Set a = 4, b = 3\n'
                                                                  'c = (a ^ b) + (a & b) * 2\n'
                                                                  'Print c'},
                                                  {   'answer': '37',
                                                      'explanation': 'p & q = 5 & 11 = 1. q ^ r = 11 ^ 7 = 12. Since 1 '
                                                                     '< 12, the condition is True. p = (11 >> 1) + (7 '
                                                                     '<< 1) = 5 + 14 = 19. Result = 19 + 11 + 7 = 37.',
                                                      'options': ['37', '32', '29', '41'],
                                                      'question': 'What is the output of the following pseudocode?\n'
                                                                  'Integer p, q, r\n'
                                                                  'Set p = 5, q = 11, r = 7\n'
                                                                  'If ((p & q) < (q ^ r))\n'
                                                                  '  p = (q >> 1) + (r << 1)\n'
                                                                  'End If\n'
                                                                  'Print p + q + r'},
                                                  {   'answer': 'Only Conclusion II follows',
                                                      'explanation': 'Since all algorithms are logic, the converse '
                                                                     "'Some logic is algorithms' is always true. "
                                                                     'However, there is no direct definite overlap '
                                                                     'between mathematics and algorithms, so I does '
                                                                     'not necessarily follow.',
                                                      'options': [   'Only Conclusion II follows',
                                                                     'Only Conclusion I follows',
                                                                     'Both I and II follow',
                                                                     'Neither follows'],
                                                      'question': 'Statements: (1) All algorithms are logic. (2) Some '
                                                                  'logic is mathematics. Conclusions: (I) Some '
                                                                  'mathematics is algorithms. (II) Some logic is '
                                                                  'algorithms.'},
                                                  {   'answer': '1/2',
                                                      'explanation': 'Total outcomes = 8. Favorable (2H or 3H): HHT, '
                                                                     'HTH, THH, HHH = 4. Probability = 4/8 = 1/2.',
                                                      'options': ['1/2', '3/8', '1/4', '5/8'],
                                                      'question': 'Three coins are tossed simultaneously. What is the '
                                                                  'probability of getting at least 2 heads?'},
                                                  {   'answer': '165731',
                                                      'explanation': 'O=1, R=6, A=5, C=7, L=3, E=1. ORACLE = 165731.',
                                                      'options': ['165731', '156731', '165371', '156371'],
                                                      'question': 'If ROSE is coded as 6821, CHAIR is coded as 73456, '
                                                                  'then what is the code for ORACLE?'},
                                                  {   'answer': '42',
                                                      'explanation': 'Differences: 4, 6, 8, 10, 12. Next term = 30 + '
                                                                     '12 = 42. Pattern: n(n+1) → 1×2, 2×3, 3×4, 4×5, '
                                                                     '5×6, 6×7=42.',
                                                      'options': ['42', '40', '36', '44'],
                                                      'question': 'Complete the series: 2, 6, 12, 20, 30, ?'}],
                          'sections': [   'Reasoning Ability (15 Qs)',
                                          'Technical Ability & Pseudocode (10 Qs)',
                                          'Verbal Ability (20 Qs)',
                                          'Numerical Puzzle Solving (4 Qs)'],
                          'tips': 'Pseudocode section has high weightage. Watch out for bitwise shift operators and '
                                  'recursive loops.',
                          'type': 'Aptitude & Technical MCQ'},
                      {   'cutoff_percentage': 60,
                          'duration_minutes': 180,
                          'name': 'HackWithInfy / SP Coding Round',
                          'questions_count': 3,
                          'round_number': 2,
                          'sample_questions': [   {   'expected': [   '2D DP table memoization',
                                                                      'O(N^2) time complexity',
                                                                      'Base cases of single characters'],
                                                      'question': 'Find the length of the longest palindromic '
                                                                  'subsequence in a given string using dynamic '
                                                                  'programming.'},
                                                  {   'expected': [   'Modified Binary Search',
                                                                      'Determine which half (left or right) is sorted',
                                                                      'Check if target lies in sorted half',
                                                                      'O(log N) time and O(1) space'],
                                                      'model_answer': 'In a rotated sorted array, dividing at mid '
                                                                      'always leaves at least one half strictly '
                                                                      'sorted. If nums[left] <= nums[mid], the left '
                                                                      'half is sorted. If target is within nums[left] '
                                                                      'and nums[mid], search left; otherwise search '
                                                                      'right. If right half is sorted, apply symmetric '
                                                                      'logic. Time complexity is O(log N).',
                                                      'question': 'Given an array of integers sorted in ascending '
                                                                  'order that has been rotated at an unknown pivot, '
                                                                  'find the index of a target value in O(log N) time.\n'
                                                                  'Input: nums = [4,5,6,7,0,1,2], target = 0\n'
                                                                  'Output: 4'},
                                                  {   'expected': [   'Dynamic Programming (Unbounded Knapsack)',
                                                                      'dp[i] = min(dp[i], dp[i - coin] + 1)',
                                                                      'O(amount * number of coins) time',
                                                                      'O(amount) space'],
                                                      'model_answer': 'Initialize dp array of size amount + 1 with '
                                                                      'infinity, dp[0] = 0. For each coin, iterate '
                                                                      'from coin to amount: dp[i] = min(dp[i], dp[i - '
                                                                      'coin] + 1). Return dp[amount] if not infinity '
                                                                      'else -1.',
                                                      'question': 'Given coins of different denominations and a total '
                                                                  'amount of money, compute the fewest number of coins '
                                                                  'that you need to make up that amount. If that '
                                                                  'amount cannot be made up, return -1.\n'
                                                                  'Input: coins = [1,2,5], amount = 11\n'
                                                                  'Output: 3 (11 = 5 + 5 + 1)'},
                                                  {   'expected': [   'Initialize first_max and second_max',
                                                                      'Single pass through array',
                                                                      'Update both when finding a new maximum',
                                                                      'Handle edge case of all equal elements',
                                                                      'O(N) time complexity'],
                                                      'model_answer': 'Initialize first = second = -infinity. For each '
                                                                      'element x: if x > first, set second = first, '
                                                                      'first = x. Else if x > second and x != first, '
                                                                      'set second = x. Return second. O(N) time, O(1) '
                                                                      'space.',
                                                      'question': 'Write pseudocode to find the second largest element '
                                                                  'in an unsorted array without sorting it.'},
                                                  {   'expected': [   'Function calling itself with a base case',
                                                                      'Example: factorial, Fibonacci, tree traversal',
                                                                      'Advantage: elegant solution for tree/graph '
                                                                      'problems',
                                                                      'Disadvantage: stack overflow risk, overhead of '
                                                                      'function calls'],
                                                      'model_answer': 'Recursion is a technique where a function calls '
                                                                      'itself with a smaller subproblem until a base '
                                                                      'case is reached. Example: factorial(n) = n × '
                                                                      'factorial(n-1), base case factorial(0) = 1. '
                                                                      'Advantages: clean code for tree traversals, '
                                                                      'divide-and-conquer. Disadvantages: risk of '
                                                                      'stack overflow for deep recursion, overhead per '
                                                                      'call.',
                                                      'question': 'Explain the concept of recursion with an example. '
                                                                  'What are its advantages and disadvantages?'}],
                          'sections': [   'Greedy / DP (Easy)',
                                          'Graph / DP (Medium)',
                                          'Advanced Segment Trees / Math (Hard)'],
                          'tips': 'Solving 1 full problem and partials usually qualifies for DSE; 2+ full problems '
                                  'qualifies for Specialist Programmer.',
                          'type': 'Advanced Coding'},
                      {   'cutoff_percentage': 70,
                          'duration_minutes': 40,
                          'name': 'Technical & HR Combined Interview',
                          'questions_count': 4,
                          'round_number': 3,
                          'sample_questions': [   {   'expected': [   'Atomicity (all or nothing)',
                                                                      'Consistency (valid state transitions)',
                                                                      'Isolation (concurrent transaction separation)',
                                                                      'Durability (committed data persists)'],
                                                      'question': 'Explain ACID properties in relational databases and '
                                                                  'provide a real-life banking transaction scenario '
                                                                  'illustrating why Atomicity is critical.'},
                                                  {   'expected': [   'Synchronous blocks calling thread until I/O '
                                                                      'completes',
                                                                      'Asynchronous registers callback/coroutine and '
                                                                      'yields execution to event loop',
                                                                      'Single-threaded event loop utilizes OS polling '
                                                                      '(epoll/kqueue) for high concurrency'],
                                                      'question': 'What is the difference between Synchronous and '
                                                                  'Asynchronous programming in modern backend systems? '
                                                                  'How does the Node.js Event Loop or Python asyncio '
                                                                  'handle non-blocking I/O?'},
                                                  {   'answer': 'Walk through the project systematically: problem '
                                                                'statement, tech stack chosen and why, your specific '
                                                                'contributions, one major blocker (e.g., API rate '
                                                                'limits, database performance), how you solved it '
                                                                '(caching, query optimization), and measurable '
                                                                'outcomes (response time improved by X%).',
                                                      'question': 'Tell me about your final year project. What '
                                                                  'challenges did you face and how did you overcome '
                                                                  'them?'},
                                                  {   'answer': 'Use the STAR method: Describe the assignment '
                                                                'deadline, your prioritization approach (breaking work '
                                                                'into smaller tasks, eliminating distractions), '
                                                                'collaboration with teammates, and the successful '
                                                                'outcome delivered on time.',
                                                      'question': 'Describe a situation where you had to meet a tight '
                                                                  'deadline. How did you manage your time?'}],
                          'sections': [   'Data Structures',
                                          'Database Management',
                                          'Project Walkthrough',
                                          'Company Alignment'],
                          'tips': 'The interviewer will ask you to explain your thought process for the code written '
                                  'during the online assessment.',
                          'type': 'Technical & HR'}],
        'slug': 'infosys'},
    {   'badge': 'Associate Software Engineer / Advanced ASE',
        'description': 'Accenture uses an elimination-based multi-stage assessment covering Cognitive, Technical, and '
                       'Coding rounds.',
        'eligibility': 'B.E/B.Tech/MCA/M.Tech with 65% or 6.5 CGPA with no active backlogs.',
        'hiring_season': 'On-Campus & Off-Campus Drives',
        'id': 'accenture',
        'name': 'Accenture',
        'package': 'INR 4.5 LPA - INR 6.5 LPA',
        'rounds': [   {   'cutoff_percentage': 65,
                          'duration_minutes': 90,
                          'name': 'Cognitive & Technical Assessment',
                          'questions_count': 90,
                          'round_number': 1,
                          'sample_questions': [   {   'answer': 'SaaS delivers end-user applications; PaaS provides '
                                                                'runtime platforms for development; IaaS provides raw '
                                                                'compute, storage, and networking.',
                                                      'explanation': 'IaaS gives infrastructure (AWS EC2), PaaS gives '
                                                                     'application platforms (Heroku, AWS Elastic '
                                                                     'Beanstalk), SaaS gives completed software '
                                                                     '(Google Workspace, Salesforce).',
                                                      'options': [   'SaaS delivers end-user applications; PaaS '
                                                                     'provides runtime platforms for development; IaaS '
                                                                     'provides raw compute, storage, and networking.',
                                                                     'PaaS is hardware only; SaaS is database only; '
                                                                     'IaaS is operating system only.',
                                                                     'They are synonymous terms for virtual machines.',
                                                                     'IaaS is strictly for web hosting.'],
                                                      'question': 'In cloud computing, what is the primary difference '
                                                                  'between SaaS, PaaS, and IaaS?'},
                                                  {   'answer': 'Valid if len >= 4, has digit, has uppercase, no '
                                                                'space/slash, start != digit',
                                                      'explanation': 'Standard Accenture cognitive & coding rule: '
                                                                     'length >= 4, starts with non-digit, contains at '
                                                                     'least one uppercase letter and one digit, with '
                                                                     'no whitespace or forward slash.',
                                                      'options': [   'Valid if len >= 4, has digit, has uppercase, no '
                                                                     'space/slash, start != digit',
                                                                     "Valid if contains '@' and length > 8",
                                                                     'Valid if all lowercase',
                                                                     'Valid if ends with a period'],
                                                      'question': 'Given a password string S, check if it is valid: at '
                                                                  'least 4 characters, at least 1 numeric digit, at '
                                                                  'least 1 capital letter, and must not have space or '
                                                                  'slash. Starting character must not be a number.'},
                                                  {   'answer': '15 years',
                                                      'explanation': 'Doubling in 5 years means Simple Interest = '
                                                                     'Principal P in 5 years (Rate R = 20%). To become '
                                                                     '4 times, Interest required = 3P. Time = (3P * '
                                                                     '100) / (P * 20) = 15 years.',
                                                      'options': ['15 years', '10 years', '20 years', '12 years'],
                                                      'question': 'A sum of money doubles itself in 5 years at simple '
                                                                  'interest. In how many years will it become 4 times '
                                                                  'of itself at the same rate of interest?'},
                                                  {   'answer': '1 km/h',
                                                      'explanation': 'Upstream speed = 12/3 = 4 km/h. Downstream speed '
                                                                     '= 12/2 = 6 km/h. Stream speed = (6-4)/2 = 1 '
                                                                     'km/h.',
                                                      'options': ['1 km/h', '2 km/h', '1.5 km/h', '3 km/h'],
                                                      'question': 'A boat goes 12 km upstream in 3 hours and 12 km '
                                                                  'downstream in 2 hours. Find the speed of the '
                                                                  'stream.'},
                                                  {   'answer': 'Monday',
                                                      'explanation': 'Day before yesterday = Thursday → Yesterday = '
                                                                     'Friday → Today = Saturday → Tomorrow = Sunday → '
                                                                     'Day after tomorrow = Monday.',
                                                      'options': ['Monday', 'Tuesday', 'Sunday', 'Wednesday'],
                                                      'question': 'If the day before yesterday was Thursday, what day '
                                                                  'will fall on the day after tomorrow?'},
                                                  {   'answer': '10%',
                                                      'explanation': 'Passed in at least one = 60+70-40 = 90%. Failed '
                                                                     'in both = 100-90 = 10%.',
                                                      'options': ['10%', '15%', '20%', '30%'],
                                                      'question': 'In a class, 60% students passed in English and 70% '
                                                                  'passed in Math. If 40% passed in both, what '
                                                                  'percentage failed in both?'}],
                          'sections': [   'Critical Thinking & Problem Solving (18 Qs)',
                                          'Abstract Reasoning (17 Qs)',
                                          'English Ability (17 Qs)',
                                          'Common Application & MS Office (12 Qs)',
                                          'Pseudocode (18 Qs)',
                                          'Networking, Security & Cloud (10 Qs)'],
                          'tips': 'This is an elimination round. You must clear sectional cutoffs to immediately '
                                  'unlock the coding assessment.',
                          'type': 'Aptitude & Technical MCQ'},
                      {   'cutoff_percentage': 50,
                          'duration_minutes': 45,
                          'name': 'Hands-on Coding Assessment',
                          'questions_count': 2,
                          'round_number': 2,
                          'sample_questions': [   {   'expected': [   'Linear scan O(N)',
                                                                      'Condition check: num % 15 == 0',
                                                                      'Overflow protection with 64-bit integer'],
                                                      'question': 'Write a function that calculates the sum of all '
                                                                  'elements in an array that are divisible by both 3 '
                                                                  'and 5.'},
                                                  {   'expected': [   'Hash Set or frequency map for O(1) difference '
                                                                      'lookup',
                                                                      'For each num, check if (num - k) and (num + k) '
                                                                      'exist',
                                                                      'O(N) time and O(N) space'],
                                                      'model_answer': 'Store all unique numbers in a Hash Set. Iterate '
                                                                      'through each element num in the set: if (num + '
                                                                      'k) is in the set, increment pair count. This '
                                                                      'achieves O(N) time complexity and O(N) '
                                                                      'auxiliary space, avoiding O(N^2) nested loops.',
                                                      'question': 'You are given an array of N integers. Return the '
                                                                  'count of pairs (nums[i], nums[j]) such that i < j '
                                                                  'and |nums[i] - nums[j]| equals a given difference '
                                                                  'k.\n'
                                                                  'Input: nums = [1,5,3,4,2], k = 2\n'
                                                                  'Output: 3 (Pairs: (1,3), (5,3), (4,2))'},
                                                  {   'expected': [   'Three pointers: prev, current, next',
                                                                      'Iterative reversal in single pass',
                                                                      'O(N) time, O(1) space',
                                                                      'Handle empty list edge case'],
                                                      'model_answer': 'def reverse_list(head):\n'
                                                                      '    prev = None\n'
                                                                      '    current = head\n'
                                                                      '    while current:\n'
                                                                      '        next_node = current.next\n'
                                                                      '        current.next = prev\n'
                                                                      '        prev = current\n'
                                                                      '        current = next_node\n'
                                                                      '    return prev',
                                                      'question': 'Write a function to reverse a linked list '
                                                                  'iteratively.'}],
                          'sections': ['Problem 1: Array Operations', 'Problem 2: String & Math Transformation'],
                          'tips': 'Solving at least 1 problem completely with all public and private test cases passed '
                                  'is essential.',
                          'type': 'Coding Assessment'},
                      {   'cutoff_percentage': 70,
                          'duration_minutes': 35,
                          'name': 'Communication Assessment & Interview',
                          'questions_count': 4,
                          'round_number': 3,
                          'sample_questions': [   {   'expected': [   'STAR methodology',
                                                                      'Resource prioritization',
                                                                      'Hands-on proof of concept',
                                                                      'Successful project delivery'],
                                                      'question': 'Tell me about a time you had to adapt to a new '
                                                                  'technology quickly under a tight deadline. How did '
                                                                  'you structure your learning?'},
                                                  {   'expected': [   'IaaS: Infrastructure (AWS EC2, Azure VMs)',
                                                                      'PaaS: Platform (Heroku, AWS Elastic Beanstalk)',
                                                                      'SaaS: Software (Gmail, Salesforce)',
                                                                      'PaaS or Container Service (ECS/GKE) chosen for '
                                                                      'rapid zero-ops deployment'],
                                                      'question': 'Explain Cloud Computing service models: IaaS, PaaS, '
                                                                  'and SaaS with real-world examples. Which model '
                                                                  'would an engineering team select to rapidly deploy '
                                                                  'a full-stack containerized web app?'},
                                                  {   'answer': 'Highlight problem-solving speed, adaptability to new '
                                                                'tech stacks, and collaborative communication. Connect '
                                                                "these to Accenture's consulting model where engineers "
                                                                'must quickly understand diverse client domains and '
                                                                'deliver solutions within tight timelines.',
                                                      'question': 'What are your strengths and how will they '
                                                                  "contribute to Accenture's client delivery model?"},
                                                  {   'answer': 'Mention specific sources: following engineering blogs '
                                                                '(Martin Fowler, Netflix Tech Blog), completing online '
                                                                'certifications (AWS, Google Cloud), contributing to '
                                                                'open-source projects, and attending tech meetups or '
                                                                'hackathons.',
                                                      'question': 'How do you stay updated with rapidly evolving '
                                                                  'technology trends?'}],
                          'sections': [   'Reading Sentences',
                                          'Repeat Sentences',
                                          'Story Retelling',
                                          'Technical & Situational Interview'],
                          'tips': 'Speak clearly into your microphone with neutral pacing. The automated engine grades '
                                  'fluency, pronunciation, and sentence mastery.',
                          'type': 'Spoken & Tech Interview'}],
        'slug': 'accenture'},
    {   'badge': 'Software Development Engineer (SDE 1)',
        'description': 'Amazon evaluates candidates on exceptional algorithmic problem solving and strict adherence to '
                       'the 14/16 Leadership Principles.',
        'eligibility': 'B.Tech/M.Tech/MCA with strong foundation in Data Structures, Algorithms, and System Design '
                       'basics.',
        'hiring_season': 'Campus Placement & Amazon WOW',
        'id': 'amazon',
        'name': 'Amazon',
        'package': 'INR 32.0 LPA - INR 45.0 LPA',
        'rounds': [   {   'cutoff_percentage': 100,
                          'duration_minutes': 90,
                          'name': 'Online Assessment (OA 1 & OA 2)',
                          'questions_count': 2,
                          'round_number': 1,
                          'sample_questions': [   {   'expected': [   'Custom comparator',
                                                                      'O(N log N) sorting time',
                                                                      'Preserve original order for digit-logs '
                                                                      '(stability)'],
                                                      'question': 'Given an array of strings representing logs, where '
                                                                  'each log starts with an identifier, reorder them '
                                                                  'such that letter-logs come before digit-logs, and '
                                                                  'letter-logs are sorted lexicographically.'},
                                                  {   'expected': [   'Vector coordinate tracking',
                                                                      'Rover is bounded if position returns to (0,0) '
                                                                      'OR direction changes from initial North after 1 '
                                                                      'sequence cycle',
                                                                      'O(N) time and O(1) space'],
                                                      'model_answer': 'Simulate one cycle of instructions with '
                                                                      'direction vectors (dx, dy). If the rover '
                                                                      'returns to (0,0) or does not face North at the '
                                                                      'end of the sequence, repeating the sequence 4 '
                                                                      'times will guarantee returning to the starting '
                                                                      'point. Thus the robot is bounded.',
                                                      'question': 'In an Amazon fulfillment center, an automated rover '
                                                                  'starts at (0,0) facing North. It receives '
                                                                  "instructions: 'G' (go 1 unit), 'L' (turn 90 deg "
                                                                  "left), 'R' (turn 90 deg right). Determine if the "
                                                                  'rover moves in a bounded circle forever.'},
                                                  {   'expected': [   'Min-Heap (Priority Queue)',
                                                                      'Greedy strategy: always connect two smallest '
                                                                      'sticks',
                                                                      'O(N log N) time complexity'],
                                                      'model_answer': 'Insert all stick lengths into a Min-Heap. While '
                                                                      'heap size > 1, extract the two smallest '
                                                                      'elements, sum them, add the sum to total cost, '
                                                                      'and insert the sum back into the heap. Returns '
                                                                      'optimal Huffman-like minimum cost.',
                                                      'question': 'You have N sticks with given positive lengths. You '
                                                                  'can connect any two sticks of lengths X and Y with '
                                                                  'cost X + Y. Find the minimum total cost to connect '
                                                                  'all sticks into one.'},
                                                  {   'expected': [   'Sliding window technique',
                                                                      'Hash set or hash map to track seen characters',
                                                                      'Move left pointer when duplicate found',
                                                                      'O(N) time complexity'],
                                                      'model_answer': 'Use sliding window with hash set. Expand right '
                                                                      'pointer; if duplicate found, shrink from left '
                                                                      'until duplicate removed. Track max window '
                                                                      'length. O(N) time, O(min(N,26)) space.',
                                                      'question': 'Given a string, find the length of the longest '
                                                                  'substring without repeating characters.'}],
                          'sections': [   'Problem 1: LeetCode Medium (Hash Map / Two Pointers / Heap)',
                                          'Problem 2: LeetCode Medium/Hard (Trees / Graphs / Dynamic Programming)',
                                          'Work Style Assessment (Leadership Principles)'],
                          'tips': 'All test cases including extreme edge cases must pass. Work style survey directly '
                                  'measures Customer Obsession and Ownership.',
                          'type': 'DSA Coding & Work Simulation'},
                      {   'cutoff_percentage': 85,
                          'duration_minutes': 60,
                          'name': 'Technical Interview 1 (DSA & Code Quality)',
                          'questions_count': 2,
                          'round_number': 2,
                          'sample_questions': [   {   'expected': [   'Recursive post-order traversal',
                                                                      'Handle negative node values',
                                                                      'Global maximum tracker',
                                                                      'O(N) time and O(H) space'],
                                                      'question': 'Given a binary tree, find the maximum path sum '
                                                                  'between any two nodes. The path may start and end '
                                                                  'at any node in the tree.'},
                                                  {   'expected': [   'Customer Obsession LP',
                                                                      'Identify user friction point',
                                                                      'Proactive solution without being asked',
                                                                      'Measurable positive impact'],
                                                      'question': 'Give me an example of when you went above and '
                                                                  'beyond for a customer or end-user of an application '
                                                                  'you built.'},
                                                  {   'expected': [   'Doubly Linked List + Hash Map',
                                                                      'Hash Map maps key to node pointer',
                                                                      'Doubly Linked List maintains access recency '
                                                                      'with O(1) node relocation',
                                                                      'Capacity eviction removes tail node in O(1)'],
                                                      'model_answer': 'Use a Hash Map paired with a Doubly Linked List '
                                                                      'with dummy head and tail nodes. get(key): '
                                                                      'lookup node in map, move to head, return value. '
                                                                      'put(key, val): if key exists, update value and '
                                                                      'move to head. If new, create node, put in map '
                                                                      'and at head. If capacity exceeded, remove node '
                                                                      'before tail and delete from map.',
                                                      'question': 'Design and implement a Least Recently Used (LRU) '
                                                                  'Cache with get(key) and put(key, value) operations '
                                                                  'running in strictly O(1) average time complexity.'},
                                                  {   'expected': [   'Recursive tree traversal',
                                                                      'Base cases: root is None, root == p, root == q',
                                                                      'If left and right recursive calls both return '
                                                                      'non-null, root is LCA',
                                                                      'O(N) time and O(H) space'],
                                                      'model_answer': 'Base case: if root is None, p, or q, return '
                                                                      'root. Recursively search left = LCA(root.left, '
                                                                      'p, q) and right = LCA(root.right, p, q). If '
                                                                      'both left and right are non-null, p and q are '
                                                                      'in separate subtrees, so root is LCA. If only '
                                                                      'one is non-null, propagate that node upward.',
                                                      'question': 'Given the root of a binary tree, find the Lowest '
                                                                  'Common Ancestor (LCA) of two given nodes p and q.'},
                                                  {   'expected': [   'Use auxiliary min-stack tracking current '
                                                                      'minimum at each level',
                                                                      'Push: push to main stack AND push min(val, '
                                                                      'minStack.top) to minStack',
                                                                      'Pop: pop from both stacks',
                                                                      'getMin: return minStack.top in O(1)'],
                                                      'model_answer': 'Maintain two stacks: main stack and min stack. '
                                                                      'On push(x): push x to main, push min(x, '
                                                                      'minStack.peek()) to minStack. On pop: pop from '
                                                                      'both. getMin returns minStack.peek(). All '
                                                                      'operations O(1).',
                                                      'question': 'Design a stack that supports push, pop, top, and '
                                                                  'retrieving the minimum element in constant time.'},
                                                  {   'expected': [   'Doubly linked list for ordering',
                                                                      'Hash map for O(1) key lookup',
                                                                      'Move accessed node to front on get',
                                                                      'Evict tail node on capacity overflow'],
                                                      'model_answer': 'Use HashMap<Key, Node> + DoublyLinkedList. '
                                                                      'get(key): find node in map O(1), move to head '
                                                                      'O(1), return value. put(key,val): if exists '
                                                                      'update and move to head; else create node, add '
                                                                      'to head, if over capacity remove tail and '
                                                                      'delete from map. All O(1).',
                                                      'question': 'Implement an LRU Cache with O(1) get and put '
                                                                  'operations.'}],
                          'sections': [   'Binary Trees & Graphs',
                                          'Dynamic Programming',
                                          'Clean Code & Modularity',
                                          'Leadership Principle: Customer Obsession'],
                          'tips': 'Never start coding immediately. Clarify constraints, propose brute force, optimize '
                                  'to optimal complexity, dry-run edge cases, then code.',
                          'type': 'Technical Interview'},
                      {   'cutoff_percentage': 85,
                          'duration_minutes': 60,
                          'name': 'Technical Interview 2 (Object-Oriented Design & DSA)',
                          'questions_count': 2,
                          'round_number': 3,
                          'sample_questions': [   {   'expected': [   'Doubly linked list for node ordering',
                                                                      'Hash map for O(1) key lookup',
                                                                      'Eviction logic when capacity exceeded'],
                                                      'question': 'Design an LRU (Least Recently Used) Cache with '
                                                                  'get(key) and put(key, value) operations running in '
                                                                  'O(1) time complexity.'},
                                                  {   'expected': [   'Dynamic Programming with Hash Set',
                                                                      'dp[i] = true if s[0:i] can be segmented',
                                                                      'Check dp[j] and s[j:i] in wordDict for j in '
                                                                      'range 0..i',
                                                                      'O(N^2) time and O(N) space'],
                                                      'model_answer': 'Store wordDict in a Hash Set. Declare dp array '
                                                                      'of size len(s)+1 with dp[0] = True. For i from '
                                                                      '1 to len(s), iterate j from 0 to i. If dp[j] is '
                                                                      'True and s[j:i] is in the word set, set dp[i] = '
                                                                      'True and break. Returns dp[len(s)].',
                                                      'question': 'Given a non-empty string s and a dictionary '
                                                                  'wordDict containing a list of non-empty words, '
                                                                  'determine if s can be segmented into a '
                                                                  'space-separated sequence of one or more dictionary '
                                                                  'words.\n'
                                                                  "Input: s = 'leetcode', wordDict = ['leet', 'code']\n"
                                                                  'Output: true'},
                                                  {   'expected': [   'Base62 encoding of auto-increment ID or hash',
                                                                      'Read-heavy: use Redis cache for hot URLs',
                                                                      'Database: NoSQL (DynamoDB) for horizontal '
                                                                      'scaling',
                                                                      'Custom domain support and analytics tracking',
                                                                      'TTL for expiring links'],
                                                      'model_answer': 'Generate short codes using Base62 encoding of a '
                                                                      'distributed sequence generator (Snowflake ID). '
                                                                      'Store mappings in DynamoDB with DAX cache '
                                                                      'layer. Use CloudFront CDN for 301 redirects. '
                                                                      'Track click analytics asynchronously via Kafka.',
                                                      'question': 'Design a URL shortener service like bit.ly that '
                                                                  'handles 100M daily URL creation requests.'}],
                          'sections': [   'Object-Oriented Design (e.g., Parking Lot, Elevator)',
                                          'Data Structures (Trie, LRU Cache)',
                                          'Leadership Principle: Ownership & Deep Dive'],
                          'tips': 'Structure classes with encapsulation and SOLID principles. Be prepared to implement '
                                  'LRU Cache with HashMap + Doubly Linked List.',
                          'type': 'Technical Interview'},
                      {   'cutoff_percentage': 85,
                          'duration_minutes': 60,
                          'name': 'Bar Raiser & Final Behavioral Round',
                          'questions_count': 3,
                          'round_number': 4,
                          'sample_questions': [   {   'expected': [   'Have Backbone; Disagree and Commit LP',
                                                                      'Objective data and benchmarking',
                                                                      'Professional debate',
                                                                      'Committed fully once decision was finalized'],
                                                      'question': 'Tell me about a time when you had a strong '
                                                                  'disagreement with your manager or team lead on a '
                                                                  'technical approach. How did you handle it?'},
                                                  {   'expected': [   'STAR structure',
                                                                      'Objective data and benchmarks used instead of '
                                                                      'emotional debate',
                                                                      'Respectful listening and debate',
                                                                      'Fully committing to the agreed path regardless '
                                                                      'of personal preference',
                                                                      'Measurable positive result'],
                                                      'question': 'Tell me about a time you had a strong technical '
                                                                  'disagreement with your team lead or peer. How did '
                                                                  'you handle it and what was the outcome? (Amazon '
                                                                  'Leadership Principle: Have Backbone; Disagree and '
                                                                  'Commit)'},
                                                  {   'expected': [   'Two-way door vs one-way door decision framework',
                                                                      'Risk assessment and rollback plan',
                                                                      'Speed of execution and bias for action',
                                                                      'Post-launch metrics tracking'],
                                                      'question': 'Give an example of a time you had to make a '
                                                                  'high-stakes technical decision without complete '
                                                                  'data or under severe time pressure. (Amazon '
                                                                  'Leadership Principle: Bias for Action)'},
                                                  {   'answer': 'Describe a project where you had to ship a feature '
                                                                'without full user research data. Explain how you made '
                                                                'a reversible decision, gathered real-time feedback '
                                                                'post-launch, and iterated rapidly. Emphasize speed '
                                                                'over perfection for reversible decisions.',
                                                      'question': 'Tell me about a time you had to make a decision '
                                                                  'with incomplete data. (Leadership Principle: Bias '
                                                                  'for Action)'},
                                                  {   'answer': 'Share how you identified manual repetitive steps in a '
                                                                'deployment or testing workflow, automated them with '
                                                                'scripts or CI/CD pipelines, reduced deployment time '
                                                                'from hours to minutes, and documented the simplified '
                                                                'process for the team.',
                                                      'question': 'Describe a time when you simplified a complex '
                                                                  'process. (Leadership Principle: Invent and '
                                                                  'Simplify)'}],
                          'sections': [   'Bar Raiser Assessment',
                                          'Disagreed and Committed',
                                          'Delivering Results under Ambiguity'],
                          'tips': 'Bar Raiser is an independent interviewer outside the hiring team ensuring the '
                                  'candidate raises the bar of the current team.',
                          'type': 'Bar Raiser & HR'}],
        'slug': 'amazon'},
    {   'badge': 'Elite National Talent Hunt (NTH) / Turbo',
        'description': 'Wipro Elite NTH screens candidates for Project Engineer and Turbo development roles through '
                       'Aptitude, Written Communication, and Coding.',
        'eligibility': '60% or 6.0 CGPA in 10th, 12th, and B.E/B.Tech/5-year Integrated-M.Tech with max 1 active '
                       'backlog.',
        'hiring_season': 'Elite NTH Drives',
        'id': 'wipro',
        'name': 'Wipro',
        'package': 'INR 3.5 LPA - INR 6.5 LPA',
        'rounds': [   {   'cutoff_percentage': 65,
                          'duration_minutes': 128,
                          'name': 'Online Assessment (Cognitive, Essay & Coding)',
                          'questions_count': 52,
                          'round_number': 1,
                          'sample_questions': [   {   'answer': '5% profit',
                                                      'explanation': 'Let CP = 100. MP = 140. SP = 140 * (75/100) = '
                                                                     '105. Profit = 105 - 100 = 5%.',
                                                      'options': ['5% profit', '10% profit', '5% loss', '15% profit'],
                                                      'question': 'A shopkeeper marks an article at 40% above the cost '
                                                                  'price and allows a discount of 25% on the marked '
                                                                  'price. What is his profit or loss percentage?'},
                                                  {   'answer': '2 km/h',
                                                      'explanation': 'Let upstream speed = u, downstream speed = v. '
                                                                     '24/u + 36/v = 6 and 36/u + 24/v = 6.5. Solving '
                                                                     'gives u = 8 km/h, v = 12 km/h. Speed of current '
                                                                     '= (v - u)/2 = (12 - 8)/2 = 2 km/h.',
                                                      'options': ['2 km/h', '3 km/h', '4 km/h', '1.5 km/h'],
                                                      'question': 'A boat travels 24 km upstream and 36 km downstream '
                                                                  'in 6 hours. It also travels 36 km upstream and 24 '
                                                                  'km downstream in 6.5 hours. Find the speed of the '
                                                                  'current.'},
                                                  {   'answer': '6 hours',
                                                      'explanation': 'Rate of 1st + 2nd = 1/10 + 1/15 = 5/30 = 1/6. '
                                                                     'Since these together fill at the same rate the '
                                                                     '3rd empties, 3rd pipe takes 6 hours.',
                                                      'options': ['6 hours', '8 hours', '10 hours', '12 hours'],
                                                      'question': 'A tank is filled by 3 pipes with uniform flow '
                                                                  'rates. The first two pipes operating simultaneously '
                                                                  'fill the tank in the same time during which the '
                                                                  'third pipe alone empties it. The first pipe alone '
                                                                  'fills the tank in 10 hours, the second in 15 hours. '
                                                                  'How long does the third pipe take to empty the '
                                                                  'tank?'}],
                          'sections': [   'Aptitude: Quant, Logical, English (48 Qs)',
                                          'Written Communication: Essay Writing (1 Topic)',
                                          'Online Coding (2 Problems)'],
                          'tips': 'Essay is evaluated by an automated AI engine checking grammar, spelling, and '
                                  'topical keywords. Avoid backspaces where disabled.',
                          'type': 'Aptitude, Essay & Coding'},
                      {   'cutoff_percentage': 70,
                          'duration_minutes': 35,
                          'name': 'Technical & HR Interview',
                          'questions_count': 4,
                          'round_number': 2,
                          'sample_questions': [   {   'expected': [   'Overloading: same class, same method name, '
                                                                      'different parameters (compile-time)',
                                                                      'Overriding: parent-child class, same signature, '
                                                                      'different implementation (runtime)'],
                                                      'question': 'What is the difference between method overloading '
                                                                  'and method overriding in Java? Give a code '
                                                                  'snippet.'},
                                                  {   'expected': [   'DFS with recursion stack tracking (visited '
                                                                      'array + in_stack array)',
                                                                      "Or Kahn's Algorithm (in-degree count)",
                                                                      'O(V + E) time'],
                                                      'model_answer': "Use DFS with two boolean arrays: 'visited' and "
                                                                      "'in_recursion_stack'. For each unvisited node, "
                                                                      'perform DFS: mark visited and '
                                                                      'in_recursion_stack. For each neighbor: if not '
                                                                      'visited, recurse; if already '
                                                                      'in_recursion_stack, a back-edge and cycle is '
                                                                      'detected. When exiting DFS for node, unmark '
                                                                      'in_recursion_stack.',
                                                      'question': 'Given a directed graph, write an algorithm to '
                                                                  'detect whether the graph contains a cycle.\n'
                                                                  'Input: 4 vertices, edges: 0->1, 1->2, 2->3, 3->1\n'
                                                                  'Output: Cycle Detected (1->2->3->1)'},
                                                  {   'expected': [   'Find number of digits n',
                                                                      'Sum each digit raised to power n',
                                                                      'Compare sum with original number',
                                                                      'Handle multi-digit Armstrong numbers (e.g., '
                                                                      '153, 370, 371)'],
                                                      'model_answer': 'def is_armstrong(num):\n'
                                                                      '    digits = str(num)\n'
                                                                      '    n = len(digits)\n'
                                                                      '    return sum(int(d)**n for d in digits) == '
                                                                      'num',
                                                      'question': 'Write a program to check whether a given number is '
                                                                  'an Armstrong number.'}],
                          'sections': [   'Core Programming Language',
                                          'SQL Joins and Indexing',
                                          'Final Year Project',
                                          'HR Questions'],
                          'tips': 'Be confident about your preferred programming language (C/Java/Python). You will be '
                                  'asked syntax and memory allocation questions.',
                          'type': 'Technical & HR'},
                      {   'cutoff_percentage': 70,
                          'duration_minutes': 40,
                          'name': 'Advanced Technical & Problem Solving',
                          'questions_count': 3,
                          'round_number': 3,
                          'sample_questions': [   {   'expected': [   'Use two-pointer technique (left and right)',
                                                                      'Skip non-alphanumeric characters',
                                                                      'Compare lowercase characters',
                                                                      'Time complexity O(N), space complexity O(1)'],
                                                      'model_answer': 'Place a left pointer at index 0 and a right '
                                                                      'pointer at len - 1. While left < right, '
                                                                      'increment left if character is not '
                                                                      'alphanumeric, decrement right if not '
                                                                      'alphanumeric. If lower(str[left]) != '
                                                                      'lower(str[right]), return false. If loop '
                                                                      'finishes, return true. O(N) time and O(1) '
                                                                      'space.',
                                                      'question': 'Write an optimal function to check whether a given '
                                                                  'string is a palindrome, ignoring non-alphanumeric '
                                                                  'characters and case sensitivity.'},
                                                  {   'expected': [   'A table can have only ONE Primary Key, but '
                                                                      'MULTIPLE Unique Keys',
                                                                      'Primary Key strictly forbids NULL values; '
                                                                      'Unique Key allows one (or multiple in some '
                                                                      'engines) NULL value',
                                                                      'Primary Key automatically defaults to a '
                                                                      'clustered index in most engines'],
                                                      'model_answer': 'A Primary Key uniquely identifies each row and '
                                                                      'strictly disallows NULLs; a table can possess '
                                                                      'only one primary key. A Unique Key enforces '
                                                                      'uniqueness across a column but allows NULL '
                                                                      'values, and a table can define multiple unique '
                                                                      'keys.',
                                                      'question': 'What is the difference between Primary Key and '
                                                                  'Unique Key constraints in a relational database?'},
                                                  {   'expected': [   'Encapsulation: bundling data with methods (bank '
                                                                      'account hiding balance)',
                                                                      'Abstraction: hiding complex implementation (car '
                                                                      'steering wheel)',
                                                                      'Inheritance: code reuse (Employee extends '
                                                                      'Person)',
                                                                      'Polymorphism: one interface multiple forms '
                                                                      '(shape.area() for circle/rectangle)'],
                                                      'model_answer': '1. Encapsulation: BankAccount class hides '
                                                                      'balance, exposes deposit()/withdraw(). 2. '
                                                                      'Abstraction: Driver uses accelerate() without '
                                                                      'knowing engine internals. 3. Inheritance: '
                                                                      'ElectricCar extends Car inheriting drive() but '
                                                                      'adding charge(). 4. Polymorphism: draw(Shape s) '
                                                                      'works for Circle, Rectangle, Triangle through '
                                                                      'method overriding.',
                                                      'question': 'Explain the four pillars of Object-Oriented '
                                                                  'Programming with real-world examples.'}],
                          'sections': ['Data Structures', 'Database Management', 'C/Java/Python Syntax', 'Debugging'],
                          'tips': 'Expect live code writing on arrays, strings, and fundamental SQL queries.',
                          'type': 'Technical Interview'},
                      {   'cutoff_percentage': 70,
                          'duration_minutes': 25,
                          'name': 'HR & Cultural Alignment',
                          'questions_count': 3,
                          'round_number': 4,
                          'sample_questions': [   {   'answer': "Detail Wipro's transition from vegetable oil in 1945 "
                                                                'to a premier global technology firm. Highlight the '
                                                                "four values: Passion for clients' success, Respect "
                                                                'for each person, Global & responsible citizenship, '
                                                                'and Unyielding integrity in everything we do.',
                                                      'question': "What do you know about Wipro and the 'Spirit of "
                                                                  "Wipro' values?"}],
                          'sections': ['Spirit of Wipro', 'Client Focus', 'Continuous Learning', 'Team Spirit'],
                          'tips': "Mention the 'Spirit of Wipro' values: Be passionate about clients' success, Treat "
                                  'each person with respect, Be global and responsible, Unyielding integrity.',
                          'type': 'HR & Behavioral'}],
        'slug': 'wipro'},
    {   'badge': 'GenC / GenC Elevate / GenC Next',
        'description': 'Cognizant divides placement hires into GenC (4 LPA), GenC Elevate (4.5 LPA), and GenC Next '
                       '(6.75 LPA) based on coding and technical proficiency.',
        'eligibility': '60% or 6.0 CGPA in 10th, 12th, and UG/PG without active backlogs.',
        'hiring_season': 'On-Campus Campus Drives',
        'id': 'cognizant',
        'name': 'Cognizant',
        'package': 'INR 4.0 LPA - INR 6.75 LPA',
        'rounds': [   {   'cutoff_percentage': 65,
                          'duration_minutes': 100,
                          'name': 'Cognizant Assessment (Aptitude & Automata Fix)',
                          'questions_count': 60,
                          'round_number': 1,
                          'sample_questions': [   {   'answer': 'if (n <= 1) return 1;',
                                                      'explanation': '0! = 1 and 1! = 1. Returning 0 causes the entire '
                                                                     'multiplication product to collapse to zero.',
                                                      'options': [   'if (n <= 1) return 1;',
                                                                     'if (n == 0) return n;',
                                                                     'if (n == 2) return 2;',
                                                                     'while (n > 0) return n;'],
                                                      'question': 'In a debugging snippet for finding the factorial of '
                                                                  "N, the base case says 'if (n == 0) return 0;'. What "
                                                                  'is the corrected base case?'},
                                                  {   'expected': [   'Synchronous blocks waiting for I/O',
                                                                      'Asynchronous registers callbacks/promises and '
                                                                      'yields CPU',
                                                                      'Thread pool allocates fixed worker threads, '
                                                                      'queueing requests when saturated'],
                                                      'question': 'What is the difference between synchronous '
                                                                  'execution and asynchronous execution in web '
                                                                  'backends? How does a thread pool handle concurrent '
                                                                  'socket requests?'},
                                                  {   'answer': '243',
                                                      'explanation': 'Each term is multiplied by 3. 81 × 3 = 243. '
                                                                     'Geometric progression with r = 3.',
                                                      'options': ['243', '162', '189', '216'],
                                                      'question': 'Find the missing number: 3, 9, 27, 81, ?'},
                                                  {   'answer': '15',
                                                      'explanation': 'Total man-days = 5 × 12 = 60. For 4 days: 60/4 = '
                                                                     '15 men.',
                                                      'options': ['15', '12', '10', '20'],
                                                      'question': 'If 5 men can do a work in 12 days, how many men are '
                                                                  'needed to complete it in 4 days?'}],
                          'sections': [   'Quantitative & Analytical Ability',
                                          'Verbal Ability',
                                          'Automata Fix (Code Debugging)'],
                          'tips': 'Automata Fix presents pre-written code with logical or syntactic bugs. You must '
                                  'identify and fix the bug in under 2 minutes per snippet.',
                          'type': 'Aptitude & Debugging'},
                      {   'cutoff_percentage': 70,
                          'duration_minutes': 35,
                          'name': 'Technical & HR Interview',
                          'questions_count': 4,
                          'round_number': 2,
                          'sample_questions': [   {   'expected': [   'Synchronous blocks until response is returned',
                                                                      'Asynchronous returns immediately with callback '
                                                                      'or future',
                                                                      'Message queues (RabbitMQ/Kafka) decouple '
                                                                      'producers and consumers for high throughput'],
                                                      'question': 'What is the difference between synchronous and '
                                                                  'asynchronous API execution, and when would you use '
                                                                  'a message queue?'},
                                                  {   'expected': [   'Min-Heap of size k',
                                                                      'Insert elements; when size > k, pop smallest',
                                                                      'Root of Min-Heap holds k-th largest',
                                                                      'O(N log K) time and O(K) space'],
                                                      'model_answer': 'Maintain a Min-Heap of capacity k. Iterate '
                                                                      'through each number in nums and push into heap. '
                                                                      'If heap size exceeds k, pop the minimum '
                                                                      'element. After scanning all elements, the top '
                                                                      'of the Min-Heap is guaranteed to be the k-th '
                                                                      'largest element in O(N log K) time.',
                                                      'question': 'Given an integer array nums and an integer k, find '
                                                                  'the k-th largest element in the array in O(N log K) '
                                                                  'time.\n'
                                                                  'Input: nums = [3,2,1,5,6,4], k = 2\n'
                                                                  'Output: 5'},
                                                  {   'expected': [   'Use hash map to count character frequencies',
                                                                      'Second pass to find first char with count 1',
                                                                      'O(N) time, O(1) space (bounded alphabet)'],
                                                      'model_answer': 'def first_non_repeating(s):\n'
                                                                      '    freq = {}\n'
                                                                      '    for c in s: freq[c] = freq.get(c, 0) + 1\n'
                                                                      '    for c in s:\n'
                                                                      '        if freq[c] == 1: return c\n'
                                                                      '    return None',
                                                      'question': 'Write a function to find the first non-repeating '
                                                                  'character in a string.'}],
                          'sections': [   'Data Structures',
                                          'Database Normalization',
                                          'Web Technologies & APIs',
                                          'Willingness to learn new stacks'],
                          'tips': 'Cognizant values versatility across modern full-stack technologies (Java Spring '
                                  'Boot, Python FastAPI, or React).',
                          'type': 'Technical & HR'},
                      {   'cutoff_percentage': 70,
                          'duration_minutes': 45,
                          'name': 'Domain Technical & Machine Coding',
                          'questions_count': 4,
                          'round_number': 3,
                          'sample_questions': [   {   'expected': [   'Use a Hash Map to store numbers or their '
                                                                      'complements',
                                                                      'For each number x, check if (target - x) exists '
                                                                      'in the map',
                                                                      'Single pass through array yields O(N) time and '
                                                                      'O(N) space'],
                                                      'model_answer': 'Use a hash map. Iterate through the array; for '
                                                                      'each element arr[i], compute complement = '
                                                                      'target - arr[i]. If complement exists in map, '
                                                                      'return [map[complement], i]. Otherwise, insert '
                                                                      'arr[i] into map. This runs in O(N) time and '
                                                                      'O(N) space.',
                                                      'question': 'Given an array of integers and a target sum, how do '
                                                                  'you find two numbers that sum up to the target in '
                                                                  '$O(N)$ time?'},
                                                  {   'expected': [   'Atomicity: All operations succeed or all roll '
                                                                      'back',
                                                                      'Consistency: Database transitions from one '
                                                                      'valid state to another',
                                                                      'Isolation: Concurrent transactions do not '
                                                                      'interfere',
                                                                      'Durability: Committed data survives crashes'],
                                                      'model_answer': 'ACID stands for Atomicity, Consistency, '
                                                                      'Isolation, and Durability. In banking, if money '
                                                                      'is debited from Account A but the credit to '
                                                                      'Account B fails, Atomicity ensures the debit is '
                                                                      'rolled back, preventing lost funds.',
                                                      'question': 'What are ACID properties in database management, '
                                                                  'and why are they critical in financial software?'}],
                          'sections': ['Algorithms', 'Web Technologies', 'SQL & Database', 'OOP Principles'],
                          'tips': 'GenC Next focuses heavily on problem solving, OOP design, and explaining time/space '
                                  'complexities.',
                          'type': 'Technical Interview'},
                      {   'cutoff_percentage': 70,
                          'duration_minutes': 30,
                          'name': 'HR & Leadership Assessment',
                          'questions_count': 3,
                          'round_number': 4,
                          'sample_questions': [   {   'answer': 'Describe your goal of mastering full-stack or cloud '
                                                                'engineering, contributing to mission-critical '
                                                                'customer delivery, gaining industry certifications '
                                                                '(e.g. AWS/Azure), and stepping into technical module '
                                                                'leadership.',
                                                      'question': 'Where do you see yourself in 3 years at '
                                                                  'Cognizant?'}],
                          'sections': ['Communication', 'Career Vision', 'Adaptability', 'Professionalism'],
                          'tips': 'Articulate clear career goals for your first 2 years in software development.',
                          'type': 'HR & Behavioral'}],
        'slug': 'cognizant'},
    {   'badge': 'Exceller / Senior Analyst',
        'description': 'Capgemini Exceller hiring screens for Analyst (4.25 LPA) and Senior Analyst (7.5 LPA) through '
                       'Game-Based Aptitude and Pseudocode assessments.',
        'eligibility': '60% or 6.0 CGPA throughout 10th, 12th, and UG with no active backlog.',
        'hiring_season': 'On-Campus Exceller Drives',
        'id': 'capgemini',
        'name': 'Capgemini',
        'package': 'INR 4.25 LPA - INR 7.5 LPA',
        'rounds': [   {   'cutoff_percentage': 65,
                          'duration_minutes': 50,
                          'name': 'Cognitive & Game-Based Assessment',
                          'questions_count': 4,
                          'round_number': 1,
                          'sample_questions': [   {   'answer': 'Cannot be determined with certainty',
                                                      'explanation': "Because only 'some' electronic gadgets are "
                                                                     'battery operated, we cannot logically conclude '
                                                                     'that all laptops are among those battery '
                                                                     'operated.',
                                                      'options': [   'Definitely True',
                                                                     'Definitely False',
                                                                     'Cannot be determined with certainty',
                                                                     'Only in low power mode'],
                                                      'question': 'In a deductive logic challenge: All laptops are '
                                                                  'electronic gadgets. Some electronic gadgets are '
                                                                  'battery operated. Therefore, are all laptops '
                                                                  'battery operated?'},
                                                  {   'answer': 'Merge Sort',
                                                      'explanation': 'Merge Sort guarantees O(N log N) worst-case time '
                                                                     'and preserves the relative order of elements '
                                                                     'with equal keys (Stability). Quick Sort and Heap '
                                                                     'Sort are not stable in their standard '
                                                                     'implementations.',
                                                      'options': [   'Merge Sort',
                                                                     'Quick Sort',
                                                                     'Heap Sort',
                                                                     'Selection Sort'],
                                                      'question': 'Which of the following sorting algorithms is Stable '
                                                                  'and has a worst-case time complexity of O(N log '
                                                                  'N)?'},
                                                  {   'answer': '54',
                                                      'explanation': 'Let numbers be 3x and 5x. 5x - 3x = 36 → 2x = 36 '
                                                                     '→ x = 18. Smaller = 3×18 = 54.',
                                                      'options': ['54', '48', '45', '63'],
                                                      'question': 'Two numbers are in the ratio 3:5 and their '
                                                                  'difference is 36. Find the smaller number.'},
                                                  {   'answer': '7.5°',
                                                      'explanation': 'At 3:15, minute hand at 90°. Hour hand at 30×3 + '
                                                                     '0.5×15 = 90+7.5 = 97.5°. Angle = |97.5 - 90| = '
                                                                     '7.5°.',
                                                      'options': ['7.5°', '0°', '15°', '22.5°'],
                                                      'question': 'A clock shows 3:15 PM. What is the angle between '
                                                                  'the hour and minute hands?'}],
                          'sections': [   'Grid Challenge',
                                          'Motion Challenge',
                                          'Deductive-Logical Challenge',
                                          'Inductive-Logical Challenge'],
                          'tips': 'Practice memory recall, visual-spatial reasoning, and swift decision making. No '
                                  'negative marking.',
                          'type': 'Gamified Aptitude'},
                      {   'cutoff_percentage': 65,
                          'duration_minutes': 30,
                          'name': 'Pseudocode & Code Debugging',
                          'questions_count': 30,
                          'round_number': 2,
                          'sample_questions': [   {   'answer': '11',
                                                      'explanation': 'For any two integers p and q, (p ^ q) + 2*(p & '
                                                                     'q) = p + q. Here (p ^ q) + (p & q) = (p + q) - '
                                                                     '(p & q). For 4 and 7: p=0100_2, q=0111_2. p ^ q '
                                                                     '= 0011_2 = 3. p & q = 0100_2 = 4. Wait, 3 + 4 = '
                                                                     '7! Wait: 4^7 = 3, 4&7 = 4, 3+4 = 7.',
                                                      'options': ['11', '12', '7', '4'],
                                                      'question': 'What is the output of the pseudocode?\n'
                                                                  'Integer p, q, r\n'
                                                                  'Set p = 4, q = 7\n'
                                                                  'r = (p ^ q) + (p & q)\n'
                                                                  'Print r'},
                                                  {   'expected': [   'Three pointers starting from the back (m - 1, n '
                                                                      '- 1, m + n - 1)',
                                                                      'Fill largest element from the end of nums1',
                                                                      'O(M + N) time and O(1) extra space'],
                                                      'model_answer': 'Set pointer p1 = m - 1, p2 = n - 1, and write '
                                                                      'pointer p = m + n - 1. While p2 >= 0: if p1 >= '
                                                                      '0 and nums1[p1] > nums2[p2], nums1[p] = '
                                                                      'nums1[p1], p1--; else nums1[p] = nums2[p2], '
                                                                      'p2--; p--. Runs in O(M + N) time with zero '
                                                                      'extra memory.',
                                                      'question': 'Given two sorted arrays nums1 and nums2, merge them '
                                                                  'into a single sorted array in-place without '
                                                                  'allocating extra space.\n'
                                                                  'Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = '
                                                                  '[2,5,6], n = 3\n'
                                                                  'Output: [1,2,2,3,5,6]'},
                                                  {   'expected': [   'Initialize max_so_far and max_ending_here',
                                                                      'Iterate through array',
                                                                      'max_ending_here = max(arr[i], max_ending_here + '
                                                                      'arr[i])',
                                                                      'Update max_so_far if max_ending_here is larger',
                                                                      'O(N) time, O(1) space'],
                                                      'model_answer': 'max_so_far = max_here = arr[0]\n'
                                                                      'for i in range(1, len(arr)):\n'
                                                                      '    max_here = max(arr[i], max_here + arr[i])\n'
                                                                      '    max_so_far = max(max_so_far, max_here)\n'
                                                                      'return max_so_far',
                                                      'question': 'Write pseudocode to find the maximum sum subarray '
                                                                  "in an array of integers (Kadane's Algorithm)."}],
                          'sections': ['Data Structures', 'Loops and Bitwise Operations', 'Algorithm Tracing'],
                          'tips': 'Pay close attention to pre/post increments, bitwise XOR/AND shifts, and nested '
                                  'loops.',
                          'type': 'Technical MCQ'},
                      {   'cutoff_percentage': 70,
                          'duration_minutes': 35,
                          'name': 'Technical & HR Interview',
                          'questions_count': 3,
                          'round_number': 3,
                          'sample_questions': [   {   'expected': [   'Clustered index physically sorts data in table',
                                                                      'Only one clustered index per table',
                                                                      'Non-clustered creates separate search tree with '
                                                                      'pointers to row data'],
                                                      'question': 'Explain the difference between clustered and '
                                                                  'non-clustered indexing in relational databases.'},
                                                  {   'answer': 'Choose a genuine failure (e.g., underestimating '
                                                                'project timeline, a bug in production). Describe the '
                                                                'impact, how you took ownership, the corrective '
                                                                'actions taken, and the lasting lesson learned (better '
                                                                'estimation, more thorough testing, communication '
                                                                'habits).',
                                                      'question': 'Tell me about a time you failed at something and '
                                                                  'what you learned from it.'}],
                          'sections': ['OOPs Principles', 'Database Queries', 'Project Architecture', 'Adaptability'],
                          'tips': 'Be confident about your final year project and understand how web clients talk to '
                                  'relational databases.',
                          'type': 'Technical & HR'}],
        'slug': 'capgemini'},
    {   'badge': 'First Careers / Graduate Engineer Trainee',
        'description': 'Global technology firm specializing in digital engineering, cloud services, and enterprise '
                       'software.',
        'eligibility': '65% throughout 10th, 12th, and B.Tech with max 1 active backlog.',
        'hiring_season': 'Campus Connect & Elite Drives',
        'id': 'hcltech',
        'name': 'HCLTech',
        'package': 'INR 3.65 LPA - INR 5.0 LPA',
        'rounds': [   {   'cutoff_percentage': 60,
                          'duration_minutes': 75,
                          'name': 'Online Aptitude & Technical Assessment',
                          'questions_count': 60,
                          'round_number': 1,
                          'sample_questions': [   {   'answer': '30 hours',
                                                      'explanation': 'Net rate per hour = 1/12 - 1/20 = (5 - 3)/60 = '
                                                                     '2/60 = 1/30. Thus, tank fills in 30 hours.',
                                                      'options': ['30 hours', '32 hours', '28 hours', '24 hours'],
                                                      'question': 'A pipe can fill a cistern in 12 hours while another '
                                                                  'empties it in 20 hours. If both are opened '
                                                                  'together, how long will it take to fill the tank?'},
                                                  {   'answer': '112.5 km/h',
                                                      'explanation': 'Total distance = 450 km, total time = 5 h. First '
                                                                     'half = 225 km at 75 km/h takes 225/75 = 3 hours. '
                                                                     'Remaining time = 5 - 3 = 2 hours. Required speed '
                                                                     'for remaining 225 km = 225 / 2 = 112.5 km/h.',
                                                      'options': ['112.5 km/h', '100 km/h', '125 km/h', '90 km/h'],
                                                      'question': 'A car covers a distance of 450 km in 5 hours. If it '
                                                                  'travels the first half of the distance at 75 km/h, '
                                                                  'at what speed must it travel the second half to '
                                                                  'complete the journey on time?'},
                                                  {   'answer': '30',
                                                      'explanation': 'Pointer arithmetic: `ptr` points to arr[0]. '
                                                                     '`*(ptr + 2)` dereferences arr[2], which holds '
                                                                     'value 30.',
                                                      'options': ['30', '20', '10', '40'],
                                                      'question': 'What is the output of the following C code?\n'
                                                                  '#include <stdio.h>\n'
                                                                  'int main() {\n'
                                                                  '  int arr[] = {10, 20, 30, 40};\n'
                                                                  '  int *ptr = arr;\n'
                                                                  "  printf('%d', *(ptr + 2));\n"
                                                                  '  return 0;\n'
                                                                  '}'},
                                                  {   'answer': 'M14N',
                                                      'explanation': 'Letters step by +3: A(+3)=D, D(+3)=G, G(+3)=J, '
                                                                     'J(+3)=M. Numbers step by +3: 2(+3)=5, 5(+3)=8, '
                                                                     '8(+3)=11, 11(+3)=14. Third letter steps by +3: '
                                                                     'C(+3)=F, F(+3)=I, I(+3)=L, L(+3)=O. Wait, L(+3) '
                                                                     "is O! Let's check: M14O is option B.",
                                                      'options': ['M14N', 'M14O', 'N14O', 'M13O'],
                                                      'question': 'What is the next term in the alphanumeric series: '
                                                                  'A2C, D5F, G8I, J11L, ?'},
                                                  {   'answer': '24 years',
                                                      'explanation': 'Doubles in 8 years: Interest = P in 8 years. '
                                                                     'Rate = 100/8 = 12.5%. To become 4 times: '
                                                                     'Interest = 3P. Time = 3 * 8 = 24 years.',
                                                      'options': ['24 years', '16 years', '32 years', '20 years'],
                                                      'question': 'A sum of money doubles itself at simple interest in '
                                                                  '8 years. In how many years will it become 4 times '
                                                                  'itself at the same rate?'}],
                          'sections': [   'Quantitative Aptitude',
                                          'Logical Reasoning',
                                          'English Verbal',
                                          'Core Technical MCQs'],
                          'tips': 'Focus on high accuracy in quantitative percentages, time-work, and basic C/Java '
                                  'syntax.',
                          'type': 'Aptitude & Technical MCQ'},
                      {   'cutoff_percentage': 65,
                          'duration_minutes': 35,
                          'name': 'Technical Interview',
                          'questions_count': 3,
                          'round_number': 2,
                          'sample_questions': [   {   'expected': [   'Process has independent memory space',
                                                                      'Threads share heap and memory of parent process',
                                                                      'Synchronization prevents race conditions using '
                                                                      'mutexes or semaphores'],
                                                      'question': 'What is the difference between a process and a '
                                                                  'thread? Explain thread synchronization.'},
                                                  {   'expected': [   'Count frequencies using fixed 26-element array '
                                                                      'or hash map',
                                                                      'Check lengths first',
                                                                      'O(N) time and O(1) space',
                                                                      'Case-insensitive handling'],
                                                      'model_answer': 'def are_anagrams(s1, s2):\n'
                                                                      '    if len(s1) != len(s2): return False\n'
                                                                      '    counts = [0] * 26\n'
                                                                      '    for c1, c2 in zip(s1.lower(), s2.lower()):\n'
                                                                      "        counts[ord(c1) - ord('a')] += 1\n"
                                                                      "        counts[ord(c2) - ord('a')] -= 1\n"
                                                                      '    return all(x == 0 for x in counts)',
                                                      'question': 'Write a function to check if two strings are '
                                                                  "anagrams of each other (e.g., 'listen' and "
                                                                  "'silent')."}],
                          'sections': ['C/C++ or Java Programming', 'SQL queries', 'Operating System Basics'],
                          'tips': 'Review memory management, difference between process and thread, and write simple '
                                  'SQL queries.',
                          'type': 'Technical Interview'},
                      {   'cutoff_percentage': 70,
                          'duration_minutes': 45,
                          'name': 'Advanced Technical & Problem Solving',
                          'questions_count': 4,
                          'round_number': 3,
                          'sample_questions': [   {   'expected': [   'Use fast and slow pointer technique (Tortoise '
                                                                      'and Hare)',
                                                                      'Slow moves 1 step while Fast moves 2 steps',
                                                                      'When Fast reaches null or end, Slow is at the '
                                                                      'middle node',
                                                                      'Time complexity O(N), Space complexity O(1)'],
                                                      'model_answer': 'Initialize two pointers, slow and fast, at the '
                                                                      'head. Advance slow by 1 node and fast by 2 '
                                                                      'nodes in each iteration. When fast reaches null '
                                                                      'or fast.next is null, slow points precisely to '
                                                                      'the middle node. This requires O(N) time and '
                                                                      'O(1) auxiliary space.',
                                                      'question': 'Given the head of a singly linked list, how do you '
                                                                  'find the middle element in a single pass without '
                                                                  'knowing the list length in advance?'},
                                                  {   'expected': [   'INNER JOIN returns only matching rows from both '
                                                                      'tables',
                                                                      'LEFT JOIN returns all rows from left table plus '
                                                                      'matching rows from right (nulls for '
                                                                      'non-matches)',
                                                                      'FULL OUTER JOIN returns all rows from both '
                                                                      'tables, filling nulls where no match exists'],
                                                      'model_answer': 'INNER JOIN returns employees assigned to '
                                                                      'existing departments. LEFT JOIN returns all '
                                                                      'employees, including new hires without an '
                                                                      'assigned department. FULL OUTER JOIN returns '
                                                                      'all employees and all departments, including '
                                                                      'departments with zero assigned employees.',
                                                      'question': 'What is the difference between INNER JOIN, LEFT '
                                                                  'OUTER JOIN, and FULL OUTER JOIN in SQL? Give a '
                                                                  'real-world employee-department example.'}],
                          'sections': ['Data Structures', 'REST APIs', 'SQL Joins', 'Debugging'],
                          'tips': 'Be ready to write clean code on an online IDE and explain edge cases.',
                          'type': 'Technical Interview'},
                      {   'cutoff_percentage': 70,
                          'duration_minutes': 30,
                          'name': 'HR & Cultural Fitment',
                          'questions_count': 3,
                          'round_number': 4,
                          'sample_questions': [   {   'answer': "Discuss HCLTech's Ideapreneurship culture, empowering "
                                                                'employees to innovate at the grassroots level. Give '
                                                                'an example from college where you learned a new '
                                                                'programming framework (like React or FastAPI) within '
                                                                'two weeks to complete a capstone project.',
                                                      'question': 'Why do you want to start your professional '
                                                                  'engineering career at HCLTech, and how do you '
                                                                  'handle rapidly learning new technology stacks?'},
                                                  {   'answer': 'Affirm that starting your career requires '
                                                                'adaptability and immersion in live customer '
                                                                'environments across India or abroad, and emphasize '
                                                                'that project success and client satisfaction are your '
                                                                'primary priorities.',
                                                      'question': 'Are you comfortable with relocation to different '
                                                                  'client locations and working in rotational project '
                                                                  'shifts?'}],
                          'sections': [   'Communication',
                                          'Career Goals',
                                          'Workplace Adaptability',
                                          'HCLTech Core Values'],
                          'tips': 'Demonstrate flexibility regarding location and shifts, and emphasize eagerness to '
                                  'learn digital engineering.',
                          'type': 'HR & Behavioral'}],
        'slug': 'hcltech'},
    {   'badge': 'Supercoder / Associate Software Engineer',
        'description': 'Digital transformation, consulting, and business re-engineering services provider under '
                       'Mahindra Group.',
        'eligibility': '60% or 6.0 CGPA throughout 10th, 12th, and Engineering with no active backlogs.',
        'hiring_season': 'Campus Drives & Off-Campus',
        'id': 'techmahindra',
        'name': 'Tech Mahindra',
        'package': 'INR 3.5 LPA - INR 5.5 LPA',
        'rounds': [   {   'cutoff_percentage': 60,
                          'duration_minutes': 65,
                          'name': 'Online Assessment & Essay Writing',
                          'questions_count': 55,
                          'round_number': 1,
                          'sample_questions': [   {   'answer': '158',
                                                      'explanation': 'Pattern: 3*2 + 2 = 8, 8*2 + 2 = 18, 18*2 + 2 = '
                                                                     '38, 38*2 + 2 = 78, 78*2 + 2 = 158.',
                                                      'options': ['158', '156', '162', '148'],
                                                      'question': 'Find the next number in the series: 3, 8, 18, 38, '
                                                                  '78, ...?'},
                                                  {   'answer': 'INR 700',
                                                      'explanation': 'SP = CP * (1 + Profit%). 840 = CP * 1.20 => CP = '
                                                                     '840 / 1.20 = INR 700.',
                                                      'options': ['INR 700', 'INR 720', 'INR 750', 'INR 680'],
                                                      'question': 'A merchant sells an article for INR 840 making a '
                                                                  'profit of 20%. What was the cost price of the '
                                                                  'article?'},
                                                  {   'answer': '120',
                                                      'explanation': 'SMART has 5 distinct letters. Total permutations '
                                                                     '= 5! = 5 * 4 * 3 * 2 * 1 = 120.',
                                                      'options': ['120', '24', '720', '60'],
                                                      'question': 'In how many different ways can the letters of the '
                                                                  "word 'SMART' be arranged?"},
                                                  {   'answer': '110101',
                                                      'explanation': '53 = 32 + 16 + 4 + 1 = 2^5 + 2^4 + 2^2 + 2^0 = '
                                                                     '110101 in binary.',
                                                      'options': ['110101', '110111', '101101', '111001'],
                                                      'question': 'What is the binary representation of the decimal '
                                                                  'number 53?'}],
                          'sections': ['Numerical Ability', 'Analytical Reasoning', 'Written English Communication'],
                          'tips': 'Essay writing is evaluated automatically for grammar, spelling, and coherence.',
                          'type': 'Aptitude & Essay'},
                      {   'cutoff_percentage': 60,
                          'duration_minutes': 45,
                          'name': 'Supercoder Hands-on Coding',
                          'questions_count': 2,
                          'round_number': 2,
                          'sample_questions': [   {   'expected': [   'Reverse entire array',
                                                                      'Reverse first K elements',
                                                                      'Reverse remaining N-K elements'],
                                                      'question': 'Write an algorithm to rotate an array of size N to '
                                                                  'the right by K steps in O(N) time and O(1) space.'},
                                                  {   'expected': [   'Use a Hash Set to track seen elements',
                                                                      'Maintain write index or append to new list',
                                                                      'O(N) time, O(N) space',
                                                                      'Preserve relative order'],
                                                      'model_answer': 'seen = set()\n'
                                                                      'result = []\n'
                                                                      'for x in arr:\n'
                                                                      '    if x not in seen:\n'
                                                                      '        seen.add(x)\n'
                                                                      '        result.append(x)\n'
                                                                      'return result',
                                                      'question': 'Write an algorithm to remove all duplicate elements '
                                                                  'from an unsorted integer array in $O(N)$ time.'}],
                          'sections': ['Array and String Algorithms', 'Mathematical Logic'],
                          'tips': 'Clean code with zero compilation errors is mandatory to qualify for the higher '
                                  'package bracket.',
                          'type': 'Coding Assessment'},
                      {   'cutoff_percentage': 70,
                          'duration_minutes': 40,
                          'name': 'Core CS & Project Architecture',
                          'questions_count': 3,
                          'round_number': 3,
                          'sample_questions': [   {   'expected': [   '1NF: Atomic values only, no repeating groups',
                                                                      '2NF: In 1NF and no partial dependency (non-key '
                                                                      'attributes depend on whole composite key)',
                                                                      '3NF: In 2NF and no transitive dependency (no '
                                                                      'non-key attribute depends on another non-key '
                                                                      'attribute)'],
                                                      'model_answer': '1NF ensures every cell contains a single atomic '
                                                                      'value. 2NF removes partial functional '
                                                                      'dependencies where an attribute depends on only '
                                                                      'part of a composite primary key. 3NF removes '
                                                                      'transitive dependencies where a non-prime '
                                                                      'attribute depends on another non-prime '
                                                                      'attribute, ensuring data is updated in one '
                                                                      'authoritative place.',
                                                      'question': 'Explain 1NF, 2NF, and 3NF database normalization '
                                                                  'with a simple table example.'},
                                                  {   'expected': [   'Clear separation of concerns (controller, '
                                                                      'service, repository)',
                                                                      'Choice of database (SQL vs NoSQL) justified by '
                                                                      'data structure',
                                                                      'Handling authentication and API security'],
                                                      'model_answer': 'Walk through your project using the 3-tier '
                                                                      'architecture: client UI, REST API backend, and '
                                                                      'relational database. Explain how you created '
                                                                      'schema relationships, indexed high-traffic '
                                                                      'tables, and used token-based authentication '
                                                                      '(JWT) to secure user endpoints.',
                                                      'question': 'How did you design the backend and database '
                                                                  'architecture in your major college project?'},
                                                  {   'expected': [   'Clustered index defines physical order of data '
                                                                      'on disk (only one per table)',
                                                                      'Non-clustered index is a separate B-tree of '
                                                                      'pointers back to rows (multiple allowed)',
                                                                      'Clustered index faster for range queries'],
                                                      'model_answer': 'A clustered index determines the physical order '
                                                                      'in which rows are stored on disk; hence only '
                                                                      'one can exist per table. A non-clustered index '
                                                                      'creates a separate structure containing indexed '
                                                                      'keys and pointers to the actual data rows; '
                                                                      'multiple non-clustered indexes can be created '
                                                                      'on a table.',
                                                      'question': 'What is the difference between a clustered and '
                                                                  'non-clustered index in SQL?'}],
                          'sections': ['DBMS Normalization', 'OOP Concepts', 'Final Year Project', 'API Architecture'],
                          'tips': 'Be thorough with every layer of your academic project and explain how you chose '
                                  'your database.',
                          'type': 'Technical Interview'},
                      {   'cutoff_percentage': 70,
                          'duration_minutes': 30,
                          'name': 'Managerial & Fitment Assessment',
                          'questions_count': 3,
                          'round_number': 4,
                          'sample_questions': [   {   'answer': 'Use the STAR method: explain the disagreement (e.g. '
                                                                'choice of tech stack), how you organized an objective '
                                                                'pros-and-cons discussion focused on project '
                                                                'deadlines, arrived at a compromise, and delivered the '
                                                                'project on time.',
                                                      'question': 'Describe a situation during a team assignment or '
                                                                  'hackathon where team members had conflicting '
                                                                  'opinions. How did you resolve it?'}],
                          'sections': ['Team Collaboration', 'Handling Pressure', 'Company Knowledge', 'Ethics'],
                          'tips': 'Emphasize collaborative mindset and adaptability to enterprise communication '
                                  'platforms.',
                          'type': 'HR & Behavioral'}],
        'slug': 'techmahindra'},
    {   'badge': 'Sparks / Graduate Trainee',
        'description': 'Global technology consulting and digital solutions company formed by the merger of L&T '
                       'Infotech and Mindtree.',
        'eligibility': '60% or 6.0 CGPA throughout 10th, 12th, and Graduation.',
        'hiring_season': 'Campus Ignite Drives',
        'id': 'ltimindtree',
        'name': 'LTIMindtree',
        'package': 'INR 4.0 LPA - INR 6.5 LPA',
        'rounds': [   {   'cutoff_percentage': 65,
                          'duration_minutes': 90,
                          'name': 'Comprehensive Online Assessment',
                          'questions_count': 52,
                          'round_number': 1,
                          'sample_questions': [   {   'answer': '9 days',
                                                      'explanation': '12 men = 18 women => 1 man = 1.5 women. 8 men + '
                                                                     '16 women = 8*1.5 + 16 = 28 women. Days = (18 * '
                                                                     '14) / 28 = 9 days.',
                                                      'options': ['9 days', '10 days', '12 days', '8 days'],
                                                      'question': 'If 12 men or 18 women can reap a field in 14 days, '
                                                                  'then in how many days can 8 men and 16 women reap '
                                                                  'the same field?'},
                                                  {   'answer': 'false true',
                                                      'explanation': "'==' compares object memory references: s1 is in "
                                                                     'String Constant Pool, s2 is a new heap object '
                                                                     "(different addresses => false). '.equals()' "
                                                                     'compares string content character by character '
                                                                     "('LTI' == 'LTI' => true).",
                                                      'options': [   'false true',
                                                                     'true true',
                                                                     'false false',
                                                                     'true false'],
                                                      'question': 'What is the output of the following Java snippet?\n'
                                                                  'public class Test {\n'
                                                                  '  public static void main(String[] args) {\n'
                                                                  "    String s1 = 'LTI';\n"
                                                                  "    String s2 = new String('LTI');\n"
                                                                  "    System.out.println((s1 == s2) + ' ' + "
                                                                  's1.equals(s2));\n'
                                                                  '  }\n'
                                                                  '}'},
                                                  {   'answer': '9 days',
                                                      'explanation': '12 men = 18 women => 1 man = 1.5 women. 8 men + '
                                                                     '16 women = 8(1.5) + 16 = 12 + 16 = 28 women. '
                                                                     'Total women-days = 18 * 14 = 252. Days for 28 '
                                                                     'women = 252 / 28 = 9 days.',
                                                      'options': ['9 days', '10 days', '12 days', '8 days'],
                                                      'question': 'If 12 men or 18 women can reap a field in 14 days, '
                                                                  'in how many days can 8 men and 16 women reap the '
                                                                  'same field?'},
                                                  {   'answer': '25.5',
                                                      'explanation': 'Sum of first N natural numbers = N(N+1)/2. '
                                                                     'Average = (N+1)/2 = 51 / 2 = 25.5.',
                                                      'options': ['25.5', '25.0', '26.0', '50.0'],
                                                      'question': 'What is the average of first 50 natural numbers?'}],
                          'sections': ['Quantitative', 'Logical', 'Verbal', 'Hands-on Coding (1 problem)'],
                          'tips': 'Both MCQs and the coding problem have sectional cutoffs.',
                          'type': 'Aptitude & Coding'},
                      {   'cutoff_percentage': 70,
                          'duration_minutes': 40,
                          'name': 'Technical & Managerial Interview',
                          'questions_count': 3,
                          'round_number': 2,
                          'sample_questions': [   {   'expected': [   'Hash function generates bucket index',
                                                                      'Linked list used for initial collisions',
                                                                      'Converts to Red-Black Tree when bucket exceeds '
                                                                      '8 entries (TREEIFY_THRESHOLD)'],
                                                      'question': 'Explain how HashMap works internally in Java, '
                                                                  'including collision resolution via chaining and '
                                                                  'treeification.'},
                                                  {   'expected': [   'Three pointers (prev, curr, next)',
                                                                      'Iterative pointer reversal in O(N) time and '
                                                                      'O(1) space',
                                                                      'Null termination of former head node'],
                                                      'model_answer': 'Initialize prev = None, curr = head. While curr '
                                                                      'is not None: next_node = curr.next, curr.next = '
                                                                      'prev, prev = curr, curr = next_node. Returns '
                                                                      'prev as the new head in O(N) time and O(1) '
                                                                      'space.',
                                                      'question': 'Given a singly linked list, reverse the nodes of '
                                                                  'the list in-place and return the reversed list.\n'
                                                                  'Input: 1 -> 2 -> 3 -> 4 -> 5\n'
                                                                  'Output: 5 -> 4 -> 3 -> 2 -> 1'},
                                                  {   'expected': [   'Convert first array to set',
                                                                      'Filter elements in second array present in set',
                                                                      'O(N + M) time and O(N) space'],
                                                      'model_answer': 'def intersection(nums1, nums2):\n'
                                                                      '    set1 = set(nums1)\n'
                                                                      '    return list(set1.intersection(nums2))',
                                                      'question': 'Write a function to find the intersection of two '
                                                                  'arrays without duplicates.'}],
                          'sections': ['DSA Problem Solving', 'Cloud & Web Concepts', 'Behavioral'],
                          'tips': 'Focus on data structures and how your academic projects were designed.',
                          'type': 'Technical Interview'},
                      {   'cutoff_percentage': 70,
                          'duration_minutes': 45,
                          'name': 'Technical Architecture & System Design',
                          'questions_count': 3,
                          'round_number': 3,
                          'sample_questions': [   {   'expected': [   'Token Bucket or Leaky Bucket algorithm',
                                                                      'Use of Redis with TTL keys to count requests '
                                                                      'per IP or API key',
                                                                      'Return HTTP 429 Too Many Requests when rate '
                                                                      'limit is exceeded'],
                                                      'model_answer': 'Use Redis with a sliding window or token bucket '
                                                                      'algorithm. For each incoming request, check the '
                                                                      "client's IP or user ID in Redis. Increment the "
                                                                      'counter with an expiry window (e.g. 100 '
                                                                      'requests per 60 seconds). If counter exceeds '
                                                                      '100, immediately return HTTP 429 Too Many '
                                                                      'Requests.',
                                                      'question': 'How would you design a rate limiter to prevent API '
                                                                  'abuse from malicious clients?'},
                                                  {   'expected': [   'Pessimistic locking locks rows on read, '
                                                                      'preventing any concurrent access until commit',
                                                                      'Optimistic locking assumes no conflict and '
                                                                      'checks version number/timestamp on write',
                                                                      'Optimistic is preferred in high-read web apps; '
                                                                      'pessimistic for high-conflict banking '
                                                                      'transactions'],
                                                      'model_answer': 'Pessimistic locking places exclusive locks on '
                                                                      'database records as soon as they are read, '
                                                                      'preventing other transactions from accessing '
                                                                      'them until commit. Optimistic locking does not '
                                                                      'hold database locks; instead, it checks a '
                                                                      "record's version column before updating: if the "
                                                                      'version changed, the transaction rolls back and '
                                                                      'retries.',
                                                      'question': 'Explain the difference between optimistic and '
                                                                  'pessimistic locking in enterprise database '
                                                                  'transactions.'}],
                          'sections': ['Data Structures', 'System Design Basics', 'SQL Window Functions', 'REST APIs'],
                          'tips': 'Focus on database optimization, indexing strategies, and clean code principles.',
                          'type': 'Technical Interview'},
                      {   'cutoff_percentage': 70,
                          'duration_minutes': 30,
                          'name': 'Managerial & Fitment Assessment',
                          'questions_count': 3,
                          'round_number': 4,
                          'sample_questions': [   {   'answer': 'Use the STAR framework: explain the changed '
                                                                'requirements, how you re-evaluated the database and '
                                                                'frontend components, communicated transparently with '
                                                                'team members, and adapted without compromising '
                                                                'project delivery.',
                                                      'question': 'Tell me about a time you worked on a project where '
                                                                  'the requirements changed midway. How did you handle '
                                                                  'it?'}],
                          'sections': ['Teamwork', 'Client Focus', 'Integrity', 'Growth Mindset'],
                          'tips': 'Show enthusiasm for digital transformation and enterprise engineering.',
                          'type': 'HR & Behavioral'}],
        'slug': 'ltimindtree'},
    {   'badge': 'Software Developer / Quality Analyst',
        'description': 'Indian SaaS pioneer. Recruitment is 100% merit-based without resume screening, focusing on '
                       'pointer manipulation, algorithmic logic, and mini-application architecture.',
        'eligibility': 'Open to all degree streams and graduation years. No minimum percentage requirement.',
        'hiring_season': 'Year-Round Off-Campus & On-Campus',
        'id': 'zoho',
        'name': 'Zoho Corporation',
        'package': 'INR 5.6 LPA - INR 8.5 LPA',
        'rounds': [   {   'cutoff_percentage': 70,
                          'duration_minutes': 75,
                          'name': 'General Aptitude & C Output Prediction',
                          'questions_count': 30,
                          'round_number': 1,
                          'sample_questions': [   {   'answer': '10 20',
                                                      'explanation': '*p++ evaluates to *(p++). Post-increment yields '
                                                                     'old pointer address for dereferencing (giving '
                                                                     '10), then advances p to point to 20.',
                                                      'options': ['10 20', '20 20', '10 10', '20 30'],
                                                      'question': 'What is the output of the C code?\n'
                                                                  'int main() {\n'
                                                                  '  int arr[] = {10, 20, 30, 40};\n'
                                                                  '  int *p = arr;\n'
                                                                  "  printf('%d ', *p++);\n"
                                                                  "  printf('%d', *p);\n"
                                                                  '  return 0;\n'
                                                                  '}'},
                                                  {   'answer': '10 30',
                                                      'explanation': '*ptr++ dereferences first (prints 10) then '
                                                                     'increments pointer to 20. Then *++ptr increments '
                                                                     'pointer first (to 30) then dereferences, '
                                                                     'printing 30.',
                                                      'options': ['10 30', '10 20', '20 30', '10 40'],
                                                      'question': 'What is the output of the following C code '
                                                                  'snippet?\n'
                                                                  '#include <stdio.h>\n'
                                                                  'int main() {\n'
                                                                  '  int arr[] = {10, 20, 30, 40, 50};\n'
                                                                  '  int *ptr = arr;\n'
                                                                  "  printf('%d ', *ptr++);\n"
                                                                  "  printf('%d', *++ptr);\n"
                                                                  '  return 0;\n'
                                                                  '}'},
                                                  {   'answer': '5 3 1 1 3 5',
                                                      'explanation': 'Head recursion prints 5, then 3, then 1. As the '
                                                                     'call stack unwinds, tail prints 1, 3, 5.',
                                                      'options': ['5 3 1 1 3 5', '5 3 1', '1 3 5 5 3 1', '5 4 3 2 1'],
                                                      'question': 'What will be printed by this C program?\n'
                                                                  '#include <stdio.h>\n'
                                                                  'void fun(int n) {\n'
                                                                  '  if (n <= 0) return;\n'
                                                                  "  printf('%d ', n);\n"
                                                                  '  fun(n - 2);\n'
                                                                  "  printf('%d ', n);\n"
                                                                  '}\n'
                                                                  'int main() {\n'
                                                                  '  fun(5);\n'
                                                                  '  return 0;\n'
                                                                  '}'},
                                                  {   'answer': '34',
                                                      'explanation': 'Fibonacci-like: each term = sum of previous two. '
                                                                     '13+21 = 34.',
                                                      'options': ['34', '32', '28', '26'],
                                                      'question': 'Find the next term: 2, 3, 5, 8, 13, 21, ?'}],
                          'sections': ['Quantitative Aptitude (15 Qs)', 'C Code Snippet Tracing (15 Qs)'],
                          'tips': 'Be a master of C pointers, recursion call stacks, static variables, and operator '
                                  'precedence.',
                          'type': 'Aptitude & C Tracing'},
                      {   'cutoff_percentage': 60,
                          'duration_minutes': 90,
                          'name': 'Basic Programming Round',
                          'questions_count': 5,
                          'round_number': 2,
                          'sample_questions': [   {   'expected': [   'Two-pointer diagonal index matching i == j and '
                                                                      'i + j == N - 1',
                                                                      'Clean console formatting'],
                                                      'question': 'Given an odd-length string, print an X-pattern '
                                                                  'where diagonals are formed by characters from the '
                                                                  'string.'},
                                                  {   'expected': [   'Nested loops iterating row i and col j',
                                                                      'Print char at j when j == i or j == len - 1 - i',
                                                                      'Print space otherwise',
                                                                      'O(N^2) time and O(1) auxiliary space'],
                                                      'model_answer': 'Let N = len(string). Outer loop i from 0 to '
                                                                      'N-1, inner loop j from 0 to N-1. If j == i: '
                                                                      'print string[i]. Else if j == N - 1 - i: print '
                                                                      'string[N - 1 - i]. Else: print space. Print '
                                                                      'newline at end of inner loop.',
                                                      'question': 'Given an odd-length string, print the string in an '
                                                                  "'X' pattern diagonally from both corners.\n"
                                                                  "Input: 'PROGRAM'\n"
                                                                  'Output:\n'
                                                                  'P     M\n'
                                                                  ' R   A \n'
                                                                  '  O R  \n'
                                                                  '   G   \n'
                                                                  '  O R  \n'
                                                                  ' R   A \n'
                                                                  'P     M'},
                                                  {   'expected': [   'Transpose the matrix (swap rows and columns)',
                                                                      'Reverse each row',
                                                                      'In-place O(1) extra space',
                                                                      'O(N²) time complexity'],
                                                      'model_answer': 'Step 1: Transpose (swap matrix[i][j] with '
                                                                      'matrix[j][i] for i<j). Step 2: Reverse each '
                                                                      'row. Result: 90° clockwise rotation. O(N²) '
                                                                      'time, O(1) space.',
                                                      'question': 'Write a function to rotate a given N×N matrix by 90 '
                                                                  'degrees clockwise in-place.'}],
                          'sections': ['Matrix Manipulation', 'String Parsing without string.h', 'Pattern Generation'],
                          'tips': 'Built-in library functions like reverse(), split(), or sort() are prohibited. '
                                  'Implement from scratch.',
                          'type': 'Hands-on Coding'},
                      {   'cutoff_percentage': 65,
                          'duration_minutes': 150,
                          'name': 'Advanced Programming / Mini-Application Round',
                          'questions_count': 1,
                          'round_number': 3,
                          'sample_questions': [   {   'expected': [   'Passenger and Ticket classes',
                                                                      'Priority queue or state machine for '
                                                                      'cancellations',
                                                                      'Modular separation of booking and reporting '
                                                                      'logic'],
                                                      'question': 'Design a Railway Ticket Reservation System with '
                                                                  'Berth Allocation (LB, MB, UB), RAC, and Waiting '
                                                                  'List management.'},
                                                  {   'expected': [   'Class definitions: Passenger, Ticket, Train, '
                                                                      'ReservationSystem',
                                                                      'Allocation rules: Senior citizens & pregnant '
                                                                      'women get Lower berths',
                                                                      'RAC and WL queues management on cancellation',
                                                                      'Encapsulation, Modular design, and Clean '
                                                                      'separation of concerns'],
                                                      'model_answer': 'Design Passenger with attributes (id, name, '
                                                                      'age, gender, berth_preference). '
                                                                      'ReservationSystem maintains lists for Confirmed '
                                                                      '(63 berths), RAC (18 berths), and Waiting List '
                                                                      '(10). On booking, check preference: if '
                                                                      'senior/female with child, prefer lower. If '
                                                                      'full, allocate RAC; if RAC full, allocate WL. '
                                                                      'On cancellation, promote first RAC to confirmed '
                                                                      'and first WL to RAC.',
                                                      'question': 'Design a Low-Level Object-Oriented Railway Ticket '
                                                                  'Reservation System with Berths (Lower, Middle, '
                                                                  'Upper, RAC, Waiting List) and automatic berth '
                                                                  'allocation based on passenger age and gender '
                                                                  'preferences.'},
                                                  {   'expected': [   'Event class with title, start_time, end_time, '
                                                                      'recurrence',
                                                                      'Calendar class managing list of events',
                                                                      'Conflict detection using interval overlap check',
                                                                      'BST or sorted list for efficient time-range '
                                                                      'queries'],
                                                      'model_answer': 'Event(title, start, end, recurrence_rule). '
                                                                      'Calendar stores events in a balanced BST keyed '
                                                                      'by start_time. addEvent checks for conflicts '
                                                                      'using interval overlap (a.start < b.end and '
                                                                      'b.start < a.end). getEventsInRange uses BST '
                                                                      'range query for O(log N + K) retrieval.',
                                                      'question': 'Design a simple event calendar application. What '
                                                                  'classes and data structures would you use?'}],
                          'sections': ['Object-Oriented Design', 'State Management', 'Console CLI Workflow'],
                          'tips': 'Typical problems include Railway Reservation, Splitwise, Bowling Alley, or Taxi '
                                  'Booking. Write modular code.',
                          'type': 'System Coding'},
                      {   'cutoff_percentage': 75,
                          'duration_minutes': 45,
                          'name': 'Technical & HR Interview',
                          'questions_count': 3,
                          'round_number': 4,
                          'sample_questions': [   {   'expected': [   'Time-space trade-off explanation',
                                                                      'Indexing and pagination strategies',
                                                                      'Decoupling memory state'],
                                                      'question': 'Why did you choose your data structure in the '
                                                                  'reservation round, and how would you optimize '
                                                                  'memory if passenger volume increased 100x?'}],
                          'sections': ['Design Defense', 'Data Structures', 'Zoho Culture Alignment'],
                          'tips': 'Explain your Round 3 code step by step. Zoho values passionate self-taught '
                                  'builders.',
                          'type': 'Face-to-Face Interview'}],
        'slug': 'zoho'},
    {   'badge': 'Software Development Engineer (SDE-1)',
        'description': 'World-leading technology corporation evaluating candidates on algorithmic perfection, scalable '
                       'system architecture, and Growth Mindset.',
        'eligibility': '7.0+ CGPA in B.Tech / M.Tech Computer Science / IT / ECE with zero active backlogs.',
        'hiring_season': 'Microsoft Engage & On-Campus Placement',
        'id': 'microsoft',
        'name': 'Microsoft',
        'package': 'INR 45.0 LPA - INR 52.0 LPA',
        'rounds': [   {   'cutoff_percentage': 85,
                          'duration_minutes': 90,
                          'name': 'Online Assessment (OA)',
                          'questions_count': 3,
                          'round_number': 1,
                          'sample_questions': [   {   'expected': [   'Pre-order traversal with delimiter and null '
                                                                      'marker (e.g. #)',
                                                                      'Queue or recursive reconstruction in O(N) time'],
                                                      'question': 'Given a binary tree, serialize it to a string '
                                                                  'format and deserialize that string back to an '
                                                                  'identical binary tree in O(N) time.'},
                                                  {   'expected': [   "Kadane's Dynamic Programming Algorithm",
                                                                      'current_sum = max(num, current_sum + num)',
                                                                      'max_sum = max(max_sum, current_sum)',
                                                                      'O(N) time and O(1) space'],
                                                      'model_answer': 'Initialize current_sum = 0 and max_sum = '
                                                                      '-infinity. Iterate through each number: '
                                                                      'current_sum = max(num, current_sum + num), '
                                                                      'max_sum = max(max_sum, current_sum). Returns '
                                                                      'max_sum in a single pass of O(N) time and O(1) '
                                                                      'auxiliary space.',
                                                      'question': 'Given an integer array nums, find the contiguous '
                                                                  'subarray (containing at least one number) which has '
                                                                  "the largest sum and return its sum (Kadane's "
                                                                  'Algorithm).\n'
                                                                  'Input: nums = [-2,1,-3,4,-1,2,1,-5,4]\n'
                                                                  'Output: 6 (Subarray [4,-1,2,1])'},
                                                  {   'expected': [   'Two-pointer technique',
                                                                      'Slow pointer tracks position of unique elements',
                                                                      'Fast pointer scans through array',
                                                                      'O(N) time, O(1) space'],
                                                      'model_answer': 'i = 0 (slow pointer). For j = 1 to n-1 (fast '
                                                                      'pointer): if nums[j] != nums[i], increment i '
                                                                      'and set nums[i] = nums[j]. Return i+1. O(N) '
                                                                      'time, O(1) space.',
                                                      'question': 'Given a sorted array, remove the duplicates '
                                                                  'in-place such that each element appears only once. '
                                                                  'Return the new length.'}],
                          'sections': ['Dynamic Programming', 'Trees & Graphs', 'String Parsing'],
                          'tips': 'All test cases including extreme edge cases (overflow, null inputs, massive arrays) '
                                  'must pass.',
                          'type': 'Algorithmic Coding'},
                      {   'cutoff_percentage': 85,
                          'duration_minutes': 60,
                          'name': 'Technical Interview 1 (DSA & Code Hygiene)',
                          'questions_count': 2,
                          'round_number': 2,
                          'sample_questions': [   {   'expected': [   'Two-heap approach: Max-Heap for lower half, '
                                                                      'Min-Heap for upper half',
                                                                      'Heap balancing invariant maintenance'],
                                                      'question': 'Find the median from a continuous stream of '
                                                                  'integers in O(1) retrieval time and O(log N) '
                                                                  'insertion time.'},
                                                  {   'expected': [   'Pre-order traversal with delimiter (comma) and '
                                                                      "null markers ('#')",
                                                                      'Queue-based iterative deserialization',
                                                                      'O(N) time and O(N) space'],
                                                      'model_answer': 'Serialization: Pre-order DFS traversal. If node '
                                                                      "is None, append '#'. Else append str(val) and "
                                                                      'recurse left and right. Deserialization: Split '
                                                                      'string by comma into a queue. Read next token: '
                                                                      "if '#', return None. Else create "
                                                                      'TreeNode(int(val)), node.left = deserialize(), '
                                                                      'node.right = deserialize(). Returns root in '
                                                                      'O(N).',
                                                      'question': 'Design an algorithm to serialize and deserialize a '
                                                                  'binary tree into and from a string format.'},
                                                  {   'expected': [   'Mutex lock for mutual exclusion',
                                                                      'Two condition variables: not_full and not_empty',
                                                                      'Producer waits on not_full when queue is full',
                                                                      'Consumer waits on not_empty when queue is empty',
                                                                      'Signal after enqueue/dequeue'],
                                                      'model_answer': 'Use a circular buffer with mutex + 2 condition '
                                                                      'variables. enqueue: lock → while full, '
                                                                      'wait(not_full) → insert → signal(not_empty) → '
                                                                      'unlock. dequeue: lock → while empty, '
                                                                      'wait(not_empty) → remove → signal(not_full) → '
                                                                      'unlock.',
                                                      'question': 'Design a thread-safe bounded blocking queue. What '
                                                                  'synchronization primitives would you use?'}],
                          'sections': ['Binary Trees', 'Heaps', 'Formal Complexity Proofs'],
                          'tips': 'Always talk out loud while coding. State time and space complexity before writing a '
                                  'single line.',
                          'type': 'Live Coding & Algorithms'},
                      {   'cutoff_percentage': 80,
                          'duration_minutes': 60,
                          'name': 'Technical Interview 2 (System & Low-Level Design)',
                          'questions_count': 2,
                          'round_number': 3,
                          'sample_questions': [   {   'expected': [   'ConcurrentHashMap or mutex locking',
                                                                      'Min-Heap or Doubly-Linked List for TTL ordering',
                                                                      'Background cleanup thread or lazy eviction on '
                                                                      'access'],
                                                      'question': 'Design a thread-safe in-memory key-value cache with '
                                                                  'TTL (Time to Live) expiration and eviction policy.'},
                                                  {   'expected': [   'Operational Transformation (OT) or CRDTs for '
                                                                      'conflict resolution',
                                                                      'WebSocket connections for real-time sync',
                                                                      'Server as central authority for OT',
                                                                      'Cursor position tracking per user',
                                                                      'Undo/redo stack per session'],
                                                      'model_answer': 'Use Operational Transformation: each edit '
                                                                      'operation (insert/delete at position) is '
                                                                      'transformed against concurrent operations to '
                                                                      'maintain consistency. WebSocket channels push '
                                                                      'operations to all connected clients. Server '
                                                                      'applies canonical ordering. CRDTs (like Yjs) '
                                                                      'offer eventual consistency without central '
                                                                      'coordination.',
                                                      'question': 'Design a real-time collaborative document editor '
                                                                  '(like Google Docs). How do you handle concurrent '
                                                                  'edits?'}],
                          'sections': ['Object-Oriented Design', 'Design Patterns', 'Concurrency & Thread Safety'],
                          'tips': 'Apply SOLID principles. Be ready to explain Factory, Strategy, and Observer design '
                                  'patterns.',
                          'type': 'Architecture & LLD'},
                      {   'cutoff_percentage': 85,
                          'duration_minutes': 45,
                          'name': 'As Appropriate / Bar Raiser & Behavioral',
                          'questions_count': 3,
                          'round_number': 4,
                          'sample_questions': [   {   'expected': [   'Systematic logging / telemetry',
                                                                      'Binary search through codebase history',
                                                                      'Documenting solution for team'],
                                                      'question': 'Tell me about a time you worked on a complex bug '
                                                                  'where you lacked documentation. How did you '
                                                                  'diagnose and solve it?'}],
                          'sections': ['Growth Mindset', 'Customer Empathy', 'Handling Project Ambiguity'],
                          'tips': 'Demonstrate curiosity and resilience. Structure answers using the STAR method.',
                          'type': 'Behavioral & Engineering Leadership'}],
        'slug': 'microsoft'},
    {   'badge': 'Software Engineer (SWE / L3)',
        'description': 'Google sets the industry benchmark for computer science rigor, evaluating graph algorithms, '
                       'dynamic programming, mathematical invariants, and Googleyness.',
        'eligibility': 'B.Tech / M.Tech / PhD in CS or related fields. Unmatched algorithmic problem solving required.',
        'hiring_season': 'Google On-Campus & Early Career',
        'id': 'google',
        'name': 'Google',
        'package': 'INR 55.0 LPA - INR 65.0 LPA',
        'rounds': [   {   'cutoff_percentage': 90,
                          'duration_minutes': 90,
                          'name': 'Online Assessment (OA)',
                          'questions_count': 2,
                          'round_number': 1,
                          'sample_questions': [   {   'expected': [   'Dynamic programming state dp[k][node] or matrix '
                                                                      'exponentiation on adjacency matrix',
                                                                      'O(K * (V + E)) complexity analysis'],
                                                      'question': 'Given an undirected weighted graph, find the '
                                                                  'shortest path from node A to node B that traverses '
                                                                  'an exact number of K edges.'},
                                                  {   'expected': [   'Two Pointers approach from left and right',
                                                                      'Maintain left_max and right_max',
                                                                      'Water trapped at pointer is max - height',
                                                                      'O(N) time and O(1) auxiliary space'],
                                                      'model_answer': 'Use two pointers left = 0, right = n - 1 with '
                                                                      'left_max = 0, right_max = 0. While left < '
                                                                      'right: if height[left] < height[right]: if '
                                                                      'height[left] >= left_max, update left_max; else '
                                                                      'water += left_max - height[left]; left++. Else: '
                                                                      'if height[right] >= right_max, update '
                                                                      'right_max; else water += right_max - '
                                                                      'height[right]; right--. Returns total water in '
                                                                      'O(N) time and O(1) space.',
                                                      'question': 'Given n non-negative integers representing an '
                                                                  'elevation map where the width of each bar is 1, '
                                                                  'compute how much water it can trap after raining.\n'
                                                                  'Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]\n'
                                                                  'Output: 6'},
                                                  {   'expected': [   'Hash map approach',
                                                                      'Store complement = target - nums[i]',
                                                                      'Check if complement exists in map',
                                                                      'O(N) time, O(N) space'],
                                                      'model_answer': 'seen = {}\n'
                                                                      'for i, num in enumerate(nums):\n'
                                                                      '    complement = target - num\n'
                                                                      '    if complement in seen: return '
                                                                      '[seen[complement], i]\n'
                                                                      '    seen[num] = i',
                                                      'question': 'Given an array of integers nums and an integer '
                                                                  'target, return indices of the two numbers such that '
                                                                  'they add up to target. Assume exactly one solution '
                                                                  'exists.'}],
                          'sections': ['Advanced Dynamic Programming', 'Disjoint Set Union / Graph Theory'],
                          'tips': 'Optimal time and space bounds are strictly checked against hidden test suites.',
                          'type': 'Advanced Coding'},
                      {   'cutoff_percentage': 85,
                          'duration_minutes': 45,
                          'name': 'Technical Interview 1 (Algorithms & Data Structures)',
                          'questions_count': 1,
                          'round_number': 2,
                          'sample_questions': [   {   'expected': [   'Pairwise word prefix comparison to build '
                                                                      'directed DAG',
                                                                      "Kahn's algorithm (Topological sort)",
                                                                      'Cycle detection for invalid dictionaries'],
                                                      'question': 'Given a set of alien language dictionary words '
                                                                  'sorted lexicographically, deduce the unique '
                                                                  'character ordering of the alien alphabet.'},
                                                  {   'expected': [   'Directed Graph construction comparing adjacent '
                                                                      'words',
                                                                      "Topological Sort using Kahn's Algorithm (BFS) "
                                                                      'or DFS cycle detection',
                                                                      'O(V + E) time where V is unique characters'],
                                                      'model_answer': 'Build a directed graph where an edge u -> v '
                                                                      'means character u precedes v. Compare adjacent '
                                                                      'words: find the first differing character and '
                                                                      'add directed edge. Count in-degrees. Apply '
                                                                      "Kahn's BFS algorithm using a queue of nodes "
                                                                      'with in-degree 0. If result length == number of '
                                                                      'unique characters, return topological string; '
                                                                      'else cycle exists (invalid).',
                                                      'question': 'There is a new alien language that uses the English '
                                                                  'alphabet. Given a list of words from the alien '
                                                                  'language dictionary sorted lexicographically, '
                                                                  'derive the order of letters in this language.\n'
                                                                  "Input: words = ['wrt','wrf','er','ett','rftt']\n"
                                                                  "Output: 'wertf'"},
                                                  {   'expected': [   'Classic egg drop problem',
                                                                      'Dynamic programming approach',
                                                                      'dp[n][k] = 1 + min over x of max(dp[n-1][x-1], '
                                                                      'dp[n][k-x])',
                                                                      'Binary search optimization for O(N*K*logK)'],
                                                      'model_answer': 'Use DP: dp[eggs][floors] = minimum worst-case '
                                                                      'trials. For each floor x from 1 to k: if egg '
                                                                      'breaks, check dp[eggs-1][x-1] floors below; if '
                                                                      'survives, check dp[eggs][k-x] floors above. '
                                                                      'dp[n][k] = 1 + min over x of max(dp[n-1][x-1], '
                                                                      'dp[n][k-x]). Optimize with binary search.',
                                                      'question': 'You have N eggs and a building with K floors. Find '
                                                                  'the minimum number of trials needed to find the '
                                                                  'critical floor in the worst case.'}],
                          'sections': ['Graph Traversal', 'Topological Sort', 'Cycle Detection'],
                          'tips': 'Write modular, bug-free code on a plain text editor without IDE autocompletion or '
                                  'syntax highlighting.',
                          'type': 'Google Docs Live Coding'},
                      {   'cutoff_percentage': 85,
                          'duration_minutes': 45,
                          'name': 'Technical Interview 2 (Optimization & Invariants)',
                          'questions_count': 1,
                          'round_number': 3,
                          'sample_questions': [   {   'expected': [   'Two DP arrays: max_ending_here[i] and '
                                                                      'max_starting_here[i]',
                                                                      'O(N) time and O(N) or O(1) space optimization'],
                                                      'question': 'Given an integer array, find the maximum sum of a '
                                                                  'non-empty subarray where you can delete at most one '
                                                                  'element.'},
                                                  {   'expected': [   'Two-stage: candidate generation + ranking',
                                                                      'Collaborative filtering for candidates',
                                                                      'Deep neural network ranker with features: watch '
                                                                      'time, CTR, user history',
                                                                      'Diversity injection to avoid filter bubbles',
                                                                      'Freshness boost for new content'],
                                                      'model_answer': 'Candidate generation: retrieve 1000 candidates '
                                                                      'using collaborative filtering and content-based '
                                                                      'embeddings. Ranking: deep neural network scores '
                                                                      'each candidate on predicted watch time, click '
                                                                      'probability, and user engagement signals. '
                                                                      'Diversity: re-rank to ensure category '
                                                                      'diversity. Freshness: time-decay boosting for '
                                                                      'recent uploads.',
                                                      'question': "Design YouTube's video recommendation system. How "
                                                                  'would you balance relevance, diversity, and '
                                                                  'freshness?'}],
                          'sections': ['Segment Trees', 'Sliding Window', 'Binary Search on Answer'],
                          'tips': 'Clarify edge cases before writing code. Check for integer overflow and empty '
                                  'inputs.',
                          'type': 'Live Coding'},
                      {   'cutoff_percentage': 80,
                          'duration_minutes': 45,
                          'name': 'Googleyness & Leadership Interview',
                          'questions_count': 4,
                          'round_number': 4,
                          'sample_questions': [   {   'expected': [   'Objective data-driven benchmarking',
                                                                      'Active listening and consensus building',
                                                                      'Commitment to the final team choice'],
                                                      'question': 'Tell me about a time you strongly disagreed with a '
                                                                  "teammate's architectural decision. How did you "
                                                                  'resolve the conflict constructively?'},
                                                  {   'answer': 'Describe the disagreement professionally (e.g., '
                                                                'architecture choice), how you presented data-driven '
                                                                "arguments, respected the team's decision when "
                                                                'consensus formed, and fully committed to making the '
                                                                'chosen approach successful.',
                                                      'question': 'Tell me about a time when you disagreed with a team '
                                                                  'decision but ultimately committed to it. '
                                                                  '(Googleyness)'}],
                          'sections': [   'Intellectual Humility',
                                          'Navigating Ambiguity',
                                          'Collaborative Problem Solving'],
                          'tips': 'Be authentic, acknowledge mistakes openly, and explain how you prioritize user '
                                  'interests above all else.',
                          'type': 'Behavioral'}],
        'slug': 'google'},
    {   'badge': 'Server Technology / Applications Developer',
        'description': 'Database and cloud infrastructure powerhouse. Rigorously tests database internals, '
                       'concurrency, operating systems, and DSA.',
        'eligibility': '7.0+ CGPA in B.Tech CS / IT with no active backlogs.',
        'hiring_season': 'On-Campus Placement Drives',
        'id': 'oracle',
        'name': 'Oracle',
        'package': 'INR 16.0 LPA - INR 22.0 LPA',
        'rounds': [   {   'cutoff_percentage': 70,
                          'duration_minutes': 105,
                          'name': 'Online Assessment (Cognitive & Technical)',
                          'questions_count': 45,
                          'round_number': 1,
                          'sample_questions': [   {   'answer': 'Exclusively at the leaf nodes',
                                                      'explanation': 'In B+ Trees, internal nodes only store key '
                                                                     'search guides; all actual record pointers reside '
                                                                     'in leaf nodes, linked for range queries.',
                                                      'options': [   'Exclusively at the leaf nodes',
                                                                     'At both internal and leaf nodes',
                                                                     'Only at the root node',
                                                                     'In a separate hash table'],
                                                      'question': 'In a B+ Tree of order M, where are actual data '
                                                                  'records or row pointers stored?'},
                                                  {   'answer': 'B+ Trees store all actual records in leaf nodes '
                                                                'connected as a doubly linked list, optimizing range '
                                                                'scans and maximizing disk block fan-out',
                                                      'explanation': 'B+ Tree nodes have high fan-out (hundreds of '
                                                                     'keys per disk page), minimizing disk I/O depth '
                                                                     '(height <= 3-4 for millions of rows). Linked '
                                                                     'leaf nodes enable fast O(1) sequential range '
                                                                     'scans.',
                                                      'options': [   'B+ Trees store all actual records in leaf nodes '
                                                                     'connected as a doubly linked list, optimizing '
                                                                     'range scans and maximizing disk block fan-out',
                                                                     'B+ Trees consume 0 bytes of RAM',
                                                                     'Binary Search Trees are mathematically '
                                                                     'un-indexable',
                                                                     'B+ Trees are only compatible with Oracle Linux'],
                                                      'question': 'Why do relational database engines (like Oracle and '
                                                                  'MySQL InnoDB) use B+ Trees rather than standard '
                                                                  'Binary Search Trees (BST) or B-Trees for disk '
                                                                  'storage indexing?'},
                                                  {   'answer': '100 and 70',
                                                      'explanation': '`COUNT(*)` counts all rows including NULLs '
                                                                     '(100). `COUNT(column_name)` ignores NULL values '
                                                                     'and counts only non-null occurrences (100 - 30 = '
                                                                     '70).',
                                                      'options': [   '100 and 70',
                                                                     '100 and 100',
                                                                     '70 and 70',
                                                                     '100 and 30'],
                                                      'question': 'What will be the output of executing the following '
                                                                  'SQL query?\n'
                                                                  'SELECT COUNT(*), COUNT(commission_pct) FROM '
                                                                  'employees;\n'
                                                                  '(Assume employees has 100 rows and 30 employees '
                                                                  'have commission_pct as NULL)'},
                                                  {   'answer': 'TRUNCATE is DDL and cannot be rolled back, while '
                                                                'DELETE is DML and can be rolled back',
                                                      'explanation': 'TRUNCATE is a DDL operation that deallocates '
                                                                     'extents, resets high water mark, does not fire '
                                                                     'triggers, and cannot be rolled back. DELETE is a '
                                                                     'DML operation that logs undo/redo for every '
                                                                     'deleted row and can be rolled back.',
                                                      'options': [   'TRUNCATE is DDL and cannot be rolled back, while '
                                                                     'DELETE is DML and can be rolled back',
                                                                     'DELETE removes all rows faster than TRUNCATE',
                                                                     'TRUNCATE requires a WHERE clause',
                                                                     'There is no difference in Oracle'],
                                                      'question': 'What is the difference between TRUNCATE and DELETE '
                                                                  'in Oracle Database?'}],
                          'sections': [   'Computer Science Fundamentals',
                                          'SQL & Database Internals',
                                          'Coding (2 Problems)'],
                          'tips': 'Be strong in B+ Tree indexing, ACID transactions, and standard library data '
                                  'structures.',
                          'type': 'MCQ & Coding'},
                      {   'cutoff_percentage': 75,
                          'duration_minutes': 50,
                          'name': 'Technical Interview 1 (Database & OS Internals)',
                          'questions_count': 3,
                          'round_number': 2,
                          'sample_questions': [   {   'expected': [   'Growing phase acquires locks, shrinking phase '
                                                                      'releases locks',
                                                                      'Strict 2PL holds exclusive locks until '
                                                                      'commit/abort, guaranteeing serializability and '
                                                                      'no cascading aborts'],
                                                      'question': 'Explain Two-Phase Locking (2PL) protocol. How does '
                                                                  'Strict 2PL prevent cascading aborts?'},
                                                  {   'expected': [   'TrieNode class with children dict and '
                                                                      'is_end_of_word boolean',
                                                                      'insert: traverse/create nodes for each char, '
                                                                      'mark end',
                                                                      'search: verify full word and is_end_of_word == '
                                                                      'True',
                                                                      'startsWith: verify prefix traversal completes',
                                                                      'All operations run in O(L) time where L is word '
                                                                      'length'],
                                                      'model_answer': 'Define TrieNode with children = {} and is_end = '
                                                                      'False. insert(word): node = root; for c in '
                                                                      'word: node = node.children.setdefault(c, '
                                                                      'TrieNode()); node.is_end = True. search(word): '
                                                                      'traverse; return node is not None and '
                                                                      'node.is_end. startsWith(prefix): traverse; '
                                                                      'return node is not None. Time complexity is '
                                                                      'O(L) per operation.',
                                                      'question': 'Implement a Trie (Prefix Tree) with insert(word), '
                                                                  'search(word), and startsWith(prefix) operations.'},
                                                  {   'expected': [   'Utilize BST ordering property',
                                                                      'If both nodes < current, traverse left',
                                                                      'If both nodes > current, traverse right',
                                                                      'Otherwise, current is LCA',
                                                                      'O(H) time complexity where H is tree height'],
                                                      'model_answer': 'def lowest_common_ancestor(root, p, q):\n'
                                                                      '    curr = root\n'
                                                                      '    while curr:\n'
                                                                      '        if p.val < curr.val and q.val < '
                                                                      'curr.val:\n'
                                                                      '            curr = curr.left\n'
                                                                      '        elif p.val > curr.val and q.val > '
                                                                      'curr.val:\n'
                                                                      '            curr = curr.right\n'
                                                                      '        else:\n'
                                                                      '            return curr',
                                                      'question': 'Write an efficient function to find the Lowest '
                                                                  'Common Ancestor (LCA) of two nodes in a Binary '
                                                                  'Search Tree (BST).'}],
                          'sections': [   'Deadlocks & Two-Phase Locking',
                                          'Virtual Memory & Paging',
                                          'Complex SQL Queries'],
                          'tips': 'Expect questions on how the Oracle Database engine manages rollback segments and '
                                  'redo logs.',
                          'type': 'Technical Interview'},
                      {   'cutoff_percentage': 75,
                          'duration_minutes': 50,
                          'name': 'Database Internals & System Design',
                          'questions_count': 4,
                          'round_number': 3,
                          'sample_questions': [   {   'expected': [   'B+ Trees have high fanout, minimizing disk I/O '
                                                                      'seeks',
                                                                      'All records stored in leaf nodes linked '
                                                                      'sequentially, making range queries fast',
                                                                      'Hash tables cannot do range queries efficiently '
                                                                      '(O(N) vs O(log N + K))',
                                                                      'BSTs have high tree height causing excessive '
                                                                      'random disk block reads'],
                                                      'model_answer': 'B+ Trees have high branching factor (fanout of '
                                                                      'hundreds), allowing millions of records to be '
                                                                      'indexed with only 3-4 tree levels, drastically '
                                                                      'cutting disk I/O. Furthermore, leaf nodes are '
                                                                      'linked sequentially as a doubly linked list, '
                                                                      'enabling O(log N) point lookups and linear '
                                                                      'disk-block sequential scans for range queries.',
                                                      'question': 'Why do relational databases use B+ Trees rather '
                                                                  'than Binary Search Trees (BST) or Hash Tables for '
                                                                  'disk-based indexing?'},
                                                  {   'expected': [   'Writers do not block readers; readers do not '
                                                                      'block writers',
                                                                      'Transactions read a snapshot of data as of '
                                                                      'transaction start',
                                                                      'Undo logs / row versions store historical '
                                                                      'states',
                                                                      'Eliminates phantom and dirty reads safely'],
                                                      'model_answer': 'MVCC creates historical versions of rows '
                                                                      'instead of locking them in-place during '
                                                                      'updates. When a transaction reads data, it '
                                                                      'reads the consistent snapshot that existed at '
                                                                      'its transaction start timestamp using undo '
                                                                      'tablespace / row versions. Thus, reading '
                                                                      'transactions never block writers, and writing '
                                                                      'transactions never block readers.',
                                                      'question': 'How does Multiversion Concurrency Control (MVCC) '
                                                                  'eliminate read-write lock contention in Oracle and '
                                                                  'PostgreSQL?'}],
                          'sections': [   'B-Trees & Indexing',
                                          'Concurrency Control',
                                          'Distributed Storage',
                                          'Memory Management'],
                          'tips': 'Oracle engineers expect deep understanding of B-Tree indexing, execution plans, and '
                                  'memory allocation.',
                          'type': 'Technical Interview'},
                      {   'cutoff_percentage': 70,
                          'duration_minutes': 40,
                          'name': 'Hiring Manager & Leadership Round',
                          'questions_count': 3,
                          'round_number': 4,
                          'sample_questions': [   {   'answer': "Emphasize Oracle's legacy of data excellence and its "
                                                                'modern gen-2 cloud architecture built for enterprise '
                                                                'mission-critical workloads. Discuss your fascination '
                                                                'with high-throughput database engines and autonomous '
                                                                'technologies.',
                                                      'question': 'Why Oracle Cloud Infrastructure (OCI) over other '
                                                                  'cloud providers, and what excites you about '
                                                                  'distributed database engineering?'}],
                          'sections': ['Ownership', 'Technical Passion', 'Collaboration', 'Career Alignment'],
                          'tips': 'Show passion for foundational enterprise cloud infrastructure and database '
                                  'reliability.',
                          'type': 'HR & Behavioral'}],
        'slug': 'oracle'},
    {   'badge': 'Associate System Engineer / CodeKnack',
        'description': 'Global hybrid cloud and AI pioneer. IBM screens candidates through Cognitive Games, English '
                       'Language Assessment, and CodeKnack coding challenges.',
        'eligibility': '60% or 6.0 CGPA throughout 10th, 12th, and UG.',
        'hiring_season': 'National Qualifier Drives',
        'id': 'ibm',
        'name': 'IBM',
        'package': 'INR 4.5 LPA - INR 11.0 LPA',
        'rounds': [   {   'cutoff_percentage': 65,
                          'duration_minutes': 60,
                          'name': 'Cognitive Ability & English Assessment',
                          'questions_count': 40,
                          'round_number': 1,
                          'sample_questions': [   {   'answer': 'Neither the engineer nor the managers were aware of '
                                                                'the server outage.',
                                                      'explanation': 'When compound subjects are connected by '
                                                                     'neither...nor, the verb agrees in number with '
                                                                     "the closer subject ('managers' is plural, so "
                                                                     "'were').",
                                                      'options': [   'Neither the engineer nor the managers were aware '
                                                                     'of the server outage.',
                                                                     'Neither the engineer nor the managers was aware '
                                                                     'of the server outage.',
                                                                     'Neither the engineer nor the managers has aware '
                                                                     'of the server outage.',
                                                                     'Neither the engineer or the managers was aware '
                                                                     'of the server outage.'],
                                                      'question': 'Identify the grammatically correct sentence:'},
                                                  {   'answer': 'An Inode stores file metadata (size, permissions, '
                                                                'owner, timestamps, and data block pointers) but not '
                                                                'file content or filename',
                                                      'explanation': 'Inodes store all filesystem metadata and disk '
                                                                     'block pointers for a file. Directory entries map '
                                                                     'filenames to their corresponding inode numbers.',
                                                      'options': [   'An Inode stores file metadata (size, '
                                                                     'permissions, owner, timestamps, and data block '
                                                                     'pointers) but not file content or filename',
                                                                     "An Inode stores the file's name and user "
                                                                     'password',
                                                                     'An Inode is an encrypted zip compression '
                                                                     'algorithm',
                                                                     'An Inode runs the Linux bootloader'],
                                                      'question': 'In Linux systems engineering, what is the role of '
                                                                  'an Inode in the Ext4 filesystem?'},
                                                  {   'answer': '720 tasks',
                                                      'explanation': 'New task rate = 600 * 1.25 = 750 tasks/hr. '
                                                                     'Success rate = 100% - 4% = 96%. Successful tasks '
                                                                     '= 750 * 0.96 = 720 tasks.',
                                                      'options': ['720 tasks', '690 tasks', '750 tasks', '710 tasks'],
                                                      'question': 'A software pipeline processes 600 tasks per hour. '
                                                                  'If throughput is increased by 25% and task failure '
                                                                  'rate drops from 8% to 4%, how many successful tasks '
                                                                  'are completed in an hour?'}],
                          'sections': ['Cognitive Mini-Games', 'English Grammar & Comprehension'],
                          'tips': 'Quick pattern matching and clear business English comprehension are tested.',
                          'type': 'Gamified & Verbal'},
                      {   'cutoff_percentage': 70,
                          'duration_minutes': 60,
                          'name': 'CodeKnack Hands-on Coding',
                          'questions_count': 2,
                          'round_number': 2,
                          'sample_questions': [   {   'expected': [   'Stack push on opening brackets',
                                                                      'Stack pop and match verification on closing '
                                                                      'brackets',
                                                                      'Empty stack check at completion'],
                                                      'question': "Given a string of brackets '()[]{}', write a "
                                                                  'function to determine if the input string is valid '
                                                                  'using a stack.'},
                                                  {   'expected': [   'Post-order DFS traversal',
                                                                      'Calculate max_depth of left and right subtrees',
                                                                      'Diameter at node = left_depth + right_depth',
                                                                      'Update global max diameter in O(N) time'],
                                                      'model_answer': 'Maintain a global variable max_diameter = 0. '
                                                                      'Helper function depth(node): if node is None '
                                                                      'return 0. Recursively calculate L = '
                                                                      'depth(node.left), R = depth(node.right). '
                                                                      'max_diameter = max(max_diameter, L + R). Return '
                                                                      'max(L, R) + 1. Returns max_diameter in O(N) '
                                                                      'time.',
                                                      'question': 'Design an algorithm to find the diameter of a '
                                                                  'Binary Tree (the longest path between any two nodes '
                                                                  'in a tree, which may or may not pass through the '
                                                                  'root).'},
                                                  {   'expected': [   'Color states: WHITE (unvisited), GRAY '
                                                                      '(currently in recursion stack), BLACK (visited '
                                                                      'and all descendants processed)',
                                                                      'Cycle detected if a GRAY neighbor is '
                                                                      'encountered (back-edge)',
                                                                      'O(V + E) time, O(V) space'],
                                                      'model_answer': 'def has_cycle(num_nodes, adj_list):\n'
                                                                      '    WHITE, GRAY, BLACK = 0, 1, 2\n'
                                                                      '    color = [WHITE] * num_nodes\n'
                                                                      '    def dfs(u):\n'
                                                                      '        color[u] = GRAY\n'
                                                                      '        for v in adj_list[u]:\n'
                                                                      '            if color[v] == GRAY: return True\n'
                                                                      '            if color[v] == WHITE and dfs(v): '
                                                                      'return True\n'
                                                                      '        color[u] = BLACK\n'
                                                                      '        return False\n'
                                                                      '    return any(color[i] == WHITE and dfs(i) for '
                                                                      'i in range(num_nodes))',
                                                      'question': 'Implement an algorithm to detect a cycle in a '
                                                                  'directed graph using Depth-First Search (DFS) and '
                                                                  'three-color marking.'}],
                          'sections': ['Data Structures', 'String Processing', 'Algorithms'],
                          'tips': 'Coding is hosted on HackerRank. Optimize for time complexity to pass hidden test '
                                  'cases.',
                          'type': 'Coding Assessment'},
                      {   'cutoff_percentage': 70,
                          'duration_minutes': 45,
                          'name': 'Cloud, AI & Architecture',
                          'questions_count': 3,
                          'round_number': 3,
                          'sample_questions': [   {   'expected': [   'VMs virtualize hardware and include a full '
                                                                      'Guest OS',
                                                                      'Containers virtualize the OS kernel and share '
                                                                      'the host kernel',
                                                                      'Containers are lightweight, start in '
                                                                      'milliseconds, and consume less memory'],
                                                      'model_answer': 'A VM runs a full guest operating system on top '
                                                                      'of a hypervisor, consuming gigabytes of storage '
                                                                      'and taking minutes to boot. A Docker container '
                                                                      'packages code and dependencies while sharing '
                                                                      'the host OS kernel, making it lightweight '
                                                                      '(megabytes), instantaneous to start, and '
                                                                      'portable across cloud environments.',
                                                      'question': 'What is the difference between a virtual machine '
                                                                  '(VM) and a Docker container?'},
                                                  {   'expected': [   'Kafka: distributed append-only commit log, high '
                                                                      'throughput, event replayable, partition-based '
                                                                      'pub/sub',
                                                                      'RabbitMQ: traditional smart broker message '
                                                                      'queue, AMQP protocol, fine-grained routing, '
                                                                      'messages deleted after ack',
                                                                      'Kafka for big data stream ingestion and '
                                                                      'analytics; RabbitMQ for transactional job task '
                                                                      'dispatch'],
                                                      'model_answer': 'RabbitMQ is a message broker that routes '
                                                                      'messages to queues and deletes them once '
                                                                      'acknowledged by consumers (great for complex '
                                                                      'routing, job queues, low latency). Apache Kafka '
                                                                      'is a distributed, append-only commit log that '
                                                                      'persists streams of events on disk with '
                                                                      'partition-based parallel consumption and '
                                                                      'message replayability (ideal for event-sourcing '
                                                                      'and high-throughput analytics).',
                                                      'question': 'What is the difference between Apache Kafka and '
                                                                  'RabbitMQ when building enterprise event-driven '
                                                                  'architectures?'}],
                          'sections': ['Cloud Architecture', 'Docker & Kubernetes', 'CAP Theorem', 'Microservices'],
                          'tips': 'Familiarize yourself with enterprise hybrid cloud and containerization concepts.',
                          'type': 'Technical Interview'},
                      {   'cutoff_percentage': 70,
                          'duration_minutes': 30,
                          'name': 'HR & Cultural Values',
                          'questions_count': 3,
                          'round_number': 4,
                          'sample_questions': [   {   'answer': 'Discuss an idea or automation script you wrote that '
                                                                'solved a real inconvenience for your peers or college '
                                                                'department, emphasizing tangible impact and '
                                                                'usefulness rather than novelty alone.',
                                                      'question': "Give an example of how you demonstrated 'Innovation "
                                                                  "that Matters' during your academic coursework or "
                                                                  'projects.'}],
                          'sections': [   'Dedication to Client Success',
                                          'Innovation that Matters',
                                          'Trust & Responsibility'],
                          'tips': "Align responses with IBM's 3 core values.",
                          'type': 'HR & Behavioral'}],
        'slug': 'ibm'},
    {   'badge': 'USI Analyst / Technical Consultant',
        'description': 'Leading global consulting and advisory firm hiring for technical consulting, cloud '
                       'engineering, and enterprise analytics.',
        'eligibility': '60% or 6.0 CGPA in 10th, 12th, and B.Tech without active backlogs.',
        'hiring_season': 'On-Campus Placement Drives',
        'id': 'deloitte',
        'name': 'Deloitte',
        'package': 'INR 4.5 LPA - INR 7.6 LPA',
        'rounds': [   {   'cutoff_percentage': 65,
                          'duration_minutes': 75,
                          'name': 'Online Aptitude & Technical Assessment',
                          'questions_count': 50,
                          'round_number': 1,
                          'sample_questions': [   {   'answer': '15 years',
                                                      'explanation': 'If amount becomes 2^1 in 5 years, it will become '
                                                                     '8 = 2^3 times in 3 * 5 = 15 years.',
                                                      'options': ['15 years', '20 years', '25 years', '10 years'],
                                                      'question': 'A sum of money doubles itself at compound interest '
                                                                  'in 5 years. In how many years will it become 8 '
                                                                  'times of itself at the same rate?'},
                                                  {   'answer': 'Symmetric uses a single shared secret key for both '
                                                                'encryption and decryption; Asymmetric uses a '
                                                                'public-private key pair',
                                                      'explanation': 'AES symmetric encryption is fast and encrypts '
                                                                     'bulk data. Asymmetric RSA/ECC uses public key '
                                                                     'for encryption and private key for decryption, '
                                                                     'solving secure key exchange.',
                                                      'options': [   'Symmetric uses a single shared secret key for '
                                                                     'both encryption and decryption; Asymmetric uses '
                                                                     'a public-private key pair',
                                                                     'Symmetric encryption only works on numbers; '
                                                                     'Asymmetric only on text',
                                                                     'Asymmetric encryption runs 1000x faster than '
                                                                     'Symmetric',
                                                                     'Symmetric encryption does not require keys'],
                                                      'question': 'What is the fundamental difference between '
                                                                  'Symmetric Encryption (e.g. AES) and Asymmetric '
                                                                  'Encryption (e.g. RSA) in enterprise security '
                                                                  'architectures?'},
                                                  {   'answer': '6,600 hours',
                                                      'explanation': 'Ratio units: Q4 - Q2 = 7 - 5 = 2 units. 2 units '
                                                                     '= 600 hours => 1 unit = 300 hours. Total ratio '
                                                                     'sum = 4 + 5 + 6 + 7 = 22 units. Total annual '
                                                                     'hours = 22 * 300 = 6,600 hours.',
                                                      'options': [   '6,600 hours',
                                                                     '6,000 hours',
                                                                     '7,200 hours',
                                                                     '5,400 hours'],
                                                      'question': 'In a technology consulting team, the billable hours '
                                                                  'for four quarters were in the ratio 4 : 5 : 6 : 7. '
                                                                  'If the difference between the fourth and second '
                                                                  'quarter billable hours was 600 hours, what were the '
                                                                  'total annual billable hours?'}],
                          'sections': [   'Quantitative & Data Interpretation',
                                          'Logical Reasoning',
                                          'Verbal Ability',
                                          'Computer Fundamentals'],
                          'tips': 'Data interpretation tables and charts are prominent. Practice fast percentage '
                                  'conversions.',
                          'type': 'Aptitude & Technical MCQ'},
                      {   'cutoff_percentage': 70,
                          'duration_minutes': 40,
                          'name': 'Technical & Case Study Interview',
                          'questions_count': 3,
                          'round_number': 2,
                          'sample_questions': [   {   'expected': [   'SELECT MAX(salary) FROM Employee WHERE salary < '
                                                                      '(SELECT MAX(salary) FROM Employee);'],
                                                      'question': 'Write an SQL query to find the second highest '
                                                                  'salary from an Employee table without using the '
                                                                  'LIMIT clause.'},
                                                  {   'expected': [   'Immutable append-only audit event log table',
                                                                      'RBAC with Users, Roles, and Permissions',
                                                                      'JWT claims containing role permissions checked '
                                                                      'in API gateway middleware',
                                                                      'Cryptographic hashing of sensitive financial '
                                                                      'records'],
                                                      'question': 'Describe how you would design an audit trail and '
                                                                  'role-based access control (RBAC) mechanism for an '
                                                                  'enterprise financial analytics dashboard.'},
                                                  {   'expected': [   'Use a Stack data structure',
                                                                      'Push open brackets onto stack',
                                                                      'Match closing brackets with top of stack',
                                                                      'O(N) time and O(N) space'],
                                                      'model_answer': 'def is_valid(s):\n'
                                                                      '    stack = []\n'
                                                                      "    mapping = {')': '(', '}': '{', ']': '['}\n"
                                                                      '    for char in s:\n'
                                                                      '        if char in mapping:\n'
                                                                      '            top = stack.pop() if stack else '
                                                                      "'#'\n"
                                                                      '            if mapping[char] != top: return '
                                                                      'False\n'
                                                                      '        else:\n'
                                                                      '            stack.append(char)\n'
                                                                      '    return not stack',
                                                      'question': 'Write a function to validate whether a given string '
                                                                  'of parentheses, brackets, and braces is balanced.'}],
                          'sections': ['SQL Queries & Joins', 'SDLC Methodologies', 'Client Problem Solving'],
                          'tips': 'Consulting requires clear communication alongside code. Explain business trade-offs '
                                  'clearly.',
                          'type': 'Technical Interview'},
                      {   'cutoff_percentage': 70,
                          'duration_minutes': 45,
                          'name': 'Business Technology & Case Analysis',
                          'questions_count': 3,
                          'round_number': 3,
                          'sample_questions': [   {   'expected': [   'Analyze legacy database bottlenecks and batch '
                                                                      'sync delays',
                                                                      'Introduce event-driven architecture (e.g. '
                                                                      'Kafka) for real-time inventory updates',
                                                                      'API Gateway integration between POS systems and '
                                                                      'cloud warehouse',
                                                                      'Phased rollout strategy with fallback'],
                                                      'model_answer': 'Begin by decoupling POS inventory updates from '
                                                                      'nightly batch processing using an event-driven '
                                                                      'architecture with Apache Kafka. Deploy an API '
                                                                      'layer connecting in-store barcode scanners to a '
                                                                      'centralized cloud inventory service. Implement '
                                                                      'a phased pilot across 10 flagship stores before '
                                                                      'nationwide rollout.',
                                                      'question': 'A legacy retail client with 500 physical stores '
                                                                  'wants to modernize their inventory system to enable '
                                                                  'real-time e-commerce pickup. How do you approach '
                                                                  'this technical transformation?'},
                                                  {   'expected': [   'Schema stability: rigid tabular vs rapidly '
                                                                      'evolving polymorphic documents',
                                                                      'ACID transactions across multiple entities vs '
                                                                      'high-speed single-document operations',
                                                                      'Complex relational JOIN queries vs hierarchical '
                                                                      'embedded documents',
                                                                      'Read/Write throughput and horizontal sharding '
                                                                      'requirements'],
                                                      'model_answer': 'Choose PostgreSQL when data has clear '
                                                                      'relational structures, requires strict ACID '
                                                                      'integrity across multiple business tables '
                                                                      '(financials, billing, order management), and '
                                                                      'relies on complex SQL joins and analytics. '
                                                                      'Choose MongoDB when the data schema is '
                                                                      'polymorphic, document-oriented (catalogs, '
                                                                      'content management), write-heavy, and requires '
                                                                      'horizontal sharding across cloud clusters.',
                                                      'question': 'How do you evaluate and choose between a relational '
                                                                  'database (e.g., PostgreSQL) and a NoSQL document '
                                                                  'database (e.g., MongoDB) for an enterprise client '
                                                                  'solution?'}],
                          'sections': [   'Cloud Migration Case Study',
                                          'Agile Methodologies',
                                          'System Integration',
                                          'Data Analysis'],
                          'tips': 'Structure answers using frameworks: Business Context -> Technical Assessment -> '
                                  'Implementation Plan -> Risk Mitigation.',
                          'type': 'Technical & Case Study'},
                      {   'cutoff_percentage': 75,
                          'duration_minutes': 35,
                          'name': 'Partner & Leadership Interview',
                          'questions_count': 3,
                          'round_number': 4,
                          'sample_questions': [   {   'answer': 'Use analogies relatable to business operations. Focus '
                                                                'on business impacts (uptime, customer checkout speed, '
                                                                'cost) rather than code-level jargon. Present clear '
                                                                'recommendations with timelines and risk assessments.',
                                                      'question': 'How do you explain a complex technical bug or '
                                                                  'architectural trade-off to a non-technical client '
                                                                  'executive?'}],
                          'sections': ['Client Communication', 'Integrity', 'Leadership', 'Deloitte Culture'],
                          'tips': 'Demonstrate executive presence, clear communication, and high emotional '
                                  'intelligence.',
                          'type': 'HR & Behavioral'}],
        'slug': 'deloitte'},
    {   'badge': 'Software Consulting Engineer / Software Engineer',
        'description': 'Worldwide leader in networking and internet infrastructure. Heavy focus on TCP/IP protocols, '
                       'socket programming, and OS kernels.',
        'eligibility': '7.0+ CGPA in B.Tech CS / IT / ECE with strong computer networking skills.',
        'hiring_season': 'Cisco Ideathon & On-Campus Drives',
        'id': 'cisco',
        'name': 'Cisco',
        'package': 'INR 15.0 LPA - INR 24.0 LPA',
        'rounds': [   {   'cutoff_percentage': 75,
                          'duration_minutes': 90,
                          'name': 'Online Assessment (Networking, Aptitude & Coding)',
                          'questions_count': 42,
                          'round_number': 1,
                          'sample_questions': [   {   'answer': '30',
                                                      'explanation': '/27 leaves 32 - 27 = 5 host bits. Total IPs = '
                                                                     '2^5 = 32. Usable host addresses = 32 - 2 '
                                                                     '(network ID & broadcast) = 30.',
                                                      'options': ['30', '32', '62', '14'],
                                                      'question': 'Given an IPv4 subnet mask 255.255.255.224 (/27), '
                                                                  'how many usable host IP addresses are available in '
                                                                  'this subnet?'},
                                                  {   'answer': 'To resolve an IP address (Network Layer) to a '
                                                                'physical MAC address (Data Link Layer) on a local LAN',
                                                      'explanation': "ARP broadcasts on Layer 2 asking 'Who has IP "
                                                                     "X.X.X.X?' and receives a unicast reply with the "
                                                                     'corresponding hardware MAC address.',
                                                      'options': [   'To resolve an IP address (Network Layer) to a '
                                                                     'physical MAC address (Data Link Layer) on a '
                                                                     'local LAN',
                                                                     'To assign dynamic IP addresses to newly '
                                                                     'connected devices',
                                                                     'To encrypt HTTP payloads using TLS',
                                                                     'To convert domain names into IP addresses'],
                                                      'question': 'In computer networking, what is the fundamental '
                                                                  'purpose of the Address Resolution Protocol (ARP)?'},
                                                  {   'answer': '30',
                                                      'explanation': '/27 prefix leaves 32 - 27 = 5 host bits. Total '
                                                                     'addresses = 2^5 = 32. Subtract 2 (network '
                                                                     'address and broadcast address) = 30 usable host '
                                                                     'addresses.',
                                                      'options': ['30', '32', '62', '28'],
                                                      'question': 'How many usable host IP addresses are available in '
                                                                  'a subnet with a /27 CIDR prefix mask?'},
                                                  {   'answer': 'To prevent broadcast storms and layer 2 bridging '
                                                                'loops while maintaining redundant links',
                                                      'explanation': 'STP prevents loops on Layer 2 Ethernet networks '
                                                                     'with redundant physical paths by blocking '
                                                                     'redundant switch ports, dynamically unblocking '
                                                                     'them if an active link fails.',
                                                      'options': [   'To prevent broadcast storms and layer 2 bridging '
                                                                     'loops while maintaining redundant links',
                                                                     'To allocate dynamic IP addresses automatically',
                                                                     'To encrypt Wi-Fi traffic across enterprise '
                                                                     'routers',
                                                                     'To accelerate TCP packet transmission speeds'],
                                                      'question': 'What is the primary role of the Spanning Tree '
                                                                  'Protocol (STP) in Ethernet switched networks?'}],
                          'sections': [   'Computer Networks (15 Qs)',
                                          'Operating Systems (15 Qs)',
                                          'Hands-on Coding (2 Problems)'],
                          'tips': 'Master CIDR subnetting, TCP 3-way handshake, OSI layers, and packet header '
                                  'structures.',
                          'type': 'Networking & Coding'},
                      {   'cutoff_percentage': 75,
                          'duration_minutes': 50,
                          'name': 'Technical Interview (Networking, Sockets & OS)',
                          'questions_count': 3,
                          'round_number': 2,
                          'sample_questions': [   {   'expected': [   'FIN -> ACK -> FIN -> ACK exchange',
                                                                      'TIME_WAIT lasts 2 * MSL (Maximum Segment '
                                                                      'Lifetime)',
                                                                      'Prevents delayed packets from being '
                                                                      'misdelivered to a new connection'],
                                                      'question': 'What happens under the hood when a TCP connection '
                                                                  'terminates via 4-way handshake, and why is the '
                                                                  'TIME_WAIT state necessary?'},
                                                  {   'expected': [   "Dijkstra's Algorithm using Min-Heap",
                                                                      'Distance array initialized to infinity',
                                                                      'O((V + E) log V) time',
                                                                      'Return max(dist) if all visited else -1'],
                                                      'model_answer': 'Build adjacency list. Use a Min-Heap '
                                                                      'initialized with (0, K). Maintain dist array '
                                                                      'initialized to infinity with dist[K] = 0. Pop '
                                                                      '(d, u): if d > dist[u], continue. For each '
                                                                      'neighbor (v, w): if d + w < dist[v], dist[v] = '
                                                                      'd + w, push (dist[v], v). After heap is empty, '
                                                                      'if max(dist) is infinity return -1; else return '
                                                                      'max(dist).',
                                                      'question': 'Given a network of N nodes connected by directed '
                                                                  'weighted edges, find the minimum time it takes for '
                                                                  'a signal sent from node K to reach all nodes. If '
                                                                  'impossible, return -1 (Network Delay Time).'},
                                                  {   'expected': [   'Iterate 32 times',
                                                                      'Shift result left and extract lowest bit from '
                                                                      'input',
                                                                      'Shift input right',
                                                                      'O(1) time and space'],
                                                      'model_answer': 'def reverse_bits(n):\n'
                                                                      '    res = 0\n'
                                                                      '    for _ in range(32):\n'
                                                                      '        res = (res << 1) | (n & 1)\n'
                                                                      '        n >>= 1\n'
                                                                      '    return res',
                                                      'question': 'Write a program to reverse the bits of a 32-bit '
                                                                  'unsigned integer.'}],
                          'sections': ['Socket Programming', 'TCP vs UDP Congestion Control', 'Linux Kernel & Memory'],
                          'tips': 'Explain the TCP sliding window, TIME_WAIT socket states, and packet flow from NIC '
                                  'to user space.',
                          'type': 'Technical Interview'},
                      {   'cutoff_percentage': 75,
                          'duration_minutes': 50,
                          'name': 'Network Architecture & Systems Programming',
                          'questions_count': 4,
                          'round_number': 3,
                          'sample_questions': [   {   'expected': [   'Application: Browser checks cache, triggers DNS '
                                                                      'lookup',
                                                                      'Transport: TCP 3-way handshake established on '
                                                                      'port 443, followed by TLS 1.3 cryptographic '
                                                                      'handshake',
                                                                      'Network: IP routing, ARP resolution to gateway '
                                                                      'MAC address',
                                                                      'Data Link & Physical: Framing, ethernet packets '
                                                                      'transmitted over physical medium',
                                                                      'HTTP GET request sent, web server returns HTML '
                                                                      'response'],
                                                      'model_answer': 'DNS resolves domain to IP via UDP 53. Transport '
                                                                      'layer initiates TCP 3-way handshake (SYN, '
                                                                      'SYN-ACK, ACK) on port 443, followed by TLS '
                                                                      'handshake negotiating cipher suites. Network '
                                                                      'layer encapsulates into IP packets routed via '
                                                                      'OSPF/BGP. Data link layer uses ARP to resolve '
                                                                      'local gateway MAC. Upon connection, HTTP GET is '
                                                                      'sent and response stream is rendered.',
                                                      'question': 'Explain what happens step-by-step at each layer of '
                                                                  'the OSI model when a user enters '
                                                                  "'https://www.cisco.com' in a browser."}],
                          'sections': [   'TCP/IP Stack',
                                          'Socket Programming',
                                          'Subnetting & Routing',
                                          'C/C++ Memory Management'],
                          'tips': 'Cisco deeply examines packet flow across layers, memory efficiency, and bit '
                                  'manipulation.',
                          'type': 'Technical Interview'},
                      {   'cutoff_percentage': 70,
                          'duration_minutes': 35,
                          'name': 'Executive & Cultural Fitment',
                          'questions_count': 3,
                          'round_number': 4,
                          'sample_questions': [   {   'answer': "Highlight that 80%+ of the world's internet traffic "
                                                                'traverses Cisco equipment. Express your passion for '
                                                                'building resilient, high-speed networking systems '
                                                                'that connect hospitals, governments, and universities '
                                                                'worldwide.',
                                                      'question': 'Why do you want to build foundational internet '
                                                                  'hardware and software at Cisco?'}],
                          'sections': ['Conscious Culture', 'Teamwork', 'Global Collaboration', 'Ethics'],
                          'tips': "Familiarize yourself with Cisco's 'Conscious Culture' and give examples of ethical "
                                  'decision making.',
                          'type': 'HR & Behavioral'}],
        'slug': 'cisco'},
    {   'badge': 'Member of Technical Staff (MTS-1)',
        'description': 'Creative software and digital experience leader. Focuses on advanced algorithms, memory '
                       'efficiency, and complex mathematical problem solving.',
        'eligibility': '7.5+ CGPA with exceptional programming and algorithmic skill.',
        'hiring_season': 'Adobe SheCodes & On-Campus Drives',
        'id': 'adobe',
        'name': 'Adobe',
        'package': 'INR 40.0 LPA - INR 48.0 LPA',
        'rounds': [   {   'cutoff_percentage': 80,
                          'duration_minutes': 90,
                          'name': 'Online Assessment (OA)',
                          'questions_count': 32,
                          'round_number': 1,
                          'sample_questions': [   {   'answer': 'Undefined behavior (derived destructor not called, '
                                                                'causing resource leaks)',
                                                      'explanation': 'Deleting an object through a base pointer '
                                                                     'without a virtual destructor causes undefined '
                                                                     'behavior; the derived class destructor will not '
                                                                     'execute.',
                                                      'options': [   'Undefined behavior (derived destructor not '
                                                                     'called, causing resource leaks)',
                                                                     'Derived destructor is called automatically',
                                                                     'Compile-time error',
                                                                     'Segmentation fault immediately'],
                                                      'question': 'In C++, what happens when a derived class object is '
                                                                  'deleted through a base class pointer that does not '
                                                                  'have a virtual destructor?'},
                                                  {   'answer': 'Bezier curves are parametric polynomial curves that '
                                                                'scale infinitely without pixelation or quality loss',
                                                      'explanation': 'Parametric Bernstein polynomial formulas allow '
                                                                     'glyphs and paths to be mathematically '
                                                                     're-rasterized at any DPI or zoom level with '
                                                                     'crisp edges.',
                                                      'options': [   'Bezier curves are parametric polynomial curves '
                                                                     'that scale infinitely without pixelation or '
                                                                     'quality loss',
                                                                     'Raster pixels run faster on CPU',
                                                                     'Bezier curves only work in black and white',
                                                                     'Vector art requires 100x more memory than bitmap '
                                                                     'images'],
                                                      'question': 'In graphic processing and document rendering '
                                                                  'engines, why are Bezier Curves preferred over '
                                                                  'raster pixel grids for scalable font glyphs and '
                                                                  'vector art?'},
                                                  {   'answer': 'Approximately 5.93 MB',
                                                      'explanation': 'Total pixels = 1920 * 1080 = 2,073,600 pixels. '
                                                                     '24 bits = 3 bytes per pixel. Total bytes = '
                                                                     '2,073,600 * 3 = 6,220,800 bytes. In megabytes '
                                                                     '(MB) = 6,220,800 / (1024 * 1024) = 5.93 MB.',
                                                      'options': [   'Approximately 5.93 MB',
                                                                     'Approximately 2.07 MB',
                                                                     'Approximately 8.35 MB',
                                                                     'Approximately 12.5 MB'],
                                                      'question': 'A digital image of dimensions 1920 x 1080 pixels '
                                                                  'uses 24-bit TrueColor depth (8 bits per RGB '
                                                                  'channel). Assuming no compression, what is the raw '
                                                                  'memory size required to store this uncompressed '
                                                                  'frame in megabytes (MB)?'}],
                          'sections': ['Computer Science MCQs (30 Qs)', 'Algorithmic Problems (2 Problems)'],
                          'tips': 'Coding questions frequently draw from Dynamic Programming and Geometric/Matrix '
                                  'algorithms.',
                          'type': 'Advanced Coding & CS'},
                      {   'cutoff_percentage': 85,
                          'duration_minutes': 60,
                          'name': 'Technical Interview (Algorithms & Memory)',
                          'questions_count': 2,
                          'round_number': 2,
                          'sample_questions': [   {   'expected': [   'Recursive bottom-up traversal',
                                                                      'Base cases returning current node if matched',
                                                                      'Combining left and right subtree results'],
                                                      'question': 'Design an algorithm to find the lowest common '
                                                                  'ancestor (LCA) of two nodes in a binary tree in '
                                                                  'O(N) time and O(H) space.'},
                                                  {   'expected': [   'BFS or DFS traversal',
                                                                      "Sink visited land cells (set grid[r][c] = '0')",
                                                                      'O(M * N) time and O(M * N) space',
                                                                      'Handle 4-directional boundary conditions'],
                                                      'model_answer': "Iterate through each cell (r, c). When a '1' is "
                                                                      'encountered, increment island count and trigger '
                                                                      "DFS/BFS to visit and flip all connected '1's "
                                                                      "(up, down, left, right) to '0'. Continue "
                                                                      'scanning. Returns total island count in O(M * '
                                                                      'N) time.',
                                                      'question': 'Given an m x n 2D binary grid grid which represents '
                                                                  "a map of '1's (land) and '0's (water), return the "
                                                                  'number of islands (connected components '
                                                                  '4-directionally).\n'
                                                                  'Input: grid with 1s and 0s\n'
                                                                  'Output: Number of islands'},
                                                  {   'expected': [   'Maintain tails array where tails[i] stores '
                                                                      'smallest tail of increasing subsequence of '
                                                                      'length i+1',
                                                                      'Binary search (`bisect_left`) to find position '
                                                                      'of current element',
                                                                      'O(N log N) time and O(N) space'],
                                                      'model_answer': 'import bisect\n'
                                                                      'def length_of_lis(nums):\n'
                                                                      '    tails = []\n'
                                                                      '    for x in nums:\n'
                                                                      '        idx = bisect.bisect_left(tails, x)\n'
                                                                      '        if idx == len(tails):\n'
                                                                      '            tails.append(x)\n'
                                                                      '        else:\n'
                                                                      '            tails[idx] = x\n'
                                                                      '    return len(tails)',
                                                      'question': 'Implement an algorithm to find the Longest '
                                                                  'Increasing Subsequence (LIS) in an integer array in '
                                                                  '$O(N \\log N)$ time using binary search (Patience '
                                                                  'Sorting).'}],
                          'sections': ['Advanced Data Structures', 'C++ Memory Management', 'Optimization'],
                          'tips': 'Discuss cache locality, pointer indirection costs, and clean object-oriented '
                                  'architecture.',
                          'type': 'Technical Interview'},
                      {   'cutoff_percentage': 75,
                          'duration_minutes': 50,
                          'name': 'Advanced Algorithms & System Design',
                          'questions_count': 4,
                          'round_number': 3,
                          'sample_questions': [   {   'expected': [   'Use a Trie (Prefix Tree) data structure',
                                                                      'Each Trie node stores top 5 trending search '
                                                                      'queries matching the prefix',
                                                                      'Prefix lookup is O(L) where L is length of '
                                                                      'typed query string',
                                                                      'Decouple updates using asynchronous batch '
                                                                      'processing'],
                                                      'model_answer': 'Use a Trie data structure. To avoid traversing '
                                                                      'subtrees on every keystroke, cache the top 5 '
                                                                      'most frequently searched terms directly inside '
                                                                      'each Trie node. Lookup time becomes O(L) where '
                                                                      'L is the prefix length, completely independent '
                                                                      'of total dictionary size.',
                                                      'question': 'How would you design an efficient Autocomplete / '
                                                                  'Search Suggestion system that returns top 5 '
                                                                  'suggested queries for millions of users?'},
                                                  {   'expected': [   'Upload raw asset to cloud object storage (e.g. '
                                                                      'S3)',
                                                                      'Enqueue render job into distributed message '
                                                                      'queue (e.g. SQS/Kafka)',
                                                                      'Auto-scaling pool of GPU/CPU worker nodes '
                                                                      'picking up jobs',
                                                                      'Chunking video into segments for parallel '
                                                                      'transcoding',
                                                                      'Stitch segments and notify client via WebSocket '
                                                                      '/ Webhook'],
                                                      'model_answer': 'When an export is triggered, upload the project '
                                                                      'payload to S3 and publish a job event to SQS. '
                                                                      'An auto-scaling fleet of stateless GPU worker '
                                                                      'instances consumes jobs from SQS. The worker '
                                                                      'splits long videos into 10-second GOP chunks, '
                                                                      'transcodes chunks in parallel across worker '
                                                                      'nodes using FFmpeg, stitches the transcoded '
                                                                      'chunks together, and writes the output back to '
                                                                      'S3. A webhook or WebSocket notification alerts '
                                                                      'the client when the export is complete.',
                                                      'question': 'How would you design a scalable background video '
                                                                  'rendering and transcoding pipeline capable of '
                                                                  'processing thousands of high-definition export '
                                                                  'requests concurrently?'}],
                          'sections': [   'Trees & Graphs',
                                          'Dynamic Programming',
                                          'Scalable Queue Architecture',
                                          'OOP Design'],
                          'tips': 'Adobe asks complex algorithmic problems and low-level object-oriented design '
                                  'questions.',
                          'type': 'Technical Interview'},
                      {   'cutoff_percentage': 75,
                          'duration_minutes': 40,
                          'name': 'Managerial & Creativity Round',
                          'questions_count': 3,
                          'round_number': 4,
                          'sample_questions': [   {   'answer': 'Discuss how UI responsiveness directly impacts '
                                                                'creative flow. Emphasize offloading heavy computation '
                                                                'to background threads or Web Workers, implementing '
                                                                'optimistic UI updates, and profiling frame rates to '
                                                                'ensure smooth user interactions.',
                                                      'question': 'Adobe products empower creators worldwide. How do '
                                                                  'you balance writing mathematically optimal code '
                                                                  'with providing a delightful user experience?'}],
                          'sections': ['Creativity', 'Customer Empathy', 'Product Thinking', 'Adobe Values'],
                          'tips': 'Show high empathy for creative professionals and software usability.',
                          'type': 'HR & Behavioral'}],
        'slug': 'adobe'},
    {   'badge': 'Walmart CodeHers / Campus SDE',
        'description': 'Walmart Global Tech India builds high-scale retail software, distributed supply-chain '
                       'microservices, and omnichannel checkout infrastructure processing billions of transactions.',
        'eligibility': 'B.Tech / M.Tech in CS / IT / ECE with 7.0+ CGPA and zero active backlogs.',
        'hiring_season': 'July - October (On-Campus & CodeHers)',
        'id': 'walmart',
        'name': 'Walmart Global Tech',
        'package': 'INR 18.0 LPA - INR 28.0 LPA',
        'rounds': [   {   'cutoff_percentage': 75,
                          'duration_minutes': 90,
                          'name': 'Online Technical Assessment (DSA & Core CS)',
                          'questions_count': 22,
                          'round_number': 1,
                          'sample_questions': [   {   'answer': 'Repeatable Read',
                                                      'explanation': 'Under ANSI SQL standards, Repeatable Read holds '
                                                                     'shared read locks until the transaction ends, '
                                                                     'preventing Dirty Reads and Non-Repeatable Reads. '
                                                                     'Phantom Reads can only occur if range locks are '
                                                                     'not acquired, which requires Serializable '
                                                                     'isolation.',
                                                      'options': [   'Read Uncommitted',
                                                                     'Read Committed',
                                                                     'Repeatable Read',
                                                                     'Serializable'],
                                                      'question': 'Which database isolation level prevents both Dirty '
                                                                  'Reads and Non-Repeatable Reads, but may still '
                                                                  'permit Phantom Reads under the ANSI SQL standard?'},
                                                  {   'answer': 'Use a deque to maintain a sliding window of prefix '
                                                                'sums of length up to k, keeping elements '
                                                                'monotonically increasing so the minimum prefix sum is '
                                                                'available at the front in O(1) amortized time, '
                                                                'yielding O(N) overall time complexity.',
                                                      'question': 'Given an array of product prices and an integer '
                                                                  'target, describe an optimal algorithm to find the '
                                                                  'maximum sub-array sum with at most k elements.'},
                                                  {   'answer': 'Trie augmented with Min-Heaps at each node',
                                                      'explanation': 'A Trie stores prefixes; storing top-K search '
                                                                     'frequencies directly at nodes allows O(L) prefix '
                                                                     'lookup without searching the entire sub-tree.',
                                                      'options': [   'Trie augmented with Min-Heaps at each node',
                                                                     'Unindexed SQLite database',
                                                                     'B+ Tree on disk',
                                                                     'Unsorted circular linked list'],
                                                      'question': 'What is the optimal data structure to support Top-K '
                                                                  "search recommendations in Walmart's search bar with "
                                                                  'sub-millisecond query latency?'},
                                                  {   'answer': '230 m',
                                                      'explanation': 'Relative speed = (54+72) × 5/18 = 126 × 5/18 = '
                                                                     '35 m/s. Total distance = speed × time = 35 × 10 '
                                                                     '= 350 m. Other train = 350 - 120 = 230 m.',
                                                      'options': ['230 m', '200 m', '250 m', '180 m'],
                                                      'question': 'Two trains running in opposite directions cross '
                                                                  'each other in 10 seconds. If the speeds are 54 km/h '
                                                                  'and 72 km/h and one train is 120 m long, find the '
                                                                  'length of the other train.'}],
                          'sections': ['Data Structures', 'Algorithms', 'Operating Systems', 'DBMS & SQL'],
                          'tips': 'Solve both algorithmic coding problems with optimal time complexity and brush up on '
                                  'indexing and transaction isolation levels.',
                          'type': 'Coding & Technical MCQ'},
                      {   'cutoff_percentage': 75,
                          'duration_minutes': 60,
                          'name': 'Technical Interview 1: Data Structures & Problem Solving',
                          'questions_count': 2,
                          'round_number': 2,
                          'sample_questions': [   {   'answer': 'Compute topological ordering using Kahn algorithm '
                                                                '(in-degrees) or DFS post-order. Initialize distances '
                                                                'to negative infinity, then relax outgoing edges in '
                                                                'topological order in O(V + E) time.',
                                                      'question': 'Given a directed acyclic graph (DAG) representing '
                                                                  'store inventory dependencies, find the longest path '
                                                                  'from any source to any sink node in O(V + E) time.'},
                                                  {   'expected': [   'Monotonic Deque storing indices',
                                                                      'Maintain strictly decreasing elements in deque',
                                                                      'Evict out-of-window indices from front',
                                                                      'O(N) time and O(K) space'],
                                                      'model_answer': 'Use a Double-ended Queue (deque) that maintains '
                                                                      'indices in monotonically decreasing order of '
                                                                      'values. For each index i: remove indices from '
                                                                      'back whose values are <= nums[i]. Remove front '
                                                                      'index if it falls outside [i - k + 1, i]. '
                                                                      'Append i. When i >= k - 1, the front of the '
                                                                      'deque is the maximum for the current window.',
                                                      'question': 'Given an array of integers nums and a sliding '
                                                                  'window of size k moving from left to right, return '
                                                                  'the max sliding window.\n'
                                                                  'Input: nums = [1,3,-1,-3,5,3,6,7], k = 3\n'
                                                                  'Output: [3,3,5,5,6,7]'},
                                                  {   'expected': [   'Use min-heap (priority queue) of size K',
                                                                      'Push head of each list to heap',
                                                                      'Pop minimum, add to result, push next node from '
                                                                      'that list',
                                                                      'O(N log K) time where N is total elements'],
                                                      'model_answer': 'import heapq\n'
                                                                      'def merge_k_lists(lists):\n'
                                                                      '    heap = [(l.val, i, l) for i, l in '
                                                                      'enumerate(lists) if l]\n'
                                                                      '    heapq.heapify(heap)\n'
                                                                      '    dummy = curr = ListNode(0)\n'
                                                                      '    while heap:\n'
                                                                      '        val, i, node = heapq.heappop(heap)\n'
                                                                      '        curr.next = node\n'
                                                                      '        curr = curr.next\n'
                                                                      '        if node.next:\n'
                                                                      '            heapq.heappush(heap, '
                                                                      '(node.next.val, i, node.next))\n'
                                                                      '    return dummy.next',
                                                      'question': 'Implement a function to merge K sorted linked lists '
                                                                  'into one sorted linked list.'}],
                          'sections': ['Dynamic Programming', 'Trees & Graphs', 'Edge Case Analysis'],
                          'tips': 'Communicate your thought process before writing code. Clarify constraints like '
                                  'negative weights and integer overflow.',
                          'type': 'Live Coding & Algorithms'},
                      {   'cutoff_percentage': 75,
                          'duration_minutes': 60,
                          'name': 'Technical Interview 2: Low-Level Design & Concurrency',
                          'questions_count': 2,
                          'round_number': 3,
                          'sample_questions': [   {   'answer': 'Combine a doubly linked list with a hash map. The '
                                                                'hash map maps keys to list nodes for O(1) lookup. '
                                                                'When accessed or updated, move node to the head. When '
                                                                'capacity is exceeded, evict from tail. Protect '
                                                                'mutations with a ReadWriteLock or concurrent '
                                                                'primitives.',
                                                      'question': 'Design an in-memory thread-safe LRU Cache with O(1) '
                                                                  'get and put operations in Java or Python.'},
                                                  {   'expected': [   'Saga Pattern (Orchestration with '
                                                                      'Kafka/Temporal)',
                                                                      'Compensating transactions on failure',
                                                                      'Outbox pattern for atomic DB write + Kafka '
                                                                      'message emission',
                                                                      'Idempotency keys on all payment webhooks'],
                                                      'model_answer': 'Avoid blocking Two-Phase Commit. Use the Saga '
                                                                      'pattern: an Order Orchestrator sends events via '
                                                                      'Kafka. Transactional Outbox pattern guarantees '
                                                                      'the DB commit and message dispatch occur '
                                                                      'atomically. If stock reservation fails, '
                                                                      'compensating events trigger payment refunds and '
                                                                      'order cancellation.',
                                                      'question': 'How do you handle distributed transactions and '
                                                                  'event consistency across Order, Payment, and Stock '
                                                                  "services in Walmart's e-commerce backend during "
                                                                  'high-concurrency flash sales?'}],
                          'sections': ['Object-Oriented Design', 'Multithreading', 'Design Patterns'],
                          'tips': 'Apply SOLID principles, explain thread synchronization mechanisms (synchronized, '
                                  'ReentrantLock), and draw clean class diagrams.',
                          'type': 'LLD & System Architecture'},
                      {   'cutoff_percentage': 70,
                          'duration_minutes': 45,
                          'name': 'Managerial & Cultural Fit',
                          'questions_count': 3,
                          'round_number': 4,
                          'sample_questions': [   {   'answer': 'Explain with Situation, Task, Action, and '
                                                                'quantifiable Result, focusing on rapid risk triage, '
                                                                'communication with stakeholders, and implementing a '
                                                                'resilient solution under tight constraints.',
                                                      'question': 'Tell me about a time when you identified a critical '
                                                                  'flaw in your software architecture right before a '
                                                                  'project deadline. How did you prioritize and '
                                                                  'address it?'}],
                          'sections': ['Customer Obsession', 'Ownership Mindset', 'Team Collaboration'],
                          'tips': 'Use the STAR method and emphasize customer-centric engineering decisions you made '
                                  'in college projects.',
                          'type': 'Behavioral & Leadership'}],
        'slug': 'walmart'},
    {   'badge': 'Freshworks Campus SDE',
        'description': 'Leading SaaS enterprise product company providing intuitive CRM, IT service management '
                       '(Freshservice), and customer support software (Freshdesk) serving over 65,000 businesses '
                       'globally.',
        'eligibility': 'B.Tech / BE / MCA with 65% or 6.5+ CGPA and strong programming skills.',
        'hiring_season': 'August - November',
        'id': 'freshworks',
        'name': 'Freshworks',
        'package': 'INR 12.0 LPA - INR 18.0 LPA',
        'rounds': [   {   'cutoff_percentage': 70,
                          'duration_minutes': 90,
                          'name': 'Online Aptitude & Coding Assessment',
                          'questions_count': 30,
                          'round_number': 1,
                          'sample_questions': [   {   'answer': 'PUT',
                                                      'explanation': 'PUT is defined by RFC 7231 as an idempotent '
                                                                     'method intended to replace the entire target '
                                                                     'resource with the requested payload, whereas '
                                                                     'PATCH is non-idempotent and updates partial '
                                                                     'fields.',
                                                      'options': ['POST', 'PUT', 'PATCH', 'CONNECT'],
                                                      'question': 'In a RESTful API design, which HTTP method should '
                                                                  'be used for idempotent updates that replace the '
                                                                  'entire resource state?'},
                                                  {   'answer': 'Maintain a balanced binary search tree or two heaps '
                                                                '(max-heap for lower 95% and min-heap for upper 5%) '
                                                                'while pruning expired timestamps outside the 1-hour '
                                                                'window.',
                                                      'question': 'Given a stream of incoming customer support tickets '
                                                                  'with timestamps, write a function to calculate the '
                                                                  '95th percentile resolution time over a sliding '
                                                                  '1-hour window.'},
                                                  {   'answer': 'Shared Database with Shared Schema and PostgreSQL '
                                                                'Row-Level Security (RLS)',
                                                      'explanation': 'Shared database + shared schema utilizes '
                                                                     'hardware resources efficiently while PostgreSQL '
                                                                     'Row-Level Security (RLS) automatically enforces '
                                                                     "'WHERE tenant_id = current_tenant' at the "
                                                                     'database engine level.',
                                                      'options': [   'Shared Database with Shared Schema and '
                                                                     'PostgreSQL Row-Level Security (RLS)',
                                                                     'Database per Tenant with dedicated EC2 instance '
                                                                     'for each customer',
                                                                     'Unindexed JSON files in an AWS S3 bucket',
                                                                     'Single flat CSV file'],
                                                      'question': 'In a multitenant SaaS CRM database like Freshsales, '
                                                                  'which architectural partitioning approach provides '
                                                                  'strong tenant data isolation while minimizing cloud '
                                                                  'infrastructure cost?'},
                                                  {   'answer': '10 days',
                                                      'explanation': '1/A+1/B = 1/12, 1/B+1/C = 1/15, 1/C+1/A = 1/20. '
                                                                     'Adding all: 2(1/A+1/B+1/C) = 1/12+1/15+1/20 = '
                                                                     '5+4+3/60 = 12/60 = 1/5. So 1/A+1/B+1/C = 1/10. '
                                                                     'Together: 10 days.',
                                                      'options': ['10 days', '8 days', '9 days', '12 days'],
                                                      'question': 'A and B together can complete a task in 12 days. B '
                                                                  'and C together in 15 days. C and A together in 20 '
                                                                  'days. How many days will all three take together?'}],
                          'sections': ['Quantitative Aptitude', 'Verbal Reasoning', 'Coding Problems'],
                          'tips': 'Practice string manipulation, array hashing, and clean code formatting in modern '
                                  'programming languages.',
                          'type': 'Aptitude & DSA Coding'},
                      {   'cutoff_percentage': 75,
                          'duration_minutes': 90,
                          'name': 'Machine Coding / Modular Design Round',
                          'questions_count': 1,
                          'round_number': 2,
                          'sample_questions': [   {   'answer': 'Create Ticket, User, SLAStrategy, and '
                                                                'NotificationObserver models. Use the Strategy pattern '
                                                                'for escalation routing and Observer pattern for '
                                                                'alerts. Ensure all inputs are validated cleanly.',
                                                      'question': 'Design and code a command-line Issue Tracking and '
                                                                  'Escalation System with priority levels, assignment '
                                                                  'rules, and SLA breach notifications.'},
                                                  {   'expected': [   'Hash Map for O(1) key lookup',
                                                                      'Min-Heap or PriorityQueue for O(log N) '
                                                                      'expiration tracking',
                                                                      'Passive eviction on get() + Active background '
                                                                      'cleanup thread',
                                                                      'Thread-safe locking'],
                                                      'model_answer': 'Use a dictionary mapping key -> (value, '
                                                                      'expire_timestamp). On get(key): check if '
                                                                      'current_time > expire_timestamp; if expired, '
                                                                      'delete and return None. Maintain a background '
                                                                      'daemon thread that periodically checks a '
                                                                      'Min-Heap of (expire_timestamp, key) to purge '
                                                                      'stale keys actively without bloating RAM.',
                                                      'question': 'Design an In-Memory Key-Value Cache with '
                                                                  'Time-to-Live (TTL) expiration in Python or Java.\n'
                                                                  'Operations: set(key, value, ttl_seconds), get(key) '
                                                                  '-> value or None.'},
                                                  {   'expected': [   'Options: separate databases, separate schemas, '
                                                                      'shared schema with tenant_id',
                                                                      'Shared schema with tenant_id column for cost '
                                                                      'efficiency at scale',
                                                                      'Row-level security policies for data isolation',
                                                                      'Connection pooling with tenant context '
                                                                      'injection'],
                                                      'model_answer': 'Use shared database with tenant_id column on '
                                                                      'every table (most scalable for SMB SaaS). '
                                                                      'Implement PostgreSQL Row-Level Security (RLS) '
                                                                      'policies so queries automatically filter by '
                                                                      'tenant. Connection middleware injects SET '
                                                                      'app.current_tenant before each request. For '
                                                                      'enterprise customers requiring strict '
                                                                      'isolation, offer dedicated schema or database '
                                                                      'tier.',
                                                      'question': 'Design a multi-tenant SaaS application where each '
                                                                  "customer's data is isolated. What database strategy "
                                                                  'would you use?'}],
                          'sections': ['Clean Code', 'OOP Design', 'Extensibility', 'Unit Testing'],
                          'tips': 'Write modular code with proper separation of concerns (controller, service, '
                                  'repository, models). Do not cram all logic in a single main function.',
                          'type': 'Machine Coding & Implementation'},
                      {   'cutoff_percentage': 75,
                          'duration_minutes': 60,
                          'name': 'Technical Architecture & Deep Dive',
                          'questions_count': 2,
                          'round_number': 3,
                          'sample_questions': [   {   'answer': 'Shared-schema isolates data via tenant_id column and '
                                                                'row-level security policies, requiring minimal '
                                                                'infrastructure overhead. Schema-per-tenant isolates '
                                                                'data via separate Postgres schemas, offering higher '
                                                                'compliance at higher migration cost. Data leaks are '
                                                                'prevented using parameterized ORM filters and '
                                                                'mandatory session tenant contexts.',
                                                      'question': 'How does multi-tenant database architecture differ '
                                                                  'between shared-database shared-schema vs '
                                                                  'schema-per-tenant, and how do you prevent data '
                                                                  'leaks between tenants?'}],
                          'sections': ['Database Optimization', 'WebSockets', 'Caching Strategies'],
                          'tips': 'Demonstrate knowledge of Redis caching, database indexes, connection pooling, and '
                                  'multi-tenant architectures.',
                          'type': 'Technical Interview'},
                      {   'cutoff_percentage': 70,
                          'duration_minutes': 45,
                          'name': 'HR & Values Alignment',
                          'questions_count': 3,
                          'round_number': 4,
                          'sample_questions': [   {   'answer': 'Emphasize your desire to have continuous ownership of '
                                                                'product features, measuring real user adoption '
                                                                'metrics, and iterating rapidly based on customer '
                                                                'telemetry and feedback.',
                                                      'question': 'Why are you passionate about working at a SaaS '
                                                                  'product company like Freshworks compared to '
                                                                  'traditional IT services?'}],
                          'sections': ['Craftsmanship', 'Empathy', 'Growth Mindset'],
                          'tips': 'Demonstrate genuine interest in SaaS product usability and explain how you '
                                  'prioritize customer happiness in engineering.',
                          'type': 'Culture & Career Goals'}],
        'slug': 'freshworks'},
    {   'badge': 'Flipkart GRiD / SDE-1 Campus',
        'description': 'India leading homegrown e-commerce pioneer, part of Walmart Inc. Renowned for its challenging '
                       '90-minute Machine Coding round and rigorous problem-solving standards.',
        'eligibility': 'B.Tech / M.Tech in CS / IT / Circuital branches with 7.0+ CGPA.',
        'hiring_season': 'July - October',
        'id': 'flipkart',
        'name': 'Flipkart',
        'package': 'INR 26.0 LPA - INR 34.0 LPA',
        'rounds': [   {   'cutoff_percentage': 80,
                          'duration_minutes': 90,
                          'name': 'Online Assessment (Algorithms & Problem Solving)',
                          'questions_count': 3,
                          'round_number': 1,
                          'sample_questions': [   {   'answer': 'O(E + V log V)',
                                                      'explanation': 'With a Fibonacci heap, decrease-key operations '
                                                                     'take O(1) amortized time, leading to O(E) for '
                                                                     'all edge relaxations, while extract-min takes '
                                                                     'O(log V) amortized time across V vertices, '
                                                                     'totaling O(E + V log V).',
                                                      'options': ['O(V^2)', 'O(E + V log V)', 'O(E log V)', 'O(V * E)'],
                                                      'question': 'What is the time complexity of finding the shortest '
                                                                  'path in a weighted graph with non-negative edge '
                                                                  'weights using a Fibonacci heap implementation of '
                                                                  'Dijkstra algorithm?'},
                                                  {   'answer': 'Model as binary search on answer combined with a '
                                                                'greedy verification function or dynamic programming '
                                                                'with bitmask states for constrained path routing.',
                                                      'question': 'Given delivery hubs and transit times, find the '
                                                                  'minimum time to deliver all orders using at most k '
                                                                  'delivery executives.'},
                                                  {   'expected': [   'Clean classes: ParkingLot, Floor, ParkingSpot, '
                                                                      'Vehicle (Motorcycle, Car, Truck), Ticket',
                                                                      'Strategy pattern for pricing calculation',
                                                                      'Thread-safe spot assignment using locks',
                                                                      'Clean API: park_vehicle(), unpark_vehicle()'],
                                                      'model_answer': 'Define abstract Vehicle class with subclasses '
                                                                      'Car, Bike, Truck. ParkingSpot has SpotType and '
                                                                      'is_available. Floor contains list of spots. '
                                                                      'ParkingLot singleton manages floors. '
                                                                      'park(vehicle) finds first matching spot, marks '
                                                                      'occupied, generates Ticket with timestamp. '
                                                                      'unpark(ticket) calculates fee via '
                                                                      'PricingStrategy, frees spot.',
                                                      'question': 'Design a low-level object-oriented Parking Lot '
                                                                  'System supporting multiple spot types (Motorcycle, '
                                                                  'Compact, Large), automated ticket generation, and '
                                                                  'fee calculation based on duration.'},
                                                  {   'expected': [   'Track both max and min products (negative × '
                                                                      'negative = positive)',
                                                                      'At each position: max_prod = max(nums[i], '
                                                                      'max_prod*nums[i], min_prod*nums[i])',
                                                                      'Similarly for min_prod',
                                                                      'O(N) time, O(1) space'],
                                                      'model_answer': 'Track max_prod, min_prod, result. For each num: '
                                                                      'if num < 0, swap max_prod and min_prod. '
                                                                      'max_prod = max(num, max_prod*num). min_prod = '
                                                                      'min(num, min_prod*num). result = max(result, '
                                                                      'max_prod). O(N) time.',
                                                      'question': 'Given an array of N integers, find the contiguous '
                                                                  'subarray with the maximum product.'}],
                          'sections': ['Dynamic Programming', 'Graph Algorithms', 'Greedy Techniques'],
                          'tips': 'All 3 algorithmic problems must pass 100% of hidden test cases with strict time '
                                  'limits (1.0s).',
                          'type': 'HackerRank Coding'},
                      {   'cutoff_percentage': 80,
                          'duration_minutes': 90,
                          'name': 'Machine Coding Round (The Flipkart Signature Round)',
                          'questions_count': 1,
                          'round_number': 2,
                          'sample_questions': [   {   'answer': 'Create Product, Inventory, Reservation, and User '
                                                                'models. Implement concurrency control using '
                                                                'synchronized blocks or ConcurrentHashMap with lock '
                                                                'striping. Apply State pattern for reservation '
                                                                'lifecycles and Strategy pattern for discount engines.',
                                                      'question': 'Design and implement an in-memory Flash Sale '
                                                                  'Inventory Booking System that handles concurrent '
                                                                  'reservations, cart timeouts (10 mins), and stock '
                                                                  'replenishment.'},
                                                  {   'expected': [   'Sort jobs by end time',
                                                                      'Dynamic programming: dp[i] = max(dp[i-1], '
                                                                      'job.profit + dp[latest_non_conflicting])',
                                                                      'Binary search (bisect) to find non-conflicting '
                                                                      'job in O(log N)',
                                                                      'O(N log N) total time'],
                                                      'model_answer': 'Sort jobs by end time. Define dp[i] as maximum '
                                                                      'profit using a subset of first i jobs. For job '
                                                                      'i, use binary search to find the latest job j '
                                                                      'whose end time <= job[i].start. dp[i] = '
                                                                      'max(dp[i-1], job[i].profit + dp[j]). Total '
                                                                      'runtime is O(N log N).',
                                                      'question': 'Given n jobs where every job has a start time, end '
                                                                  'time, and profit, find the maximum profit you can '
                                                                  'achieve such that no two jobs overlap.\n'
                                                                  'Input: startTime = [1,2,3,3], endTime = [3,4,5,6], '
                                                                  'profit = [50,10,40,70]\n'
                                                                  'Output: 120'},
                                                  {   'expected': [   'Redis for atomic inventory decrement (DECR '
                                                                      'command)',
                                                                      'Optimistic locking or distributed locks for '
                                                                      'race condition prevention',
                                                                      'Event-driven architecture with Kafka for order '
                                                                      'processing',
                                                                      'Database eventual consistency with '
                                                                      'reconciliation jobs'],
                                                      'model_answer': 'Use Redis DECR for atomic stock countdown '
                                                                      'during flash sales. If DECR returns ≥ 0, allow '
                                                                      'order; if < 0, reject and INCR back. Push '
                                                                      'successful orders to Kafka for async database '
                                                                      'persistence. Run reconciliation jobs to sync '
                                                                      'Redis and PostgreSQL inventory.',
                                                      'question': 'Design a real-time inventory management system for '
                                                                  'an e-commerce platform handling flash sales with '
                                                                  '100K concurrent users.'}],
                          'sections': ['Object-Oriented Design', 'Design Patterns', 'Executable Driver Code'],
                          'tips': 'Focus on writing clean, working, extensible code with in-memory data structures. '
                                  'Implement demo driver code in main() to demonstrate all functional requirements.',
                          'type': 'Live Modular Coding & OOP'},
                      {   'cutoff_percentage': 75,
                          'duration_minutes': 60,
                          'name': 'Problem Solving & Data Structures Deep Dive',
                          'questions_count': 2,
                          'round_number': 3,
                          'sample_questions': [   {   'answer': 'Use a Trie where each node stores a min-heap or '
                                                                'sorted list of the top 5 keywords passing through '
                                                                'that node. Looking up a prefix takes O(K) to reach '
                                                                'the prefix node, and reading the precomputed top 5 '
                                                                'takes O(1).',
                                                      'question': 'Design an autocomplete search engine prefix query '
                                                                  'system that returns the top 5 most frequently '
                                                                  'searched product keywords in O(K) time where K is '
                                                                  'prefix length.'}],
                          'sections': ['Binary Search Trees', 'Tries', 'Sub-array DP'],
                          'tips': 'Write production-grade code on a shared whiteboard or editor without syntax errors '
                                  'and verify boundary inputs.',
                          'type': 'Live Coding Interview'},
                      {   'cutoff_percentage': 70,
                          'duration_minutes': 45,
                          'name': 'Hiring Manager & Bar Raiser Round',
                          'questions_count': 3,
                          'round_number': 4,
                          'sample_questions': [   {   'answer': 'Discuss how you assessed critical path impact, '
                                                                'communicated transparently with team members, and '
                                                                'delivered a high-quality MVP on time followed by '
                                                                'iterative improvements.',
                                                      'question': 'Describe a scenario where you faced conflicting '
                                                                  'deadlines across two critical software modules. How '
                                                                  'did you negotiate and deliver?'}],
                          'sections': ['Customer Centricity', 'Bias for Action', 'Engineering Ownership'],
                          'tips': 'Demonstrate resilience when dealing with failed experiments and articulate clear '
                                  'technical trade-offs.',
                          'type': 'Behavioral & System Intuition'}],
        'slug': 'flipkart'},
    {   'badge': 'PayPal Campus SDE-1',
        'description': 'Global financial technology giant powering digital payments, digital wallets, and payment '
                       'gateways for over 430 million active accounts globally.',
        'eligibility': 'B.Tech / M.Tech in CS / IT / ECE with 7.5+ CGPA and strong fundamentals in algorithms and '
                       'computer systems.',
        'hiring_season': 'August - November',
        'id': 'paypal',
        'name': 'PayPal',
        'package': 'INR 24.0 LPA - INR 32.0 LPA',
        'rounds': [   {   'cutoff_percentage': 75,
                          'duration_minutes': 90,
                          'name': 'Online Coding & Technical Assessment',
                          'questions_count': 24,
                          'round_number': 1,
                          'sample_questions': [   {   'answer': 'Durability',
                                                      'explanation': 'Durability guarantees that once a transaction '
                                                                     'has committed, its changes are written to '
                                                                     'non-volatile storage (such as write-ahead '
                                                                     'transaction logs) and will survive any '
                                                                     'subsequent system crash.',
                                                      'options': [   'Atomicity',
                                                                     'Consistency',
                                                                     'Isolation',
                                                                     'Durability'],
                                                      'question': 'Which property of database transactions guarantees '
                                                                  'that once a payment transaction commits, its '
                                                                  'updates survive system crashes and power failures?'},
                                                  {   'answer': 'Use prefix sum modulo k with a hash map storing the '
                                                                'earliest occurrence of each remainder. If (prefix_sum '
                                                                '% k) repeats at index i and j, subarray between i+1 '
                                                                'and j has sum divisible by k.',
                                                      'question': 'Given an array of integer account balances, find '
                                                                  'the longest contiguous subarray whose sum is '
                                                                  'divisible by k in O(N) time.'},
                                                  {   'answer': 'IEEE 754 binary floating point cannot accurately '
                                                                'represent base-10 fractions like 0.1, causing balance '
                                                                'drift',
                                                      'explanation': 'Binary floating-point numbers represent '
                                                                     'fractions as powers of 2. For instance, 0.1 + '
                                                                     '0.2 equals 0.30000000000000004 in IEEE 754, '
                                                                     'which accumulates into serious financial balance '
                                                                     'errors.',
                                                      'options': [   'IEEE 754 binary floating point cannot accurately '
                                                                     'represent base-10 fractions like 0.1, causing '
                                                                     'balance drift',
                                                                     'Floats cannot be stored in SQL tables',
                                                                     'Float calculations run 1000x slower on modern '
                                                                     'CPUs',
                                                                     'IEEE 754 is restricted to 3D gaming chips'],
                                                      'question': 'Why must financial payment software strictly store '
                                                                  'monetary balances as integer cents or '
                                                                  'arbitrary-precision Decimal types instead of '
                                                                  'standard IEEE 754 float?'},
                                                  {   'answer': '12',
                                                      'explanation': 'x++ evaluates to 5 (post-increment, x becomes '
                                                                     '6). ++x evaluates to 7 (pre-increment, x becomes '
                                                                     '7). 5 + 7 = 12.',
                                                      'options': ['12', '11', '10', '13'],
                                                      'question': 'What is the output?\n'
                                                                  'int x = 5;\n'
                                                                  'System.out.println(x++ + ++x);'}],
                          'sections': ['Data Structures', 'Algorithms', 'Bit Manipulation', 'Operating Systems'],
                          'tips': 'Solve algorithmic challenges with focus on memory efficiency and edge cases like '
                                  'overflow and negative integers.',
                          'type': 'HackerRank Test'},
                      {   'cutoff_percentage': 75,
                          'duration_minutes': 60,
                          'name': 'Technical Interview 1: Data Structures & System Algorithms',
                          'questions_count': 2,
                          'round_number': 2,
                          'sample_questions': [   {   'answer': 'Use Floyd Cycle Detection (slow and fast pointers '
                                                                'moving at 1x and 2x speed). When they meet, reset '
                                                                'slow to head and advance both at 1x until they meet '
                                                                'at the cycle start. Traverse to find the last node in '
                                                                'the cycle and set its next pointer to null.',
                                                      'question': 'Implement an algorithm to detect and remove a cycle '
                                                                  'in a singly linked list in O(N) time and O(1) '
                                                                  'auxiliary space.'},
                                                  {   'expected': [   'Prefix Sum + Hash Map technique',
                                                                      'running_sum - k lookup in frequency map',
                                                                      'O(N) time and O(N) space',
                                                                      'Avoids O(N^2) brute force'],
                                                      'model_answer': 'Maintain a running prefix sum and a hash map '
                                                                      'storing the frequency of prefix sums '
                                                                      'encountered so far, initialized with {0: 1}. '
                                                                      'For each num: add to running sum. If '
                                                                      '(running_sum - k) is in the map, increment '
                                                                      'count by map[running_sum - k]. Add current '
                                                                      'running_sum to map. Runs in O(N) time.',
                                                      'question': 'Given an array of integers nums and an integer k, '
                                                                  'return the total number of continuous subarrays '
                                                                  'whose sum equals to k.\n'
                                                                  'Input: nums = [1,1,1], k = 2\n'
                                                                  'Output: 2'},
                                                  {   'expected': [   'In-order traversal should produce sorted '
                                                                      'sequence',
                                                                      'Or recursive approach with min/max bounds',
                                                                      'Left subtree values < node < right subtree '
                                                                      'values',
                                                                      'Handle edge cases: duplicate values, single '
                                                                      'node'],
                                                      'model_answer': "def is_valid_bst(node, min_val=float('-inf'), "
                                                                      "max_val=float('inf')):\n"
                                                                      '    if not node: return True\n'
                                                                      '    if node.val <= min_val or node.val >= '
                                                                      'max_val: return False\n'
                                                                      '    return is_valid_bst(node.left, min_val, '
                                                                      'node.val) and is_valid_bst(node.right, '
                                                                      'node.val, max_val)',
                                                      'question': 'Implement a function to detect if a binary tree is '
                                                                  'a valid Binary Search Tree (BST).'}],
                          'sections': ['Linked Lists', 'Binary Trees', 'Two Pointers', 'Complexity Analysis'],
                          'tips': 'State time and space complexities explicitly before writing code. Handle null and '
                                  'empty inputs cleanly.',
                          'type': 'Live Coding Interview'},
                      {   'cutoff_percentage': 75,
                          'duration_minutes': 60,
                          'name': 'Technical Interview 2: Concurrency, Multithreading & Transactions',
                          'questions_count': 2,
                          'round_number': 3,
                          'sample_questions': [   {   'answer': 'Always acquire account locks in a globally '
                                                                'deterministic order (e.g., lock the account with the '
                                                                'smaller account ID first, then lock the larger ID). '
                                                                'This eliminates circular wait conditions, completely '
                                                                'preventing deadlocks. Combine with transactional '
                                                                'balance verification and idempotency keys.',
                                                      'question': 'How do you design a payment transfer endpoint '
                                                                  'between two accounts (Account A to Account B) that '
                                                                  'prevents deadlocks under high concurrent '
                                                                  'bidirectional transfers?'},
                                                  {   'expected': [   'Stream processing with Apache Flink or Kafka '
                                                                      'Streams',
                                                                      'ML model scoring in real-time pipeline',
                                                                      'Feature engineering: transaction velocity, '
                                                                      'geolocation anomaly, device fingerprint',
                                                                      'Rule engine for known fraud patterns',
                                                                      'Human review queue for borderline cases'],
                                                      'model_answer': 'Ingest transaction events via Kafka. Flink '
                                                                      'stream processor enriches with user history and '
                                                                      'computes real-time features (transaction '
                                                                      'velocity, geo-distance from last transaction). '
                                                                      'ML model (gradient boosted trees) scores fraud '
                                                                      'probability. Rules engine catches known '
                                                                      'patterns. Transactions scoring above threshold '
                                                                      'are held for review; others proceed.',
                                                      'question': 'Design a fraud detection system for PayPal that '
                                                                  'flags suspicious transactions in real-time.'}],
                          'sections': ['Thread Safety', 'Deadlocks', 'Distributed Transactions', 'Idempotency'],
                          'tips': 'Explain the difference between optimistic and pessimistic locking in financial '
                                  'transfer systems and define idempotency keys.',
                          'type': 'Core Engineering & Concurrency'},
                      {   'cutoff_percentage': 70,
                          'duration_minutes': 45,
                          'name': 'Managerial & Core Cultural Values',
                          'questions_count': 3,
                          'round_number': 4,
                          'sample_questions': [   {   'answer': 'Articulate the responsibility of building systems '
                                                                'where errors directly impact livelihoods. Discuss '
                                                                'unit testing, regression testing, automated canary '
                                                                'deployments, and observability as essential '
                                                                'engineering habits.',
                                                      'question': 'Why do you want to build fintech software at '
                                                                  'PayPal, and how do you ensure high reliability in '
                                                                  'critical software systems?'}],
                          'sections': ['Integrity', 'Collaboration', 'Innovation', 'Inclusion'],
                          'tips': 'Highlight your commitment to ethical engineering, data privacy, and attention to '
                                  'detail when dealing with sensitive user information.',
                          'type': 'Behavioral & Leadership'}],
        'slug': 'paypal'}]

class CompanyInterviewService:
    def list_companies(self) -> List[Dict[str, Any]]:
        return [
            {
                "id": c["id"],
                "name": c["name"],
                "slug": c["slug"],
                "badge": c["badge"],
                "package": c["package"],
                "hiring_season": c["hiring_season"],
                "eligibility": c["eligibility"],
                "description": c["description"],
                "rounds_count": len(c["rounds"]),
                "rounds_summary": [f"Round {r['round_number']}: {r['name']}" for r in c["rounds"]]
            }
            for c in COMPANIES_DATA
        ]

    def get_company(self, slug: str) -> Optional[Dict[str, Any]]:
        for c in COMPANIES_DATA:
            if c["slug"].lower() == slug.lower() or c["id"].lower() == slug.lower():
                return c
        return None

    def add_question(self, slug: str, round_number: int, question_data: Dict[str, Any]) -> bool:
        comp = self.get_company(slug)
        if not comp:
            return False
        for r in comp["rounds"]:
            if r["round_number"] == round_number:
                r.setdefault("sample_questions", []).append(question_data)
                return True
        return False

company_service = CompanyInterviewService()
