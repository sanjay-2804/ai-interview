import React, { useState, useEffect } from 'react';
import { useParams, useNavigate, Link } from 'react-router-dom';
import { api } from '../../services/api';
import { MockInterviewDetail } from '../../types';
import {
  ArrowLeft, ArrowRight, Mic, Sparkles, CheckCircle2, AlertCircle,
  Trophy, ThumbsUp, AlertTriangle, Lightbulb, BookOpen
} from 'lucide-react';

export const InterviewSessionRunner: React.FC = () => {
  const { sessionId } = useParams<{ sessionId: string }>();
  const navigate = useNavigate();

  const [session, setSession] = useState<MockInterviewDetail | null>(null);
  const [responseText, setResponseText] = useState<string>('');
  const [isSubmitting, setIsSubmitting] = useState<boolean>(false);
  const [errorMsg, setErrorMsg] = useState<string | null>(null);
  const [loading, setLoading] = useState<boolean>(true);

  const loadInterview = async () => {
    if (!sessionId) return;
    try {
      const data = await api.getMockInterview(parseInt(sessionId, 10));
      setSession(data);
    } catch (err: any) {
      setErrorMsg(err.message || 'Failed to load interview session.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadInterview();
  }, [sessionId]);

  const handleSubmitResponse = async () => {
    if (!session || !responseText.trim() || isSubmitting) return;
    setIsSubmitting(true);
    setErrorMsg(null);
    try {
      const updated = await api.submitMockInterviewResponse({
        session_id: session.id,
        response_text: responseText,
      });
      setSession(updated);
      setResponseText('');
    } catch (err: any) {
      setErrorMsg(err.message || 'Failed to evaluate response.');
    } finally {
      setIsSubmitting(false);
    }
  };

  if (loading) {
    return (
      <div className="flex h-96 items-center justify-center">
        <div className="h-8 w-8 animate-spin rounded-full border-4 border-brand-600 border-t-transparent" />
      </div>
    );
  }

  if (errorMsg || !session) {
    return (
      <div className="max-w-xl mx-auto mt-12 rounded-2xl border border-rose-200 bg-white p-8 text-center shadow-subtle">
        <AlertCircle className="mx-auto h-12 w-12 text-rose-500 mb-3" />
        <h2 className="text-lg font-bold text-navy-800">Unable to Load Interview</h2>
        <p className="mt-1 text-sm text-slateText-secondary">{errorMsg || 'Session not found.'}</p>
        <Link
          to="/app/interview"
          className="mt-6 inline-flex items-center gap-2 rounded-lg bg-brand-600 px-5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-brand-700"
        >
          <ArrowLeft className="h-4 w-4" />
          Back to Interview Center
        </Link>
      </div>
    );
  }

  const isCompleted = session.status === 'completed';

  return (
    <div className="max-w-4xl mx-auto space-y-6 pb-20">
      {/* Top Header */}
      <div className="flex items-center justify-between border-b border-surface-border pb-4">
        <Link
          to="/app/interview"
          className="inline-flex items-center gap-2 text-xs font-semibold text-slateText-secondary hover:text-brand-600 transition-all hover:-translate-x-0.5 group"
        >
          <ArrowLeft className="h-4 w-4 transition-transform group-hover:-translate-x-1" />
          Exit Interview Room
        </Link>

        <div className="flex items-center gap-2">
          <span className="text-xs font-bold text-brand-600 uppercase bg-brand-50 px-2.5 py-1 rounded-full border border-brand-200">
            {session.category} Mock Interview
          </span>
          <span className="text-slate-300">•</span>
          <span className="text-xs font-semibold text-slateText-secondary">
            Question {Math.min(session.completed_questions + (isCompleted ? 0 : 1), session.total_questions)} of {session.total_questions}
          </span>
        </div>
      </div>

      {/* FINAL REPORT VIEW WHEN COMPLETED */}
      {isCompleted ? (
        <div className="space-y-6">
          <div className="rounded-2xl border border-emerald-300 bg-white p-8 text-center shadow-card space-y-3">
            <div className="flex h-16 w-16 mx-auto items-center justify-center rounded-full bg-emerald-100 text-emerald-700">
              <Trophy className="h-8 w-8" />
            </div>
            <h1 className="text-2xl font-extrabold text-navy-800">
              Mock Interview Round Completed
            </h1>
            <p className="text-sm text-slateText-secondary max-w-xl mx-auto">
              {session.feedback_summary}
            </p>

            {session.overall_score && (
              <div className="inline-block bg-brand-50 border border-brand-200 rounded-xl px-6 py-2.5 mt-2">
                <span className="text-xs text-slateText-muted uppercase font-bold">Overall Score</span>
                <div className="text-3xl font-black text-brand-700">{session.overall_score} / 10</div>
              </div>
            )}
          </div>

          {/* Detailed Question Review */}
          <div className="space-y-4">
            <h3 className="text-base font-bold text-navy-800">Detailed Question-by-Question Evaluation</h3>
            {session.responses.map((resp, idx) => (
              <div
                key={resp.id}
                className="rounded-2xl border border-surface-border bg-white p-6 sm:p-7 shadow-card hover:border-brand-300 hover:shadow-card-hover transition-all duration-200 space-y-4"
              >
                <div className="flex items-start justify-between gap-4 border-b border-slate-100 pb-3">
                  <div>
                    <span className="text-[10px] font-bold uppercase tracking-wider text-brand-600 bg-brand-50 px-2 py-0.5 rounded border border-brand-200">
                      Question {idx + 1}
                    </span>
                    <h4 className="text-sm font-bold text-navy-800 mt-1">{resp.question_text}</h4>
                  </div>
                  <div className="text-right shrink-0">
                    <span className="text-sm font-extrabold text-brand-700 bg-brand-50 px-2.5 py-1 rounded-lg border border-brand-200">
                      {resp.score} / 10
                    </span>
                  </div>
                </div>

                <div className="space-y-3.5 text-xs leading-relaxed">
                  <div>
                    <span className="font-bold text-slateText-muted block mb-1">Your Response:</span>
                    <p className="text-slateText-primary bg-slate-50 p-4 rounded-xl border border-slate-200 leading-relaxed font-medium">
                      {resp.student_response}
                    </p>
                  </div>

                  <div className="grid grid-cols-1 md:grid-cols-2 gap-3.5 pt-1">
                    <div className="rounded-xl bg-emerald-50/60 border border-emerald-200 p-4">
                      <span className="font-bold text-emerald-800 flex items-center gap-1.5 mb-2">
                        <ThumbsUp className="h-4 w-4" /> Strengths
                      </span>
                      <ul className="list-disc list-inside space-y-1 text-emerald-950 font-medium">
                        {resp.strengths.map((s, i) => <li key={i}>{s}</li>)}
                      </ul>
                    </div>

                    <div className="rounded-xl bg-amber-50/60 border border-amber-200 p-4">
                      <span className="font-bold text-amber-800 flex items-center gap-1.5 mb-2">
                        <AlertTriangle className="h-4 w-4" /> Missing Concepts
                      </span>
                      <ul className="list-disc list-inside space-y-1 text-amber-950 font-medium">
                        {resp.missing_concepts.map((m, i) => <li key={i}>{m}</li>)}
                      </ul>
                    </div>
                  </div>

                  <div className="rounded-xl bg-blue-50/60 border border-blue-200 p-4">
                    <span className="font-bold text-brand-800 flex items-center gap-1.5 mb-1.5">
                      <BookOpen className="h-4 w-4" /> Reference High-Scoring Response
                    </span>
                    <p className="text-slateText-primary leading-relaxed font-medium">{resp.sample_answer}</p>
                  </div>
                </div>
              </div>
            ))}
          </div>

          <div className="text-center pt-6">
            <Link
              to="/app/interview"
              className="inline-flex items-center gap-2 rounded-xl bg-brand-600 px-7 py-3 text-xs font-bold text-white shadow-sm hover:bg-brand-700 hover:shadow-md active:scale-[0.98] transition-all"
            >
              Start Another Interview Session
            </Link>
          </div>
        </div>
      ) : (
        /* ACTIVE QUESTION WORKSPACE */
        <div className="space-y-6">
          <div className="rounded-2xl border border-surface-border bg-white p-7 sm:p-9 shadow-card space-y-5">
            <div className="flex items-center justify-between">
              <span className="text-xs font-bold uppercase tracking-wider text-brand-600 bg-brand-50 px-3 py-1 rounded-full border border-brand-200">
                Current Question
              </span>
              <span className="text-xs text-slateText-muted">
                Engine: <strong className="text-slateText-primary font-bold">InterviewAI Placement Evaluator</strong>
              </span>
            </div>

            <h3 className="text-xl font-extrabold text-navy-800 leading-relaxed">
              {session.current_question_text}
            </h3>

            {/* Answer Input */}
            <div className="pt-2">
              <label className="block text-xs font-bold uppercase tracking-wider text-slateText-secondary mb-2.5">
                Your Articulated Response
              </label>
              <textarea
                value={responseText}
                onChange={(e) => setResponseText(e.target.value)}
                rows={6}
                placeholder="Type your response clearly. For technical questions, define terms and explain mechanisms; for behavioral questions, follow the STAR approach (Situation, Task, Action, Result)..."
                className="w-full rounded-2xl border border-slate-300 p-5 text-sm text-slateText-primary focus:border-brand-600 focus:outline-none focus:ring-2 focus:ring-brand-500/20 leading-relaxed shadow-xs transition-all"
              />
            </div>

            <div className="flex items-center justify-between pt-2">
              <span className="text-xs font-medium text-slateText-muted">
                Word count: {responseText.trim().split(/\s+/).filter(Boolean).length} words
              </span>

              <button
                onClick={handleSubmitResponse}
                disabled={!responseText.trim() || isSubmitting}
                className="inline-flex items-center gap-2 rounded-xl bg-brand-600 px-7 py-3 text-xs font-bold text-white shadow-sm hover:bg-brand-700 hover:shadow-md active:scale-[0.98] disabled:opacity-40 transition-all cursor-pointer"
              >
                {isSubmitting ? 'Evaluating Response...' : 'Submit & Analyze Response'}
                <ArrowRight className="h-4 w-4" />
              </button>
            </div>
          </div>

          {/* Past answered questions in this session */}
          {session.responses.length > 0 && (
            <div className="space-y-4 pt-4 border-t border-slate-200">
              <h4 className="text-xs font-bold uppercase tracking-wider text-slateText-secondary">
                Evaluated in this session ({session.responses.length})
              </h4>
              {session.responses.map((r, i) => (
                <div key={r.id} className="rounded-xl border border-slate-200 bg-white p-4 text-xs space-y-2">
                  <div className="flex justify-between font-bold text-navy-800">
                    <span>Q{i + 1}: {r.question_text}</span>
                    <span className="text-brand-700">{r.score} / 10</span>
                  </div>
                  <div className="text-slateText-muted">
                    <strong className="text-emerald-700">Strength: </strong>
                    {r.strengths[0] || 'Good effort.'}
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      )}
    </div>
  );
};

