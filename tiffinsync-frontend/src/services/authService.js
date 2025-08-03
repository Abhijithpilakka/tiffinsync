import API from './api';

export const registerUser = async (data) => {
  const res = await API.post('/auth/register', data);
  return res.data;
};

export const loginUser = async (email, password) => {
  const res = await API.post('/auth/login', null, { params: { email, password } });
  return res.data;
};
