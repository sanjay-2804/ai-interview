import React, { useState } from 'react';
import { useAuth } from '../../context/AuthContext';
import { api } from '../../services/api';
import { Check, Sparkles, Target, Code, Clock, BookOpen, X } from 'lucide-react';

interface OnboardingModalProps {
  isOpen: boolean;
  onClose: () => void;
}

export const OnboardingModal: React.FC<OnboardingModalProps> = ({ isOpen, onClose }) => {
  const { user, refreshUser } = useAuth();
  const profile = user?.profile;

  const [college, setCollege] = useState(profile?.college || '');
  const [degree, setDegree] = useState(profile?.degree || 'B.Tech / B.E.');
  const [targetRole, setTargetRole] = useState(profile?.target_role || 'Software Developer');
  const [preferredLanguage, setPreferredLanguage] = useState(profile?.preferred_language || 'Python');
  const [skillLevel, setSkillLevel] = useState(profile?.skill_level || 'Beginner');
  const [studyHours, setStudyHours] = useState(profile?.study_hours_per_day || 2.5);
  const [isSubmitting, setIsSubmitting] = useState(false);

  if (!isOpen) return null;

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsSubmitting(true);
    try {
      await api.updateOnboarding({
        college,
        degree,
        target_role: targetRole,
        preferred_language: preferredLanguage,
        skill_level: skillLevel,
        study_hours_per_day: Number(studyHours),
        preferred_topics: ['Data Structures', 'Aptitude', 'SQL'],
        prep_priorities: ['Campus Placement', 'Product Companies'],
      });
      await refreshUser();
      onClose();
    } catch (err) {
      console.error('Failed to save onboarding:', err);
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-900/60 backdrop-blur-sm animate-in fade-in">
      <div className="w-full max-w-2xl bg-white rounded-2xl shadow-2xl border border-slate-200 overflow-hidden">
        {/* Modal Header */}
        <div className="bg-gradient-to-r from-brand-700 to-brand-600 px-6 py-5 text-white flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-white/20 backdrop-blur-md">
              <Sparkles className="h-5 w-5 text-white" />
            </div>
            <div>
              <h2 className="text-lg font-bold">Personalize Your Placement Prep</h2>
              <p className="text-xs text-brand-100">
                Tailor your learning roadmap, aptitude milestones, and coding challenges.
              </p>
            </div>
          </div>
          {profile?.onboarding_completed && (
            <button onClick={onClose} className="text-white/80 hover:text-white">
              <X className="h-5 w-5" />
            </button>
          )}
        </div>

        {/* Form Body */}
        <form onSubmit={handleSubmit} className="p-7 sm:p-9 space-y-6">
          {/* Target Role & Preferred Language */}
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-5">
            <div>
              <label className="block text-xs font-bold uppercase tracking-wider text-slateText-secondary mb-2">
                Target Career Role
              </label>
              <select
                value={targetRole}
                onChange={(e) => setTargetRole(e.target.value)}
                className="w-full rounded-xl border border-slate-300 px-3.5 py-2.5 text-xs font-medium text-slateText-primary focus:border-brand-600 focus:outline-none focus:ring-2 focus:ring-brand-500/20 shadow-xs cursor-pointer hover:border-brand-400 transition-colors"
              >
                <option value="Software Engineer">Software Engineer</option>
                <option value="Software Developer">Software Developer</option>
                <option value="Java Developer">Java Developer</option>
                <option value="Python Developer">Python Developer</option>
                <option value="Frontend Developer">Frontend Developer</option>
                <option value="Backend Developer">Backend Developer</option>
                <option value="Full-Stack Developer">Full-Stack Developer</option>
                <option value="Data Analyst">Data Analyst</option>
                <option value="Data Scientist">Data Scientist</option>
                <option value="AI / Machine Learning Engineer">AI / Machine Learning Engineer</option>
                <option value="Cybersecurity Analyst">Cybersecurity Analyst</option>
                <option value="Cloud Engineer">Cloud Engineer</option>
                <option value="DevOps Engineer">DevOps Engineer</option>
                <option value="Mobile App Developer">Mobile App Developer</option>
                <option value="QA / Software Testing Engineer">QA / Software Testing Engineer</option>
                <option value="Database Engineer">Database Engineer</option>
                <option value="Other / Explore Careers">Other / Explore Careers</option>
              </select>
            </div>

            <div>
              <label className="block text-xs font-bold uppercase tracking-wider text-slateText-secondary mb-2">
                Primary Programming Language
              </label>
              <select
                value={preferredLanguage}
                onChange={(e) => setPreferredLanguage(e.target.value)}
                className="w-full rounded-xl border border-slate-300 px-3.5 py-2.5 text-xs font-medium text-slateText-primary focus:border-brand-600 focus:outline-none focus:ring-2 focus:ring-brand-500/20 shadow-xs cursor-pointer hover:border-brand-400 transition-colors"
              >
                <option value="Python">Python</option>
                <option value="Java">Java</option>
                <option value="C++">C++</option>
                <option value="JavaScript">JavaScript / TypeScript</option>
              </select>
            </div>
          </div>

          {/* Skill Level Selection */}
          <div>
            <label className="block text-xs font-bold uppercase tracking-wider text-slateText-secondary mb-2.5">
              Current Skill Level
            </label>
            <div className="grid grid-cols-3 gap-3.5">
              {['Beginner', 'Intermediate', 'Advanced'].map((lvl) => (
                <button
                  type="button"
                  key={lvl}
                  onClick={() => setSkillLevel(lvl)}
                  className={`flex flex-col items-center justify-center p-3.5 rounded-2xl border text-center transition-all duration-200 cursor-pointer ${
                    skillLevel === lvl
                      ? 'border-brand-600 bg-brand-50 text-brand-700 font-bold shadow-xs -translate-y-0.5'
                      : 'border-slate-200 hover:border-brand-300 hover:bg-slate-50 text-slateText-secondary'
                  }`}
                >
                  <span className="text-sm font-extrabold">{lvl}</span>
                  <span className="text-[11px] text-slateText-muted mt-1 font-medium">
                    {lvl === 'Beginner' ? 'Concepts & Foundations' : lvl === 'Intermediate' ? 'Problem Solving' : 'High Performance'}
                  </span>
                </button>
              ))}
            </div>
          </div>

          {/* Daily Study Commitment */}
          <div>
            <div className="flex items-center justify-between mb-2">
              <label className="text-xs font-bold uppercase tracking-wider text-slateText-secondary flex items-center gap-2">
                <Clock className="h-4 w-4 text-brand-600" />
                Available Study Time: {studyHours} Hours/Day
              </label>
            </div>
            <input
              type="range"
              min="1"
              max="6"
              step="0.5"
              value={studyHours}
              onChange={(e) => setStudyHours(parseFloat(e.target.value))}
              className="w-full accent-brand-600 cursor-pointer h-2 bg-slate-200 rounded-lg"
            />
            <div className="flex justify-between text-[11px] text-slateText-muted mt-1.5 font-medium">
              <span>1 hr (Steady)</span>
              <span>3 hrs (Standard Placement Pace)</span>
              <span>6+ hrs (Intensive Boot Camp)</span>
            </div>
          </div>

          {/* Academic Background (Optional) */}
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 pt-3 border-t border-slate-100">
            <div>
              <label className="block text-xs font-bold uppercase tracking-wider text-slateText-secondary mb-1.5">
                College / Institution (Optional)
              </label>
              <input
                type="text"
                value={college}
                onChange={(e) => setCollege(e.target.value)}
                placeholder="e.g. National Institute of Tech"
                className="w-full rounded-xl border border-slate-300 px-3.5 py-2.5 text-xs text-slateText-primary focus:border-brand-600 focus:outline-none focus:ring-2 focus:ring-brand-500/20 shadow-xs transition-colors"
              />
            </div>
            <div>
              <label className="block text-xs font-bold uppercase tracking-wider text-slateText-secondary mb-1.5">
                Degree / Program
              </label>
              <input
                type="text"
                value={degree}
                onChange={(e) => setDegree(e.target.value)}
                placeholder="e.g. B.Tech Computer Science"
                className="w-full rounded-xl border border-slate-300 px-3.5 py-2.5 text-xs text-slateText-primary focus:border-brand-600 focus:outline-none focus:ring-2 focus:ring-brand-500/20 shadow-xs transition-colors"
              />
            </div>
          </div>

          {/* Action buttons */}
          <div className="flex items-center justify-end gap-3 pt-5 border-t border-slate-200">
            {profile?.onboarding_completed && (
              <button
                type="button"
                onClick={onClose}
                className="rounded-xl px-5 py-2.5 text-xs font-bold text-slateText-secondary hover:bg-slate-100 transition-colors cursor-pointer"
              >
                Cancel
              </button>
            )}
            <button
              type="submit"
              disabled={isSubmitting}
              className="inline-flex items-center gap-2 rounded-xl bg-brand-600 px-7 py-3 text-xs font-bold text-white shadow-sm hover:bg-brand-700 hover:shadow-md active:scale-[0.98] transition-all disabled:opacity-50 cursor-pointer"
            >
              {isSubmitting ? 'Saving Profile...' : 'Save & Build My Roadmap'}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

