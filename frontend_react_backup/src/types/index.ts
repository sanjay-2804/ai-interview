export interface UserProfile {
  id: number;
  college?: string;
  course?: string;
  degree?: string;
  study_year?: string;
  graduation_year?: string;
  target_role: string;
  preferred_programming_language?: string;
  preferred_language?: string;
  skill_level: string;
  study_availability?: number;
  study_hours_per_day?: number;
  preferred_topics: string[];
  prep_priorities: string[];
  onboarding_completed: boolean;
}

export interface User {
  id: number;
  email: string;
  full_name: string;
  role: 'student' | 'admin';
  is_active: boolean;
  created_at: string;
  profile?: UserProfile;
}

export interface AuthResponse {
  access_token: string;
  token_type: string;
  user: User;
}

export interface QuestionOptionPublic {
  option_key: string;
  option_text: string;
}

export interface QuestionPublic {
  id: number;
  topic_id: number;
  question_type: string;
  difficulty: string;
  question_text: string;
  code_snippet?: string;
  options: QuestionOptionPublic[];
}

export interface OptionFeedback {
  option_key: string;
  option_text: string;
  is_correct: boolean;
  why_wrong?: string;
}

export interface AnswerFeedback {
  question_id: number;
  selected_option: string;
  correct_option: string;
  is_correct: boolean;
  status: string;
  explanation: string;
  step_by_step_reasoning: string;
  practical_example: string;
  common_mistake: string;
  learning_tip: string;
  related_concept_url?: string;
  encouraging_feedback: string;
  options_breakdown: OptionFeedback[];
}

export interface SessionQuestionItem {
  order_index: number;
  question: QuestionPublic;
  is_answered: boolean;
  submitted_answer?: string;
  is_correct?: boolean;
  feedback?: AnswerFeedback;
}

export interface PracticeSessionDetail {
  id: number;
  category: string;
  subcategory?: string;
  difficulty: string;
  session_mode?: string;
  time_limit_seconds?: number;
  marked_for_review_json?: number[];
  total_questions: number;
  completed_questions: number;
  correct_count: number;
  score_percentage: number;
  status: 'in_progress' | 'completed';
  questions: SessionQuestionItem[];
}

export interface CommunicationPrompt {
  id: number;
  title: string;
  category: string;
  question: string;
  framework: string;
  target_duration_seconds: number;
  sample_answer: string;
}

export interface CommunicationSessionRecord {
  id: number;
  category: string;
  prompt_title: string;
  prompt_question: string;
  framework?: string;
  audio_filename?: string;
  audio_duration_seconds: number;
  transcript: string;
  overall_score: number;
  relevance_score: number;
  clarity_score: number;
  grammar_score: number;
  conciseness_score: number;
  delivery_score: number;
  wpm: number;
  filler_words_count: number;
  filler_words_list: string[];
  strengths: string[];
  improvements: string[];
  sample_answer?: string;
  status: string;
  created_at: string;
}

export interface CodingProblemListOut {
  id: number;
  title: string;
  slug: string;
  difficulty: string;
  category: string;
  time_complexity: string;
  space_complexity: string;
  external_url?: string;
  external_platform?: string;
  has_attempted: boolean;
  is_solved: boolean;
}

export interface CodingProblemDetail {
  id: number;
  topic_id: number;
  title: string;
  slug: string;
  difficulty: string;
  category: string;
  description: string;
  input_format: string;
  output_format: string;
  constraints: string;
  sample_input: string;
  sample_output: string;
  starter_code_python: string;
  starter_code_javascript: string;
  starter_code_java: string;
  starter_code_cpp: string;
  solution_explanation: string;
  time_complexity: string;
  space_complexity: string;
  hints: string[];
  external_url?: string;
  external_platform?: string;
}

export interface CodeRunResult {
  status: string;
  output_log: string;
  runtime_ms: number;
  memory_kb: number;
  passed_tests: number;
  total_tests: number;
  is_sample_preview: boolean;
  guidance: string;
}

export interface MockInterviewResponseOut {
  id: number;
  question_text: string;
  category: string;
  student_response: string;
  score?: number;
  evaluation_status: string;
  strengths: string[];
  missing_concepts: string[];
  improvement_suggestions: string[];
  sample_answer: string;
  ai_engine: string;
}

export interface MockInterviewDetail {
  id: number;
  category: string;
  target_role: string;
  difficulty: string;
  total_questions: number;
  completed_questions: number;
  status: 'in_progress' | 'completed';
  current_question_text?: string;
  responses: MockInterviewResponseOut[];
  overall_score?: number;
  feedback_summary?: string;
}

export interface ResumeData {
  id?: number;
  title: string;
  full_name: string;
  email: string;
  phone?: string;
  location?: string;
  target_role?: string;
  summary?: string;
  education_json: Array<{
    degree: string;
    institution: string;
    year: string;
    score: string;
  }>;
  skills_json: string[];
  projects_json: Array<{
    title: string;
    description: string;
    tech_stack: string;
    link: string;
  }>;
  experience_json: Array<{
    role: string;
    company: string;
    period: string;
    description: string;
  }>;
  certifications_json: Array<{
    name: string;
    issuer: string;
    year: string;
  }>;
  links_json: {
    github?: string;
    linkedin?: string;
    portfolio?: string;
  };
  ai_review_feedback?: {
    score?: number;
    strengths?: string[];
    improvements?: string[];
    keyword_suggestions?: string[];
    engine?: string;
  };
}

export interface Bookmark {
  id: number;
  item_type: string;
  item_id: number;
  title: string;
  topic_name?: string;
  category?: string;
  link_path: string;
  created_at: string;
}

export interface DashboardStats {
  total_questions_attempted: number;
  overall_accuracy_percentage: number;
  total_lessons_completed: number;
  total_coding_solved: number;
  total_mock_interviews: number;
  streak_days: number;
  recent_activities: Array<{
    id: number;
    type: string;
    title: string;
    details?: string;
    time: string;
  }>;
  weak_topics: Array<{
    topic: string;
    category: string;
    accuracy: number;
    attempts: number;
  }>;
  strong_topics: Array<{
    topic: string;
    category: string;
    accuracy: number;
    attempts: number;
  }>;
  recommended_activities: Array<{
    title: string;
    action: string;
    link: string;
    category: string;
  }>;
  roadmap_progress_percentage: number;
  target_role: string;
  skill_level: string;
}

export interface TopicItem {
  id: number;
  name: string;
  slug: string;
  category: string;
  subcategory: string;
  description: string;
  icon: string;
  lesson_count: number;
  resource_count: number;
  question_count: number;
  coding_count: number;
}

export interface LessonDetail {
  id: number;
  topic_id: number;
  title: string;
  slug: string;
  difficulty: string;
  content_markdown: string;
  key_takeaways: string[];
  estimated_minutes: number;
  is_completed: boolean;
  resources: Array<{
    id: number;
    title: string;
    url: string;
    resource_type: string;
    provider_name: string;
    language: string;
    description: string;
  }>;
}

export interface ProjectBlueprint {
  id: number;
  title: string;
  role: string;
  difficulty: string;
  problem_statement: string;
  objectives: string[];
  tech_stack: string[];
  main_features: string[];
  milestones: string[];
  database_schema: string;
  testing_requirements: string;
  github_guidance: string;
  interview_questions: string[];
}

