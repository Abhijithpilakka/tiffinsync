import React, { useState } from 'react';
import LocationModal from './LocationModal';

const TopBar = () => {
  const [location, setLocation] = useState('Englewood CHS');
  const [isModalOpen, setIsModalOpen] = useState(false);

  return (
    <>
      <div className="fixed top-0 left-0 w-full bg-white shadow-md z-50 flex justify-between items-center px-4 py-2">
        {/* App Logo */}
        <div className="flex items-center gap-2">
          <img src="/tiffinsync.png" alt="TiffinSync Logo" className= "h-8" />
          
        </div>

        {/* Current Location */}
        <div
          className="flex items-center gap-1 text-sm font-medium text-gray-700 cursor-pointer"
          onClick={() => setIsModalOpen(true)}
        >
          📍 <span>{location} ▼</span>
        </div>
      </div>

      {/* Location Picker Modal */}
      <LocationModal
        isOpen={isModalOpen}
        onClose={() => setIsModalOpen(false)}
        onSelect={setLocation}
      />
    </>
  );
};

export default TopBar;
