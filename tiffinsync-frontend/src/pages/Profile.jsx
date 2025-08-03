import React, { useContext } from 'react';
import Layout from '../components/Layout';
import { AuthContext } from '../context/AuthContext';

const Profile = () => {
  const { logout } = useContext(AuthContext);

  const user = {
    name: 'Abhijith P',
    email: 'abhijith@example.com',
    phone: '+91 9876543210',
    joined: 'March 2024',
  };

  return (
    <Layout>
      <h1 className="text-xl font-semibold mb-4">👤 Your Profile</h1>
      <div className="bg-white p-4 rounded shadow mb-4">
        <p><b>Name:</b> {user.name}</p>
        <p><b>Email:</b> {user.email}</p>
        <p><b>Phone:</b> {user.phone}</p>
        <p><b>Joined:</b> {user.joined}</p>
      </div>
      <button
        onClick={() => { logout(); window.location.href = '/login'; }}
        className="bg-red-600 text-white w-full py-2 rounded"
      >
        Logout
      </button>
    </Layout>
  );
};

export default Profile;
