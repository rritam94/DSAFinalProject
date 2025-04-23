import React from 'react';
import '../styles/SortPanel.css';

//control panel
const SortPanel = ({ 
  onSort, 
  sortTime,
  currentAlgorithm,
  currentCriteria,
  setAlgorithm,
  setCriteria,
  onRestore
}) => {
  //sorting options
  const criteriaOptions = ['date', 'user', 'likes', 'retweets', 'replies', 'id'];
  const algorithmOptions = ['heap', 'counting'];

  //updated the selected options
  const handleCriteriaClick = (crit) => {
    setLocalCriteria(crit);
  };

  //updated algo
  const handleAlgoClick = (algo) => {
    setLocalAlgorithm(algo);
  }

  //init actual sort operation
  const handleConfirmSort = () => {
    setCriteria(localCriteria);
    setAlgorithm(localAlgorithm);
    onSort(localAlgorithm, localCriteria);
  };

  const handleRestoreOriginal = () => {
    setLocalCriteria('date');
    setLocalAlgorithm('heap');
    
    setCriteria('date');
    setAlgorithm('heap');
    
    if (typeof onRestore === 'function') {
      onRestore();
    } else {
      window.location.reload();
    }
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
            className={localAlgorithm === algo ? 'active' : ''}
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
            className={localCriteria === crit ? 'active' : ''}
          >
            {crit.charAt(0).toUpperCase() + crit.slice(1)} 
          </button>
        ))}
      </div>

      {/*performance display + sort button*/}
      <button className="confirm-sort-button" onClick={handleConfirmSort}>
        Sort Now
      </button>

      <button className="restore-button" onClick={handleRestoreOriginal}>
        Restore Original Order
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