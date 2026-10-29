import React from 'react';
import { Link } from 'react-router-dom';
import {
  Brain, Code2, Mic, BookOpen, FileText, BarChart3,
  CheckCircle2, ArrowRight, ShieldCheck, Lock, Sparkles
} from 'lucide-react';

export const Features: React.FC = () => {
  return (
    <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-16 space-y-16">
      {/* Header */}
      <div className="text-center max-w-3xl mx-auto space-y-4">
        <span className="text-xs font-bold uppercase tracking-wider text-brand-600 bg-brand-50 px-3 py-1 rounded-full border border-brand-200">
          Platform Architecture & Capabilities
        </span>
        <h1 className="text-3xl sm:text-4xl font-extrabold text-navy-800 tracking-tight">
          Everything You Need to Get Placement Ready
        </h1>
        <p className="text-sm text-slateText-secondary leading-relaxed">
          InterviewAI replaces superficial quiz tests with deep retrieval practice. Every feature is designed around conceptual clarity, honest feedback, and measurable growth.
        </p>
      </div>

      {/* Feature 1: Learn from Every Answer */}
      <div className="rounded-3xl border border-surface-border bg-white p-8 sm:p-12 shadow-card hover:border-brand-300 hover:shadow-card-hover hover:-translate-y-1 transition-all duration-300 grid grid-cols-1 md:grid-cols-2 gap-10 items-center">
        <div className="space-y-5">
          <div className="flex h-14 w-14 items-center justify-center rounded-2xl bg-blue-100 text-brand-600 shadow-xs">
            <Brain className="h-7 w-7" />
          </div>
          <h2 className="text-2xl sm:text-3xl font-extrabold text-navy-800 tracking-tight">Learn From Every Answer</h2>
          <p className="text-sm text-slateText-secondary leading-relaxed font-medium">
            Submitting an answer locks your choice and immediately generates a comprehensive pedagogical breakdown.
            Understand the exact step-by-step reasoning, see a real-world placement example, learn common pitfalls to avoid, and read why incorrect choices are wrong.
          </p>
          <ul className="space-y-3 text-xs text-slateText-primary font-bold">
            <li className="flex items-center gap-2.5">
              <CheckCircle2 className="h-4 w-4 text-emerald-600 shrink-0" />
              Locked submissions enforce honest memory retrieval.
            </li>
            <li className="flex items-center gap-2.5">
              <CheckCircle2 className="h-4 w-4 text-emerald-600 shrink-0" />
              Detailed breakdown of why alternative options fail.
            </li>
            <li className="flex items-center gap-2.5">
              <CheckCircle2 className="h-4 w-4 text-emerald-600 shrink-0" />
              Explicit "Next Question" progression to give you time to study.
            </li>
          </ul>
        </div>
        <div className="rounded-2xl border border-slate-200 bg-slate-50/90 p-7 text-xs font-mono space-y-2.5 shadow-inner">
          <div className="text-brand-700 font-bold font-sans uppercase tracking-wider text-[11px] mb-2">Pedagogical Feedback Structure:</div>
          <div className="text-slate-700 font-medium">• Result status: Correct / Incorrect</div>
          <div className="text-slate-700 font-medium">• Step-by-step mathematical reasoning</div>
          <div className="text-slate-700 font-medium">• Why Option A, C, D are wrong breakdown</div>
          <div className="text-slate-700 font-medium">• Practical placement example</div>
          <div className="text-slate-700 font-medium">• Typical pitfalls and tricks to avoid</div>
          <div className="text-slate-700 font-medium">• Quick learning tip and related concept link</div>
        </div>
      </div>

      {/* Feature 2: Coding Sandbox */}
      <div className="rounded-3xl border border-surface-border bg-white p-8 sm:p-12 shadow-card hover:border-brand-300 hover:shadow-card-hover hover:-translate-y-1 transition-all duration-300 grid grid-cols-1 md:grid-cols-2 gap-10 items-center">
        <div className="order-2 md:order-1 rounded-2xl border border-slate-200 bg-slate-50/90 p-7 text-xs font-mono text-slate-800 space-y-3 shadow-inner">
          <div className="flex items-center justify-between text-slateText-secondary font-sans border-b border-slate-200 pb-3">
            <span className="font-bold text-navy-800">Solution.py</span>
            <span className="text-emerald-700 font-bold bg-emerald-50 px-3 py-1 rounded-full border border-emerald-200 text-[10px]">Time: O(N) | Space: O(N)</span>
          </div>
          <pre className="text-slate-800 leading-relaxed font-semibold">
{`def twoSum(nums: list[int], target: int):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []`}
          </pre>
        </div>
        <div className="order-1 md:order-2 space-y-5">
          <div className="flex h-14 w-14 items-center justify-center rounded-2xl bg-amber-100 text-amber-600 shadow-xs">
            <Code2 className="h-7 w-7" />
          </div>
          <h2 className="text-2xl sm:text-3xl font-extrabold text-navy-800 tracking-tight">Dedicated Coding Sandbox</h2>
          <p className="text-sm text-slateText-secondary leading-relaxed font-medium">
            Solve curated interview problems across 20 algorithmic categories.
            Write code in Python, JavaScript, Java, or C++ with starter templates, sample test case verification, and official LeetCode / GeeksforGeeks links.
          </p>
        </div>
      </div>

      {/* Feature 3: Mock Interview Centre */}
      <div className="rounded-3xl border border-surface-border bg-white p-8 sm:p-12 shadow-card hover:border-brand-300 hover:shadow-card-hover hover:-translate-y-1 transition-all duration-300 grid grid-cols-1 md:grid-cols-2 gap-10 items-center">
        <div className="space-y-5">
          <div className="flex h-14 w-14 items-center justify-center rounded-2xl bg-purple-100 text-purple-600 shadow-xs">
            <Mic className="h-7 w-7" />
          </div>
          <h2 className="text-2xl sm:text-3xl font-extrabold text-navy-800 tracking-tight">Placement Mock Interview Lab</h2>
          <p className="text-sm text-slateText-secondary leading-relaxed font-medium">
            Practice technical screening and HR behavioral questions. Receive immediate structured feedback that highlights your strengths, identifies missing technical aspects, and provides high-scoring model responses.
          </p>
        </div>
        <div className="rounded-2xl border border-purple-200 bg-purple-50/50 p-7 text-xs space-y-2.5 shadow-xs">
          <div className="text-purple-900 font-bold font-sans uppercase tracking-wider text-[11px] mb-2">Interview Evaluation Rubric:</div>
          <div className="text-slateText-secondary font-medium">• Readiness score out of 10</div>
          <div className="text-slateText-secondary font-medium">• Key technical aspects covered vs missing</div>
          <div className="text-slateText-secondary font-medium">• Recommendations for structured storytelling (STAR)</div>
          <div className="text-slateText-secondary font-medium">• Benchmark answer for comparison</div>
        </div>
      </div>

      {/* CTA */}
      <div className="text-center pt-8">
        <Link
          to="/register"
          className="inline-flex items-center gap-2 rounded-2xl bg-brand-600 px-9 py-4 text-sm font-extrabold text-white shadow-card hover:bg-brand-700 hover:shadow-card-hover active:scale-[0.98] transition-all"
        >
          Start Preparing Now
          <ArrowRight className="h-4 w-4" />
        </Link>
      </div>
    </div>
  );
};

