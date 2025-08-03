import React, { useState } from 'react';

const LocationModal = ({ isOpen, onClose, onSelect }) => {
  const [locations] = useState([
    'Englewood CHS',
    'Andheri East',
    'Bandra West',
    'Powai',
    'Borivali'
  ]);

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center z-50">
      <div className="bg-white rounded-lg p-4 w-80 shadow-lg">
        <h2 className="text-lg font-semibold mb-3">Select Location</h2>
        <ul className="space-y-2">
          {locations.map((loc, idx) => (
            <li
              key={idx}
              className="p-2 hover:bg-gray-200 rounded cursor-pointer"
              onClick={() => {
                onSelect(loc);
                onClose();
              }}
            >
              {loc}
            </li>
          ))}
        </ul>
        <button
          onClick={onClose}
          className="mt-4 w-full bg-gray-800 text-white py-2 rounded"
        >
          Cancel
        </button>
      </div>
    </div>
  );
};

export default LocationModal;
