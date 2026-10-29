import React, { useState } from 'react';
import { Link, useNavigate, useLocation } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { GraduationCap, Menu, X, ArrowRight, LayoutDashboard, User, LogOut, Shield } from 'lucide-react';

export const Navbar: React.FC = () => {
  const { user, isAuthenticated, logout } = useAuth();
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const navigate = useNavigate();
  const location = useLocation();

  const isPublicPage = !location.pathname.startsWith('/app') && !location.pathname.startsWith('/admin');

  return (
    <header className="sticky top-0 z-40 w-full border-b border-surface-border bg-white/95 backdrop-blur-md">
      <div className="mx-auto flex h-16 max-w-7xl items-center justify-between px-4 sm:px-6 lg:px-8">
        {/* Brand Logo */}
        <Link to="/" className="flex items-center gap-2.5 group">
          <div className="flex h-9 w-9 items-center justify-center rounded-lg bg-brand-600 text-white shadow-sm transition-transform group-hover:scale-105">
            <GraduationCap className="h-5 w-5" />
          </div>
          <div className="flex flex-col">
            <span className="text-lg font-bold tracking-tight text-navy-800">InterviewAI</span>
            <span className="text-[10px] font-medium uppercase tracking-wider text-slateText-secondary -mt-1">
              Placement Prep
            </span>
          </div>
        </Link>

        {/* Public Desktop Navigation */}
        {isPublicPage && (
          <nav className="hidden md:flex items-center gap-2">
            <Link to="/" className="px-3.5 py-2 rounded-xl text-xs font-semibold text-slateText-secondary hover:text-brand-600 hover:bg-brand-50/60 transition-all">
              Home
            </Link>
            <Link to="/features" className="px-3.5 py-2 rounded-xl text-xs font-semibold text-slateText-secondary hover:text-brand-600 hover:bg-brand-50/60 transition-all">
              Features
            </Link>
            <Link to="/learning-paths" className="px-3.5 py-2 rounded-xl text-xs font-semibold text-slateText-secondary hover:text-brand-600 hover:bg-brand-50/60 transition-all">
              Learning Paths
            </Link>
            <Link to="/placement-prep" className="px-3.5 py-2 rounded-xl text-xs font-semibold text-slateText-secondary hover:text-brand-600 hover:bg-brand-50/60 transition-all">
              Placement Prep
            </Link>
            <Link to="/about" className="px-3.5 py-2 rounded-xl text-xs font-semibold text-slateText-secondary hover:text-brand-600 hover:bg-brand-50/60 transition-all">
              About
            </Link>
          </nav>
        )}

        {/* Action Buttons */}
        <div className="hidden md:flex items-center gap-3">
          {isAuthenticated ? (
            <div className="flex items-center gap-3">
              {user?.role === 'admin' ? (
                <Link
                  to="/admin"
                  className="inline-flex items-center gap-1.5 rounded-xl border border-brand-200 bg-brand-50 px-4 py-2 text-xs font-bold text-brand-700 hover:bg-brand-100 hover:shadow-2xs active:scale-[0.98] transition-all cursor-pointer"
                >
                  <Shield className="h-4 w-4 text-brand-600" />
                  Admin Portal
                </Link>
              ) : null}
              <Link
                to="/app/dashboard"
                className="inline-flex items-center gap-2 rounded-xl bg-brand-600 px-5 py-2.5 text-xs font-bold text-white shadow-sm hover:bg-brand-700 hover:shadow-md active:scale-[0.98] transition-all cursor-pointer"
              >
                <LayoutDashboard className="h-4 w-4" />
                Student Dashboard
              </Link>
              <button
                onClick={logout}
                title="Sign out"
                className="flex h-10 w-10 items-center justify-center rounded-xl border border-slate-200 text-slateText-secondary hover:bg-rose-50 hover:text-rose-600 hover:border-rose-200 active:scale-95 transition-all cursor-pointer"
              >
                <LogOut className="h-4 w-4" />
              </button>
            </div>
          ) : (
            <div className="flex items-center gap-2">
              <Link
                to="/login"
                className="rounded-xl px-4 py-2.5 text-xs font-bold text-slateText-primary hover:text-brand-600 hover:bg-slate-50 transition-colors"
              >
                Sign In
              </Link>
              <Link
                to="/register"
                className="inline-flex items-center gap-1.5 rounded-xl bg-brand-600 px-5 py-2.5 text-xs font-bold text-white shadow-sm hover:bg-brand-700 hover:shadow-md active:scale-[0.98] transition-all cursor-pointer"
              >
                Get Started Free
                <ArrowRight className="h-4 w-4" />
              </Link>
            </div>
          )}
        </div>

        {/* Mobile Hamburger Button */}
        <div className="flex md:hidden">
          <button
            onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
            className="p-2 rounded-lg text-slateText-secondary hover:bg-slate-100"
          >
            {mobileMenuOpen ? <X className="h-6 w-6" /> : <Menu className="h-6 w-6" />}
          </button>
        </div>
      </div>

      {/* Mobile Menu Dropdown */}
      {mobileMenuOpen && (
        <div className="md:hidden border-b border-surface-border bg-white px-4 pt-2 pb-6 space-y-3">
          {isPublicPage && (
            <div className="space-y-1">
              <Link
                to="/"
                onClick={() => setMobileMenuOpen(false)}
                className="block px-3 py-2 text-base font-medium text-slateText-primary hover:bg-slate-50 rounded-md"
              >
                Home
              </Link>
              <Link
                to="/features"
                onClick={() => setMobileMenuOpen(false)}
                className="block px-3 py-2 text-base font-medium text-slateText-primary hover:bg-slate-50 rounded-md"
              >
                Features
              </Link>
              <Link
                to="/learning-paths"
                onClick={() => setMobileMenuOpen(false)}
                className="block px-3 py-2 text-base font-medium text-slateText-primary hover:bg-slate-50 rounded-md"
              >
                Learning Paths
              </Link>
              <Link
                to="/placement-prep"
                onClick={() => setMobileMenuOpen(false)}
                className="block px-3 py-2 text-base font-medium text-slateText-primary hover:bg-slate-50 rounded-md"
              >
                Placement Prep
              </Link>
              <Link
                to="/about"
                onClick={() => setMobileMenuOpen(false)}
                className="block px-3 py-2 text-base font-medium text-slateText-primary hover:bg-slate-50 rounded-md"
              >
                About
              </Link>
            </div>
          )}

          <div className="pt-2 border-t border-slate-100 space-y-2">
            {isAuthenticated ? (
              <>
                <Link
                  to="/app/dashboard"
                  onClick={() => setMobileMenuOpen(false)}
                  className="block w-full text-center rounded-lg bg-brand-600 px-4 py-2.5 text-sm font-semibold text-white"
                >
                  Go to Dashboard
                </Link>
                {user?.role === 'admin' && (
                  <Link
                    to="/admin"
                    onClick={() => setMobileMenuOpen(false)}
                    className="block w-full text-center rounded-lg border border-brand-300 bg-brand-50 px-4 py-2.5 text-sm font-semibold text-brand-700"
                  >
                    Admin Portal
                  </Link>
                )}
                <button
                  onClick={() => {
                    setMobileMenuOpen(false);
                    logout();
                  }}
                  className="block w-full text-center rounded-lg border border-slate-200 px-4 py-2 text-sm font-medium text-slateText-secondary hover:bg-slate-50"
                >
                  Sign Out
                </button>
              </>
            ) : (
              <div className="grid grid-cols-2 gap-2">
                <Link
                  to="/login"
                  onClick={() => setMobileMenuOpen(false)}
                  className="block text-center rounded-lg border border-slate-200 px-4 py-2 text-sm font-medium text-slateText-primary"
                >
                  Sign In
                </Link>
                <Link
                  to="/register"
                  onClick={() => setMobileMenuOpen(false)}
                  className="block text-center rounded-lg bg-brand-600 px-4 py-2 text-sm font-semibold text-white"
                >
                  Register
                </Link>
              </div>
            )}
          </div>
        </div>
      )}
    </header>
  );
};

