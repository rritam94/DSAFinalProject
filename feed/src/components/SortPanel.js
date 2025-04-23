import React from 'react';
import '../styles/SortPanel.css';

//control panel
const SortPanel = ({ 
  onSort, 
  sortTime,
  currentAlgorithm,
  currentCriteria,
  setAlgorithm,
  setCriteria
}) => {
  //sorting options
  const criteriaOptions = ['date', 'user', 'likes', 'retweets', 'replies', 'id'];
  const algorithmOptions = ['heap', 'counting'];

  //updated the selected options
  const handleCriteriaClick = (crit) => {
    setCriteria(crit); 
  };

  //updated algo
  const handleAlgoClick = (algo) => {
    setAlgorithm(algo);
  }

  //init actual sort operation
  const handleConfirmSort = () => {
    onSort(currentAlgorithm, currentCriteria);
  };

  return (
    <div className="sort-panel">
      <h3>Sort Tweets</h3>
      
      {/*algo select buttons*/}
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

      {/*Criteria select buttons*/}
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

      {/*performance display + sort button*/}
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