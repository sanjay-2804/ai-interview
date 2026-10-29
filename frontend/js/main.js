/**
 * InterviewAI — Common UI Component Injector & Navigation Handler
 */

document.addEventListener('DOMContentLoaded', () => {
  initShell();
});

function initShell() {
  const sidebarEl = document.getElementById('sidebar');
  const topbarEl = document.getElementById('topbar');

  if (sidebarEl) {
    renderSidebar(sidebarEl);
  }

  if (topbarEl) {
    renderTopbar(topbarEl);
  }

  // Initialize Lucide icons if available
  if (window.lucide && typeof window.lucide.createIcons === 'function') {
    window.lucide.createIcons();
  }
}

function renderSidebar(container) {
  const currentFull = window.location.pathname.split('/').pop() + window.location.search;
  const currentPath = window.location.pathname.split('/').pop() || 'dashboard.html';
  const user = auth.getUser() || { name: 'Student', email: '', role: 'student' };
  const isAdmin = user.role === 'admin';

  const navItems = [
    { title: 'Overview & Goals', items: [
      { name: 'Dashboard', url: 'dashboard.html', icon: 'layout-dashboard' },
      { name: 'Home', url: 'index.html', icon: 'home' },
      { name: 'Career Assessment', url: 'career-setup.html', icon: 'crosshair' },
      { name: 'Career Roadmap', url: 'roadmap.html', icon: 'map' },
      { name: 'Daily Challenges', url: 'daily-challenges.html', icon: 'flame' },
    ]},
    { title: 'Aptitude & Tests', items: [
      { name: 'Aptitude Practice', url: 'aptitude.html', icon: 'brain-circuit' },
      { name: 'Logical Reasoning', url: 'aptitude.html?cat=Logical', icon: 'puzzle' },
      { name: 'Verbal Ability', url: 'aptitude.html?cat=Verbal', icon: 'spell-check' },
      { name: 'Timed Assessments', url: 'aptitude.html?mode=timed', icon: 'timer' },
      { name: 'Technical MCQs', url: 'aptitude.html?cat=Technical', icon: 'help-circle' },
      { name: 'Revision Centre', url: 'revision.html', icon: 'history' },
      { name: 'Bookmarks', url: 'bookmarks.html', icon: 'bookmark' },
    ]},
    { title: 'Coding & DSA', items: [
      { name: 'Coding Practice', url: 'coding.html', icon: 'code-2' },
      { name: 'DSA Learning Path', url: 'dsa.html', icon: 'binary' },
      { name: 'Programming Languages', url: 'languages.html', icon: 'terminal' },
    ]},
    { title: 'Core CS & Architecture', items: [
      { name: 'Core CS Subjects', url: 'learning.html', icon: 'book-open' },
      { name: 'System Design', url: 'system-design.html', icon: 'network' },
      { name: 'Projects & Portfolio', url: 'projects.html', icon: 'folder-git-2' },
    ]},
    { title: 'Company Drives', items: [
      { name: 'Company Preparation', url: 'company-interviews.html', icon: 'building-2' },
      { name: 'Company Questions', url: 'company-questions.html', icon: 'file-question' },
      { name: 'Previous Placement Papers', url: 'placement-papers.html', icon: 'archive' },
      { name: 'Interview Experiences', url: 'experiences.html', icon: 'users' },
    ]},
    { title: 'Interview & Soft Skills', items: [
      { name: 'Mock Interviews', url: 'interviews.html', icon: 'message-square-quote' },
      { name: 'HR Interview Prep', url: 'hr-prep.html', icon: 'smile' },
      { name: 'English Communication', url: 'communication.html', icon: 'mic' },
      { name: 'Group Discussion', url: 'group-discussion.html', icon: 'messages-square' },
      { name: 'Resume Builder', url: 'resume.html', icon: 'file-text' },
      { name: 'Resume-Based Questions', url: 'resume-questions.html', icon: 'file-check' },
    ]},
    { title: 'Progress & Support', items: [
      { name: 'Learning Progress', url: 'progress.html', icon: 'line-chart' },
      { name: 'Achievements', url: 'achievements.html', icon: 'award' },
      { name: 'Notifications', url: 'notifications.html', icon: 'bell' },
      { name: 'Profile & Settings', url: 'profile.html', icon: 'user' },
      { name: 'Help & Feedback', url: 'help.html', icon: 'life-buoy' },
    ]}
  ];

  if (isAdmin) {
    navItems.push({
      title: 'Administration',
      items: [
        { name: 'Admin Dashboard', url: 'admin.html', icon: 'shield-alert' }
      ]
    });
  }

  let html = `
    <div class="sidebar-header">
      <a href="dashboard.html" class="brand-logo">
        <div class="brand-icon">AI</div>
        <span>InterviewAI</span>
      </a>
    </div>
    <div class="sidebar-nav">
  `;

  navItems.forEach(group => {
    html += `<div class="nav-group-title">${group.title}</div>`;
    group.items.forEach(item => {
      const isActive = (item.url.includes('?') && currentFull === item.url) || (!item.url.includes('?') && currentPath === item.url);
      html += `
        <a href="${item.url}" class="sidebar-link ${isActive ? 'active' : ''}">
          <i data-lucide="${item.icon}"></i>
          <span>${item.name}</span>
        </a>
      `;
    });
  });

  html += `
    </div>
    <div class="sidebar-footer">
      <div class="user-profile-pill">
        <div class="user-avatar">${(user.name || 'S').charAt(0).toUpperCase()}</div>
        <div class="user-details" style="flex:1;">
          <div class="user-name">${escapeHtml(user.name || 'Student')}</div>
          <div class="user-role-badge">${user.role === 'admin' ? 'Administrator' : 'Student'}</div>
        </div>
        <button id="logoutBtn" title="Sign Out" style="background:none;border:none;color:var(--color-text-subtle);cursor:pointer;padding:4px;">
          <i data-lucide="log-out" style="width:16px;height:16px;"></i>
        </button>
      </div>
    </div>
  `;

  container.className = 'app-sidebar';
  container.innerHTML = html;

  // Bind logout button
  const logoutBtn = container.querySelector('#logoutBtn');
  if (logoutBtn) {
    logoutBtn.addEventListener('click', () => auth.logout());
  }
}

function renderTopbar(container) {
  const user = auth.getUser() || { name: 'Student' };

  container.className = 'app-topbar';
  container.innerHTML = `
    <div style="display:flex;align-items:center;gap:1rem;">
      <button class="mobile-menu-btn btn btn-secondary btn-sm" id="sidebarToggle" style="padding:0.4rem 0.6rem;">
        <i data-lucide="menu" style="width:18px;height:18px;"></i>
      </button>
      <div style="font-size:0.875rem;color:var(--color-text-subtle);">
        Welcome back, <strong style="color:var(--color-text-main);">${escapeHtml(user.name || 'Student')}</strong>
      </div>
    </div>

    <div style="display:flex;align-items:center;gap:0.75rem;">
      <span class="badge badge-success" style="font-size:0.75rem;padding:0.25rem 0.5rem;">
        <i data-lucide="check-circle" style="width:12px;height:12px;display:inline-block;"></i> API Connected
      </span>
      <a href="profile.html" class="btn btn-secondary btn-sm" style="font-size:0.8125rem;">
        <i data-lucide="settings" style="width:14px;height:14px;"></i> Settings
      </a>
    </div>
  `;

  const toggle = container.querySelector('#sidebarToggle');
  if (toggle) {
    toggle.addEventListener('click', () => {
      const sidebar = document.getElementById('sidebar');
      if (sidebar) {
        sidebar.classList.toggle('open');
      }
    });
  }
}
