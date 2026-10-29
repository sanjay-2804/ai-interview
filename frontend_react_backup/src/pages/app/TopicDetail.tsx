import React, { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import { api } from '../../services/api';
import { BookOpen, ExternalLink, ArrowRight, ArrowLeft, CheckCircle2, Clock } from 'lucide-react';

export const TopicDetail: React.FC = () => {
  const { slug } = useParams<{ slug: string }>();
  const [topic, setTopic] = useState<any>(null);
  const [loading, setLoading] = useState<boolean>(true);

  useEffect(() => {
    if (slug) {
      api.getTopicDetail(slug)
        .then(setTopic)
        .catch((err) => console.error('Failed to load topic detail:', err))
        .finally(() => setLoading(false));
    }
  }, [slug]);

  if (loading) {
    return (
      <div className="flex h-96 items-center justify-center">
        <div className="h-8 w-8 animate-spin rounded-full border-4 border-brand-600 border-t-transparent" />
      </div>
    );
  }

  if (!topic) {
    return (
      <div className="text-center py-12">
        <p className="text-sm text-slateText-secondary">Topic not found.</p>
        <Link to="/app/technical" className="mt-4 inline-flex items-center gap-2 text-sm text-brand-600">
          <ArrowLeft className="h-4 w-4" /> Back to Technical Centre
        </Link>
      </div>
    );
  }

  return (
    <div className="max-w-5xl mx-auto space-y-8 pb-16">
      {/* Back button */}
      <div>
        <Link
          to="/app/technical"
          className="inline-flex items-center gap-2 text-xs font-semibold text-slateText-secondary hover:text-brand-600 transition-all hover:-translate-x-0.5 group"
        >
          <ArrowLeft className="h-4 w-4 transition-transform group-hover:-translate-x-1" />
          Back to All Subjects
        </Link>
      </div>

      {/* Header */}
      <div className="rounded-2xl border border-surface-border bg-white p-7 sm:p-9 shadow-card">
        <span className="inline-block text-[11px] font-bold uppercase tracking-wider text-brand-600 bg-brand-50 px-3 py-1 rounded-full border border-brand-200">
          {topic.category.toUpperCase()} • {topic.subcategory.toUpperCase()}
        </span>
        <h1 className="text-2xl sm:text-3xl font-extrabold text-navy-800 tracking-tight mt-3">
          {topic.name}
        </h1>
        <p className="mt-2.5 text-sm text-slateText-secondary leading-relaxed max-w-3xl">
          {topic.description}
        </p>

        {/* Quick actions */}
        <div className="mt-7 pt-5 border-t border-slate-100 flex flex-wrap gap-3">
          <Link
            to="/app/aptitude"
            className="inline-flex items-center gap-2 rounded-xl bg-brand-600 px-5 py-2.5 text-xs font-bold text-white shadow-sm hover:bg-brand-700 hover:shadow-md active:scale-[0.98] transition-all"
          >
            Practice Assessment MCQs
            <ArrowRight className="h-3.5 w-3.5" />
          </Link>
        </div>
      </div>

      {/* Lessons List */}
      <div className="space-y-4">
        <h2 className="text-base font-bold text-navy-800">Lessons & Core Explanations</h2>
        {topic.lessons && topic.lessons.length > 0 ? (
          <div className="grid grid-cols-1 gap-3.5">
            {topic.lessons.map((lesson: any) => (
              <Link
                key={lesson.id}
                to={`/app/technical/lesson/${lesson.id}`}
                className="flex items-center justify-between p-5 sm:p-6 rounded-2xl border border-surface-border bg-white shadow-subtle hover:border-brand-300 hover:shadow-card-hover hover:-translate-y-0.5 transition-all duration-200 group"
              >
                <div className="flex items-center gap-4">
                  <div className="flex h-11 w-11 shrink-0 items-center justify-center rounded-xl bg-brand-50 text-brand-600 group-hover:bg-brand-600 group-hover:text-white transition-colors duration-200">
                    <BookOpen className="h-5 w-5" />
                  </div>
                  <div>
                    <h3 className="text-sm font-bold text-slateText-primary group-hover:text-brand-700 transition-colors">
                      {lesson.title}
                    </h3>
                    <div className="flex items-center gap-3 text-xs text-slateText-muted mt-1">
                      <span className="capitalize font-medium text-slateText-secondary">{lesson.difficulty} Level</span>
                      <span>•</span>
                      <span className="flex items-center gap-1.5 font-medium">
                        <Clock className="h-3.5 w-3.5" />
                        {lesson.estimated_minutes} mins read
                      </span>
                    </div>
                  </div>
                </div>

                <div className="flex items-center gap-2 text-xs font-bold text-brand-600 group-hover:translate-x-1 transition-transform">
                  <span>Read Lesson</span>
                  <ArrowRight className="h-4 w-4" />
                </div>
              </Link>
            ))}
          </div>
        ) : (
          <p className="text-xs text-slateText-muted">Lessons for this topic are being synchronized.</p>
        )}
      </div>

      {/* Verified External Resources */}
      {topic.resources && topic.resources.length > 0 && (
        <div className="space-y-4 pt-6 border-t border-slate-100">
          <div>
            <h2 className="text-base font-bold text-navy-800">Verified External Reference Links</h2>
            <p className="text-xs text-slateText-secondary mt-0.5">
              Authoritative documentation and practice platforms.
            </p>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
            {topic.resources.map((res: any) => (
              <a
                key={res.id}
                href={res.url}
                target="_blank"
                rel="noopener noreferrer"
                className="rounded-2xl border border-surface-border bg-white p-5 sm:p-6 shadow-subtle hover:border-brand-300 hover:shadow-card-hover hover:-translate-y-1 transition-all duration-200 group flex flex-col justify-between"
              >
                <div>
                  <div className="flex items-center justify-between text-[11px] font-semibold text-slateText-muted mb-2">
                    <span className="text-brand-700 font-bold">{res.provider_name}</span>
                    <span className="capitalize bg-slate-100 text-slateText-secondary px-2.5 py-0.5 rounded-full text-[10px] font-bold">
                      {res.resource_type}
                    </span>
                  </div>
                  <h4 className="text-sm font-bold text-slateText-primary group-hover:text-brand-700 transition-colors">
                    {res.title}
                  </h4>
                  <p className="text-xs text-slateText-secondary mt-1.5 line-clamp-2 leading-relaxed">
                    {res.description}
                  </p>
                </div>
                <div className="mt-4 pt-3 border-t border-slate-100 flex items-center gap-1.5 text-xs font-bold text-brand-600 group-hover:translate-x-0.5 transition-transform">
                  <span>Visit {res.provider_name}</span>
                  <ExternalLink className="h-3.5 w-3.5" />
                </div>
              </a>
            ))}
          </div>
        </div>
      )}
    </div>
  );
};

