import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import BlogApp from './BlogApp'; // this is the renamed MUI Blog App
import Home from './Home'; // or whatever your main page is

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/blog" element={<BlogApp />} />
      </Routes>
    </Router>
  );
}

export default App;