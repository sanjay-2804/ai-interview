import React, { useState, useEffect } from 'react';
import { api } from '../../services/api';
import { DashboardStats } from '../../types';
import {
  BarChart3, TrendingUp, CheckCircle, Flame, Target,
  BookOpen, Code2, Mic, AlertCircle, ArrowRight
} from 'lucide-react';
import { ResponsiveContainer, BarChart, Bar, XAxis, YAxis, Tooltip, Cell } from 'recharts';

export const ProgressAnalytics: React.FC = () => {
  const [stats, setStats] = useState<DashboardStats | null>(null);
  const [loading, setLoading] = useState<boolean>(true);

  useEffect(() => {
    api.getDashboardStats()
      .then(setStats)
      .catch((err) => console.error('Failed to load stats:', err))
      .finally(() => setLoading(false));
  }, []);

  if (loading) {
    return (
      <div className="flex h-96 items-center justify-center">
        <div className="h-8 w-8 animate-spin rounded-full border-4 border-brand-600 border-t-transparent" />
      </div>
    );
  }

  const topicAccuracyData = [
    ...(stats?.strong_topics || []).map((t) => ({ name: t.topic, accuracy: t.accuracy, fill: '#10B981' })),
    ...(stats?.weak_topics || []).map((t) => ({ name: t.topic, accuracy: t.accuracy, fill: '#F43F5E' })),
  ];

  return (
    <div className="max-w-5xl mx-auto space-y-8 pb-16">
      {/* Header */}
      <div className="border-b border-surface-border pb-6">
        <div className="flex items-center gap-2 text-xs font-bold uppercase tracking-wider text-brand-600 mb-1">
          <BarChart3 className="h-4 w-4" />
          <span>Real-Time Performance Diagnostics</span>
        </div>
        <h1 className="text-2xl sm:text-3xl font-extrabold text-navy-800 tracking-tight">
          My Progress & Assessment Scores
        </h1>
        <p className="mt-2 text-sm text-slateText-secondary max-w-3xl leading-relaxed">
          Aggregated performance data based entirely on your recorded attempts.
          We identify concept gaps and track learning consistency without fabricated stats.
        </p>
      </div>

      {/* KPI Cards */}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
        <div className="rounded-2xl border border-surface-border bg-white p-6 shadow-card hover:-translate-y-1 hover:shadow-card-hover hover:border-brand-300 transition-all duration-200">
          <span className="text-xs font-bold text-slateText-muted uppercase tracking-wider">Overall Accuracy</span>
          <div className="mt-2.5 text-3xl sm:text-4xl font-extrabold text-brand-700">
            {stats?.overall_accuracy_percentage}%
          </div>
          <p className="mt-1.5 text-xs text-slateText-secondary font-medium">
            {stats?.total_questions_attempted} total questions
          </p>
        </div>

        <div className="rounded-2xl border border-surface-border bg-white p-6 shadow-card hover:-translate-y-1 hover:shadow-card-hover hover:border-amber-300 transition-all duration-200">
          <span className="text-xs font-bold text-slateText-muted uppercase tracking-wider">Coding Solved</span>
          <div className="mt-2.5 text-3xl sm:text-4xl font-extrabold text-amber-600">
            {stats?.total_coding_solved}
          </div>
          <p className="mt-1.5 text-xs text-slateText-secondary font-medium">Distinct problems passed</p>
        </div>

        <div className="rounded-2xl border border-surface-border bg-white p-6 shadow-card hover:-translate-y-1 hover:shadow-card-hover hover:border-emerald-300 transition-all duration-200">
          <span className="text-xs font-bold text-slateText-muted uppercase tracking-wider">Lessons Completed</span>
          <div className="mt-2.5 text-3xl sm:text-4xl font-extrabold text-emerald-600">
            {stats?.total_lessons_completed}
          </div>
          <p className="mt-1.5 text-xs text-slateText-secondary font-medium">Concepts mastered</p>
        </div>

        <div className="rounded-2xl border border-surface-border bg-white p-6 shadow-card hover:-translate-y-1 hover:shadow-card-hover hover:border-orange-300 transition-all duration-200">
          <span className="text-xs font-bold text-slateText-muted uppercase tracking-wider">Active Streak</span>
          <div className="mt-2.5 text-3xl sm:text-4xl font-extrabold text-orange-600 flex items-center gap-1.5">
            <Flame className="h-7 w-7 text-orange-500 fill-orange-100" />
            <span>{stats?.streak_days} Days</span>
          </div>
          <p className="mt-1.5 text-xs text-slateText-secondary font-medium">Consecutive study days</p>
        </div>
      </div>

      {/* Topic Accuracy Breakdown Chart */}
      <div className="rounded-2xl border border-surface-border bg-white p-7 sm:p-9 shadow-card space-y-4">
        <div>
          <h2 className="text-lg font-extrabold text-navy-800">Topic-Wise Assessment Accuracy</h2>
          <p className="text-xs text-slateText-secondary mt-0.5 font-medium">
            Performance comparison across quantitative, logical, and technical modules.
          </p>
        </div>

        {topicAccuracyData.length > 0 ? (
          <div className="h-64 w-full pt-4">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={topicAccuracyData} margin={{ top: 10, right: 20, left: -10, bottom: 20 }}>
                <XAxis dataKey="name" tick={{ fontSize: 11, fill: '#526179' }} interval={0} angle={-15} textAnchor="end" />
                <YAxis domain={[0, 100]} tick={{ fontSize: 11, fill: '#526179' }} />
                <Tooltip
                  formatter={(val: any) => [`${val}%`, 'Accuracy']}
                  contentStyle={{ backgroundColor: '#FFFFFF', borderRadius: '12px', border: '1px solid #E2E8F0', fontSize: '12px', boxShadow: '0 4px 6px -1px rgba(0, 0, 0, 0.05)' }}
                />
                <Bar dataKey="accuracy" radius={[6, 6, 0, 0]}>
                  {topicAccuracyData.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={entry.fill} />
                  ))}
                </Bar>
              </BarChart>
            </ResponsiveContainer>
          </div>
        ) : (
          <div className="rounded-2xl border border-dashed border-slate-200 p-10 text-center text-xs text-slateText-muted">
            Complete at least 2 practice sessions to render topic accuracy diagnostics.
          </div>
        )}
      </div>

      {/* Actionable Next Steps */}
      <div className="rounded-2xl border border-brand-200 bg-brand-50/50 p-7 sm:p-8 shadow-card space-y-3">
        <h3 className="text-base font-bold text-brand-900">Recommended Focus for Your Next Session</h3>
        <p className="text-xs text-slateText-secondary leading-relaxed font-medium">
          {stats?.weak_topics && stats.weak_topics.length > 0 ? (
            <>
              You are currently performing well in your strong topics. Focus your next 30 minutes on{' '}
              <strong className="text-slateText-primary font-bold">{stats.weak_topics[0].topic}</strong>, where your accuracy is{' '}
              <strong className="text-rose-600 font-bold">{stats.weak_topics[0].accuracy}%</strong>.
            </>
          ) : (
            'Complete your foundational lessons in Data Structures & Aptitude to establish your personalized accuracy curve.'
          )}
        </p>
      </div>
    </div>
  );
};

