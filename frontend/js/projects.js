/**
 * InterviewAI — Projects Blueprint Controller
 */

document.addEventListener('DOMContentLoaded', async () => {
  const user = await auth.requireAuth();
  if (!user) return;

  loadProjects();
});

async function loadProjects() {
  const container = document.getElementById('projectsGrid');
  try {
    const data = await api.get('/projects');
    if (!data || data.length === 0) {
      container.innerHTML = `<div style="text-align:center;padding:2rem;color:var(--color-text-subtle);">No project blueprints found.</div>`;
      return;
    }

    let html = '';
    data.forEach(p => {
      let stackHtml = '';
      if (p.tech_stack && p.tech_stack.length > 0) {
        stackHtml = p.tech_stack.map(t => `<span class="badge badge-primary" style="font-size:0.75rem;">${escapeHtml(t)}</span>`).join(' ');
      }

      let milestonesHtml = '';
      if (p.milestones && p.milestones.length > 0) {
        milestonesHtml = p.milestones.map(m => `<li style="margin-bottom:0.25rem;">${escapeHtml(m)}</li>`).join('');
      }

      let questionsHtml = '';
      if (p.interview_questions && p.interview_questions.length > 0) {
        questionsHtml = p.interview_questions.map(q => `<li style="margin-bottom:0.25rem;color:var(--color-text-muted);">"${escapeHtml(q)}"</li>`).join('');
      }

      html += `
        <div class="card" style="display:flex; flex-direction:column; justify-content:space-between; padding:1.75rem;">
          <div>
            <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:0.75rem;">
              <span class="badge badge-accent">${escapeHtml(p.role || 'Full-Stack')}</span>
              <span class="badge ${p.difficulty === 'Advanced' ? 'badge-danger' : 'badge-warning'}">${p.difficulty}</span>
            </div>

            <h3 style="font-size:1.25rem; margin-bottom:0.5rem; color:var(--color-text-main);">${escapeHtml(p.title)}</h3>
            <p style="font-size:0.875rem; color:var(--color-text-muted); line-height:1.5; margin-bottom:1rem;">
              ${escapeHtml(p.problem_statement)}
            </p>

            <div style="display:flex; flex-wrap:wrap; gap:0.4rem; margin-bottom:1.25rem;">
              ${stackHtml}
            </div>

            <div style="margin-bottom:1rem; font-size:0.8125rem;">
              <strong>Key Milestones:</strong>
              <ul style="padding-left:1.2rem; margin-top:0.35rem; color:var(--color-text-muted);">
                ${milestonesHtml}
              </ul>
            </div>

            ${questionsHtml ? `
              <div style="margin-top:1rem; padding:0.75rem; background:var(--color-bg-page); border-radius:var(--radius-md); font-size:0.8125rem; border:1px solid var(--color-border);">
                <strong style="color:var(--color-primary);">Technical Interview Defense Questions:</strong>
                <ul style="padding-left:1.2rem; margin-top:0.35rem;">
                  ${questionsHtml}
                </ul>
              </div>
            ` : ''}
          </div>

          <div style="margin-top:1.5rem; border-top:1px solid var(--color-border); padding-top:1rem;">
            <a href="resume.html" class="btn btn-secondary btn-sm btn-full">
              <i data-lucide="plus" style="width:14px;height:14px;"></i> Add to My Resume
            </a>
          </div>
        </div>
      `;
    });

    container.innerHTML = html;
    if (window.lucide) lucide.createIcons();

  } catch (err) {
    console.error('Failed to load projects:', err);
    container.innerHTML = `<div style="text-align:center;padding:2rem;color:#ef4444;">Failed to load project blueprints.</div>`;
  }
}
