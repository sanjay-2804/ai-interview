import React, { useState, useEffect } from 'react';
import { api } from '../../services/api';
import { Shield, Users, HelpCircle, BarChart3, CheckCircle2, TrendingUp, Database } from 'lucide-react';
import { ResponsiveContainer, BarChart, Bar, XAxis, YAxis, Tooltip, Cell } from 'recharts';

export const AdminDashboard: React.FC = () => {
  const [analytics, setAnalytics] = useState<any>(null);
  const [loading, setLoading] = useState<boolean>(true);

  useEffect(() => {
    api.getAdminAnalytics()
      .then(setAnalytics)
      .catch((err) => console.error('Failed to load admin analytics:', err))
      .finally(() => setLoading(false));
  }, []);

  if (loading) {
    return (
      <div className="flex h-96 items-center justify-center">
        <div className="flex flex-col items-center gap-2">
          <div className="h-8 w-8 animate-spin rounded-full border-4 border-brand-600 border-t-transparent" />
          <p className="text-sm font-medium text-slateText-secondary">Loading platform analytics...</p>
        </div>
      </div>
    );
  }

  const chartData = analytics?.question_category_distribution || [];

  return (
    <div className="space-y-8 max-w-6xl mx-auto pb-12">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-surface-border pb-5">
        <div>
          <span className="text-xs font-bold uppercase tracking-wider text-brand-600">
            System Administration
          </span>
          <h1 className="text-2xl font-bold text-navy-800 mt-1">Platform Analytics & Health</h1>
        </div>
        <div className="flex items-center gap-2">
          <span className="bg-emerald-50 border border-emerald-200 text-emerald-700 text-xs px-3 py-1 rounded-full font-semibold flex items-center gap-1.5">
            <span className="h-2 w-2 rounded-full bg-emerald-500 animate-pulse" />
            Database Online & Connected
          </span>
        </div>
      </div>

      {/* KPI Stats Grid */}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
        <div className="rounded-2xl border border-surface-border bg-white p-6 shadow-card hover:-translate-y-1 hover:shadow-card-hover hover:border-brand-300 transition-all duration-200">
          <span className="text-xs font-bold text-slateText-muted uppercase tracking-wider">Total Students</span>
          <div className="mt-2.5 text-3xl sm:text-4xl font-extrabold text-navy-800">
            {analytics?.total_students || 0}
          </div>
          <p className="mt-1.5 text-xs text-slateText-secondary font-medium">Registered learners</p>
        </div>

        <div className="rounded-2xl border border-surface-border bg-white p-6 shadow-card hover:-translate-y-1 hover:shadow-card-hover hover:border-brand-300 transition-all duration-200">
          <span className="text-xs font-bold text-slateText-muted uppercase tracking-wider">Questions Attempted</span>
          <div className="mt-2.5 text-3xl sm:text-4xl font-extrabold text-brand-600">
            {analytics?.total_answers_submitted || 0}
          </div>
          <p className="mt-1.5 text-xs text-slateText-secondary font-medium">Student submissions</p>
        </div>

        <div className="rounded-2xl border border-surface-border bg-white p-6 shadow-card hover:-translate-y-1 hover:shadow-card-hover hover:border-emerald-300 transition-all duration-200">
          <span className="text-xs font-bold text-slateText-muted uppercase tracking-wider">Platform Accuracy</span>
          <div className="mt-2.5 text-3xl sm:text-4xl font-extrabold text-emerald-600">
            {analytics?.platform_average_accuracy || 0}%
          </div>
          <p className="mt-1.5 text-xs text-slateText-secondary font-medium">Average accuracy rate</p>
        </div>

        <div className="rounded-2xl border border-surface-border bg-white p-6 shadow-card hover:-translate-y-1 hover:shadow-card-hover hover:border-brand-300 transition-all duration-200">
          <span className="text-xs font-bold text-slateText-muted uppercase tracking-wider">Active Question Bank</span>
          <div className="mt-2.5 text-3xl sm:text-4xl font-extrabold text-navy-800">
            {analytics?.total_questions_in_bank || 0}
          </div>
          <p className="mt-1.5 text-xs text-slateText-secondary font-medium">Curated items</p>
        </div>
      </div>

      {/* Analytics Chart & Breakdown */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <div className="lg:col-span-2 rounded-2xl border border-surface-border bg-white p-6 shadow-subtle">
          <div className="flex items-center justify-between border-b border-slate-100 pb-4 mb-4">
            <div>
              <h2 className="text-base font-bold text-navy-800">Question Distribution by Category</h2>
              <p className="text-xs text-slateText-secondary">
                Breakdown of active assessment questions across modules.
              </p>
            </div>
          </div>

          <div className="h-64 w-full">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={chartData} margin={{ top: 10, right: 10, left: -20, bottom: 0 }}>
                <XAxis dataKey="category" stroke="#94A3B8" fontSize={11} tickLine={false} />
                <YAxis stroke="#94A3B8" fontSize={11} tickLine={false} axisLine={false} />
                <Tooltip
                  contentStyle={{
                    backgroundColor: '#FFFFFF',
                    border: '1px solid #E2E8F0',
                    borderRadius: '8px',
                    fontSize: '12px',
                    boxShadow: '0 4px 6px -1px rgba(0, 0, 0, 0.05)',
                  }}
                  cursor={{ fill: 'rgba(36, 87, 197, 0.04)' }}
                />
                <Bar dataKey="count" radius={[6, 6, 0, 0]}>
                  {chartData.map((_: any, index: number) => (
                    <Cell
                      key={`cell-${index}`}
                      fill={['#2457C5', '#10B981', '#F59E0B', '#8B5CF6'][index % 4]}
                    />
                  ))}
                </Bar>
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>

        {/* Database & Architecture Summary Card */}
        <div className="rounded-2xl border border-surface-border bg-white p-6 shadow-subtle space-y-4">
          <div className="border-b border-slate-100 pb-3">
            <h3 className="text-sm font-bold text-navy-800 flex items-center gap-2">
              <Database className="h-4 w-4 text-brand-600" />
              <span>Database Architecture</span>
            </h3>
            <p className="text-xs text-slateText-secondary mt-0.5">
              Production schema specifications.
            </p>
          </div>

          <div className="space-y-3 text-xs">
            <div className="flex items-center justify-between py-1.5 border-b border-slate-50">
              <span className="text-slateText-secondary font-medium">ORM Framework</span>
              <span className="font-semibold text-navy-800">SQLAlchemy 2.0</span>
            </div>
            <div className="flex items-center justify-between py-1.5 border-b border-slate-50">
              <span className="text-slateText-secondary font-medium">Migration Engine</span>
              <span className="font-semibold text-navy-800">Alembic 1.20</span>
            </div>
            <div className="flex items-center justify-between py-1.5 border-b border-slate-50">
              <span className="text-slateText-secondary font-medium">Session Security</span>
              <span className="font-semibold text-emerald-700">HttpOnly + SHA-256</span>
            </div>
            <div className="flex items-center justify-between py-1.5 border-b border-slate-50">
              <span className="text-slateText-secondary font-medium">Role Access Level</span>
              <span className="font-semibold text-brand-700">Platform Administrator</span>
            </div>
            <div className="flex items-center justify-between py-1.5">
              <span className="text-slateText-secondary font-medium">API Documentation</span>
              <a
                href="/docs"
                target="_blank"
                rel="noreferrer"
                className="font-bold text-brand-600 hover:underline"
              >
                /docs (OpenAPI)
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
