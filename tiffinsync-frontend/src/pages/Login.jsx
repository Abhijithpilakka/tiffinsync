import React, { useState, useContext } from 'react';
import { loginUser } from '../services/authService';
import { AuthContext } from '../context/AuthContext';

const Login = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const { login } = useContext(AuthContext);

  const handleLogin = async () => {
    try {
      const res = await loginUser(email, password);
      login(res.access_token, res.refresh_token);
      window.location.href = '/';
    } catch {
      alert('Invalid credentials');
    }
  };

  return (
    <div className="flex flex-col max-w-sm mx-auto mt-20 p-4 border rounded shadow">
      <h1 className="text-lg font-bold mb-4">Login</h1>
      <input
        type="email"
        placeholder="Email"
        className="border p-2 mb-2 rounded"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />
      <input
        type="password"
        placeholder="Password"
        className="border p-2 mb-2 rounded"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />
      <button
        onClick={handleLogin}
        className="bg-gray-800 text-white py-2 rounded"
      >
        Login
      </button>
    </div>
  );
};

export default Login;
