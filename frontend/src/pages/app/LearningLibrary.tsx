import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { api } from '../../services/api';
import { Bookmark } from '../../types';
import { BookmarkCheck, Trash2, ExternalLink, ArrowRight, BookOpen, Code2, HelpCircle } from 'lucide-react';

export const LearningLibrary: React.FC = () => {
  const [bookmarks, setBookmarks] = useState<Bookmark[]>([]);
  const [filterType, setFilterType] = useState<string>('all');
  const [loading, setLoading] = useState<boolean>(true);

  const loadBookmarks = async () => {
    try {
      const data = await api.getBookmarks();
      setBookmarks(data);
    } catch (err) {
      console.error('Failed to load bookmarks:', err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadBookmarks();
  }, []);

  const handleDelete = async (id: number) => {
    try {
      await api.deleteBookmark(id);
      setBookmarks((prev) => prev.filter((b) => b.id !== id));
    } catch (err) {
      console.error('Failed to delete bookmark:', err);
    }
  };

  const filtered = filterType === 'all'
    ? bookmarks
    : bookmarks.filter((b) => b.item_type === filterType);

  return (
    <div className="max-w-5xl mx-auto space-y-8 pb-16">
      {/* Header */}
      <div className="border-b border-surface-border pb-6 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <div className="flex items-center gap-2 text-xs font-bold uppercase tracking-wider text-brand-600 mb-1">
            <BookmarkCheck className="h-4 w-4" />
            <span>Personal Revision Library</span>
          </div>
          <h1 className="text-2xl sm:text-3xl font-extrabold text-navy-800 tracking-tight">
            My Bookmarked Concepts & Problems
          </h1>
          <p className="mt-1 text-sm text-slateText-secondary max-w-2xl leading-relaxed">
            Quickly revisit important questions, tricky edge cases, and fundamental lessons that you flagged during practice.
          </p>
        </div>

        {/* Filter Pills */}
        <div className="flex gap-2">
          {['all', 'lesson', 'coding_problem', 'question'].map((type) => (
            <button
              key={type}
              onClick={() => setFilterType(type)}
              className={`px-4 py-2 rounded-xl text-xs font-bold capitalize transition-all duration-200 cursor-pointer ${filterType === type
                  ? 'bg-brand-600 text-white shadow-sm -translate-y-0.5'
                  : 'bg-white border border-slate-200 text-slateText-secondary hover:border-brand-300 hover:bg-slate-50'
                }`}
            >
              {type === 'all' ? 'All Items' : type.replace('_', ' ')}
            </button>
          ))}
        </div>
      </div>

      {loading ? (
        <div className="flex h-64 items-center justify-center">
          <div className="h-8 w-8 animate-spin rounded-full border-4 border-brand-600 border-t-transparent" />
        </div>
      ) : filtered.length > 0 ? (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
          {filtered.map((b) => (
            <div
              key={b.id}
              className="rounded-2xl border border-surface-border bg-white p-6 sm:p-7 shadow-card hover:border-brand-300 hover:shadow-card-hover hover:-translate-y-1 transition-all duration-200 flex flex-col justify-between group"
            >
              <div>
                <div className="flex items-center justify-between mb-3">
                  <span className="text-[10px] font-bold uppercase tracking-wider px-2.5 py-1 rounded-full bg-brand-100 text-brand-800">
                    {b.item_type.replace('_', ' ')}
                  </span>
                  <button
                    onClick={() => handleDelete(b.id)}
                    className="p-1.5 text-slateText-muted hover:text-rose-600 hover:bg-rose-50 rounded-lg transition-colors cursor-pointer"
                    title="Remove from library"
                  >
                    <Trash2 className="h-4 w-4" />
                  </button>
                </div>
                <h3 className="text-base font-bold text-navy-800 mb-1 group-hover:text-brand-700 transition-colors">{b.title}</h3>
                {b.topic_name && (
                  <p className="text-xs text-slateText-muted font-medium">Topic: {b.topic_name}</p>
                )}
              </div>

              <div className="mt-5 pt-4 border-t border-slate-100 flex items-center justify-end">
                <Link
                  to={b.link_path}
                  className="inline-flex items-center gap-1.5 text-xs font-bold text-brand-600 group-hover:text-brand-800 group-hover:translate-x-0.5 transition-all"
                >
                  <span>Open Item</span>
                  <ArrowRight className="h-4 w-4" />
                </Link>
              </div>
            </div>
          ))}
        </div>
      ) : (
        <div className="rounded-2xl border border-dashed border-slate-200 bg-white p-14 text-center text-slateText-muted space-y-3 shadow-subtle">
          <BookmarkCheck className="h-12 w-12 mx-auto text-slate-300" />
          <h3 className="text-base font-bold text-navy-800">No Bookmarks Saved Yet</h3>
          <p className="text-xs max-w-sm mx-auto leading-relaxed">
            While reviewing lessons or coding problems, click the bookmark icon to save them for quick revision.
          </p>
        </div>
      )}
    </div>
  );
};

