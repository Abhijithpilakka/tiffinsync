import React, { createContext, useState, useEffect } from 'react';
import jwtDecode from 'jwt-decode';
import API from '../services/api';

export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [token, setToken] = useState(localStorage.getItem('token') || null);
  const [refreshToken, setRefreshToken] = useState(localStorage.getItem('refreshToken') || null);

  const isTokenExpired = (t) => {
    try {
      const decoded = jwtDecode(t);
      return decoded.exp * 1000 < Date.now();
    } catch {
      return true;
    }
  };

  const refreshAccessToken = async () => {
    if (!refreshToken || isTokenExpired(refreshToken)) {
      handleSessionExpired();
      return;
    }
    try {
      const res = await API.post('/auth/refresh', { refresh_token: refreshToken });
      const newAccessToken = res.data.access_token;
      setToken(newAccessToken);
      localStorage.setItem('token', newAccessToken);
    } catch {
      handleSessionExpired();
    }
  };

  const handleSessionExpired = () => {
    alert('Your session has expired. Please log in again.');
    logout();
    window.location.href = '/login';
  };

  useEffect(() => {
    if (token && isTokenExpired(token)) {
      refreshAccessToken();
    }
  }, [token]);

  const login = (accessToken, refresh) => {
    setToken(accessToken);
    setRefreshToken(refresh);
    localStorage.setItem('token', accessToken);
    localStorage.setItem('refreshToken', refresh);
  };

  const logout = () => {
    setToken(null);
    setRefreshToken(null);
    localStorage.removeItem('token');
    localStorage.removeItem('refreshToken');
  };

  return (
    <AuthContext.Provider value={{ token, login, logout, isAuthenticated: !!token }}>
      {children}
    </AuthContext.Provider>
  );
};
