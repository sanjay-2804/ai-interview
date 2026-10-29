import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { api } from '../../services/api';
import { useAuth } from '../../context/AuthContext';
import {
  Map, CheckCircle2, Clock, ArrowRight, Sparkles, BookOpen,
  Code2, Brain, ChevronRight, Lock, Unlock, Settings2, RefreshCw
} from 'lucide-react';

export const Roadmap: React.FC = () => {
  const { refreshUser } = useAuth();
  const [roadmap, setRoadmap] = useState<any>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [isSwitching, setIsSwitching] = useState<boolean>(false);
  const [showRoleSelector, setShowRoleSelector] = useState<boolean>(false);

  const careerRoles = [
    'Software Developer',
    'Frontend Developer',
    'Backend Developer',
    'Full-Stack Developer',
    'Data Analyst',
    'QA / Test Automation'
  ];

  const fetchRoadmap = () => {
    return api.getMyRoadmap()
      .then(setRoadmap)
      .catch((err) => console.error('Failed to load roadmap:', err))
      .finally(() => setLoading(false));
  };

  useEffect(() => {
    fetchRoadmap();
  }, []);

  const handleRoleChange = async (newRole: string) => {
    setIsSwitching(true);
    try {
      await api.updateOnboarding({ target_role: newRole });
      await refreshUser();
      await fetchRoadmap();
      setShowRoleSelector(false);
    } catch (err) {
      console.error('Failed to update career path:', err);
    } finally {
      setIsSwitching(false);
    }
  };

  if (loading) {
    return (
      <div className="flex h-96 items-center justify-center">
        <div className="h-8 w-8 animate-spin rounded-full border-4 border-brand-600 border-t-transparent" />
      </div>
    );
  }

  const completedCount = roadmap?.stages?.filter((s: any) => s.status === 'completed').length || 0;
  const totalStages = roadmap?.stages?.length || 13;
  const progressPercent = Math.round((completedCount / totalStages) * 100);

  return (
    <div className="max-w-5xl mx-auto space-y-8 pb-16">
      {/* Header */}
      <div className="rounded-3xl border border-brand-200 bg-white p-7 sm:p-9 shadow-card">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-6">
          <div className="space-y-3">
            <div className="flex flex-wrap items-center gap-2">
              <span className="inline-flex items-center gap-1.5 rounded-full bg-brand-100 px-3 py-1 text-xs font-bold text-brand-800">
                <Sparkles className="h-3.5 w-3.5 text-brand-600" />
                <span>Target Career: {roadmap?.target_role} ({roadmap?.preferred_language})</span>
              </span>

              <button
                onClick={() => setShowRoleSelector(!showRoleSelector)}
                className="inline-flex items-center gap-1.5 rounded-full bg-slate-100 hover:bg-brand-50 hover:text-brand-700 hover:border-brand-300 border border-slate-200 px-3 py-1 text-xs font-bold text-slateText-secondary transition-all cursor-pointer shadow-2xs"
              >
                <Settings2 className="h-3.5 w-3.5" />
                <span>Change Career Path</span>
              </button>
            </div>

            {/* Quick Track Switcher Dropdown */}
            {showRoleSelector && (
              <div className="p-4 rounded-2xl bg-brand-50/60 border border-brand-200 space-y-2.5 animate-in fade-in duration-150">
                <div className="text-xs font-bold text-brand-900 uppercase tracking-wider">
                  Select a New Target Career Track:
                </div>
                <div className="flex flex-wrap gap-2">
                  {careerRoles.map((role) => (
                    <button
                      key={role}
                      onClick={() => handleRoleChange(role)}
                      disabled={isSwitching || roadmap?.target_role === role}
                      className={`px-3 py-1.5 rounded-xl text-xs font-bold transition-all cursor-pointer ${
                        roadmap?.target_role === role
                          ? 'bg-brand-600 text-white shadow-xs'
                          : 'bg-white border border-slate-200 text-slateText-secondary hover:border-brand-400 hover:text-brand-700 shadow-2xs'
                      }`}
                    >
                      {role}
                    </button>
                  ))}
                </div>
              </div>
            )}

            <h1 className="text-2xl sm:text-3xl font-extrabold text-navy-800 tracking-tight">
              Personalized Learning Roadmap
            </h1>
            <p className="text-sm text-slateText-secondary max-w-2xl leading-relaxed font-medium">
              A comprehensive {totalStages}-stage placement curriculum calibrated for {roadmap?.target_role}. All modules remain accessible without semester gatekeeping.
            </p>
          </div>

          {/* Progress Indicator */}
          <div className="shrink-0 bg-slate-50 border border-slate-200 rounded-2xl p-5 text-center sm:w-48 shadow-inner">
            <span className="text-xs uppercase font-extrabold text-slateText-muted tracking-wider">Roadmap Progress</span>
            <div className="text-3xl font-black text-brand-700 mt-1">{progressPercent}%</div>
            <div className="text-xs text-slateText-secondary mt-1 font-semibold">
              {completedCount} of {totalStages} Stages
            </div>
            <div className="w-full bg-slate-200 h-2.5 rounded-full mt-3 overflow-hidden">
              <div
                className="bg-brand-600 h-full rounded-full transition-all duration-500"
                style={{ width: `${progressPercent}%` }}
              />
            </div>
          </div>
        </div>
      </div>

      {/* Ordered Stages Timeline */}
      <div className="relative space-y-6">
        {roadmap?.stages?.map((stage: any, index: number) => {
          const isCompleted = stage.status === 'completed';
          const isInProgress = stage.status === 'in_progress';

          return (
            <div
              key={stage.stage_number}
              className={`rounded-2xl border p-6 sm:p-7 transition-all duration-200 hover:-translate-y-1 hover:shadow-card-hover ${
                isCompleted
                  ? 'border-emerald-200 bg-emerald-50/25 hover:border-emerald-300'
                  : isInProgress
                  ? 'border-brand-300 bg-white shadow-card ring-1 ring-brand-100 hover:border-brand-400'
                  : 'border-slate-200 bg-white hover:border-brand-300 shadow-subtle'
              }`}
            >
              <div className="flex flex-col sm:flex-row sm:items-start justify-between gap-5">
                <div className="flex items-start gap-4 sm:gap-5">
                  {/* Status Circle */}
                  <div
                    className={`flex h-11 w-11 shrink-0 items-center justify-center rounded-2xl font-extrabold text-sm shadow-xs ${
                      isCompleted
                        ? 'bg-emerald-600 text-white'
                        : isInProgress
                        ? 'bg-brand-600 text-white'
                        : 'bg-slate-100 text-slateText-secondary'
                    }`}
                  >
                    {isCompleted ? (
                      <CheckCircle2 className="h-6 w-6" />
                    ) : (
                      <span>{stage.stage_number}</span>
                    )}
                  </div>

                  <div>
                    <div className="flex items-center gap-2.5">
                      <h3 className="text-base font-bold text-navy-800">{stage.title}</h3>
                      <span
                        className={`text-[10px] uppercase font-bold px-2.5 py-0.5 rounded-full ${
                          isCompleted
                            ? 'bg-emerald-100 text-emerald-800'
                            : isInProgress
                            ? 'bg-brand-100 text-brand-800'
                            : 'bg-slate-100 text-slateText-secondary'
                        }`}
                      >
                        {isCompleted ? 'Completed' : isInProgress ? 'In Progress' : 'Available'}
                      </span>
                    </div>

                    <p className="mt-1.5 text-xs text-slateText-secondary leading-relaxed max-w-2xl font-medium">
                      {stage.description}
                    </p>

                    {/* Skills Covered Tags */}
                    <div className="mt-3.5 flex flex-wrap gap-1.5">
                      {stage.skills?.map((skill: string, sIdx: number) => (
                        <span
                          key={sIdx}
                          className="rounded-lg bg-slate-100 px-2.5 py-1 text-[11px] font-bold text-slateText-secondary"
                        >
                          {skill}
                        </span>
                      ))}
                    </div>
                  </div>
                </div>

                {/* Right Action / Link */}
                <div className="flex flex-row sm:flex-col items-center sm:items-end justify-between sm:justify-start gap-3 shrink-0 pt-2 sm:pt-0">
                  <div className="flex items-center gap-1.5 text-xs text-slateText-muted font-bold">
                    <Clock className="h-4 w-4" />
                    <span>~{stage.estimated_hours} hrs</span>
                  </div>

                  <Link
                    to={stage.recommended_practice}
                    className="inline-flex items-center gap-2 rounded-xl bg-brand-50 px-4 py-2.5 text-xs font-bold text-brand-700 hover:bg-brand-600 hover:text-white active:scale-95 transition-all duration-150 shadow-xs"
                  >
                    <span>Open Module</span>
                    <ArrowRight className="h-3.5 w-3.5" />
                  </Link>
                </div>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};

