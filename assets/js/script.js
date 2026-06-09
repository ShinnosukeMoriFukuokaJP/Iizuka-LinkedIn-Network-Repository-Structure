/* ================================================
   JavaScript - Minimal, No Dependencies
   ================================================ */

// Set active navigation link based on current page
document.addEventListener('DOMContentLoaded', function() {
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('nav a');
    
    navLinks.forEach(link => {
        const href = link.getAttribute('href');
        // Remove trailing slashes for comparison
        const normalizedHref = href.replace(/\/$/, '');
        const normalizedPath = currentPath.replace(/\/$/, '');
        
        // Handle root path
        if ((href === '/' && normalizedPath === '') || 
            (href !== '/' && normalizedPath.endsWith(normalizedHref))) {
            link.classList.add('active');
        } else {
            link.classList.remove('active');
        }
    });
});

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        const href = this.getAttribute('href');
        if (href !== '#' && document.querySelector(href)) {
            e.preventDefault();
            document.querySelector(href).scrollIntoView({
                behavior: 'smooth'
            });
        }
    });
});

// Add noopener to external links
document.querySelectorAll('a[href^="http"]').forEach(link => {
    link.setAttribute('rel', 'noopener noreferrer');
    link.setAttribute('target', '_blank');
});
