/**
 * InterviewAI — Technical Learning Controller
 * Renders technical tracks, markdown content, and lesson completion tracking.
 */

let allLessons = [];
let activeLesson = null;

document.addEventListener('DOMContentLoaded', async () => {
  const user = await auth.requireAuth();
  if (!user) return;

  loadLessons();
  bindLessonEvents();
});

async function loadLessons() {
  const container = document.getElementById('topicsContainer');
  try {
    const data = await api.get('/learning/lessons');
    allLessons = data || [];

    if (allLessons.length === 0) {
      container.innerHTML = `<div style="font-size:0.875rem; color:var(--color-text-subtle);">No technical lessons available.</div>`;
      return;
    }

    let html = '';
    allLessons.forEach(l => {
      html += `
        <div class="card lesson-item" data-id="${l.id}" style="padding:0.6rem 0.75rem; cursor:pointer;">
          <div style="font-weight:600; font-size:0.875rem; color:var(--color-text-main);">${escapeHtml(l.title)}</div>
          <div style="font-size:0.75rem; color:var(--color-text-subtle); display:flex; justify-content:space-between; margin-top:0.15rem;">
            <span>${escapeHtml(l.topic_name || 'Technical')}</span>
            <span>${l.estimated_minutes || 15}m</span>
          </div>
        </div>
      `;
    });
    container.innerHTML = html;

    container.querySelectorAll('.lesson-item').forEach(el => {
      el.addEventListener('click', () => {
        const id = parseInt(el.dataset.id, 10);
        selectLesson(id);
      });
    });

    // Automatically select first lesson
    if (allLessons.length > 0) {
      selectLesson(allLessons[0].id);
    }

  } catch (err) {
    console.error('Failed to load lessons:', err);
    if (container) {
      container.innerHTML = `<div style="font-size:0.875rem;color:#ef4444;">Failed to load technical lessons.</div>`;
    }
  }
}

async function selectLesson(id) {
  try {
    const lesson = await api.get(`/learning/lessons/${id}`);
    if (!lesson) return;

    activeLesson = lesson;

    document.getElementById('lessonTitle').textContent = lesson.title;
    document.getElementById('lessonTopicBadge').textContent = lesson.topic_name || 'Core CS';
    document.getElementById('lessonDuration').textContent = `${lesson.estimated_minutes || 15} mins`;
    document.getElementById('lessonDifficulty').textContent = lesson.difficulty || 'Medium';

    // Content
    const contentEl = document.getElementById('lessonContent');
    contentEl.innerHTML = formatMarkdown(lesson.content_markdown || 'No content available.');

    // Takeaways
    const takeawaysBox = document.getElementById('takeawaysBox');
    if (lesson.key_takeaways) {
      takeawaysBox.style.display = 'block';
      document.getElementById('takeawaysText').textContent = lesson.key_takeaways;
    } else {
      takeawaysBox.style.display = 'none';
    }

    // Completion button
    const completeBtn = document.getElementById('markCompleteBtn');
    if (lesson.is_completed) {
      completeBtn.className = 'btn btn-success btn-sm';
      completeBtn.innerHTML = `<i data-lucide="check-check" style="width:14px;height:14px;"></i> Completed`;
      completeBtn.disabled = true;
    } else {
      completeBtn.className = 'btn btn-outline btn-sm';
      completeBtn.innerHTML = `<i data-lucide="check" style="width:14px;height:14px;"></i> Mark Completed`;
      completeBtn.disabled = false;
    }

    if (window.lucide) lucide.createIcons();

  } catch (err) {
    console.error('Failed to select lesson:', err);
  }
}

function bindLessonEvents() {
  const completeBtn = document.getElementById('markCompleteBtn');
  completeBtn.addEventListener('click', async () => {
    if (!activeLesson) return;
    try {
      await api.put(`/learning/lessons/${activeLesson.id}/progress`);
      showToast('Lesson marked as completed! Activity recorded.', 'success');
      activeLesson.is_completed = true;
      completeBtn.className = 'btn btn-success btn-sm';
      completeBtn.innerHTML = `<i data-lucide="check-check" style="width:14px;height:14px;"></i> Completed`;
      completeBtn.disabled = true;
    } catch (err) {
      showToast(err.message || 'Failed to update progress.', 'error');
    }
  });
}

function formatMarkdown(md) {
  if (!md) return '';
  return md
    .replace(/^### (.*$)/gim, '<h4 style="font-size:1.05rem;margin:1rem 0 0.35rem;color:var(--color-text-main);">$1</h4>')
    .replace(/^## (.*$)/gim, '<h3 style="font-size:1.2rem;margin:1.25rem 0 0.5rem;color:var(--color-text-main);">$1</h3>')
    .replace(/^# (.*$)/gim, '<h2 style="font-size:1.35rem;margin:1.5rem 0 0.75rem;color:var(--color-text-main);">$1</h2>')
    .replace(/\*\*(.*)\*\*/gim, '<strong>$1</strong>')
    .replace(/\*(.*)\*/gim, '<em>$1</em>')
    .replace(/```([\s\S]*?)```/gim, '<pre style="background:#0f172a;color:#f8fafc;padding:1rem;border-radius:var(--radius-md);overflow-x:auto;margin:1rem 0;font-family:var(--font-mono);font-size:0.875rem;"><code>$1</code></pre>')
    .replace(/`([^`]+)`/gim, '<code style="background:var(--color-bg-subtle);padding:0.15rem 0.35rem;border-radius:4px;font-family:var(--font-mono);font-size:0.875rem;">$1</code>')
    .replace(/\n\n/gim, '<br><br>');
}
