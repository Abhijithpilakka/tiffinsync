import React from 'react';
import { Link } from 'react-router-dom';

const Sidebar = () => (
  <nav className="flex flex-col gap-4 pt-12">
    <Link to="/" className="hover:bg-gray-700 p-2 rounded">🏠 Home</Link>
    <Link to="/search" className="hover:bg-gray-700 p-2 rounded">🔍 Search</Link>
    <Link to="/dashboard" className="hover:bg-gray-700 p-2 rounded">📊 Dashboard</Link>
    <Link to="/profile" className="hover:bg-gray-700 p-2 rounded">👤 Profile</Link>
  </nav>
);

export default Sidebar;
