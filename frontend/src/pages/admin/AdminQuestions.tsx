import React, { useState, useEffect } from 'react';
import { api } from '../../services/api';
import { HelpCircle, Plus, Trash2, CheckCircle2, XCircle, X, BookOpen, Layers } from 'lucide-react';

export const AdminQuestions: React.FC = () => {
  const [questions, setQuestions] = useState<any[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [showCreateModal, setShowCreateModal] = useState<boolean>(false);

  // New question form state
  const [questionText, setQuestionText] = useState('');
  const [topicId, setTopicId] = useState(1);
  const [difficulty, setDifficulty] = useState('intermediate');
  const [explanation, setExplanation] = useState('');
  const [reasoning, setReasoning] = useState('');
  const [example, setExample] = useState('');
  const [mistake, setMistake] = useState('');
  const [tip, setTip] = useState('');
  const [options, setOptions] = useState([
    { option_key: 'A', option_text: '', is_correct: false, why_wrong_explanation: '' },
    { option_key: 'B', option_text: '', is_correct: true, why_wrong_explanation: '' },
    { option_key: 'C', option_text: '', is_correct: false, why_wrong_explanation: '' },
    { option_key: 'D', option_text: '', is_correct: false, why_wrong_explanation: '' },
  ]);

  const loadQuestions = async () => {
    try {
      const data = await api.getAdminQuestions();
      setQuestions(data);
    } catch (err) {
      console.error('Failed to load admin questions:', err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadQuestions();
  }, []);

  const handleDelete = async (id: number) => {
    if (!window.confirm('Are you sure you want to delete this question?')) return;
    try {
      await api.deleteAdminQuestion(id);
      setQuestions((prev) => prev.filter((q) => q.id !== id));
    } catch (err) {
      console.error('Failed to delete question:', err);
    }
  };

  const handleCreate = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await api.createAdminQuestion({
        topic_id: topicId,
        question_type: 'aptitude_mcq',
        difficulty,
        question_text: questionText,
        explanation,
        step_by_step_reasoning: reasoning,
        practical_example: example,
        common_mistake: mistake,
        learning_tip: tip,
        options,
      });
      setShowCreateModal(false);
      // Reset form
      setQuestionText('');
      setExplanation('');
      setReasoning('');
      loadQuestions();
    } catch (err) {
      console.error('Failed to create question:', err);
    }
  };

  return (
    <div className="space-y-6 max-w-6xl mx-auto pb-16">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-surface-border pb-5">
        <div>
          <span className="text-xs font-bold uppercase tracking-wider text-brand-600">Content Management</span>
          <h1 className="text-2xl font-extrabold text-navy-800 mt-1">Question Bank & Answer Keys</h1>
        </div>

        <button
          onClick={() => setShowCreateModal(true)}
          className="inline-flex items-center gap-2 rounded-xl bg-brand-600 px-5 py-2.5 text-xs font-bold text-white shadow-sm hover:bg-brand-700 hover:shadow-md active:scale-95 transition-all cursor-pointer"
        >
          <Plus className="h-4 w-4" />
          Add Assessment Question
        </button>
      </div>

      {loading ? (
        <div className="flex h-64 items-center justify-center">
          <div className="h-8 w-8 animate-spin rounded-full border-4 border-brand-600 border-t-transparent" />
        </div>
      ) : (
        <div className="space-y-4">
          {questions.map((q) => (
            <div
              key={q.id}
              className="rounded-2xl border border-surface-border bg-white p-6 sm:p-7 space-y-4 shadow-card hover:border-brand-300 hover:shadow-card-hover hover:-translate-y-0.5 transition-all duration-200"
            >
              <div className="flex items-start justify-between gap-4">
                <div>
                  <div className="flex items-center gap-2 mb-2">
                    <span className="text-[10px] font-bold uppercase tracking-wider px-2.5 py-1 rounded-full bg-brand-50 text-brand-700 border border-brand-200">
                      {q.topic_name}
                    </span>
                    <span className="text-[10px] uppercase font-bold text-slateText-muted bg-slate-100 px-2 py-0.5 rounded-full">
                      {q.difficulty}
                    </span>
                  </div>
                  <h3 className="text-base font-bold text-navy-800 leading-relaxed">
                    {q.question_text}
                  </h3>
                </div>

                <button
                  onClick={() => handleDelete(q.id)}
                  className="p-2 text-slateText-muted hover:text-rose-600 transition-colors cursor-pointer rounded-xl hover:bg-rose-50"
                  title="Delete question"
                >
                  <Trash2 className="h-4 w-4" />
                </button>
              </div>

              {/* Options breakdown preview */}
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 pt-2">
                {q.options?.map((opt: any) => (
                  <div
                    key={opt.option_key}
                    className={`flex items-center justify-between p-3 rounded-xl border text-xs font-medium ${
                      opt.is_correct
                        ? 'border-emerald-300 bg-emerald-50 text-emerald-900 font-bold shadow-2xs'
                        : 'border-slate-200 bg-slate-50 text-slateText-secondary'
                    }`}
                  >
                    <div className="flex items-center gap-2">
                      <span className="font-bold">{opt.option_key}.</span>
                      <span>{opt.option_text}</span>
                    </div>
                    {opt.is_correct && (
                      <span className="text-[10px] font-bold uppercase text-emerald-700 flex items-center gap-1">
                        <CheckCircle2 className="h-3 w-3" /> Correct
                      </span>
                    )}
                  </div>
                ))}
              </div>

              {q.explanation && (
                <div className="pt-2 border-t border-slate-100 text-xs text-slateText-secondary">
                  <strong className="text-navy-800">Explanation:</strong> {q.explanation}
                </div>
              )}
            </div>
          ))}

          {questions.length === 0 && (
            <div className="py-16 text-center bg-white rounded-2xl border border-surface-border p-8">
              <HelpCircle className="h-10 w-10 text-slateText-muted mx-auto mb-2" />
              <h3 className="text-base font-bold text-navy-800">No Assessment Questions Found</h3>
              <p className="text-xs text-slateText-secondary mt-1">
                Add questions manually or run the seed script to populate the question bank.
              </p>
            </div>
          )}
        </div>
      )}

      {/* Create Modal */}
      {showCreateModal && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-900/40 backdrop-blur-sm">
          <div className="relative w-full max-w-2xl bg-white border border-surface-border rounded-2xl p-6 shadow-2xl max-h-[90vh] overflow-y-auto">
            <div className="flex items-center justify-between border-b border-slate-100 pb-3 mb-4">
              <h2 className="text-base font-bold text-navy-800">Create New Question</h2>
              <button
                onClick={() => setShowCreateModal(false)}
                className="text-slateText-muted hover:text-slateText-primary cursor-pointer"
              >
                <X className="h-5 w-5" />
              </button>
            </div>

            <form onSubmit={handleCreate} className="space-y-4 text-xs">
              <div>
                <label className="block font-bold text-slateText-secondary uppercase mb-1">
                  Question Text
                </label>
                <textarea
                  rows={2}
                  required
                  value={questionText}
                  onChange={(e) => setQuestionText(e.target.value)}
                  className="w-full bg-white border border-slate-300 rounded-lg p-2.5 text-navy-800 focus:outline-none focus:border-brand-600"
                  placeholder="Enter the placement question problem statement..."
                />
              </div>

              <div className="grid grid-cols-2 gap-4">
                <div>
                  <label className="block font-bold text-slateText-secondary uppercase mb-1">
                    Difficulty Level
                  </label>
                  <select
                    value={difficulty}
                    onChange={(e) => setDifficulty(e.target.value)}
                    className="w-full bg-white border border-slate-300 rounded-lg p-2 text-navy-800 focus:outline-none focus:border-brand-600"
                  >
                    <option value="beginner">Beginner</option>
                    <option value="intermediate">Intermediate</option>
                    <option value="advanced">Advanced</option>
                  </select>
                </div>
                <div>
                  <label className="block font-bold text-slateText-secondary uppercase mb-1">
                    Topic ID
                  </label>
                  <input
                    type="number"
                    value={topicId}
                    onChange={(e) => setTopicId(Number(e.target.value))}
                    className="w-full bg-white border border-slate-300 rounded-lg p-2 text-navy-800 focus:outline-none focus:border-brand-600"
                  />
                </div>
              </div>

              {/* Options */}
              <div className="space-y-2 pt-2 border-t border-slate-100">
                <label className="block font-bold text-slateText-secondary uppercase">
                  Options & Correct Answer
                </label>
                {options.map((opt, idx) => (
                  <div key={opt.option_key} className="flex items-center gap-2">
                    <span className="font-bold w-4 text-navy-800">{opt.option_key}</span>
                    <input
                      type="text"
                      required
                      placeholder={`Option ${opt.option_key} text...`}
                      value={opt.option_text}
                      onChange={(e) => {
                        const copy = [...options];
                        copy[idx].option_text = e.target.value;
                        setOptions(copy);
                      }}
                      className="flex-1 bg-white border border-slate-300 rounded-lg p-2 text-navy-800 focus:outline-none focus:border-brand-600"
                    />
                    <label className="flex items-center gap-1 cursor-pointer">
                      <input
                        type="radio"
                        name="correct_option"
                        checked={opt.is_correct}
                        onChange={() => {
                          const copy = options.map((o, i) => ({ ...o, is_correct: i === idx }));
                          setOptions(copy);
                        }}
                        className="text-brand-600"
                      />
                      <span className="text-[11px] font-semibold text-slateText-secondary">Correct</span>
                    </label>
                  </div>
                ))}
              </div>

              {/* Explanations */}
              <div className="space-y-3 pt-2 border-t border-slate-100">
                <div>
                  <label className="block font-bold text-slateText-secondary uppercase mb-1">
                    Overall Conceptual Explanation
                  </label>
                  <textarea
                    rows={2}
                    required
                    value={explanation}
                    onChange={(e) => setExplanation(e.target.value)}
                    className="w-full bg-white border border-slate-300 rounded-lg p-2 text-navy-800 focus:outline-none focus:border-brand-600"
                    placeholder="Comprehensive explanation of the underlying logic..."
                  />
                </div>

                <div>
                  <label className="block font-bold text-slateText-secondary uppercase mb-1">
                    Step-by-Step Reasoning
                  </label>
                  <textarea
                    rows={2}
                    value={reasoning}
                    onChange={(e) => setReasoning(e.target.value)}
                    className="w-full bg-white border border-slate-300 rounded-lg p-2 text-navy-800 focus:outline-none focus:border-brand-600"
                    placeholder="Step 1: ..., Step 2: ..."
                  />
                </div>

                <div className="grid grid-cols-2 gap-4">
                  <div>
                    <label className="block font-bold text-slateText-secondary uppercase mb-1">
                      Common Traps / Mistakes
                    </label>
                    <input
                      type="text"
                      value={mistake}
                      onChange={(e) => setMistake(e.target.value)}
                      className="w-full bg-white border border-slate-300 rounded-lg p-2 text-navy-800 focus:outline-none focus:border-brand-600"
                      placeholder="e.g. Forgetting to divide by Cost Price"
                    />
                  </div>
                  <div>
                    <label className="block font-bold text-slateText-secondary uppercase mb-1">
                      Exam Speed Tip
                    </label>
                    <input
                      type="text"
                      value={tip}
                      onChange={(e) => setTip(e.target.value)}
                      className="w-full bg-white border border-slate-300 rounded-lg p-2 text-navy-800 focus:outline-none focus:border-brand-600"
                      placeholder="e.g. Use 1/6 = 16.66% formula"
                    />
                  </div>
                </div>
              </div>

              <div className="flex justify-end gap-3 pt-4 border-t border-slate-100">
                <button
                  type="button"
                  onClick={() => setShowCreateModal(false)}
                  className="px-4 py-2 border border-slate-300 rounded-lg text-slateText-secondary hover:bg-slate-50 font-semibold cursor-pointer"
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  className="px-5 py-2 bg-brand-600 text-white font-bold rounded-lg hover:bg-brand-700 transition-colors cursor-pointer"
                >
                  Save Question
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};
