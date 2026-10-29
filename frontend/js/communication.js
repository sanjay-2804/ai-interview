/**
 * InterviewAI — Communication Lab Controller
 * Implements real browser MediaRecorder, Web Speech transcription,
 * transparent 5-pillar rubric evaluation, and attempt history persistence.
 */

let allPrompts = [];
let activePrompt = null;
let mediaRecorder = null;
let audioChunks = [];
let audioBlob = null;
let recordTimerInterval = null;
let recordDurationSeconds = 0;
let recognition = null;

document.addEventListener('DOMContentLoaded', async () => {
  const user = await auth.requireAuth();
  if (!user) return;

  bindRecorderEvents();
  initSpeechRecognition();
  loadPrompts();
  loadHistory();
});

async function loadPrompts() {
  const listEl = document.getElementById('promptsList');
  try {
    const data = await api.get('/communication/prompts');
    allPrompts = data || [];
    renderPromptsList();
    if (allPrompts.length > 0) {
      selectPrompt(allPrompts[0].id);
    }
  } catch (err) {
    console.error('Failed to load prompts:', err);
    if (listEl) listEl.innerHTML = `<div style="font-size:0.875rem;color:#ef4444;">Failed to load prompts.</div>`;
  }
}

function renderPromptsList() {
  const listEl = document.getElementById('promptsList');
  if (!listEl) return;

  let html = '';
  allPrompts.forEach(p => {
    const isActive = activePrompt && activePrompt.id === p.id;
    html += `
      <div class="card prompt-item" data-id="${p.id}" style="padding:0.6rem 0.75rem; cursor:pointer; border-color:${isActive ? 'var(--color-primary)' : 'var(--color-border)'}; background:${isActive ? 'var(--color-primary-light)' : '#ffffff'};">
        <div style="font-weight:600; font-size:0.8125rem; color:var(--color-text-main);">${escapeHtml(p.title)}</div>
        <div style="font-size:0.75rem; color:var(--color-text-subtle);">${escapeHtml(p.category)}</div>
      </div>
    `;
  });

  listEl.innerHTML = html;

  listEl.querySelectorAll('.prompt-item').forEach(el => {
    el.addEventListener('click', () => {
      const id = parseInt(el.dataset.id, 10);
      selectPrompt(id);
    });
  });
}

function selectPrompt(id) {
  const prompt = allPrompts.find(p => p.id === id);
  if (!prompt) return;

  activePrompt = prompt;
  renderPromptsList();

  document.getElementById('promptTitle').textContent = prompt.title;
  document.getElementById('promptCategoryBadge').textContent = prompt.category;
  document.getElementById('promptQuestion').textContent = prompt.question;
  document.getElementById('promptFramework').textContent = prompt.framework || 'Structured response';
  document.getElementById('targetDurationBadge').textContent = `Target: ${prompt.target_duration_seconds || 90}s`;

  // Reset audio & transcript
  resetAudio();
}

async function loadHistory() {
  const listEl = document.getElementById('historyList');
  try {
    const history = await api.get('/communication/history');
    if (!history || history.length === 0) {
      listEl.innerHTML = `<div style="font-size:0.8125rem; color:var(--color-text-subtle);">No previous sessions recorded.</div>`;
      return;
    }

    let html = '';
    history.forEach(item => {
      html += `
        <div style="padding:0.5rem 0.75rem; border:1px solid var(--color-border); border-radius:var(--radius-sm); background:var(--color-bg-page); font-size:0.8125rem;">
          <div style="display:flex; justify-content:space-between; font-weight:600;">
            <span>${escapeHtml(item.prompt_title || 'Speaking Round')}</span>
            <span style="color:var(--color-primary);">${item.overall_score || 0}/100</span>
          </div>
          <div style="font-size:0.75rem; color:var(--color-text-subtle); display:flex; justify-content:space-between; margin-top:0.15rem;">
            <span>${item.wpm || 0} WPM</span>
            <span>${item.created_at ? new Date(item.created_at).toLocaleDateString() : ''}</span>
          </div>
        </div>
      `;
    });
    listEl.innerHTML = html;
  } catch (err) {
    console.warn('Could not load communication history:', err);
  }
}

function initSpeechRecognition() {
  const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  if (SpeechRecognition) {
    recognition = new SpeechRecognition();
    recognition.continuous = true;
    recognition.interimResults = true;
    recognition.lang = 'en-US';

    recognition.onresult = (event) => {
      let finalTranscript = '';
      for (let i = 0; i < event.results.length; ++i) {
        finalTranscript += event.results[i][0].transcript + ' ';
      }
      document.getElementById('speechTranscript').value = finalTranscript.trim();
      document.getElementById('submitSpeechBtn').disabled = finalTranscript.trim().length === 0;
    };

    recognition.onerror = (e) => {
      console.warn('Speech recognition warning:', e.error);
    };
  }
}

function bindRecorderEvents() {
  const startBtn = document.getElementById('startRecordBtn');
  const stopBtn = document.getElementById('stopRecordBtn');
  const reRecordBtn = document.getElementById('reRecordBtn');
  const submitBtn = document.getElementById('submitSpeechBtn');
  const transcriptInput = document.getElementById('speechTranscript');

  startBtn.addEventListener('click', startRecording);
  stopBtn.addEventListener('click', stopRecording);
  reRecordBtn.addEventListener('click', resetAudio);

  transcriptInput.addEventListener('input', () => {
    submitBtn.disabled = transcriptInput.value.trim().length === 0;
  });

  submitBtn.addEventListener('click', submitSpeechEvaluation);
}

async function startRecording() {
  if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
    showToast('Your browser does not support audio recording. You can still type or paste your response in the box below.', 'info');
    return;
  }

  try {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    audioChunks = [];
    mediaRecorder = new MediaRecorder(stream);

    mediaRecorder.ondataavailable = (e) => {
      if (e.data.size > 0) {
        audioChunks.push(e.data);
      }
    };

    mediaRecorder.onstop = () => {
      audioBlob = new Blob(audioChunks, { type: 'audio/webm' });
      const audioUrl = URL.createObjectURL(audioBlob);
      const player = document.getElementById('audioPlayer');
      player.src = audioUrl;
      document.getElementById('audioPlaybackContainer').style.display = 'block';

      // Stream tracks stop
      stream.getTracks().forEach(track => track.stop());
    };

    mediaRecorder.start();

    // Start recognition if available
    if (recognition) {
      try { recognition.start(); } catch {}
    }

    // UI Updates
    document.getElementById('startRecordBtn').style.display = 'none';
    document.getElementById('stopRecordBtn').style.display = 'inline-flex';
    document.getElementById('reRecordBtn').style.display = 'none';
    
    const statusPill = document.getElementById('recordingStatusPill');
    statusPill.className = 'badge badge-danger';
    statusPill.textContent = '● Recording Audio...';

    // Timer
    recordDurationSeconds = 0;
    updateTimerText();
    recordTimerInterval = setInterval(() => {
      recordDurationSeconds++;
      updateTimerText();
    }, 1000);

  } catch (err) {
    console.error('Microphone access denied:', err);
    showToast('Microphone permission was denied. Please allow microphone access or paste your speech text.', 'error');
  }
}

function stopRecording() {
  if (mediaRecorder && mediaRecorder.state !== 'inactive') {
    mediaRecorder.stop();
  }
  if (recognition) {
    try { recognition.stop(); } catch {}
  }
  if (recordTimerInterval) {
    clearInterval(recordTimerInterval);
    recordTimerInterval = null;
  }

  document.getElementById('stopRecordBtn').style.display = 'none';
  document.getElementById('reRecordBtn').style.display = 'inline-flex';

  const statusPill = document.getElementById('recordingStatusPill');
  statusPill.className = 'badge badge-success';
  statusPill.textContent = 'Audio Captured';

  const transcript = document.getElementById('speechTranscript').value.trim();
  if (transcript.length > 0) {
    document.getElementById('submitSpeechBtn').disabled = false;
  }
}

function resetAudio() {
  if (recordTimerInterval) {
    clearInterval(recordTimerInterval);
    recordTimerInterval = null;
  }
  recordDurationSeconds = 0;
  updateTimerText();

  audioBlob = null;
  audioChunks = [];

  document.getElementById('startRecordBtn').style.display = 'inline-flex';
  document.getElementById('stopRecordBtn').style.display = 'none';
  document.getElementById('reRecordBtn').style.display = 'none';
  document.getElementById('audioPlaybackContainer').style.display = 'none';

  const statusPill = document.getElementById('recordingStatusPill');
  statusPill.className = 'badge badge-neutral';
  statusPill.textContent = 'Microphone Idle';

  document.getElementById('speechTranscript').value = '';
  document.getElementById('submitSpeechBtn').disabled = true;
  document.getElementById('evaluationReportCard').style.display = 'none';
}

function updateTimerText() {
  const m = Math.floor(recordDurationSeconds / 60);
  const s = recordDurationSeconds % 60;
  document.getElementById('recordingTimer').textContent = `${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
}

async function submitSpeechEvaluation() {
  if (!activePrompt) return;
  const transcript = document.getElementById('speechTranscript').value.trim();
  if (!transcript) {
    showToast('Please speak or enter a transcript to evaluate.', 'info');
    return;
  }

  const submitBtn = document.getElementById('submitSpeechBtn');
  setButtonLoading(submitBtn, true, 'Evaluating 5-Pillar Rubric...');

  try {
    const payload = {
      prompt_id: activePrompt.id,
      prompt_title: activePrompt.title,
      prompt_question: activePrompt.question,
      category: activePrompt.category,
      framework: activePrompt.framework,
      audio_duration_seconds: recordDurationSeconds > 0 ? recordDurationSeconds : 45,
      transcript: transcript
    };

    const result = await api.post('/communication/submit', payload);

    // Render Evaluation Report
    renderEvaluationReport(result);
    showToast('Speech evaluated successfully!', 'success');
    loadHistory();

  } catch (err) {
    showToast(err.message || 'Evaluation failed.', 'error');
  } finally {
    setButtonLoading(submitBtn, false);
  }
}

function renderEvaluationReport(res) {
  const card = document.getElementById('evaluationReportCard');
  card.style.display = 'block';

  document.getElementById('overallScoreVal').textContent = `${res.overall_score || 0}/100`;
  document.getElementById('relevanceScore').textContent = `${res.relevance_score || 0}/25`;
  document.getElementById('clarityScore').textContent = `${res.clarity_score || 0}/25`;
  document.getElementById('grammarScore').textContent = `${res.grammar_score || 0}/20`;
  document.getElementById('structureScore').textContent = `${res.conciseness_score || 0}/15`;
  document.getElementById('deliveryScore').textContent = `${res.delivery_score || 0}/15`;

  document.getElementById('wpmCadence').textContent = `${res.wpm || 130} WPM`;
  document.getElementById('fillersCount').textContent = `${res.filler_words_count || 0} detected`;
  
  const fillerListText = (res.filler_words_list && res.filler_words_list.length > 0)
    ? res.filler_words_list.join(', ')
    : 'None detected';
  document.getElementById('fillersList').textContent = `Examples: ${fillerListText}`;

  // Concepts Demonstrated list
  const demEl = document.getElementById('conceptsDemonstratedList');
  if (demEl) {
    const demItems = Array.isArray(res.concepts_demonstrated) ? res.concepts_demonstrated : [];
    demEl.innerHTML = demItems.length > 0
      ? demItems.map(item => `<li>${escapeHtml(item)}</li>`).join('')
      : '<li>Direct conversational engagement with question theme.</li>';
  }

  // Concepts Missing list
  const misEl = document.getElementById('conceptsMissingList');
  if (misEl) {
    const misItems = Array.isArray(res.concepts_missing) ? res.concepts_missing : [];
    misEl.innerHTML = misItems.length > 0
      ? misItems.map(item => `<li>${escapeHtml(item)}</li>`).join('')
      : '<li>No major thematic competencies missed.</li>';
  }

  // Targeted Follow-Up Question
  const followUpEl = document.getElementById('followUpQuestionText');
  if (followUpEl) {
    followUpEl.textContent = res.follow_up_question || 'Can you explain the most challenging trade-off you encountered in this context?';
  }

  const coachEl = document.getElementById('personalizedCoachingText');
  if (coachEl) {
    coachEl.textContent = res.personalized_coaching ? `💡 Coaching Tip: ${res.personalized_coaching}` : '';
  }

  const strengthsEl = document.getElementById('strengthsText');
  if (strengthsEl) {
    strengthsEl.textContent = Array.isArray(res.strengths) ? res.strengths.join(' • ') : (res.strengths || '');
  }

  const improvementsEl = document.getElementById('improvementsText');
  if (improvementsEl) {
    improvementsEl.textContent = Array.isArray(res.improvements) ? res.improvements.join(' • ') : (res.improvements || '');
  }

  document.getElementById('modelAnswerText').textContent = res.sample_answer || activePrompt.sample_answer || '';

  if (window.lucide) lucide.createIcons();
  card.scrollIntoView({ behavior: 'smooth' });
}
