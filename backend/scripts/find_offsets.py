with open('backend/app/services/company_interview_service.py', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if '"id":' in l:
        print(f"Line {i+1}: {l.strip()}")

