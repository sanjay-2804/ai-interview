import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useAuth } from '../../context/AuthContext';
import { api } from '../../services/api';
import { Map, ArrowRight, CheckCircle2, Sparkles, BookOpen, Clock } from 'lucide-react';

export const LearningPaths: React.FC = () => {
  const { isAuthenticated, refreshUser } = useAuth();
  const navigate = useNavigate();

  const careerPaths = [
    {
      roleKey: 'Software Developer',
      title: 'Software Developer (Generalist)',
      desc: 'The gold standard for campus recruitment and tier-1 product engineering companies.',
      stages: 13,
      hours: '180 hrs',
      coreTopics: ['Data Structures & Algorithms', 'System Architecture', 'OOP in Java/Python/C++', 'DBMS & SQL', 'Operating Systems', 'Computer Networks'],
      targetRoles: ['SDE-1', 'Graduate Engineer Trainee', 'Associate Software Engineer'],
    },
    {
      roleKey: 'Frontend Developer',
      title: 'Frontend Developer',
      desc: 'Master modern component lifecycles, state management, web performance, and responsive design.',
      stages: 13,
      hours: '150 hrs',
      coreTopics: ['HTML5 & Modern CSS', 'JavaScript (ES6+) & TypeScript', 'React Architecture & Hooks', 'REST & GraphQL APIs', 'Web Security & Web Vitals'],
      targetRoles: ['Frontend Engineer', 'UI/UX Developer', 'React Specialist'],
    },
    {
      roleKey: 'Backend Developer',
      title: 'Backend Developer',
      desc: 'Build high-throughput REST APIs, database schemas, authentication, and caching services.',
      stages: 13,
      hours: '170 hrs',
      coreTopics: ['Python FastAPI / Node.js / Java Spring', 'Relational Normalization & SQL', 'Redis Caching & Queues', 'Microservices Architecture', 'Docker & CI/CD'],
      targetRoles: ['Backend Engineer', 'API Developer', 'Cloud Services Trainee'],
    },
    {
      roleKey: 'Full-Stack Developer',
      title: 'Full-Stack Developer',
      desc: 'End-to-end software delivery combining interactive user interfaces with resilient server architectures.',
      stages: 13,
      hours: '220 hrs',
      coreTopics: ['React & Tailwind CSS', 'FastAPI & PostgreSQL', 'JWT Authentication', 'Full-Stack Capstone Projects', 'Testing & Deployment'],
      targetRoles: ['Full-Stack Engineer', 'Product Developer', 'Startup Generalist'],
    },
    {
      roleKey: 'Data Analyst',
      title: 'Data Analyst & Business Intelligence',
      desc: 'Extract actionable intelligence from complex relational data using SQL, Python, and data storytelling.',
      stages: 12,
      hours: '130 hrs',
      coreTopics: ['Advanced SQL (Window Functions & CTEs)', 'Python (Pandas, NumPy)', 'Data Cleaning & ETL', 'Data Interpretation & Probability'],
      targetRoles: ['Data Analyst', 'BI Engineer', 'Analytics Associate'],
    },
    {
      roleKey: 'QA / Test Automation',
      title: 'QA & Test Automation Engineer',
      desc: 'Ensure software reliability with unit testing, integration suites, API validation, and automated test runners.',
      stages: 12,
      hours: '120 hrs',
      coreTopics: ['Software Testing Fundamentals', 'Selenium / Playwright Automation', 'Pytest / Vitest Testing Frameworks', 'API Testing with Postman'],
      targetRoles: ['QA Engineer', 'Automation Test Trainee', 'Software Development Engineer in Test (SDET)'],
    },
  ];

  const handleSelectTrack = async (roleKey: string) => {
    if (isAuthenticated) {
      try {
        await api.updateOnboarding({ target_role: roleKey });
        await refreshUser();
        navigate('/app/roadmap');
      } catch (err) {
        console.error('Failed to switch track:', err);
        navigate('/app/roadmap');
      }
    } else {
      navigate(`/register?role=${encodeURIComponent(roleKey)}`);
    }
  };

  return (
    <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-16 space-y-16">
      {/* Header */}
      <div className="text-center max-w-3xl mx-auto space-y-4">
        <span className="text-xs font-bold uppercase tracking-wider text-brand-600 bg-brand-50 px-3 py-1 rounded-full border border-brand-200">
          Career Trajectories
        </span>
        <h1 className="text-3xl sm:text-4xl font-extrabold text-navy-800 tracking-tight">
          Role-Specific Learning Roadmaps
        </h1>
        <p className="text-sm text-slateText-secondary leading-relaxed">
          Never restricted by semester or academic year. Every student can follow a structured 11-to-14 stage curriculum calibrated for their specific dream company and target engineering role.
        </p>
      </div>

      {/* Path Cards Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
        {careerPaths.map((path, idx) => (
          <div
            key={idx}
            className="rounded-2xl border border-surface-border bg-white p-8 sm:p-9 shadow-subtle hover:-translate-y-1.5 hover:shadow-card-hover hover:border-brand-300 transition-all duration-200 flex flex-col justify-between space-y-6 group cursor-pointer"
          >
            <div className="space-y-4">
              <div className="flex items-center justify-between">
                <span className="text-xs font-bold uppercase text-brand-600 bg-brand-50 border border-brand-200 px-2.5 py-0.5 rounded-full">
                  {path.stages} Structured Stages
                </span>
                <span className="flex items-center gap-1.5 text-xs text-slateText-muted font-semibold">
                  <Clock className="h-3.5 w-3.5 text-brand-600" />
                  {path.hours}
                </span>
              </div>

              <h2 className="text-xl font-bold text-navy-800 group-hover:text-brand-700 transition-colors">{path.title}</h2>
              <p className="text-xs text-slateText-secondary leading-relaxed">{path.desc}</p>

              <div>
                <h4 className="text-[11px] font-bold uppercase tracking-wider text-slateText-muted mb-2">
                  Core Topics Covered:
                </h4>
                <div className="flex flex-wrap gap-1.5">
                  {path.coreTopics.map((topic, tIdx) => (
                    <span
                      key={tIdx}
                      className="rounded-lg bg-slate-50 border border-slate-200 px-2.5 py-1 text-[11px] font-medium text-navy-800 hover:bg-brand-50 hover:border-brand-200 transition-colors"
                    >
                      {topic}
                    </span>
                  ))}
                </div>
              </div>
            </div>

            <div className="pt-4 border-t border-slate-100 flex flex-col sm:flex-row sm:items-center justify-between gap-3">
              <div className="text-[11px] text-slateText-muted font-medium">
                Prepares for: {path.targetRoles.join(', ')}
              </div>
              <button
                onClick={() => handleSelectTrack(path.roleKey)}
                className="inline-flex items-center justify-center gap-1.5 rounded-xl bg-brand-600 px-5 py-2.5 text-xs font-bold text-white shadow-sm hover:bg-brand-700 hover:shadow-md active:scale-[0.98] transition-all duration-150 cursor-pointer"
              >
                <span>{isAuthenticated ? 'Set as Active Track' : 'Select Track & Start'}</span>
                <ArrowRight className="h-3.5 w-3.5 transition-transform group-hover:translate-x-1" />
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

