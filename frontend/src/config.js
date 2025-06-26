const API_BASE_URL = import.meta.env.VITE_API_URL || (
  window.location.hostname === 'localhost' 
    ? 'http://localhost:5000/api'
    : `https://${window.location.hostname}/api`
);

export const API_CONFIG = {
  BASE_URL: API_BASE_URL,
  ENDPOINTS: {
    SCRAPING_STATUS: '/scraping/status',
    SCRAPING_RUN: '/scraping/run',
    SCRAPING_RESULTS: '/scraping/results',
    SCRAPING_SOURCES: '/scraping/sources',
    SCRAPING_STATS: '/scraping/stats',
    AUTH_STATUS: '/auth/status',
    AUTH_LOGIN: '/auth/google/login',
    HEALTH: '/health'
  }
};

// Helper function for API calls
export const apiCall = async (endpoint, options = {}) => {
  const url = `${API_BASE_URL}${endpoint}`;
  const defaultOptions = {
    headers: {
      'Content-Type': 'application/json',
    },
    credentials: 'include', // Pour les cookies de session
  };

  const finalOptions = { ...defaultOptions, ...options };

  try {
    const response = await fetch(url, finalOptions);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error('API call failed:', error);
    throw error;
  }
};