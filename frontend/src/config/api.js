// API configuration
export const API_CONFIG = {
  baseUrl: process.env.REACT_APP_API_URL || 'http://localhost:8000',
  timeout: 10000,
};

// Create axios instance with default configuration
import axios from 'axios';

export const api = axios.create({
  baseURL: API_CONFIG.baseUrl,
  timeout: API_CONFIG.timeout,
});

// Add a request interceptor
api.interceptors.request.use(
  (config) => {
    // Add any common headers or modifications here
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Add a response interceptor
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response) {
      // The request was made and the server responded with a status code
      // that falls out of the range of 2xx
      console.error('API Error:', error.response.data);
    } else if (error.request) {
      // The request was made but no response was received
      console.error('No response received:', error.request);
    } else {
      // Something happened in setting up the request that triggered an Error
      console.error('Error:', error.message);
    }
    return Promise.reject(error);
  }
);
