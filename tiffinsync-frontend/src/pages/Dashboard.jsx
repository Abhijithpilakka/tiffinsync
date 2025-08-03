import React from 'react';
import Layout from '../components/layout';

const Dashboard = () => (
  <Layout>
    <h1 className="text-xl font-bold mb-4">📊 Monthly Analytics</h1>
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
      <div className="bg-white shadow p-4 rounded">
        <p className="text-sm text-gray-500">Total Meals</p>
        <p className="text-2xl font-bold">24</p>
      </div>
      <div className="bg-white shadow p-4 rounded">
        <p className="text-sm text-gray-500">Skipped Meals</p>
        <p className="text-2xl font-bold">6</p>
      </div>
      <div className="bg-white shadow p-4 rounded">
        <p className="text-sm text-gray-500">Total Spend</p>
        <p className="text-2xl font-bold">₹2400</p>
      </div>
    </div>
    <div className="mt-6 bg-white p-4 rounded shadow">
      <p className="font-semibold mb-2">Spending Trend</p>
      <div className="h-40 flex items-center justify-center text-gray-400">
        (Chart Placeholder)
      </div>
    </div>
  </Layout>
);

export default Dashboard;
