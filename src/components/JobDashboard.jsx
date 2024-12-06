import React, { useState, useEffect } from 'react';
import axios from 'axios';

const JobDashboard = () => {
  const [jobs, setJobs] = useState([]);
  const [loading, setLoading] = useState(true);
  const [filters, setFilters] = useState({
    status: '',
    priority: '',
    search: '',
    dateRange: {
      start: '',
      end: ''
    }
  });

  useEffect(() => {
    fetchJobs();
  }, [filters]);

  const fetchJobs = async () => {
    try {
      const params = new URLSearchParams(filters).toString();
      const response = await axios.get(`/api/jobs/?${params}`);
      setJobs(response.data);
      setLoading(false);
    } catch (error) {
      console.error('Error fetching jobs:', error);
      setLoading(false);
    }
  };

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Job Dashboard</h1>
      
      {/* Filters */}
      <div className="mb-4 flex gap-4">
        <input
          type="text"
          placeholder="Search jobs..."
          value={filters.search}
          onChange={(e) => setFilters({...filters, search: e.target.value})}
          className="border p-2 rounded"
        />
        
        <input
          type="date"
          value={filters.dateRange.start}
          onChange={(e) => setFilters({
            ...filters,
            dateRange: {...filters.dateRange, start: e.target.value}
          })}
          className="border p-2 rounded"
        />
        
        <input
          type="date"
          value={filters.dateRange.end}
          onChange={(e) => setFilters({
            ...filters,
            dateRange: {...filters.dateRange, end: e.target.value}
          })}
          className="border p-2 rounded"
        />
        
        <select
          value={filters.status}
          onChange={(e) => setFilters({...filters, status: e.target.value})}
          className="border p-2 rounded"
        >
          <option value="">All Statuses</option>
          <option value="pending">Pending</option>
          <option value="prepress">Pre-press</option>
          <option value="printing">Printing</option>
          <option value="finishing">Finishing</option>
          <option value="delivered">Delivered</option>
        </select>

        <select
          value={filters.priority}
          onChange={(e) => setFilters({...filters, priority: e.target.value})}
          className="border p-2 rounded"
        >
          <option value="">All Priorities</option>
          <option value="low">Low</option>
          <option value="medium">Medium</option>
          <option value="high">High</option>
          <option value="urgent">Urgent</option>
        </select>
      </div>

      {/* Jobs List */}
      {loading ? (
        <div>Loading...</div>
      ) : (
        <div className="grid gap-4">
          {jobs.map(job => (
            <div 
              key={job.id} 
              className="border p-4 rounded shadow hover:shadow-lg transition-shadow"
            >
              <div className="flex justify-between items-start">
                <div>
                  <h2 className="text-xl font-semibold">{job.title}</h2>
                  <p className="text-gray-600">#{job.job_number}</p>
                </div>
                <div className="flex gap-2">
                  <span className={`px-2 py-1 rounded text-sm ${
                    job.priority === 'urgent' ? 'bg-red-100 text-red-800' :
                    job.priority === 'high' ? 'bg-orange-100 text-orange-800' :
                    job.priority === 'medium' ? 'bg-blue-100 text-blue-800' :
                    'bg-gray-100 text-gray-800'
                  }`}>
                    {job.priority}
                  </span>
                  <span className="px-2 py-1 rounded bg-gray-100 text-gray-800 text-sm">
                    {job.status}
                  </span>
                </div>
              </div>
              <p className="mt-2 text-gray-600">{job.description}</p>
              <div className="mt-4 text-sm text-gray-500">
                Deadline: {new Date(job.deadline).toLocaleDateString()}
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default JobDashboard; 