import React, { useState, useEffect } from 'react';
import axios from 'axios';

const JobDetails = ({ jobId }) => {
  const [job, setJob] = useState(null);
  const [comment, setComment] = useState('');
  const [files, setFiles] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchJobDetails();
  }, [jobId]);

  const fetchJobDetails = async () => {
    try {
      const response = await axios.get(`/api/jobs/${jobId}/`);
      setJob(response.data);
      setLoading(false);
    } catch (error) {
      console.error('Error fetching job details:', error);
      setLoading(false);
    }
  };

  const handleFileUpload = async (event) => {
    const file = event.target.files[0];
    const formData = new FormData();
    formData.append('file', file);
    formData.append('file_type', file.type);

    try {
      await axios.post(`/api/jobs/${jobId}/upload_file/`, formData);
      fetchJobDetails();
    } catch (error) {
      console.error('Error uploading file:', error);
    }
  };

  const handleAddComment = async () => {
    try {
      await axios.post(`/api/jobs/${jobId}/add_comment/`, {
        content: comment
      });
      setComment('');
      fetchJobDetails();
    } catch (error) {
      console.error('Error adding comment:', error);
    }
  };

  const handleStatusUpdate = async (newStatus) => {
    try {
      await axios.post(`/api/jobs/${jobId}/update_status/`, {
        status: newStatus
      });
      fetchJobDetails();
    } catch (error) {
      console.error('Error updating status:', error);
    }
  };

  if (loading) return <div>Loading...</div>;
  if (!job) return <div>Job not found</div>;

  return (
    <div className="container mx-auto p-4">
      <div className="bg-white shadow-lg rounded-lg p-6">
        <div className="flex justify-between items-start mb-6">
          <div>
            <h1 className="text-3xl font-bold">{job.title}</h1>
            <p className="text-gray-600">#{job.job_number}</p>
          </div>
          <div className="flex gap-2">
            <span className={`px-3 py-1 rounded-full text-sm ${
              job.priority === 'urgent' ? 'bg-red-100 text-red-800' :
              job.priority === 'high' ? 'bg-orange-100 text-orange-800' :
              'bg-blue-100 text-blue-800'
            }`}>
              {job.priority}
            </span>
            <span className="px-3 py-1 rounded-full bg-gray-100 text-gray-800 text-sm">
              {job.status}
            </span>
          </div>
        </div>

        {/* Job Details */}
        <div className="grid grid-cols-2 gap-4 mb-6">
          <div>
            <h2 className="font-semibold">Client</h2>
            <p>{job.client_name}</p>
          </div>
          <div>
            <h2 className="font-semibold">Assigned To</h2>
            <p>{job.assigned_to_name}</p>
          </div>
          <div>
            <h2 className="font-semibold">Job Type</h2>
            <p>{job.job_type}</p>
          </div>
          <div>
            <h2 className="font-semibold">Quantity</h2>
            <p>{job.quantity}</p>
          </div>
        </div>

        {/* File Upload */}
        <div className="mb-6">
          <h2 className="text-xl font-semibold mb-3">Files</h2>
          <input
            type="file"
            onChange={handleFileUpload}
            className="block w-full text-sm text-gray-500
              file:mr-4 file:py-2 file:px-4
              file:rounded-full file:border-0
              file:text-sm file:font-semibold
              file:bg-blue-50 file:text-blue-700
              hover:file:bg-blue-100"
          />
          <div className="mt-3 space-y-2">
            {job.files?.map(file => (
              <div key={file.id} className="flex items-center gap-2">
                <a href={file.file} className="text-blue-600 hover:underline">
                  {file.file.split('/').pop()}
                </a>
                <span className="text-sm text-gray-500">
                  ({new Date(file.uploaded_at).toLocaleDateString()})
                </span>
              </div>
            ))}
          </div>
        </div>

        {/* Comments */}
        <div className="mb-6">
          <h2 className="text-xl font-semibold mb-3">Comments</h2>
          <div className="space-y-4 mb-4">
            {job.comments?.map(comment => (
              <div key={comment.id} className="bg-gray-50 p-3 rounded">
                <div className="flex justify-between">
                  <span className="font-semibold">{comment.user_name}</span>
                  <span className="text-sm text-gray-500">
                    {new Date(comment.created_at).toLocaleString()}
                  </span>
                </div>
                <p className="mt-1">{comment.content}</p>
              </div>
            ))}
          </div>
          <div className="flex gap-2">
            <input
              type="text"
              value={comment}
              onChange={(e) => setComment(e.target.value)}
              className="flex-1 border rounded p-2"
              placeholder="Add a comment..."
            />
            <button
              onClick={handleAddComment}
              className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
            >
              Add Comment
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default JobDetails; 