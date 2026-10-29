import React from 'react';
import { Link } from 'react-router-dom';
import {
  GraduationCap, ArrowRight, CheckCircle2, Sparkles, BookOpen,
  Code2, Brain, Mic, FileText, BarChart3, ShieldCheck, ChevronRight
} from 'lucide-react';

export const Home: React.FC = () => {
  const features = [
    {
      icon: Brain,
      title: 'Learn From Every Answer',
      desc: 'Never just see "Right" or "Wrong". Get step-by-step mathematical reasoning, traps to avoid, practical software examples, and memorable placement tips.',
    },
    {
      icon: Code2,
      title: 'Algorithmic Coding Sandbox',
      desc: 'Solve curated interview problems with time and space complexity validation, starter templates in Python, JS, Java, and C++, and official LeetCode links.',
    },
    {
      icon: Mic,
      title: 'Placement Mock Interviews',
      desc: 'Simulate technical and HR interviews with real-time feedback identifying missing technical concepts, STAR behavioral delivery, and model answers.',
    },
    {
      icon: BookOpen,
      title: 'Technical Learning Centre',
      desc: 'Structured curricula in OS, DBMS, Networks, OOP, and Web Systems with key takeaways and verified external reference links from MDN and W3Schools.',
    },
    {
      icon: FileText,
      title: 'ATS Resume Builder & Projects',
      desc: 'Build recruiter-approved single-page resumes with automated keyword optimization, plus industry project blueprints with database schemas.',
    },
    {
      icon: BarChart3,
      title: 'True Performance Diagnostics',
      desc: 'Authentic analytics calculated from your database submissions. Pinpoint exact weak topics and track your real daily study streak.',
    },
  ];

  const steps = [
    { num: '01', title: 'Choose Your Target Role', desc: 'Select Software Developer, Frontend, Backend, or Data Analyst.' },
    { num: '02', title: 'Calibrate Current Skill Level', desc: 'Start at Beginner, Intermediate, or Advanced without semester limits.' },
    { num: '03', title: 'Follow Personal Roadmap', desc: 'Work through an ordered 13-stage placement curriculum.' },
    { num: '04', title: 'Practise & Understand Every Answer', desc: 'Lock in retrieval practice and review the comprehensive feedback.' },
    { num: '05', title: 'Strengthen Weak Concepts', desc: 'Dynamic recommendations adapt based on your lowest accuracy areas.' },
  ];

  const paths = [
    { title: 'Software Developer', lang: 'Python / Java / C++', stages: '13 Stages', badge: 'Most Popular' },
    { title: 'Frontend Developer', lang: 'React & TypeScript', stages: '12 Stages', badge: 'High Demand' },
    { title: 'Backend Developer', lang: 'FastAPI, Node, SQL', stages: '13 Stages', badge: 'High Demand' },
    { title: 'Full-Stack Developer', lang: 'React + Python/Node', stages: '14 Stages', badge: 'Comprehensive' },
    { title: 'Data Analyst', lang: 'SQL, Python, Analytics', stages: '11 Stages', badge: 'Industry Track' },
    { title: 'Data Engineer', lang: 'Distributed Systems, SQL', stages: '12 Stages', badge: 'Advanced' },
  ];

  const faqs = [
    {
      q: 'Does InterviewAI restrict my roadmap based on my academic semester or year?',
      a: 'No. Target users include students from every semester and background. Learning paths are personalized by career goals, target language, and skill level—never blocked by academic semester.',
    },
    {
      q: 'What is the "Learn From Every Answer" philosophy?',
      a: 'Most platforms test for memorization. In InterviewAI, every single question you submit locks your answer and reveals why the correct option is right, why the incorrect choices are flawed, the exact step-by-step reasoning, and common traps.',
    },
    {
      q: 'Are the progress statistics and analytics genuine?',
      a: 'Yes. Every accuracy percentage, question count, and streak day is calculated directly from your database records. We do not use mock charts or fake stats.',
    },
    {
      q: 'How does AI integration work when external credentials are not set?',
      a: 'If an AI API key is configured, InterviewAI communicates with live Gemini endpoints. If not configured, the platform seamlessly uses our deterministic placement rubric engine—always clearly labeled without false claims.',
    },
  ];

  return (
    <div className="space-y-24 pb-20">
      {/* Hero Section */}
      <section className="relative overflow-hidden pt-12 md:pt-20">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
          <div className="text-center max-w-3xl mx-auto space-y-6">
            <div className="inline-flex items-center gap-2 rounded-full border border-brand-200 bg-brand-50 px-4 py-1.5 text-xs font-semibold text-brand-700 shadow-subtle">
              <Sparkles className="h-4 w-4 text-brand-600" />
              <span>AI-Assisted Placement Preparation Platform</span>
            </div>

            <h1 className="text-4xl sm:text-5xl lg:text-6xl font-black tracking-tight text-navy-800 leading-[1.15]">
              Prepare Smarter. Understand Deeper.{' '}
              <span className="text-brand-600 block mt-1">Get Placement Ready.</span>
            </h1>

            <p className="text-base sm:text-lg text-slateText-secondary leading-relaxed max-w-2xl mx-auto">
              Your personalized AI-assisted placement preparation platform. Learn technical concepts, practise coding and aptitude, improve interview skills, and track your progress in one place.
            </p>

            <div className="flex flex-col sm:flex-row items-center justify-center gap-3.5 pt-3">
              <Link
                to="/register"
                className="w-full sm:w-auto inline-flex items-center justify-center gap-2 rounded-xl bg-brand-600 px-8 py-3.5 text-sm font-bold text-white shadow-card hover:bg-brand-700 hover:shadow-md active:scale-[0.98] transition-all duration-150 cursor-pointer"
              >
                <span>Start Preparing Free</span>
                <ArrowRight className="h-4 w-4" />
              </Link>
              <Link
                to="/learning-paths"
                className="w-full sm:w-auto inline-flex items-center justify-center gap-2 rounded-xl border border-slate-300 bg-white px-7 py-3.5 text-sm font-bold text-slateText-primary hover:bg-slate-50 hover:border-brand-300 hover:shadow-xs active:scale-[0.98] transition-all duration-150"
              >
                <span>Explore Learning Paths</span>
              </Link>
            </div>
          </div>

          {/* Product Dashboard Preview (Clean genuine interface mock) */}
          <div className="mt-14 rounded-2xl border border-slate-300 bg-white p-3 shadow-2xl max-w-5xl mx-auto">
            <div className="rounded-xl border border-slate-200 bg-surface-ground p-6 overflow-hidden">
              <div className="flex items-center justify-between border-b border-slate-200 pb-4 mb-6">
                <div className="flex items-center gap-2">
                  <div className="h-3 w-3 rounded-full bg-rose-400" />
                  <div className="h-3 w-3 rounded-full bg-amber-400" />
                  <div className="h-3 w-3 rounded-full bg-emerald-400" />
                  <span className="ml-3 text-xs font-mono font-medium text-slateText-muted">
                    interviewai.dev/app/dashboard
                  </span>
                </div>
                <span className="text-xs font-bold text-brand-700 bg-brand-50 border border-brand-200 px-2.5 py-0.5 rounded">
                  Active Student Session
                </span>
              </div>

              {/* Sample Dashboard UI Mock */}
              <div className="grid grid-cols-1 sm:grid-cols-4 gap-4 mb-6">
                <div className="bg-white p-4 rounded-xl border border-slate-200 shadow-subtle">
                  <span className="text-[10px] uppercase font-bold text-slateText-muted">Accuracy</span>
                  <div className="text-xl font-black text-brand-700 mt-1">82.4%</div>
                  <span className="text-[10px] text-slateText-secondary">Across 45 Questions</span>
                </div>
                <div className="bg-white p-4 rounded-xl border border-slate-200 shadow-subtle">
                  <span className="text-[10px] uppercase font-bold text-slateText-muted">Coding Problems</span>
                  <div className="text-xl font-black text-amber-600 mt-1">12 Solved</div>
                  <span className="text-[10px] text-slateText-secondary">Arrays & Two Pointers</span>
                </div>
                <div className="bg-white p-4 rounded-xl border border-slate-200 shadow-subtle">
                  <span className="text-[10px] uppercase font-bold text-slateText-muted">Active Streak</span>
                  <div className="text-xl font-black text-orange-600 mt-1">6 Days</div>
                  <span className="text-[10px] text-slateText-secondary">Continuous consistency</span>
                </div>
                <div className="bg-white p-4 rounded-xl border border-slate-200 shadow-subtle">
                  <span className="text-[10px] uppercase font-bold text-slateText-muted">Roadmap</span>
                  <div className="text-xl font-black text-emerald-600 mt-1">Stage 4 of 13</div>
                  <span className="text-[10px] text-slateText-secondary">OOP & System Design</span>
                </div>
              </div>

              {/* Sample Locked Question Feedback Bar */}
              <div className="rounded-xl border border-emerald-300 bg-emerald-50/50 p-4 text-xs">
                <div className="flex items-center justify-between font-bold text-emerald-900 mb-1">
                  <span>Question #12 Submitted & Evaluated (Correct: Option B)</span>
                  <span className="bg-emerald-600 text-white px-2 py-0.5 rounded text-[10px]">LOCKED</span>
                </div>
                <p className="text-slateText-secondary">
                  "Step-by-step breakdown: Pipe A fills 1/12/hr, Pipe B drains 1/18/hr. Net rate = 1/36/hr = 36 hours total. Avoid adding the rates!"
                </p>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Feature Highlights Grid */}
      <section className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <div className="text-center max-w-2xl mx-auto mb-16">
          <h2 className="text-3xl font-extrabold text-navy-800 tracking-tight">
            Engineered for Deep Understanding
          </h2>
          <p className="mt-2 text-sm text-slateText-secondary">
            Everything college students need to succeed in campus recruitment and technical assessments.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {features.map((feat, idx) => {
            const Icon = feat.icon;
            return (
              <div
                key={idx}
                className="rounded-2xl border border-surface-border bg-white p-8 sm:p-9 shadow-subtle hover:-translate-y-1.5 hover:shadow-card-hover hover:border-brand-300 transition-all duration-200 group cursor-pointer"
              >
                <div className="flex h-12 w-12 items-center justify-center rounded-2xl bg-brand-50 text-brand-600 mb-5 shadow-2xs group-hover:scale-110 transition-transform">
                  <Icon className="h-6 w-6" />
                </div>
                <h3 className="text-lg font-bold text-navy-800 mb-2 group-hover:text-brand-700 transition-colors">
                  {feat.title}
                </h3>
                <p className="text-sm text-slateText-secondary leading-relaxed">{feat.desc}</p>
              </div>
            );
          })}
        </div>
      </section>

      {/* How It Works */}
      <section className="bg-white border-y border-surface-border py-20">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
          <div className="text-center max-w-2xl mx-auto mb-16">
            <span className="text-xs font-bold uppercase tracking-wider text-brand-600">The Student Journey</span>
            <h2 className="text-3xl font-extrabold text-navy-800 tracking-tight mt-1">
              How InterviewAI Prepares You
            </h2>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-5 gap-6">
            {steps.map((step) => (
              <div key={step.num} className="rounded-xl border border-slate-200 bg-surface-ground p-6 space-y-2">
                <span className="text-2xl font-black text-brand-600">{step.num}</span>
                <h4 className="text-sm font-bold text-navy-800">{step.title}</h4>
                <p className="text-xs text-slateText-secondary leading-relaxed">{step.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Learning Paths Preview */}
      <section className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-12">
          <div>
            <h2 className="text-3xl font-extrabold text-navy-800 tracking-tight">
              Configurable Career Learning Paths
            </h2>
            <p className="text-sm text-slateText-secondary mt-1">
              Select your path and learn at your own pace without semester barriers.
            </p>
          </div>
          <Link
            to="/learning-paths"
            className="inline-flex items-center gap-1.5 text-sm font-bold text-brand-600 hover:text-brand-800"
          >
            <span>View All Paths</span>
            <ArrowRight className="h-4 w-4" />
          </Link>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
          {paths.map((p, idx) => (
            <div
              key={idx}
              className="rounded-2xl border border-surface-border bg-white p-6 shadow-subtle hover:border-brand-300 transition-all flex flex-col justify-between"
            >
              <div>
                <div className="flex items-center justify-between mb-3">
                  <span className="text-[10px] font-bold uppercase px-2 py-0.5 rounded bg-brand-100 text-brand-800">
                    {p.badge}
                  </span>
                  <span className="text-xs text-slateText-muted">{p.stages}</span>
                </div>
                <h3 className="text-base font-bold text-navy-800 mb-1">{p.title}</h3>
                <p className="text-xs text-slateText-secondary font-medium">Stack: {p.lang}</p>
              </div>

              <div className="mt-6 pt-4 border-t border-slate-100 flex items-center justify-between">
                <Link
                  to="/register"
                  className="inline-flex items-center gap-1 text-xs font-bold text-brand-600 hover:text-brand-800"
                >
                  Start This Track <ChevronRight className="h-3.5 w-3.5" />
                </Link>
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* Frequently Asked Questions */}
      <section className="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-12">
          <h2 className="text-3xl font-extrabold text-navy-800 tracking-tight">
            Frequently Asked Questions
          </h2>
          <p className="mt-1 text-sm text-slateText-secondary">
            Transparent information about our architecture and pedagogical philosophy.
          </p>
        </div>

        <div className="space-y-4">
          {faqs.map((faq, idx) => (
            <div key={idx} className="rounded-xl border border-surface-border bg-white p-6 shadow-subtle space-y-2">
              <h3 className="text-sm font-bold text-navy-800">{faq.q}</h3>
              <p className="text-xs text-slateText-secondary leading-relaxed">{faq.a}</p>
            </div>
          ))}
        </div>
      </section>

      {/* Final Call to Action */}
      <section className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <div className="rounded-3xl bg-gradient-to-r from-brand-700 via-brand-600 to-brand-800 p-8 sm:p-14 text-center text-white shadow-card">
          <h2 className="text-3xl sm:text-4xl font-extrabold tracking-tight">
            Ready to Accelerate Your Placement Preparation?
          </h2>
          <p className="mt-3 text-sm sm:text-base text-brand-100 max-w-xl mx-auto leading-relaxed">
            Create your account today, calibrate your skills, and master technical and aptitude concepts with step-by-step explanations.
          </p>
          <div className="mt-8 flex flex-col sm:flex-row items-center justify-center gap-3">
            <Link
              to="/register"
              className="inline-flex items-center gap-2 rounded-xl bg-white px-8 py-3.5 text-sm font-bold text-brand-700 shadow hover:bg-brand-50 transition-all cursor-pointer"
            >
              Get Started Free
              <ArrowRight className="h-4 w-4" />
            </Link>
            <Link
              to="/login"
              className="inline-flex items-center gap-2 rounded-xl border border-white/40 bg-white/10 px-7 py-3.5 text-sm font-semibold text-white hover:bg-white/20 transition-all"
            >
              Sign In to Account
            </Link>
          </div>
        </div>
      </section>
    </div>
  );
};

