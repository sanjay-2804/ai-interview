import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { api } from '../../services/api';
import { Mic, ArrowRight, Sparkles, Trophy, Clock, CheckCircle2, History } from 'lucide-react';

export const MockInterview: React.FC = () => {
  const navigate = useNavigate();
  const [category, setCategory] = useState<string>('Technical');
  const [difficulty, setDifficulty] = useState<string>('Medium');
  const [questionCount, setQuestionCount] = useState<number>(3);
  const [isStarting, setIsStarting] = useState<boolean>(false);
  const [history, setHistory] = useState<any[]>([]);
  const [loadingHistory, setLoadingHistory] = useState<boolean>(true);

  useEffect(() => {
    api.getInterviewHistory()
      .then(setHistory)
      .catch((err) => console.error('Failed to load interview history:', err))
      .finally(() => setLoadingHistory(false));
  }, []);

  const handleStartInterview = async () => {
    setIsStarting(true);
    try {
      const session = await api.startMockInterview({
        category,
        target_role: 'Software Developer',
        difficulty,
        question_count: questionCount,
      });
      navigate(`/app/interview/session/${session.id}`);
    } catch (err) {
      console.error('Failed to start interview:', err);
    } finally {
      setIsStarting(false);
    }
  };

  return (
    <div className="max-w-5xl mx-auto space-y-8 pb-16">
      {/* Header */}
      <div className="border-b border-surface-border pb-6">
        <div className="flex items-center gap-2 text-xs font-bold uppercase tracking-wider text-brand-600 mb-1">
          <Mic className="h-4 w-4" />
          <span>Real-Time Placement Simulation</span>
        </div>
        <h1 className="text-2xl sm:text-3xl font-extrabold text-navy-800 tracking-tight">
          Mock Interview Centre
        </h1>
        <p className="mt-2 text-sm text-slateText-secondary max-w-3xl leading-relaxed">
          Simulate real campus recruitment and technical screening rounds.
          Submit your conceptual reasoning or behavioral answers and receive rigorous feedback on missing concepts, structured delivery, and high-scoring sample responses.
        </p>
      </div>

      {/* Start Interview Setup Card */}
      <div className="rounded-2xl border border-brand-200 bg-white p-6 sm:p-8 lg:p-10 shadow-card">
        <h2 className="text-base font-bold text-navy-800 mb-6 border-b border-slate-100 pb-4">
          Configure Your Interview Round
        </h2>

        <div className="grid grid-cols-1 sm:grid-cols-3 gap-6">
          {/* Category */}
          <div>
            <label className="block text-xs font-bold uppercase tracking-wider text-slateText-secondary mb-2.5">
              Interview Track
            </label>
            <div className="space-y-2">
              {[
                { id: 'Technical', label: 'Technical Core (OS, DBMS, OOP, APIs)' },
                { id: 'DSA', label: 'DSA & Algorithmic Strategy' },
                { id: 'HR', label: 'HR & Behavioral (STAR Method)' },
              ].map((c) => (
                <button
                  key={c.id}
                  type="button"
                  onClick={() => setCategory(c.id)}
                  className={`w-full text-left p-3.5 sm:p-4 rounded-xl border text-xs font-semibold transition-all duration-150 cursor-pointer ${
                    category === c.id
                      ? 'border-2 border-brand-600 bg-brand-50 text-brand-900 shadow-2xs'
                      : 'border-slate-200 text-slateText-secondary hover:border-brand-300 hover:bg-slate-50/80 hover:translate-x-0.5'
                  }`}
                >
                  {c.label}
                </button>
              ))}
            </div>
          </div>

          {/* Difficulty */}
          <div>
            <label className="block text-xs font-bold uppercase tracking-wider text-slateText-secondary mb-2.5">
              Rigor Level
            </label>
            <div className="space-y-2">
              {[
                { id: 'Beginner', label: 'Campus Tier-1 (Standard Entry)' },
                { id: 'Medium', label: 'Product Tier (In-Depth Technical)' },
                { id: 'Hard', label: 'Top Tier (Edge Cases & Architecture)' },
              ].map((d) => (
                <button
                  key={d.id}
                  type="button"
                  onClick={() => setDifficulty(d.id)}
                  className={`w-full text-left p-3.5 sm:p-4 rounded-xl border text-xs font-semibold transition-all duration-150 cursor-pointer ${
                    difficulty === d.id
                      ? 'border-2 border-brand-600 bg-brand-50 text-brand-900 shadow-2xs'
                      : 'border-slate-200 text-slateText-secondary hover:border-brand-300 hover:bg-slate-50/80 hover:translate-x-0.5'
                  }`}
                >
                  {d.label}
                </button>
              ))}
            </div>
          </div>

          {/* Question Count */}
          <div>
            <label className="block text-xs font-bold uppercase tracking-wider text-slateText-secondary mb-2.5">
              Questions per Session
            </label>
            <div className="space-y-2">
              {[
                { count: 2, label: '2 Questions (Quick 10-Minute Drill)' },
                { count: 3, label: '3 Questions (Standard Screening)' },
                { count: 5, label: '5 Questions (Full Technical Round)' },
              ].map((qc) => (
                <button
                  key={qc.count}
                  type="button"
                  onClick={() => setQuestionCount(qc.count)}
                  className={`w-full text-left p-3.5 sm:p-4 rounded-xl border text-xs font-semibold transition-all duration-150 cursor-pointer ${
                    questionCount === qc.count
                      ? 'border-2 border-brand-600 bg-brand-50 text-brand-900 shadow-2xs'
                      : 'border-slate-200 text-slateText-secondary hover:border-brand-300 hover:bg-slate-50/80 hover:translate-x-0.5'
                  }`}
                >
                  {qc.label}
                </button>
              ))}
            </div>
          </div>
        </div>

        {/* Start Button */}
        <div className="mt-8 pt-6 border-t border-slate-100 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
          <div className="flex items-center gap-2 text-xs text-slateText-muted">
            <Sparkles className="h-4 w-4 text-brand-600 shrink-0" />
            <span>Honest evaluation engine: live AI when key is provided, deterministic rubrics otherwise.</span>
          </div>

          <button
            onClick={handleStartInterview}
            disabled={isStarting}
            className="inline-flex items-center justify-center gap-2 rounded-xl bg-brand-600 px-8 py-3 text-sm font-bold text-white shadow-sm hover:bg-brand-700 hover:shadow-md active:scale-[0.98] transition-all duration-150 disabled:opacity-50 cursor-pointer"
          >
            {isStarting ? 'Preparing Panel Questions...' : 'Start Mock Interview Session'}
            <ArrowRight className="h-4 w-4" />
          </button>
        </div>
      </div>

      {/* Past Interview History */}
      <div className="space-y-4">
        <div className="flex items-center gap-2 text-navy-800 font-bold text-base">
          <History className="h-4 w-4 text-brand-600" />
          <h2>Your Past Interview Sessions</h2>
        </div>

        {loadingHistory ? (
          <div className="text-xs text-slateText-muted py-4">Loading past sessions...</div>
        ) : history.length > 0 ? (
          <div className="divide-y divide-slate-100 rounded-2xl border border-surface-border bg-white shadow-subtle overflow-hidden">
            {history.map((s) => (
              <div key={s.id} className="p-4 sm:p-5 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
                <div>
                  <div className="flex items-center gap-2 mb-1">
                    <span className="text-xs font-bold text-navy-800">{s.category} Interview</span>
                    <span className="text-slate-300">•</span>
                    <span className="text-xs text-slateText-muted">{s.created_at}</span>
                  </div>
                  <p className="text-xs text-slateText-secondary max-w-xl">
                    {s.feedback_summary || `Completed ${s.completed_questions} of ${s.total_questions} questions.`}
                  </p>
                </div>

                <div className="flex items-center gap-4 shrink-0">
                  {s.overall_score && (
                    <div className="text-right">
                      <div className="text-xs text-slateText-muted uppercase">Readiness</div>
                      <div className="text-sm font-bold text-brand-700">{s.overall_score} / 10</div>
                    </div>
                  )}

                  <button
                    onClick={() => navigate(`/app/interview/session/${s.id}`)}
                    className="rounded-lg border border-slate-200 bg-white px-3 py-1.5 text-xs font-semibold text-slateText-primary hover:bg-slate-50"
                  >
                    View Report
                  </button>
                </div>
              </div>
            ))}
          </div>
        ) : (
          <div className="rounded-xl border border-slate-200 bg-white p-8 text-center text-xs text-slateText-muted">
            No interview sessions completed yet. Start your first session above!
          </div>
        )}
      </div>
    </div>
  );
};

