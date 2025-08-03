import API from './api';

export const fetchMeals = async () => {
  const res = await API.get('/meals');
  return res.data;
};
