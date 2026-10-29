/**
 * InterviewAI — Career Roadmap Controller
 * Loads stages tailored to the student's target career role.
 */

document.addEventListener('DOMContentLoaded', async () => {
  const user = await auth.requireAuth();
  if (!user) return;

  loadRoadmap();
});

async function loadRoadmap() {
  const listEl = document.getElementById('stagesList');
  try {
    const data = await api.get('/roadmap');
    if (!data || !data.stages) {
      listEl.innerHTML = `<div style="text-align:center;padding:2rem;color:var(--color-text-subtle);">No roadmap generated. Please complete career setup.</div>`;
      return;
    }

    document.getElementById('roadmapRoleName').textContent = data.target_role || 'Software Developer';

    const stages = data.stages;
    const completedCount = stages.filter(s => s.status === 'completed').length;
    const pct = Math.round((completedCount / stages.length) * 100);

    document.getElementById('roadmapProgressPct').textContent = `${completedCount} of ${stages.length} Stages Completed (${pct}%)`;
    document.getElementById('roadmapProgressBar').style.width = `${pct}%`;

    let html = '';
    stages.forEach((s, idx) => {
      const isCompleted = s.status === 'completed';
      const isInProgress = s.status === 'in_progress';

      let statusBadge = `<span class="badge badge-neutral">Upcoming</span>`;
      let borderColor = 'var(--color-border)';

      if (isCompleted) {
        statusBadge = `<span class="badge badge-success">✓ Completed</span>`;
        borderColor = 'var(--color-success-border)';
      } else if (isInProgress) {
        statusBadge = `<span class="badge badge-primary">● In Progress</span>`;
        borderColor = 'var(--color-primary)';
      }

      let skillsHtml = '';
      if (s.skills && s.skills.length > 0) {
        skillsHtml = s.skills.map(skill => `<span class="badge badge-neutral" style="font-size:0.75rem;">${escapeHtml(skill)}</span>`).join(' ');
      }

      html += `
        <div class="card" style="border-left: 4px solid ${borderColor}; padding:1.5rem;">
          <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:0.75rem; flex-wrap:wrap; gap:0.5rem;">
            <div>
              <div style="font-size:0.75rem; font-weight:700; color:var(--color-primary); text-transform:uppercase;">
                Stage ${s.stage_number || idx + 1} • ~${s.estimated_hours || 12} Hours
              </div>
              <h3 style="font-size:1.2rem; margin-top:0.2rem;">${escapeHtml(s.title)}</h3>
            </div>
            <div>${statusBadge}</div>
          </div>

          <p style="font-size:0.9375rem; color:var(--color-text-muted); line-height:1.5; margin-bottom:1rem;">
            ${escapeHtml(s.description)}
          </p>

          <div style="display:flex; flex-wrap:wrap; gap:0.4rem; margin-bottom:1.25rem;">
            ${skillsHtml}
          </div>

          <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid var(--color-border); padding-top:0.75rem; font-size:0.8125rem;">
            <div style="color:var(--color-text-subtle);">
              Recommended Activity: <strong>${escapeHtml(s.recommended_practice || 'Practice Module')}</strong>
            </div>
            <div>
              <a href="aptitude.html" class="btn btn-secondary btn-sm" style="font-size:0.8125rem;">
                Practice Stage Skills
              </a>
            </div>
          </div>
        </div>
      `;
    });

    listEl.innerHTML = html;

  } catch (err) {
    console.error('Failed to load roadmap:', err);
    listEl.innerHTML = `<div style="text-align:center;padding:2rem;color:#ef4444;">Failed to load roadmap from server.</div>`;
  }
}
