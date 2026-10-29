import {
  AuthResponse, User, UserProfile, DashboardStats, PracticeSessionDetail,
  AnswerFeedback, CodingProblemListOut, CodingProblemDetail, CodeRunResult,
  MockInterviewDetail, ResumeData, Bookmark, TopicItem, LessonDetail, ProjectBlueprint
} from '../types';

const API_BASE = '/api';

class ApiService {
  private getToken(): string | null {
    return localStorage.getItem('interviewai_token');
  }

  private getHeaders(customHeaders: Record<string, string> = {}): HeadersInit {
    const headers: Record<string, string> = {
      'Content-Type': 'application/json',
      ...customHeaders,
    };
    const token = this.getToken();
    if (token) {
      headers['Authorization'] = `Bearer ${token}`;
    }
    return headers;
  }

  private async request<T>(endpoint: string, options: RequestInit = {}): Promise<T> {
    const url = `${API_BASE}${endpoint}`;
    const headers = this.getHeaders((options.headers as Record<string, string>) || {});

    const response = await fetch(url, {
      ...options,
      credentials: 'include',
      headers,
    });

    if (response.status === 401) {
      localStorage.removeItem('interviewai_token');
      localStorage.removeItem('interviewai_user');
      if (window.location.pathname.startsWith('/app') || window.location.pathname.startsWith('/admin')) {
        window.location.href = '/login';
      }
    }

    if (!response.ok) {
      let errorMsg = 'An unexpected error occurred.';
      try {
        const errorData = await response.json();
        errorMsg = errorData.detail || errorData.message || errorMsg;
      } catch {
        // Fallback to status text
        errorMsg = response.statusText || errorMsg;
      }
      throw new Error(errorMsg);
    }

    return response.json();
  }

  // --- Auth ---
  async login(payload: { email: string; password: string; remember_me?: boolean }): Promise<AuthResponse> {
    return this.request<AuthResponse>('/auth/login', {
      method: 'POST',
      body: JSON.stringify(payload),
    });
  }

  async register(payload: { full_name?: string; name?: string; email: string; password: string; target_role?: string }): Promise<AuthResponse> {
    return this.request<AuthResponse>('/auth/register', {
      method: 'POST',
      body: JSON.stringify(payload),
    });
  }

  async logout(): Promise<{ message: string }> {
    try {
      return await this.request<{ message: string }>('/auth/logout', { method: 'POST' });
    } catch {
      return { message: 'Logged out.' };
    }
  }

  async forgotPassword(email: string): Promise<{ message: string; reset_token?: string }> {
    return this.request<{ message: string; reset_token?: string }>('/auth/forgot-password', {
      method: 'POST',
      body: JSON.stringify({ email }),
    });
  }

  async resetPassword(payload: { token: string; new_password: string }): Promise<{ message: string }> {
    return this.request<{ message: string }>('/auth/reset-password', {
      method: 'POST',
      body: JSON.stringify(payload),
    });
  }

  async getMe(): Promise<User> {
    return this.request<User>('/auth/me');
  }

  async getProfile(): Promise<UserProfile> {
    return this.request<UserProfile>('/profile/');
  }

  async updateProfile(payload: Partial<UserProfile>): Promise<UserProfile> {
    return this.request<UserProfile>('/profile/', {
      method: 'PATCH',
      body: JSON.stringify(payload),
    });
  }

  async updateOnboarding(payload: Partial<UserProfile>): Promise<UserProfile> {
    return this.request<UserProfile>('/onboarding/', {
      method: 'POST',
      body: JSON.stringify(payload),
    });
  }

  // --- Dashboard ---
  async getDashboardStats(): Promise<DashboardStats> {
    return this.request<DashboardStats>('/dashboard/stats');
  }

  // --- Practice & Learn From Every Answer ---
  async startPracticeSession(payload: {
    category: string;
    subcategory?: string;
    difficulty?: string;
    question_count?: number;
    session_mode?: string;
    time_limit_seconds?: number;
  }): Promise<PracticeSessionDetail> {
    return this.request<PracticeSessionDetail>('/practice/session', {
      method: 'POST',
      body: JSON.stringify(payload),
    });
  }

  async getPracticeSession(sessionId: number): Promise<PracticeSessionDetail> {
    return this.request<PracticeSessionDetail>(`/practice/session/${sessionId}`);
  }

  async submitPracticeAnswer(payload: {
    session_id?: number;
    question_id: number;
    selected_option: string;
  }): Promise<AnswerFeedback> {
    return this.request<AnswerFeedback>('/practice/submit', {
      method: 'POST',
      body: JSON.stringify(payload),
    });
  }

  async markQuestionForReview(sessionId: number, questionIndex: number, isMarked: boolean): Promise<any> {
    return this.request<any>(`/practice/sessions/${sessionId}/mark-review`, {
      method: 'POST',
      body: JSON.stringify({ question_index: questionIndex, is_marked: isMarked }),
    });
  }

  async completePracticeSession(sessionId: number): Promise<PracticeSessionDetail> {
    return this.request<PracticeSessionDetail>(`/practice/sessions/${sessionId}/complete`, {
      method: 'POST',
    });
  }

  // --- Communication Lab ---
  async getCommunicationPrompts(): Promise<any[]> {
    return this.request<any[]>('/communication/prompts');
  }

  async submitCommunicationAttempt(payload: {
    category: string;
    prompt_title: string;
    prompt_question: string;
    framework?: string;
    transcript: string;
    audio_duration_seconds?: number;
    audio_filename?: string;
  }): Promise<any> {
    return this.request<any>('/communication/submit', {
      method: 'POST',
      body: JSON.stringify(payload),
    });
  }

  async getCommunicationHistory(): Promise<any[]> {
    return this.request<any[]>('/communication/history');
  }

  async getCommunicationSession(id: number): Promise<any> {
    return this.request<any>(`/communication/session/${id}`);
  }

  // --- Coding Practice ---
  async getCodingProblems(difficulty?: string, category?: string): Promise<CodingProblemListOut[]> {
    const params = new URLSearchParams();
    if (difficulty) params.append('difficulty', difficulty);
    if (category) params.append('category', category);
    return this.request<CodingProblemListOut[]>(`/coding/problems?${params.toString()}`);
  }

  async getCodingProblemDetail(id: number): Promise<CodingProblemDetail> {
    return this.request<CodingProblemDetail>(`/coding/problems/${id}`);
  }

  async runCode(payload: { problem_id: number; language: string; code: string }): Promise<CodeRunResult> {
    return this.request<CodeRunResult>('/coding/run', {
      method: 'POST',
      body: JSON.stringify(payload),
    });
  }

  async getCodingSubmissions(problemId: number): Promise<any[]> {
    return this.request<any[]>(`/coding/problems/${problemId}/submissions`);
  }

  // --- Mock Interview ---
  async startMockInterview(payload: {
    category: string;
    target_role: string;
    difficulty: string;
    question_count: number;
  }): Promise<MockInterviewDetail> {
    return this.request<MockInterviewDetail>('/interview/start', {
      method: 'POST',
      body: JSON.stringify(payload),
    });
  }

  async getMockInterview(id: number): Promise<MockInterviewDetail> {
    return this.request<MockInterviewDetail>(`/interview/${id}`);
  }

  async submitMockInterviewResponse(payload: {
    session_id: number;
    response_text: string;
  }): Promise<MockInterviewDetail> {
    return this.request<MockInterviewDetail>('/interview/submit-response', {
      method: 'POST',
      body: JSON.stringify(payload),
    });
  }

  async getInterviewHistory(): Promise<any[]> {
    return this.request<any[]>('/interview/history/list');
  }

  // --- Roadmap ---
  async getMyRoadmap(): Promise<any> {
    return this.request<any>('/roadmap/my-roadmap');
  }

  // --- Technical Centre & Lessons ---
  async getTopics(category?: string, subcategory?: string): Promise<TopicItem[]> {
    const params = new URLSearchParams();
    if (category) params.append('category', category);
    if (subcategory) params.append('subcategory', subcategory);
    return this.request<TopicItem[]>(`/lessons/topics?${params.toString()}`);
  }

  async getTopicDetail(slug: string): Promise<any> {
    return this.request<any>(`/lessons/topic/${slug}`);
  }

  async getLesson(id: number): Promise<LessonDetail> {
    return this.request<LessonDetail>(`/lessons/lesson/${id}`);
  }

  async completeLesson(id: number): Promise<any> {
    return this.request<any>(`/lessons/lesson/${id}/complete`, { method: 'POST' });
  }

  // --- Resume ---
  async getMyResume(): Promise<ResumeData> {
    return this.request<ResumeData>('/resume/my-resume');
  }

  async updateMyResume(payload: Partial<ResumeData>): Promise<ResumeData> {
    return this.request<ResumeData>('/resume/my-resume', {
      method: 'PUT',
      body: JSON.stringify(payload),
    });
  }

  async reviewResume(): Promise<any> {
    return this.request<any>('/resume/review', { method: 'POST' });
  }

  // --- Bookmarks ---
  async getBookmarks(): Promise<Bookmark[]> {
    return this.request<Bookmark[]>('/bookmarks/');
  }

  async toggleBookmark(payload: {
    item_type: string;
    item_id: number;
    title: string;
    topic_name?: string;
    category?: string;
    link_path: string;
  }): Promise<Bookmark> {
    return this.request<Bookmark>('/bookmarks/', {
      method: 'POST',
      body: JSON.stringify(payload),
    });
  }

  async deleteBookmark(id: number): Promise<any> {
    return this.request<any>(`/bookmarks/${id}`, { method: 'DELETE' });
  }

  // --- Projects ---
  async getProjectBlueprints(): Promise<ProjectBlueprint[]> {
    return this.request<ProjectBlueprint[]>('/projects/');
  }

  // --- Admin ---
  async getAdminAnalytics(): Promise<any> {
    return this.request<any>('/admin/analytics');
  }

  async getAdminUsers(): Promise<any[]> {
    return this.request<any[]>('/admin/users');
  }

  async toggleUserStatus(userId: number): Promise<any> {
    return this.request<any>(`/admin/users/${userId}/toggle-status`, { method: 'POST' });
  }

  async getAdminQuestions(): Promise<any[]> {
    return this.request<any[]>('/admin/questions');
  }

  async createAdminQuestion(payload: any): Promise<any> {
    return this.request<any>('/admin/questions', {
      method: 'POST',
      body: JSON.stringify(payload),
    });
  }

  async deleteAdminQuestion(id: number): Promise<any> {
    return this.request<any>(`/admin/questions/${id}`, { method: 'DELETE' });
  }
}

export const api = new ApiService();

