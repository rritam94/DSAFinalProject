import React from 'react';
import '../styles/Post.css';

//the individul tweet component
const Post = ({ post }) => {
  const { id, username, displayName, content, timestamp, likes, retweets, replies } = post;

  //convert timestamp into a readable date
  const formatDate = (timestamp) => {
    const date = new Date(timestamp);
    return date.toLocaleString('en-US', { 
      month: 'short', 
      day: 'numeric',
      year: 'numeric',
      hour: 'numeric',
      minute: '2-digit'
    });
  };

  return (
    <div className="post">
      {/*avatar*/}
      <div className="post-avatar">
        <img 
          src={`https://api.dicebear.com/7.x/initials/svg?seed=${username}`} 
          alt={`${displayName}'s avatar`} 
        />
      </div>
      <div className="post-content">
        {/*User info*/}
        <div className="post-header">
          <span className="post-display-name">{displayName}</span>
          <span className="post-username">@{username}</span>
          <span className="post-time">{formatDate(timestamp)}</span>
        </div>
        {/*Post content*/}
        <div className="post-text">{content}</div>
        {/*metrics*/}
        <div className="post-actions">
          <div className="post-action">
            <span className="action-icon">💬</span>
            <span>{replies}</span>
          </div>
          <div className="post-action">
            <span className="action-icon">🔄</span>
            <span>{retweets}</span>
          </div>
          <div className="post-action">
            <span className="action-icon">❤️</span>
            <span>{likes}</span>
          </div>
          <div className="post-action">
            <span className="action-icon">📤</span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Post; 