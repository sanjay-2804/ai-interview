import React from 'react';
import { NavLink } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import {
  GraduationCap, LayoutDashboard, Map, BookOpen, Brain, Code2, Mic,
  MessageSquare, FileText, BarChart3, BookmarkCheck, Settings,
  LogOut, Shield, ChevronRight
} from 'lucide-react';

interface SidebarProps {
  onCloseMobile?: () => void;
}

export const Sidebar: React.FC<SidebarProps> = ({ onCloseMobile }) => {
  const { user, logout } = useAuth();

  const navItems = [
    { name: 'Dashboard', path: '/app/dashboard', icon: LayoutDashboard },
    { name: 'Personal Roadmap', path: '/app/roadmap', icon: Map },
    { name: 'Technical Centre', path: '/app/technical', icon: BookOpen },
    { name: 'Aptitude & Reasoning', path: '/app/aptitude', icon: Brain },
    { name: 'Coding Practice', path: '/app/coding', icon: Code2 },
    { name: 'Mock Interview Lab', path: '/app/interview', icon: Mic },
    { name: 'Communication Lab', path: '/app/communication', icon: MessageSquare },
    { name: 'Projects & Resume', path: '/app/resume', icon: FileText },
    { name: 'Progress & Scores', path: '/app/progress', icon: BarChart3 },
    { name: 'Learning Library', path: '/app/library', icon: BookmarkCheck },
    { name: 'Profile & Settings', path: '/app/profile', icon: Settings },
  ];

  return (
    <aside className="flex flex-col h-full bg-white border-r border-surface-border w-64 select-none shadow-xs">
      {/* Brand Header */}
      <div className="flex items-center gap-2.5 px-5 py-4 border-b border-surface-border bg-white">
        <div className="flex h-9 w-9 items-center justify-center rounded-xl bg-brand-600 text-white shadow-xs">
          <GraduationCap className="h-5 w-5" />
        </div>
        <div>
          <span className="text-base font-bold text-navy-800 tracking-tight block leading-tight">
            InterviewAI
          </span>
          <span className="text-[10px] font-semibold text-brand-600 uppercase tracking-wider block">
            Placement Prep
          </span>
        </div>
      </div>

      {/* Student Profile Quick Card */}
      <div className="p-4 border-b border-surface-border bg-slate-50/60">
        <div className="flex items-center gap-3">
          <div className="flex h-10 w-10 shrink-0 items-center justify-center rounded-full bg-brand-100 text-brand-700 font-bold text-sm ring-2 ring-brand-200/60">
            {user?.full_name?.charAt(0) || 'S'}
          </div>
          <div className="overflow-hidden">
            <h3 className="text-xs font-bold text-navy-800 truncate">
              {user?.full_name || 'Student'}
            </h3>
            <p className="text-[11px] text-slateText-secondary truncate">
              {user?.profile?.target_role || 'Software Engineer'}
            </p>
          </div>
        </div>

        {/* Level badge */}
        <div className="mt-3 flex items-center justify-between text-[11px] bg-white px-3 py-1.5 rounded-lg border border-slate-200 shadow-2xs">
          <span className="text-slateText-secondary font-medium">Skill Level:</span>
          <span className="font-bold text-brand-700">
            {user?.profile?.skill_level || 'Beginner'}
          </span>
        </div>
      </div>

      {/* Navigation Links */}
      <nav className="flex-1 overflow-y-auto px-3.5 py-4 space-y-1.5">
        {navItems.map((item) => {
          const Icon = item.icon;
          return (
            <NavLink
              key={item.path}
              to={item.path}
              onClick={onCloseMobile}
              className={({ isActive }) =>
                `group flex items-center justify-between px-3.5 py-2.5 rounded-xl text-xs font-semibold transition-all duration-200 cursor-pointer ${
                  isActive
                    ? 'bg-brand-50 text-brand-700 border-l-4 border-brand-600 shadow-2xs'
                    : 'text-slateText-secondary hover:bg-slate-50/80 hover:text-navy-800 hover:translate-x-1'
                }`
              }
            >
              <div className="flex items-center gap-3">
                <Icon className="h-4 w-4 shrink-0 transition-transform group-hover:scale-110" />
                <span>{item.name}</span>
              </div>
              <ChevronRight className="h-3 w-3 opacity-0 -translate-x-1 transition-all duration-200 group-hover:opacity-60 group-hover:translate-x-0" />
            </NavLink>
          );
        })}

        {user?.role === 'admin' && (
          <div className="pt-4 mt-4 border-t border-slate-100">
            <span className="px-3 text-[10px] font-bold uppercase tracking-wider text-slateText-muted">
              Administration
            </span>
            <NavLink
              to="/admin"
              onClick={onCloseMobile}
              className="mt-1.5 flex items-center gap-3 px-3.5 py-2.5 rounded-xl text-xs font-bold text-purple-700 bg-purple-50/80 hover:bg-purple-100 border border-purple-200/60 transition-all duration-200 hover:translate-x-1 cursor-pointer"
            >
              <Shield className="h-4 w-4 text-purple-600 shrink-0" />
              <span>Admin Portal</span>
            </NavLink>
          </div>
        )}
      </nav>

      {/* Logout Footer */}
      <div className="p-3 border-t border-surface-border bg-slate-50/40">
        <button
          onClick={logout}
          className="flex w-full items-center gap-2.5 px-3.5 py-2.5 rounded-xl text-xs font-semibold text-rose-600 hover:bg-rose-50 hover:text-rose-700 active:scale-[0.98] transition-all duration-150 cursor-pointer"
        >
          <LogOut className="h-4 w-4" />
          <span>Sign Out</span>
        </button>
      </div>
    </aside>
  );
};
