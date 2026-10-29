/**
 * InterviewAI — Resume Builder Controller
 */

document.addEventListener('DOMContentLoaded', async () => {
  const user = await auth.requireAuth();
  if (!user) return;

  loadResume();
  bindResumeEvents();
});

async function loadResume() {
  try {
    const res = await api.get('/resume/my-resume');
    if (!res) return;

    document.getElementById('resFullName').value = res.full_name || '';
    document.getElementById('resEmail').value = res.email || '';
    document.getElementById('resPhone').value = res.phone || '';
    document.getElementById('resLocation').value = res.location || '';
    document.getElementById('resTargetRole').value = res.target_role || '';
    document.getElementById('resSummary').value = res.summary || '';

    if (res.skills_json && Array.isArray(res.skills_json)) {
      document.getElementById('resSkills').value = res.skills_json.join(', ');
    }
    if (res.projects_json && Array.isArray(res.projects_json)) {
      document.getElementById('resProjects').value = res.projects_json.map(p => typeof p === 'string' ? p : (p.title + ': ' + p.description)).join('\n');
    }
    if (res.education_json && Array.isArray(res.education_json)) {
      document.getElementById('resEducation').value = res.education_json.map(e => typeof e === 'string' ? e : (e.degree + ' - ' + e.institution)).join('\n');
    }

    updatePreview();

  } catch (err) {
    console.warn('Could not load existing resume:', err);
  }
}

function bindResumeEvents() {
  ['resFullName', 'resEmail', 'resPhone', 'resLocation', 'resTargetRole', 'resSummary', 'resSkills', 'resProjects', 'resEducation'].forEach(id => {
    const el = document.getElementById(id);
    if (el) el.addEventListener('input', updatePreview);
  });

  const saveBtn = document.getElementById('saveResumeBtn');
  if (saveBtn) saveBtn.addEventListener('click', saveResume);

  const analyzeBtn = document.getElementById('analyzeResumeBtn');
  if (analyzeBtn) analyzeBtn.addEventListener('click', analyzeResume);
}

function updatePreview() {
  const name = document.getElementById('resFullName').value || 'YOUR NAME';
  const email = document.getElementById('resEmail').value || 'email@college.edu';
  const phone = document.getElementById('resPhone').value || '+91 9876543210';
  const loc = document.getElementById('resLocation').value || 'Bangalore, India';
  const summary = document.getElementById('resSummary').value || 'Professional summary...';
  const skills = document.getElementById('resSkills').value || 'Python, Java, React, SQL';
  const projects = document.getElementById('resProjects').value || 'Projects details...';
  const education = document.getElementById('resEducation').value || 'Education details...';

  document.getElementById('prevName').textContent = name.toUpperCase();
  document.getElementById('prevContact').textContent = `${email} | ${phone} | ${loc}`;
  document.getElementById('prevSummary').textContent = summary;
  document.getElementById('prevSkills').textContent = skills;
  document.getElementById('prevProjects').textContent = projects;
  document.getElementById('prevEducation').textContent = education;
}

async function saveResume() {
  const saveBtn = document.getElementById('saveResumeBtn');
  setButtonLoading(saveBtn, true, 'Saving...');

  const skillsArr = document.getElementById('resSkills').value.split(',').map(s => s.trim()).filter(Boolean);
  const projectsArr = document.getElementById('resProjects').value.split('\n').map(p => p.trim()).filter(Boolean);
  const educationArr = document.getElementById('resEducation').value.split('\n').map(e => e.trim()).filter(Boolean);

  const payload = {
    full_name: document.getElementById('resFullName').value.trim(),
    email: document.getElementById('resEmail').value.trim(),
    phone: document.getElementById('resPhone').value.trim(),
    location: document.getElementById('resLocation').value.trim(),
    target_role: document.getElementById('resTargetRole').value.trim(),
    summary: document.getElementById('resSummary').value.trim(),
    skills_json: skillsArr,
    projects_json: projectsArr,
    education_json: educationArr
  };

  try {
    await api.put('/resume/my-resume', payload);
    showToast('Resume saved successfully to database!', 'success');
  } catch (err) {
    showToast(err.message || 'Failed to save resume.', 'error');
  } finally {
    setButtonLoading(saveBtn, false);
  }
}

async function analyzeResume() {
  const analyzeBtn = document.getElementById('analyzeResumeBtn');
  setButtonLoading(analyzeBtn, true, 'Analyzing...');

  try {
    const feedback = await api.post('/resume/review');
    const card = document.getElementById('atsFeedbackCard');
    card.style.display = 'block';

    let content = '';
    if (typeof feedback === 'string') {
      content = feedback;
    } else if (feedback) {
      content = `<strong>Score:</strong> ${feedback.ats_score || 85}/100<br><br>
        <strong>Feedback:</strong> ${escapeHtml(feedback.summary || feedback.feedback || 'Strong technical skills matching campus hiring requirements.')}<br><br>
        <strong>Actionable Advice:</strong> Ensure project bullet points start with strong action verbs and highlight measurable results.`;
    }

    document.getElementById('atsFeedbackContent').innerHTML = content;
    card.scrollIntoView({ behavior: 'smooth' });
    showToast('ATS review completed!', 'success');

  } catch (err) {
    showToast(err.message || 'ATS analysis unavailable without provider keys.', 'info');
  } finally {
    setButtonLoading(analyzeBtn, false);
  }
}
