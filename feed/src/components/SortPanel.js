import React from 'react';
import '../styles/SortPanel.css';

// sort panel component
const SortPanel = ({ 
  onSort, 
  sortTime,
  currentAlgorithm,
  currentCriteria,
  setAlgorithm,
  setCriteria,
  onRestore
}) => {
  // criteria options
  const criteriaOptions = ['date', 'user', 'likes', 'retweets', 'replies'];
  // algorithm options
  const algorithmOptions = ['heap', 'counting'];

  // local criteria and algorithm
  const [localCriteria, setLocalCriteria] = React.useState(currentCriteria);
  const [localAlgorithm, setLocalAlgorithm] = React.useState(currentAlgorithm);

  // useEffect to set the local criteria and algorithm
  React.useEffect(() => {
    setLocalCriteria(currentCriteria);
    setLocalAlgorithm(currentAlgorithm);
  }, []);

  // handle criteria click
  const handleCriteriaClick = (crit) => {
    setLocalCriteria(crit);
  };

  // handle algorithm click
  const handleAlgoClick = (algo) => {
    setLocalAlgorithm(algo);
  }

  // handle confirm sort
  const handleConfirmSort = () => {
    setCriteria(localCriteria);
    setAlgorithm(localAlgorithm);
    onSort(localAlgorithm, localCriteria);
  };

  // handle restore original
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

      {/* sort group */}
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