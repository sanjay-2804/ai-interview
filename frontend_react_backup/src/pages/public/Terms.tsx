import React from 'react';

export const Terms: React.FC = () => {
  return (
    <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-16 space-y-8">
      <div className="border-b border-surface-border pb-6">
        <h1 className="text-3xl font-extrabold text-navy-800 tracking-tight">Terms of Service</h1>
        <p className="mt-2 text-sm text-slateText-secondary">
          Academic terms and acceptable use guidelines for the InterviewAI educational platform.
        </p>
      </div>

      <div className="rounded-2xl border border-surface-border bg-white p-6 sm:p-8 shadow-subtle space-y-6 text-sm text-slateText-primary leading-relaxed">
        <section className="space-y-2">
          <h2 className="text-base font-bold text-navy-800">1. Educational Purpose</h2>
          <p className="text-slateText-secondary text-xs leading-relaxed">
            InterviewAI is an educational preparation platform designed to help students understand core computer science, algorithmic coding, and placement aptitude concepts. AI-generated feedback and practice scores represent prep diagnostics and do not constitute an official employment guarantee with any hiring partner.
          </p>
        </section>

        <section className="space-y-2">
          <h2 className="text-base font-bold text-navy-800">2. Account Responsibility</h2>
          <p className="text-slateText-secondary text-xs leading-relaxed">
            Users are responsible for maintaining the confidentiality of their credentials. Reverse engineering, running automated scraper bots against the question bank, or attempting to compromise execution environments is strictly prohibited.
          </p>
        </section>

        <section className="space-y-2">
          <h2 className="text-base font-bold text-navy-800">3. External Links & Fair Attribution</h2>
          <p className="text-slateText-secondary text-xs leading-relaxed">
            InterviewAI links to authoritative external documentation (e.g. MDN Web Docs, LeetCode, GeeksforGeeks) for student reference. Such links do not imply an official corporate affiliation or endorsement by those external third-party platforms.
          </p>
        </section>
      </div>
    </div>
  );
};

