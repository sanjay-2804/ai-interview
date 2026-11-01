import asyncio
import sys
import os

# Ensure backend and root are in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from api.index import app
from httpx import AsyncClient, ASGITransport

async def run_vercel_readiness_tests():
    print("==================================================")
    print("INTERVIEWAI VERCEL DEPLOYMENT READINESS VERIFICATION")
    print("==================================================")
    
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="https://interviewai.vercel.app") as client:
        # 1. Health check
        print("\n[1/8] Testing API Health Check (/health & /api/v1/health)...")
        res = await client.get("/health")
        assert res.status_code == 200, f"Expected 200, got {res.status_code}: {res.text}"
        data = res.json()
        print(f"  -> Health OK: {data}")

        res_v1 = await client.get("/api/v1/health")
        assert res_v1.status_code == 200, f"Expected 200, got {res_v1.status_code}"
        print(f"  -> /api/v1/health OK: {res_v1.json().get('status')}")

        # 2. Seed student login
        print("\n[2/8] Testing Existing Seed Account Login (/api/v1/auth/login)...")
        login_res = await client.post("/api/v1/auth/login", json={
            "email": "student@interviewai.dev",
            "password": "Student@123456"
        })
        assert login_res.status_code == 200, f"Login failed: {login_res.status_code} {login_res.text}"
        token = login_res.json().get("access_token")
        assert token, "Token missing in login response"
        print("  -> Seed Login successful! Bearer token acquired.")

        auth_headers = {"Authorization": f"Bearer {token}"}

        # 3. New User Registration
        print("\n[3/8] Testing Dynamic User Registration (/api/v1/auth/register)...")
        import uuid
        test_email = f"candidate_{uuid.uuid4().hex[:6]}@example.com"
        reg_res = await client.post("/api/v1/auth/register", json={
            "email": test_email,
            "password": "Password@123",
            "full_name": "Test Candidate"
        })
        assert reg_res.status_code in [200, 201], f"Registration failed: {reg_res.status_code} {reg_res.text}"
        print(f"  -> Registration OK for {test_email}")

        # 4. Profile / Dashboard data retrieval
        print("\n[4/8] Testing Authenticated Profile (/api/v1/auth/me & /api/v1/profile)...")
        me_res = await client.get("/api/v1/auth/me", headers=auth_headers)
        assert me_res.status_code == 200, f"Get /auth/me failed: {me_res.status_code}"
        user_info = me_res.json()
        print(f"  -> User: {user_info.get('full_name')} ({user_info.get('email')}), Role: {user_info.get('role')}")

        prof_res = await client.get("/api/v1/profile", headers=auth_headers)
        assert prof_res.status_code == 200, f"Get /profile failed: {prof_res.status_code}"
        prof_info = prof_res.json()
        print(f"  -> Target Role: {prof_info.get('target_role')}, Level: {prof_info.get('skill_level')}")

        # 5. Practice Question Retrieval
        print("\n[5/8] Testing Question Retrieval (/api/v1/practice/questions)...")
        q_res = await client.get("/api/v1/practice/questions?limit=5", headers=auth_headers)
        assert q_res.status_code == 200, f"Get questions failed: {q_res.status_code}"
        questions = q_res.json()
        print(f"  -> Successfully retrieved {len(questions)} practice questions.")

        # 6. HR & Mock Interview Question Retrieval
        print("\n[6/8] Testing Interview Question Bank (/api/v1/interviews/hr-questions)...")
        hr_res = await client.get("/api/v1/interviews/hr-questions", headers=auth_headers)
        assert hr_res.status_code == 200, f"Get HR questions failed: {hr_res.status_code}"
        hr_questions = hr_res.json()
        print(f"  -> Successfully retrieved {len(hr_questions)} interview questions.")

        # 7. Mock Interview Session Creation & AI Evaluation
        print("\n[7/8] Testing Mock Interview Session & AI Evaluation...")
        start_session_res = await client.post("/api/v1/interviews/sessions", json={
            "category": "technical",
            "target_role": "Software Developer",
            "difficulty": "medium",
            "question_count": 3
        }, headers=auth_headers)
        assert start_session_res.status_code == 200, f"Start interview session failed: {start_session_res.status_code} {start_session_res.text}"
        session_data = start_session_res.json()
        session_id = session_data.get("id")
        current_q = session_data.get("current_question_text", "Explain object-oriented programming")
        print(f"  -> Started interview session #{session_id} with {session_data.get('total_questions')} questions.")
        print(f"  -> Question #1: {current_q[:60]}...")

        submit_res = await client.post(f"/api/v1/interviews/sessions/{session_id}/responses", json={
            "response_text": "In a software architecture, I prioritize separation of concerns, writing clean modular functions, handling exceptions gracefully, and verifying behavior with automated unit tests."
        }, headers=auth_headers)
        assert submit_res.status_code == 200, f"Submit answer failed: {submit_res.status_code} {submit_res.text}"
        updated_session = submit_res.json()
        responses = updated_session.get("responses", [])
        assert len(responses) > 0, "No responses returned after evaluation"
        latest_eval = responses[-1]
        print(f"  -> Answer evaluated! Score: {latest_eval.get('score')}/10")
        print(f"  -> Evaluated by: {latest_eval.get('ai_engine')}")
        print(f"  -> Strengths: {latest_eval.get('strengths')}")

        # 8. Static file serving compatibility
        print("\n[8/8] Testing Static Frontend Serving Fallback...")
        page_res = await client.get("/login.html")
        assert page_res.status_code == 200, f"Frontend static load failed: {page_res.status_code}"
        assert "<!DOCTYPE html>" in page_res.text, "HTML doctype not found in login.html"
        print("  -> Static HTML frontend successfully served!")

    print("\n==================================================")
    print("ALL 8 VERCEL READINESS CHECKS PASSED WITH 100% SUCCESS!")
    print("==================================================")

if __name__ == "__main__":
    asyncio.run(run_vercel_readiness_tests())
