/**
 * InterviewAI — Personalized AI Placement Tutor Controller
 * Connects frontend chat to /api/v1/tutor endpoints and displays live student diagnostics.
 */

document.addEventListener('DOMContentLoaded', async () => {
  if (window.lucide) lucide.createIcons();

  const user = await auth.requireAuth();
  if (!user) return;

  loadDiagnosticContext();
  bindTutorEvents();
});

async function loadDiagnosticContext() {
  try {
    const diag = await api.get('/tutor/diagnostic-context');
    if (!diag) return;

    document.getElementById('diagTargetRole').textContent = diag.target_role || 'Software Developer';
    document.getElementById('diagSkillLang').textContent = `${diag.skill_level} (${diag.primary_language})`;
    document.getElementById('diagAccuracy').textContent = `${diag.mcq_accuracy_percentage}% (${diag.mcq_questions_attempted} Qs)`;
    document.getElementById('diagWeakArea').textContent = diag.primary_weak_topic || 'Dynamic Programming';
    document.getElementById('diagCodingComm').textContent = `${diag.coding_problems_solved} Solved • ${diag.communication_average_score}/10`;
    document.getElementById('diagRecommendation').textContent = diag.recommended_next_step;

  } catch (err) {
    console.warn('Could not load diagnostic context:', err);
  }
}

function bindTutorEvents() {
  const form = document.getElementById('tutorChatForm');
  const input = document.getElementById('tutorInput');

  if (form) {
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const message = input.value.trim();
      if (!message) return;

      appendUserMessage(message);
      input.value = '';
      await sendTutorMessage(message);
    });
  }

  // Quick prompt buttons
  document.querySelectorAll('.quick-prompt-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const promptText = btn.textContent.replace(/^[^\w]+/, '').trim();
      input.value = promptText;
      form.dispatchEvent(new Event('submit'));
    });
  });
}

function appendUserMessage(text) {
  const container = document.getElementById('tutorMessagesContainer');
  const msgEl = document.createElement('div');
  msgEl.style.cssText = 'display:flex; justify-content:flex-end; gap:0.75rem;';
  msgEl.innerHTML = `
    <div style="background:var(--color-primary); color:#ffffff; padding:0.875rem 1.25rem; border-radius:var(--radius-md); max-width:80%; font-size:0.9375rem; line-height:1.5; box-shadow:var(--shadow-sm);">
      ${escapeHtml(text)}
    </div>
  `;
  container.appendChild(msgEl);
  container.scrollTop = container.scrollHeight;
}

async function sendTutorMessage(message) {
  const container = document.getElementById('tutorMessagesContainer');
  const sendBtn = document.getElementById('tutorSendBtn');
  setButtonLoading(sendBtn, true, 'Thinking...');

  // Temporary typing bubble
  const typingEl = document.createElement('div');
  typingEl.id = 'typingBubble';
  typingEl.style.cssText = 'display:flex; gap:0.75rem; max-width:85%;';
  typingEl.innerHTML = `
    <div style="width:36px; height:36px; border-radius:var(--radius-full); background:var(--color-primary); color:#ffffff; display:flex; align-items:center; justify-content:center; flex-shrink:0;">
      <i data-lucide="bot" style="width:18px;height:18px;"></i>
    </div>
    <div style="background:#ffffff; border:1px solid var(--color-border); padding:0.75rem 1.25rem; border-radius:var(--radius-md); font-size:0.875rem; color:var(--color-text-muted);">
      Tutor is formulating pedagogical explanation...
    </div>
  `;
  container.appendChild(typingEl);
  if (window.lucide) lucide.createIcons();
  container.scrollTop = container.scrollHeight;

  try {
    const res = await api.post('/tutor/chat', { message });
    typingEl.remove();

    // Render tutor response
    const replyEl = document.createElement('div');
    replyEl.style.cssText = 'display:flex; gap:0.75rem; max-width:85%;';
    replyEl.innerHTML = `
      <div style="width:36px; height:36px; border-radius:var(--radius-full); background:var(--color-primary); color:#ffffff; display:flex; align-items:center; justify-content:center; flex-shrink:0;">
        <i data-lucide="bot" style="width:18px;height:18px;"></i>
      </div>
      <div style="background:#ffffff; border:1px solid var(--color-border); padding:1rem 1.25rem; border-radius:var(--radius-md); box-shadow:var(--shadow-sm); font-size:0.9375rem; line-height:1.6;">
        <div style="margin-bottom:0.75rem;">${formatMarkdown(res.reply)}</div>
        
        <div style="margin-top:0.75rem; padding:0.6rem 0.85rem; background:#eff6ff; border:1px solid #bfdbfe; border-radius:var(--radius-sm); font-size:0.8125rem; color:#1e40af;">
          <strong>💡 Concept Focus:</strong> ${escapeHtml(res.concept_summary)}
        </div>

        <div style="margin-top:0.5rem; font-size:0.8125rem; color:var(--color-text-muted);">
          <em>${escapeHtml(res.follow_up_prompt)}</em>
        </div>
      </div>
    `;
    container.appendChild(replyEl);
    if (window.lucide) lucide.createIcons();
    container.scrollTop = container.scrollHeight;

  } catch (err) {
    typingEl.remove();
    showToast(err.message || 'Tutor response unavailable.', 'error');
  } finally {
    setButtonLoading(sendBtn, false);
  }
}

function formatMarkdown(text) {
  if (!text) return '';
  return text
    .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
    .replace(/\*(.*?)\*/g, '<em>$1</em>')
    .replace(/`([^`]+)`/g, '<code style="background:#f1f5f9;padding:0.15rem 0.35rem;border-radius:4px;font-size:0.875rem;">$1</code>')
    .replace(/\n\n/g, '<br><br>')
    .replace(/\n/g, '<br>');
}

