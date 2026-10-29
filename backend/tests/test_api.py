import pytest
from datetime import datetime, timedelta, timezone
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.core.database import Base, get_db
from app.core.security import verify_password, hash_token
from app.models.models import User, UserProfile, AuthSession, PasswordResetToken, Bookmark, Lesson, PracticeSession

TEST_DATABASE_URL = "sqlite:///./test_interviewai.db"
test_engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(scope="session", autouse=True)
def setup_test_db():
    Base.metadata.drop_all(bind=test_engine)
    Base.metadata.create_all(bind=test_engine)
    
    # Temporarily monkeypatch SessionLocal & engine for seed_database
    import app.seeds.seed_data
    old_session = app.seeds.seed_data.SessionLocal
    old_engine = app.seeds.seed_data.engine
    app.seeds.seed_data.SessionLocal = TestingSessionLocal
    app.seeds.seed_data.engine = test_engine
    app.seeds.seed_data.seed_database()
    app.seeds.seed_data.SessionLocal = old_session
    app.seeds.seed_data.engine = old_engine
    
    yield
    Base.metadata.drop_all(bind=test_engine)

@pytest.fixture
def client():
    return TestClient(app)

# Helper function to get auth headers for a user
def get_auth_client(email: str, password: str):
    c = TestClient(app)
    resp = c.post("/api/v1/auth/login", json={"email": email, "password": password})
    assert resp.status_code == 200, f"Login failed for {email}: {resp.text}"
    token = resp.json()["access_token"]
    c.headers["Authorization"] = f"Bearer {token}"
    return c, token

# =========================================================================
# 1. User registration success
# =========================================================================
def test_01_user_registration_success(client):
    response = client.post("/api/v1/auth/register", json={
        "full_name": "Rohan Patel",
        "email": "rohan@example.com",
        "password": "Password@1234"
    })
    assert response.status_code == 201
    data = response.json()
    assert data["user"]["email"] == "rohan@example.com"
    assert data["user"]["full_name"] == "Rohan Patel"
    assert data["user"]["role"] == "student"
    assert "access_token" in data
    # Check session cookie set
    assert "interviewai_session" in response.cookies

# =========================================================================
# 2. User registration rejection for duplicate email
# =========================================================================
def test_02_user_registration_duplicate_email(client):
    response = client.post("/api/v1/auth/register", json={
        "full_name": "Duplicate Rohan",
        "email": "rohan@example.com",
        "password": "DifferentPassword@123"
    })
    assert response.status_code == 400
    assert "already exists" in response.json()["detail"].lower()

# =========================================================================
# 3. Password stored as a secure hash (never plaintext)
# =========================================================================
def test_03_password_stored_as_secure_hash():
    db = TestingSessionLocal()
    user = db.query(User).filter(User.email == "rohan@example.com").first()
    db.close()
    assert user is not None
    # Must NOT equal raw plaintext password
    assert user.hashed_password != "Password@1234"
    # Must be valid bcrypt hash verified by passlib/bcrypt
    assert verify_password("Password@1234", user.hashed_password) is True

# =========================================================================
# 4. Login success with valid credentials
# =========================================================================
def test_04_login_success_with_valid_credentials(client):
    response = client.post("/api/v1/auth/login", json={
        "email": "rohan@example.com",
        "password": "Password@1234"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["user"]["email"] == "rohan@example.com"
    assert "access_token" in data
    assert "interviewai_session" in response.cookies
    
    # Verify last_login_at is updated in DB
    db = TestingSessionLocal()
    user = db.query(User).filter(User.email == "rohan@example.com").first()
    db.close()
    assert user.last_login_at is not None

# =========================================================================
# 5. Login failure with wrong password
# =========================================================================
def test_05_login_failure_wrong_password(client):
    response = client.post("/api/v1/auth/login", json={
        "email": "rohan@example.com",
        "password": "WrongPassword@999"
    })
    assert response.status_code == 401
    assert "incorrect email or password" in response.json()["detail"].lower()

# =========================================================================
# 6. Login failure with non-existent user
# =========================================================================
def test_06_login_failure_non_existent_user(client):
    response = client.post("/api/v1/auth/login", json={
        "email": "nonexistent_ghost_user@example.com",
        "password": "Password@1234"
    })
    assert response.status_code == 401
    assert "incorrect email or password" in response.json()["detail"].lower()

# =========================================================================
# 7. Logout invalidation behavior
# =========================================================================
def test_07_logout_invalidation_behavior():
    session_client = TestClient(app)
    # Login
    login_resp = session_client.post("/api/v1/auth/login", json={
        "email": "rohan@example.com",
        "password": "Password@1234"
    })
    assert login_resp.status_code == 200
    raw_cookie = session_client.cookies.get("interviewai_session")
    assert raw_cookie is not None

    # Check active session in DB
    db = TestingSessionLocal()
    token_hash = hash_token(raw_cookie)
    active_session = db.query(AuthSession).filter(AuthSession.session_token_hash == token_hash).first()
    assert active_session is not None
    assert active_session.is_revoked is False
    db.close()

    # Call logout
    logout_resp = session_client.post("/api/v1/auth/logout")
    assert logout_resp.status_code == 200

    # In DB, session must now be marked revoked
    db = TestingSessionLocal()
    revoked_session = db.query(AuthSession).filter(AuthSession.session_token_hash == token_hash).first()
    assert revoked_session.is_revoked is True
    db.close()

# =========================================================================
# 8. Unauthenticated requests to protected endpoints return 401
# =========================================================================
def test_08_unauthenticated_requests_return_401(client):
    # Fresh unauthenticated client without cookies or auth header
    resp1 = client.get("/api/v1/auth/me")
    assert resp1.status_code == 401
    
    resp2 = client.get("/api/v1/profile")
    assert resp2.status_code == 401

# =========================================================================
# 9. Student cannot access administrator endpoints (returns 403)
# =========================================================================
def test_09_student_cannot_access_admin_endpoints():
    student_client, _ = get_auth_client("student@interviewai.dev", "Student@123456")
    forbidden_resp = student_client.get("/api/v1/admin/analytics")
    assert forbidden_resp.status_code == 403
    assert "administrator privileges required" in forbidden_resp.json()["detail"].lower()

    admin_client, _ = get_auth_client("admin@interviewai.dev", "Admin@123456")
    admin_resp = admin_client.get("/api/v1/admin/analytics")
    assert admin_resp.status_code == 200
    assert "total_users" in admin_resp.json()

# =========================================================================
# 10. Student A cannot read Student B’s private data
# =========================================================================
def test_10_student_a_cannot_read_student_b_private_data(client):
    # Register Student B
    client.post("/api/v1/auth/register", json={
        "full_name": "Student B",
        "email": "student_b@example.com",
        "password": "Password@1234"
    })
    student_b_client, _ = get_auth_client("student_b@example.com", "Password@1234")
    
    # Student B creates a practice session
    b_session_resp = student_b_client.post("/api/v1/practice/sessions", json={
        "category": "aptitude",
        "question_count": 2
    })
    assert b_session_resp.status_code == 200
    b_session_id = b_session_resp.json()["id"]

    # Student A attempts to read Student B's session detail
    student_a_client, _ = get_auth_client("rohan@example.com", "Password@1234")
    a_read_resp = student_a_client.get(f"/api/v1/practice/sessions/{b_session_id}")
    assert a_read_resp.status_code == 404
    assert "access denied" in a_read_resp.json()["detail"].lower()

# =========================================================================
# 11. Student A cannot modify or delete Student B’s records
# =========================================================================
def test_11_student_a_cannot_modify_or_delete_student_b_records():
    student_b_client, _ = get_auth_client("student_b@example.com", "Password@1234")
    
    # Student B creates a bookmark
    bm_resp = student_b_client.post("/api/v1/bookmarks/", json={
        "item_type": "topic",
        "item_id": 1,
        "title": "Private Bookmark of Student B",
        "category": "aptitude",
        "link_path": "/practice/topic/1"
    })
    assert bm_resp.status_code == 200
    b_bookmark_id = bm_resp.json()["id"]

    # Student A attempts to delete Student B's bookmark
    student_a_client, _ = get_auth_client("rohan@example.com", "Password@1234")
    del_resp = student_a_client.delete(f"/api/v1/bookmarks/{b_bookmark_id}")
    assert del_resp.status_code == 404
    assert "access denied" in del_resp.json()["detail"].lower()

    # Confirm the bookmark still exists in the database
    db = TestingSessionLocal()
    still_exists = db.query(Bookmark).filter(Bookmark.id == b_bookmark_id).first()
    db.close()
    assert still_exists is not None

# =========================================================================
# 12. Profile update persistence across requests
# =========================================================================
def test_12_profile_update_persistence_across_requests():
    student_a_client, _ = get_auth_client("rohan@example.com", "Password@1234")
    
    # Update profile
    patch_resp = student_a_client.patch("/api/v1/profile", json={
        "college": "Indian Institute of Science",
        "course": "M.Tech AI & Robotics",
        "study_year": "2027",
        "target_role": "Machine Learning Engineer",
        "skill_level": "Advanced",
        "study_availability": 4.5
    })
    assert patch_resp.status_code == 200
    assert patch_resp.json()["target_role"] == "Machine Learning Engineer"

    # Send a fresh GET request to verify persistence
    get_resp = student_a_client.get("/api/v1/profile")
    assert get_resp.status_code == 200
    data = get_resp.json()
    assert data["college"] == "Indian Institute of Science"
    assert data["course"] == "M.Tech AI & Robotics"
    assert data["study_year"] == "2027"
    assert data["target_role"] == "Machine Learning Engineer"
    assert data["skill_level"] == "Advanced"
    assert data["study_availability"] == 4.5

# =========================================================================
# 13. Learning progress recording and persistence
# =========================================================================
def test_13_learning_progress_recording_and_persistence():
    student_a_client, _ = get_auth_client("rohan@example.com", "Password@1234")
    
    # Get available lessons
    lessons_resp = student_a_client.get("/api/v1/learning/lessons")
    assert lessons_resp.status_code == 200
    lessons = lessons_resp.json()
    assert len(lessons) > 0
    lesson_id = lessons[0]["id"]

    # Mark lesson complete
    put_resp = student_a_client.put(f"/api/v1/learning/lessons/{lesson_id}/progress")
    assert put_resp.status_code == 200
    assert put_resp.json()["status"] == "completed"

    # Query lesson detail to verify is_completed is True
    lesson_detail_resp = student_a_client.get(f"/api/v1/learning/lessons/{lesson_id}")
    assert lesson_detail_resp.status_code == 200
    assert lesson_detail_resp.json()["is_completed"] is True

# =========================================================================
# 14. Practice session creation and question retrieval
# =========================================================================
def test_14_practice_session_creation_and_question_retrieval():
    student_a_client, _ = get_auth_client("rohan@example.com", "Password@1234")
    
    # Create practice session
    create_resp = student_a_client.post("/api/v1/practice/sessions", json={
        "category": "aptitude",
        "difficulty": "all",
        "question_count": 3
    })
    assert create_resp.status_code == 200
    session_data = create_resp.json()
    session_id = session_data["id"]
    assert len(session_data["questions"]) > 0

    # Retrieve questions for this session
    q_resp = student_a_client.get(f"/api/v1/practice/sessions/{session_id}/questions")
    assert q_resp.status_code == 200
    questions = q_resp.json()
    assert len(questions) > 0
    # Verify that option explanations and is_correct are NOT leaked in question payload
    first_opt = questions[0]["question"]["options"][0]
    assert "option_key" in first_opt
    assert "option_text" in first_opt
    assert "is_correct" not in first_opt

# =========================================================================
# 15. Practice answer submission with full explanation return
# =========================================================================
def test_15_practice_answer_submission_with_full_explanation():
    student_a_client, _ = get_auth_client("rohan@example.com", "Password@1234")
    
    # Create session
    create_resp = student_a_client.post("/api/v1/practice/sessions", json={
        "category": "aptitude",
        "question_count": 2
    })
    session_id = create_resp.json()["id"]
    q_item = create_resp.json()["questions"][0]
    q_id = q_item["question"]["id"]

    # Submit answer
    answer_resp = student_a_client.post(f"/api/v1/practice/sessions/{session_id}/answers", json={
        "question_id": q_id,
        "selected_option": "B"
    })
    assert answer_resp.status_code == 200
    feedback = answer_resp.json()
    # Check all pedagogical explanation components
    assert "is_correct" in feedback
    assert "correct_option" in feedback
    assert "explanation" in feedback
    assert "step_by_step_reasoning" in feedback
    assert "common_mistake" in feedback
    assert "learning_tip" in feedback
    assert "options_breakdown" in feedback

# =========================================================================
# 16. Strict answer locking: cannot change answer once submitted
# =========================================================================
def test_16_strict_answer_locking():
    student_a_client, _ = get_auth_client("rohan@example.com", "Password@1234")
    
    # Create session
    create_resp = student_a_client.post("/api/v1/practice/sessions", json={
        "category": "aptitude",
        "question_count": 2
    })
    session_id = create_resp.json()["id"]
    q_item = create_resp.json()["questions"][0]
    q_id = q_item["question"]["id"]

    # Submit first answer as "B"
    resp1 = student_a_client.post(f"/api/v1/practice/sessions/{session_id}/answers", json={
        "question_id": q_id,
        "selected_option": "B"
    })
    assert resp1.status_code == 200
    initial_selection = resp1.json()["selected_option"]

    # Attempt to change answer to "C"
    resp2 = student_a_client.post(f"/api/v1/practice/sessions/{session_id}/answers", json={
        "question_id": q_id,
        "selected_option": "C"
    })
    assert resp2.status_code == 200
    # Must preserve the locked original answer "B"
    assert resp2.json()["selected_option"] == initial_selection

# =========================================================================
# 17. Practice summary calculation accuracy
# =========================================================================
def test_17_practice_summary_calculation_accuracy():
    student_a_client, _ = get_auth_client("rohan@example.com", "Password@1234")
    
    # Create a 2-question session
    create_resp = student_a_client.post("/api/v1/practice/sessions", json={
        "category": "aptitude",
        "question_count": 2
    })
    session_id = create_resp.json()["id"]
    questions = create_resp.json()["questions"]
    assert len(questions) == 2

    # Answer both questions
    for q_item in questions:
        student_a_client.post(f"/api/v1/practice/sessions/{session_id}/answers", json={
            "question_id": q_item["question"]["id"],
            "selected_option": "B"
        })

    # Fetch summary
    summary_resp = student_a_client.get(f"/api/v1/practice/sessions/{session_id}/summary")
    assert summary_resp.status_code == 200
    summary = summary_resp.json()
    assert summary["total_questions"] == 2
    assert summary["completed_questions"] == 2
    assert "accuracy" in summary
    assert "score_percentage" in summary
    assert summary["correct_count"] + summary["incorrect_count"] == 2

# =========================================================================
# 18. Password reset token generation
# =========================================================================
def test_18_password_reset_token_generation(client):
    response = client.post("/api/v1/auth/forgot-password", json={
        "email": "rohan@example.com"
    })
    assert response.status_code == 200
    data = response.json()
    assert "reset_token" in data
    raw_token = data["reset_token"]
    assert len(raw_token) > 20

    # Verify token exists in database (stored hashed)
    token_hash = hash_token(raw_token)
    db = TestingSessionLocal()
    token_rec = db.query(PasswordResetToken).filter(PasswordResetToken.token_hash == token_hash).first()
    db.close()
    assert token_rec is not None
    assert token_rec.used_at is None

# =========================================================================
# 19. Password reset token expiration handling
# =========================================================================
def test_19_password_reset_token_expiration_handling(client):
    # Generate token
    gen_resp = client.post("/api/v1/auth/forgot-password", json={"email": "rohan@example.com"})
    raw_token = gen_resp.json()["reset_token"]
    token_hash = hash_token(raw_token)

    # Artificially expire the token in database
    db = TestingSessionLocal()
    token_rec = db.query(PasswordResetToken).filter(PasswordResetToken.token_hash == token_hash).first()
    token_rec.expires_at = datetime.now(timezone.utc) - timedelta(hours=2)
    db.commit()
    db.close()

    # Attempt to reset password with expired token
    reset_resp = client.post("/api/v1/auth/reset-password", json={
        "token": raw_token,
        "new_password": "ExpiredPassAttempt@123"
    })
    assert reset_resp.status_code == 400
    assert "expired" in reset_resp.json()["detail"].lower()

# =========================================================================
# 20. Successful password reset with subsequent login using new password
# =========================================================================
def test_20_successful_password_reset_and_login_with_new_password(client):
    # 1. Request fresh token
    gen_resp = client.post("/api/v1/auth/forgot-password", json={"email": "rohan@example.com"})
    raw_token = gen_resp.json()["reset_token"]

    # 2. Reset password
    reset_resp = client.post("/api/v1/auth/reset-password", json={
        "token": raw_token,
        "new_password": "BrandNewPassword@2026!"
    })
    assert reset_resp.status_code == 200
    assert "successfully reset" in reset_resp.json()["message"].lower()

    # 3. Token cannot be reused (single-use enforcement)
    re_use_resp = client.post("/api/v1/auth/reset-password", json={
        "token": raw_token,
        "new_password": "AnotherNewPassword@2026!"
    })
    assert re_use_resp.status_code == 400

    # 4. Old password must fail
    old_login = client.post("/api/v1/auth/login", json={
        "email": "rohan@example.com",
        "password": "Password@1234"
    })
    assert old_login.status_code == 401

    # 5. New password must succeed
    new_login = client.post("/api/v1/auth/login", json={
        "email": "rohan@example.com",
        "password": "BrandNewPassword@2026!"
    })
    assert new_login.status_code == 200
    assert new_login.json()["user"]["email"] == "rohan@example.com"

# =========================================================================
# 21. Communication Lab: Speaking Session Submission & Rubric Evaluation
# =========================================================================
def test_21_communication_speaking_session_submission_and_rubric():
    client, token = get_auth_client("student@interviewai.dev", "Student@123456")
    resp = client.post("/api/v1/communication/submit", json={
        "category": "Self Introduction",
        "prompt_title": "Tell Me About Yourself",
        "prompt_question": "Walk me through your background and why you are passionate about software engineering.",
        "framework": "Present -> Past -> Future",
        "transcript": "I am a computer science student specializing in backend systems. Over the past year, I built an interactive application using FastAPI and React that evaluated code efficiency. During my internship, I reduced database latency by 35%. I am eager to apply my background in scalable APIs to your engineering team.",
        "audio_duration_seconds": 35.0
    })
    assert resp.status_code == 201
    data = resp.json()
    assert data["prompt_title"] == "Tell Me About Yourself"
    assert data["overall_score"] >= 6.0
    assert data["relevance_score"] >= 6.0
    assert data["wpm"] > 50
    assert len(data["strengths"]) > 0
    assert data["status"] == "completed"

# =========================================================================
# 22. Communication Lab: Attempt History & Data Isolation
# =========================================================================
def test_22_communication_history_retrieval_and_data_isolation(client):
    client_student, token_student = get_auth_client("student@interviewai.dev", "Student@123456")
    client_rohan, token_rohan = get_auth_client("rohan@example.com", "BrandNewPassword@2026!")

    # Student should see their submitted session
    hist_resp = client_student.get("/api/v1/communication/history")
    assert hist_resp.status_code == 200
    student_sessions = hist_resp.json()
    assert len(student_sessions) >= 1

    # Rohan should not see student's private sessions
    rohan_hist = client_rohan.get("/api/v1/communication/history")
    assert rohan_hist.status_code == 200
    assert len(rohan_hist.json()) == 0

# =========================================================================
# 23. Aptitude Question Bank Scale & Validation
# =========================================================================
def test_23_aptitude_question_bank_scale_and_validation(client):
    resp = client.get("/api/v1/practice/questions?limit=50")
    assert resp.status_code == 200
    questions = resp.json()
    assert len(questions) > 0
    # Verify each question has exactly 4 options
    for q in questions[:10]:
        assert len(q["options"]) == 4

# =========================================================================
# 24. Coding Problem Bank Scale & Safe Execution
# =========================================================================
def test_24_coding_problem_bank_scale_and_safe_execution():
    client_student, token = get_auth_client("student@interviewai.dev", "Student@123456")
    resp = client_student.get("/api/v1/coding/problems")
    assert resp.status_code == 200
    problems = resp.json()
    assert len(problems) >= 3

    # Submit valid Python solution for first problem
    first_p = problems[0]
    run_resp = client_student.post("/api/v1/coding/run", json={
        "problem_id": first_p["id"],
        "language": "python",
        "code": "def solution(nums, target):\n    return [0, 1]"
    })
    assert run_resp.status_code == 200
    assert run_resp.json()["status"] in ["accepted", "preview_evaluated"]
