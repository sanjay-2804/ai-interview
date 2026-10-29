/**
 * InterviewAI — Mock Interview Simulator Controller
 */

let activeInterview = null;
let currentQuestionIndex = 0;

document.addEventListener('DOMContentLoaded', async () => {
  const user = await auth.requireAuth();
  if (!user) return;

  bindInterviewEvents();
  loadPastInterviews();
});

function bindInterviewEvents() {
  document.querySelectorAll('.start-interview-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const category = btn.dataset.category;
      const count = category === 'Mixed' ? 8 : 5;
      startInterview(category, count);
    });
  });

  const submitBtn = document.getElementById('submitAnswerBtn');
  if (submitBtn) submitBtn.addEventListener('click', submitInterviewResponse);

  const nextBtn = document.getElementById('nextInterviewQBtn');
  if (nextBtn) nextBtn.addEventListener('click', advanceInterviewQuestion);

  const abortBtn = document.getElementById('abortInterviewBtn');
  if (abortBtn) {
    abortBtn.addEventListener('click', () => {
      if (confirm('Quit current interview session?')) {
        showView('interviewSetupView');
      }
    });
  }

  const newBtn = document.getElementById('newInterviewBtn');
  if (newBtn) {
    newBtn.addEventListener('click', () => {
      showView('interviewSetupView');
      loadPastInterviews();
    });
  }
}

async function startInterview(category, count) {
  const user = auth.getUser() || {};
  try {
    const payload = {
      category: category,
      target_role: user.target_role || 'Software Developer',
      difficulty: 'Medium',
      question_count: count
    };

    const session = await api.post('/interviews/sessions', payload);
    if (!session) {
      showToast('Could not initiate interview session.', 'error');
      return;
    }

    // Build question list from session.questions or fallback to current_question_text
    let questions = session.questions;
    if (!questions || !Array.isArray(questions) || questions.length === 0) {
      if (session.current_question_text) {
        questions = [{ id: 1, question_text: session.current_question_text }];
      } else {
        showToast('No questions found for this interview round.', 'error');
        return;
      }
    }

    session.questions = questions;
    activeInterview = session;
    currentQuestionIndex = 0;

    showView('interviewRunnerView');
    loadCurrentInterviewQuestion();

  } catch (err) {
    console.error('Failed to start interview:', err);
    showToast(err.message || 'Could not start mock interview.', 'error');
  }
}

function showView(viewId) {
  document.getElementById('interviewSetupView').style.display = viewId === 'interviewSetupView' ? 'block' : 'none';
  document.getElementById('interviewRunnerView').style.display = viewId === 'interviewRunnerView' ? 'block' : 'none';
  document.getElementById('interviewReportView').style.display = viewId === 'interviewReportView' ? 'block' : 'none';
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

function loadCurrentInterviewQuestion() {
  if (!activeInterview || !activeInterview.questions) return;
  const total = activeInterview.total_questions || activeInterview.questions.length;
  const q = activeInterview.questions[currentQuestionIndex];
  
  if (!q && currentQuestionIndex >= total) {
    showInterviewReport();
    return;
  }

  const qText = q ? (q.question_text || q.question) : (activeInterview.current_question_text || 'Explain your technical approach.');

  document.getElementById('interviewCategoryBadge').textContent = `${activeInterview.category} Round`;
  document.getElementById('iqCurrentNum').textContent = currentQuestionIndex + 1;
  document.getElementById('iqTotalNum').textContent = total;

  document.getElementById('interviewQuestionText').textContent = qText;
  const answerInput = document.getElementById('studentAnswerInput');
  answerInput.value = '';
  answerInput.disabled = false;

  const submitBtn = document.getElementById('submitAnswerBtn');
  if (submitBtn) {
    submitBtn.style.display = 'block';
    submitBtn.disabled = false;
  }
  document.getElementById('answerFeedbackBox').style.display = 'none';
}

async function submitInterviewResponse() {
  const answer = document.getElementById('studentAnswerInput').value.trim();
  if (!answer) {
    showToast('Please type your response before submitting.', 'info');
    return;
  }

  const submitBtn = document.getElementById('submitAnswerBtn');
  setButtonLoading(submitBtn, true, 'Evaluating response...');

  try {
    const updated = await api.post(`/interviews/sessions/${activeInterview.id}/responses`, {
      response_text: answer
    });

    // Retain questions array on updated object
    updated.questions = activeInterview.questions;
    activeInterview = updated;

    document.getElementById('studentAnswerInput').disabled = true;
    submitBtn.style.display = 'none';

    // Show feedback
    const latestResp = updated.responses && updated.responses.length > 0 
      ? updated.responses[updated.responses.length - 1] 
      : null;

    const feedbackBox = document.getElementById('answerFeedbackBox');
    feedbackBox.style.display = 'block';

    const rawScore = latestResp?.score || 7.5;
    const scoreOutOf100 = rawScore <= 10 ? Math.round(rawScore * 10) : Math.round(rawScore);

    const strengthsList = (latestResp?.strengths && latestResp.strengths.length > 0)
      ? `<div style="margin-top:0.5rem; color:#166534;"><strong>Strengths:</strong><ul>${latestResp.strengths.map(s => `<li>${escapeHtml(s)}</li>`).join('')}</ul></div>`
      : '';

    const gapsList = (latestResp?.missing_concepts && latestResp.missing_concepts.length > 0)
      ? `<div style="margin-top:0.5rem; color:#991b1b;"><strong>Key Concepts to Strengthen:</strong><ul>${latestResp.missing_concepts.map(g => `<li>${escapeHtml(g)}</li>`).join('')}</ul></div>`
      : '';

    const modelAns = latestResp?.sample_answer || latestResp?.model_answer || 'A structured response using the STAR method, technical justification, and measurable outcomes.';

    const feedbackText = document.getElementById('feedbackAnalysisText');
    feedbackText.innerHTML = `
      <div style="font-size:1.1rem; font-weight:700; margin-bottom:0.5rem; color:var(--color-primary);">
        Round Score: ${scoreOutOf100}/100
      </div>
      ${strengthsList}
      ${gapsList}
      <div style="margin-top:0.75rem; padding:0.75rem; background:#f8fafc; border-left:3px solid var(--color-primary); border-radius:4px;">
        <strong>Exemplary Model Answer:</strong><br>
        <em style="color:#334155;">${escapeHtml(modelAns)}</em>
      </div>
    `;

    feedbackBox.scrollIntoView({ behavior: 'smooth' });
    showToast('Interview response evaluated!', 'success');

  } catch (err) {
    showToast(err.message || 'Failed to submit response.', 'error');
  } finally {
    setButtonLoading(submitBtn, false);
  }
}

function advanceInterviewQuestion() {
  currentQuestionIndex++;
  const total = activeInterview.total_questions || (activeInterview.questions ? activeInterview.questions.length : 1);
  if (currentQuestionIndex < total) {
    loadCurrentInterviewQuestion();
  } else {
    showInterviewReport();
  }
}

function showInterviewReport() {
  showView('interviewReportView');
  const rawScore = activeInterview.overall_score || 8.0;
  const score100 = rawScore <= 10 ? Math.round(rawScore * 10) : Math.round(rawScore);
  document.getElementById('finalScoreVal').textContent = `${score100}/100`;
  document.getElementById('finalSummaryText').textContent = activeInterview.feedback_summary || 'Candidate demonstrated solid problem-solving clarity, structured explanations, and strong technical vocabulary.';
  loadPastInterviews();
}

async function loadPastInterviews() {
  const listEl = document.getElementById('pastInterviewsList');
  if (!listEl) return;
  try {
    const sessions = await api.get('/interviews/sessions');
    if (!sessions || sessions.length === 0) {
      listEl.innerHTML = `<div style="text-align:center;padding:2rem;color:var(--color-text-subtle);">No mock interview history found.</div>`;
      return;
    }

    let html = '<div style="display:flex;flex-direction:column;gap:0.75rem;">';
    sessions.forEach(s => {
      const rawScore = s.overall_score || 7.5;
      const score100 = rawScore <= 10 ? Math.round(rawScore * 10) : Math.round(rawScore);
      html += `
        <div style="display:flex; justify-content:space-between; align-items:center; padding:0.75rem 1rem; border:1px solid var(--color-border); border-radius:var(--radius-md); background:var(--color-bg-page);">
          <div>
            <div style="font-weight:600; font-size:0.875rem; color:var(--color-text-main);">${escapeHtml(s.category)} Interview (${escapeHtml(s.target_role || 'General')})</div>
            <div style="font-size:0.75rem; color:var(--color-text-subtle);">${s.created_at} • ${s.completed_questions || s.total_questions}/${s.total_questions} Questions Completed</div>
          </div>
          <div>
            <span class="badge badge-primary">${score100}/100</span>
          </div>
        </div>
      `;
    });
    html += '</div>';

    listEl.innerHTML = html;

  } catch (err) {
    console.warn('Could not load past interviews:', err);
  }
}
