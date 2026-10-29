import React from 'react';
import { Outlet, Navigate, Link, NavLink } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { Shield, LayoutDashboard, Users, HelpCircle, LogOut, ArrowLeft } from 'lucide-react';

export const AdminLayout: React.FC = () => {
  const { user, isAuthenticated, isLoading, logout } = useAuth();

  if (isLoading) {
    return (
      <div className="flex h-screen items-center justify-center bg-surface-ground">
        <div className="h-8 w-8 animate-spin rounded-full border-4 border-brand-600 border-t-transparent" />
      </div>
    );
  }

  if (!isAuthenticated || user?.role !== 'admin') {
    return <Navigate to="/app/dashboard" replace />;
  }

  return (
    <div className="flex h-screen bg-surface-ground text-slateText-primary overflow-hidden">
      {/* Admin Sidebar */}
      <aside className="w-64 bg-white border-r border-surface-border flex flex-col justify-between select-none">
        <div>
          <div className="p-5 border-b border-surface-border flex items-center justify-between bg-slate-50/50">
            <div className="flex items-center gap-2.5">
              <div className="flex h-8 w-8 items-center justify-center rounded-lg bg-brand-600 text-white shadow-xs">
                <Shield className="h-4 w-4" />
              </div>
              <span className="font-bold text-navy-800 text-base">Admin Portal</span>
            </div>
            <span className="bg-brand-50 border border-brand-200 text-brand-700 text-[10px] px-2 py-0.5 rounded-full font-bold">
              ADMIN
            </span>
          </div>

          <nav className="p-3 space-y-1">
            <NavLink
              to="/admin"
              end
              className={({ isActive }) =>
                `flex items-center gap-3 px-3 py-2.5 rounded-lg text-sm font-medium transition-all ${
                  isActive
                    ? 'bg-brand-50 text-brand-700 font-semibold border-l-4 border-brand-600'
                    : 'text-slateText-secondary hover:bg-slate-50 hover:text-slateText-primary'
                }`
              }
            >
              <LayoutDashboard className="h-4 w-4 shrink-0" />
              Analytics Dashboard
            </NavLink>
            <NavLink
              to="/admin/users"
              className={({ isActive }) =>
                `flex items-center gap-3 px-3 py-2.5 rounded-lg text-sm font-medium transition-all ${
                  isActive
                    ? 'bg-brand-50 text-brand-700 font-semibold border-l-4 border-brand-600'
                    : 'text-slateText-secondary hover:bg-slate-50 hover:text-slateText-primary'
                }`
              }
            >
              <Users className="h-4 w-4 shrink-0" />
              User Management
            </NavLink>
            <NavLink
              to="/admin/questions"
              className={({ isActive }) =>
                `flex items-center gap-3 px-3 py-2.5 rounded-lg text-sm font-medium transition-all ${
                  isActive
                    ? 'bg-brand-50 text-brand-700 font-semibold border-l-4 border-brand-600'
                    : 'text-slateText-secondary hover:bg-slate-50 hover:text-slateText-primary'
                }`
              }
            >
              <HelpCircle className="h-4 w-4 shrink-0" />
              Question Bank
            </NavLink>
          </nav>
        </div>

        <div className="p-4 border-t border-surface-border bg-slate-50/50 space-y-2">
          <Link
            to="/app/dashboard"
            className="flex items-center gap-2 text-xs font-semibold text-slateText-secondary hover:text-brand-600 transition-colors"
          >
            <ArrowLeft className="h-4 w-4" />
            Switch to Student Workspace
          </Link>
          <button
            onClick={logout}
            className="flex items-center gap-2 text-xs font-semibold text-rose-600 hover:text-rose-700 transition-colors w-full pt-1 cursor-pointer"
          >
            <LogOut className="h-4 w-4" />
            Sign Out
          </button>
        </div>
      </aside>

      {/* Main Admin Content */}
      <main className="flex-1 overflow-y-auto bg-surface-ground p-6 sm:p-8">
        <Outlet />
      </main>
    </div>
  );
};
