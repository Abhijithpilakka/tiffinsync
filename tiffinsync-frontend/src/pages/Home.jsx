import React, { useState } from 'react';
import Layout from '../components/layout';

const Home = () => {
  const [meals, setMeals] = useState([
    { type: 'Breakfast', description: 'Idly-3, Sambar, Chutney', optedIn: false },
    { type: 'Lunch', description: 'Chapati-2, Dal fry, Rice, Paneer Subjee', optedIn: true },
    { type: 'Dinner', description: 'Chapati-3, Dal fry, Veg Subjee', optedIn: true },
  ]);

  const toggleOpt = (index) => {
    const updatedMeals = [...meals];
    updatedMeals[index].optedIn = !updatedMeals[index].optedIn;
    setMeals(updatedMeals);
  };

  return (
    <Layout>
      <div className="bg-white p-4 rounded-xl shadow mb-4">
        <div className="flex justify-between text-sm font-medium mb-4">
          <p>{new Date().toLocaleDateString()}</p>
          <p className="text-right">Tiffin Provider Name</p>
        </div>
        {meals.map((meal, i) => (
          <div
            key={i}
            className="flex justify-between items-center bg-gray-200 rounded-lg p-2 mb-2"
          >
            <div>
              <p className="text-xs text-gray-500">{meal.type}</p>
              <p className="text-sm font-medium">{meal.description}</p>
            </div>
            <button
              className={`w-6 h-6 rounded-sm ${meal.optedIn ? 'bg-green-800' : 'bg-red-800'}`}
              onClick={() => toggleOpt(i)}
            >
              <input
                type="checkbox"
                checked={meal.optedIn}
                readOnly
                className="opacity-0 w-full h-full cursor-pointer"
              />
            </button>
          </div>
        ))}
        <button className="w-full mt-3 bg-gray-800 text-white py-2 rounded-md">
          Submit ➤
        </button>
      </div>

      <div className="bg-gray-100 rounded-xl p-4">
        <div className="flex justify-between mb-2">
          <div className="text-center">
            <p className="text-lg font-bold">24</p>
            <p className="text-xs">Meals Ordered</p>
          </div>
          <div className="text-center">
            <p className="text-lg font-bold">6</p>
            <p className="text-xs">Skipped Meals</p>
          </div>
        </div>
        <div className="bg-gray-300 text-center py-2 rounded-md">
          <p className="font-bold text-lg">₹2400</p>
          <p className="text-sm">Total Spend</p>
        </div>
      </div>
    </Layout>
  );
};

export default Home;
