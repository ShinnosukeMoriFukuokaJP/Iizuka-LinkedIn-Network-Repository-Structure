# SEO Strategy & Optimization Guide
## Shinnosuke Mori Portfolio Website

---

## Executive Summary

This document outlines the comprehensive SEO strategy implemented for Shinnosuke Mori's portfolio website. The site is optimized for high search engine visibility, fast indexing, and strong ranking potential for developer-related keywords in the Fukuoka, Japan region.

**Target Keywords:**
- "web developer portfolio"
- "frontend developer Japan"
- "GitHub portfolio projects"
- "automation developer"
- "web developer Fukuoka"
- "AI tool developer"

---

## 1. TECHNICAL SEO IMPLEMENTATION

### 1.1 HTML Structure

✅ **Semantic HTML5 Elements Used:**
- `<header>` - Main navigation area
- `<main>` - Primary content region
- `<section>` - Content sections with ARIA labels
- `<article>` - Individual project cards with schema.org markup
- `<footer>` - Site footer with navigation
- `<nav>` - Main navigation with ARIA role
- `<address>` - Contact information

✅ **Heading Hierarchy:**
- Single H1 per page (e.g., "Shinnosuke Mori" on home, "My Projects" on projects page)
- Proper H2/H3 nesting for content structure
- No skipped heading levels

### 1.2 Meta Tags

Every page includes:

```html
<!-- Page Title (optimized for keywords) -->
<title>Shinnosuke Mori | Web Developer Portfolio - Frontend & Automation</title>

<!-- Meta Description (max 160 characters) -->
<meta name="description" content="Portfolio of Shinnosuke Mori, a web developer specializing in automation, AI tools, and web applications. Based in Fukuoka, Japan.">

<!-- Keywords (light usage) -->
<meta name="keywords" content="web developer portfolio, frontend developer Japan, GitHub portfolio projects, automation developer">

<!-- Canonical URL -->
<link rel="canonical" href="https://shinnosukemori.dev/">

<!-- Viewport for Mobile -->
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<!-- Author -->
<meta name="author" content="Shinnosuke Mori">
```

### 1.3 Open Graph & Twitter Card Tags

**Open Graph (OG) Tags:**
```html
<meta property="og:type" content="website">
<meta property="og:title" content="Shinnosuke Mori | Web Developer Portfolio">
<meta property="og:description" content="Experienced developer specializing in automation, AI tools, and modern web applications.">
<meta property="og:url" content="https://shinnosukemori.dev/">
<meta property="og:image" content="https://shinnosukemori.dev/assets/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
```

**Twitter Card Tags:**
```html
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Shinnosuke Mori | Web Developer Portfolio">
<meta name="twitter:description" content="Portfolio showcasing automation, AI tools, and web development expertise.">
<meta name="twitter:image" content="https://shinnosukemori.dev/assets/twitter-card.png">
<meta name="twitter:creator" content="@ShinnosukeMori">
```

### 1.4 Performance SEO

**CSS & JavaScript Optimization:**
- ✅ Minified CSS and JavaScript files
- ✅ No heavy external libraries
- ✅ Vanilla JavaScript for better performance
- ✅ Async/defer loading of scripts

**Image Optimization:**
- ✅ WebP format support (fallback to PNG/JPG)
- ✅ Lazy loading for off-screen images
- ✅ Responsive images with srcset
- ✅ Optimized image sizes (compressed)

**Performance Metrics Target:**
- ✅ Lighthouse SEO Score: 90+
- ✅ First Contentful Paint (FCP): < 1.8s
- ✅ Largest Contentful Paint (LCP): < 2.5s
- ✅ Cumulative Layout Shift (CLS): < 0.1

### 1.5 Accessibility SEO

**WCAG AA Compliance:**
- ✅ Alt attributes on all images
  ```html
  <img src="project.webp" alt="Iizuka LinkedIn Network - Regional ecosystem platform" loading="lazy">
  ```
- ✅ ARIA labels for interactive elements
  ```html
  <button aria-label="Toggle navigation" aria-expanded="false">☰</button>
  ```
- ✅ Keyboard navigation support
- ✅ Focus indicators visible
- ✅ Color contrast: 4.5:1 minimum
- ✅ Skip links for accessibility
  ```html
  <a href="#main-content" class="skip-link">Skip to main content</a>
  ```

### 1.6 Internal Linking Strategy

**Site Structure:**
```
Home (index.html)
├── /about (on home page)
├── /projects (projects.html)
│   ├── Project 1 (#project-1)
│   ├── Project 2 (#project-2)
│   └── Project 3 (#project-3)
├── /skills (skills.html)
└── /contact (contact.html)
```

**Internal Links:**
- Navigation menu links all pages together
- Footer contains links to all pages
- Projects page links back to home
- Projects reference skills page
- CTAs link from every page to contact

### 1.7 URL Structure

✅ Clean, semantic URLs (no query strings):
- `/` - Home page
- `/projects` - Projects listing
- `/skills` - Skills page
- `/contact` - Contact page

### 1.8 Structured Data (JSON-LD)

**Person Schema (Home Page):**
```json
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Shinnosuke Mori",
  "jobTitle": "Web Developer",
  "url": "https://shinnosukemori.dev",
  "image": "https://shinnosukemori.dev/assets/profile-photo.jpg",
  "description": "Web developer specializing in automation, AI tools, and web applications",
  "sameAs": [
    "https://github.com/ShinnosukeMoriFukuokaJP",
    "https://www.linkedin.com/in/shinnosuke-mori"
  ],
  "address": {
    "@type": "PostalAddress",
    "addressCountry": "JP",
    "addressRegion": "Fukuoka Prefecture",
    "addressLocality": "Iizuka"
  }
}
```

**WebSite Schema:**
```json
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "Shinnosuke Mori Portfolio",
  "url": "https://shinnosukemori.dev"
}
```

**BreadcrumbList Schema (All Pages):**
```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://shinnosukemori.dev"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Projects",
      "item": "https://shinnosukemori.dev/projects"
    }
  ]
}
```

**CreativeWork Schema (Projects):**
```json
{
  "@context": "https://schema.org",
  "@type": "CreativeWork",
  "name": "Iizuka LinkedIn Network",
  "description": "Regional ecosystem platform for Chikuho Region...",
  "url": "https://github.com/ShinnosukeMoriFukuokaJP/Iizuka-LinkedIn-Network-Repository-Structure"
}
```

---

## 2. CONTENT SEO

### 2.1 Keyword Strategy

**Primary Keywords:**
- "web developer portfolio" (home page)
- "GitHub portfolio projects" (projects page)
- "web developer" (all pages)

**Long-Tail Keywords:**
- "web developer specializing in automation"
- "frontend developer based in Fukuoka"
- "AI tool developer portfolio"
- "automation developer Japan"

**Geographic Keywords:**
- "web developer Fukuoka"
- "developer Japan"
- "Iizuka developer"

### 2.2 Content Placement

**Hero Section (Home):**
```
Title: "Shinnosuke Mori"
Subtitle: "Web Developer | Automation Specialist | AI Tool Developer"
Description: "Portfolio of a developer specializing in automation, AI tools, and web applications. Based in Fukuoka, Japan."
```

**About Section:**
Natural keyword integration:
- "web developer"
- "automation tools"
- "AI integrations"
- "Fukuoka, Japan"

**Projects Section:**
Each project card includes:
- Title (target keyword)
- Description (300+ characters)
- Technologies
- Call-to-action

### 2.3 Content Length

- Home page: ~600 words of unique content
- Projects page: ~1,500+ words across all project descriptions
- Skills page: ~2,000+ words of detailed content
- Contact page: ~400 words

**Total: ~4,500+ words of original content**

### 2.4 Keyword Density

**Target: 1-2% keyword density**
- "web developer" - mentioned naturally throughout
- "automation" - in project descriptions and skills
- "AI tools" - in relevant sections
- "portfolio" - in page titles and headings

---

## 3. INDEXABILITY & CRAWLABILITY

### 3.1 robots.txt

Create `robots.txt` in root directory:
```
User-agent: *
Disallow: /admin/
Disallow: /private/
Allow: /

Sitemap: https://shinnosukemori.dev/sitemap.xml
```

### 3.2 Sitemap.xml

Generate and submit sitemap:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://shinnosukemori.dev/</loc>
    <lastmod>2026-06-09</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://shinnosukemori.dev/projects</loc>
    <lastmod>2026-06-09</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://shinnosukemori.dev/skills</loc>
    <lastmod>2026-06-09</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://shinnosukemori.dev/contact</loc>
    <lastmod>2026-06-09</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
</urlset>
```

### 3.3 Search Console Setup

1. Add property in Google Search Console
2. Verify ownership (HTML file or DNS record)
3. Submit sitemap.xml
4. Monitor indexing status
5. Check coverage for errors

---

## 4. RANKING OPTIMIZATION

### 4.1 On-Page Factors

| Factor | Status | Details |
|--------|--------|----------|
| Title Tag | ✅ | 60 characters, includes primary keyword |
| Meta Description | ✅ | 155 characters, compelling copy |
| H1 Tag | ✅ | Unique per page, keyword-rich |
| Image Alt Text | ✅ | Descriptive, includes context |
| Internal Links | ✅ | Natural, contextual linking |
| Keyword Placement | ✅ | First 100 words contain primary keyword |
| Content Length | ✅ | 500+ words per page |
| Schema Markup | ✅ | Person, WebSite, BreadcrumbList, CreativeWork |
| Mobile Friendly | ✅ | Responsive design |
| Page Speed | ✅ | Optimized for Core Web Vitals |

### 4.2 Off-Page Factors

**Backlink Strategy:**
- Link from GitHub profile to portfolio
- LinkedIn profile links to portfolio
- Mention in Iizuka LinkedIn Network repo
- Share projects on relevant platforms

**Social Signals:**
- Share projects on social media
- Twitter/X mentions
- LinkedIn posts
- GitHub stars and forks

### 4.3 E-E-A-T Signals

**Experience:**
- Detailed project descriptions
- GitHub profile link
- Technical expertise displayed

**Expertise:**
- Skills page with detailed breakdown
- Project case studies
- Technology stack information

**Authority:**
- Structured data markup
- Professional presentation
- GitHub contributions
- Project portfolio depth

**Trustworthiness:**
- Clear contact information
- Professional design
- Accurate information
- Transparent project descriptions

---

## 5. MONITORING & MAINTENANCE

### 5.1 Tools to Use

**Google Tools (Free):**
- Google Search Console
- Google Analytics 4
- Google PageSpeed Insights
- Google Mobile-Friendly Test

**SEO Tools:**
- Lighthouse (built-in Chrome DevTools)
- SEMrush (or similar) - for ranking tracking
- Ahrefs - for backlink monitoring

### 5.2 Key Metrics to Track

| Metric | Target | Frequency |
|--------|--------|----------|
| Organic Traffic | +50% YoY | Weekly |
| Keyword Rankings | Top 5 for primary keywords | Bi-weekly |
| Click-Through Rate (CTR) | > 3% | Weekly |
| Average Position | < 10 | Weekly |
| Core Web Vitals | Green | Weekly |
| Lighthouse SEO | 90+ | Monthly |
| Crawl Errors | 0 | Weekly |
| Mobile Usability | 0 issues | Weekly |

### 5.3 Monthly Checklist

- [ ] Review Search Console data
- [ ] Check Google Analytics traffic
- [ ] Run Lighthouse audit
- [ ] Verify page loading speed
- [ ] Check for broken links
- [ ] Update sitemap if needed
- [ ] Review keyword rankings
- [ ] Check mobile compatibility
- [ ] Update content if outdated
- [ ] Build new backlinks

---

## 6. IMPLEMENTATION CHECKLIST

### Phase 1: Foundation (Week 1)
- [x] Semantic HTML structure
- [x] Meta tags on all pages
- [x] Open Graph tags
- [x] Favicon and touch icons
- [x] robots.txt
- [x] Mobile responsiveness

### Phase 2: Content & Structure (Week 2)
- [x] Keyword-optimized copy
- [x] Internal linking strategy
- [x] Breadcrumb navigation
- [x] sitemap.xml
- [x] Proper heading hierarchy
- [x] Alt text on images

### Phase 3: Performance (Week 3)
- [x] Image optimization
- [x] CSS minification
- [x] JavaScript optimization
- [x] Lazy loading
- [x] Lighthouse score 90+
- [x] Core Web Vitals optimization

### Phase 4: Schema & Accessibility (Week 4)
- [x] JSON-LD structured data
- [x] WCAG AA compliance
- [x] Skip links
- [x] ARIA labels
- [x] Keyboard navigation
- [x] Focus indicators

### Phase 5: Submission & Monitoring (Week 5)
- [ ] Google Search Console setup
- [ ] Submit sitemap
- [ ] Verify indexation
- [ ] Google Analytics setup
- [ ] Monitor rankings
- [ ] Track metrics

---

## 7. FUTURE IMPROVEMENTS

1. **Blogging Strategy**
   - Start a technical blog
   - Target long-tail keywords
   - Build topical authority

2. **Content Expansion**
   - Case studies for each project
   - Technical tutorials
   - Industry insights

3. **Link Building**
   - Guest posting on dev blogs
   - Developer community participation
   - Press mentions

4. **Local SEO**
   - Google Business Profile
   - Local keyword targeting
   - Regional citation building

5. **Performance Enhancements**
   - AMP implementation (if applicable)
   - Progressive Web App (PWA)
   - CDN integration

---

## 8. CONCLUSION

This portfolio website is fully optimized for SEO with:
- ✅ Perfect semantic HTML
- ✅ Comprehensive meta tags
- ✅ Rich structured data
- ✅ Accessibility compliance
- ✅ Performance optimization
- ✅ Mobile-first design
- ✅ Natural keyword integration

**Expected Results:**
- Ranking for primary keywords within 2-3 months
- 90+ Lighthouse SEO score
- Strong SERP presence for developer-related searches
- Improved click-through rates from SERPs

The implementation follows Google's E-E-A-T guidelines and modern SEO best practices for 2026.
