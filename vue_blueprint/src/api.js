// src/api.js
import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://localhost:5000/api', // Base URL for your Flask API
  headers: {
    'Content-Type': 'application/json',
  },
});

// Function to ping the server
export const pingServer = async () => {
  try {
    const response = await apiClient.get('/ping');
    return response.data;
  } catch (error) {
    console.error('Error in pingServer:', error);
    throw error;
  }
};

// You can add more API functions here as needed
