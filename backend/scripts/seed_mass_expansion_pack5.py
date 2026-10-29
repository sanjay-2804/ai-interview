"""
InterviewAI — Massive Question Expansion Pack 5
Brings all remaining sparse topics to a minimum of 12-15+ questions each.
"""

import sqlite3
import os
from datetime import datetime, timezone

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "interviewai.db")

QUESTIONS_DATA = [
    # -----------------------------------------------------------------
    # Topic 22: Problems on Ages (10 Questions)
    # -----------------------------------------------------------------
    {
        "topic_id": 22,
        "difficulty": "easy",
        "question_text": "A mother is 4 times as old as her daughter. In 20 years, she will be twice as old as her daughter. What is the current age of the daughter?",
        "explanation": "Let daughter's age be $x$. Mother's age is $4x$. In 20 years: $4x + 20 = 2(x + 20) \\Rightarrow 4x + 20 = 2x + 40 \\Rightarrow 2x = 20 \\Rightarrow x = 10$. Daughter is 10 years old.",
        "options": [
            ("A", "10 years", True, "Correct: 4(10)+20 = 60, and 2(10+20) = 60."),
            ("B", "12 years", False, "Incorrect: Would not satisfy the 20-year condition."),
            ("C", "15 years", False, "Incorrect: Daughter would be 35 and mother 80 (not double)."),
            ("D", "8 years", False, "Incorrect: Calculations do not match.")
        ]
    },
    {
        "topic_id": 22,
        "difficulty": "medium",
        "question_text": "The sum of the ages of 5 children born at intervals of 3 years each is 50 years. What is the age of the youngest child?",
        "explanation": "Let ages be $x, x+3, x+6, x+9, x+12$. Sum $= 5x + 30 = 50 \\Rightarrow 5x = 20 \\Rightarrow x = 4$ years.",
        "options": [
            ("A", "4 years", True, "Correct: 4 + 7 + 10 + 13 + 16 = 50."),
            ("B", "2 years", False, "Incorrect: Sum would be 2 + 5 + 8 + 11 + 14 = 40."),
            ("C", "3 years", False, "Incorrect: Sum would be 45."),
            ("D", "5 years", False, "Incorrect: Sum would be 55.")
        ]
    },
    {
        "topic_id": 22,
        "difficulty": "medium",
        "question_text": "A person was asked to state his age. His reply was: 'Take my age three years hence, multiply it by 3, and then subtract three times my age three years ago, and you will know how old I am.' What is his age?",
        "explanation": "Let his age be $x$. Equation: $3(x + 3) - 3(x - 3) = x \\Rightarrow (3x + 9) - (3x - 9) = x \\Rightarrow 18 = x$. His age is 18 years.",
        "options": [
            ("A", "18 years", True, "Correct: 3(21) - 3(15) = 63 - 45 = 18."),
            ("B", "24 years", False, "Incorrect: Algebraic evaluation yields 18."),
            ("C", "20 years", False, "Incorrect: Does not satisfy equation."),
            ("D", "15 years", False, "Incorrect: Misinterprets the constant difference.")
        ]
    },
    {
        "topic_id": 22,
        "difficulty": "hard",
        "question_text": "Six years ago, the ratio of the ages of Kunal and Sagar was 6 : 5. Four years hence, the ratio of their ages will be 11 : 10. What is Sagar's present age?",
        "explanation": "Let ages 6 yrs ago be $6x$ and $5x$. Present ages are $6x + 6$ and $5x + 6$. Four years hence: $(6x + 10)/(5x + 10) = 11/10 \\Rightarrow 10(6x + 10) = 11(5x + 10) \\Rightarrow 60x + 100 = 55x + 110 \\Rightarrow 5x = 10 \\Rightarrow x = 2$. Sagar's present age $= 5(2) + 6 = 16$ years.",
        "options": [
            ("A", "16 years", True, "Correct: 5(2) + 6 = 16 years."),
            ("B", "18 years", False, "Incorrect: Kunal's present age is 18, not Sagar's."),
            ("C", "20 years", False, "Incorrect: Four years hence Sagar will be 20, present is 16."),
            ("D", "14 years", False, "Incorrect: Arithmetic error in cross-multiplication.")
        ]
    },

    # -----------------------------------------------------------------
    # Topic 24: Geometry & Mensuration (More Questions)
    # -----------------------------------------------------------------
    {
        "topic_id": 24,
        "difficulty": "medium",
        "question_text": "The length of a rectangle is increased by 20% and its breadth is decreased by 10%. What is the net percentage change in its area?",
        "explanation": "Formula: Net change $= a + b + \\frac{ab}{100} = 20 - 10 + \\frac{20 \\times (-10)}{100} = 10 - 2 = +8\\%$. The area increases by 8%.",
        "options": [
            ("A", "Increases by 8%", True, "Correct: 1.20 * 0.90 = 1.08, which is an 8% increase."),
            ("B", "Increases by 10%", False, "Incorrect: Ignores cross product term."),
            ("C", "Decreases by 2%", False, "Incorrect: Net change is positive."),
            ("D", "Remains unchanged", False, "Incorrect: Proportions differ, causing net change.")
        ]
    },
    {
        "topic_id": 24,
        "difficulty": "medium",
        "question_text": "What is the total surface area of a solid right circular cylinder of radius 7 cm and height 10 cm? (Use $\\pi = 22/7$)",
        "explanation": "Formula: $\\text{TSA} = 2\\pi r(h + r) = 2 \\times \\frac{22}{7} \\times 7 \\times (10 + 7) = 44 \\times 17 = 748\\text{ cm}^2$.",
        "options": [
            ("A", "$748\\text{ cm}^2$", True, "Correct: 2 * (22/7) * 7 * (10 + 7) = 44 * 17 = 748."),
            ("B", "$440\\text{ cm}^2$", False, "Incorrect: 440 is the Curved Surface Area (CSA), not Total Surface Area."),
            ("C", "$616\\text{ cm}^2$", False, "Incorrect: Area of two circles only."),
            ("D", "$880\\text{ cm}^2$", False, "Incorrect: Multiplication mistake.")
        ]
    },
    {
        "topic_id": 24,
        "difficulty": "hard",
        "question_text": "Two concentric circles have radii of 13 cm and 5 cm. What is the length of the chord of the larger circle that touches the smaller circle?",
        "explanation": "The radius to the point of tangency is perpendicular to the chord, bisecting it. By Pythagoras theorem in the right triangle: $(\\text{half-chord})^2 + 5^2 = 13^2 \\Rightarrow (\\text{half-chord})^2 = 169 - 25 = 144 \\Rightarrow \\text{half-chord} = 12$ cm. Full chord $= 2 \\times 12 = 24$ cm.",
        "options": [
            ("A", "24 cm", True, "Correct: 2 * sqrt(13^2 - 5^2) = 2 * 12 = 24 cm."),
            ("B", "12 cm", False, "Incorrect: 12 cm is half of the chord."),
            ("C", "18 cm", False, "Incorrect: Arithmetic error."),
            ("D", "26 cm", False, "Incorrect: Diameter of larger circle.")
        ]
    },

    # -----------------------------------------------------------------
    # Topic 25: Progressions (AP & GP) (More Questions)
    # -----------------------------------------------------------------
    {
        "topic_id": 25,
        "difficulty": "medium",
        "question_text": "If the 3rd and 7th terms of an Arithmetic Progression (AP) are 18 and 30 respectively, what is the 15th term?",
        "explanation": "$a_3 = a + 2d = 18$ and $a_7 = a + 6d = 30$. Subtracting: $4d = 12 \\Rightarrow d = 3$. Then $a + 2(3) = 18 \\Rightarrow a = 12$. The 15th term $a_{15} = a + 14d = 12 + 14(3) = 12 + 42 = 54$.",
        "options": [
            ("A", "54", True, "Correct: a = 12, d = 3; a_15 = 12 + 14*3 = 54."),
            ("B", "48", False, "Incorrect: This is the 13th term."),
            ("C", "60", False, "Incorrect: This is the 17th term."),
            ("D", "51", False, "Incorrect: Used 13d instead of 14d.")
        ]
    },
    {
        "topic_id": 25,
        "difficulty": "hard",
        "question_text": "Find the sum of the infinite Geometric Progression (GP): $1 + \\frac{1}{3} + \\frac{1}{9} + \\frac{1}{27} + \\dots$",
        "explanation": "Formula for sum of infinite GP where $|r| < 1$: $S_\\infty = \\frac{a}{1 - r}$. Here $a = 1$ and $r = 1/3$. $S_\\infty = \\frac{1}{1 - 1/3} = \\frac{1}{2/3} = \\frac{3}{2} = 1.5$.",
        "options": [
            ("A", "$1.5$ (or $3/2$)", True, "Correct: a / (1 - r) = 1 / (2/3) = 1.5."),
            ("B", "$2.0$", False, "Incorrect: Result for r = 1/2."),
            ("C", "$1.33$", False, "Incorrect: First two terms only."),
            ("D", "$\\infty$", False, "Incorrect: Since |r| < 1, the series converges.")
        ]
    },

    # -----------------------------------------------------------------
    # Topic 26: Algebra & Equations (More Questions)
    # -----------------------------------------------------------------
    {
        "topic_id": 26,
        "difficulty": "medium",
        "question_text": "Find the roots of the quadratic equation $2x^2 - 7x + 3 = 0$.",
        "explanation": "Factoring: $2x^2 - 6x - x + 3 = 0 \\Rightarrow 2x(x - 3) - 1(x - 3) = 0 \\Rightarrow (2x - 1)(x - 3) = 0$. Roots are $x = 1/2$ and $x = 3$.",
        "options": [
            ("A", "$x = 3$ and $x = 0.5$", True, "Correct: (2x - 1)(x - 3) = 0."),
            ("B", "$x = -3$ and $x = -0.5$", False, "Incorrect: Sign reversal error."),
            ("C", "$x = 2$ and $x = 1.5$", False, "Incorrect: Factoring error."),
            ("D", "$x = 6$ and $x = 1$", False, "Incorrect: Failed quadratic formula.")
        ]
    },
    {
        "topic_id": 26,
        "difficulty": "hard",
        "question_text": "If $\\alpha$ and $\\beta$ are the roots of the equation $x^2 - 5x + 6 = 0$, what is the value of $\\alpha^2 + \\beta^2$?",
        "explanation": "Sum of roots $\\alpha + \\beta = 5$. Product of roots $\\alpha\\beta = 6$. $\\alpha^2 + \\beta^2 = (\\alpha + \\beta)^2 - 2\\alpha\\beta = 5^2 - 2(6) = 25 - 12 = 13$.",
        "options": [
            ("A", "13", True, "Correct: (5)^2 - 2(6) = 25 - 12 = 13."),
            ("B", "25", False, "Incorrect: Forgetting to subtract 2*alpha*beta."),
            ("C", "19", False, "Incorrect: Subtracting alpha*beta once instead of twice."),
            ("D", "12", False, "Incorrect: Calculation error.")
        ]
    },

    # -----------------------------------------------------------------
    # Topic 61: Reading Comprehension & Para Jumbles (More Questions)
    # -----------------------------------------------------------------
    {
        "topic_id": 61,
        "difficulty": "medium",
        "question_text": "Passage: 'Artificial intelligence models require vast amounts of compute and electricity to train and serve at scale. As data centers expand to support AI workloads, tech companies face mounting challenges to meet their net-zero carbon pledges without jeopardizing computational performance.'\n\nWhat is the primary dilemma highlighted in the passage?",
        "explanation": "The text directly states the tension between the soaring energy requirements of AI data centers and tech companies' environmental carbon-neutral pledges.",
        "options": [
            ("A", "Balancing high AI computational demands against corporate commitments to carbon neutrality.", True, "Correct: Expresses the core conflict of energy vs environmental goals."),
            ("B", "The inability of hardware manufacturers to produce GPUs fast enough.", False, "Incorrect: Hardware manufacturing shortages are not mentioned."),
            ("C", "The risk of artificial intelligence replacing software engineers.", False, "Incorrect: Job displacement is not discussed in the passage."),
            ("D", "The rising subscription prices of consumer cloud software.", False, "Incorrect: Pricing is not mentioned.")
        ]
    },
    {
        "topic_id": 61,
        "difficulty": "medium",
        "question_text": "Reorder the sentences into a coherent paragraph:\n1. This decentralized ledger ensures transparency without relying on a central authority.\n2. Blockchain technology was originally devised to power peer-to-peer digital currency.\n3. Every participant in the network maintains an identical cryptographically secured copy.\n4. Today, its applications extend far beyond cryptocurrency to supply chain tracking and healthcare.",
        "explanation": "Sentence 2 introduces the subject and its origin. Sentence 1 describes how it works (decentralized ledger). Sentence 3 elaborates on the mechanism (participants maintaining identical copies). Sentence 4 summarizes modern applications ('Today, its applications extend...'). The logical flow is 2 -> 1 -> 3 -> 4.",
        "options": [
            ("A", "2 - 1 - 3 - 4", True, "Correct: Origin -> Definition -> Mechanism -> Modern Applications."),
            ("B", "1 - 2 - 4 - 3", False, "Incorrect: Cannot start with 'This decentralized ledger' without defining it first."),
            ("C", "4 - 3 - 2 - 1", False, "Incorrect: Chronology is inverted."),
            ("D", "2 - 4 - 1 - 3", False, "Incorrect: Jumps to modern applications before explaining the ledger.")
        ]
    },

    # -----------------------------------------------------------------
    # Topic 57: JavaScript & TypeScript (More Questions)
    # -----------------------------------------------------------------
    {
        "topic_id": 57,
        "difficulty": "medium",
        "question_text": "What is the output of the following JavaScript snippet?\n```javascript\nconsole.log(typeof NaN);\nconsole.log(NaN === NaN);\n```",
        "explanation": "In JavaScript, `NaN` (Not-a-Number) is of type `'number'`. According to IEEE 754 floating point standard and JS spec, `NaN` is not equal to any value, including itself (`NaN === NaN` is `false`).",
        "options": [
            ("A", "'number' and false", True, "Correct: typeof NaN is 'number', and NaN is never equal to itself."),
            ("B", "'undefined' and true", False, "Incorrect: NaN is of type number and comparisons yield false."),
            ("C", "'object' and false", False, "Incorrect: NaN is not an object."),
            ("D", "'nan' and true", False, "Incorrect: 'nan' is not a valid JS primitive type.")
        ]
    },
    {
        "topic_id": 57,
        "difficulty": "hard",
        "question_text": "In TypeScript, what does the `unknown` type represent compared to `any`?",
        "explanation": "`any` turns off all type checking, allowing arbitrary property accesses and method calls. `unknown` is the type-safe counterpart of `any`: anything can be assigned to `unknown`, but no operations or method calls are permitted without explicit type narrowing or type assertions.",
        "options": [
            ("A", "`unknown` accepts any value but forbids operations until type narrowing or assertion is performed, unlike `any`.", True, "Correct: unknown enforces compile-time type safety."),
            ("B", "`unknown` can only hold string values, while `any` holds numbers.", False, "Incorrect: Both hold any type, but unknown is type-safe."),
            ("C", "`unknown` is converted to `void` during runtime.", False, "Incorrect: TypeScript types are stripped at runtime."),
            ("D", "`any` is faster at runtime than `unknown`.", False, "Incorrect: Neither type has any runtime overhead.")
        ]
    },

    # -----------------------------------------------------------------
    # Topic 58: Software Engineering & Testing (More Questions)
    # -----------------------------------------------------------------
    {
        "topic_id": 58,
        "difficulty": "medium",
        "question_text": "In Git version control, what does `git cherry-pick <commit-hash>` do?",
        "explanation": "`git cherry-pick` applies the changes introduced by an existing commit from another branch onto the current branch by creating a brand new commit with the same diff.",
        "options": [
            ("A", "Applies the changes from a specific commit on another branch onto the current HEAD.", True, "Correct: Selectively ports a commit diff without merging the whole branch."),
            ("B", "Permanently deletes the specified commit from remote repository history.", False, "Incorrect: That would be an interactive rebase or reset."),
            ("C", "Creates a zip archive of the specified commit.", False, "Incorrect: That is `git archive`."),
            ("D", "Reverts all changes in the current branch back to the initial commit.", False, "Incorrect: That is `git reset --hard`.")
        ]
    },
    {
        "topic_id": 58,
        "difficulty": "medium",
        "question_text": "In Agile Scrum, what is the primary purpose of the Sprint Retrospective meeting?",
        "explanation": "The Sprint Retrospective occurs at the end of every sprint for the team to inspect how the last sprint went with regards to people, relationships, process, and tools, and identify actionable improvements for the next sprint.",
        "options": [
            ("A", "To reflect on the team's process, tools, and collaboration to identify continuous improvements for future sprints.", True, "Correct: Focuses on process improvement, not product demonstrations."),
            ("B", "To demo completed software features to external stakeholders and clients.", False, "Incorrect: That is the Sprint Review / Demo meeting."),
            ("C", "To conduct annual employee performance evaluations.", False, "Incorrect: Retrospectives are blameless process reviews."),
            ("D", "To estimate user story story points for the entire upcoming year.", False, "Incorrect: That is release planning or backlog grooming.")
        ]
    }
]

def seed_expansion_pack5():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    now_iso = datetime.now(timezone.utc).isoformat()

    added_q = 0
    added_opt = 0

    for item in QUESTIONS_DATA:
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
            "Apply standard placement calculation and engineering principles.",
            "Campus placement benchmark assessment.",
            "Careless calculations or misinterpreting constraints.",
            "Write out equations clearly and double check units.",
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

    print(f"Pack 5: Successfully added {added_q} questions and {added_opt} options.")

if __name__ == "__main__":
    seed_expansion_pack5()

