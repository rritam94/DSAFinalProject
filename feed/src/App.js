import React, { useState } from 'react';
import { Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import Feed from './components/Feed';
import SortPanel from './components/SortPanel';
import './styles/App.css';

function App() {
  //different states for sorting
  const [sortAlgorithm, setSortAlgorithm] = useState('heap');
  const [sortCriteria, setSortCriteria] = useState('date');
  const [sortTime, setSortTime] = useState(null);
  const [triggerSort, setTriggerSort] = useState(0);

  //button clicker handler
  const handleSort = (algorithm, criteria) => {
    console.log(`App: Triggering sort with ${algorithm} by ${criteria}`);
    setSortAlgorithm(algorithm);
    setSortCriteria(criteria);
    setTriggerSort(prev => prev + 1);
  };

  return (
    <div className="app">
      <Header />
      <div className="app-content">
        <main className="main-content">
          <Routes>
            <Route
              path="/"
              element={
                <Feed
                  algorithm={sortAlgorithm}
                  criteria={sortCriteria}
                  setSortTime={setSortTime}
                  triggerSort={triggerSort}
                />
              }
            />
          </Routes>
        </main>
        {/*control/sort panel*/}
        <SortPanel 
          onSort={handleSort} 
          sortTime={sortTime}
          currentAlgorithm={sortAlgorithm}
          currentCriteria={sortCriteria}
          setAlgorithm={setSortAlgorithm}
          setCriteria={setSortCriteria}
        />
      </div>
    </div>
  );
}

export default App; 