"""
Database Seeder for InterviewAI:
Loads 541+ Aptitude Questions & 313+ Coding Problems cleanly into the database.
"""

import json
import os
from sqlalchemy.orm import Session
from app.core.database import SessionLocal, engine, Base
from app.models.models import Subject, Topic, Question, QuestionOption, CodingProblem, utc_now

def seed_large_banks():
    Base.metadata.create_all(bind=engine)
    db: Session = SessionLocal()

    try:
        # 1. Ensure Parent Subjects exist
        subj_map = {}
        subjects_info = [
            ("Quantitative Aptitude", "quantitative-aptitude", "Calculator", "Master essential arithmetic, algebra, and numerical reasoning."),
            ("Logical Reasoning", "logical-reasoning", "Brain", "Sharpen analytical thinking, deductions, puzzles, and patterns."),
            ("Verbal Ability", "verbal-ability", "BookOpen", "Excel in English grammar, comprehension, and vocabulary."),
            ("Coding & Algorithms", "coding-algorithms", "Code2", "Hands-on data structures, algorithms, and technical placement prep.")
        ]
        for name, slug, icon, desc in subjects_info:
            s = db.query(Subject).filter((Subject.name == name) | (Subject.slug == slug)).first()
            if not s:
                s = Subject(name=name, slug=slug, icon=icon, description=desc)
                db.add(s)
                db.flush()
            subj_map[name] = s.id

        # 2. Load Generated Aptitude Bank
        apt_file = os.path.join(os.path.dirname(__file__), "generated_aptitude_bank.json")
        with open(apt_file, "r", encoding="utf-8") as f:
            aptitude_data = json.load(f)

        print(f"Loaded {len(aptitude_data)} aptitude questions from JSON.")

        # Ensure all topics exist
        topic_cache = {}
        for item in aptitude_data:
            slug = item["topic_slug"]
            if slug not in topic_cache:
                t = db.query(Topic).filter(Topic.slug == slug).first()
                if not t:
                    # Choose parent subject
                    subcat = item.get("subcategory", "quantitative")
                    subj_name = "Quantitative Aptitude"
                    if subcat == "logical":
                        subj_name = "Logical Reasoning"
                    elif subcat == "verbal":
                        subj_name = "Verbal Ability"

                    t = Topic(
                        subject_id=subj_map.get(subj_name),
                        name=item["topic_name"],
                        slug=slug,
                        category="aptitude",
                        subcategory=subcat,
                        description=f"Curated placement preparation for {item['topic_name']}.",
                        icon="Calculator" if subcat == "quantitative" else ("Brain" if subcat == "logical" else "BookOpen")
                    )
                    db.add(t)
                    db.flush()
                topic_cache[slug] = t.id

        # Insert questions
        inserted_q = 0
        for item in aptitude_data:
            topic_id = topic_cache[item["topic_slug"]]
            existing_q = db.query(Question).filter(Question.question_text == item["question_text"]).first()
            if not existing_q:
                q = Question(
                    topic_id=topic_id,
                    question_type=item["question_type"],
                    difficulty=item["difficulty"],
                    question_text=item["question_text"],
                    code_snippet=None,
                    explanation=item["explanation"],
                    step_by_step_reasoning=item["reasoning"],
                    practical_example=item["example"],
                    common_mistake=item["mistake"],
                    learning_tip=item["tip"],
                    related_concept_url=item["url"],
                    is_published=True,
                    created_at=utc_now()
                )
                db.add(q)
                db.flush()

                for key, opt_text, is_corr, why_wrong in item["options"]:
                    opt = QuestionOption(
                        question_id=q.id,
                        option_key=key,
                        option_text=opt_text,
                        is_correct=is_corr,
                        why_wrong_explanation=why_wrong
                    )
                    db.add(opt)
                inserted_q += 1

        db.commit()
        print(f"Successfully seeded {inserted_q} new aptitude questions into database.")

        # 3. Load Generated Coding Problems Bank
        coding_file = os.path.join(os.path.dirname(__file__), "generated_coding_bank.json")
        with open(coding_file, "r", encoding="utf-8") as f:
            coding_data = json.load(f)

        print(f"Loaded {len(coding_data)} coding problems from JSON.")

        # Ensure coding topic exists
        dsa_topic = db.query(Topic).filter(Topic.slug == "dsa").first()
        if not dsa_topic:
            dsa_topic = Topic(
                subject_id=subj_map.get("Coding & Algorithms"),
                name="Data Structures & Algorithms",
                slug="dsa",
                category="technical",
                subcategory="cs",
                description="Core algorithmic problems, arrays, strings, trees, and dynamic programming.",
                icon="Code2"
            )
            db.add(dsa_topic)
            db.flush()

        inserted_p = 0
        for p in coding_data:
            existing_p = db.query(CodingProblem).filter(CodingProblem.slug == p["slug"]).first()
            if not existing_p:
                prob = CodingProblem(
                    topic_id=dsa_topic.id,
                    title=p["title"],
                    slug=p["slug"],
                    difficulty=p["difficulty"],
                    category=p["category"],
                    description=p["description"],
                    input_format=p["input_format"],
                    output_format=p["output_format"],
                    constraints=p["constraints"],
                    sample_input=p["sample_input"],
                    sample_output=p["sample_output"],
                    test_cases_json=p["test_cases"],
                    starter_code_python=p["starter_code_python"],
                    starter_code_javascript=p["starter_code_javascript"],
                    starter_code_java=p["starter_code_java"],
                    starter_code_cpp=p["starter_code_cpp"],
                    solution_explanation=p["solution_explanation"],
                    time_complexity=p["time_complexity"],
                    space_complexity=p["space_complexity"],
                    hints=p["hints"],
                    external_url=p["external_url"],
                    external_platform=p["external_platform"]
                )
                db.add(prob)
                inserted_p += 1

        db.commit()
        print(f"Successfully seeded {inserted_p} new coding problems into database.")

        # Total counts check
        total_q = db.query(Question).count()
        total_p = db.query(CodingProblem).count()
        print("==================================================")
        print(f"DATABASE VERIFICATION:")
        print(f"Total Aptitude Questions in DB: {total_q}")
        print(f"Total Coding Problems in DB: {total_p}")
        print("==================================================")

    finally:
        db.close()

if __name__ == "__main__":
    seed_large_banks()
