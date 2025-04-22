import React, { useState, useEffect, useRef } from 'react';
import axios from 'axios';
import Post from './Post';
import '../styles/Feed.css';

const Feed = ({ algorithm, criteria, setSortTime, triggerSort }) => {
  const [allPosts, setAllPosts] = useState([]);
  const [displayPosts, setDisplayPosts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [loadingMore, setLoadingMore] = useState(false);
  const [loadingSort, setLoadingSort] = useState(false);
  const [error, setError] = useState(null);
  const [page, setPage] = useState(1);
  const [hasMore, setHasMore] = useState(true);
  const isMounted = useRef(true);

  useEffect(() => {
    isMounted.current = true;

    if (!hasMore) {
        setLoading(false);
        setLoadingMore(false);
        return; 
    }

    const fetchPosts = async () => {
      if (page === 1) {
        setLoading(true); 
      } else {
        setLoadingMore(true);
      }
      setError(null);

      try {
        const data = (await import('../data/twitter_sample_100k.json')).default;
        
        const postsPerPage = 20;
        const startIndex = (page - 1) * postsPerPage;
        const endIndex = startIndex + postsPerPage;
        const newPostsRaw = data.slice(startIndex, endIndex);

        if (!isMounted.current) return; 

        if (newPostsRaw.length < postsPerPage) {
          setHasMore(false);
        }

        if (newPostsRaw.length > 0) {
          const newPosts = newPostsRaw.map(rawPost => ({
            id: String(rawPost.id),
            username: rawPost.user,
            displayName: rawPost.user,
            content: rawPost.tweet,
            timestamp: rawPost.date,
            likes: parseInt(rawPost.likes) || 0,
            retweets: parseInt(rawPost.retweets) || 0,
            replies: parseInt(rawPost.replies) || 0,
          })).filter(p => p.id && p.username && p.content && p.timestamp);

          console.log(`Feed: Loaded ${newPosts.length} new posts (Page ${page})`);
          setAllPosts(prevAll => [...prevAll, ...newPosts]);
          setDisplayPosts(prevDisplay => [...prevDisplay, ...newPosts]);
        }

      } catch (err) {
        if (isMounted.current) {
          console.error('Error loading posts:', err);
          setError('Failed to load posts. Please check data file or network.');
          setHasMore(false);
        }
      } finally {
        if (isMounted.current) {
          setLoading(false);
          setLoadingMore(false);
        }
      }
    };

    fetchPosts();

    return () => { isMounted.current = false; };

  }, [page]);

  useEffect(() => {
    if (triggerSort === 0 || allPosts.length === 0) return;
    isMounted.current = true; 

    const sortPosts = async () => {
      console.log(`Feed: Sorting triggered. Algorithm: ${algorithm}, Criteria: ${criteria}`);
      setLoadingSort(true);
      setError(null);
      setSortTime(null);

      try {
        const backendUrl = 'http://localhost:5001/sort';
        const postsToSort = allPosts; 
        
        console.log(`Feed: Sending ${postsToSort.length} posts to backend for sorting.`);

        const response = await axios.post(backendUrl, {
          tweets: postsToSort, 
          criteria: criteria,
          algorithm: algorithm
        });

        if (isMounted.current) {
          console.log('Feed: Received sorted data from backend:', response.data?.sorted_tweets?.slice(0, 5)); 
          const sortedData = response.data.sorted_tweets;

          if (sortedData && Array.isArray(sortedData)) {
              console.log('Feed: Current displayPosts state (first 5):', displayPosts.slice(0, 5));

              const newSortedArray = [...sortedData]; 
              
              setAllPosts(newSortedArray);
              setDisplayPosts(newSortedArray);
              
              console.log('Feed: Set displayPosts state with new array (first 5):', newSortedArray.slice(0, 5));
              
              setSortTime(response.data.sort_time_ms);
          } else {
              console.error('Feed: Received invalid sorted data format from backend');
              setError('Received invalid sorted data format from backend.');
          }
        }

      } catch (err) {
        if (isMounted.current) {
          console.error('Error sorting posts:', err);
          const errorMsg = err.response?.data?.error || 'Failed to sort posts. Backend might be down or encountered an error.';
          setError(errorMsg);
        }
      } finally {
        if (isMounted.current) {
          setLoadingSort(false);
        }
      }
    };

    sortPosts();
    
    return () => { isMounted.current = false; };

  }, [triggerSort, algorithm, criteria]); 

  const handleLoadMore = () => {
    if (!loadingMore && !loadingSort && hasMore) {
      setPage(prevPage => prevPage + 1);
    }
  };

  if (loading && displayPosts.length === 0) {
    return <div className="loading">Loading posts...</div>;
  }

  if (error && displayPosts.length === 0) { 
    return <div className="error">Error: {error}</div>;
  }

  console.log(`Feed: Rendering component. loading=${loading}, loadingSort=${loadingSort}. Displaying ${displayPosts.length} posts.`);

  return (
    <div className="feed">
      <div className="feed-header">
        <h2>Home</h2>
        {loadingSort && <div className="loading-sort">Sorting...</div>}
        {error && !loadingSort && <div className="error feed-error">Error: {error}</div>} {/*Show non-fatal errors */} 
      </div>

      <div className="posts">
        {displayPosts.map((post, index) => (
          <Post key={`${post.id}-${index}`} post={post} />
        ))}
      </div>

      {loadingMore && <div className="loading">Loading more posts...</div>}

      {!loadingSort && !loadingMore && hasMore && (
        <div className="load-more">
          <button onClick={handleLoadMore} disabled={loadingMore || loadingSort}>
            Load More
          </button>
        </div>
      )}

      {!loadingSort && !loadingMore && !hasMore && displayPosts.length > 0 && (
        <div className="end-message">You've reached the end of the feed.</div>
      )}
      
      {!loading && !loadingMore && !hasMore && displayPosts.length === 0 && (
          <div className="end-message">No posts to display.</div>
      )}
    </div>
  );
};

export default Feed; 