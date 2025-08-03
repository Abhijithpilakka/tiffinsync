import React from 'react';
import Layout from '../components/layout';

const Profile = () => {
  const user = {
    name: 'Abhijith P',
    email: 'abhijith@example.com',
    phone: '+91 9876543210',
    joined: 'March 2024',
  };

  return (
    <Layout>
      <h1 className="text-xl font-semibold mb-4">👤 Your Profile</h1>
      <div className="bg-white shadow-md rounded-lg p-4">
        <p className="text-sm text-gray-500">Name:</p>
        <p className="text-lg font-semibold mb-2">{user.name}</p>
        <p className="text-sm text-gray-500">Email:</p>
        <p className="text-md mb-2">{user.email}</p>
        <p className="text-sm text-gray-500">Phone:</p>
        <p className="text-md mb-2">{user.phone}</p>
        <p className="text-sm text-gray-500">Joined:</p>
        <p className="text-md">{user.joined}</p>
      </div>
    </Layout>
  );
};

export default Profile;
