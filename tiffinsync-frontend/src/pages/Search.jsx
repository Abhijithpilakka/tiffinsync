import React, { useEffect, useState } from 'react';
import Layout from '../components/Layout';
import { fetchProviders } from '../services/providerService';

const Search = () => {
  const [providers, setProviders] = useState([]);

  useEffect(() => {
    const loadProviders = async () => {
      const data = await fetchProviders();
      setProviders(data);
    };
    loadProviders();
  }, []);

  return (
    <Layout>
      <h1 className="text-xl font-bold mb-4">Available Providers</h1>
      {providers.map((provider) => (
        <div key={provider.id} className="p-2 bg-gray-200 rounded mb-2">
          <p className="font-semibold">{provider.name}</p>
          <p>{provider.location}</p>
          <p>⭐ {provider.rating}</p>
        </div>
      ))}
    </Layout>
  );
};

export default Search;

