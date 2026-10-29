import React from 'react';
import { ShieldCheck, Lock, EyeOff, Database } from 'lucide-react';

export const Privacy: React.FC = () => {
  return (
    <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-16 space-y-8">
      <div className="border-b border-surface-border pb-6">
        <h1 className="text-3xl font-extrabold text-navy-800 tracking-tight">Privacy Policy</h1>
        <p className="mt-2 text-sm text-slateText-secondary">
          Last updated: October 2026. How InterviewAI safeguards student data and learning records.
        </p>
      </div>

      <div className="rounded-2xl border border-surface-border bg-white p-6 sm:p-8 shadow-subtle space-y-6 text-sm text-slateText-primary leading-relaxed">
        <section className="space-y-2">
          <h2 className="text-base font-bold text-navy-800">1. Data Minimization & Collection</h2>
          <p className="text-slateText-secondary text-xs leading-relaxed">
            We collect only the essential information needed to personalize your placement roadmaps and evaluate question submissions: your name, email, target role, and study preferences. Resume details are accessible strictly to your authenticated session.
          </p>
        </section>

        <section className="space-y-2">
          <h2 className="text-base font-bold text-navy-800">2. Answer Keys and Assessment Integrity</h2>
          <p className="text-slateText-secondary text-xs leading-relaxed">
            Answer evaluation occurs strictly on our secure backend. Correct options and why-wrong breakdowns are never exposed in public quiz payload responses until an answer has been officially submitted by the student.
          </p>
        </section>

        <section className="space-y-2">
          <h2 className="text-base font-bold text-navy-800">3. Artificial Intelligence & Privacy</h2>
          <p className="text-slateText-secondary text-xs leading-relaxed">
            When interacting with configured AI models, requests contain only the technical question context and student response. No passwords, private authentication tokens, or extraneous identifying data are ever transmitted to third-party model providers.
          </p>
        </section>

        <section className="space-y-2">
          <h2 className="text-base font-bold text-navy-800">4. Data Ownership & Deletion</h2>
          <p className="text-slateText-secondary text-xs leading-relaxed">
            Students retain full ownership of their notes, bookmarks, and resume blueprints. You may request account deletion at any time by contacting support@interviewai.dev.
          </p>
        </section>
      </div>
    </div>
  );
};

