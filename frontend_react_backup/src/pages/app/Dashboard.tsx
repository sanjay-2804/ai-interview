import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from '../../context/AuthContext';
import { api } from '../../services/api';
import { DashboardStats } from '../../types';
import {
  CheckCircle, Flame, Target, BookOpen, Code2, Mic, ArrowRight,
  TrendingUp, AlertTriangle, Sparkles, Clock, Calendar, BarChart2
} from 'lucide-react';
import { ResponsiveContainer, BarChart, Bar, XAxis, YAxis, Tooltip, Cell } from 'recharts';

export const Dashboard: React.FC = () => {
  const { user } = useAuth();
  const [stats, setStats] = useState<DashboardStats | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    api.getDashboardStats()
      .then(setStats)
      .catch((err) => console.error('Failed to load dashboard statistics:', err))
      .finally(() => setLoading(false));
  }, []);

  if (loading) {
    return (
      <div className="flex h-96 items-center justify-center">
        <div className="flex flex-col items-center gap-2">
          <div className="h-8 w-8 animate-spin rounded-full border-4 border-brand-600 border-t-transparent" />
          <p className="text-sm text-slateText-secondary">Calculating your placement progress...</p>
        </div>
      </div>
    );
  }

  const hasActivity = (stats?.total_questions_attempted || 0) > 0 || (stats?.total_lessons_completed || 0) > 0;

  const chartData = [
    { name: 'Questions', value: stats?.total_questions_attempted || 0, color: '#2457C5' },
    { name: 'Lessons', value: stats?.total_lessons_completed || 0, color: '#10B981' },
    { name: 'Coding', value: stats?.total_coding_solved || 0, color: '#F59E0B' },
    { name: 'Interviews', value: stats?.total_mock_interviews || 0, color: '#8B5CF6' },
  ];

  return (
    <div className="space-y-8 max-w-7xl mx-auto pb-12">
      {/* Welcome Banner */}
      <div className="rounded-2xl bg-gradient-to-r from-brand-700 via-brand-600 to-brand-800 p-6 sm:p-8 text-white shadow-card">
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-6">
          <div>
            <div className="inline-flex items-center gap-2 rounded-full bg-white/20 px-3 py-1 text-xs font-semibold backdrop-blur-md mb-2">
              <Sparkles className="h-3.5 w-3.5" />
              <span>Target Career Role: {stats?.target_role}</span>
            </div>
            <h1 className="text-2xl sm:text-3xl font-extrabold tracking-tight">
              Welcome back, {user?.full_name?.split(' ')[0]}!
            </h1>
            <p className="mt-2 text-sm text-brand-100 max-w-2xl leading-relaxed">
              Your preparation roadmap is calibrated for {stats?.target_role} ({stats?.skill_level} track).
              Focus on conceptual mastery: understand why every correct answer is right and why false options fail.
            </p>
          </div>

          <div className="flex items-center gap-3 shrink-0">
            <Link
              to="/app/aptitude"
              className="inline-flex items-center gap-2 rounded-xl bg-white px-5 py-3 text-sm font-bold text-brand-700 shadow-sm hover:bg-brand-50 transition-all"
            >
              Start Practice Session
              <ArrowRight className="h-4 w-4" />
            </Link>
          </div>
        </div>
      </div>

      {/* Primary KPI Metrics Grid */}
      <div className="grid grid-cols-2 lg:grid-cols-5 gap-4 sm:gap-5">
        {/* Questions Attempted */}
        <div className="rounded-2xl border border-surface-border bg-white p-5 sm:p-6 shadow-subtle hover:-translate-y-1 hover:shadow-card-hover hover:border-brand-200 transition-all duration-200 cursor-default">
          <div className="flex items-center justify-between">
            <span className="text-xs font-bold text-slateText-secondary uppercase tracking-wider">Questions</span>
            <div className="flex h-8 w-8 items-center justify-center rounded-lg bg-brand-50 text-brand-600">
              <Target className="h-4 w-4" />
            </div>
          </div>
          <div className="mt-3">
            <span className="text-2xl sm:text-3xl font-extrabold text-navy-800">{stats?.total_questions_attempted}</span>
            <span className="text-xs text-slateText-muted ml-1.5 font-medium">attempted</span>
          </div>
          <div className="mt-2.5 text-xs font-medium text-slateText-secondary pt-2 border-t border-slate-50">
            Accuracy: <strong className="text-brand-700">{stats?.overall_accuracy_percentage}%</strong>
          </div>
        </div>

        {/* Coding Solved */}
        <div className="rounded-2xl border border-surface-border bg-white p-5 sm:p-6 shadow-subtle hover:-translate-y-1 hover:shadow-card-hover hover:border-amber-200 transition-all duration-200 cursor-default">
          <div className="flex items-center justify-between">
            <span className="text-xs font-bold text-slateText-secondary uppercase tracking-wider">Coding</span>
            <div className="flex h-8 w-8 items-center justify-center rounded-lg bg-amber-50 text-amber-600">
              <Code2 className="h-4 w-4" />
            </div>
          </div>
          <div className="mt-3">
            <span className="text-2xl sm:text-3xl font-extrabold text-navy-800">{stats?.total_coding_solved}</span>
            <span className="text-xs text-slateText-muted ml-1.5 font-medium">solved</span>
          </div>
          <div className="mt-2.5 text-xs font-medium text-slateText-secondary pt-2 border-t border-slate-50">
            Algorithmic patterns
          </div>
        </div>

        {/* Lessons Completed */}
        <div className="rounded-2xl border border-surface-border bg-white p-5 sm:p-6 shadow-subtle hover:-translate-y-1 hover:shadow-card-hover hover:border-emerald-200 transition-all duration-200 cursor-default">
          <div className="flex items-center justify-between">
            <span className="text-xs font-bold text-slateText-secondary uppercase tracking-wider">Lessons</span>
            <div className="flex h-8 w-8 items-center justify-center rounded-lg bg-emerald-50 text-emerald-600">
              <BookOpen className="h-4 w-4" />
            </div>
          </div>
          <div className="mt-3">
            <span className="text-2xl sm:text-3xl font-extrabold text-navy-800">{stats?.total_lessons_completed}</span>
            <span className="text-xs text-slateText-muted ml-1.5 font-medium">completed</span>
          </div>
          <div className="mt-2.5 text-xs font-medium text-slateText-secondary pt-2 border-t border-slate-50">
            Technical foundation
          </div>
        </div>

        {/* Mock Interviews */}
        <div className="rounded-2xl border border-surface-border bg-white p-5 sm:p-6 shadow-subtle hover:-translate-y-1 hover:shadow-card-hover hover:border-purple-200 transition-all duration-200 cursor-default">
          <div className="flex items-center justify-between">
            <span className="text-xs font-bold text-slateText-secondary uppercase tracking-wider">Interviews</span>
            <div className="flex h-8 w-8 items-center justify-center rounded-lg bg-purple-50 text-purple-600">
              <Mic className="h-4 w-4" />
            </div>
          </div>
          <div className="mt-3">
            <span className="text-2xl sm:text-3xl font-extrabold text-navy-800">{stats?.total_mock_interviews}</span>
            <span className="text-xs text-slateText-muted ml-1.5 font-medium">rounds</span>
          </div>
          <div className="mt-2.5 text-xs font-medium text-slateText-secondary pt-2 border-t border-slate-50">
            Technical & Behavioral
          </div>
        </div>

        {/* Learning Streak */}
        <div className="rounded-2xl border border-surface-border bg-white p-5 sm:p-6 shadow-subtle col-span-2 lg:col-span-1 hover:-translate-y-1 hover:shadow-card-hover hover:border-orange-200 transition-all duration-200 cursor-default">
          <div className="flex items-center justify-between">
            <span className="text-xs font-bold text-slateText-secondary uppercase tracking-wider">Active Streak</span>
            <div className="flex h-8 w-8 items-center justify-center rounded-lg bg-orange-50 text-orange-500">
              <Flame className="h-4 w-4 animate-pulse" />
            </div>
          </div>
          <div className="mt-3">
            <span className="text-2xl sm:text-3xl font-extrabold text-navy-800">{stats?.streak_days}</span>
            <span className="text-xs text-slateText-muted ml-1.5 font-medium">days</span>
          </div>
          <div className="mt-2.5 text-xs font-medium text-slateText-secondary pt-2 border-t border-slate-50">
            {stats?.streak_days ? 'Daily consistency recorded' : 'Practice today to begin'}
          </div>
        </div>
      </div>

      {/* Main Grid: Recommended Actions & Analytics Overview */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Next Recommended Learning Activities */}
        <div className="lg:col-span-2 space-y-6">
          <div className="rounded-2xl border border-surface-border bg-white p-6 sm:p-7 shadow-subtle">
            <div className="flex items-center justify-between border-b border-slate-100 pb-4 mb-5">
              <div>
                <h2 className="text-base font-bold text-navy-800">Recommended Next Steps</h2>
                <p className="text-xs text-slateText-secondary mt-0.5">
                  Dynamically adjusted based on your assessed strengths and accuracy.
                </p>
              </div>
              <span className="text-[11px] font-bold text-brand-700 bg-brand-50 border border-brand-200 px-2.5 py-1 rounded-full uppercase tracking-wider">
                Personalized
              </span>
            </div>

            <div className="space-y-3.5">
              {stats?.recommended_activities?.map((item, idx) => (
                <div
                  key={idx}
                  className="flex items-center justify-between p-4 sm:p-5 rounded-xl border border-slate-200 bg-white hover:border-brand-300 hover:shadow-xs hover:bg-brand-50/30 transition-all duration-200 group cursor-pointer"
                >
                  <div className="space-y-1.5">
                    <div className="flex items-center gap-2">
                      <span className="text-[10px] font-bold uppercase px-2.5 py-0.5 rounded-full bg-brand-100 text-brand-800 border border-brand-200/60">
                        {item.category}
                      </span>
                      <h4 className="text-sm font-bold text-navy-800 group-hover:text-brand-700 transition-colors">
                        {item.title}
                      </h4>
                    </div>
                    <p className="text-xs text-slateText-secondary leading-relaxed">{item.action}</p>
                  </div>
                  <Link
                    to={item.link}
                    className="shrink-0 flex h-9 w-9 items-center justify-center rounded-xl bg-slate-50 border border-slate-200 text-slateText-secondary group-hover:bg-brand-600 group-hover:text-white group-hover:border-brand-600 shadow-2xs group-hover:scale-105 active:scale-95 transition-all duration-150 ml-3"
                  >
                    <ArrowRight className="h-4 w-4" />
                  </Link>
                </div>
              ))}
            </div>
          </div>

          {/* Weak Topics & Strong Topics Analysis */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {/* Weak Topics */}
            <div className="rounded-xl border border-rose-200 bg-rose-50/30 p-5">
              <div className="flex items-center gap-2 text-rose-800 mb-3">
                <AlertTriangle className="h-4 w-4 text-rose-600" />
                <h3 className="text-sm font-bold uppercase tracking-wider">Areas for Growth</h3>
              </div>
              {stats?.weak_topics && stats.weak_topics.length > 0 ? (
                <ul className="space-y-2.5">
                  {stats.weak_topics.map((t, i) => (
                    <li key={i} className="flex items-center justify-between text-xs bg-white p-2.5 rounded-lg border border-rose-100">
                      <span className="font-medium text-slateText-primary">{t.topic}</span>
                      <span className="font-bold text-rose-600">{t.accuracy}% Accuracy</span>
                    </li>
                  ))}
                </ul>
              ) : (
                <p className="text-xs text-slateText-muted leading-relaxed">
                  No weak topics identified yet. Complete additional practice sessions to detect concept gaps.
                </p>
              )}
            </div>

            {/* Strong Topics */}
            <div className="rounded-xl border border-emerald-200 bg-emerald-50/30 p-5">
              <div className="flex items-center gap-2 text-emerald-800 mb-3">
                <CheckCircle className="h-4 w-4 text-emerald-600" />
                <h3 className="text-sm font-bold uppercase tracking-wider">Demonstrated Strengths</h3>
              </div>
              {stats?.strong_topics && stats.strong_topics.length > 0 ? (
                <ul className="space-y-2.5">
                  {stats.strong_topics.map((t, i) => (
                    <li key={i} className="flex items-center justify-between text-xs bg-white p-2.5 rounded-lg border border-emerald-100">
                      <span className="font-medium text-slateText-primary">{t.topic}</span>
                      <span className="font-bold text-emerald-700">{t.accuracy}% Accuracy</span>
                    </li>
                  ))}
                </ul>
              ) : (
                <p className="text-xs text-slateText-muted leading-relaxed">
                  Practice questions to identify topics where your accuracy consistently exceeds 75%.
                </p>
              )}
            </div>
          </div>
        </div>

        {/* Right Sidebar: Activity Chart & Recent Logs */}
        <div className="space-y-6">
          {/* Activity Breakdown Chart */}
          <div className="rounded-2xl border border-surface-border bg-white p-6 shadow-subtle">
            <h3 className="text-sm font-bold text-navy-800 mb-1">Preparation Breakdown</h3>
            <p className="text-xs text-slateText-muted mb-4">Milestones recorded in database</p>
            <div className="h-48 w-full">
              <ResponsiveContainer width="100%" height="100%">
                <BarChart data={chartData} margin={{ top: 10, right: 10, left: -25, bottom: 0 }}>
                  <XAxis dataKey="name" tick={{ fontSize: 11, fill: '#526179' }} />
                  <YAxis tick={{ fontSize: 11, fill: '#526179' }} />
                  <Tooltip
                    contentStyle={{ backgroundColor: '#FFFFFF', borderRadius: '8px', border: '1px solid #E2E8F0', fontSize: '12px' }}
                  />
                  <Bar dataKey="value" radius={[4, 4, 0, 0]}>
                    {chartData.map((entry, index) => (
                      <Cell key={`cell-${index}`} fill={entry.color} />
                    ))}
                  </Bar>
                </BarChart>
              </ResponsiveContainer>
            </div>
          </div>

          {/* Recent Activity Log */}
          <div className="rounded-2xl border border-surface-border bg-white p-6 shadow-subtle">
            <h3 className="text-sm font-bold text-navy-800 mb-3">Recent Activity</h3>
            {stats?.recent_activities && stats.recent_activities.length > 0 ? (
              <div className="space-y-3">
                {stats.recent_activities.map((a) => (
                  <div key={a.id} className="border-l-2 border-brand-500 pl-3 py-1 text-xs">
                    <p className="font-semibold text-slateText-primary">{a.title}</p>
                    {a.details && <p className="text-slateText-secondary">{a.details}</p>}
                    <span className="text-[10px] text-slateText-muted">{a.time}</span>
                  </div>
                ))}
              </div>
            ) : (
              <div className="text-center py-6 text-xs text-slateText-muted">
                No recent activity recorded yet. Start your first session!
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

