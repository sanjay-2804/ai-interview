/**
 * InterviewAI — Administrator Dashboard Controller
 * Enforces server-side administrator authorization and handles platform management.
 */

document.addEventListener('DOMContentLoaded', async () => {
  const admin = await auth.requireAdmin();
  if (!admin) return;

  loadAdminAnalytics();
  loadAdminUsers();
  bindAdminEvents();
});

async function loadAdminAnalytics() {
  try {
    const data = await api.get('/admin/analytics');
    if (!data) return;

    if (data.total_users !== undefined) document.getElementById('adminUsersCount').textContent = data.total_users;
    if (data.total_questions !== undefined) document.getElementById('adminQuestionsCount').textContent = data.total_questions;
    if (data.total_coding_problems !== undefined) document.getElementById('adminCodingCount').textContent = data.total_coding_problems;
    if (data.total_lessons !== undefined) document.getElementById('adminLessonsCount').textContent = data.total_lessons;

  } catch (err) {
    console.error('Failed to load admin analytics:', err);
  }
}

async function loadAdminUsers() {
  const tbody = document.getElementById('adminUsersTableBody');
  try {
    const users = await api.get('/admin/users');
    if (!users || users.length === 0) {
      tbody.innerHTML = `<tr><td colspan="6" style="padding:1.5rem;text-align:center;color:var(--color-text-subtle);">No registered users found.</td></tr>`;
      return;
    }

    let html = '';
    users.forEach(u => {
      html += `
        <tr style="border-bottom:1px solid var(--color-border);">
          <td style="padding:0.75rem; font-family:var(--font-mono);">${u.id}</td>
          <td style="padding:0.75rem; font-weight:600;">${escapeHtml(u.name || u.full_name || 'Student')}</td>
          <td style="padding:0.75rem; color:var(--color-text-muted);">${escapeHtml(u.email)}</td>
          <td style="padding:0.75rem;"><span class="badge ${u.role === 'admin' ? 'badge-danger' : 'badge-primary'}">${u.role}</span></td>
          <td style="padding:0.75rem; font-size:0.8125rem;">${escapeHtml(u.target_role || 'Not set')}</td>
          <td style="padding:0.75rem;"><span class="badge badge-success">Active</span></td>
        </tr>
      `;
    });

    tbody.innerHTML = html;

  } catch (err) {
    console.error('Failed to load admin users:', err);
    tbody.innerHTML = `<tr><td colspan="6" style="padding:1.5rem;text-align:center;color:#ef4444;">Failed to load user records.</td></tr>`;
  }
}

function bindAdminEvents() {
  const form = document.getElementById('createQuestionForm');
  const saveBtn = document.getElementById('saveQuestionBtn');

  if (form) {
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      setButtonLoading(saveBtn, true, 'Publishing...');

      const optA = document.getElementById('optA').value.trim();
      const optB = document.getElementById('optB').value.trim();
      const optC = document.getElementById('optC').value.trim();
      const optD = document.getElementById('optD').value.trim();
      const correctKey = document.getElementById('correctKey').value;

      const payload = {
        topic_id: 1, // Default topic
        question_type: "aptitude_mcq",
        difficulty: document.getElementById('qDifficulty').value.toLowerCase(),
        question_text: document.getElementById('qText').value.trim(),
        explanation: document.getElementById('qExplanation').value.trim(),
        step_by_step_reasoning: document.getElementById('qExplanation').value.trim(),
        practical_example: "Real campus assessment problem.",
        common_mistake: "Carefully inspect unit dimensions and timing.",
        learning_tip: "Eliminate extreme outliers first.",
        options: [
          { option_key: "A", option_text: optA, is_correct: correctKey === "A" },
          { option_key: "B", option_text: optB, is_correct: correctKey === "B" },
          { option_key: "C", option_text: optC, is_correct: correctKey === "C" },
          { option_key: "D", option_text: optD, is_correct: correctKey === "D" }
        ]
      };

      try {
        await api.post('/admin/questions', payload);
        showToast('Question published successfully to database!', 'success');
        form.reset();
        loadAdminAnalytics();
      } catch (err) {
        showToast(err.message || 'Failed to publish question.', 'error');
      } finally {
        setButtonLoading(saveBtn, false);
      }
    });
  }
}
