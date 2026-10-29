/**
 * InterviewAI — Authentication & Session Manager
 */

const auth = {
  getUser() {
    const raw = localStorage.getItem('interviewai_user') || sessionStorage.getItem('interviewai_user');
    try {
      return raw ? JSON.parse(raw) : null;
    } catch {
      return null;
    }
  },

  setUser(user, rememberMe = true) {
    const serialized = JSON.stringify(user);
    if (rememberMe) {
      localStorage.setItem('interviewai_user', serialized);
    } else {
      sessionStorage.setItem('interviewai_user', serialized);
    }
  },

  getToken() {
    return localStorage.getItem('interviewai_token') || sessionStorage.getItem('interviewai_token');
  },

  setToken(token, rememberMe = true) {
    if (rememberMe) {
      localStorage.setItem('interviewai_token', token);
    } else {
      sessionStorage.setItem('interviewai_token', token);
    }
  },

  clear() {
    localStorage.removeItem('interviewai_token');
    localStorage.removeItem('interviewai_user');
    sessionStorage.removeItem('interviewai_token');
    sessionStorage.removeItem('interviewai_user');
  },

  async fetchCurrentUser() {
    try {
      const user = await api.get('/auth/me');
      if (user) {
        this.setUser(user);
        return user;
      }
    } catch (err) {
      console.warn('Could not refresh current user session:', err);
      if (err.message && (err.message.includes('401') || err.message.includes('Authentication') || err.message.includes('expired'))) {
        this.clear();
        return null;
      }
      return this.getUser();
    }
    return null;
  },

  async login(email, password, rememberMe = false) {
    const res = await api.post('/auth/login', {
      email,
      password,
      remember_me: rememberMe
    });

    if (res && res.access_token) {
      this.setToken(res.access_token, rememberMe);
      if (res.user) {
        this.setUser(res.user, rememberMe);
      }
      return res;
    }
    throw new Error('Invalid login response from server.');
  },

  async register(name, email, password, confirmPassword, consent = true) {
    if (!consent) {
      throw new Error('You must agree to the Terms of Service & Privacy Policy.');
    }
    if (password !== confirmPassword) {
      throw new Error('Passwords do not match.');
    }

    const res = await api.post('/auth/register', {
      name,
      email,
      password,
      confirm_password: confirmPassword,
      terms_accepted: consent
    });

    if (res && res.access_token) {
      this.setToken(res.access_token, true);
      if (res.user) {
        this.setUser(res.user, true);
      }
      return res;
    }
    throw new Error('Registration failed. Please try again.');
  },

  async logout() {
    try {
      await api.post('/auth/logout', {});
    } catch (err) {
      console.warn('Backend logout call finished or cookies cleared:', err);
    } finally {
      this.clear();
      window.location.href = 'login.html';
    }
  },

  async requireAuth() {
    let user = this.getUser();
    if (!user && !this.getToken()) {
      window.location.href = 'login.html';
      return null;
    }
    
    // Validate with backend
    try {
      const freshUser = await this.fetchCurrentUser();
      if (!freshUser) {
        window.location.href = 'login.html';
        return null;
      }
      return freshUser;
    } catch {
      window.location.href = 'login.html';
      return null;
    }
  },

  async requireAdmin() {
    const user = await this.requireAuth();
    if (!user) return null;
    if (user.role !== 'admin') {
      alert('Access restricted: Administrator privileges required.');
      window.location.href = 'dashboard.html';
      return null;
    }
    return user;
  },

  redirectIfAuthenticated() {
    const user = this.getUser();
    const token = this.getToken();
    if (user || token) {
      window.location.href = 'dashboard.html';
    }
  }
};
