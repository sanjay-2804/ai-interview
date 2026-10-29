import React, { useState, useEffect, useRef } from 'react';
import { useParams, useNavigate, Link } from 'react-router-dom';
import { api } from '../../services/api';
import { PracticeSessionDetail, SessionQuestionItem, AnswerFeedback } from '../../types';
import { FeedbackPanel } from '../../components/FeedbackPanel';
import {
  HelpCircle, ArrowLeft, ArrowRight, CheckCircle, XCircle,
  Trophy, RotateCcw, BookOpen, AlertCircle, Timer, Flag, CheckCheck
} from 'lucide-react';

export const PracticeSessionRunner: React.FC = () => {
  const { sessionId } = useParams<{ sessionId: string }>();
  const navigate = useNavigate();

  const [session, setSession] = useState<PracticeSessionDetail | null>(null);
  const [currentIndex, setCurrentIndex] = useState<number>(0);
  const [selectedOption, setSelectedOption] = useState<string>('');
  const [isSubmitting, setIsSubmitting] = useState<boolean>(false);
  const [errorMsg, setErrorMsg] = useState<string | null>(null);
  const [loading, setLoading] = useState<boolean>(true);

  // Timed Test State
  const [remainingSeconds, setRemainingSeconds] = useState<number | null>(null);
  const timerIntervalRef = useRef<any>(null);
  const [markedQuestions, setMarkedQuestions] = useState<Set<number>>(new Set());
  const [isConfirmingFinish, setIsConfirmingFinish] = useState<boolean>(false);

  // Load session from backend
  const loadSessionData = async () => {
    if (!sessionId) return;
    try {
      const data = await api.getPracticeSession(parseInt(sessionId, 10));
      setSession(data);
      if (data.marked_for_review_json) {
        setMarkedQuestions(new Set(data.marked_for_review_json));
      }

      // Initialize timer if session has a time limit
      if (data.time_limit_seconds && data.status !== 'completed') {
        setRemainingSeconds(data.time_limit_seconds);
      }

      // Find first unanswered question
      const firstUnanswered = data.questions.findIndex((q) => !q.is_answered);
      if (firstUnanswered !== -1) {
        setCurrentIndex(firstUnanswered);
      } else {
        setCurrentIndex(data.questions.length - 1);
      }
    } catch (err: any) {
      setErrorMsg(err.message || 'Failed to load practice session.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadSessionData();
  }, [sessionId]);

  // Countdown Timer Hook
  useEffect(() => {
    if (remainingSeconds !== null && remainingSeconds > 0 && session?.status !== 'completed') {
      timerIntervalRef.current = setInterval(() => {
        setRemainingSeconds((prev) => {
          if (prev !== null && prev <= 1) {
            clearInterval(timerIntervalRef.current);
            handleAutoSubmitTimerExpired();
            return 0;
          }
          return prev !== null ? prev - 1 : null;
        });
      }, 1000);
    } else {
      clearInterval(timerIntervalRef.current);
    }
    return () => clearInterval(timerIntervalRef.current);
  }, [remainingSeconds, session?.status]);

  const handleAutoSubmitTimerExpired = async () => {
    if (!session) return;
    try {
      const updated = await api.completePracticeSession(session.id);
      setSession(updated);
    } catch (e) {
      console.warn('Auto finish session:', e);
    }
  };

  if (loading) {
    return (
      <div className="flex h-96 items-center justify-center">
        <div className="flex flex-col items-center gap-3">
          <div className="h-8 w-8 animate-spin rounded-full border-4 border-brand-600 border-t-transparent" />
          <p className="text-sm font-medium text-slateText-secondary">Loading question set...</p>
        </div>
      </div>
    );
  }

  if (errorMsg || !session) {
    return (
      <div className="max-w-xl mx-auto mt-12 rounded-2xl border border-rose-200 bg-white p-8 text-center shadow-subtle">
        <AlertCircle className="mx-auto h-12 w-12 text-rose-500 mb-3" />
        <h2 className="text-lg font-bold text-navy-800">Unable to Load Assessment</h2>
        <p className="mt-1 text-sm text-slateText-secondary">{errorMsg || 'Session not found.'}</p>
        <Link
          to="/app/aptitude"
          className="mt-6 inline-flex items-center gap-2 rounded-xl bg-brand-600 px-5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-brand-700"
        >
          <ArrowLeft className="h-4 w-4" />
          Return to Aptitude Practice
        </Link>
      </div>
    );
  }

  const currentItem: SessionQuestionItem = session.questions[currentIndex];
  const isCurrentAnswered = currentItem.is_answered;
  const isSessionFinished = session.status === 'completed' || session.questions.every((q) => q.is_answered);
  const isCurrentMarked = markedQuestions.has(currentIndex);

  // Toggle Mark for Review
  const handleToggleMark = async () => {
    const nextMarked = !isCurrentMarked;
    const updated = new Set(markedQuestions);
    if (nextMarked) {
      updated.add(currentIndex);
    } else {
      updated.delete(currentIndex);
    }
    setMarkedQuestions(updated);
    try {
      await api.markQuestionForReview(session.id, currentIndex, nextMarked);
    } catch (e) {
      console.warn('Failed to sync mark for review:', e);
    }
  };

  // Handle Answer Submission (Strict Rule: Lock after submit)
  const handleSubmitAnswer = async () => {
    if (!selectedOption || isCurrentAnswered || isSubmitting) return;

    setIsSubmitting(true);
    setErrorMsg(null);
    try {
      const feedback: AnswerFeedback = await api.submitPracticeAnswer({
        session_id: session.id,
        question_id: currentItem.question.id,
        selected_option: selectedOption,
      });

      // Update state in place
      const updatedQuestions = [...session.questions];
      updatedQuestions[currentIndex] = {
        ...currentItem,
        is_answered: true,
        submitted_answer: selectedOption,
        is_correct: feedback.is_correct,
        feedback: feedback,
      };

      const newCorrectCount = updatedQuestions.filter((q) => q.is_correct).length;
      const newCompletedCount = updatedQuestions.filter((q) => q.is_answered).length;
      const newPct = Math.round((newCorrectCount / session.total_questions) * 100);

      setSession({
        ...session,
        questions: updatedQuestions,
        completed_questions: newCompletedCount,
        correct_count: newCorrectCount,
        score_percentage: newPct,
        status: newCompletedCount >= session.total_questions ? 'completed' : 'in_progress',
      });
    } catch (err: any) {
      setErrorMsg(err.message || 'Failed to submit answer.');
    } finally {
      setIsSubmitting(false);
    }
  };

  // Explicit advance to next question
  const handleNextQuestion = () => {
    setSelectedOption('');
    if (currentIndex < session.questions.length - 1) {
      setCurrentIndex((prev) => prev + 1);
    }
  };

  const handleFinishEarly = async () => {
    try {
      const updated = await api.completePracticeSession(session.id);
      setSession(updated);
      setIsConfirmingFinish(false);
    } catch (e) {
      console.error(e);
    }
  };

  const formatTimer = (totalSecs: number) => {
    const mins = Math.floor(totalSecs / 60);
    const secs = totalSecs % 60;
    return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
  };

  return (
    <div className="max-w-5xl mx-auto space-y-6 pb-16">
      {/* Session Progress & Timer Bar */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-surface-border pb-4">
        <div>
          <div className="flex items-center gap-2">
            <span className="text-xs font-bold uppercase tracking-wider text-brand-600">
              {session.category.toUpperCase()} ASSESSMENT
            </span>
            <span className="text-slate-300">•</span>
            <span className="text-xs font-medium text-slateText-muted capitalize">
              {session.session_mode || 'Practice'} Mode
            </span>
          </div>
          <h2 className="text-lg font-bold text-navy-800">
            Question {currentIndex + 1} of {session.total_questions}
          </h2>
        </div>

        {/* Timed Test Countdown Display */}
        {remainingSeconds !== null && (
          <div className={`flex items-center gap-2 px-4 py-2 rounded-xl font-mono text-sm font-bold border ${
            remainingSeconds <= 120
              ? 'bg-rose-50 text-rose-700 border-rose-300 animate-pulse'
              : 'bg-blue-50 text-brand-700 border-blue-200'
          }`}>
            <Timer className="h-4 w-4" />
            <span>Time Remaining: {formatTimer(remainingSeconds)}</span>
          </div>
        )}

        {/* Actions Bar */}
        <div className="flex items-center gap-2">
          <button
            type="button"
            onClick={handleToggleMark}
            className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-bold border transition-all ${
              isCurrentMarked
                ? 'bg-amber-100 text-amber-900 border-amber-300'
                : 'bg-white text-slateText-secondary border-slate-200 hover:bg-slate-50'
            }`}
          >
            <Flag className={`h-3.5 w-3.5 ${isCurrentMarked ? 'fill-amber-600 text-amber-600' : ''}`} />
            <span>{isCurrentMarked ? 'Marked' : 'Mark for Review'}</span>
          </button>

          {!isSessionFinished && (
            <button
              onClick={() => setIsConfirmingFinish(true)}
              className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-bold text-navy-800 bg-slate-100 hover:bg-slate-200 border border-slate-200"
            >
              <CheckCheck className="h-3.5 w-3.5" />
              <span>Finish Test</span>
            </button>
          )}
        </div>
      </div>

      {/* Question Palette Indicator */}
      <div className="flex items-center gap-1.5 flex-wrap p-3 rounded-xl bg-slate-50 border border-slate-200">
        <span className="text-[11px] font-bold text-slateText-secondary mr-2">Question Palette:</span>
        {session.questions.map((q, idx) => {
          const isMarked = markedQuestions.has(idx);
          const isCurrent = idx === currentIndex;
          return (
            <button
              key={idx}
              onClick={() => {
                setSelectedOption('');
                setCurrentIndex(idx);
              }}
              className={`relative flex h-8 w-8 items-center justify-center rounded-lg text-xs font-bold transition-all ${
                isCurrent ? 'ring-2 ring-brand-600 ring-offset-2' : ''
              } ${
                q.is_answered
                  ? q.is_correct
                    ? 'bg-emerald-100 text-emerald-800 border border-emerald-300'
                    : 'bg-rose-100 text-rose-800 border border-rose-300'
                  : 'bg-white text-slateText-secondary border border-slate-200 hover:bg-slate-100'
              }`}
            >
              {idx + 1}
              {isMarked && (
                <span className="absolute -top-1 -right-1 h-2.5 w-2.5 rounded-full bg-amber-500 ring-1 ring-white" />
              )}
            </button>
          );
        })}
      </div>

      {/* Main Question Card */}
      <div className="rounded-2xl border border-surface-border bg-white p-6 sm:p-8 shadow-card">
        {/* Difficulty badge & status */}
        <div className="flex items-center justify-between mb-4">
          <span className="inline-flex items-center rounded-md bg-slate-100 px-2.5 py-1 text-[11px] font-semibold text-slateText-secondary uppercase">
            {currentItem.question.difficulty}
          </span>
          {isCurrentAnswered && (
            <span className="text-xs font-semibold text-slateText-muted">
              Submission Locked
            </span>
          )}
        </div>

        {/* Question Text */}
        <h3 className="text-base sm:text-lg font-semibold text-slateText-primary leading-relaxed whitespace-pre-line">
          {currentItem.question.question_text}
        </h3>

        {/* Optional Code Snippet */}
        {currentItem.question.code_snippet && (
          <pre className="mt-4 rounded-xl bg-slate-50 border border-slate-200 p-4 text-xs font-mono text-slate-800 overflow-x-auto shadow-xs">
            <code>{currentItem.question.code_snippet}</code>
          </pre>
        )}

        {/* Answer Options */}
        <div className="mt-6 space-y-3">
          {currentItem.question.options.map((opt) => {
            const isOptionSelected =
              (isCurrentAnswered && currentItem.submitted_answer === opt.option_key) ||
              (!isCurrentAnswered && selectedOption === opt.option_key);

            return (
              <button
                key={opt.option_key}
                type="button"
                disabled={isCurrentAnswered || isSubmitting}
                onClick={() => setSelectedOption(opt.option_key)}
                className={`flex w-full items-start gap-4 p-4 sm:p-5 rounded-2xl border text-left text-sm transition-all duration-150 ${
                  isOptionSelected
                    ? isCurrentAnswered
                      ? currentItem.is_correct
                        ? 'border-2 border-emerald-500 bg-emerald-50/80 text-emerald-950 font-medium shadow-xs'
                        : 'border-2 border-rose-500 bg-rose-50/80 text-rose-950 font-medium shadow-xs'
                      : 'border-2 border-brand-600 bg-brand-50/80 text-brand-950 font-semibold shadow-xs'
                    : isCurrentAnswered
                    ? 'border-slate-200 bg-slate-50/50 text-slateText-secondary opacity-75 cursor-not-allowed'
                    : 'border-slate-200 hover:border-brand-400 hover:bg-brand-50/40 hover:translate-x-1 hover:shadow-xs text-slateText-primary cursor-pointer active:scale-[0.99]'
                }`}
              >
                <div
                  className={`flex h-7 w-7 shrink-0 items-center justify-center rounded-xl text-xs font-bold transition-transform ${
                    isOptionSelected
                      ? isCurrentAnswered
                        ? currentItem.is_correct
                          ? 'bg-emerald-600 text-white shadow-xs'
                          : 'bg-rose-600 text-white shadow-xs'
                        : 'bg-brand-600 text-white shadow-xs scale-105'
                      : 'bg-slate-100 text-slateText-secondary'
                  }`}
                >
                  {opt.option_key}
                </div>
                <span className="flex-1 pt-0.5 leading-relaxed font-medium">{opt.option_text}</span>
              </button>
            );
          })}
        </div>

        {/* Submit Button (Only visible BEFORE answer is submitted) */}
        {!isCurrentAnswered && (
          <div className="mt-8 flex items-center justify-between border-t border-slate-100 pt-6">
            <span className="text-xs text-slateText-muted font-medium">
              Select an option above to submit your answer.
            </span>
            <button
              onClick={handleSubmitAnswer}
              disabled={!selectedOption || isSubmitting}
              className="inline-flex items-center gap-2 rounded-xl bg-brand-600 px-8 py-3 text-sm font-bold text-white shadow-sm hover:bg-brand-700 hover:shadow-md active:scale-[0.98] transition-all duration-150 disabled:opacity-40 cursor-pointer"
            >
              {isSubmitting ? 'Evaluating Logic...' : 'Submit & Understand Answer'}
            </button>
          </div>
        )}

        {/* FEEDBACK PANEL: Rendered immediately after submission */}
        {isCurrentAnswered && currentItem.feedback && (
          <FeedbackPanel
            feedback={currentItem.feedback}
            onNext={handleNextQuestion}
            isLastQuestion={currentIndex === session.questions.length - 1}
          />
        )}
      </div>

      {/* Finish Early Confirmation Modal */}
      {isConfirmingFinish && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/40 backdrop-blur-xs p-4">
          <div className="w-full max-w-md rounded-2xl bg-white p-6 shadow-xl space-y-4">
            <h3 className="text-base font-bold text-navy-800">Submit Assessment & View Report?</h3>
            <p className="text-xs text-slateText-secondary leading-relaxed">
              You have answered {session.completed_questions} of {session.total_questions} questions.
              {session.completed_questions < session.total_questions && (
                <span className="block mt-1 font-semibold text-amber-700">
                  {session.total_questions - session.completed_questions} questions remain unanswered!
                </span>
              )}
            </p>
            <div className="flex items-center justify-end gap-3 pt-3">
              <button
                onClick={() => setIsConfirmingFinish(false)}
                className="px-4 py-2 rounded-xl text-xs font-semibold text-slateText-secondary hover:bg-slate-100"
              >
                Continue Test
              </button>
              <button
                onClick={handleFinishEarly}
                className="px-5 py-2 rounded-xl text-xs font-bold text-white bg-brand-600 hover:bg-brand-700 shadow-sm"
              >
                Confirm & Submit
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Completion Summary Card (When all questions answered or test finished) */}
      {(session.completed_questions >= session.total_questions || session.status === 'completed') && (
        <div className="rounded-2xl border border-emerald-300 bg-white p-8 shadow-card text-center space-y-4 animate-fadeIn">
          <div className="flex h-16 w-16 mx-auto items-center justify-center rounded-full bg-emerald-100 text-emerald-700">
            <Trophy className="h-8 w-8" />
          </div>
          <h2 className="text-2xl font-bold text-navy-800">Placement Assessment Completed!</h2>
          <p className="text-sm text-slateText-secondary max-w-lg mx-auto">
            You scored <strong className="text-navy-800">{session.correct_count}</strong> out of{' '}
            <strong className="text-navy-800">{session.total_questions}</strong> (
            <span className="font-bold text-emerald-700">{session.score_percentage}% Accuracy</span>).
            Every attempted question and its detailed explanations are recorded in your history.
          </p>

          <div className="pt-4 flex flex-wrap items-center justify-center gap-3">
            <Link
              to="/app/aptitude"
              className="inline-flex items-center gap-2 rounded-xl bg-brand-600 px-6 py-2.5 text-sm font-semibold text-white shadow hover:bg-brand-700 transition-all"
            >
              <RotateCcw className="h-4 w-4" />
              Start Another Assessment
            </Link>
            <Link
              to="/app/dashboard"
              className="inline-flex items-center gap-2 rounded-xl border border-slate-300 bg-white px-5 py-2.5 text-sm font-semibold text-slateText-primary hover:bg-slate-50 transition-all"
            >
              Back to Dashboard
            </Link>
          </div>
        </div>
      )}
    </div>
  );
};
