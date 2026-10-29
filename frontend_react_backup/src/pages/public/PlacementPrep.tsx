import React from 'react';
import { Link } from 'react-router-dom';
import {
  Brain, Calculator, BookMarked, Code2, Mic, CheckCircle2,
  ArrowRight, ShieldCheck, HelpCircle
} from 'lucide-react';

export const PlacementPrep: React.FC = () => {
  return (
    <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-16 space-y-16">
      {/* Header */}
      <div className="text-center max-w-3xl mx-auto space-y-4">
        <span className="text-xs font-bold uppercase tracking-wider text-brand-600 bg-brand-50 px-3 py-1 rounded-full border border-brand-200">
          Campus Recruitment Strategy
        </span>
        <h1 className="text-3xl sm:text-4xl font-extrabold text-navy-800 tracking-tight">
          Comprehensive Placement Preparation
        </h1>
        <p className="text-sm text-slateText-secondary leading-relaxed">
          Recruitment processes test across multiple distinct rounds. Prepare systematically for online tests, coding challenges, technical interviews, and behavioral HR rounds.
        </p>
      </div>

      {/* Rounds Breakdown */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <div className="rounded-3xl border border-surface-border bg-white p-7 shadow-card hover:border-brand-300 hover:shadow-card-hover hover:-translate-y-1 transition-all duration-200 space-y-3.5">
          <div className="flex h-12 w-12 items-center justify-center rounded-2xl bg-blue-100 text-brand-700 font-extrabold text-base shadow-xs">
            1
          </div>
          <h3 className="text-base font-bold text-navy-800">Online Aptitude Round</h3>
          <p className="text-xs text-slateText-secondary leading-relaxed font-medium">
            Timed testing on Percentages, Profit/Loss, Time-Speed-Distance, Blood Relations, Syllogisms, and Grammar.
          </p>
        </div>

        <div className="rounded-3xl border border-surface-border bg-white p-7 shadow-card hover:border-amber-300 hover:shadow-card-hover hover:-translate-y-1 transition-all duration-200 space-y-3.5">
          <div className="flex h-12 w-12 items-center justify-center rounded-2xl bg-amber-100 text-amber-700 font-extrabold text-base shadow-xs">
            2
          </div>
          <h3 className="text-base font-bold text-navy-800">Coding Assessment</h3>
          <p className="text-xs text-slateText-secondary leading-relaxed font-medium">
            2 to 3 algorithmic problems on Arrays, Strings, Stacks, Trees, or Dynamic Programming within 60 to 90 minutes.
          </p>
        </div>

        <div className="rounded-3xl border border-surface-border bg-white p-7 shadow-card hover:border-purple-300 hover:shadow-card-hover hover:-translate-y-1 transition-all duration-200 space-y-3.5">
          <div className="flex h-12 w-12 items-center justify-center rounded-2xl bg-purple-100 text-purple-700 font-extrabold text-base shadow-xs">
            3
          </div>
          <h3 className="text-base font-bold text-navy-800">Technical Interview</h3>
          <p className="text-xs text-slateText-secondary leading-relaxed font-medium">
            Live problem solving, code complexity justification, OS process models, DBMS normalization, and project architecture deep dives.
          </p>
        </div>

        <div className="rounded-3xl border border-surface-border bg-white p-7 shadow-card hover:border-emerald-300 hover:shadow-card-hover hover:-translate-y-1 transition-all duration-200 space-y-3.5">
          <div className="flex h-12 w-12 items-center justify-center rounded-2xl bg-emerald-100 text-emerald-700 font-extrabold text-base shadow-xs">
            4
          </div>
          <h3 className="text-base font-bold text-navy-800">HR & Behavioral</h3>
          <p className="text-xs text-slateText-secondary leading-relaxed font-medium">
            Evaluating culture fit, communication clarity, teamwork, conflict resolution, and career motivation using the STAR method.
          </p>
        </div>
      </div>

      {/* Honest Placement Advice Card */}
      <div className="rounded-3xl border border-brand-200 bg-brand-50/50 p-8 sm:p-10 shadow-card space-y-4">
        <div className="flex items-center gap-2.5">
          <ShieldCheck className="h-6 w-6 text-brand-600" />
          <h2 className="text-xl font-extrabold text-navy-800">Our Core Pedagogical Pledge</h2>
        </div>
        <p className="text-sm text-slateText-secondary leading-relaxed font-medium">
          InterviewAI strictly avoids rote memorization. We do not promise magical shortcuts or fabricate placement percentages.
          Instead, we build genuine conceptual mastery so that when an interviewer asks an unexpected variant of a problem, you have the foundational problem-solving intuition to solve it from first principles.
        </p>

        <div className="pt-3">
          <Link
            to="/register"
            className="inline-flex items-center gap-2 rounded-2xl bg-brand-600 px-7 py-3 text-xs font-bold text-white shadow-sm hover:bg-brand-700 hover:shadow-md active:scale-[0.98] transition-all"
          >
            Start Preparing Now <ArrowRight className="h-4 w-4" />
          </Link>
        </div>
      </div>
    </div>
  );
};

