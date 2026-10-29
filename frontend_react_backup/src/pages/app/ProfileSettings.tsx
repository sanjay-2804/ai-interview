import React, { useState } from 'react';
import { useAuth } from '../../context/AuthContext';
import { api } from '../../services/api';
import { User, Check, Settings, Save, Shield } from 'lucide-react';

export const ProfileSettings: React.FC = () => {
  const { user, refreshUser } = useAuth();
  const profile = user?.profile;

  const [college, setCollege] = useState(profile?.college || '');
  const [degree, setDegree] = useState(profile?.course || profile?.degree || 'B.Tech Computer Science');
  const [targetRole, setTargetRole] = useState(profile?.target_role || 'Software Developer');
  const [preferredLanguage, setPreferredLanguage] = useState(profile?.preferred_programming_language || profile?.preferred_language || 'Python');
  const [skillLevel, setSkillLevel] = useState(profile?.skill_level || 'Intermediate');
  const [studyHours, setStudyHours] = useState(profile?.study_availability || profile?.study_hours_per_day || 2.5);
  const [isSaving, setIsSaving] = useState<boolean>(false);
  const [savedSuccess, setSavedSuccess] = useState<boolean>(false);

  const handleSave = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsSaving(true);
    setSavedSuccess(false);
    try {
      await api.updateProfile({
        college,
        course: degree,
        degree,
        target_role: targetRole,
        preferred_programming_language: preferredLanguage,
        preferred_language: preferredLanguage,
        skill_level: skillLevel,
        study_availability: Number(studyHours),
        study_hours_per_day: Number(studyHours),
      });
      await refreshUser();
      setSavedSuccess(true);
      setTimeout(() => setSavedSuccess(false), 3000);
    } catch (err) {
      console.error('Failed to update profile settings:', err);
    } finally {
      setIsSaving(false);
    }
  };

  return (
    <div className="max-w-4xl mx-auto space-y-8 pb-16">
      {/* Header */}
      <div className="border-b border-surface-border pb-6">
        <h1 className="text-2xl sm:text-3xl font-extrabold text-navy-800 tracking-tight">
          Profile & Placement Settings
        </h1>
        <p className="mt-1 text-sm text-slateText-secondary leading-relaxed">
          Manage your account credentials, target engineering career track, and study commitment.
        </p>
      </div>

      <form onSubmit={handleSave} className="space-y-6">
        {/* Account Details Box */}
        <div className="rounded-2xl border border-surface-border bg-white p-6 shadow-subtle space-y-4">
          <h2 className="text-sm font-bold text-navy-800 border-b border-slate-100 pb-3">
            Account Information
          </h2>

          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label className="block text-xs font-semibold text-slateText-secondary mb-1">
                Full Name
              </label>
              <input
                type="text"
                disabled
                value={user?.full_name || ''}
                className="w-full rounded-lg border border-slate-200 bg-slate-50 p-2.5 text-xs text-slateText-muted"
              />
            </div>

            <div>
              <label className="block text-xs font-semibold text-slateText-secondary mb-1">
                Email Address
              </label>
              <input
                type="email"
                disabled
                value={user?.email || ''}
                className="w-full rounded-lg border border-slate-200 bg-slate-50 p-2.5 text-xs text-slateText-muted"
              />
            </div>
          </div>
        </div>

        {/* Preparation Target Box */}
        <div className="rounded-2xl border border-surface-border bg-white p-6 shadow-subtle space-y-4">
          <h2 className="text-sm font-bold text-navy-800 border-b border-slate-100 pb-3">
            Placement & Curriculum Configuration
          </h2>

          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label className="block text-xs font-semibold text-slateText-secondary mb-1">
                Target Role
              </label>
              <select
                value={targetRole}
                onChange={(e) => setTargetRole(e.target.value)}
                className="w-full rounded-lg border border-slate-300 p-2.5 text-xs text-slateText-primary focus:border-brand-600 focus:outline-none"
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
              <label className="block text-xs font-semibold text-slateText-secondary mb-1">
                Primary Programming Language
              </label>
              <select
                value={preferredLanguage}
                onChange={(e) => setPreferredLanguage(e.target.value)}
                className="w-full rounded-lg border border-slate-300 p-2.5 text-xs text-slateText-primary focus:border-brand-600 focus:outline-none"
              >
                <option value="Python">Python</option>
                <option value="Java">Java</option>
                <option value="C++">C++</option>
                <option value="JavaScript">JavaScript / TypeScript</option>
              </select>
            </div>

            <div>
              <label className="block text-xs font-semibold text-slateText-secondary mb-1">
                Current Skill Level
              </label>
              <select
                value={skillLevel}
                onChange={(e) => setSkillLevel(e.target.value)}
                className="w-full rounded-lg border border-slate-300 p-2.5 text-xs text-slateText-primary focus:border-brand-600 focus:outline-none"
              >
                <option value="Beginner">Beginner (Foundations & Syntax)</option>
                <option value="Intermediate">Intermediate (Algorithmic Problem Solving)</option>
                <option value="Advanced">Advanced (High-Performance Architecture)</option>
              </select>
            </div>

            <div>
              <label className="block text-xs font-semibold text-slateText-secondary mb-1">
                Daily Study Target (Hours)
              </label>
              <input
                type="number"
                step="0.5"
                min="0.5"
                max="8"
                value={studyHours}
                onChange={(e) => setStudyHours(parseFloat(e.target.value))}
                className="w-full rounded-lg border border-slate-300 p-2 text-xs text-slateText-primary focus:border-brand-600 focus:outline-none"
              />
            </div>
          </div>
        </div>

        {/* Submit */}
        <div className="flex items-center justify-between pt-2">
          {savedSuccess && (
            <span className="text-xs font-bold text-emerald-600 flex items-center gap-1">
              <Check className="h-4 w-4" /> Preferences saved and roadmap updated.
            </span>
          )}
          <div className="ml-auto">
            <button
              type="submit"
              disabled={isSaving}
              className="inline-flex items-center gap-2 rounded-xl bg-brand-600 px-6 py-2.5 text-xs font-bold text-white shadow hover:bg-brand-700 disabled:opacity-50 transition-all cursor-pointer"
            >
              <Save className="h-4 w-4" />
              {isSaving ? 'Saving...' : 'Save Settings'}
            </button>
          </div>
        </div>
      </form>
    </div>
  );
};

