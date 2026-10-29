/**
 * InterviewAI — Aptitude Assessment Controller
 * Handles 7 Learning Modes, Question Locks, Timer Countdown,
 * Strict Session Integrity, and 14-Point Educational Explanations.
 */

let currentSession = null;
let currentQuestionIndex = 0;
let selectedOptionKey = null;
let timerInterval = null;
let timeRemaining = 0;

document.addEventListener('DOMContentLoaded', async () => {
  const user = await auth.requireAuth();
  if (!user) return;

  initModes();
  bindRunnerEvents();

  // Check URL query parameters (e.g. ?mode=weak)
  const urlParams = new URLSearchParams(window.location.search);
  const requestedMode = urlParams.get('mode');
  if (requestedMode) {
    launchSession(requestedMode);
  } else {
    // Check if there is an active session in sessionStorage
    const savedSessionId = sessionStorage.getItem('active_aptitude_session_id');
    if (savedSessionId) {
      resumeSession(parseInt(savedSessionId, 10));
    }
  }
});

function initModes() {
  document.querySelectorAll('.launch-mode-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.stopPropagation();
      const mode = btn.dataset.mode;
      if (mode === 'cheatsheet') {
        toggleCheatsheet(true);
      } else {
        launchSession(mode);
      }
    });
  });

  const closeCheatsheetBtn = document.getElementById('closeCheatsheetBtn');
  if (closeCheatsheetBtn) {
    closeCheatsheetBtn.addEventListener('click', () => toggleCheatsheet(false));
  }
}

function toggleCheatsheet(show) {
  const modal = document.getElementById('cheatsheetModal');
  if (modal) {
    modal.style.display = show ? 'block' : 'none';
    if (show) modal.scrollIntoView({ behavior: 'smooth' });
  }
}

async function launchSession(mode) {
  let category = 'All';
  let questionCount = 10;
  let timeLimitSeconds = null;

  if (mode === 'timed') {
    timeLimitSeconds = 900; // 15 mins
    questionCount = 10;
  } else if (mode === 'mock') {
    timeLimitSeconds = 1800; // 30 mins
    questionCount = 25;
  } else if (mode === 'daily') {
    questionCount = 5;
  } else if (mode === 'weak') {
    questionCount = 10;
  }

  try {
    const payload = {
      category: category,
      subcategory: 'all',
      difficulty: 'all',
      question_count: questionCount,
      session_mode: mode,
      time_limit_seconds: timeLimitSeconds
    };

    const session = await api.post('/practice/sessions', payload);
    if (!session || !session.questions || session.questions.length === 0) {
      showToast('No questions found for this configuration.', 'error');
      return;
    }

    currentSession = session;
    currentQuestionIndex = 0;
    sessionStorage.setItem('active_aptitude_session_id', session.id);

    showView('runnerView');
    loadCurrentQuestion();

    if (timeLimitSeconds) {
      startTimer(timeLimitSeconds);
    } else {
      stopTimer();
      document.getElementById('timerContainer').style.display = 'none';
    }
  } catch (err) {
    console.error('Failed to start session:', err);
    showToast(err.message || 'Could not start practice session.', 'error');
  }
}

async function resumeSession(sessionId) {
  try {
    const session = await api.get(`/practice/sessions/${sessionId}`);
    if (session && !session.is_completed) {
      currentSession = session;
      currentQuestionIndex = 0;
      showView('runnerView');
      loadCurrentQuestion();
      if (session.time_limit_seconds) {
        startTimer(session.time_limit_seconds);
      }
    } else {
      sessionStorage.removeItem('active_aptitude_session_id');
    }
  } catch {
    sessionStorage.removeItem('active_aptitude_session_id');
  }
}

function showView(viewId) {
  document.getElementById('setupView').style.display = viewId === 'setupView' ? 'block' : 'none';
  document.getElementById('runnerView').style.display = viewId === 'runnerView' ? 'block' : 'none';
  document.getElementById('summaryView').style.display = viewId === 'summaryView' ? 'block' : 'none';
}

function loadCurrentQuestion() {
  if (!currentSession || !currentSession.questions) return;
  const item = currentSession.questions[currentQuestionIndex];
  if (!item) {
    finishSession();
    return;
  }
  const q = item.question || item;

  selectedOptionKey = null;

  // Header badges
  document.getElementById('currentQuestionNum').textContent = currentQuestionIndex + 1;
  document.getElementById('totalQuestionsNum').textContent = currentSession.questions.length;
  document.getElementById('sessionModeLabel').textContent = `${(currentSession.session_mode || 'Practice').toUpperCase()} MODE`;
  document.getElementById('questionTopicBadge').textContent = q.topic_name || q.category || 'Aptitude';
  document.getElementById('questionDifficultyBadge').textContent = q.difficulty || 'Medium';

  // Question text
  document.getElementById('questionText').textContent = q.question_text;

  // Render 4 options
  const optionsGrid = document.getElementById('optionsGrid');
  optionsGrid.innerHTML = '';

  const options = q.options || [
    { option_key: 'A', option_text: q.option_a },
    { option_key: 'B', option_text: q.option_b },
    { option_key: 'C', option_text: q.option_c },
    { option_key: 'D', option_text: q.option_d },
  ].filter(o => o.option_text);

  options.forEach(opt => {
    const btn = document.createElement('button');
    btn.className = 'option-btn';
    btn.dataset.key = opt.option_key;
    btn.innerHTML = `
      <span class="option-key-badge">${opt.option_key}</span>
      <span style="flex:1;">${escapeHtml(opt.option_text)}</span>
    `;

    btn.addEventListener('click', () => {
      if (btn.disabled) return;
      document.querySelectorAll('.option-btn').forEach(b => b.classList.remove('selected'));
      btn.classList.add('selected');
      selectedOptionKey = opt.option_key;
      document.getElementById('submitAnswerBtn').disabled = false;
    });

    optionsGrid.appendChild(btn);
  });

  // Reset actions
  const submitBtn = document.getElementById('submitAnswerBtn');
  submitBtn.disabled = true;
  submitBtn.style.display = 'inline-flex';

  const nextBtn = document.getElementById('nextQuestionBtn');
  nextBtn.style.display = 'none';

  const feedbackBox = document.getElementById('feedbackBox');
  feedbackBox.style.display = 'none';

  const lockNotice = document.getElementById('lockNotice');
  lockNotice.style.display = 'none';
}

function bindRunnerEvents() {
  const submitBtn = document.getElementById('submitAnswerBtn');
  submitBtn.addEventListener('click', submitCurrentAnswer);

  const nextBtn = document.getElementById('nextQuestionBtn');
  nextBtn.addEventListener('click', () => {
    currentQuestionIndex++;
    if (currentQuestionIndex < currentSession.questions.length) {
      loadCurrentQuestion();
    } else {
      finishSession();
    }
  });

  const endBtn = document.getElementById('endSessionBtn');
  endBtn.addEventListener('click', () => {
    if (confirm('Are you sure you want to complete this assessment now?')) {
      finishSession();
    }
  });

  const returnBtn = document.getElementById('returnToModesBtn');
  returnBtn.addEventListener('click', () => {
    sessionStorage.removeItem('active_aptitude_session_id');
    showView('setupView');
  });

  const markBtn = document.getElementById('markReviewBtn');
  markBtn.addEventListener('click', async () => {
    if (!currentSession) return;
    try {
      await api.post(`/practice/sessions/${currentSession.id}/mark-review`, {
        question_index: currentQuestionIndex,
        is_marked: true
      });
      showToast('Question marked for review.', 'info');
    } catch (e) {
      console.warn(e);
    }
  });
}

async function submitCurrentAnswer() {
  if (!selectedOptionKey || !currentSession) return;
  const item = currentSession.questions[currentQuestionIndex];
  const q = item.question || item;
  const submitBtn = document.getElementById('submitAnswerBtn');
  setButtonLoading(submitBtn, true, 'Submitting...');

  try {
    const feedback = await api.post(`/practice/sessions/${currentSession.id}/answers`, {
      question_id: q.id,
      selected_option: selectedOptionKey
    });

    // 1. Lock all option buttons (Strict rule: No redo/retry in same session)
    document.querySelectorAll('.option-btn').forEach(btn => {
      btn.disabled = true;
      if (btn.dataset.key === feedback.correct_option) {
        btn.classList.add('correct');
      } else if (btn.dataset.key === selectedOptionKey && !feedback.is_correct) {
        btn.classList.add('incorrect');
      }
    });

    // 2. Hide submit, show Next Question button
    submitBtn.style.display = 'none';
    const nextBtn = document.getElementById('nextQuestionBtn');
    nextBtn.style.display = 'inline-flex';
    document.getElementById('lockNotice').style.display = 'inline-block';

    // 3. Render 14-Point Educational Feedback
    renderFeedback(feedback);

  } catch (err) {
    showToast(err.message || 'Failed to submit answer.', 'error');
    setButtonLoading(submitBtn, false);
  }
}

function renderFeedback(feedback) {
  const box = document.getElementById('feedbackBox');
  box.style.display = 'block';
  box.className = `feedback-box ${feedback.is_correct ? 'correct' : 'incorrect'}`;

  const statusBadge = document.getElementById('feedbackStatusBadge');
  if (feedback.is_correct) {
    statusBadge.className = 'badge badge-success';
    statusBadge.textContent = '✓ Correct Answer (+1 Mark)';
  } else {
    statusBadge.className = 'badge badge-danger';
    statusBadge.textContent = `✗ Incorrect (Correct Key: Option ${feedback.correct_option})`;
  }

  // Step-by-step reasoning
  document.getElementById('solutionText').textContent = feedback.explanation || 'Step-by-step solution available.';

  // Distractor analysis if provided
  const distractorContainer = document.getElementById('distractorAnalysisContainer');
  if (feedback.distractor_explanations) {
    distractorContainer.style.display = 'block';
    let dText = '';
    if (typeof feedback.distractor_explanations === 'object') {
      for (const [k, v] of Object.entries(feedback.distractor_explanations)) {
        dText += `Option ${k}: ${v}\n`;
      }
    } else {
      dText = feedback.distractor_explanations;
    }
    document.getElementById('distractorAnalysisText').textContent = dText;
  } else {
    distractorContainer.style.display = 'none';
  }

  // Common trap
  document.getElementById('trapText').textContent = feedback.common_mistake || 'Avoid misreading the unit conversions or inverse ratios.';

  // Pro tip
  document.getElementById('proTipText').textContent = feedback.pro_tip || 'Use elimination technique when two extreme options contradict.';

  box.scrollIntoView({ behavior: 'smooth' });
}

async function finishSession() {
  stopTimer();
  if (!currentSession) return;

  try {
    const summary = await api.post(`/practice/sessions/${currentSession.id}/complete`);
    sessionStorage.removeItem('active_aptitude_session_id');

    // Populate summary view
    document.getElementById('summaryScore').textContent = `${summary.score || summary.correct_answers || 0}/${summary.total_questions || currentSession.questions.length}`;
    document.getElementById('summaryAccuracy').textContent = `${summary.accuracy || 0}%`;
    document.getElementById('summaryTime').textContent = `${summary.time_spent_seconds || 60}s`;

    showView('summaryView');
  } catch (err) {
    console.error('Failed to complete session:', err);
    showView('setupView');
  }
}

function startTimer(seconds) {
  stopTimer();
  timeRemaining = seconds;
  const container = document.getElementById('timerContainer');
  const timerText = document.getElementById('countdownTimer');
  container.style.display = 'flex';

  function update() {
    const m = Math.floor(timeRemaining / 60);
    const s = timeRemaining % 60;
    timerText.textContent = `${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
    if (timeRemaining <= 0) {
      stopTimer();
      showToast('Time expired! Auto-submitting assessment...', 'info');
      finishSession();
    }
    timeRemaining--;
  }

  update();
  timerInterval = setInterval(update, 1000);
}

function stopTimer() {
  if (timerInterval) {
    clearInterval(timerInterval);
    timerInterval = null;
  }
}
