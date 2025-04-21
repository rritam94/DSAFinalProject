import React, { useState, useEffect } from 'react';
import Post from './Post';
import '../styles/Feed.css';

const Feed = () => {
  const [posts, setPosts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [page, setPage] = useState(1);
  const [hasMore, setHasMore] = useState(true);

  useEffect(() => {
    const fetchPosts = async () => {
      try {
        const response = await import('../data/tweets.json');
        const data = response.default;

        const postsPerPage = 20;
        const startIndex = (page - 1) * postsPerPage;
        const endIndex = startIndex + postsPerPage;
        const newPosts = data.slice(startIndex, endIndex);
        
        if (newPosts.length === 0) {
          setHasMore(false);
        } else {
          setPosts(prevPosts => [...prevPosts, ...newPosts]);
        }
        
        setLoading(false);
      } catch (err) {
        console.error('Error loading posts:', err);
        setError('Failed to load posts. Please try again later.');
        setLoading(false);
      }
    };

    if (hasMore) {
      fetchPosts();
    }
  }, [page, hasMore]);

  const handleLoadMore = () => {
    setPage(prevPage => prevPage + 1);
  };

  if (loading && page === 1) {
    return <div className="loading">Loading posts...</div>;
  }

  if (error) {
    return <div className="error">{error}</div>;
  }

  return (
    <div className="feed">
      <div className="feed-header">
        <h2>Home</h2>
      </div>
      
      <div className="posts">
        {posts.map(post => (
          <Post key={post.id} post={post} />
        ))}
      </div>
      
      {loading && <div className="loading">Loading more posts...</div>}
      
      {!loading && hasMore && (
        <div className="load-more">
          <button onClick={handleLoadMore}>Load More</button>
        </div>
      )}
      
      {!hasMore && (
        <div className="end-message">You've reached the end of the feed.</div>
      )}
    </div>
  );
};

export default Feed; 