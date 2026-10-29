import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { api } from '../../services/api';
import { GraduationCap, ArrowLeft, Mail, CheckCircle2, AlertCircle, KeyRound, Loader2, ExternalLink } from 'lucide-react';

export const ForgotPassword: React.FC = () => {
  const [email, setEmail] = useState('');
  const [submitted, setSubmitted] = useState(false);
  const [devToken, setDevToken] = useState<string | null>(null);
  const [errorMsg, setErrorMsg] = useState<string | null>(null);
  const [isSubmitting, setIsSubmitting] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!email.trim()) return;

    setIsSubmitting(true);
    setErrorMsg(null);
    try {
      const response = await api.forgotPassword(email.trim().toLowerCase());
      setSubmitted(true);
      if (response.reset_token) {
        setDevToken(response.reset_token);
      }
    } catch (err: any) {
      setErrorMsg(err.message || 'Unable to generate password reset request.');
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <div className="min-h-[75vh] flex items-center justify-center px-4 py-12">
      <div className="w-full max-w-md space-y-6">
        <div className="text-center space-y-2">
          <Link to="/" className="inline-flex items-center gap-2">
            <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-brand-600 text-white shadow-sm">
              <GraduationCap className="h-6 w-6" />
            </div>
            <span className="text-2xl font-bold text-navy-800 tracking-tight">InterviewAI</span>
          </Link>
          <h2 className="text-xl font-bold text-navy-800">Reset Your Password</h2>
          <p className="text-xs text-slateText-secondary">
            Enter your registered email address to receive secure reset credentials.
          </p>
        </div>

        {errorMsg && (
          <div className="rounded-xl border border-rose-200 bg-rose-50 p-3.5 text-xs font-medium text-rose-800 flex items-center gap-2.5">
            <AlertCircle className="h-4 w-4 shrink-0 text-rose-600" />
            <span>{errorMsg}</span>
          </div>
        )}

        <div className="rounded-3xl border border-surface-border bg-white p-7 sm:p-9 shadow-card">
          {submitted ? (
            <div className="text-center space-y-5 py-2">
              <div className="flex h-14 w-14 mx-auto items-center justify-center rounded-2xl bg-emerald-100 text-emerald-600 shadow-xs">
                <CheckCircle2 className="h-7 w-7" />
              </div>
              <h3 className="text-base font-extrabold text-navy-800">Password Reset Requested</h3>
              <p className="text-xs text-slateText-secondary leading-relaxed font-medium">
                If an account exists with <strong className="text-slateText-primary font-bold">{email}</strong>, a secure password reset token has been registered in the database.
              </p>

              {/* Development Testing Mode Token Box */}
              {devToken && (
                <div className="mt-4 rounded-2xl border border-brand-200 bg-brand-50/70 p-4 text-left space-y-2.5 shadow-xs">
                  <div className="flex items-center gap-2 text-xs font-bold text-brand-900">
                    <KeyRound className="h-4 w-4 text-brand-600" />
                    <span>Development Environment Direct Reset:</span>
                  </div>
                  <p className="text-[11px] text-slateText-secondary font-medium">
                    SMTP email delivery is disabled in local development. Use the generated single-use token below to complete testing:
                  </p>
                  <div className="p-2.5 bg-white rounded-xl border border-brand-200 font-mono text-[10px] break-all select-all text-slate-700 shadow-2xs">
                    {devToken}
                  </div>
                  <Link
                    to={`/reset-password?token=${devToken}`}
                    className="inline-flex items-center gap-2 text-xs font-bold text-brand-700 hover:text-white bg-white hover:bg-brand-600 border border-brand-300 rounded-xl px-4 py-2.5 w-full justify-center shadow-xs active:scale-95 transition-all"
                  >
                    <span>Proceed with Token to Reset Password</span>
                    <ExternalLink className="h-3.5 w-3.5" />
                  </Link>
                </div>
              )}

              <div className="pt-2">
                <Link
                  to="/login"
                  className="inline-flex items-center gap-2 text-xs font-bold text-brand-600 hover:text-brand-800"
                >
                  <ArrowLeft className="h-4 w-4" />
                  Return to Sign In
                </Link>
              </div>
            </div>
          ) : (
            <form onSubmit={handleSubmit} className="space-y-4">
              <div>
                <label className="block text-xs font-bold uppercase tracking-wider text-slateText-secondary mb-1.5">
                  Registered Email Address
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

              <button
                type="submit"
                disabled={isSubmitting}
                className="w-full rounded-xl bg-brand-600 py-3 text-xs font-bold text-white shadow-sm hover:bg-brand-700 hover:shadow-md disabled:opacity-50 active:scale-[0.98] transition-all cursor-pointer flex items-center justify-center gap-2"
              >
                {isSubmitting ? (
                  <>
                    <Loader2 className="h-4 w-4 animate-spin" />
                    <span>Processing Request...</span>
                  </>
                ) : (
                  'Request Password Reset'
                )}
              </button>

              <div className="text-center pt-2">
                <Link to="/login" className="text-xs font-bold text-slateText-secondary hover:text-brand-600 transition-colors">
                  Cancel and Return to Sign In
                </Link>
              </div>
            </form>
          )}
        </div>
      </div>
    </div>
  );
};
