import React, { useState, useContext } from 'react';
import { useNavigate } from 'react-router-dom';
import { requestOtp } from '../services/authService';
import { AuthContext } from '../context/AuthContext';

const Login = () => {
  const [phone, setPhone] = useState('');
  const navigate = useNavigate();

  const handleLogin = async () => {
    try {
      await requestOtp(phone);
      navigate('/verify-otp', { state: { phone } });
    } catch {
      alert('Failed to send OTP');
    }
  };

  return (
    <div className="flex flex-col max-w-sm mx-auto mt-20 p-6 border rounded shadow">
      <h1 className="text-xl font-semibold mb-6">Login</h1>
      <input
        type="tel"
        placeholder="Mobile Number"
        className="border p-3 mb-4 rounded"
        value={phone}
        onChange={(e) => setPhone(e.target.value)}
      />
      <button
        onClick={handleLogin}
        className="bg-gray-900 text-white py-3 rounded"
      >
        Send OTP
      </button>
    </div>
  );
};

export default Login;
