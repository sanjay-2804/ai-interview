/**
 * InterviewAI — Student Profile Controller
 */

document.addEventListener('DOMContentLoaded', async () => {
  const user = await auth.requireAuth();
  if (!user) return;

  loadProfile(user);
  bindProfileEvents();
});

async function loadProfile(user) {
  document.getElementById('profName').value = user.name || user.full_name || '';
  document.getElementById('profEmail').value = user.email || '';

  try {
    const prof = await api.get('/profile');
    if (!prof) return;

    if (prof.college) document.getElementById('profCollege').value = prof.college;
    if (prof.course) document.getElementById('profCourse').value = prof.course;
    if (prof.target_role) document.getElementById('profTargetRole').value = prof.target_role;
    if (prof.preferred_programming_language) document.getElementById('profLang').value = prof.preferred_programming_language;
    if (prof.skill_level) document.getElementById('profSkill').value = prof.skill_level;

  } catch (err) {
    console.warn('Could not load extra profile attributes:', err);
  }
}

function bindProfileEvents() {
  const form = document.getElementById('profileForm');
  const saveBtn = document.getElementById('saveProfileBtn');

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    setButtonLoading(saveBtn, true, 'Saving...');

    const payload = {
      college: document.getElementById('profCollege').value.trim(),
      course: document.getElementById('profCourse').value.trim(),
      target_role: document.getElementById('profTargetRole').value,
      preferred_programming_language: document.getElementById('profLang').value,
      skill_level: document.getElementById('profSkill').value
    };

    try {
      await api.patch('/profile', payload);
      // Refresh current user session cache
      await auth.fetchCurrentUser();
      showToast('Profile and career preferences updated!', 'success');
    } catch (err) {
      showToast(err.message || 'Failed to update profile.', 'error');
    } finally {
      setButtonLoading(saveBtn, false);
    }
  });

  const logoutBtn = document.getElementById('profLogoutBtn');
  if (logoutBtn) {
    logoutBtn.addEventListener('click', () => auth.logout());
  }
}
