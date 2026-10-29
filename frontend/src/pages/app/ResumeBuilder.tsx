import React, { useState, useEffect } from 'react';
import { api } from '../../services/api';
import { ResumeData, ProjectBlueprint } from '../../types';
import {
  FileText, Download, Sparkles, Check, Plus, Trash2,
  FolderGit2, ExternalLink, Printer, ShieldCheck, AlertCircle
} from 'lucide-react';

export const ResumeBuilder: React.FC = () => {
  const [activeTab, setActiveTab] = useState<'resume' | 'projects'>('resume');
  const [resume, setResume] = useState<ResumeData | null>(null);
  const [projects, setProjects] = useState<ProjectBlueprint[]>([]);
  const [isSaving, setIsSaving] = useState<boolean>(false);
  const [isReviewing, setIsReviewing] = useState<boolean>(false);
  const [reviewResult, setReviewResult] = useState<any>(null);
  const [saveSuccess, setSaveSuccess] = useState<boolean>(false);
  const [loading, setLoading] = useState<boolean>(true);

  useEffect(() => {
    Promise.all([api.getMyResume(), api.getProjectBlueprints()])
      .then(([resData, projData]) => {
        setResume(resData);
        if (resData.ai_review_feedback) {
          setReviewResult(resData.ai_review_feedback);
        }
        setProjects(projData);
      })
      .catch((err) => console.error('Failed to load resume/projects:', err))
      .finally(() => setLoading(false));
  }, []);

  const handleSaveResume = async () => {
    if (!resume) return;
    setIsSaving(true);
    setSaveSuccess(false);
    try {
      const updated = await api.updateMyResume(resume);
      setResume(updated);
      setSaveSuccess(true);
      setTimeout(() => setSaveSuccess(false), 3000);
    } catch (err) {
      console.error('Failed to save resume:', err);
    } finally {
      setIsSaving(false);
    }
  };

  const handleReviewResume = async () => {
    setIsReviewing(true);
    try {
      const feedback = await api.reviewResume();
      setReviewResult(feedback);
    } catch (err) {
      console.error('Failed to run resume review:', err);
    } finally {
      setIsReviewing(false);
    }
  };

  const handlePrint = () => {
    window.print();
  };

  if (loading) {
    return (
      <div className="flex h-96 items-center justify-center">
        <div className="h-8 w-8 animate-spin rounded-full border-4 border-brand-600 border-t-transparent" />
      </div>
    );
  }

  return (
    <div className="max-w-6xl mx-auto space-y-8 pb-16">
      {/* Header */}
      <div className="border-b border-surface-border pb-6 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h1 className="text-2xl sm:text-3xl font-extrabold text-navy-800 tracking-tight">
            Projects & ATS Resume Builder
          </h1>
          <p className="mt-1 text-sm text-slateText-secondary max-w-2xl leading-relaxed">
            Format a clean, recruiter-approved single-page resume with measurable outcomes.
            Explore curated industry project blueprints with database schemas and interview questions.
          </p>
        </div>

        {/* Tab Switcher */}
        <div className="flex gap-2 bg-slate-100 p-2 rounded-2xl shrink-0 shadow-inner">
          <button
            onClick={() => setActiveTab('resume')}
            className={`px-5 py-2.5 rounded-xl text-xs font-bold transition-all duration-200 cursor-pointer ${
              activeTab === 'resume'
                ? 'bg-white text-navy-800 shadow-sm -translate-y-0.5'
                : 'text-slateText-secondary hover:text-slateText-primary hover:bg-white/60'
            }`}
          >
            Resume Builder
          </button>
          <button
            onClick={() => setActiveTab('projects')}
            className={`px-5 py-2.5 rounded-xl text-xs font-bold transition-all duration-200 cursor-pointer ${
              activeTab === 'projects'
                ? 'bg-white text-navy-800 shadow-sm -translate-y-0.5'
                : 'text-slateText-secondary hover:text-slateText-primary hover:bg-white/60'
            }`}
          >
            Project Blueprints
          </button>
        </div>
      </div>

      {activeTab === 'resume' ? (
        /* RESUME BUILDER SECTION */
        <div className="space-y-6">
          {/* Action Toolbar */}
          <div className="flex flex-wrap items-center justify-between gap-4 bg-white p-5 sm:p-6 rounded-2xl border border-slate-200 shadow-card">
            <div className="flex items-center gap-2">
              <span className="text-xs font-bold text-slateText-secondary uppercase tracking-wider">Status:</span>
              {saveSuccess ? (
                <span className="text-xs font-bold text-emerald-600 flex items-center gap-1.5 bg-emerald-50 px-3 py-1 rounded-full border border-emerald-200">
                  <Check className="h-4 w-4" /> Saved to Database
                </span>
              ) : (
                <span className="text-xs text-slateText-muted font-medium">Auto-saves on manual click</span>
              )}
            </div>

            <div className="flex items-center gap-3">
              <button
                onClick={handleReviewResume}
                disabled={isReviewing}
                className="inline-flex items-center gap-2 rounded-xl border border-purple-300 bg-purple-50 px-4 py-2.5 text-xs font-bold text-purple-700 hover:bg-purple-100 hover:shadow-xs active:scale-95 transition-all cursor-pointer"
              >
                <Sparkles className="h-4 w-4" />
                {isReviewing ? 'Analyzing...' : 'Run ATS Audit'}
              </button>

              <button
                onClick={handleSaveResume}
                disabled={isSaving}
                className="inline-flex items-center gap-2 rounded-xl bg-brand-600 px-5 py-2.5 text-xs font-bold text-white shadow-sm hover:bg-brand-700 hover:shadow-md active:scale-95 transition-all cursor-pointer"
              >
                {isSaving ? 'Saving...' : 'Save Resume'}
              </button>

              <button
                onClick={handlePrint}
                className="inline-flex items-center gap-2 rounded-xl border border-slate-300 bg-white px-4 py-2.5 text-xs font-bold text-slateText-primary hover:bg-slate-50 hover:border-slate-400 active:scale-95 transition-all cursor-pointer shadow-xs"
              >
                <Printer className="h-4 w-4" />
                Print / Export PDF
              </button>
            </div>
          </div>

          {/* AI ATS Review Card (if available) */}
          {reviewResult && (
            <div className="rounded-2xl border border-purple-200 bg-purple-50/50 p-6 shadow-subtle space-y-3">
              <div className="flex items-center justify-between border-b border-purple-200/60 pb-3">
                <div className="flex items-center gap-2">
                  <Sparkles className="h-5 w-5 text-purple-600" />
                  <h3 className="text-sm font-bold text-purple-900">Resume Review & ATS Optimization</h3>
                </div>
                <div className="text-sm font-bold text-purple-700">
                  ATS Score: {reviewResult.score || 75} / 100
                </div>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
                <div>
                  <strong className="text-emerald-800 block mb-1">Strong Points:</strong>
                  <ul className="list-disc list-inside space-y-1 text-slateText-secondary">
                    {reviewResult.strengths?.map((s: string, i: number) => <li key={i}>{s}</li>)}
                  </ul>
                </div>
                <div>
                  <strong className="text-amber-800 block mb-1">Recommended Enhancements:</strong>
                  <ul className="list-disc list-inside space-y-1 text-slateText-secondary">
                    {reviewResult.improvements?.map((imp: string, i: number) => <li key={i}>{imp}</li>)}
                  </ul>
                </div>
              </div>

              {reviewResult.keyword_suggestions && (
                <div className="pt-2">
                  <span className="text-[11px] font-bold text-purple-900 block mb-1.5">
                    Recommended High-Priority ATS Keywords:
                  </span>
                  <div className="flex flex-wrap gap-1.5">
                    {reviewResult.keyword_suggestions.map((kw: string, i: number) => (
                      <span key={i} className="bg-white border border-purple-200 text-purple-800 px-2 py-0.5 rounded text-[11px] font-medium">
                        {kw}
                      </span>
                    ))}
                  </div>
                </div>
              )}
            </div>
          )}

          {/* Side-by-Side: Edit Form + Live Clean A4 Preview */}
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
            {/* Form Column (6 Cols) */}
            <div className="lg:col-span-6 space-y-4 rounded-2xl border border-surface-border bg-white p-6 shadow-subtle">
              <h3 className="text-sm font-bold text-navy-800 border-b border-slate-100 pb-3">
                Edit Resume Details
              </h3>

              {/* Personal Info */}
              <div className="grid grid-cols-2 gap-3">
                <div>
                  <label className="block text-[11px] font-semibold text-slateText-secondary mb-1">Full Name</label>
                  <input
                    type="text"
                    value={resume?.full_name || ''}
                    onChange={(e) => setResume({ ...resume!, full_name: e.target.value })}
                    className="w-full rounded-lg border border-slate-300 p-2 text-xs"
                  />
                </div>
                <div>
                  <label className="block text-[11px] font-semibold text-slateText-secondary mb-1">Email</label>
                  <input
                    type="email"
                    value={resume?.email || ''}
                    onChange={(e) => setResume({ ...resume!, email: e.target.value })}
                    className="w-full rounded-lg border border-slate-300 p-2 text-xs"
                  />
                </div>
                <div>
                  <label className="block text-[11px] font-semibold text-slateText-secondary mb-1">Phone</label>
                  <input
                    type="text"
                    value={resume?.phone || ''}
                    onChange={(e) => setResume({ ...resume!, phone: e.target.value })}
                    className="w-full rounded-lg border border-slate-300 p-2 text-xs"
                  />
                </div>
                <div>
                  <label className="block text-[11px] font-semibold text-slateText-secondary mb-1">Location</label>
                  <input
                    type="text"
                    value={resume?.location || ''}
                    onChange={(e) => setResume({ ...resume!, location: e.target.value })}
                    className="w-full rounded-lg border border-slate-300 p-2 text-xs"
                  />
                </div>
              </div>

              {/* Summary */}
              <div>
                <label className="block text-[11px] font-semibold text-slateText-secondary mb-1">
                  Professional Summary
                </label>
                <textarea
                  value={resume?.summary || ''}
                  onChange={(e) => setResume({ ...resume!, summary: e.target.value })}
                  rows={3}
                  className="w-full rounded-lg border border-slate-300 p-2 text-xs leading-relaxed"
                />
              </div>

              {/* Skills (Comma-separated) */}
              <div>
                <label className="block text-[11px] font-semibold text-slateText-secondary mb-1">
                  Technical Skills (Comma separated)
                </label>
                <input
                  type="text"
                  value={resume?.skills_json?.join(', ') || ''}
                  onChange={(e) => setResume({
                    ...resume!,
                    skills_json: e.target.value.split(',').map((s) => s.trim()).filter(Boolean)
                  })}
                  className="w-full rounded-lg border border-slate-300 p-2 text-xs"
                />
              </div>

              {/* Projects Guidance */}
              <div className="pt-2 text-xs text-slateText-muted">
                Tip: Quantify your results (e.g. "Reduced query response time by 35% using PostgreSQL B-Tree indexes").
              </div>
            </div>

            {/* Live A4 Preview Column (6 Cols) */}
            <div className="lg:col-span-6 bg-slate-100 p-4 rounded-2xl flex justify-center">
              <div
                id="resume-printable-area"
                className="w-full max-w-xl bg-white shadow-xl rounded-lg p-8 text-slateText-primary space-y-4 print:shadow-none print:p-0 print:m-0"
                style={{ minHeight: '650px', fontFamily: 'Inter, sans-serif' }}
              >
                {/* Header */}
                <div className="border-b border-slate-300 pb-3 text-center">
                  <h1 className="text-xl font-bold uppercase tracking-tight text-navy-900">
                    {resume?.full_name || 'Your Full Name'}
                  </h1>
                  <div className="flex flex-wrap justify-center gap-2 text-[10px] text-slateText-secondary mt-1">
                    {resume?.email && <span>{resume.email}</span>}
                    {resume?.phone && <span>• {resume.phone}</span>}
                    {resume?.location && <span>• {resume.location}</span>}
                    {resume?.links_json?.linkedin && <span>• LinkedIn</span>}
                    {resume?.links_json?.github && <span>• GitHub</span>}
                  </div>
                </div>

                {/* Summary */}
                {resume?.summary && (
                  <div>
                    <h2 className="text-[11px] font-bold uppercase tracking-wider text-navy-800 border-b border-slate-200 pb-0.5 mb-1">
                      Professional Summary
                    </h2>
                    <p className="text-[10px] text-slateText-secondary leading-relaxed">
                      {resume.summary}
                    </p>
                  </div>
                )}

                {/* Education */}
                {resume?.education_json && resume.education_json.length > 0 && (
                  <div>
                    <h2 className="text-[11px] font-bold uppercase tracking-wider text-navy-800 border-b border-slate-200 pb-0.5 mb-1">
                      Education
                    </h2>
                    {resume.education_json.map((edu, i) => (
                      <div key={i} className="flex justify-between text-[10px] py-0.5">
                        <div>
                          <strong className="text-navy-900">{edu.degree}</strong>
                          <div className="text-slateText-muted">{edu.institution}</div>
                        </div>
                        <div className="text-right">
                          <span className="text-slateText-muted">{edu.year}</span>
                          <div className="font-semibold text-slateText-secondary">{edu.score}</div>
                        </div>
                      </div>
                    ))}
                  </div>
                )}

                {/* Technical Skills */}
                {resume?.skills_json && resume.skills_json.length > 0 && (
                  <div>
                    <h2 className="text-[11px] font-bold uppercase tracking-wider text-navy-800 border-b border-slate-200 pb-0.5 mb-1">
                      Technical Skills
                    </h2>
                    <p className="text-[10px] text-slateText-secondary leading-relaxed">
                      {resume.skills_json.join(' • ')}
                    </p>
                  </div>
                )}

                {/* Projects */}
                {resume?.projects_json && resume.projects_json.length > 0 && (
                  <div>
                    <h2 className="text-[11px] font-bold uppercase tracking-wider text-navy-800 border-b border-slate-200 pb-0.5 mb-1">
                      Key Technical Projects
                    </h2>
                    {resume.projects_json.map((p, i) => (
                      <div key={i} className="py-1">
                        <div className="flex justify-between text-[10px]">
                          <strong className="text-navy-900">{p.title}</strong>
                          <span className="text-[9px] text-slateText-muted">{p.tech_stack}</span>
                        </div>
                        <p className="text-[10px] text-slateText-secondary leading-relaxed mt-0.5">
                          {p.description}
                        </p>
                      </div>
                    ))}
                  </div>
                )}
              </div>
            </div>
          </div>
        </div>
      ) : (
        /* PROJECT BLUEPRINTS SECTION */
        <div className="space-y-6">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {projects.map((proj) => (
              <div
                key={proj.id}
                className="rounded-2xl border border-surface-border bg-white p-7 shadow-card hover:border-brand-300 hover:shadow-card-hover hover:-translate-y-1 transition-all duration-200 space-y-4"
              >
                <div className="flex items-center justify-between">
                  <span className="text-[10px] font-bold uppercase tracking-wider px-2.5 py-1 rounded-full bg-brand-100 text-brand-800">
                    {proj.role}
                  </span>
                  <span className="text-[10px] font-bold uppercase tracking-wider px-2.5 py-1 rounded-full bg-slate-100 text-slateText-secondary">
                    {proj.difficulty}
                  </span>
                </div>

                <h3 className="text-base font-extrabold text-navy-800">{proj.title}</h3>
                <p className="text-xs text-slateText-secondary leading-relaxed font-medium">
                  {proj.problem_statement}
                </p>

                {/* Tech Stack */}
                <div className="flex flex-wrap gap-1.5">
                  {proj.tech_stack.map((t, idx) => (
                    <span key={idx} className="bg-slate-50 border border-slate-200 text-slateText-secondary px-2.5 py-1 rounded-lg text-[10px] font-bold shadow-2xs">
                      {t}
                    </span>
                  ))}
                </div>

                {/* Suggested Database Schema */}
                <div className="rounded-xl bg-slate-50 border border-slate-200 p-4 text-[11px] font-mono text-slate-800 shadow-inner">
                  <div className="text-[10px] uppercase font-sans font-bold text-slateText-secondary mb-1.5 tracking-wider">
                    Suggested Database Schema:
                  </div>
                  <pre className="whitespace-pre-line text-[10px] leading-relaxed text-slate-700">
                    {proj.database_schema}
                  </pre>
                </div>

                {/* Interview Questions Preview */}
                <div className="rounded-xl bg-amber-50/60 border border-amber-200 p-4 text-xs shadow-xs">
                  <strong className="text-amber-900 block mb-1.5 font-bold uppercase tracking-wider text-[10px]">Likely Interview Questions:</strong>
                  <ul className="list-disc list-inside space-y-1 text-amber-950 text-[11px] font-medium">
                    {proj.interview_questions.slice(0, 2).map((q, qIdx) => (
                      <li key={qIdx}>{q}</li>
                    ))}
                  </ul>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
};

