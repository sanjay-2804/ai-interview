from sqlalchemy.orm import Session
from sqlalchemy import func
from fastapi import HTTPException, status
from typing import Dict, Any, List, Optional
import datetime
from app.models.models import (
    Question, QuestionOption, PracticeSession, SessionQuestion,
    SubmittedAnswer, Topic, ActivityEvent, utc_now
)
from app.schemas.schemas import (
    AnswerFeedback, OptionFeedback, QuestionPublic, QuestionOptionPublic,
    SessionQuestionItem, PracticeSessionDetail
)

class PracticeService:
    def create_session(
        self,
        db: Session,
        user_id: int,
        category: str,
        subcategory: Optional[str] = None,
        difficulty: str = "all",
        question_count: int = 5,
        session_mode: str = "practice",
        time_limit_seconds: Optional[int] = None
    ) -> PracticeSession:
        # Query matching questions
        query = db.query(Question).join(Topic)
        if category and category != "all":
            query = query.filter(Topic.category == category)
        if subcategory and subcategory != "all":
            query = query.filter(Topic.subcategory == subcategory)
        if difficulty and difficulty != "all":
            query = query.filter(Question.difficulty == difficulty.lower())

        # Order randomly or by id
        questions = query.order_by(func.random()).limit(question_count).all()

        if not questions:
            # Fallback to any published questions
            questions = db.query(Question).filter(Question.is_published == True).limit(question_count).all()

        if not questions:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No questions found for the selected category and difficulty."
            )

        session = PracticeSession(
            user_id=user_id,
            category=category,
            subcategory=subcategory,
            difficulty=difficulty,
            session_mode=session_mode,
            time_limit_seconds=time_limit_seconds,
            marked_for_review_json=[],
            total_questions=len(questions),
            completed_questions=0,
            correct_count=0,
            score_percentage=0.0,
            status="in_progress",
            started_at=utc_now()
        )
        db.add(session)
        db.flush()

        for idx, q in enumerate(questions):
            sq = SessionQuestion(
                session_id=session.id,
                question_id=q.id,
                order_index=idx + 1,
                is_answered=False
            )
            db.add(sq)

        db.commit()
        db.refresh(session)
        return session

    def get_session_detail(self, db: Session, session_id: int, user_id: int) -> PracticeSessionDetail:
        session = db.query(PracticeSession).filter(
            PracticeSession.id == session_id,
            PracticeSession.user_id == user_id
        ).first()

        if not session:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Practice session not found or access denied."
            )

        session_questions = db.query(SessionQuestion).filter(
            SessionQuestion.session_id == session.id
        ).order_by(SessionQuestion.order_index).all()

        items: List[SessionQuestionItem] = []
        for sq in session_questions:
            q = sq.question
            public_options = [
                QuestionOptionPublic(option_key=opt.option_key, option_text=opt.option_text)
                for opt in q.options
            ]
            public_q = QuestionPublic(
                id=q.id,
                topic_id=q.topic_id,
                question_type=q.question_type,
                difficulty=q.difficulty,
                question_text=q.question_text,
                code_snippet=q.code_snippet,
                options=public_options
            )

            feedback = None
            if sq.is_answered:
                feedback = self._build_feedback(q, sq.submitted_answer, sq.is_correct)

            items.append(SessionQuestionItem(
                order_index=sq.order_index,
                question=public_q,
                is_answered=sq.is_answered,
                submitted_answer=sq.submitted_answer,
                is_correct=sq.is_correct,
                feedback=feedback
            ))

        return PracticeSessionDetail(
            id=session.id,
            category=session.category,
            subcategory=session.subcategory,
            difficulty=session.difficulty,
            session_mode=getattr(session, "session_mode", "practice") or "practice",
            time_limit_seconds=getattr(session, "time_limit_seconds", None),
            marked_for_review_json=getattr(session, "marked_for_review_json", []) or [],
            total_questions=session.total_questions,
            completed_questions=session.completed_questions,
            correct_count=session.correct_count,
            score_percentage=session.score_percentage,
            status=session.status,
            questions=items
        )

    def toggle_mark_for_review(self, db: Session, user_id: int, session_id: int, question_index: int, is_marked: bool) -> List[int]:
        session = db.query(PracticeSession).filter(
            PracticeSession.id == session_id,
            PracticeSession.user_id == user_id
        ).first()
        if not session:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Session not found.")
        
        current_marks = list(session.marked_for_review_json or [])
        if is_marked and question_index not in current_marks:
            current_marks.append(question_index)
        elif not is_marked and question_index in current_marks:
            current_marks.remove(question_index)
        
        session.marked_for_review_json = current_marks
        db.commit()
        return current_marks

    def complete_session(self, db: Session, user_id: int, session_id: int) -> PracticeSessionDetail:
        session = db.query(PracticeSession).filter(
            PracticeSession.id == session_id,
            PracticeSession.user_id == user_id
        ).first()
        if not session:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Session not found.")
        
        session.status = "completed"
        session.completed_at = utc_now()
        db.commit()
        return self.get_session_detail(db, session_id, user_id)

    def submit_answer(
        self,
        db: Session,
        user_id: int,
        question_id: int,
        selected_option: str,
        session_id: Optional[int] = None
    ) -> AnswerFeedback:
        selected_option = selected_option.strip().upper()

        # If inside a practice session, enforce strict rules
        if session_id:
            session = db.query(PracticeSession).filter(
                PracticeSession.id == session_id,
                PracticeSession.user_id == user_id
            ).first()

            if not session:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Practice session not found."
                )

            sq = db.query(SessionQuestion).filter(
                SessionQuestion.session_id == session_id,
                SessionQuestion.question_id == question_id
            ).first()

            if not sq:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Question does not belong to this practice session."
                )

            # RULE: Cannot change submitted answer in the current session
            if sq.is_answered:
                # Return existing feedback without recalculating or modifying score
                return self._build_feedback(sq.question, sq.submitted_answer, sq.is_correct)

        question = db.query(Question).filter(Question.id == question_id).first()
        if not question:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Question not found."
            )

        correct_opt = next((opt for opt in question.options if opt.is_correct), None)
        if not correct_opt:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Question configuration error: no correct option set."
            )

        is_correct = (selected_option == correct_opt.option_key)

        # Record in submitted_answers
        sub = SubmittedAnswer(
            user_id=user_id,
            question_id=question_id,
            session_id=session_id,
            selected_option=selected_option,
            is_correct=is_correct,
            created_at=utc_now()
        )
        db.add(sub)

        # Update session state if part of a session
        if session_id and sq:
            sq.is_answered = True
            sq.submitted_answer = selected_option
            sq.is_correct = is_correct
            sq.answered_at = utc_now()

            session.completed_questions += 1
            if is_correct:
                session.correct_count += 1
            session.score_percentage = round((session.correct_count / session.total_questions) * 100, 1)

            if session.completed_questions >= session.total_questions:
                session.status = "completed"
                session.completed_at = utc_now()

                # Record activity event
                activity = ActivityEvent(
                    user_id=user_id,
                    event_type="practice_session",
                    title=f"Completed {session.category.capitalize()} Practice Session",
                    details=f"Score: {session.correct_count}/{session.total_questions} ({session.score_percentage}%)",
                    metadata_json={"session_id": session.id, "accuracy": session.score_percentage}
                )
                db.add(activity)

        db.commit()

        return self._build_feedback(question, selected_option, is_correct)

    def _build_feedback(self, question: Question, selected_option: str, is_correct: bool) -> AnswerFeedback:
        correct_opt = next((opt for opt in question.options if opt.is_correct), None)
        correct_key = correct_opt.option_key if correct_opt else ""

        breakdown = []
        for opt in question.options:
            breakdown.append(OptionFeedback(
                option_key=opt.option_key,
                option_text=opt.option_text,
                is_correct=opt.is_correct,
                why_wrong=opt.why_wrong_explanation if not opt.is_correct else "This is the correct answer."
            ))

        if is_correct:
            encouraging_feedback = "Great work! You understood the core concept. Keep building on this progress."
            status_text = "Correct"
        else:
            encouraging_feedback = "Every mistake is an opportunity to strengthen your understanding. Review the explanation and continue when you're ready."
            status_text = "Incorrect"

        return AnswerFeedback(
            question_id=question.id,
            selected_option=selected_option,
            correct_option=correct_key,
            is_correct=is_correct,
            status=status_text,
            explanation=question.explanation,
            step_by_step_reasoning=question.step_by_step_reasoning,
            practical_example=question.practical_example,
            common_mistake=question.common_mistake,
            learning_tip=question.learning_tip,
            related_concept_url=question.related_concept_url,
            encouraging_feedback=encouraging_feedback,
            options_breakdown=breakdown
        )

practice_service = PracticeService()

