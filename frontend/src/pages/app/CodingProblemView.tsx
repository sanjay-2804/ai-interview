import React, { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import { api } from '../../services/api';
import { CodingProblemDetail, CodeRunResult } from '../../types';
import {
  ArrowLeft, Play, CheckCircle2, XCircle, Code2, ExternalLink,
  Lightbulb, ChevronDown, ChevronUp, Terminal, Clock, Sparkles
} from 'lucide-react';

export const CodingProblemView: React.FC = () => {
  const { problemId } = useParams<{ problemId: string }>();
  const [problem, setProblem] = useState<CodingProblemDetail | null>(null);
  const [language, setLanguage] = useState<string>('python');
  const [code, setCode] = useState<string>('');
  const [isRunning, setIsRunning] = useState<boolean>(false);
  const [runResult, setRunResult] = useState<CodeRunResult | null>(null);
  const [showHints, setShowHints] = useState<boolean>(false);
  const [loading, setLoading] = useState<boolean>(true);

  useEffect(() => {
    if (problemId) {
      api.getCodingProblemDetail(parseInt(problemId, 10))
        .then((data) => {
          setProblem(data);
          setCode(data.starter_code_python);
        })
        .catch((err) => console.error('Failed to load problem:', err))
        .finally(() => setLoading(false));
    }
  }, [problemId]);

  // Update starter code on language switch
  const handleLanguageChange = (newLang: string) => {
    setLanguage(newLang);
    if (!problem) return;
    switch (newLang) {
      case 'python':
        setCode(problem.starter_code_python);
        break;
      case 'javascript':
        setCode(problem.starter_code_javascript);
        break;
      case 'java':
        setCode(problem.starter_code_java);
        break;
      case 'cpp':
        setCode(problem.starter_code_cpp);
        break;
      default:
        setCode(problem.starter_code_python);
    }
  };

  const handleRunCode = async () => {
    if (!problem || !code || isRunning) return;
    setIsRunning(true);
    setRunResult(null);
    try {
      const res = await api.runCode({
        problem_id: problem.id,
        language,
        code,
      });
      setRunResult(res);
    } catch (err: any) {
      setRunResult({
        status: 'wrong_answer',
        output_log: `Execution Error: ${err.message || 'Unknown error occurred'}`,
        runtime_ms: 0,
        memory_kb: 0,
        passed_tests: 0,
        total_tests: 1,
        is_sample_preview: true,
        guidance: 'Review your code structure and syntax.',
      });
    } finally {
      setIsRunning(false);
    }
  };

  if (loading) {
    return (
      <div className="flex h-96 items-center justify-center">
        <div className="h-8 w-8 animate-spin rounded-full border-4 border-brand-600 border-t-transparent" />
      </div>
    );
  }

  if (!problem) {
    return (
      <div className="text-center py-12">
        <p className="text-sm text-slateText-secondary">Problem not found.</p>
        <Link to="/app/coding" className="mt-4 inline-flex items-center gap-2 text-sm text-brand-600">
          <ArrowLeft className="h-4 w-4" /> Back to Coding Practice
        </Link>
      </div>
    );
  }

  return (
    <div className="h-full flex flex-col space-y-4 pb-12">
      {/* Top action bar */}
      <div className="flex items-center justify-between border-b border-surface-border pb-4">
        <Link
          to="/app/coding"
          className="inline-flex items-center gap-2 text-xs font-semibold text-slateText-secondary hover:text-brand-600 transition-all hover:-translate-x-0.5 group"
        >
          <ArrowLeft className="h-4 w-4 transition-transform group-hover:-translate-x-1" />
          Back to Problem Bank
        </Link>

        {problem.external_url && (
          <a
            href={problem.external_url}
            target="_blank"
            rel="noopener noreferrer"
            className="inline-flex items-center gap-2 text-xs font-bold text-brand-600 hover:text-brand-800 bg-brand-50 hover:bg-brand-100 border border-brand-200 px-3.5 py-1.5 rounded-xl transition-all shadow-xs"
          >
            <span>Solve on {problem.external_platform || 'LeetCode'}</span>
            <ExternalLink className="h-3.5 w-3.5" />
          </a>
        )}
      </div>

      {/* Two-Column Problem Solving Workspace */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 flex-1 min-h-[700px]">
        {/* Left Column: Problem Description & Test Cases (5 Cols) */}
        <div className="lg:col-span-5 rounded-2xl border border-surface-border bg-white p-7 shadow-card overflow-y-auto max-h-[820px] space-y-6">
          <div>
            <div className="flex items-center gap-2.5 mb-2.5">
              <span className="text-[10px] font-bold uppercase px-2.5 py-1 rounded-full bg-brand-100 text-brand-800">
                {problem.category}
              </span>
              <span
                className={`text-[10px] font-bold uppercase px-2.5 py-1 rounded-full ${
                  problem.difficulty === 'Easy'
                    ? 'bg-emerald-100 text-emerald-800'
                    : problem.difficulty === 'Medium'
                    ? 'bg-amber-100 text-amber-800'
                    : 'bg-rose-100 text-rose-800'
                }`}
              >
                {problem.difficulty}
              </span>
            </div>

            <h1 className="text-xl font-extrabold text-navy-800 tracking-tight">
              {problem.title}
            </h1>
          </div>

          {/* Description */}
          <div className="text-sm text-slateText-primary leading-relaxed whitespace-pre-line space-y-3">
            {problem.description}
          </div>

          {/* Sample Input / Output */}
          <div className="space-y-3 border-t border-slate-100 pt-4">
            <h4 className="text-xs font-bold uppercase tracking-wider text-slateText-secondary">
              Sample Examples
            </h4>
            <div className="rounded-xl bg-slate-50 border border-slate-200 p-3.5 text-xs font-mono space-y-2">
              <div>
                <span className="text-slateText-muted block text-[10px] uppercase font-sans">Input:</span>
                <span className="text-slateText-primary">{problem.sample_input}</span>
              </div>
              <div className="border-t border-slate-200 pt-2">
                <span className="text-slateText-muted block text-[10px] uppercase font-sans">Expected Output:</span>
                <span className="text-emerald-700 font-bold">{problem.sample_output}</span>
              </div>
            </div>
          </div>

          {/* Constraints */}
          <div className="space-y-2 border-t border-slate-100 pt-4">
            <h4 className="text-xs font-bold uppercase tracking-wider text-slateText-secondary">
              Constraints
            </h4>
            <pre className="rounded-lg bg-slate-50 border border-slate-200 p-3 text-xs font-mono text-slateText-primary whitespace-pre-wrap">
              {problem.constraints}
            </pre>
          </div>

          {/* Complexity Expectations */}
          <div className="rounded-xl border border-blue-100 bg-brand-50/50 p-3.5 text-xs">
            <div className="font-bold text-brand-900 mb-1">Target Complexity:</div>
            <div className="flex gap-4 text-brand-800">
              <span>Time: <code>{problem.time_complexity}</code></span>
              <span>Space: <code>{problem.space_complexity}</code></span>
            </div>
          </div>

          {/* Hints Accordion */}
          {problem.hints && problem.hints.length > 0 && (
            <div className="border-t border-slate-100 pt-4">
              <button
                onClick={() => setShowHints(!showHints)}
                className="flex w-full items-center justify-between text-xs font-bold text-slateText-secondary hover:text-brand-600 transition-colors"
              >
                <span className="flex items-center gap-1.5">
                  <Lightbulb className="h-4 w-4 text-amber-500" />
                  Algorithmic Hints ({problem.hints.length})
                </span>
                {showHints ? <ChevronUp className="h-4 w-4" /> : <ChevronDown className="h-4 w-4" />}
              </button>

              {showHints && (
                <div className="mt-3 space-y-2 pl-2">
                  {problem.hints.map((hint, idx) => (
                    <div key={idx} className="p-2.5 rounded-lg bg-amber-50/60 border border-amber-200 text-xs text-amber-900">
                      <strong>Hint {idx + 1}: </strong> {hint}
                    </div>
                  ))}
                </div>
              )}
            </div>
          )}
        </div>

        {/* Right Column: Code Editor & Execution Terminal (7 Cols) */}
        <div className="lg:col-span-7 flex flex-col rounded-2xl border border-surface-border bg-white shadow-subtle overflow-hidden">
          {/* Editor Toolbar */}
          <div className="flex items-center justify-between bg-slate-50 px-5 py-3 text-navy-800 border-b border-surface-border">
            <div className="flex items-center gap-3">
              <Code2 className="h-4 w-4 text-brand-600" />
              <select
                value={language}
                onChange={(e) => handleLanguageChange(e.target.value)}
                className="rounded-xl bg-white border border-slate-300 px-3 py-1.5 text-xs text-slateText-primary font-semibold focus:outline-none focus:border-brand-600 shadow-xs cursor-pointer hover:border-brand-400 transition-colors"
              >
                <option value="python">Python 3</option>
                <option value="javascript">JavaScript (ES6)</option>
                <option value="java">Java 17</option>
                <option value="cpp">C++ 20</option>
              </select>
            </div>

            <button
              onClick={handleRunCode}
              disabled={isRunning}
              className="inline-flex items-center gap-2 rounded-xl bg-brand-600 px-5 py-2 text-xs font-bold text-white shadow-xs hover:bg-brand-700 hover:shadow-md active:scale-[0.98] disabled:opacity-50 transition-all cursor-pointer"
            >
              <Play className="h-3.5 w-3.5 fill-current" />
              {isRunning ? 'Running Checks...' : 'Run & Test'}
            </button>
          </div>

          {/* Code Textarea Area */}
          <div className="flex-1 min-h-[360px] bg-slate-50/40 p-4">
            <textarea
              value={code}
              onChange={(e) => setCode(e.target.value)}
              spellCheck={false}
              className="w-full h-full min-h-[340px] bg-transparent text-slate-900 font-mono text-xs leading-relaxed focus:outline-none resize-none"
              placeholder="// Write your algorithmic solution here..."
            />
          </div>

          {/* Test Case & Execution Output */}
          <div className="border-t border-surface-border bg-slate-50/80 p-4 text-xs font-mono text-slate-800">
            <div className="flex items-center justify-between mb-2 pb-2 border-b border-slate-200">
              <span className="flex items-center gap-1.5 text-[11px] font-bold text-slateText-secondary uppercase tracking-wider font-sans">
                <Terminal className="h-3.5 w-3.5 text-brand-600" />
                Execution Results & Sample Tests
              </span>
              {runResult && (
                <span
                  className={`px-2.5 py-0.5 rounded text-[10px] font-bold uppercase font-sans border ${
                    runResult.status === 'accepted'
                      ? 'bg-emerald-50 text-emerald-700 border-emerald-200'
                      : 'bg-rose-50 text-rose-700 border-rose-200'
                  }`}
                >
                  {runResult.status.replace('_', ' ')}
                </span>
              )}
            </div>

            {runResult ? (
              <div className="space-y-2">
                <pre className="text-slate-800 whitespace-pre-wrap leading-relaxed text-[11px] bg-white border border-slate-200 rounded-lg p-3">
                  {runResult.output_log}
                </pre>
                <div className="text-[11px] text-slateText-secondary font-sans pt-1">
                  {runResult.guidance}
                </div>
              </div>
            ) : (
              <p className="text-slateText-muted text-[11px] font-sans">
                Click "Run & Test" to evaluate your logic against sample test cases.
              </p>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

