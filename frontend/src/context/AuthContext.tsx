import React, { createContext, useContext, useState, useEffect } from 'react';
import { User } from '../types';
import { api } from '../services/api';

interface AuthContextType {
  user: User | null;
  isAuthenticated: boolean;
  isLoading: boolean;
  login: (email: string, pass: string, rememberMe?: boolean) => Promise<User>;
  register: (name: string, email: string, pass: string, targetRole?: string) => Promise<User>;
  logout: () => Promise<void>;
  refreshUser: () => Promise<void>;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [user, setUser] = useState<User | null>(() => {
    const saved = localStorage.getItem('interviewai_user');
    return saved ? JSON.parse(saved) : null;
  });
  const [isLoading, setIsLoading] = useState<boolean>(true);

  useEffect(() => {
    // Attempt session restoration with HttpOnly cookie or stored token
    api.getMe()
      .then((fetchedUser) => {
        setUser(fetchedUser);
        localStorage.setItem('interviewai_user', JSON.stringify(fetchedUser));
      })
      .catch(() => {
        localStorage.removeItem('interviewai_token');
        localStorage.removeItem('interviewai_user');
        setUser(null);
      })
      .finally(() => setIsLoading(false));
  }, []);

  const login = async (email: string, pass: string, rememberMe: boolean = false): Promise<User> => {
    const res = await api.login({ email, password: pass, remember_me: rememberMe });
    if (res.access_token) {
      localStorage.setItem('interviewai_token', res.access_token);
    }
    localStorage.setItem('interviewai_user', JSON.stringify(res.user));
    setUser(res.user);
    return res.user;
  };

  const register = async (name: string, email: string, pass: string, targetRole?: string): Promise<User> => {
    const res = await api.register({ full_name: name, email, password: pass, target_role: targetRole });
    if (res.access_token) {
      localStorage.setItem('interviewai_token', res.access_token);
    }
    localStorage.setItem('interviewai_user', JSON.stringify(res.user));
    setUser(res.user);
    return res.user;
  };

  const logout = async () => {
    try {
      await api.logout();
    } catch {
      // Ignored
    } finally {
      localStorage.removeItem('interviewai_token');
      localStorage.removeItem('interviewai_user');
      setUser(null);
      window.location.href = '/login';
    }
  };

  const refreshUser = async () => {
    try {
      const updated = await api.getMe();
      setUser(updated);
      localStorage.setItem('interviewai_user', JSON.stringify(updated));
    } catch {
      // Ignored
    }
  };

  return (
    <AuthContext.Provider
      value={{
        user,
        isAuthenticated: !!user,
        isLoading,
        login,
        register,
        logout,
        refreshUser,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};

