import React from 'react';
import { Link } from 'react-router-dom';
import '../styles/Header.css';

const Header = () => {
  return (
    <header className="header">
      <div className="header-container">
        {/*Logo/home link*/}
        <Link to="/" className="logo">
          <h1>Twitter Feed</h1>
        </Link>
        
        {/*nav menu*/}
        <nav className="nav">
          <Link to="/" className="nav-link">Home</Link>
        </nav>
      </div>
    </header>
  );
};

export default Header; 