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
      setLoading(true);
      try {
        const response = await import('../data/twitter_sample_100k.json');
        const data = response.default;

        const postsPerPage = 20;
        const startIndex = (page - 1) * postsPerPage;
        const endIndex = startIndex + postsPerPage;
        const newPostsRaw = data.slice(startIndex, endIndex);

        if (newPostsRaw.length === 0) {
          setHasMore(false);
        } else {
          const newPosts = newPostsRaw.map(rawPost => ({
            id: String(rawPost.id),
            username: rawPost.user,
            displayName: rawPost.user,
            content: rawPost.tweet,
            timestamp: rawPost.date,
            likes: parseInt(rawPost.likes) || 0,
            retweets: parseInt(rawPost.retweets) || 0,
            replies: parseInt(rawPost.replies) || 0,
          }));

          const validPosts = newPosts.filter(p => p.id && p.username && p.content && p.timestamp);

          setPosts(prevPosts => [...prevPosts, ...validPosts]);
        }

      } catch (err) {
        console.error('Error loading posts:', err);
        setError('Failed to load posts. Please try again later.');
        setHasMore(false);
      } finally {
        setLoading(false);
      }
    };

    if (hasMore) {
      fetchPosts();
    }
  }, [page, hasMore]);

  const handleLoadMore = () => {
    if (!loading) {
      setPage(prevPage => prevPage + 1);
    }
  };

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

      {loading && page > 1 && <div className="loading">Loading more posts...</div>}

      {!loading && hasMore && (
        <div className="load-more">
          <button onClick={handleLoadMore}>Load More</button>
        </div>
      )}

      {!loading && !hasMore && posts.length > 0 && (
        <div className="end-message">You've reached the end of the feed.</div>
      )}
      
      {loading && page === 1 && posts.length === 0 && <div className="loading">Loading posts...</div>}
      {!loading && !hasMore && posts.length === 0 && <div className="end-message">No posts to display.</div>}
    </div>
  );
};

export default Feed; 