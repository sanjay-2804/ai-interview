import React, { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import { api } from '../../services/api';
import { LessonDetail } from '../../types';
import {
  ArrowLeft, CheckCircle2, Clock, BookOpen, ExternalLink,
  Bookmark, BookmarkCheck, Sparkles, Check
} from 'lucide-react';

export const LessonView: React.FC = () => {
  const { lessonId } = useParams<{ lessonId: string }>();
  const [lesson, setLesson] = useState<LessonDetail | null>(null);
  const [isCompleted, setIsCompleted] = useState<boolean>(false);
  const [isCompleting, setIsCompleting] = useState<boolean>(false);
  const [isBookmarked, setIsBookmarked] = useState<boolean>(false);
  const [loading, setLoading] = useState<boolean>(true);

  useEffect(() => {
    if (lessonId) {
      api.getLesson(parseInt(lessonId, 10))
        .then((data) => {
          setLesson(data);
          setIsCompleted(data.is_completed);
        })
        .catch((err) => console.error('Failed to load lesson:', err))
        .finally(() => setLoading(false));
    }
  }, [lessonId]);

  const handleMarkComplete = async () => {
    if (!lesson || isCompleted || isCompleting) return;
    setIsCompleting(true);
    try {
      await api.completeLesson(lesson.id);
      setIsCompleted(true);
    } catch (err) {
      console.error('Failed to mark lesson complete:', err);
    } finally {
      setIsCompleting(false);
    }
  };

  const handleToggleBookmark = async () => {
    if (!lesson) return;
    try {
      await api.toggleBookmark({
        item_type: 'lesson',
        item_id: lesson.id,
        title: lesson.title,
        link_path: `/app/technical/lesson/${lesson.id}`,
      });
      setIsBookmarked(!isBookmarked);
    } catch (err) {
      console.error('Failed to bookmark lesson:', err);
    }
  };

  if (loading) {
    return (
      <div className="flex h-96 items-center justify-center">
        <div className="h-8 w-8 animate-spin rounded-full border-4 border-brand-600 border-t-transparent" />
      </div>
    );
  }

  if (!lesson) {
    return (
      <div className="text-center py-12">
        <p className="text-sm text-slateText-secondary">Lesson not found.</p>
        <Link to="/app/technical" className="mt-4 inline-flex items-center gap-2 text-sm text-brand-600">
          <ArrowLeft className="h-4 w-4" /> Back to Technical Centre
        </Link>
      </div>
    );
  }

  return (
    <div className="max-w-4xl mx-auto space-y-8 pb-20">
      {/* Back and Action bar */}
      <div className="flex items-center justify-between">
        <Link
          to="/app/technical"
          className="inline-flex items-center gap-2 text-xs font-semibold text-slateText-secondary hover:text-brand-600 transition-all hover:-translate-x-0.5 group"
        >
          <ArrowLeft className="h-4 w-4 transition-transform group-hover:-translate-x-1" />
          Back to Technical Centre
        </Link>

        <div className="flex items-center gap-3">
          <button
            onClick={handleToggleBookmark}
            className={`flex items-center gap-2 rounded-xl border px-4 py-2 text-xs font-bold transition-all active:scale-95 cursor-pointer shadow-xs ${
              isBookmarked
                ? 'border-brand-300 bg-brand-50 text-brand-700 hover:bg-brand-100'
                : 'border-slate-200 bg-white text-slateText-secondary hover:border-brand-300 hover:bg-slate-50'
            }`}
          >
            {isBookmarked ? (
              <>
                <BookmarkCheck className="h-4 w-4 text-brand-600" />
                <span>Bookmarked</span>
              </>
            ) : (
              <>
                <Bookmark className="h-4 w-4" />
                <span>Bookmark Concept</span>
              </>
            )}
          </button>
        </div>
      </div>

      {/* Lesson Header Card */}
      <div className="rounded-2xl border border-surface-border bg-white p-7 sm:p-9 shadow-card">
        <div className="flex items-center gap-2.5 mb-3">
          <span className="inline-flex items-center rounded-full bg-brand-100 px-3 py-1 text-xs font-bold uppercase tracking-wider text-brand-800">
            {lesson.difficulty} Level
          </span>
          <span className="text-slate-300">•</span>
          <span className="flex items-center gap-1.5 text-xs text-slateText-muted font-medium">
            <Clock className="h-3.5 w-3.5" />
            {lesson.estimated_minutes} min read
          </span>
          {isCompleted && (
            <span className="ml-auto inline-flex items-center gap-1.5 text-xs font-bold text-emerald-700 bg-emerald-50 px-3 py-1 rounded-full border border-emerald-200">
              <CheckCircle2 className="h-4 w-4" />
              Completed
            </span>
          )}
        </div>

        <h1 className="text-2xl sm:text-3xl font-extrabold text-navy-800 tracking-tight">
          {lesson.title}
        </h1>

        {/* Key Takeaways Box */}
        {lesson.key_takeaways && lesson.key_takeaways.length > 0 && (
          <div className="mt-7 rounded-2xl border border-blue-100 bg-brand-50/50 p-6 shadow-xs">
            <h3 className="text-xs font-bold uppercase tracking-wider text-brand-800 flex items-center gap-2 mb-3">
              <Sparkles className="h-4 w-4 text-brand-600" />
              Key Placement Takeaways
            </h3>
            <ul className="space-y-2">
              {lesson.key_takeaways.map((point, idx) => (
                <li key={idx} className="flex items-start gap-2.5 text-xs text-slateText-primary leading-relaxed font-medium">
                  <Check className="h-4 w-4 text-brand-600 shrink-0 mt-0.5" />
                  <span>{point}</span>
                </li>
              ))}
            </ul>
          </div>
        )}
      </div>

      {/* Lesson Content Markdown Body */}
      <div className="rounded-2xl border border-surface-border bg-white p-7 sm:p-10 shadow-card prose prose-slate max-w-none text-sm text-slateText-primary leading-relaxed">
        <div className="whitespace-pre-line leading-relaxed space-y-4">
          {lesson.content_markdown}
        </div>
      </div>

      {/* Completion CTA */}
      <div className="rounded-2xl border border-brand-200 bg-gradient-to-r from-brand-50 via-white to-brand-50/30 p-7 sm:p-8 shadow-card flex flex-col sm:flex-row sm:items-center justify-between gap-5">
        <div>
          <h4 className="text-base font-bold text-navy-800">Finished Reading This Concept?</h4>
          <p className="text-xs text-slateText-secondary mt-1">
            Marking this lesson complete updates your preparation roadmap and unlocks progress stats.
          </p>
        </div>

        <button
          onClick={handleMarkComplete}
          disabled={isCompleted || isCompleting}
          className={`inline-flex items-center gap-2 rounded-xl px-7 py-3 text-xs font-bold shadow-sm transition-all duration-200 ${
            isCompleted
              ? 'bg-emerald-600 text-white cursor-default shadow-xs'
              : 'bg-brand-600 text-white hover:bg-brand-700 hover:shadow-md active:scale-[0.98] cursor-pointer'
          }`}
        >
          <CheckCircle2 className="h-4 w-4" />
          {isCompleted ? 'Lesson Completed' : isCompleting ? 'Updating...' : 'Mark as Complete'}
        </button>
      </div>

      {/* Related External Resources */}
      {lesson.resources && lesson.resources.length > 0 && (
        <div className="space-y-4 pt-4">
          <h3 className="text-base font-bold text-navy-800">Curated External Practice Links</h3>
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
            {lesson.resources.map((r) => (
              <a
                key={r.id}
                href={r.url}
                target="_blank"
                rel="noopener noreferrer"
                className="flex items-center justify-between p-5 rounded-2xl border border-slate-200 bg-white shadow-subtle hover:border-brand-300 hover:shadow-card-hover hover:-translate-y-0.5 transition-all duration-200 group text-xs"
              >
                <div>
                  <div className="font-bold text-slateText-primary group-hover:text-brand-700 transition-colors">
                    {r.title}
                  </div>
                  <div className="text-[11px] text-slateText-muted mt-1 font-medium">{r.provider_name}</div>
                </div>
                <ExternalLink className="h-4 w-4 text-slateText-muted group-hover:text-brand-600 group-hover:translate-x-0.5 transition-all" />
              </a>
            ))}
          </div>
        </div>
      )}
    </div>
  );
};

