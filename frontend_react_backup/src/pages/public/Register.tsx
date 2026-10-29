import React, { useState, useMemo } from 'react';
import { Link, useNavigate, useSearchParams } from 'react-router-dom';
import { useAuth } from '../../context/AuthContext';
import { api } from '../../services/api';
import {
  GraduationCap, Lock, Mail, User, AlertCircle, Eye, EyeOff,
  CheckCircle2, XCircle, Loader2, Compass
} from 'lucide-react';

export const Register: React.FC = () => {
  const { register } = useAuth();
  const navigate = useNavigate();
  const [searchParams] = useSearchParams();

  const initialRole = searchParams.get('role') || 'Software Developer';
  const [targetRole, setTargetRole] = useState(initialRole);
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [showPassword, setShowPassword] = useState(false);
  const [showConfirmPassword, setShowConfirmPassword] = useState(false);
  const [agreeTerms, setAgreeTerms] = useState(false);
  const [errorMsg, setErrorMsg] = useState<string | null>(null);
  const [isSubmitting, setIsSubmitting] = useState(false);

  // Dynamic Password Strength Calculations
  const passwordCriteria = useMemo(() => {
    return {
      minLength: password.length >= 8,
      hasLetter: /[a-zA-Z]/.test(password),
      hasNumber: /\d/.test(password),
      hasSpecial: /[^a-zA-Z0-9]/.test(password),
    };
  }, [password]);

  const strengthScore = useMemo(() => {
    let score = 0;
    if (passwordCriteria.minLength) score += 1;
    if (passwordCriteria.hasLetter) score += 1;
    if (passwordCriteria.hasNumber) score += 1;
    if (passwordCriteria.hasSpecial) score += 1;
    return score;
  }, [passwordCriteria]);

  const strengthLabel = useMemo(() => {
    if (!password) return { text: '', color: 'bg-slate-200' };
    if (strengthScore <= 1) return { text: 'Weak', color: 'bg-rose-500', textColor: 'text-rose-600' };
    if (strengthScore <= 3) return { text: 'Medium', color: 'bg-amber-500', textColor: 'text-amber-600' };
    return { text: 'Strong', color: 'bg-emerald-500', textColor: 'text-emerald-600' };
  }, [password, strengthScore]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (password.length < 8) {
      setErrorMsg('Password must be at least 8 characters long.');
      return;
    }
    if (password !== confirmPassword) {
      setErrorMsg('Passwords do not match. Please re-enter both passwords.');
      return;
    }
    if (!agreeTerms) {
      setErrorMsg('You must agree to the Terms of Service and Privacy Policy to create an account.');
      return;
    }

    setIsSubmitting(true);
    setErrorMsg(null);
    try {
      await register(name.trim(), email.trim().toLowerCase(), password, targetRole);
      // Ensure user's career path is synced in database
      try {
        await api.updateOnboarding({ target_role: targetRole });
      } catch (e) {
        console.warn('Initial role sync:', e);
      }
      navigate('/app/dashboard');
    } catch (err: any) {
      setErrorMsg(err.message || 'Registration failed. An account with this email may already exist.');
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
          <h2 className="text-xl font-bold text-navy-800">Create Your Student Account</h2>
          <p className="text-xs text-slateText-secondary">
            Personalize your placement roadmap, diagnostic practice, and career goals.
          </p>
        </div>

        {/* Error Notification */}
        {errorMsg && (
          <div className="rounded-xl border border-rose-200 bg-rose-50 p-3.5 text-xs font-medium text-rose-800 flex items-center gap-2.5">
            <AlertCircle className="h-4 w-4 shrink-0 text-rose-600" />
            <span>{errorMsg}</span>
          </div>
        )}

        {/* Registration Card */}
        <div className="rounded-3xl border border-surface-border bg-white p-7 sm:p-9 shadow-card">
          <form onSubmit={handleSubmit} className="space-y-4">
            <div>
              <label className="block text-xs font-bold uppercase tracking-wider text-slateText-secondary mb-1.5">
                Full Name
              </label>
              <div className="relative">
                <User className="absolute left-3.5 top-3 h-4 w-4 text-slateText-muted" />
                <input
                  type="text"
                  value={name}
                  onChange={(e) => { setName(e.target.value); setErrorMsg(null); }}
                  required
                  placeholder="e.g. Priya Sharma"
                  className="w-full rounded-xl border border-slate-300 pl-10 pr-3.5 py-2.5 text-xs text-slateText-primary focus:border-brand-600 focus:outline-none focus:ring-2 focus:ring-brand-500/20 shadow-xs transition-colors"
                />
              </div>
            </div>

            <div>
              <label className="block text-xs font-bold uppercase tracking-wider text-slateText-secondary mb-1.5">
                College or Personal Email
              </label>
              <div className="relative">
                <Mail className="absolute left-3.5 top-3 h-4 w-4 text-slateText-muted" />
                <input
                  type="email"
                  value={email}
                  onChange={(e) => { setEmail(e.target.value); setErrorMsg(null); }}
                  required
                  placeholder="priya@college.edu"
                  className="w-full rounded-xl border border-slate-300 pl-10 pr-3.5 py-2.5 text-xs text-slateText-primary focus:border-brand-600 focus:outline-none focus:ring-2 focus:ring-brand-500/20 shadow-xs transition-colors"
                />
              </div>
            </div>

            <div>
              <label className="block text-xs font-bold uppercase tracking-wider text-slateText-secondary mb-1.5 flex items-center gap-1.5">
                <Compass className="h-3.5 w-3.5 text-brand-600" />
                Target Career Path
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
              <label className="block text-xs font-bold uppercase tracking-wider text-slateText-secondary mb-1.5">
                Password
              </label>
              <div className="relative">
                <Lock className="absolute left-3.5 top-3 h-4 w-4 text-slateText-muted" />
                <input
                  type={showPassword ? 'text' : 'password'}
                  value={password}
                  onChange={(e) => { setPassword(e.target.value); setErrorMsg(null); }}
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
              {password.length > 0 && (
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
                Confirm Password
              </label>
              <div className="relative">
                <Lock className="absolute left-3.5 top-3 h-4 w-4 text-slateText-muted" />
                <input
                  type={showConfirmPassword ? 'text' : 'password'}
                  value={confirmPassword}
                  onChange={(e) => { setConfirmPassword(e.target.value); setErrorMsg(null); }}
                  required
                  placeholder="Re-enter password"
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
              {confirmPassword && password !== confirmPassword && (
                <p className="mt-1 text-[11px] text-rose-600 font-medium">Passwords do not match.</p>
              )}
            </div>

            {/* Terms and Privacy Checkbox */}
            <div className="flex items-start gap-2.5 pt-2">
              <input
                id="agree_terms"
                type="checkbox"
                checked={agreeTerms}
                onChange={(e) => { setAgreeTerms(e.target.checked); setErrorMsg(null); }}
                className="mt-0.5 h-4 w-4 rounded border-slate-300 text-brand-600 focus:ring-brand-500 cursor-pointer"
              />
              <label htmlFor="agree_terms" className="text-xs text-slateText-secondary leading-tight cursor-pointer select-none font-medium">
                I agree to the{' '}
                <Link to="/terms" target="_blank" className="font-bold text-brand-600 hover:underline">
                  Terms of Service
                </Link>{' '}
                and{' '}
                <Link to="/privacy" target="_blank" className="font-bold text-brand-600 hover:underline">
                  Privacy Policy
                </Link>
                .
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
                  <span>Creating Account...</span>
                </>
              ) : (
                'Create Student Account'
              )}
            </button>
          </form>

          <div className="mt-6 pt-4 border-t border-slate-100 text-center text-xs text-slateText-muted">
            Already have an account?{' '}
            <Link to="/login" className="font-bold text-brand-600 hover:underline">
              Sign in here
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
};
