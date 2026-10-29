import React, { useState } from 'react';
import { Outlet, Navigate, Link } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { Sidebar } from '../components/Sidebar';
import { Navbar } from '../components/Navbar';
import { Menu, X, Bell, BookOpen, AlertCircle } from 'lucide-react';
import { OnboardingModal } from '../pages/app/OnboardingModal';

export const AppLayout: React.FC = () => {
  const { user, isAuthenticated, isLoading } = useAuth();
  const [mobileSidebarOpen, setMobileSidebarOpen] = useState(false);
  const [showOnboarding, setShowOnboarding] = useState(false);

  if (isLoading) {
    return (
      <div className="flex h-screen w-full items-center justify-center bg-surface-ground">
        <div className="flex flex-col items-center gap-3">
          <div className="h-9 w-9 animate-spin rounded-full border-4 border-brand-600 border-t-transparent" />
          <p className="text-sm font-medium text-slateText-secondary">Loading your learning workspace...</p>
        </div>
      </div>
    );
  }

  if (!isAuthenticated) {
    return <Navigate to="/login" replace />;
  }

  const needsOnboarding = user?.profile && !user.profile.onboarding_completed;

  return (
    <div className="flex h-screen bg-surface-ground overflow-hidden">
      {/* Desktop Sidebar */}
      <div className="hidden md:flex shrink-0">
        <Sidebar />
      </div>

      {/* Mobile Drawer */}
      {mobileSidebarOpen && (
        <div className="fixed inset-0 z-50 flex md:hidden">
          <div
            className="fixed inset-0 bg-slate-900/50 backdrop-blur-sm"
            onClick={() => setMobileSidebarOpen(false)}
          />
          <div className="relative z-10 w-64 bg-white shadow-xl">
            <Sidebar onCloseMobile={() => setMobileSidebarOpen(false)} />
          </div>
        </div>
      )}

      {/* Main Content Workspace */}
      <div className="flex flex-1 flex-col overflow-hidden">
        {/* Top App Header */}
        <header className="flex h-16 shrink-0 items-center justify-between border-b border-surface-border bg-white px-6 sm:px-8 shadow-2xs">
          <div className="flex items-center gap-3">
            <button
              onClick={() => setMobileSidebarOpen(true)}
              className="p-2 rounded-lg text-slateText-secondary hover:bg-slate-100 md:hidden transition-colors cursor-pointer"
            >
              <Menu className="h-5 w-5" />
            </button>
            <h1 className="text-base sm:text-lg font-bold text-navy-800 tracking-tight">
              InterviewAI Workspace
            </h1>
          </div>

          <div className="flex items-center gap-4">
            {needsOnboarding && (
              <button
                onClick={() => setShowOnboarding(true)}
                className="hidden sm:inline-flex items-center gap-1.5 rounded-full bg-amber-50 px-3.5 py-1 text-xs font-semibold text-amber-800 border border-amber-200 hover:bg-amber-100 hover:shadow-xs active:scale-[0.98] transition-all cursor-pointer"
              >
                <AlertCircle className="h-3.5 w-3.5" />
                Finish Onboarding Profile
              </button>
            )}
            <div className="flex items-center gap-2.5">
              <span className="text-xs font-semibold text-slateText-secondary hidden sm:inline">
                {user?.full_name}
              </span>
              <div className="flex h-9 w-9 items-center justify-center rounded-full bg-brand-600 text-white text-xs font-bold ring-2 ring-brand-100 hover:ring-brand-200 transition-all cursor-pointer shadow-xs">
                {user?.full_name?.charAt(0) || 'U'}
              </div>
            </div>
          </div>
        </header>

        {/* Scrollable Page Body */}
        <main className="flex-1 overflow-y-auto p-6 sm:p-8 lg:p-10 pb-24">
          <Outlet />
        </main>
      </div>

      {/* Onboarding Dialog */}
      {(needsOnboarding || showOnboarding) && (
        <OnboardingModal isOpen={true} onClose={() => setShowOnboarding(false)} />
      )}
    </div>
  );
};

