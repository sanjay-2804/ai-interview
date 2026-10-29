import React from 'react';
import { GraduationCap, ShieldCheck, Heart, Sparkles, CheckCircle2 } from 'lucide-react';

export const About: React.FC = () => {
  return (
    <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-16 space-y-12">
      {/* Header */}
      <div className="text-center space-y-3">
        <span className="text-xs font-bold uppercase tracking-wider text-brand-600 bg-brand-50 px-3 py-1 rounded-full border border-brand-200">
          Our Mission & Philosophy
        </span>
        <h1 className="text-3xl sm:text-4xl font-extrabold text-navy-800 tracking-tight">
          About InterviewAI
        </h1>
        <p className="text-sm text-slateText-secondary max-w-2xl mx-auto leading-relaxed">
          Built for college students seeking genuine conceptual mastery in placement assessments, algorithmic coding, and technical communication.
        </p>
      </div>

      {/* Core Principles */}
      <div className="space-y-6 text-sm text-slateText-primary leading-relaxed">
        <div className="rounded-3xl border border-surface-border bg-white p-7 sm:p-9 shadow-card hover:border-brand-300 hover:shadow-card-hover hover:-translate-y-1 transition-all duration-200 space-y-3.5">
          <h2 className="text-xl font-extrabold text-navy-800 flex items-center gap-2.5">
            <GraduationCap className="h-6 w-6 text-brand-600" />
            1. Why We Built InterviewAI
          </h2>
          <p className="text-slateText-secondary font-medium leading-relaxed">
            Most recruitment test preparation websites simply tell students whether an answer is "Correct" or "Wrong" and leave them to guess why.
            InterviewAI was founded on the principle that the real learning happens in the feedback loop.
            Every answer submission locks the choice and unlocks deep step-by-step reasoning, mathematical proofs, code complexity breakdowns, and common traps.
          </p>
        </div>

        <div className="rounded-3xl border border-surface-border bg-white p-7 sm:p-9 shadow-card hover:border-emerald-300 hover:shadow-card-hover hover:-translate-y-1 transition-all duration-200 space-y-3.5">
          <h2 className="text-xl font-extrabold text-navy-800 flex items-center gap-2.5">
            <ShieldCheck className="h-6 w-6 text-emerald-600" />
            2. Truth in Data & Honest Metrics
          </h2>
          <p className="text-slateText-secondary font-medium leading-relaxed">
            We reject the practice of fabricating placement rates, student testimonials, or misleading progress statistics.
            Every number on your dashboard—from your 82.4% accuracy to your 4-day study streak—originates directly from verified database records.
          </p>
        </div>

        <div className="rounded-3xl border border-surface-border bg-white p-7 sm:p-9 shadow-card hover:border-purple-300 hover:shadow-card-hover hover:-translate-y-1 transition-all duration-200 space-y-3.5">
          <h2 className="text-xl font-extrabold text-navy-800 flex items-center gap-2.5">
            <Sparkles className="h-6 w-6 text-purple-600" />
            3. Open Access Across Academic Years
          </h2>
          <p className="text-slateText-secondary font-medium leading-relaxed">
            Students should never be locked out of advanced algorithms or system design simply because of their current semester.
            Our 13-stage roadmaps are open, flexible, and adapted strictly to your career aspirations, target language, and demonstrated performance.
          </p>
        </div>
      </div>
    </div>
  );
};

