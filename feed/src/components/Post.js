import React from 'react';
import '../styles/Post.css';

const Post = ({ post }) => {
  // get the post data
  const { id, username, displayName, content, timestamp, likes, retweets, replies } = post;

  // format the date
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

  // return the post component
  return (
    <div className="post">
      <div className="post-avatar">
        <img 
          src={`https://api.dicebear.com/7.x/initials/svg?seed=${username}`} 
          alt={`${displayName}'s avatar`} 
        />
      </div>
      <div className="post-content">
        <div className="post-header">
          <span className="post-display-name">{displayName}</span>
          <span className="post-username">@{username}</span>
          <span className="post-time">{formatDate(timestamp)}</span>
        </div>
        <div className="post-text">{content}</div>
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