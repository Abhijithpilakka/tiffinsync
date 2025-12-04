import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000/auth';

export const requestOtp = async (phone) => {
  const res = await axios.post(`${API_URL}/send-otp`, { phone });
  return res.data;
};

export const verifyOtp = async (phone, otp) => {
  const res = await axios.post(`${API_URL}/verify-otp`, { phone, otp });
  return res.data;
};
