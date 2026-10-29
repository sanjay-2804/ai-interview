/**
 * InterviewAI — Student Dashboard Controller
 * Loads real-time statistics, weekly progress chart, and personalized diagnostics.
 */

document.addEventListener('DOMContentLoaded', async () => {
  const user = await auth.requireAuth();
  if (!user) return;

  // If user hasn't set up career, redirect to career setup
  const targetRole = user.target_role || user.profile?.target_role;
  if (!targetRole) {
    window.location.href = 'career-setup.html';
    return;
  }

  loadDashboardData(user);
});

async function loadDashboardData(user) {
  // Update header labels
  const userGreeting = document.getElementById('userGreeting');
  if (userGreeting) userGreeting.textContent = `Welcome back, ${user.name || user.full_name || 'Student'}!`;

  const careerRoleBadge = document.getElementById('careerRoleBadge');
  if (careerRoleBadge) careerRoleBadge.textContent = user.target_role || user.profile?.target_role || 'Software Developer';

  const skillLevelBadge = document.getElementById('skillLevelBadge');
  if (skillLevelBadge) skillLevelBadge.textContent = user.skill_level || user.profile?.skill_level || 'Intermediate';

  try {
    const stats = await api.get('/dashboard/stats');
    if (!stats) return;

    // Metric 1: Streak
    const streakDaysEl = document.getElementById('streakDays');
    if (streakDaysEl) streakDaysEl.textContent = stats.streak_days || 0;

    // Metric 2: Coding Solved
    const codingSolvedEl = document.getElementById('codingSolved');
    if (codingSolvedEl) codingSolvedEl.textContent = stats.coding_problems_solved || 0;

    // Metric 3: Aptitude Accuracy
    const aptitudeAccuracyEl = document.getElementById('aptitudeAccuracy');
    if (aptitudeAccuracyEl) aptitudeAccuracyEl.textContent = `${stats.accuracy || 0}%`;

    // Metric 4: Lessons Completed
    const lessonsCompletedEl = document.getElementById('lessonsCompleted');
    if (lessonsCompletedEl) lessonsCompletedEl.textContent = stats.lessons_completed || 0;

    // Render Weekly Activity Chart
    renderWeeklyChart(stats.weekly_activity);

    // Render Recent Activity
    renderRecentActivity(stats.recent_activity);

    // Render Weak Topics
    renderWeakTopics(stats.weak_topics);

  } catch (err) {
    console.error('Failed to load dashboard metrics:', err);
    showToast('Could not load recent metrics from backend.', 'error');
  }
}

function renderWeeklyChart(weeklyData) {
  const canvas = document.getElementById('weeklyActivityChart');
  if (!canvas) return;

  const labels = weeklyData ? weeklyData.map(d => d.day) : ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'];
  const values = weeklyData ? weeklyData.map(d => d.count || 0) : [0, 0, 0, 0, 0, 0, 0];

  new Chart(canvas, {
    type: 'bar',
    data: {
      labels: labels,
      datasets: [{
        label: 'Practice Activities Completed',
        data: values,
        backgroundColor: '#3b82f6',
        borderRadius: 6,
        hoverBackgroundColor: '#2563eb'
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { display: false },
        tooltip: {
          backgroundColor: '#0f172a',
          padding: 10,
          titleFont: { size: 12 },
          bodyFont: { size: 12 }
        }
      },
      scales: {
        y: {
          beginAtZero: true,
          ticks: { stepSize: 1, color: '#64748b' },
          grid: { color: '#f1f5f9' }
        },
        x: {
          ticks: { color: '#64748b' },
          grid: { display: false }
        }
      }
    }
  });
}

function renderRecentActivity(activities) {
  const container = document.getElementById('recentActivityList');
  if (!container) return;

  if (!activities || activities.length === 0) {
    container.innerHTML = `
      <div style="text-align:center; padding: 2rem 1rem; color:var(--color-text-subtle);">
        <i data-lucide="calendar" style="width:36px;height:36px;margin:0 auto 0.5rem;opacity:0.4;"></i>
        <p>No recent activity yet. Start your first practice session!</p>
      </div>
    `;
    if (window.lucide) lucide.createIcons();
    return;
  }

  let html = '<div style="display:flex; flex-direction:column; gap:0.75rem;">';
  activities.forEach(item => {
    let icon = 'check-circle';
    let iconBg = 'var(--color-primary-light)';
    let iconColor = 'var(--color-primary)';

    if (item.type?.includes('coding')) {
      icon = 'code';
      iconBg = '#fdf2f8';
      iconColor = '#db2777';
    } else if (item.type?.includes('communication')) {
      icon = 'mic';
      iconBg = '#f0fdf4';
      iconColor = '#16a34a';
    }

    html += `
      <div style="display:flex; align-items:center; justify-content:space-between; padding:0.75rem; border:1px solid var(--color-border); border-radius:var(--radius-md); background:#ffffff;">
        <div style="display:flex; align-items:center; gap:0.75rem;">
          <div style="width:36px;height:36px;border-radius:var(--radius-sm);background:${iconBg};color:${iconColor};display:flex;align-items:center;justify-content:center;flex-shrink:0;">
            <i data-lucide="${icon}" style="width:18px;height:18px;"></i>
          </div>
          <div>
            <div style="font-weight:600; font-size:0.875rem; color:var(--color-text-main);">${escapeHtml(item.title || 'Practice Event')}</div>
            <div style="font-size:0.75rem; color:var(--color-text-subtle);">${escapeHtml(item.details || '')}</div>
          </div>
        </div>
        <div style="font-size:0.75rem; color:var(--color-text-subtle); white-space:nowrap;">${escapeHtml(item.time || '')}</div>
      </div>
    `;
  });
  html += '</div>';

  container.innerHTML = html;
  if (window.lucide) lucide.createIcons();
}

function renderWeakTopics(topics) {
  const container = document.getElementById('weakTopicsList');
  if (!container) return;

  if (!topics || topics.length === 0) {
    container.innerHTML = `
      <div style="text-align:center; padding: 2rem 1rem; color:var(--color-text-subtle);">
        <i data-lucide="sparkles" style="width:36px;height:36px;margin:0 auto 0.5rem;opacity:0.4;"></i>
        <p>Attempt aptitude and coding assessments to generate personalized diagnostic recommendations.</p>
      </div>
    `;
    if (window.lucide) lucide.createIcons();
    return;
  }

  let html = '<div style="display:flex; flex-direction:column; gap:0.75rem;">';
  topics.forEach(t => {
    html += `
      <div style="display:flex; align-items:center; justify-content:space-between; padding:0.75rem; border:1px solid var(--color-border); border-radius:var(--radius-md); background:#ffffff;">
        <div>
          <div style="font-weight:600; font-size:0.875rem; color:var(--color-text-main);">${escapeHtml(t.topic || t.name)}</div>
          <div style="font-size:0.75rem; color:#ef4444; font-weight:500;">Accuracy: ${t.accuracy_percentage || 0}% (${t.correct_attempts || 0}/${t.total_attempts || 0})</div>
        </div>
        <a href="aptitude.html?mode=weak" class="btn btn-outline btn-sm" style="font-size:0.75rem;">Practice Topic</a>
      </div>
    `;
  });
  html += '</div>';

  container.innerHTML = html;
  if (window.lucide) lucide.createIcons();
}
