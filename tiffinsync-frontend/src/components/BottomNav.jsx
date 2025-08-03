import React from 'react';
import { Link } from 'react-router-dom';

const BottomNav = () => (
  <div className="fixed bottom-0 left-0 w-full flex justify-around bg-gray-200 py-3 rounded-t-xl z-50">
    <Link to="/">🏠</Link>
    <Link to="/search">🔍</Link>
    <Link to="/dashboard">📊</Link>
    <Link to="/profile">👤</Link>
  </div>
);

export default BottomNav;
