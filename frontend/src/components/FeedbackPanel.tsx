import React from 'react';
import { AnswerFeedback } from '../types';
import { CheckCircle2, XCircle, Lightbulb, AlertTriangle, BookOpen, ArrowRight, ExternalLink } from 'lucide-react';

interface FeedbackPanelProps {
  feedback: AnswerFeedback;
  onNext: () => void;
  isLastQuestion?: boolean;
}

export const FeedbackPanel: React.FC<FeedbackPanelProps> = ({
  feedback,
  onNext,
  isLastQuestion = false,
}) => {
  const isCorrect = feedback.is_correct;

  return (
    <div
      className={`mt-8 rounded-2xl border p-6 sm:p-8 transition-all shadow-sm ${
        isCorrect
          ? 'bg-state-successBg/40 border-state-success/30'
          : 'bg-state-errorBg/40 border-state-error/30'
      }`}
    >
      {/* Result Status Header */}
      <div className="flex items-start justify-between gap-4 border-b pb-4 border-slate-200">
        <div className="flex items-center gap-3">
          {isCorrect ? (
            <div className="flex h-10 w-10 items-center justify-center rounded-full bg-emerald-100 text-emerald-700">
              <CheckCircle2 className="h-6 w-6" />
            </div>
          ) : (
            <div className="flex h-10 w-10 items-center justify-center rounded-full bg-rose-100 text-rose-700">
              <XCircle className="h-6 w-6" />
            </div>
          )}
          <div>
            <div className="flex items-center gap-2">
              <span
                className={`inline-flex items-center rounded-md px-2.5 py-0.5 text-xs font-semibold uppercase tracking-wider ${
                  isCorrect
                    ? 'bg-emerald-600 text-white'
                    : 'bg-rose-600 text-white'
                }`}
              >
                {isCorrect ? 'Correct Answer' : 'Incorrect Answer'}
              </span>
              <span className="text-xs font-medium text-slateText-secondary">
                Submitted Option: <strong className="text-slateText-primary">{feedback.selected_option}</strong>
              </span>
            </div>
            <p className="mt-1 text-sm font-medium text-slateText-primary">
              {feedback.encouraging_feedback}
            </p>
          </div>
        </div>

        {/* Expected/Correct Option Indicator */}
        <div className="text-right">
          <span className="text-xs uppercase font-semibold text-slateText-muted">Reference Solution</span>
          <div className="text-lg font-bold text-brand-700">Option {feedback.correct_option}</div>
        </div>
      </div>

      {/* Why other options are wrong breakdown */}
      {feedback.options_breakdown && feedback.options_breakdown.length > 0 && (
        <div className="mt-4">
          <h4 className="text-xs font-bold uppercase tracking-wider text-slateText-secondary mb-2">
            Option-by-Option Breakdown
          </h4>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-2">
            {feedback.options_breakdown.map((opt) => (
              <div
                key={opt.option_key}
                className={`p-3 rounded-lg border text-xs leading-relaxed ${
                  opt.is_correct
                    ? 'border-emerald-300 bg-white/90 text-emerald-900 font-medium'
                    : 'border-slate-200 bg-white/60 text-slateText-secondary'
                }`}
              >
                <div className="flex items-center gap-1.5 font-bold mb-1">
                  <span>Option {opt.option_key}:</span>
                  <span className="truncate">{opt.option_text}</span>
                  {opt.is_correct && (
                    <span className="ml-auto text-[10px] bg-emerald-100 text-emerald-800 px-1.5 py-0.5 rounded">
                      Correct
                    </span>
                  )}
                </div>
                {opt.why_wrong && (
                  <p className="text-[11px] text-slateText-muted">{opt.why_wrong}</p>
                )}
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Core Explanation & Step-by-Step Reasoning */}
      <div className="mt-5 space-y-4">
        <div className="rounded-lg bg-white p-4 shadow-subtle border border-slate-200">
          <h4 className="flex items-center gap-2 text-xs font-bold uppercase tracking-wider text-slateText-primary mb-2">
            <BookOpen className="h-4 w-4 text-brand-600" />
            Detailed Explanation & Theory
          </h4>
          <p className="text-sm text-slateText-primary leading-relaxed whitespace-pre-line">
            {feedback.explanation}
          </p>
        </div>

        <div className="rounded-lg bg-white p-4 shadow-subtle border border-slate-200">
          <h4 className="text-xs font-bold uppercase tracking-wider text-slateText-primary mb-2">
            Step-by-Step Mathematical & Conceptual Reasoning
          </h4>
          <pre className="text-xs font-mono text-slateText-primary bg-slate-50 p-3 rounded-md overflow-x-auto whitespace-pre-wrap leading-relaxed border border-slate-100">
            {feedback.step_by_step_reasoning}
          </pre>
        </div>

        {/* Practical Example & Common Mistakes Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div className="rounded-lg bg-white p-4 shadow-subtle border border-slate-200">
            <h4 className="flex items-center gap-2 text-xs font-bold uppercase tracking-wider text-slateText-primary mb-2">
              <Lightbulb className="h-4 w-4 text-amber-500" />
              Practical Placement Example
            </h4>
            <p className="text-xs text-slateText-secondary leading-relaxed">
              {feedback.practical_example}
            </p>
          </div>

          <div className="rounded-lg bg-white p-4 shadow-subtle border border-slate-200">
            <h4 className="flex items-center gap-2 text-xs font-bold uppercase tracking-wider text-rose-700 mb-2">
              <AlertTriangle className="h-4 w-4 text-rose-600" />
              Common Trap or Mistake to Avoid
            </h4>
            <p className="text-xs text-slateText-secondary leading-relaxed">
              {feedback.common_mistake}
            </p>
          </div>
        </div>

        {/* Learning Tip Callout */}
        <div className="rounded-lg bg-blue-50/80 border border-blue-200 p-3.5 flex items-start gap-3">
          <Lightbulb className="h-5 w-5 text-brand-600 shrink-0 mt-0.5" />
          <div className="text-xs leading-relaxed">
            <strong className="text-brand-900 block font-semibold mb-0.5">Quick Placement Takeaway:</strong>
            <span className="text-brand-800">{feedback.learning_tip}</span>
          </div>
        </div>

        {/* Related External Concept Link */}
        {feedback.related_concept_url && (
          <div className="flex items-center justify-between text-xs text-slateText-secondary pt-1">
            <span>Recommended Reading:</span>
            <a
              href={feedback.related_concept_url}
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center gap-1 font-medium text-brand-600 hover:text-brand-800 underline"
            >
              Explore Topic Documentation <ExternalLink className="h-3 w-3" />
            </a>
          </div>
        )}
      </div>

      {/* Action Footer: ONLY Next Question is displayed. STRICT RULE: No retry or redo! */}
      <div className="mt-8 flex items-center justify-end border-t border-slate-200/80 pt-5">
        <button
          onClick={onNext}
          className="inline-flex items-center gap-2 rounded-xl bg-brand-600 px-7 py-3 text-sm font-bold text-white shadow-sm hover:bg-brand-700 hover:shadow-md focus:outline-none focus:ring-2 focus:ring-brand-500/20 active:scale-[0.98] transition-all duration-150 cursor-pointer"
        >
          <span>{isLastQuestion ? 'Complete Assessment & View Summary' : 'Next Question'}</span>
          <ArrowRight className="h-4 w-4" />
        </button>
      </div>
    </div>
  );
};

