import React from 'react';
import Layout from '../components/layout';

const Search = () => {
  const providers = [
    { name: 'Mr. Sarthak Jain', rating: 4 },
    { name: 'Mr. Ramesh Kumar', rating: 5 },
    { name: 'Mr. Amit Sharma', rating: 3 },
  ];

  return (
    <Layout>
      
      {providers.map((provider, idx) => (
        <div
          key={idx}
          className="flex items-center justify-between bg-gray-200 p-3 rounded-xl mb-2"
        >
          <div className="flex items-center gap-2">
            <div className="w-10 h-10 bg-gray-400 rounded-full"></div>
            <div>
              <p className="font-semibold text-sm">{provider.name}</p>
              <p className="text-xs text-gray-600">Breakfast, Lunch, Dinner</p>
            </div>
          </div>
          <div className="flex flex-col items-end">
            <div className="text-yellow-400 text-sm">
              {'★'.repeat(provider.rating) + '☆'.repeat(5 - provider.rating)}
            </div>
            <div className="flex gap-1 mt-1">
              <span className="w-2 h-2 bg-green-600 rounded-full"></span>
              <span className="w-2 h-2 bg-red-600 rounded-full"></span>
            </div>
          </div>
        </div>
      ))}
    </Layout>
  );
};

export default Search;
