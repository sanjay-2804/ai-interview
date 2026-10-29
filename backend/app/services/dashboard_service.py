from sqlalchemy.orm import Session
from sqlalchemy import func, distinct, case
import datetime
from typing import Dict, Any, List
from app.models.models import (
    User, UserProfile, SubmittedAnswer, LessonProgress, CodingSubmission,
    InterviewSession, ActivityEvent, Question, Topic, Lesson, Bookmark
)
from app.schemas.schemas import DashboardStats

class DashboardService:
    def get_student_stats(self, db: Session, user: User) -> DashboardStats:
        user_id = user.id
        profile = user.profile

        target_role = profile.target_role if profile else "Software Developer"
        skill_level = profile.skill_level if profile else "Beginner"

        # Questions attempted
        total_attempts = db.query(SubmittedAnswer).filter(SubmittedAnswer.user_id == user_id).count()
        correct_attempts = db.query(SubmittedAnswer).filter(
            SubmittedAnswer.user_id == user_id,
            SubmittedAnswer.is_correct == True
        ).count()
        accuracy = round((correct_attempts / total_attempts * 100), 1) if total_attempts > 0 else 0.0

        # Lessons completed
        lessons_completed = db.query(LessonProgress).filter(
            LessonProgress.user_id == user_id,
            LessonProgress.status == "completed"
        ).count()

        # Coding problems solved (distinct problem_id where status == accepted or preview_evaluated)
        coding_solved = db.query(distinct(CodingSubmission.problem_id)).filter(
            CodingSubmission.user_id == user_id
        ).count()

        # Mock interviews completed
        mock_interviews = db.query(InterviewSession).filter(
            InterviewSession.user_id == user_id,
            InterviewSession.status == "completed"
        ).count()

        # Calculate actual streak days from ActivityEvent timestamps
        activities = db.query(ActivityEvent).filter(
            ActivityEvent.user_id == user_id
        ).order_by(ActivityEvent.created_at.desc()).all()

        streak_days = self._calculate_streak(activities)

        recent_activity_list = [
            {
                "id": a.id,
                "type": a.event_type,
                "title": a.title,
                "details": a.details,
                "time": a.created_at.strftime("%b %d, %Y %H:%M")
            }
            for a in activities[:6]
        ]

        # Weak and Strong topics calculation from real submitted answers
        topic_perf = db.query(
            Topic.name,
            Topic.category,
            func.count(SubmittedAnswer.id).label("total"),
            func.sum(case((SubmittedAnswer.is_correct == True, 1), else_=0)).label("correct")
        ).join(Question, Question.topic_id == Topic.id)\
         .join(SubmittedAnswer, SubmittedAnswer.question_id == Question.id)\
         .filter(SubmittedAnswer.user_id == user_id)\
         .group_by(Topic.id).all()

        weak_topics = []
        strong_topics = []

        for name, category, total, correct in topic_perf:
            total_cnt = total or 0
            correct_cnt = correct or 0
            pct = round((correct_cnt / total_cnt) * 100, 1) if total_cnt > 0 else 0.0
            item = {"topic": name, "category": category, "accuracy": pct, "attempts": total_cnt}
            if pct < 65.0:
                weak_topics.append(item)
            elif pct >= 75.0:
                strong_topics.append(item)

        # Dynamic recommendations
        recommended = []
        if total_attempts == 0:
            recommended.append({
                "title": "Start with Quantitative Aptitude Foundations",
                "action": "Begin your first practice set to evaluate your starting baseline.",
                "link": "/practice/aptitude",
                "category": "Aptitude"
            })
            recommended.append({
                "title": "Review Data Structures & Algorithms Roadmap",
                "action": "Explore core topics in Arrays, Linked Lists, and Asymptotic Complexity.",
                "link": "/roadmap",
                "category": "Technical"
            })
        elif weak_topics:
            worst = sorted(weak_topics, key=lambda x: x["accuracy"])[0]
            recommended.append({
                "title": f"Review {worst['topic']}",
                "action": f"Your accuracy is currently {worst['accuracy']}%. Strengthen concepts with targeted questions.",
                "link": "/practice/aptitude" if worst['category'] == 'aptitude' else "/practice/technical",
                "category": worst['category'].capitalize()
            })
            recommended.append({
                "title": "Complete a Coding Practice Problem",
                "action": "Reinforce algorithmic problem solving with hands-on practice.",
                "link": "/coding",
                "category": "Coding"
            })
        else:
            recommended.append({
                "title": "Conduct a 15-Minute Mock Technical Interview",
                "action": "Practice speaking through technical solutions and receive instant AI feedback.",
                "link": "/interview",
                "category": "Interview"
            })
            recommended.append({
                "title": "Build and Format Placement Resume",
                "action": "Run ATS optimization and project impact review on your resume.",
                "link": "/resume",
                "category": "Career"
            })

        # Roadmap progress estimation
        total_roadmap_milestones = 13
        completed_milestones = min(int((lessons_completed * 0.5) + (coding_solved * 0.5) + (1 if mock_interviews > 0 else 0)), total_roadmap_milestones)
        roadmap_pct = round((completed_milestones / total_roadmap_milestones) * 100, 1)

        return DashboardStats(
            total_questions_attempted=total_attempts,
            overall_accuracy_percentage=accuracy,
            total_lessons_completed=lessons_completed,
            total_coding_solved=coding_solved,
            total_mock_interviews=mock_interviews,
            streak_days=streak_days,
            recent_activities=recent_activity_list,
            weak_topics=weak_topics,
            strong_topics=strong_topics,
            recommended_activities=recommended,
            roadmap_progress_percentage=roadmap_pct,
            target_role=target_role,
            skill_level=skill_level
        )

    def _calculate_streak(self, activities: List[ActivityEvent]) -> int:
        if not activities:
            return 0
        
        # Get unique dates of activity
        dates = sorted({a.created_at.date() for a in activities}, reverse=True)
        today = datetime.datetime.now(datetime.timezone.utc).date()
        yesterday = today - datetime.timedelta(days=1)

        if not dates or (dates[0] != today and dates[0] != yesterday):
            return 0

        streak = 1
        current = dates[0]
        for d in dates[1:]:
            if d == current - datetime.timedelta(days=1):
                streak += 1
                current = d
            else:
                break
        return streak

dashboard_service = DashboardService()

