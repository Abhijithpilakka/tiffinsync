import React, { useEffect, useState } from 'react';
import Layout from '../components/Layout';
import { fetchMeals } from '../services/mealService';

const Home = () => {
  const [meals, setMeals] = useState([]);

  useEffect(() => {
    const loadMeals = async () => {
      const data = await fetchMeals();
      setMeals(data);
    };
    loadMeals();
  }, []);

  return (
    <Layout>
      <h1 className="text-xl font-bold mb-4">Today's Meals</h1>
      {meals.map((meal) => (
        <div key={meal.id} className="p-2 bg-gray-200 rounded mb-2">
          <p className="font-semibold">{meal.type}</p>
          <p>{meal.description}</p>
        </div>
      ))}
    </Layout>
  );
};

export default Home;

