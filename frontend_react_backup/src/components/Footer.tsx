import React from 'react';
import { Link } from 'react-router-dom';
import { GraduationCap, Github, Linkedin, ShieldCheck, Mail } from 'lucide-react';

export const Footer: React.FC = () => {
  return (
    <footer className="border-t border-surface-border bg-white text-slateText-secondary">
      <div className="mx-auto max-w-7xl px-4 py-12 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
          {/* Brand Info */}
          <div className="space-y-4 md:col-span-1">
            <Link to="/" className="flex items-center gap-2">
              <div className="flex h-8 w-8 items-center justify-center rounded-lg bg-brand-600 text-white">
                <GraduationCap className="h-5 w-5" />
              </div>
              <span className="text-lg font-bold text-navy-800">InterviewAI</span>
            </Link>
            <p className="text-xs text-slateText-muted leading-relaxed">
              Empowering college students with concept-driven placement preparation, honest question feedback, algorithmic assessments, and structured roadmaps.
            </p>
            <div className="flex items-center gap-3 text-slateText-muted">
              <a href="https://github.com" target="_blank" rel="noreferrer" className="p-2 rounded-lg hover:bg-slate-100 hover:text-brand-600 transition-all">
                <Github className="h-4 w-4" />
              </a>
              <a href="https://linkedin.com" target="_blank" rel="noreferrer" className="p-2 rounded-lg hover:bg-slate-100 hover:text-brand-600 transition-all">
                <Linkedin className="h-4 w-4" />
              </a>
              <a href="mailto:support@interviewai.dev" className="p-2 rounded-lg hover:bg-slate-100 hover:text-brand-600 transition-all">
                <Mail className="h-4 w-4" />
              </a>
            </div>
          </div>

          {/* Quick Links */}
          <div>
            <h4 className="text-xs font-bold uppercase tracking-wider text-slateText-primary mb-3">
              Preparation Modules
            </h4>
            <ul className="space-y-2 text-xs">
              <li>
                <Link to="/placement-prep" className="hover:text-brand-600 transition-colors">
                  Aptitude & Reasoning
                </Link>
              </li>
              <li>
                <Link to="/learning-paths" className="hover:text-brand-600 transition-colors">
                  Software Engineering Roadmaps
                </Link>
              </li>
              <li>
                <Link to="/features" className="hover:text-brand-600 transition-colors">
                  Coding Assessment Sandbox
                </Link>
              </li>
              <li>
                <Link to="/features" className="hover:text-brand-600 transition-colors">
                  Mock Interview Center
                </Link>
              </li>
            </ul>
          </div>

          {/* Verified External Learning Resources */}
          <div>
            <h4 className="text-xs font-bold uppercase tracking-wider text-slateText-primary mb-3">
              Trusted Resources
            </h4>
            <ul className="space-y-2 text-xs">
              <li>
                <a href="https://developer.mozilla.org" target="_blank" rel="noreferrer" className="hover:text-brand-600">
                  MDN Web Docs
                </a>
              </li>
              <li>
                <a href="https://leetcode.com" target="_blank" rel="noreferrer" className="hover:text-brand-600">
                  LeetCode Practice
                </a>
              </li>
              <li>
                <a href="https://www.geeksforgeeks.org" target="_blank" rel="noreferrer" className="hover:text-brand-600">
                  GeeksforGeeks CS Core
                </a>
              </li>
              <li>
                <a href="https://roadmap.sh" target="_blank" rel="noreferrer" className="hover:text-brand-600">
                  Developer Roadmaps
                </a>
              </li>
            </ul>
          </div>

          {/* Legal and Integrity */}
          <div>
            <h4 className="text-xs font-bold uppercase tracking-wider text-slateText-primary mb-3">
              Academic Integrity & Legal
            </h4>
            <ul className="space-y-2 text-xs">
              <li>
                <Link to="/privacy" className="hover:text-brand-600 transition-colors">
                  Privacy Policy
                </Link>
              </li>
              <li>
                <Link to="/terms" className="hover:text-brand-600 transition-colors">
                  Terms of Service
                </Link>
              </li>
              <li>
                <Link to="/about" className="hover:text-brand-600 transition-colors">
                  About InterviewAI
                </Link>
              </li>
            </ul>
            <div className="mt-4 flex items-center gap-1.5 text-[11px] text-emerald-700 bg-emerald-50 px-2.5 py-1.5 rounded border border-emerald-200">
              <ShieldCheck className="h-4 w-4 shrink-0" />
              <span>Grounded Concept Learning</span>
            </div>
          </div>
        </div>

        <div className="mt-8 border-t border-slate-100 pt-6 flex flex-col sm:flex-row items-center justify-between text-xs text-slateText-muted">
          <p>© {new Date().getFullYear()} InterviewAI Platform. Dedicated to genuine conceptual placement mastery.</p>
          <p className="mt-2 sm:mt-0">Built with React, FastAPI & SQLAlchemy</p>
        </div>
      </div>
    </footer>
  );
};

