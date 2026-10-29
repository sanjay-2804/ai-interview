  import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useAuth } from '../../context/AuthContext';
import { GraduationCap, Lock, Mail, AlertCircle, Shield, Eye, EyeOff, Loader2 } from 'lucide-react';

export const Login: React.FC = () => {
  const { login } = useAuth();
  const navigate = useNavigate();

  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [showPassword, setShowPassword] = useState(false);
  const [rememberMe, setRememberMe] = useState(true);
  const [errorMsg, setErrorMsg] = useState<string | null>(null);
  const [isSubmitting, setIsSubmitting] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!email.trim() || !password) {
      setErrorMsg('Please enter both your email address and password.');
      return;
    }
    setIsSubmitting(true);
    setErrorMsg(null);
    try {
      const loggedUser = await login(email.trim(), password, rememberMe);
      if (loggedUser.role === 'admin') {
        navigate('/admin');
      } else {
        navigate('/app/dashboard');
      }
    } catch (err: any) {
      setErrorMsg(err.message || 'Incorrect email or password. Please verify your credentials.');
    } finally {
      setIsSubmitting(false);
    }
  };

  const handleQuickFill = (role: 'student' | 'admin') => {
    if (role === 'student') {
      setEmail('student@interviewai.dev');
      setPassword('Student@123456');
    } else {
      setEmail('admin@interviewai.dev');
      setPassword('Admin@123456');
    }
    setErrorMsg(null);
  };

  return (
    <div className="min-h-[80vh] flex items-center justify-center px-4 py-12">
      <div className="w-full max-w-md space-y-6">
        {/* Brand Header */}
        <div className="text-center space-y-2">
          <Link to="/" className="inline-flex items-center gap-2">
            <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-brand-600 text-white shadow-sm">
              <GraduationCap className="h-6 w-6" />
            </div>
            <span className="text-2xl font-bold text-navy-800 tracking-tight">InterviewAI</span>
          </Link>
          <h2 className="text-xl font-bold text-navy-800">Sign In to Your Workspace</h2>
          <p className="text-xs text-slateText-secondary">
            Continue your placement preparation, mock tests, and skill roadmaps.
          </p>
        </div>

        {/* Demo Fast-Login Pill */}
        <div className="rounded-2xl border border-brand-200 bg-brand-50/70 p-4 text-xs space-y-2.5 shadow-xs">
          <div className="font-bold text-brand-900 flex items-center gap-2">
            <Shield className="h-4 w-4 text-brand-600" />
            <span>Development Quick-Login:</span>
          </div>
          <div className="flex gap-2.5">
            <button
              type="button"
              onClick={() => handleQuickFill('student')}
              className="flex-1 bg-white border border-brand-200 rounded-xl px-3 py-2 text-xs font-bold text-brand-700 hover:bg-brand-50 hover:border-brand-300 active:scale-95 transition-all cursor-pointer shadow-2xs"
            >
              Fill Demo Student
            </button>
            <button
              type="button"
              onClick={() => handleQuickFill('admin')}
              className="flex-1 bg-white border border-purple-200 rounded-xl px-3 py-2 text-xs font-bold text-purple-700 hover:bg-purple-50 hover:border-purple-300 active:scale-95 transition-all cursor-pointer shadow-2xs"
            >
              Fill Demo Admin
            </button>
          </div>
        </div>

        {/* Error Alert */}
        {errorMsg && (
          <div className="rounded-2xl border border-rose-200 bg-rose-50 p-4 text-xs font-medium text-rose-800 flex items-center gap-3">
            <AlertCircle className="h-4 w-4 shrink-0 text-rose-600" />
            <span>{errorMsg}</span>
          </div>
        )}

        {/* Login Card */}
        <div className="rounded-3xl border border-surface-border bg-white p-7 sm:p-9 shadow-card">
          <form onSubmit={handleSubmit} className="space-y-5">
            <div>
              <label className="block text-xs font-bold uppercase tracking-wider text-slateText-secondary mb-1.5">
                Email Address
              </label>
              <div className="relative">
                <Mail className="absolute left-3.5 top-3 h-4 w-4 text-slateText-muted" />
                <input
                  type="email"
                  value={email}
                  onChange={(e) => { setEmail(e.target.value); setErrorMsg(null); }}
                  required
                  placeholder="student@example.com"
                  className="w-full rounded-xl border border-slate-300 pl-10 pr-3.5 py-2.5 text-xs text-slateText-primary focus:border-brand-600 focus:outline-none focus:ring-2 focus:ring-brand-500/20 shadow-xs transition-colors"
                />
              </div>
            </div>

            <div>
              <div className="flex items-center justify-between mb-1.5">
                <label className="block text-xs font-bold uppercase tracking-wider text-slateText-secondary">
                  Password
                </label>
                <Link to="/forgot-password" className="text-[11px] font-bold text-brand-600 hover:underline">
                  Forgot password?
                </Link>
              </div>
              <div className="relative">
                <Lock className="absolute left-3.5 top-3 h-4 w-4 text-slateText-muted" />
                <input
                  type={showPassword ? 'text' : 'password'}
                  value={password}
                  onChange={(e) => { setPassword(e.target.value); setErrorMsg(null); }}
                  required
                  placeholder="••••••••"
                  className="w-full rounded-xl border border-slate-300 pl-10 pr-10 py-2.5 text-xs text-slateText-primary focus:border-brand-600 focus:outline-none focus:ring-2 focus:ring-brand-500/20 shadow-xs transition-colors"
                />
                <button
                  type="button"
                  onClick={() => setShowPassword(!showPassword)}
                  className="absolute right-3.5 top-3 text-slateText-muted hover:text-slateText-primary cursor-pointer"
                  tabIndex={-1}
                  aria-label={showPassword ? 'Hide password' : 'Show password'}
                >
                  {showPassword ? <EyeOff className="h-4 w-4" /> : <Eye className="h-4 w-4" />}
                </button>
              </div>
            </div>

            {/* Remember Me */}
            <div className="flex items-center gap-2 pt-1">
              <input
                id="remember_me"
                type="checkbox"
                checked={rememberMe}
                onChange={(e) => setRememberMe(e.target.checked)}
                className="h-4 w-4 rounded border-slate-300 text-brand-600 focus:ring-brand-500 cursor-pointer"
              />
              <label htmlFor="remember_me" className="text-xs text-slateText-secondary cursor-pointer select-none font-medium">
                Remember my session on this device
              </label>
            </div>

            <button
              type="submit"
              disabled={isSubmitting}
              className="w-full rounded-xl bg-brand-600 py-3 text-xs font-bold text-white shadow-sm hover:bg-brand-700 hover:shadow-md disabled:opacity-50 active:scale-[0.98] transition-all cursor-pointer flex items-center justify-center gap-2 mt-2"
            >
              {isSubmitting ? (
                <>
                  <Loader2 className="h-4 w-4 animate-spin" />
                  <span>Signing In...</span>
                </>
              ) : (
                'Sign In'
              )}
            </button>
          </form>

          <div className="mt-6 pt-4 border-t border-slate-100 text-center text-xs text-slateText-muted">
            Don't have an account yet?{' '}
            <Link to="/register" className="font-bold text-brand-600 hover:underline">
              Create student account
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
};
