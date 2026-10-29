import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { api } from '../../services/api';
import { CodingProblemListOut } from '../../types';
import { Code2, ExternalLink, CheckCircle2, ArrowRight, Filter, Search } from 'lucide-react';

export const CodingPractice: React.FC = () => {
  const [problems, setProblems] = useState<CodingProblemListOut[]>([]);
  const [difficultyFilter, setDifficultyFilter] = useState<string>('all');
  const [categoryFilter, setCategoryFilter] = useState<string>('all');
  const [searchTerm, setSearchTerm] = useState<string>('');
  const [loading, setLoading] = useState<boolean>(true);

  useEffect(() => {
    api.getCodingProblems(
      difficultyFilter === 'all' ? undefined : difficultyFilter,
      categoryFilter === 'all' ? undefined : categoryFilter
    )
      .then(setProblems)
      .catch((err) => console.error('Failed to load coding problems:', err))
      .finally(() => setLoading(false));
  }, [difficultyFilter, categoryFilter]);

  const filteredProblems = problems.filter((p) =>
    p.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
    p.category.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div className="max-w-6xl mx-auto space-y-8 pb-16">
      {/* Header */}
      <div className="border-b border-surface-border pb-6">
        <div className="flex items-center gap-2 text-xs font-bold uppercase tracking-wider text-brand-600 mb-1">
          <Code2 className="h-4 w-4" />
          <span>Algorithmic Problem Solving</span>
        </div>
        <h1 className="text-2xl sm:text-3xl font-extrabold text-navy-800 tracking-tight">
          Coding Practice Centre
        </h1>
        <p className="mt-2 text-sm text-slateText-secondary max-w-3xl leading-relaxed">
          Master interview patterns in Arrays, Hash Maps, Stacks, Trees, and Dynamic Programming.
          Write solutions in Python, JavaScript, Java, or C++ with complexity validation and official LeetCode / GeeksforGeeks problem cross-references.
        </p>

        {/* Search & Filters */}
        <div className="mt-6 flex flex-col sm:flex-row gap-3">
          <div className="relative flex-1">
            <Search className="absolute left-3.5 top-3 h-4 w-4 text-slateText-muted" />
            <input
              type="text"
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              placeholder="Search problems by name or algorithmic pattern..."
              className="w-full rounded-xl border border-slate-300 pl-10 pr-4 py-2.5 text-xs text-slateText-primary focus:border-brand-600 focus:ring-2 focus:ring-brand-500/20 focus:outline-none transition-all shadow-xs"
            />
          </div>

          <div className="flex gap-2">
            <select
              value={difficultyFilter}
              onChange={(e) => setDifficultyFilter(e.target.value)}
              className="rounded-xl border border-slate-300 bg-white px-4 py-2.5 text-xs font-semibold text-slateText-secondary focus:border-brand-600 focus:outline-none shadow-xs cursor-pointer"
            >
              <option value="all">All Difficulties</option>
              <option value="Easy">Easy</option>
              <option value="Medium">Medium</option>
              <option value="Hard">Hard</option>
            </select>
          </div>
        </div>
      </div>

      {loading ? (
        <div className="flex h-64 items-center justify-center">
          <div className="h-8 w-8 animate-spin rounded-full border-4 border-brand-600 border-t-transparent" />
        </div>
      ) : (
        <div className="rounded-2xl border border-surface-border bg-white shadow-card overflow-hidden">
          <div className="divide-y divide-slate-100">
            {filteredProblems.map((p) => {
              const diffColor =
                p.difficulty === 'Easy'
                  ? 'text-emerald-700 bg-emerald-50 border-emerald-200'
                  : p.difficulty === 'Medium'
                  ? 'text-amber-700 bg-amber-50 border-amber-200'
                  : 'text-rose-700 bg-rose-50 border-rose-200';

              return (
                <div
                  key={p.id}
                  className="flex flex-col sm:flex-row sm:items-center justify-between p-5 sm:p-6 hover:bg-brand-50/40 hover:pl-7 transition-all duration-200 gap-4 group"
                >
                  <div className="space-y-1.5">
                    <div className="flex items-center gap-2.5">
                      {p.is_solved && (
                        <CheckCircle2 className="h-4 w-4 text-emerald-600 shrink-0" />
                      )}
                      <Link
                        to={`/app/coding/${p.id}`}
                        className="text-sm font-bold text-navy-800 hover:text-brand-600 transition-colors"
                      >
                        {p.title}
                      </Link>
                      <span className={`text-[10px] font-bold uppercase px-2 py-0.5 rounded border ${diffColor}`}>
                        {p.difficulty}
                      </span>
                    </div>

                    <div className="flex flex-wrap items-center gap-3 text-xs text-slateText-muted">
                      <span>Pattern: <strong className="text-slateText-secondary">{p.category}</strong></span>
                      <span>•</span>
                      <span>Time: <code className="text-navy-800 font-semibold">{p.time_complexity}</code></span>
                      <span>•</span>
                      <span>Space: <code className="text-navy-800 font-semibold">{p.space_complexity}</code></span>
                    </div>
                  </div>

                  <div className="flex items-center gap-3 shrink-0">
                    {p.external_url && (
                      <a
                        href={p.external_url}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="flex items-center gap-1 text-xs text-slateText-muted hover:text-brand-600 transition-colors px-2.5 py-1.5 rounded-lg hover:bg-slate-50"
                        title={`Open on ${p.external_platform || 'LeetCode'}`}
                      >
                        <span>{p.external_platform || 'LeetCode'}</span>
                        <ExternalLink className="h-3 w-3" />
                      </a>
                    )}

                    <Link
                      to={`/app/coding/${p.id}`}
                      className="inline-flex items-center gap-1.5 rounded-xl bg-brand-50 border border-brand-200/60 px-4 py-2 text-xs font-bold text-brand-700 group-hover:bg-brand-600 group-hover:text-white group-hover:border-brand-600 transition-all duration-150 shadow-2xs active:scale-95 cursor-pointer"
                    >
                      <span>Solve Problem</span>
                      <ArrowRight className="h-3.5 w-3.5 transition-transform group-hover:translate-x-1" />
                    </Link>
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      )}
    </div>
  );
};

