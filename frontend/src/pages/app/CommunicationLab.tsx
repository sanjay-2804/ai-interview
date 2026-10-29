import React, { useState, useEffect, useRef } from 'react';
import { api } from '../../services/api';
import { CommunicationPrompt, CommunicationSessionRecord } from '../../types';
import {
  Mic, MicOff, Play, Pause, RotateCcw, Send, Volume2, Sparkles,
  CheckCircle2, AlertCircle, Clock, Award, BarChart3, MessageSquare,
  ChevronRight, ArrowRight, ShieldCheck, History, Info
} from 'lucide-react';

export const CommunicationLab: React.FC = () => {
  const [prompts, setPrompts] = useState<CommunicationPrompt[]>([]);
  const [selectedPrompt, setSelectedPrompt] = useState<CommunicationPrompt | null>(null);
  const [history, setHistory] = useState<CommunicationSessionRecord[]>([]);

  // Audio Recording State
  const [isRecording, setIsRecording] = useState<boolean>(false);
  const [isPaused, setIsPaused] = useState<boolean>(false);
  const [recordDuration, setRecordDuration] = useState<number>(0);
  const [audioBlob, setAudioBlob] = useState<Blob | null>(null);
  const [audioUrl, setAudioUrl] = useState<string | null>(null);
  const [transcript, setTranscript] = useState<string>('');
  const [manualTextFallback, setManualTextFallback] = useState<string>('');
  const [permissionError, setPermissionError] = useState<string | null>(null);

  // Submission & Feedback State
  const [isAnalyzing, setIsAnalyzing] = useState<boolean>(false);
  const [analysisReport, setAnalysisReport] = useState<CommunicationSessionRecord | null>(null);
  const [activeTab, setActiveTab] = useState<'studio' | 'history'>('studio');

  // MediaRecorder & SpeechRecognition refs
  const mediaRecorderRef = useRef<MediaRecorder | null>(null);
  const audioChunksRef = useRef<Blob[]>([]);
  const timerIntervalRef = useRef<any>(null);
  const speechRecognitionRef = useRef<any>(null);

  // Load prompts & history on mount
  useEffect(() => {
    loadPromptsAndHistory();
  }, []);

  const loadPromptsAndHistory = async () => {
    try {
      const p = await api.getCommunicationPrompts();
      setPrompts(p);
      if (p.length > 0) setSelectedPrompt(p[0]);

      const h = await api.getCommunicationHistory();
      setHistory(h);
    } catch (e) {
      console.error('Failed to load communication lab data:', e);
    }
  };

  // Setup Web Speech API for real speech-to-text
  useEffect(() => {
    const SpeechRecognition = (window as any).SpeechRecognition || (window as any).webkitSpeechRecognition;
    if (SpeechRecognition) {
      const recognition = new SpeechRecognition();
      recognition.continuous = true;
      recognition.interimResults = true;
      recognition.lang = 'en-US';

      recognition.onresult = (event: any) => {
        let finalTranscript = '';
        for (let i = 0; i < event.results.length; i++) {
          finalTranscript += event.results[i][0].transcript + ' ';
        }
        setTranscript(finalTranscript.trim());
      };

      recognition.onerror = (e: any) => {
        console.warn('Speech recognition notice:', e.error);
      };

      speechRecognitionRef.current = recognition;
    }
  }, []);

  // Timer effect
  useEffect(() => {
    if (isRecording && !isPaused) {
      timerIntervalRef.current = setInterval(() => {
        setRecordDuration((prev) => prev + 1);
      }, 1000);
    } else {
      clearInterval(timerIntervalRef.current);
    }
    return () => clearInterval(timerIntervalRef.current);
  }, [isRecording, isPaused]);

  // Start Audio Recording
  const handleStartRecording = async () => {
    setPermissionError(null);
    setAudioUrl(null);
    setAudioBlob(null);
    setTranscript('');
    setRecordDuration(0);
    setAnalysisReport(null);
    audioChunksRef.current = [];

    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      const mediaRecorder = new MediaRecorder(stream);
      mediaRecorderRef.current = mediaRecorder;

      mediaRecorder.ondataavailable = (e) => {
        if (e.data.size > 0) audioChunksRef.current.push(e.data);
      };

      mediaRecorder.onstop = () => {
        const blob = new Blob(audioChunksRef.current, { type: 'audio/webm' });
        setAudioBlob(blob);
        const url = URL.createObjectURL(blob);
        setAudioUrl(url);
        // Stop all tracks to release mic hardware
        stream.getTracks().forEach((track) => track.stop());
      };

      mediaRecorder.start(250);
      setIsRecording(true);
      setIsPaused(false);

      // Start live speech recognition if supported
      if (speechRecognitionRef.current) {
        try {
          speechRecognitionRef.current.start();
        } catch (err) {
          // Already started or busy
        }
      }
    } catch (err: any) {
      console.error('Microphone access denied:', err);
      setPermissionError(
        'Microphone permission is required to record your voice. Please allow microphone access in your browser or type your spoken response manually below.'
      );
    }
  };

  // Pause / Resume
  const handleTogglePause = () => {
    if (!mediaRecorderRef.current) return;
    if (isPaused) {
      mediaRecorderRef.current.resume();
      setIsPaused(false);
      try { speechRecognitionRef.current?.start(); } catch (e) {}
    } else {
      mediaRecorderRef.current.pause();
      setIsPaused(true);
      try { speechRecognitionRef.current?.stop(); } catch (e) {}
    }
  };

  // Stop Recording
  const handleStopRecording = () => {
    if (mediaRecorderRef.current && isRecording) {
      mediaRecorderRef.current.stop();
      setIsRecording(false);
      setIsPaused(false);
      try { speechRecognitionRef.current?.stop(); } catch (e) {}
    }
  };

  // Re-record
  const handleResetRecording = () => {
    handleStopRecording();
    setAudioUrl(null);
    setAudioBlob(null);
    setTranscript('');
    setRecordDuration(0);
    setAnalysisReport(null);
  };

  // Submit Attempt for Evaluation
  const handleSubmitAttempt = async () => {
    if (!selectedPrompt) return;
    const finalContent = transcript.trim() || manualTextFallback.trim();
    if (!finalContent) {
      setPermissionError('Please speak aloud or type your spoken response before submitting for analysis.');
      return;
    }

    setIsAnalyzing(true);
    setPermissionError(null);

    try {
      const report: CommunicationSessionRecord = await api.submitCommunicationAttempt({
        category: selectedPrompt.category,
        prompt_title: selectedPrompt.title,
        prompt_question: selectedPrompt.question,
        framework: selectedPrompt.framework,
        transcript: finalContent,
        audio_duration_seconds: recordDuration > 0 ? recordDuration : undefined,
      });

      setAnalysisReport(report);
      // Reload history
      const h = await api.getCommunicationHistory();
      setHistory(h);
    } catch (err: any) {
      setPermissionError(err.message || 'Failed to analyze communication session.');
    } finally {
      setIsAnalyzing(false);
    }
  };

  const formatTimer = (seconds: number) => {
    const mins = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
  };

  return (
    <div className="max-w-6xl mx-auto space-y-8 pb-16">
      {/* Header */}
      <div className="border-b border-surface-border pb-6 flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
        <div>
          <div className="flex items-center gap-2 text-xs font-bold uppercase tracking-wider text-brand-600 mb-1">
            <Mic className="h-4 w-4" />
            <span>Practical Audio Speaking Studio</span>
          </div>
          <h1 className="text-2xl sm:text-3xl font-extrabold text-navy-800 tracking-tight">
            Communication & HR Speaking Lab
          </h1>
          <p className="mt-1 text-sm text-slateText-secondary max-w-3xl leading-relaxed">
            Speak aloud, record your answers, and receive an instant articulation report with filler-word counts,
            speech cadence (WPM), and rubric-weighted feedback.
          </p>
        </div>

        {/* Tab Switcher */}
        <div className="flex items-center gap-2 bg-slate-100 p-1.5 rounded-xl border border-slate-200 self-start sm:self-auto">
          <button
            onClick={() => setActiveTab('studio')}
            className={`px-4 py-2 text-xs font-bold rounded-lg transition-all ${
              activeTab === 'studio'
                ? 'bg-white text-navy-800 shadow-xs'
                : 'text-slateText-secondary hover:text-navy-800'
            }`}
          >
            Speaking Studio
          </button>
          <button
            onClick={() => setActiveTab('history')}
            className={`px-4 py-2 text-xs font-bold rounded-lg transition-all flex items-center gap-1.5 ${
              activeTab === 'history'
                ? 'bg-white text-navy-800 shadow-xs'
                : 'text-slateText-secondary hover:text-navy-800'
            }`}
          >
            <History className="h-3.5 w-3.5" />
            <span>Attempt History ({history.length})</span>
          </button>
        </div>
      </div>

      {permissionError && (
        <div className="rounded-2xl border border-rose-200 bg-rose-50 p-4 text-xs font-medium text-rose-800 flex items-start gap-3">
          <AlertCircle className="h-5 w-5 text-rose-600 shrink-0 mt-0.5" />
          <div>{permissionError}</div>
        </div>
      )}

      {activeTab === 'history' ? (
        /* History View */
        <div className="space-y-4">
          <h2 className="text-lg font-bold text-navy-800">Your Communication Practice Sessions</h2>
          {history.length === 0 ? (
            <div className="rounded-2xl border border-surface-border bg-white p-12 text-center shadow-subtle">
              <Mic className="mx-auto h-12 w-12 text-slate-300 mb-3" />
              <h3 className="text-base font-bold text-navy-800">No speaking sessions recorded yet</h3>
              <p className="text-xs text-slateText-secondary mt-1 max-w-md mx-auto">
                Select a prompt in the Speaking Studio, record your voice, and get your first articulation report.
              </p>
              <button
                onClick={() => setActiveTab('studio')}
                className="mt-5 inline-flex items-center gap-2 rounded-xl bg-brand-600 px-5 py-2.5 text-xs font-bold text-white shadow-sm hover:bg-brand-700"
              >
                Go to Speaking Studio
                <ArrowRight className="h-4 w-4" />
              </button>
            </div>
          ) : (
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              {history.map((h) => (
                <div
                  key={h.id}
                  onClick={() => {
                    setAnalysisReport(h);
                    setActiveTab('studio');
                  }}
                  className="rounded-2xl border border-surface-border bg-white p-5 shadow-subtle hover:border-brand-300 hover:shadow-card-hover transition-all cursor-pointer group"
                >
                  <div className="flex items-start justify-between gap-3 mb-2">
                    <div>
                      <span className="text-[10px] font-bold uppercase tracking-wider text-brand-600 bg-blue-50 px-2 py-0.5 rounded">
                        {h.category}
                      </span>
                      <h4 className="text-sm font-bold text-navy-800 mt-1.5 group-hover:text-brand-700 transition-colors">
                        {h.prompt_title}
                      </h4>
                    </div>
                    <div className="flex items-center gap-1 rounded-xl bg-emerald-50 px-2.5 py-1 text-xs font-bold text-emerald-800 border border-emerald-200">
                      <Award className="h-3.5 w-3.5" />
                      <span>{h.overall_score.toFixed(1)}/10</span>
                    </div>
                  </div>

                  <p className="text-xs text-slateText-secondary line-clamp-2 italic mb-3">
                    "{h.transcript}"
                  </p>

                  <div className="flex items-center justify-between text-[11px] text-slateText-muted pt-3 border-t border-slate-100">
                    <div className="flex items-center gap-3">
                      <span>Cadence: <strong>{h.wpm} WPM</strong></span>
                      <span>Fillers: <strong>{h.filler_words_count}</strong></span>
                    </div>
                    <span>{new Date(h.created_at).toLocaleDateString()}</span>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      ) : (
        /* Speaking Studio View */
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8">
          {/* Left Column: Prompt Selector & Speaking Guide */}
          <div className="lg:col-span-5 space-y-5">
            <div className="rounded-2xl border border-surface-border bg-white p-6 shadow-subtle">
              <h3 className="text-xs font-bold uppercase tracking-wider text-slateText-secondary mb-3">
                1. Select Interview Prompt
              </h3>
              <div className="space-y-2">
                {prompts.map((p) => {
                  const isSelected = selectedPrompt?.id === p.id;
                  return (
                    <div
                      key={p.id}
                      onClick={() => {
                        setSelectedPrompt(p);
                        handleResetRecording();
                      }}
                      className={`p-3.5 rounded-xl border transition-all cursor-pointer ${
                        isSelected
                          ? 'border-brand-600 bg-blue-50/50 shadow-xs'
                          : 'border-slate-200 hover:border-slate-300 bg-white'
                      }`}
                    >
                      <div className="flex items-center justify-between">
                        <span className="text-[10px] font-bold uppercase tracking-wider text-brand-700">
                          {p.category}
                        </span>
                        <span className="text-[10px] text-slateText-muted flex items-center gap-1">
                          <Clock className="h-3 w-3" />
                          ~{p.target_duration_seconds}s
                        </span>
                      </div>
                      <h4 className="text-xs font-bold text-navy-800 mt-1">{p.title}</h4>
                    </div>
                  );
                })}
              </div>
            </div>

            {selectedPrompt && (
              <div className="rounded-2xl border border-surface-border bg-white p-6 shadow-subtle space-y-4">
                <div className="flex items-center gap-2 text-xs font-bold uppercase tracking-wider text-purple-700">
                  <Sparkles className="h-4 w-4" />
                  <span>Structured Speaking Strategy</span>
                </div>
                <div className="rounded-xl bg-purple-50/50 border border-purple-200 p-3.5 text-xs text-purple-900 leading-relaxed font-medium">
                  {selectedPrompt.framework}
                </div>
                <div>
                  <h4 className="text-xs font-bold text-navy-800 mb-1.5">Interviewer's Exact Question:</h4>
                  <p className="text-xs text-slateText-secondary leading-relaxed bg-slate-50 p-3 rounded-xl border border-slate-200">
                    "{selectedPrompt.question}"
                  </p>
                </div>
              </div>
            )}
          </div>

          {/* Right Column: Audio Recorder & Real-time Visualizer */}
          <div className="lg:col-span-7 space-y-6">
            <div className="rounded-2xl border border-surface-border bg-white p-6 sm:p-8 shadow-subtle text-center space-y-6">
              <div>
                <h3 className="text-lg font-bold text-navy-800">
                  {selectedPrompt ? selectedPrompt.title : 'Audio Practice Studio'}
                </h3>
                <p className="text-xs text-slateText-secondary mt-1">
                  Aim for 120-150 words per minute. Speak clearly with minimal filler words.
                </p>
              </div>

              {/* Big Audio Wave / Record Button */}
              <div className="py-6 flex flex-col items-center justify-center">
                <div className="relative">
                  {isRecording && (
                    <div className="absolute inset-0 rounded-full bg-rose-400 animate-ping opacity-30" />
                  )}
                  <button
                    onClick={isRecording ? handleStopRecording : handleStartRecording}
                    className={`relative z-10 flex h-24 w-24 items-center justify-center rounded-full shadow-lg transition-all transform active:scale-95 ${
                      isRecording
                        ? 'bg-rose-600 text-white hover:bg-rose-700'
                        : 'bg-brand-600 text-white hover:bg-brand-700 hover:scale-105'
                    }`}
                  >
                    {isRecording ? <MicOff className="h-10 w-10" /> : <Mic className="h-10 w-10" />}
                  </button>
                </div>

                {/* Duration Timer */}
                <div className="mt-4 flex items-center gap-2 font-mono text-2xl font-extrabold text-navy-800">
                  <div className={`h-2.5 w-2.5 rounded-full ${isRecording ? 'bg-rose-500 animate-pulse' : 'bg-slate-300'}`} />
                  <span>{formatTimer(recordDuration)}</span>
                </div>

                <p className="mt-1 text-xs font-medium text-slateText-secondary">
                  {isRecording
                    ? isPaused
                      ? 'Recording paused. Click Resume or Stop.'
                      : 'Listening... Speak your answer aloud now.'
                    : audioUrl
                    ? 'Recording captured! Listen below or submit for evaluation.'
                    : 'Click microphone button to begin speaking.'}
                </p>
              </div>

              {/* In-Recording Controls */}
              {isRecording && (
                <div className="flex items-center justify-center gap-3">
                  <button
                    onClick={handleTogglePause}
                    className="flex items-center gap-2 rounded-xl border border-slate-200 bg-slate-50 px-4 py-2 text-xs font-bold text-slateText-primary hover:bg-slate-100"
                  >
                    {isPaused ? <Play className="h-3.5 w-3.5" /> : <Pause className="h-3.5 w-3.5" />}
                    <span>{isPaused ? 'Resume' : 'Pause'}</span>
                  </button>
                  <button
                    onClick={handleStopRecording}
                    className="flex items-center gap-2 rounded-xl bg-navy-800 px-5 py-2 text-xs font-bold text-white hover:bg-navy-900 shadow-xs"
                  >
                    <span>Finish Recording</span>
                  </button>
                </div>
              )}

              {/* Audio Playback & Re-record Controls */}
              {audioUrl && !isRecording && (
                <div className="p-4 rounded-xl bg-slate-50 border border-slate-200 flex flex-col sm:flex-row items-center justify-between gap-4">
                  <audio src={audioUrl} controls className="h-10 w-full sm:max-w-xs" />
                  <button
                    onClick={handleResetRecording}
                    className="flex items-center gap-1.5 text-xs font-semibold text-slateText-secondary hover:text-rose-600 transition-colors"
                  >
                    <RotateCcw className="h-3.5 w-3.5" />
                    <span>Re-record</span>
                  </button>
                </div>
              )}

              {/* Live Speech-to-Text Transcript Display */}
              <div className="text-left space-y-2">
                <div className="flex items-center justify-between">
                  <label className="text-xs font-bold text-navy-800">
                    Spoken Transcript (Captured Speech):
                  </label>
                  <span className="text-[11px] text-slateText-muted">
                    {transcript.trim() ? `${transcript.trim().split(/\s+/).length} words` : '0 words'}
                  </span>
                </div>
                <div className="p-4 rounded-xl border border-slate-200 bg-slate-50 min-h-[90px] text-xs text-slateText-primary leading-relaxed font-mono">
                  {transcript || (
                    <span className="text-slateText-muted italic">
                      Live speech will transcribe here as you speak. If you prefer, you can also type below.
                    </span>
                  )}
                </div>

                {!transcript && !isRecording && (
                  <div className="pt-2">
                    <label className="text-[11px] font-semibold text-slateText-secondary block mb-1">
                      Manual Input Alternative (Optional):
                    </label>
                    <textarea
                      value={manualTextFallback}
                      onChange={(e) => setManualTextFallback(e.target.value)}
                      placeholder="Type your spoken draft here if microphone is unavailable..."
                      rows={3}
                      className="w-full rounded-xl border border-slate-200 p-3 text-xs text-slateText-primary focus:border-brand-600 focus:outline-none"
                    />
                  </div>
                )}
              </div>

              {/* Submit for Analysis Button */}
              <div>
                <button
                  onClick={handleSubmitAttempt}
                  disabled={isRecording || isAnalyzing || (!transcript.trim() && !manualTextFallback.trim())}
                  className="w-full flex items-center justify-center gap-2 rounded-xl bg-brand-600 px-6 py-3.5 text-sm font-bold text-white shadow-sm hover:bg-brand-700 disabled:opacity-50 disabled:cursor-not-allowed transition-all"
                >
                  {isAnalyzing ? (
                    <>
                      <div className="h-4 w-4 animate-spin rounded-full border-2 border-white border-t-transparent" />
                      <span>Analyzing Speech Cadence & Rubric...</span>
                    </>
                  ) : (
                    <>
                      <Sparkles className="h-4 w-4" />
                      <span>Submit for Comprehensive Articulation Report</span>
                    </>
                  )}
                </button>
              </div>
            </div>

            {/* Analysis Report Card (Rendered After Submission) */}
            {analysisReport && (
              <div className="rounded-2xl border border-emerald-200 bg-white p-6 sm:p-8 shadow-subtle space-y-6 animate-fadeIn">
                {/* Score Header */}
                <div className="flex items-start justify-between border-b border-slate-200 pb-5">
                  <div>
                    <span className="text-[10px] font-bold uppercase tracking-wider text-emerald-700 bg-emerald-50 px-2.5 py-0.5 rounded-full border border-emerald-200">
                      Articulation Evaluation Completed
                    </span>
                    <h3 className="text-xl font-bold text-navy-800 mt-2">
                      Speech Analysis Report: {analysisReport.prompt_title}
                    </h3>
                  </div>
                  <div className="text-right">
                    <div className="text-3xl font-extrabold text-brand-700">
                      {analysisReport.overall_score.toFixed(1)}
                      <span className="text-sm font-medium text-slateText-muted">/10</span>
                    </div>
                    <span className="text-[10px] uppercase font-bold text-slateText-muted tracking-wider">
                      Overall Score
                    </span>
                  </div>
                </div>

                {/* Weighted 5-Pillar Rubric Breakdown */}
                <div>
                  <h4 className="text-xs font-bold uppercase tracking-wider text-slateText-secondary mb-3">
                    Weighted 5-Pillar Evaluation Rubric
                  </h4>
                  <div className="grid grid-cols-2 sm:grid-cols-5 gap-2.5 text-center">
                    <div className="p-3 rounded-xl bg-slate-50 border border-slate-200">
                      <div className="text-sm font-bold text-navy-800">{analysisReport.relevance_score.toFixed(1)}/10</div>
                      <div className="text-[10px] text-slateText-secondary font-medium mt-0.5">Relevance (25%)</div>
                    </div>
                    <div className="p-3 rounded-xl bg-slate-50 border border-slate-200">
                      <div className="text-sm font-bold text-navy-800">{analysisReport.clarity_score.toFixed(1)}/10</div>
                      <div className="text-[10px] text-slateText-secondary font-medium mt-0.5">Clarity (25%)</div>
                    </div>
                    <div className="p-3 rounded-xl bg-slate-50 border border-slate-200">
                      <div className="text-sm font-bold text-navy-800">{analysisReport.grammar_score.toFixed(1)}/10</div>
                      <div className="text-[10px] text-slateText-secondary font-medium mt-0.5">Grammar (20%)</div>
                    </div>
                    <div className="p-3 rounded-xl bg-slate-50 border border-slate-200">
                      <div className="text-sm font-bold text-navy-800">{analysisReport.conciseness_score.toFixed(1)}/10</div>
                      <div className="text-[10px] text-slateText-secondary font-medium mt-0.5">Structure (15%)</div>
                    </div>
                    <div className="p-3 rounded-xl bg-slate-50 border border-slate-200">
                      <div className="text-sm font-bold text-navy-800">{analysisReport.delivery_score.toFixed(1)}/10</div>
                      <div className="text-[10px] text-slateText-secondary font-medium mt-0.5">Cadence (15%)</div>
                    </div>
                  </div>
                </div>

                {/* Delivery Metrics: WPM & Fillers */}
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                  <div className="p-4 rounded-xl bg-blue-50/60 border border-blue-200 flex items-center justify-between">
                    <div>
                      <span className="text-[10px] uppercase font-bold text-blue-800 tracking-wider">
                        Speaking Cadence
                      </span>
                      <div className="text-xl font-extrabold text-navy-800 mt-0.5">
                        {analysisReport.wpm} WPM
                      </div>
                      <p className="text-[11px] text-slateText-secondary mt-0.5">
                        Target range: 120 - 150 words per minute
                      </p>
                    </div>
                    <div className="h-10 w-10 rounded-xl bg-blue-100 text-brand-700 flex items-center justify-center font-bold">
                      <BarChart3 className="h-5 w-5" />
                    </div>
                  </div>

                  <div className="p-4 rounded-xl bg-amber-50/60 border border-amber-200 flex items-center justify-between">
                    <div>
                      <span className="text-[10px] uppercase font-bold text-amber-800 tracking-wider">
                        Filler Word Observations
                      </span>
                      <div className="text-xl font-extrabold text-navy-800 mt-0.5">
                        {analysisReport.filler_words_count} detected
                      </div>
                      <p className="text-[11px] text-slateText-secondary mt-0.5">
                        {analysisReport.filler_words_list.length > 0
                          ? `Found: "${analysisReport.filler_words_list.join('", "')}"`
                          : 'Zero excessive filler words detected!'}
                      </p>
                    </div>
                    <div className="h-10 w-10 rounded-xl bg-amber-100 text-amber-800 flex items-center justify-center font-bold">
                      <Volume2 className="h-5 w-5" />
                    </div>
                  </div>
                </div>

                {/* Strengths & Priority Improvements */}
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  <div className="p-4 rounded-xl bg-emerald-50/40 border border-emerald-200 space-y-2">
                    <h5 className="text-xs font-bold text-emerald-900 flex items-center gap-1.5">
                      <CheckCircle2 className="h-4 w-4 text-emerald-600" />
                      Demonstrated Strengths
                    </h5>
                    <ul className="text-xs text-slateText-primary space-y-1.5 pl-5 list-disc">
                      {analysisReport.strengths.map((s, idx) => (
                        <li key={idx} className="leading-relaxed">{s}</li>
                      ))}
                    </ul>
                  </div>

                  <div className="p-4 rounded-xl bg-amber-50/40 border border-amber-200 space-y-2">
                    <h5 className="text-xs font-bold text-amber-900 flex items-center gap-1.5">
                      <AlertCircle className="h-4 w-4 text-amber-600" />
                      Priority Improvements
                    </h5>
                    <ul className="text-xs text-slateText-primary space-y-1.5 pl-5 list-disc">
                      {analysisReport.improvements.map((imp, idx) => (
                        <li key={idx} className="leading-relaxed">{imp}</li>
                      ))}
                    </ul>
                  </div>
                </div>

                {/* Benchmark Model Answer */}
                {analysisReport.sample_answer && (
                  <div className="p-5 rounded-xl bg-slate-50 border border-slate-200 space-y-2">
                    <h5 className="text-xs font-bold text-navy-800 flex items-center gap-2">
                      <Info className="h-4 w-4 text-brand-600" />
                      Reference Solution & Ideal Response Delivery
                    </h5>
                    <p className="text-xs text-slateText-secondary leading-relaxed italic">
                      "{analysisReport.sample_answer}"
                    </p>
                  </div>
                )}
              </div>
            )}
          </div>
        </div>
      )}
    </div>
  );
};
