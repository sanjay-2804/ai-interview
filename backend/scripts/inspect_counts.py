import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from app.services.company_interview_service import COMPANIES_DATA

print("--- COMPANY INTERVIEW QUESTIONS BREAKDOWN ---")
total_rounds = 0
total_qs = 0
for c in COMPANIES_DATA:
    q_count = sum(len(r.get('sample_questions', [])) for r in c.get('rounds', []))
    rounds_count = len(c.get('rounds', []))
    total_rounds += rounds_count
    total_qs += q_count
    print(f"{c['name']} ({c['slug']}): {rounds_count} rounds, {q_count} questions")

print("---------------------------------------------")
print(f"Total Companies: {len(COMPANIES_DATA)}")
print(f"Total Rounds: {total_rounds}")
print(f"Total Company Questions: {total_qs}")

