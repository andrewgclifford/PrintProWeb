import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import JobDashboard from './components/JobDashboard';
import JobDetails from './components/JobDetails';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<JobDashboard />} />
        <Route path="/job/:jobId" element={<JobDetails />} />
      </Routes>
    </Router>
  );
}

export default App; 