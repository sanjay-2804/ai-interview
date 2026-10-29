import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { api } from '../../services/api';
import { TopicItem } from '../../types';
import { BookOpen, Code2, Globe, Database, Cpu, Network, ArrowRight, ExternalLink } from 'lucide-react';

export const TechnicalCentre: React.FC = () => {
  const [topics, setTopics] = useState<TopicItem[]>([]);
  const [selectedCategory, setSelectedCategory] = useState<string>('all');
  const [loading, setLoading] = useState<boolean>(true);

  useEffect(() => {
    api.getTopics()
      .then(setTopics)
      .catch((err) => console.error('Failed to load technical topics:', err))
      .finally(() => setLoading(false));
  }, []);

  const categories = [
    { id: 'all', label: 'All Subjects' },
    { id: 'technical', label: 'Computer Science Core' },
    { id: 'aptitude', label: 'Placement Aptitude' },
  ];

  const filteredTopics = selectedCategory === 'all'
    ? topics
    : topics.filter((t) => t.category === selectedCategory);

  const getTopicIcon = (iconName: string) => {
    switch (iconName) {
      case 'Binary': return <Code2 className="h-5 w-5" />;
      case 'Database': return <Database className="h-5 w-5" />;
      case 'Cpu': return <Cpu className="h-5 w-5" />;
      case 'Network': return <Network className="h-5 w-5" />;
      case 'Globe': return <Globe className="h-5 w-5" />;
      default: return <BookOpen className="h-5 w-5" />;
    }
  };

  return (
    <div className="max-w-6xl mx-auto space-y-8 pb-16">
      {/* Header */}
      <div className="border-b border-surface-border pb-6">
        <h1 className="text-2xl sm:text-3xl font-extrabold text-navy-800 tracking-tight">
          Technical Learning Centre
        </h1>
        <p className="mt-2 text-sm text-slateText-secondary max-w-3xl leading-relaxed">
          Structured conceptual modules covering core computer science subjects, algorithms, and system fundamentals.
          Includes concept guides, common interview questions, and verified English external learning links.
        </p>

        {/* Filter buttons */}
        <div className="mt-6 flex flex-wrap gap-2.5">
          {categories.map((c) => (
            <button
              key={c.id}
              onClick={() => setSelectedCategory(c.id)}
              className={`px-4 py-2 rounded-xl text-xs font-semibold transition-all duration-150 cursor-pointer ${
                selectedCategory === c.id
                  ? 'bg-brand-600 text-white shadow-xs'
                  : 'bg-white border border-slate-200 text-slateText-secondary hover:bg-slate-50 hover:border-brand-200'
              }`}
            >
              {c.label}
            </button>
          ))}
        </div>
      </div>

      {loading ? (
        <div className="flex h-64 items-center justify-center">
          <div className="h-8 w-8 animate-spin rounded-full border-4 border-brand-600 border-t-transparent" />
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {filteredTopics.map((topic) => (
            <div
              key={topic.id}
              className="flex flex-col justify-between rounded-2xl border border-surface-border bg-white p-6 sm:p-7 shadow-subtle hover:-translate-y-1.5 hover:shadow-card-hover hover:border-brand-300 transition-all duration-200 group cursor-pointer"
            >
              <div>
                <div className="flex items-center justify-between mb-4">
                  <div className="flex h-11 w-11 items-center justify-center rounded-xl bg-brand-50 text-brand-600 shadow-2xs group-hover:scale-105 transition-transform">
                    {getTopicIcon(topic.icon)}
                  </div>
                  <span className="text-[11px] font-bold text-slateText-muted uppercase tracking-wider bg-slate-50 border border-slate-200 px-2 py-0.5 rounded-full">
                    {topic.subcategory}
                  </span>
                </div>

                <h3 className="text-base font-bold text-navy-800 mb-2 group-hover:text-brand-700 transition-colors">
                  {topic.name}
                </h3>
                <p className="text-xs text-slateText-secondary leading-relaxed line-clamp-3">
                  {topic.description}
                </p>

                {/* Stats Pills */}
                <div className="mt-4 flex flex-wrap gap-2 text-[11px] font-medium text-slateText-muted">
                  <span className="bg-slate-50 border border-slate-200/80 px-2.5 py-1 rounded-md">
                    {topic.lesson_count} Lessons
                  </span>
                  <span className="bg-slate-50 border border-slate-200/80 px-2.5 py-1 rounded-md">
                    {topic.question_count} MCQs
                  </span>
                  <span className="bg-slate-50 border border-slate-200/80 px-2.5 py-1 rounded-md">
                    {topic.resource_count} Curated Links
                  </span>
                </div>
              </div>

              <div className="mt-6 pt-4 border-t border-slate-100 flex items-center justify-between">
                <Link
                  to={`/app/technical/topic/${topic.slug}`}
                  className="inline-flex items-center gap-1.5 text-xs font-bold text-brand-600 group-hover:text-brand-700 transition-colors"
                >
                  <span>View Topic Curriculum</span>
                  <ArrowRight className="h-3.5 w-3.5 transition-transform group-hover:translate-x-1" />
                </Link>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

