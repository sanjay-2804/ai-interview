import React, { useState, useMemo } from 'react';
import { Link, useNavigate, useSearchParams } from 'react-router-dom';
import { api } from '../../services/api';
import {
  GraduationCap, Lock, KeyRound, AlertCircle, Eye, EyeOff,
  CheckCircle2, XCircle, Loader2, ArrowRight
} from 'lucide-react';

export const ResetPassword: React.FC = () => {
  const [searchParams] = useSearchParams();
  const navigate = useNavigate();

  const tokenParam = searchParams.get('token') || '';
  const [token, setToken] = useState(tokenParam);
  const [newPassword, setNewPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [showPassword, setShowPassword] = useState(false);
  const [showConfirmPassword, setShowConfirmPassword] = useState(false);
  const [errorMsg, setErrorMsg] = useState<string | null>(null);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [isSuccess, setIsSuccess] = useState(false);

  // Dynamic Password Strength Calculations
  const passwordCriteria = useMemo(() => {
    return {
      minLength: newPassword.length >= 8,
      hasLetter: /[a-zA-Z]/.test(newPassword),
      hasNumber: /\d/.test(newPassword),
      hasSpecial: /[^a-zA-Z0-9]/.test(newPassword),
    };
  }, [newPassword]);

  const strengthScore = useMemo(() => {
    let score = 0;
    if (passwordCriteria.minLength) score += 1;
    if (passwordCriteria.hasLetter) score += 1;
    if (passwordCriteria.hasNumber) score += 1;
    if (passwordCriteria.hasSpecial) score += 1;
    return score;
  }, [passwordCriteria]);

  const strengthLabel = useMemo(() => {
    if (!newPassword) return { text: '', color: 'bg-slate-200' };
    if (strengthScore <= 1) return { text: 'Weak', color: 'bg-rose-500', textColor: 'text-rose-600' };
    if (strengthScore <= 3) return { text: 'Medium', color: 'bg-amber-500', textColor: 'text-amber-600' };
    return { text: 'Strong', color: 'bg-emerald-500', textColor: 'text-emerald-600' };
  }, [newPassword, strengthScore]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!token.trim()) {
      setErrorMsg('A valid password reset token is required.');
      return;
    }
    if (newPassword.length < 8) {
      setErrorMsg('New password must be at least 8 characters long.');
      return;
    }
    if (newPassword !== confirmPassword) {
      setErrorMsg('Passwords do not match. Please ensure both fields are identical.');
      return;
    }

    setIsSubmitting(true);
    setErrorMsg(null);
    try {
      await api.resetPassword({
        token: token.trim(),
        new_password: newPassword,
      });
      setIsSuccess(true);
    } catch (err: any) {
      setErrorMsg(err.message || 'Failed to reset password. The reset token may be expired or already used.');
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <div className="min-h-[85vh] flex items-center justify-center px-4 py-12">
      <div className="w-full max-w-md space-y-6">
        {/* Brand Header */}
        <div className="text-center space-y-2">
          <Link to="/" className="inline-flex items-center gap-2">
            <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-brand-600 text-white shadow-sm">
              <GraduationCap className="h-6 w-6" />
            </div>
            <span className="text-2xl font-bold text-navy-800 tracking-tight">InterviewAI</span>
          </Link>
          <h2 className="text-xl font-bold text-navy-800">Set New Account Password</h2>
          <p className="text-xs text-slateText-secondary">
            Enter your secure single-use token and choose a new password.
          </p>
        </div>

        {/* Error Notification */}
        {errorMsg && (
          <div className="rounded-xl border border-rose-200 bg-rose-50 p-3.5 text-xs font-medium text-rose-800 flex items-center gap-2.5">
            <AlertCircle className="h-4 w-4 shrink-0 text-rose-600" />
            <span>{errorMsg}</span>
          </div>
        )}

        <div className="rounded-3xl border border-surface-border bg-white p-7 sm:p-9 shadow-card">
          {isSuccess ? (
            <div className="text-center space-y-5 py-3">
              <div className="flex h-14 w-14 mx-auto items-center justify-center rounded-2xl bg-emerald-100 text-emerald-600 shadow-xs">
                <CheckCircle2 className="h-7 w-7" />
              </div>
              <h3 className="text-base font-extrabold text-navy-800">Password Reset Successful!</h3>
              <p className="text-xs text-slateText-secondary leading-relaxed font-medium">
                Your password has been securely updated. Any previously active sessions have been invalidated.
              </p>
              <div className="pt-2">
                <button
                  type="button"
                  onClick={() => navigate('/login')}
                  className="w-full rounded-xl bg-brand-600 py-3 text-xs font-bold text-white shadow-sm hover:bg-brand-700 hover:shadow-md active:scale-[0.98] transition-all cursor-pointer flex items-center justify-center gap-2"
                >
                  <span>Sign In with New Password</span>
                  <ArrowRight className="h-4 w-4" />
                </button>
              </div>
            </div>
          ) : (
            <form onSubmit={handleSubmit} className="space-y-4">
              <div>
                <label className="block text-xs font-bold uppercase tracking-wider text-slateText-secondary mb-1.5">
                  Reset Token
                </label>
                <div className="relative">
                  <KeyRound className="absolute left-3.5 top-3 h-4 w-4 text-slateText-muted" />
                  <input
                    type="text"
                    value={token}
                    onChange={(e) => { setToken(e.target.value); setErrorMsg(null); }}
                    required
                    placeholder="Paste your reset token here"
                    className="w-full rounded-xl border border-slate-300 pl-10 pr-3.5 py-2.5 text-xs font-mono text-slateText-primary focus:border-brand-600 focus:outline-none focus:ring-2 focus:ring-brand-500/20 shadow-xs transition-colors"
                  />
                </div>
              </div>

              <div>
                <label className="block text-xs font-bold uppercase tracking-wider text-slateText-secondary mb-1.5">
                  New Password
                </label>
                <div className="relative">
                  <Lock className="absolute left-3.5 top-3 h-4 w-4 text-slateText-muted" />
                  <input
                    type={showPassword ? 'text' : 'password'}
                    value={newPassword}
                    onChange={(e) => { setNewPassword(e.target.value); setErrorMsg(null); }}
                    required
                    placeholder="At least 8 characters"
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

                {/* Password Strength Indicator */}
                {newPassword.length > 0 && (
                  <div className="mt-2 space-y-1.5">
                    <div className="flex items-center justify-between text-[11px]">
                      <span className="text-slateText-muted">Password Strength:</span>
                      <span className={`font-bold ${strengthLabel.textColor}`}>{strengthLabel.text}</span>
                    </div>
                    <div className="grid grid-cols-4 gap-1 h-1.5">
                      <div className={`rounded-full ${strengthScore >= 1 ? strengthLabel.color : 'bg-slate-200'}`} />
                      <div className={`rounded-full ${strengthScore >= 2 ? strengthLabel.color : 'bg-slate-200'}`} />
                      <div className={`rounded-full ${strengthScore >= 3 ? strengthLabel.color : 'bg-slate-200'}`} />
                      <div className={`rounded-full ${strengthScore >= 4 ? strengthLabel.color : 'bg-slate-200'}`} />
                    </div>
                    <div className="grid grid-cols-2 gap-1 pt-1 text-[10px] text-slateText-secondary">
                      <div className="flex items-center gap-1">
                        {passwordCriteria.minLength ? (
                          <CheckCircle2 className="h-3 w-3 text-emerald-600" />
                        ) : (
                          <XCircle className="h-3 w-3 text-slate-300" />
                        )}
                        <span>8+ characters</span>
                      </div>
                      <div className="flex items-center gap-1">
                        {passwordCriteria.hasLetter ? (
                          <CheckCircle2 className="h-3 w-3 text-emerald-600" />
                        ) : (
                          <XCircle className="h-3 w-3 text-slate-300" />
                        )}
                        <span>Letters (a-z)</span>
                      </div>
                      <div className="flex items-center gap-1">
                        {passwordCriteria.hasNumber ? (
                          <CheckCircle2 className="h-3 w-3 text-emerald-600" />
                        ) : (
                          <XCircle className="h-3 w-3 text-slate-300" />
                        )}
                        <span>Numbers (0-9)</span>
                      </div>
                      <div className="flex items-center gap-1">
                        {passwordCriteria.hasSpecial ? (
                          <CheckCircle2 className="h-3 w-3 text-emerald-600" />
                        ) : (
                          <XCircle className="h-3 w-3 text-slate-300" />
                        )}
                        <span>Special symbol (!@#)</span>
                      </div>
                    </div>
                  </div>
                )}
              </div>

              <div>
                <label className="block text-xs font-bold uppercase tracking-wider text-slateText-secondary mb-1.5">
                  Confirm New Password
                </label>
                <div className="relative">
                  <Lock className="absolute left-3.5 top-3 h-4 w-4 text-slateText-muted" />
                  <input
                    type={showConfirmPassword ? 'text' : 'password'}
                    value={confirmPassword}
                    onChange={(e) => { setConfirmPassword(e.target.value); setErrorMsg(null); }}
                    required
                    placeholder="Re-enter new password"
                    className="w-full rounded-xl border border-slate-300 pl-10 pr-10 py-2.5 text-xs text-slateText-primary focus:border-brand-600 focus:outline-none focus:ring-2 focus:ring-brand-500/20 shadow-xs transition-colors"
                  />
                  <button
                    type="button"
                    onClick={() => setShowConfirmPassword(!showConfirmPassword)}
                    className="absolute right-3.5 top-3 text-slateText-muted hover:text-slateText-primary cursor-pointer"
                    tabIndex={-1}
                    aria-label={showConfirmPassword ? 'Hide password' : 'Show password'}
                  >
                    {showConfirmPassword ? <EyeOff className="h-4 w-4" /> : <Eye className="h-4 w-4" />}
                  </button>
                </div>
                {confirmPassword && newPassword !== confirmPassword && (
                  <p className="mt-1 text-[11px] text-rose-600 font-medium">Passwords do not match.</p>
                )}
              </div>

              <button
                type="submit"
                disabled={isSubmitting}
                className="w-full rounded-xl bg-brand-600 py-3 text-xs font-bold text-white shadow-sm hover:bg-brand-700 hover:shadow-md disabled:opacity-50 active:scale-[0.98] transition-all cursor-pointer flex items-center justify-center gap-2 mt-2"
              >
                {isSubmitting ? (
                  <>
                    <Loader2 className="h-4 w-4 animate-spin" />
                    <span>Updating Password...</span>
                  </>
                ) : (
                  'Update Password'
                )}
              </button>

              <div className="text-center pt-2">
                <Link to="/login" className="text-xs font-bold text-slateText-secondary hover:text-brand-600 transition-colors">
                  Return to Sign In
                </Link>
              </div>
            </form>
          )}
        </div>
      </div>
    </div>
  );
};

