import API from './api';

export const fetchProviders = async () => {
  const res = await API.get('/providers');
  return res.data;
};
