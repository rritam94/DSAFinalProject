import React from 'react';
import '../styles/SortPanel.css';

const SortPanel = ({ 
  onSort, 
  sortTime,
  currentAlgorithm,
  currentCriteria,
  setAlgorithm,
  setCriteria
}) => {
  const criteriaOptions = ['date', 'user', 'likes', 'retweets', 'replies', 'id'];
  const algorithmOptions = ['heap', 'counting'];

  const handleCriteriaClick = (crit) => {
    setCriteria(crit); 
  };

  const handleAlgoClick = (algo) => {
    setAlgorithm(algo);
  }

  const handleConfirmSort = () => {
    onSort(currentAlgorithm, currentCriteria);
  };

  return (
    <div className="sort-panel">
      <h3>Sort Tweets</h3>
      
      <div className="sort-group">
        <h4>Algorithm:</h4>
        {algorithmOptions.map(algo => (
          <button 
            key={algo} 
            onClick={() => handleAlgoClick(algo)}
            className={currentAlgorithm === algo ? 'active' : ''}
          >
            {algo === 'heap' ? 'Heap Sort' : 'Counting Sort'}
          </button>
        ))}
      </div>

      <div className="sort-group">
        <h4>Criteria:</h4>
        {criteriaOptions.map(crit => (
          <button 
            key={crit} 
            onClick={() => handleCriteriaClick(crit)}
            className={currentCriteria === crit ? 'active' : ''}
          >
            {crit.charAt(0).toUpperCase() + crit.slice(1)} 
          </button>
        ))}
      </div>

      {} 
      <button className="confirm-sort-button" onClick={handleConfirmSort}>
        Sort Now
      </button>

      {sortTime !== null && (
        <div className="sort-time">
          Sort Time: {sortTime.toFixed(2)} ms
        </div>
      )}
    </div>
  );
};

export default SortPanel; 