import React, { useEffect, useState } from 'react';
import Layout from '../components/Layout';
import { fetchMeals } from '../services/mealService';

const Home = () => {
  const [meals, setMeals] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const loadMeals = async () => {
      try {
        const data = await fetchMeals();
        setMeals(data);
      } catch {
        setError("Failed to load meals");
      } finally {
        setLoading(false);
      }
    };
    loadMeals();
  }, []);

  return (
    <Layout>
      <h1 className="text-xl font-bold mb-4">Today's Meals</h1>
      {loading && <p>Loading...</p>}
      {error && <p className="text-red-500">{error}</p>}
      {!loading && !error && meals.length === 0 && <p>No meals available today.</p>}
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
