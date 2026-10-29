import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider } from './context/AuthContext';

// Layouts
import { PublicLayout } from './layouts/PublicLayout';
import { AppLayout } from './layouts/AppLayout';
import { AdminLayout } from './layouts/AdminLayout';

// Public Pages
import { Home } from './pages/public/Home';
import { Features } from './pages/public/Features';
import { LearningPaths } from './pages/public/LearningPaths';
import { PlacementPrep } from './pages/public/PlacementPrep';
import { About } from './pages/public/About';
import { Login } from './pages/public/Login';
import { Register } from './pages/public/Register';
import { ForgotPassword } from './pages/public/ForgotPassword';
import { ResetPassword } from './pages/public/ResetPassword';
import { Privacy } from './pages/public/Privacy';
import { Terms } from './pages/public/Terms';

// Authenticated Student Pages
import { Dashboard } from './pages/app/Dashboard';
import { Roadmap } from './pages/app/Roadmap';
import { TechnicalCentre } from './pages/app/TechnicalCentre';
import { TopicDetail } from './pages/app/TopicDetail';
import { LessonView } from './pages/app/LessonView';
import { AptitudePractice } from './pages/app/AptitudePractice';
import { PracticeSessionRunner } from './pages/app/PracticeSessionRunner';
import { CodingPractice } from './pages/app/CodingPractice';
import { CodingProblemView } from './pages/app/CodingProblemView';
import { MockInterview } from './pages/app/MockInterview';
import { InterviewSessionRunner } from './pages/app/InterviewSessionRunner';
import { CommunicationLab } from './pages/app/CommunicationLab';
import { ResumeBuilder } from './pages/app/ResumeBuilder';
import { ProgressAnalytics } from './pages/app/ProgressAnalytics';
import { LearningLibrary } from './pages/app/LearningLibrary';
import { ProfileSettings } from './pages/app/ProfileSettings';

// Admin Pages
import { AdminDashboard } from './pages/admin/AdminDashboard';
import { AdminUsers } from './pages/admin/AdminUsers';
import { AdminQuestions } from './pages/admin/AdminQuestions';

export function App() {
  return (
    <AuthProvider>
      <BrowserRouter>
        <Routes>
          {/* Public Routes */}
          <Route element={<PublicLayout />}>
            <Route path="/" element={<Home />} />
            <Route path="/features" element={<Features />} />
            <Route path="/learning-paths" element={<LearningPaths />} />
            <Route path="/placement-prep" element={<PlacementPrep />} />
            <Route path="/about" element={<About />} />
            <Route path="/login" element={<Login />} />
            <Route path="/register" element={<Register />} />
            <Route path="/forgot-password" element={<ForgotPassword />} />
            <Route path="/reset-password" element={<ResetPassword />} />
            <Route path="/privacy" element={<Privacy />} />
            <Route path="/terms" element={<Terms />} />
          </Route>

          {/* Authenticated Student Routes */}
          <Route path="/app" element={<AppLayout />}>
            <Route index element={<Navigate to="/app/dashboard" replace />} />
            <Route path="dashboard" element={<Dashboard />} />
            <Route path="roadmap" element={<Roadmap />} />
            <Route path="technical" element={<TechnicalCentre />} />
            <Route path="technical/topic/:slug" element={<TopicDetail />} />
            <Route path="technical/lesson/:lessonId" element={<LessonView />} />
            <Route path="aptitude" element={<AptitudePractice />} />
            <Route path="practice/session/:sessionId" element={<PracticeSessionRunner />} />
            <Route path="coding" element={<CodingPractice />} />
            <Route path="coding/:problemId" element={<CodingProblemView />} />
            <Route path="interview" element={<MockInterview />} />
            <Route path="interview/session/:sessionId" element={<InterviewSessionRunner />} />
            <Route path="communication" element={<CommunicationLab />} />
            <Route path="resume" element={<ResumeBuilder />} />
            <Route path="progress" element={<ProgressAnalytics />} />
            <Route path="library" element={<LearningLibrary />} />
            <Route path="profile" element={<ProfileSettings />} />
          </Route>

          {/* Protected Administrator Routes */}
          <Route path="/admin" element={<AdminLayout />}>
            <Route index element={<AdminDashboard />} />
            <Route path="users" element={<AdminUsers />} />
            <Route path="questions" element={<AdminQuestions />} />
          </Route>

          {/* Fallback */}
          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      </BrowserRouter>
    </AuthProvider>
  );
}

export default App;

