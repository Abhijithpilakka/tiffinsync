import API from './api';
import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000/auth';

export const requestOtp = async (phone) => {
  const res = await API.post('/auth/send-otp', { phone });
  return res.data;
};

export const verifyOtp = async (phone, otp) => {
  const res = await API.post('/verify-otp', { phone, otp });
  return res.data;
};
