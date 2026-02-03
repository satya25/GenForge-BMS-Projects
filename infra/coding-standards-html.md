 
# Coding Standards: HTML

## Overview
These standards define how HTML should be written and maintained across all GenForge projects. They ensure clarity, accessibility, and maintainability of markup, while aligning with modern web development best practices.

## General Principles
- Follow **HTML5** standards.
- Write **semantic HTML** (use `<header>`, `<nav>`, `<section>`, `<article>`, `<footer>` appropriately).
- Ensure **accessibility** (WCAG compliance).
- Keep markup clean and minimal; avoid unnecessary tags.

---

## Naming Conventions
- **IDs**: `camelCase` (e.g., `mainHeader`, `footerSection`).
- **Classes**: `kebab-case` (e.g., `user-profile-card`, `nav-bar`).
- **Files**: descriptive lowercase with hyphens (e.g., `dashboard-page.html`).

---

## Code Structure
- **Indentation**: 2 spaces.
- **Line Length**: max 100 characters.
- **Attributes**: always use lowercase and double quotes (`class="nav-bar"`).
- **Comments**: use `<!-- ... -->` for section headers and explanations.

Example:
```html
<!-- User Profile Section -->
<section class="user-profile-card">
  <h2>User Profile</h2>
  <p id="userEmail">Email: example@domain.com</p>
</section>
```

---

## Accessibility Standards
- Always provide `alt` text for images.
- Use proper heading hierarchy (`<h1>` → `<h2>` → `<h3>`).
- Ensure sufficient color contrast (defined in CSS standards).
- Use ARIA attributes where necessary for dynamic content.

---

## Best Practices
- Separate structure (HTML), style (CSS), and behavior (JS).
- Avoid inline styles and inline JavaScript.
- Validate HTML with W3C validator.
- Use descriptive titles and meta tags for SEO.
- Ensure forms have labels and proper input types.

---

## Security Standards
- Escape dynamic content before rendering.
- Use HTTPS for all linked resources.
- Avoid exposing sensitive data in hidden fields.

---

## Future Enhancements
- Automated linting with **HTMLHint**.
- Accessibility audits with tools like **axe-core**.
- Continuous integration checks for HTML validation.
 