import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import Pokedex from './Pokedex'

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <Pokedex />
  </React.StrictMode>
);

