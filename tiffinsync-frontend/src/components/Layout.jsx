import React from 'react';
import Sidebar from './Sidebar';
import BottomNav from './BottomNav';
import TopBar from './TopBar';

const Layout = ({ children }) => {
  return (
    <div className="flex min-h-screen bg-gray-50">
      <div className="hidden md:block w-60 bg-gray-800 text-white p-4">
        <Sidebar />
      </div>
      <div className="flex-1 relative pb-16 md:pb-0 pt-14 p-4">
        <TopBar />
        {children}
      </div>
      <div className="md:hidden">
        <BottomNav />
      </div>
    </div>
  );
};

export default Layout;

