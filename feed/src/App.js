import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import Feed from './components/Feed';
import './styles/App.css';

function App() {
  return (
    <div className="app">
      <Header />
      <main className="main-content">
        <Routes>
          <Route path="/" element={<Feed />} />
        </Routes>
      </main>
    </div>
  );
}

export default App; 