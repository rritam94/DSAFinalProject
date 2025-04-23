import React from 'react';
import { Link } from 'react-router-dom';
import '../styles/Header.css';

const Header = () => {
  return (
    // header for the feed
    <header className="header">
      <div className="header-container">
        <Link to="/" className="logo">
          <h1>Twitter Feed</h1>
        </Link>
      </div>
    </header>
  );
};

export default Header; 