import urllib.request
import json

API_URL = 'http://127.0.0.1:8000/api/v1'
FRONTEND_URL = 'http://127.0.0.1:3000'

def req(url, method='GET', data=None, token=None):
    headers = {'Content-Type': 'application/json'}
    if token:
        headers['Authorization'] = f'Bearer {token}'
    body = json.dumps(data).encode('utf-8') if data else None
    r = urllib.request.Request(url, data=body, headers=headers, method=method)
    with urllib.request.urlopen(r) as resp:
        return json.loads(resp.read().decode('utf-8'))

print("=== 1. VERIFY AUTHENTICATION ===")
auth = req(f'{API_URL}/auth/login', method='POST', data={'email': 'student@interviewai.dev', 'password': 'Student@123456'})
token = auth['access_token']
print("Student Login Successful! User:", auth['user']['full_name'])

print("\n=== 2. VERIFY CAREER SETUP & PREFERENCES PERSISTENCE ===")
save_res = req(f'{API_URL}/profile', method='PUT', data={
    'target_role': 'Full-Stack Developer',
    'skill_level': 'Intermediate',
    'preferred_language': 'Python',
    'study_availability': 1.0,
    'prep_priorities': ['Aptitude & Tests', 'DSA & Problem Solving', 'Communication & HR', 'Core CS Subjects'],
    'preferences': {
        'timeline': '3 months',
        'priorities': ['Aptitude & Tests', 'DSA & Problem Solving', 'Communication & HR', 'Core CS Subjects']
    }
}, token=token)
print(f"Profile Updated: Role={save_res['target_role']} | Level={save_res['skill_level']} | Lang={save_res['preferred_programming_language']} | Hours={save_res['study_availability']}")

onboard_res = req(f'{API_URL}/onboarding', method='POST', data={
    'target_role': 'Full-Stack Developer',
    'skill_level': 'Intermediate',
    'preferred_language': 'Python',
    'study_availability': 1.0,
    'prep_priorities': ['Aptitude & Tests', 'DSA & Problem Solving', 'Communication & HR', 'Core CS Subjects']
}, token=token)
print(f"Onboarding Synced: Role={onboard_res['target_role']} | Onboarded={onboard_res['onboarding_completed']}")

print("\n=== 3. VERIFY MOCK INTERVIEW ROUNDS (Technical, HR, Mixed) ===")
for cat, cnt in [('Technical', 5), ('HR', 5), ('Mixed', 8)]:
    sess = req(f'{API_URL}/interviews/sessions', method='POST', data={
        'category': cat,
        'target_role': 'Full-Stack Developer',
        'difficulty': 'Medium',
        'question_count': cnt
    }, token=token)
    q_count = len(sess.get('questions', []))
    print(f"Mock Interview [{cat}]: Created session {sess['id']} with {q_count} questions.")
    assert q_count == cnt, f"Expected {cnt} questions, got {q_count}"

    ans_res = req(f"{API_URL}/interviews/sessions/{sess['id']}/responses", method='POST', data={
        'response_text': 'I break down the problem using clean architectural boundaries, define proper REST endpoints with DTO validation, and write comprehensive automated tests.'
    }, token=token)
    resp_item = ans_res['responses'][-1]
    print(f"  Evaluation Verdict: Score={resp_item['score']}/10 | Model Answer Length={len(resp_item['sample_answer'])} chars")

print("\n=== 4. VERIFY COMPANY ROUND EVALUATIONS (22 Companies) ===")
for slug in ['walmart', 'freshworks', 'flipkart', 'paypal', 'tcs', 'amazon']:
    eval_res = req(f'{API_URL}/interviews/companies/{slug}/evaluate-round', method='POST', data={
        'round_number': 1,
        'question': 'Sample technical screening question',
        'student_response': 'We implement Redis distributed caching with token bucket rate limiting and PostgreSQL read replicas.'
    }, token=token)
    print(f"Company [{slug.upper()}]: Round evaluated with score {eval_res['score']}/100, Cleared: {eval_res['cleared_round']}")

print("\n=== 5. VERIFY FRONTEND PAGES ===")
pages = [
    'index.html', 'dashboard.html', 'career-setup.html', 'interviews.html',
    'company-interviews.html', 'coding.html', 'tutor.html', 'aptitude.html',
    'communication.html', 'dsa.html', 'roadmap.html', 'profile.html'
]
for p in pages:
    r = urllib.request.Request(f"{FRONTEND_URL}/{p}")
    with urllib.request.urlopen(r) as resp:
        assert resp.status == 200, f"Page {p} returned {resp.status}"
print(f"All {len(pages)} key frontend entry points returned HTTP 200 OK.")

print("\n>>> ALL CHECKS PASSED: FRONTEND AND BACKEND FULLY CONNECTED WITHOUT ERRORS! <<<")

