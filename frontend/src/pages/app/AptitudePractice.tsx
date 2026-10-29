import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { api } from '../../services/api';
import {
  Brain, Calculator, BookMarked, ArrowRight, CheckCircle2, Sparkles, Filter,
  Timer, Award, Calendar, Target, Zap, HelpCircle, Layers, PieChart, FileText
} from 'lucide-react';

export const AptitudePractice: React.FC = () => {
  const navigate = useNavigate();
  const [selectedMode, setSelectedMode] = useState<
    'practice' | 'timed' | 'mock_placement' | 'daily_challenge' | 'weak_topic' | 'learn'
  >('practice');
  const [subcategory, setSubcategory] = useState<string>('quantitative');
  const [difficulty, setDifficulty] = useState<string>('all');
  const [questionCount, setQuestionCount] = useState<number>(10);
  const [timedDurationMinutes, setTimedDurationMinutes] = useState<number>(15);
  const [isStarting, setIsStarting] = useState<boolean>(false);
  const [errorMsg, setErrorMsg] = useState<string | null>(null);

  const subcategories = [
    { id: 'quantitative', label: 'Quantitative Aptitude', count: '41 Topics', desc: 'Percentages, Time & Work, Speed & Distance, HCF/LCM, Algebra, Mensuration' },
    { id: 'logical', label: 'Logical Reasoning', count: '24 Topics', desc: 'Syllogisms, Blood Relations, Seating Arrangements, Clocks & Calendars' },
    { id: 'verbal', label: 'Verbal Ability & English', count: '21 Topics', desc: 'Grammar Rules, Subject-Verb Agreement, Synonyms, Para Jumbles' },
    { id: 'placement', label: 'Company-Style Tests', count: 'Top IT & Product', desc: 'TCS, Infosys, Wipro, Accenture, Cognizant, Amazon practice sets' }
  ];

  const modes = [
    {
      id: 'practice',
      title: 'Mode B: Topic Practice',
      desc: 'Step-by-step learning loop with in-depth mathematical reasoning after every single question.',
      icon: Target,
      badge: 'Recommended for Concepts'
    },
    {
      id: 'timed',
      title: 'Mode D: Timed Placement Test',
      desc: 'Realistic countdown timer, question status palette, mark-for-review, and end-of-test scorecard.',
      icon: Timer,
      badge: 'Speed & Exam Pressure'
    },
    {
      id: 'mock_placement',
      title: 'Mode E: Full Placement Mock Test',
      desc: 'Comprehensive multi-section assessment covering Quantitative, Logical, Verbal, and Data Interpretation.',
      icon: Award,
      badge: 'Campus Drive Screening'
    },
    {
      id: 'daily_challenge',
      title: 'Mode F: Daily Placement Challenge',
      desc: 'Curated 10-question placement sprint to build and maintain your daily preparation streak.',
      icon: Calendar,
      badge: 'Daily Streak'
    },
    {
      id: 'weak_topic',
      title: 'Mode G: Weak Topic Improvement',
      desc: 'Targeted questions specifically generated from topics where your historical accuracy is below 65%.',
      icon: Zap,
      badge: 'Personalized Focus'
    },
    {
      id: 'learn',
      title: 'Mode A: Learn Topic Formulas',
      desc: 'Review mathematical theorems, shortcuts, and solved example walkthroughs before testing.',
      icon: FileText,
      badge: 'Formulas & Cheatsheet'
    }
  ];

  const handleStartSession = async () => {
    setIsStarting(true);
    setErrorMsg(null);

    try {
      const qCount = selectedMode === 'mock_placement' ? 20 : (selectedMode === 'daily_challenge' ? 10 : questionCount);
      const timeLimitSecs = (selectedMode === 'timed' || selectedMode === 'mock_placement')
        ? timedDurationMinutes * 60
        : undefined;

      const session = await api.startPracticeSession({
        category: 'aptitude',
        subcategory: selectedMode === 'mock_placement' ? undefined : subcategory,
        difficulty: difficulty === 'all' ? undefined : difficulty,
        question_count: qCount,
        session_mode: selectedMode,
        time_limit_seconds: timeLimitSecs
      });

      navigate(`/app/practice/session/${session.id}`);
    } catch (err: any) {
      setErrorMsg(err.message || 'Failed to initialize aptitude assessment.');
    } finally {
      setIsStarting(false);
    }
  };

  return (
    <div className="max-w-6xl mx-auto space-y-8 pb-16">
      {/* Header */}
      <div className="border-b border-surface-border pb-6">
        <div className="flex items-center gap-2 text-xs font-bold uppercase tracking-wider text-brand-600 mb-1">
          <Brain className="h-4 w-4" />
          <span>Aptitude & Placement Assessment Centre (540+ Validated Questions)</span>
        </div>
        <h1 className="text-2xl sm:text-3xl font-extrabold text-navy-800 tracking-tight">
          Aptitude & Campus Placement Mastery
        </h1>
        <p className="mt-2 text-sm text-slateText-secondary max-w-3xl leading-relaxed">
          Prepare for technical campus recruitment and competitive tests. Every submitted question features a
          comprehensive 14-point explanation with step-by-step calculations, traps to avoid, and speed shortcuts.
        </p>
      </div>

      {errorMsg && (
        <div className="rounded-2xl border border-rose-200 bg-rose-50 p-4 text-xs font-medium text-rose-800">
          {errorMsg}
        </div>
      )}

      {/* Mode Selection Cards */}
      <div className="space-y-3">
        <div className="flex items-center justify-between">
          <h2 className="text-xs font-bold uppercase tracking-wider text-slateText-secondary">
            Select Placement Learning Mode
          </h2>
          <span className="text-xs text-brand-700 font-semibold">7 Validated Learning Modes</span>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          {modes.map((m) => {
            const Icon = m.icon;
            const isSelected = selectedMode === m.id;
            return (
              <div
                key={m.id}
                onClick={() => setSelectedMode(m.id as any)}
                className={`rounded-2xl border p-5 transition-all cursor-pointer group ${
                  isSelected
                    ? 'border-brand-600 bg-blue-50/50 shadow-sm ring-1 ring-brand-600/20'
                    : 'border-surface-border bg-white hover:border-brand-300 hover:shadow-subtle'
                }`}
              >
                <div className="flex items-center justify-between mb-3">
                  <div className={`flex h-10 w-10 items-center justify-center rounded-xl transition-colors ${
                    isSelected ? 'bg-brand-600 text-white' : 'bg-blue-100 text-brand-700 group-hover:scale-105'
                  }`}>
                    <Icon className="h-5 w-5" />
                  </div>
                  <span className={`text-[10px] font-bold uppercase tracking-wider px-2 py-0.5 rounded ${
                    isSelected ? 'bg-brand-100 text-brand-800' : 'bg-slate-100 text-slateText-muted'
                  }`}>
                    {m.badge}
                  </span>
                </div>
                <h3 className="text-sm font-bold text-navy-800 group-hover:text-brand-700 transition-colors">
                  {m.title}
                </h3>
                <p className="mt-1 text-xs text-slateText-secondary leading-relaxed">
                  {m.desc}
                </p>
              </div>
            );
          })}
        </div>
      </div>

      {/* Mode A: Formula & Theory Modal/Section if selected */}
      {selectedMode === 'learn' && (
        <div className="rounded-2xl border border-brand-200 bg-white p-6 sm:p-8 shadow-card space-y-5 animate-fadeIn">
          <div className="flex items-center gap-2 border-b border-slate-100 pb-4">
            <FileText className="h-5 w-5 text-brand-600" />
            <h3 className="text-base font-bold text-navy-800">Essential Mathematical Formulas & Shortcuts Cheatsheet</h3>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs leading-relaxed text-slateText-primary">
            <div className="p-4 rounded-xl bg-slate-50 border border-slate-200 space-y-2">
              <h4 className="font-bold text-brand-700">Percentages & Profit-Loss</h4>
              <p>• <strong>Profit %</strong> = (Profit / Cost Price) × 100</p>
              <p>• <strong>Loss %</strong> = (Loss / Cost Price) × 100</p>
              <p>• <strong>Discount %</strong> = (Discount / Marked Price) × 100</p>
              <p>• <strong>Price Rise Consumption Rule</strong>: If price rises by R%, consumption drops by [R / (100 + R)] × 100%.</p>
            </div>
            <div className="p-4 rounded-xl bg-slate-50 border border-slate-200 space-y-2">
              <h4 className="font-bold text-brand-700">Time, Speed & Work</h4>
              <p>• <strong>Speed Conversion</strong>: 1 km/h = 5/18 m/s; 1 m/s = 18/5 km/h</p>
              <p>• <strong>Combined Work</strong>: Time = (A × B) / (A + B) days</p>
              <p>• <strong>Relative Speed (Opposite)</strong>: S1 + S2</p>
              <p>• <strong>Relative Speed (Same Direction)</strong>: |S1 - S2|</p>
            </div>
            <div className="p-4 rounded-xl bg-slate-50 border border-slate-200 space-y-2">
              <h4 className="font-bold text-brand-700">Compound & Simple Interest</h4>
              <p>• <strong>SI</strong> = (P × R × T) / 100</p>
              <p>• <strong>CI - SI (2 Years)</strong> = P × (R / 100)²</p>
              <p>• <strong>Rule of 72</strong>: Years to double money ≈ 72 / Interest Rate</p>
            </div>
            <div className="p-4 rounded-xl bg-slate-50 border border-slate-200 space-y-2">
              <h4 className="font-bold text-brand-700">Clocks, Calendars & Combinations</h4>
              <p>• <strong>Clock Angle</strong>: |30H - 5.5M| degrees</p>
              <p>• <strong>Leap Year</strong>: Adds 2 odd days (ordinary year adds 1 odd day)</p>
              <p>• <strong>Combinations</strong>: nCr = n! / (r! × (n-r)!)</p>
            </div>
          </div>
          <div className="pt-2">
            <button
              onClick={() => setSelectedMode('practice')}
              className="inline-flex items-center gap-2 rounded-xl bg-brand-600 px-5 py-2.5 text-xs font-bold text-white hover:bg-brand-700 shadow-sm"
            >
              Start Practicing Questions Now
              <ArrowRight className="h-4 w-4" />
            </button>
          </div>
        </div>
      )}

      {/* Configuration & Launch Panel */}
      <div className="rounded-2xl border border-brand-200 bg-white p-6 sm:p-8 shadow-card space-y-6">
        <div className="flex items-center justify-between border-b border-slate-100 pb-4">
          <div className="flex items-center gap-2">
            <Filter className="h-4 w-4 text-brand-600" />
            <h3 className="text-base font-bold text-navy-800">
              Configure {modes.find((m) => m.id === selectedMode)?.title}
            </h3>
          </div>
          <span className="text-xs font-medium text-slateText-muted">
            {selectedMode === 'mock_placement' ? '20 Questions • 4 Sections' : `${questionCount} Questions`}
          </span>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {/* Subcategory */}
          <div>
            <label className="block text-xs font-bold uppercase tracking-wider text-slateText-secondary mb-2.5">
              Topic Module
            </label>
            <div className="space-y-2">
              {subcategories.map((sub) => (
                <button
                  key={sub.id}
                  type="button"
                  onClick={() => setSubcategory(sub.id)}
                  className={`w-full text-left p-3 rounded-xl border text-xs transition-all ${
                    subcategory === sub.id
                      ? 'border-brand-600 bg-blue-50/60 font-bold text-navy-800 shadow-2xs'
                      : 'border-slate-200 bg-white text-slateText-secondary hover:border-slate-300'
                  }`}
                >
                  <div className="flex items-center justify-between">
                    <span>{sub.label}</span>
                    <span className="text-[10px] text-brand-700 font-semibold">{sub.count}</span>
                  </div>
                </button>
              ))}
            </div>
          </div>

          {/* Difficulty */}
          <div>
            <label className="block text-xs font-bold uppercase tracking-wider text-slateText-secondary mb-2.5">
              Target Difficulty
            </label>
            <div className="space-y-2">
              {[
                { id: 'all', label: 'All Difficulties (Adaptive Mix)' },
                { id: 'beginner', label: 'Beginner (Campus Screening)' },
                { id: 'intermediate', label: 'Intermediate (Technical Round)' },
                { id: 'advanced', label: 'Advanced (Product & Top Tech)' }
              ].map((diff) => (
                <button
                  key={diff.id}
                  type="button"
                  onClick={() => setDifficulty(diff.id)}
                  className={`w-full text-left p-3 rounded-xl border text-xs transition-all ${
                    difficulty === diff.id
                      ? 'border-brand-600 bg-blue-50/60 font-bold text-navy-800 shadow-2xs'
                      : 'border-slate-200 bg-white text-slateText-secondary hover:border-slate-300'
                  }`}
                >
                  {diff.label}
                </button>
              ))}
            </div>
          </div>

          {/* Assessment Parameters */}
          <div className="space-y-4">
            <div>
              <label className="block text-xs font-bold uppercase tracking-wider text-slateText-secondary mb-2.5">
                Question Count
              </label>
              <div className="grid grid-cols-3 gap-2">
                {[5, 10, 20].map((num) => (
                  <button
                    key={num}
                    type="button"
                    onClick={() => setQuestionCount(num)}
                    className={`py-2.5 rounded-xl border text-xs font-bold transition-all ${
                      questionCount === num
                        ? 'border-brand-600 bg-brand-600 text-white shadow-2xs'
                        : 'border-slate-200 bg-white text-slateText-secondary hover:border-slate-300'
                    }`}
                  >
                    {num} Qs
                  </button>
                ))}
              </div>
            </div>

            {(selectedMode === 'timed' || selectedMode === 'mock_placement') && (
              <div>
                <label className="block text-xs font-bold uppercase tracking-wider text-slateText-secondary mb-2.5">
                  Countdown Timer Limit
                </label>
                <div className="grid grid-cols-3 gap-2">
                  {[10, 15, 25].map((mins) => (
                    <button
                      key={mins}
                      type="button"
                      onClick={() => setTimedDurationMinutes(mins)}
                      className={`py-2.5 rounded-xl border text-xs font-bold transition-all ${
                        timedDurationMinutes === mins
                          ? 'border-brand-600 bg-brand-600 text-white shadow-2xs'
                          : 'border-slate-200 bg-white text-slateText-secondary hover:border-slate-300'
                      }`}
                    >
                      {mins} Mins
                    </button>
                  ))}
                </div>
              </div>
            )}

            <div className="pt-2">
              <button
                type="button"
                onClick={handleStartSession}
                disabled={isStarting}
                className="w-full flex items-center justify-center gap-2 rounded-xl bg-brand-600 px-6 py-3.5 text-sm font-bold text-white shadow-sm hover:bg-brand-700 active:scale-[0.98] disabled:opacity-50 transition-all"
              >
                {isStarting ? (
                  <>
                    <div className="h-4 w-4 animate-spin rounded-full border-2 border-white border-t-transparent" />
                    <span>Preparing Question Set...</span>
                  </>
                ) : (
                  <>
                    <span>Start {modes.find((m) => m.id === selectedMode)?.title.split(':')[1] || 'Assessment'}</span>
                    <ArrowRight className="h-4 w-4" />
                  </>
                )}
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
