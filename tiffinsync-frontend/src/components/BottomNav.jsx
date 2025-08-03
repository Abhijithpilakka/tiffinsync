import React from 'react';
import { Link } from 'react-router-dom';

const BottomNav = () => (
  <div className="fixed bottom-0 left-0 w-full flex justify-around bg-gray-200 py-3 rounded-t-xl z-50 shadow-md">
    <Link to="/" className="text-xl">🏠</Link>
    <Link to="/search" className="text-xl">🔍</Link>
    <Link to="/dashboard" className="text-xl">📊</Link>
    <Link to="/profile" className="text-xl">👤</Link>
  </div>
);

export default BottomNav;

