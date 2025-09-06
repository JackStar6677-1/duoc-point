// PWA Installation
let deferredPrompt;
const installBtn = document.getElementById('install-button');

if (installBtn) {
  window.addEventListener('beforeinstallprompt', (e) => {
    e.preventDefault();
    deferredPrompt = e;
    installBtn.style.display = 'block';
  });

  installBtn.addEventListener('click', async () => {
    if (deferredPrompt) {
      deferredPrompt.prompt();
      const { outcome } = await deferredPrompt.userChoice;
      console.log(`User response to the install prompt: ${outcome}`);
      deferredPrompt = null;
      installBtn.style.display = 'none';
    }
  });
}

// Service Worker Registration
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('/sw.js')
    .then((registration) => {
      console.log('Service Worker registrado exitosamente:', registration);
    })
    .catch((error) => {
      console.log('Error al registrar Service Worker:', error);
    });
}

// Authentication helpers
function getAuthToken() {
  return localStorage.getItem('access_token');
}

function setAuthToken(token) {
  localStorage.setItem('access_token', token);
}

function removeAuthToken() {
  localStorage.removeItem('access_token');
  localStorage.removeItem('refresh_token');
  localStorage.removeItem('user_email');
}

function isAuthenticated() {
  return !!getAuthToken();
}

function logout() {
  removeAuthToken();
  window.location.href = '/login.html';
}

// API helper
async function apiRequest(url, options = {}) {
  const token = getAuthToken();
  const defaultOptions = {
    headers: {
      'Content-Type': 'application/json',
      ...(token && { 'Authorization': `Bearer ${token}` })
    }
  };
  
  const finalOptions = { ...defaultOptions, ...options };
  
  try {
    const response = await fetch(url, finalOptions);
    
    if (response.status === 401) {
      // Token expirado, redirigir al login
      logout();
      return null;
    }
    
    return response;
  } catch (error) {
    console.error('Error en API request:', error);
    throw error;
  }
}

// Navigation helpers
function showLoginRequired() {
  if (!isAuthenticated()) {
    window.location.href = '/login.html';
    return true;
  }
  return false;
}

// Initialize app
document.addEventListener('DOMContentLoaded', function() {
  // Check authentication status
  const currentPath = window.location.pathname;
  const protectedPaths = ['/forum/', '/market/', '/portfolio/', '/streetview/'];
  
  if (protectedPaths.some(path => currentPath.includes(path))) {
    if (showLoginRequired()) {
      return;
    }
  }
  
  // Update navigation based on auth status
  updateNavigation();
});

function updateNavigation() {
  const isLoggedIn = isAuthenticated();
  const userEmail = localStorage.getItem('user_email');
  
  // Update login/logout links
  const loginLinks = document.querySelectorAll('.login-link');
  const logoutLinks = document.querySelectorAll('.logout-link');
  const userInfo = document.querySelector('.user-info');
  
  loginLinks.forEach(link => {
    link.style.display = isLoggedIn ? 'none' : 'block';
  });
  
  logoutLinks.forEach(link => {
    link.style.display = isLoggedIn ? 'block' : 'none';
  });
  
  if (userInfo && userEmail) {
    userInfo.textContent = userEmail;
    userInfo.style.display = 'block';
  }
}
