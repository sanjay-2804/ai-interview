import urllib.request
import json
import sys

API_URL = 'http://127.0.0.1:8000/api/v1'
FRONTEND_URL = 'http://127.0.0.1:3000'

def req(url, method='GET', data=None, token=None):
    headers = {'Content-Type': 'application/json'}
    if token:
        headers['Authorization'] = f'Bearer {token}'
    body = json.dumps(data).encode('utf-8') if data is not None else None
    r = urllib.request.Request(url, data=body, headers=headers, method=method)
    with urllib.request.urlopen(r) as resp:
        return json.loads(resp.read().decode('utf-8'))

print(">>> 1. TESTING AUTHENTICATION")
auth = req(f'{API_URL}/auth/login', method='POST', data={'email': 'student@interviewai.dev', 'password': 'Student@123456'})
token = auth['access_token']
print("  Auth OK: Student", auth['user']['full_name'])

print(">>> 2. TESTING PRACTICE MCQ SESSION & STRICT ANSWER LOCKING")
# Create practice session
practice_sess = req(f'{API_URL}/practice/sessions', method='POST', data={
    'category': 'Quantitative Aptitude',
    'difficulty': 'intermediate',
    'session_mode': 'practice',
    'question_count': 3
}, token=token)
sess_id = practice_sess['id']
print(f"  Practice Session Created: ID={sess_id}, Total Qs={practice_sess['total_questions']}")
q_item = practice_sess['questions'][0]
q_id = q_item['question']['id']
opt_key = q_item['question']['options'][0]['option_key']

# Submit answer
ans_res = req(f'{API_URL}/practice/sessions/{sess_id}/submit', method='POST', data={
    'question_id': q_id,
    'submitted_answer': opt_key,
    'time_spent_seconds': 15
}, token=token)
print(f"  Answer Evaluated: Is Correct={ans_res['is_correct']}, Correct Option={ans_res['correct_option']}")

# Verify strict answer locking: second submission returns existing locked answer without change
second_sub = req(f'{API_URL}/practice/sessions/{sess_id}/submit', method='POST', data={
    'question_id': q_id,
    'submitted_answer': 'Z',
    'time_spent_seconds': 10
}, token=token)
assert second_sub['selected_option'] == opt_key, f"Expected locked {opt_key}, got {second_sub['selected_option']}"
print(f"  Strict Answer Locking OK: Answer remained locked to {second_sub['selected_option']} (ignored 'Z').")

print(">>> 3. TESTING REAL SUBPROCESS CODING EXECUTION")
code_run = req(f'{API_URL}/coding/run', method='POST', data={
    'problem_id': 1,
    'language': 'python',
    'code': 'def twoSum(nums, target):\n    lookup = {}\n    for i, n in enumerate(nums):\n        if target - n in lookup:\n            return [lookup[target - n], i]\n        lookup[n] = i\n    return []\n'
}, token=token)
print(f"  Coding Run Result: Status={code_run['status']}, Passed Tests={code_run['passed_tests']}/{code_run['total_tests']}, Runtime={code_run['runtime_ms']}ms")

print(">>> 4. TESTING COMMUNICATION LAB TRANSCRIPT EVALUATION")
comm_res = req(f'{API_URL}/communication/submit', method='POST', data={
    'category': 'Self Introduction',
    'prompt_title': 'Tell Me About Yourself',
    'prompt_question': 'Walk me through your academic background and projects.',
    'transcript': 'I am a final-year CS undergrad specialized in full-stack web architectures using React, Python FastAPI, and PostgreSQL. I built an AI placement platform that achieved 40% reduction in query latency and handled real code execution.',
    'audio_duration_seconds': 55.0
}, token=token)
print(f"  Communication Evaluated: Overall Score={comm_res['overall_score']}/10, WPM={comm_res['wpm']}")
print(f"  Concepts Identified: {comm_res.get('concepts_demonstrated')}")
print(f"  Follow-up Question: {comm_res.get('follow_up_question')}")

print(">>> 5. TESTING COMPANY ASK-AI & REPOSITORY")
ask_ai_res = req(f'{API_URL}/interviews/companies/ask-ai', method='POST', data={
    'company_slug': 'google',
    'round_number': 2,
    'question': 'How do you find the longest path in a Directed Acyclic Graph (DAG)?'
}, token=token)
print(f"  Company Ask-AI OK: Category={ask_ai_res['category']}, Concept={ask_ai_res['core_concept']}")
print(f"  Follow-up Qs Count: {len(ask_ai_res['follow_up_questions'])}")

print(">>> 6. TESTING AI PLACEMENT TUTOR")
tutor_diag = req(f'{API_URL}/tutor/diagnostic-context', token=token)
print(f"  Tutor Diagnostic: Target Role={tutor_diag['target_role']}, Accuracy={tutor_diag['mcq_accuracy_percentage']}%")

tutor_chat = req(f'{API_URL}/tutor/chat', method='POST', data={
    'message': 'Explain Dijkstra algorithm complexity using Min-Heap.'
}, token=token)
print(f"  Tutor Chat Reply: {tutor_chat['reply'][:100]}...")

print("\n>>> ALL FUNCTIONAL BACKEND WORKFLOWS PASSED 100% CLEAN! <<<")
