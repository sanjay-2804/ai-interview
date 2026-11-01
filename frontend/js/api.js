/**
 * InterviewAI — Centralized REST API Client
 * Connects frontend to the FastAPI backend with credentials & authorization headers.
 */

// Automatically use relative path '/api/v1' for production/Vercel or same-origin backend,
// fallback to 'http://127.0.0.1:8000/api/v1' only if opened via separate local dev server (e.g. Vite port 5173 / LiveServer port 5500)
const API_BASE_URL = (() => {
  if (typeof window === 'undefined') return '/api/v1';
  const isLocalDevPort = (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') &&
    (window.location.port && window.location.port !== '8000' && window.location.port !== '');
  if (isLocalDevPort) {
    return 'http://127.0.0.1:8000/api/v1';
  }
  return '/api/v1';
})();

const api = {
  baseUrl: API_BASE_URL,

  async request(endpoint, options = {}) {
    const url = endpoint.startsWith('http') ? endpoint : `${this.baseUrl}${endpoint.startsWith('/') ? '' : '/'}${endpoint}`;
    
    const headers = {
      'Accept': 'application/json',
      ...options.headers,
    };

    // If body is object and not FormData, stringify it
    let body = options.body;
    if (body && typeof body === 'object' && !(body instanceof FormData)) {
      headers['Content-Type'] = 'application/json';
      body = JSON.stringify(body);
    }

    // Attach Bearer token if present in localStorage / sessionStorage
    const token = localStorage.getItem('interviewai_token') || sessionStorage.getItem('interviewai_token');
    if (token && !headers['Authorization']) {
      headers['Authorization'] = `Bearer ${token}`;
    }

    const config = {
      ...options,
      headers,
      body,
      credentials: 'include', // sends and receives HttpOnly session cookies
    };

    try {
      const response = await fetch(url, config);

      if (response.status === 401 && !endpoint.includes('/auth/login') && !endpoint.includes('/auth/register')) {
        // Session expired or unauthenticated
        localStorage.removeItem('interviewai_token');
        sessionStorage.removeItem('interviewai_token');
        localStorage.removeItem('interviewai_user');
        
        const currentPath = window.location.pathname.toLowerCase();
        const isExemptPage = currentPath.endsWith('login.html') ||
          currentPath.endsWith('register.html') ||
          currentPath.endsWith('index.html') ||
          currentPath.endsWith('career-setup.html') ||
          currentPath.endsWith('help.html') ||
          currentPath === '/' ||
          currentPath === '';

        if (!isExemptPage) {
          window.location.href = 'login.html?expired=1';
        }
        throw new Error('Authentication required or session expired.');
      }

      if (response.status === 204) {
        return null;
      }

      const data = await response.json().catch(() => null);

      if (!response.ok) {
        const errorMsg = data?.detail || data?.message || `Request failed with status ${response.status}`;
        throw new Error(typeof errorMsg === 'string' ? errorMsg : JSON.stringify(errorMsg));
      }

      return data;
    } catch (err) {
      console.error(`[API Error] ${options.method || 'GET'} ${url}:`, err);
      throw err;
    }
  },

  get(endpoint, options = {}) {
    return this.request(endpoint, { ...options, method: 'GET' });
  },

  post(endpoint, data, options = {}) {
    return this.request(endpoint, { ...options, method: 'POST', body: data });
  },

  put(endpoint, data, options = {}) {
    return this.request(endpoint, { ...options, method: 'PUT', body: data });
  },

  patch(endpoint, data, options = {}) {
    return this.request(endpoint, { ...options, method: 'PATCH', body: data });
  },

  delete(endpoint, options = {}) {
    return this.request(endpoint, { ...options, method: 'DELETE' });
  }
};

/** Toast notification helper */
function showToast(message, type = 'info', duration = 4000) {
  let container = document.getElementById('toast-container');
  if (!container) {
    container = document.createElement('div');
    container.id = 'toast-container';
    container.className = 'toast-container';
    document.body.appendChild(container);
  }

  const toast = document.createElement('div');
  toast.className = `toast toast-${type}`;
  toast.innerHTML = `
    <span class="toast-message">${escapeHtml(message)}</span>
  `;
  container.appendChild(toast);

  setTimeout(() => {
    toast.style.opacity = '0';
    toast.style.transform = 'translateY(8px)';
    toast.style.transition = 'all 0.25s ease-out';
    setTimeout(() => toast.remove(), 250);
  }, duration);
}

/** Utility: Escape HTML string */
function escapeHtml(str) {
  if (str === null || str === undefined) return '';
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}

/** Set button loading state */
function setButtonLoading(btn, isLoading, loadingText = 'Processing...') {
  if (!btn) return;
  if (isLoading) {
    btn.dataset.originalHtml = btn.innerHTML;
    btn.disabled = true;
    btn.innerHTML = `<span style="display:inline-block;animation:spin 1s linear infinite;margin-right:0.5rem;">↻</span> ${loadingText}`;
  } else {
    btn.disabled = false;
    if (btn.dataset.originalHtml) {
      btn.innerHTML = btn.dataset.originalHtml;
    }
  }
}
