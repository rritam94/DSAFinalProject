import React, { useState, useEffect, useRef } from 'react';
import axios from 'axios';
import Post from './Post';
import '../styles/Feed.css';

// react component for the twitter feed
const Feed = ({ algorithm, criteria, setSortTime, triggerSort }) => {
  // state variables for the feed
  const [allPosts, setAllPosts] = useState([]);
  const [displayPosts, setDisplayPosts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [loadingMore, setLoadingMore] = useState(false);
  const [loadingSort, setLoadingSort] = useState(false);
  const [error, setError] = useState(null);
  const [page, setPage] = useState(1);
  const [hasMore, setHasMore] = useState(true);
  const isMounted = useRef(true);

  // useEffect to load the posts  
  useEffect(() => {
    isMounted.current = true;

    if (triggerSort > 0) {
      return;
    }

    if (!hasMore) {
      setLoading(false);
      setLoadingMore(false);
      return; 
    }

    const fetchPosts = async () => {
      if (page === 1) {
        setLoading(true); 
      } 
      
      else {
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
            // map the raw post to the post object
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

  }, [page, triggerSort, hasMore]);

  useEffect(() => {
    if (triggerSort === 0 || allPosts.length === 0) return;

    // useEffect to sort the posts

    const sortPosts = async () => {
      console.log(`Feed: Sorting triggered. Algorithm: ${algorithm}, Criteria: ${criteria}`);
      setLoadingSort(true);
      setError(null);
      setSortTime(null);

      try {
        const allJsonData = (await import('../data/twitter_sample_100k.json')).default;
        
        const allFormattedPosts = allJsonData.map(rawPost => ({
          id: String(rawPost.id),
          username: rawPost.user,
          displayName: rawPost.user,
          content: rawPost.tweet,
          timestamp: rawPost.date,
          likes: parseInt(rawPost.likes) || 0,
          retweets: parseInt(rawPost.retweets) || 0,
          replies: parseInt(rawPost.replies) || 0,
        })).filter(p => p.id && p.username && p.content && p.timestamp);
        
        console.log(`Feed: Sending all ${allFormattedPosts.length} posts from JSON to backend for sorting.`);
        
        // send the posts to the backend for sorting
        const backendUrl = 'http://localhost:5001/sort';
        const response = await axios.post(backendUrl, {
          tweets: allFormattedPosts, 
          criteria: criteria,
          algorithm: algorithm
        });

        if (!isMounted.current) return;

        console.log('Feed: Received sorted data from backend:', response.data?.sorted_tweets?.slice(0, 5)); 
        const sortedData = response.data.sorted_tweets;

        // if the sorted data is valid, update the state
        if (sortedData && Array.isArray(sortedData)) {
            console.log(`Feed: Setting ${sortedData.length} sorted posts`);
            
            // update the display posts
            setDisplayPosts([]);
            
            setAllPosts(sortedData);
              
            const postsPerPage = 20;
            setTimeout(() => {
              if (isMounted.current) {
                setDisplayPosts(sortedData.slice(0, postsPerPage));
                setPage(1);
                setHasMore(sortedData.length > postsPerPage);
                setSortTime(response.data.sort_time_ms);
                console.log('Feed: Display updated with sorted posts');
              }
            }, 0);
        } else {
            console.error('Feed: Received invalid sorted data format from backend');
            setError('Received invalid sorted data format from backend.');
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

  // function to load more posts
  const handleLoadMore = () => {
    if (!loadingMore && !loadingSort && hasMore) {
      const postsPerPage = 20;
      const nextPage = page + 1;
      const startIndex = (nextPage - 1) * postsPerPage;
      const endIndex = startIndex + postsPerPage;
      
      setDisplayPosts(prevPosts => [
        ...prevPosts,
        ...allPosts.slice(startIndex, endIndex)
      ]);
      
      setPage(nextPage);
      
      if (endIndex >= allPosts.length) {
        setHasMore(false);
      }
    }
  };

  // if the posts are loading, display a loading message
  if (loading && displayPosts.length === 0) {
    return <div className="loading">Loading posts...</div>;
  }

  // if there is an error, display an error message
  if (error && displayPosts.length === 0) { 
    return <div className="error">Error: {error}</div>;
  }

  // log the component state    
  console.log(`Feed: Rendering component. loading=${loading}, loadingSort=${loadingSort}. Displaying ${displayPosts.length} posts.`);

  return (
    // main div for the feed  
    <div className="feed">
      {/* header for the feed */}
      <div className="feed-header">
        <h2>Home</h2>
        {loadingSort && <div className="loading-sort">Sorting...</div>}
        {error && !loadingSort && <div className="error feed-error">Error: {error}</div>} 
      </div>

      {/* div for the posts */}
      <div className="posts">
        {displayPosts.map((post, index) => (
          <Post key={`${post.id}-${index}`} post={post} />
        ))}
      </div>

      {/* div for the loading more posts */}
      {loadingMore && <div className="loading">Loading more posts...</div>}

      {/* div for the load more button */}
      {!loadingSort && !loadingMore && hasMore && (
        <div className="load-more">
          <button onClick={handleLoadMore} disabled={loadingMore || loadingSort}>
            Load More
          </button>
        </div>
      )}

    </div>
  );
};

export default Feed; 