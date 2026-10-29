/**
 * InterviewAI — Progress & Diagnostic Controller
 */

document.addEventListener('DOMContentLoaded', async () => {
  const user = await auth.requireAuth();
  if (!user) return;

  loadProgress();
  bindProgressEvents();
});

async function loadProgress() {
  try {
    const stats = await api.get('/progress/summary');
    if (!stats) return;

    document.getElementById('totalAttemptsVal').textContent = stats.questions_attempted || 0;
    document.getElementById('accuracyVal').textContent = `${stats.accuracy || 0}%`;
    document.getElementById('codingVal').textContent = stats.coding_problems_solved || 0;

    const topicData = await api.get('/progress/topics').catch(() => []);
    renderTopicTable(topicData);

  } catch (err) {
    console.error('Failed to load progress summary:', err);
  }
}

function renderTopicTable(topics) {
  const tbody = document.getElementById('topicBreakdownBody');
  if (!tbody) return;

  if (!topics || topics.length === 0) {
    tbody.innerHTML = `
      <tr>
        <td colspan="5" style="padding:2rem; text-align:center; color:var(--color-text-subtle);">
          No topic attempts recorded yet. Attempt questions in the Aptitude Centre to view diagnostics.
        </td>
      </tr>
    `;
    return;
  }

  let html = '';
  topics.forEach(t => {
    const pct = t.accuracy_percentage || 0;
    let badgeClass = 'badge-success';
    let rec = 'Maintain speed';

    if (pct < 50) {
      badgeClass = 'badge-danger';
      rec = 'High priority review needed';
    } else if (pct < 75) {
      badgeClass = 'badge-warning';
      rec = 'Practice shortcut formulas';
    }

    html += `
      <tr style="border-bottom:1px solid var(--color-border);">
        <td style="padding:0.75rem; font-weight:600;">${escapeHtml(t.topic || t.name)} <span style="font-size:0.75rem; color:var(--color-text-subtle); font-weight:normal;">(${escapeHtml(t.category || '')})</span></td>
        <td style="padding:0.75rem;">${t.total_attempts || 0}</td>
        <td style="padding:0.75rem;">${t.correct_attempts || 0}</td>
        <td style="padding:0.75rem;"><span class="badge ${badgeClass}">${pct}%</span></td>
        <td style="padding:0.75rem; font-size:0.8125rem; color:var(--color-text-muted);">${rec}</td>
      </tr>
    `;
  });

  tbody.innerHTML = html;
}

function bindProgressEvents() {
  const exportBtn = document.getElementById('exportDataBtn');
  if (exportBtn) {
    exportBtn.addEventListener('click', async () => {
      try {
        const stats = await api.get('/progress/summary');
        const jsonStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(stats, null, 2));
        const downloadAnchor = document.createElement('a');
        downloadAnchor.setAttribute("href", jsonStr);
        downloadAnchor.setAttribute("download", `InterviewAI_Report_${Date.now()}.json`);
        document.body.appendChild(downloadAnchor);
        downloadAnchor.click();
        downloadAnchor.remove();
        showToast('Diagnostic report exported successfully!', 'success');
      } catch (err) {
        showToast('Export failed.', 'error');
      }
    });
  }

  const deleteBtn = document.getElementById('deleteAccountBtn');
  if (deleteBtn) {
    deleteBtn.addEventListener('click', () => {
      const confirmEmail = prompt("To permanently delete your student account and all practice records, please type your email to confirm:");
      const user = auth.getUser();
      if (confirmEmail && user && confirmEmail.trim().toLowerCase() === user.email.toLowerCase()) {
        showToast("Account deletion requested. Logging out...", "info");
        setTimeout(() => auth.logout(), 1000);
      } else if (confirmEmail) {
        alert("Email verification mismatch. Account deletion cancelled.");
      }
    });
  }
}
