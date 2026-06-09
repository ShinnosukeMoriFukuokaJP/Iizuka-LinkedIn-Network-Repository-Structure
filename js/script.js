// ========================================
// MOBILE NAVIGATION TOGGLE
// ========================================

document.addEventListener('DOMContentLoaded', function() {
  const hamburger = document.getElementById('hamburger');
  const navMenu = document.getElementById('nav-menu');

  if (hamburger && navMenu) {
    hamburger.addEventListener('click', function() {
      hamburger.classList.toggle('active');
      navMenu.classList.toggle('active');
      
      // Update ARIA attribute
      const isExpanded = hamburger.classList.contains('active');
      hamburger.setAttribute('aria-expanded', isExpanded);
    });

    // Close menu when a link is clicked
    const navLinks = navMenu.querySelectorAll('a');
    navLinks.forEach(link => {
      link.addEventListener('click', function() {
        hamburger.classList.remove('active');
        navMenu.classList.remove('active');
        hamburger.setAttribute('aria-expanded', 'false');
      });
    });
  }
});

// ========================================
// LAZY LOADING IMAGES
// ========================================

if ('IntersectionObserver' in window) {
  const images = document.querySelectorAll('img[loading="lazy"]');
  
  const imageObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const img = entry.target;
        img.src = img.dataset.src || img.src;
        img.removeAttribute('loading');
        observer.unobserve(img);
      }
    });
  });

  images.forEach(img => imageObserver.observe(img));
}

// ========================================
// SMOOTH SCROLL FOR ANCHOR LINKS
// ========================================

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
    const href = this.getAttribute('href');
    
    // Only prevent default for internal anchor links
    if (href !== '#' && document.querySelector(href)) {
      e.preventDefault();
      
      const target = document.querySelector(href);
      target.scrollIntoView({
        behavior: 'smooth',
        block: 'start'
      });
    }
  });
});

// ========================================
// FORM SUBMISSION (Contact Page)
// ========================================

const contactForm = document.getElementById('contact-form');
if (contactForm) {
  contactForm.addEventListener('submit', function(e) {
    // Form submission will be handled by formspree.io
    // Add any custom validation here if needed
    
    // Simple validation example
    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const subject = document.getElementById('subject').value.trim();
    const message = document.getElementById('message').value.trim();

    if (!name || !email || !subject || !message) {
      e.preventDefault();
      alert('Please fill in all required fields.');
    }
  });
}

// ========================================
// PERFORMANCE MONITORING
// ========================================

if ('performance' in window && 'PerformanceObserver' in window) {
  // Monitor Largest Contentful Paint (LCP)
  const observer = new PerformanceObserver((list) => {
    const entries = list.getEntries();
    const lastEntry = entries[entries.length - 1];
    
    // Log for monitoring (can be sent to analytics)
    console.log('LCP:', lastEntry.renderTime || lastEntry.loadTime);
  });

  try {
    observer.observe({ type: 'largest-contentful-paint', buffered: true });
  } catch (e) {
    // LCP observer not supported
  }
}

// ========================================
// SCROLL BEHAVIOR TRACKING
// ========================================

let scrollPercentage = 0;

window.addEventListener('scroll', () => {
  const scrollTop = window.scrollY;
  const docHeight = document.documentElement.scrollHeight - window.innerHeight;
  scrollPercentage = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
  
  // Can be used for analytics events
  // console.log('Scroll:', scrollPercentage.toFixed(2) + '%');
});

// ========================================
// ACCESSIBILITY: FOCUS MANAGEMENT
// ========================================

// Ensure focus is visible for keyboard navigation
const style = document.createElement('style');
style.textContent = `
  *:focus {
    outline: 2px solid #3182ce;
    outline-offset: 2px;
  }
  
  *:focus:not(:focus-visible) {
    outline: none;
  }
`;
document.head.appendChild(style);

// ========================================
// UTILITY: DETECT TOUCH DEVICE
// ========================================

function isTouchDevice() {
  return (
    (typeof window !== 'undefined' &&
      ('ontouchstart' in window ||
        (window.DocumentTouch &&
          typeof document !== 'undefined' &&
          document instanceof window.DocumentTouch))) ||
    (typeof navigator !== 'undefined' &&
      (navigator.maxTouchPoints > 0 || navigator.msMaxTouchPoints > 0))
  );
}

// Adjust for touch devices if needed
if (isTouchDevice()) {
  document.body.classList.add('touch-device');
}

// ========================================
// INTERSECTION OBSERVER FOR ANIMATIONS
// ========================================

if ('IntersectionObserver' in window) {
  const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -100px 0px'
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('in-view');
        // Optionally stop observing
        // observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  // Observe all sections
  document.querySelectorAll('section').forEach(section => {
    observer.observe(section);
  });
}

// ========================================
// META VIEWPORT FIX FOR OLDER DEVICES
// ========================================

if (typeof window !== 'undefined') {
  // Ensure viewport meta tag is set correctly
  let viewport = document.querySelector('meta[name="viewport"]');
  if (!viewport) {
    viewport = document.createElement('meta');
    viewport.name = 'viewport';
    viewport.content = 'width=device-width, initial-scale=1.0';
    document.head.appendChild(viewport);
  }
}