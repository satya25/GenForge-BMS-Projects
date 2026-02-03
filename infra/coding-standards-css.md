H
# Coding Standards: CSS

## Overview
These standards define how CSS should be written and maintained across all GenForge projects. They ensure consistency, readability, and maintainability of styles, while aligning with modern best practices.

## General Principles
- Use **external stylesheets**; avoid inline styles.
- Follow a **mobile-first** approach for responsive design.
- Keep styles modular and reusable.
- Prefer **class selectors** over IDs for styling.

---

## Naming Conventions
- **Classes**: `kebab-case` (e.g., `user-profile-card`, `nav-bar`).
- **IDs**: `camelCase` (e.g., `mainHeader`, `footerSection`).
- **Variables (CSS custom properties)**: `--kebab-case` (e.g., `--primary-color`).
- **Files**: descriptive lowercase with hyphens (e.g., `dashboard-styles.css`).

---

## Code Structure
- **Indentation**: 2 spaces.
- **Line Length**: max 100 characters.
- **Grouping**: group related styles together (layout, typography, colors).
- **Comments**: use `/* ... */` for section headers and explanations.

Example:
```css
/* Navigation Bar */
.nav-bar {
  background-color: var(--primary-color);
  display: flex;
  justify-content: space-between;
  padding: 10px;
}
```

---

## Styling Standards
- Use **CSS variables** for colors, fonts, and spacing.
- Define a **color palette** and reuse consistently.
- Use **rem/em** units for font sizes and spacing (avoid px for scalability).
- Ensure **contrast ratios** meet accessibility standards.

---

## Responsive Design
- Use **flexbox** or **CSS grid** for layouts.
- Apply **media queries** for breakpoints:
  - Mobile: `max-width: 600px`
  - Tablet: `max-width: 1024px`
  - Desktop: default
- Test across multiple devices and browsers.

---

## Best Practices
- Avoid deep selector nesting.
- Minimize use of `!important`.
- Keep styles DRY (Don’t Repeat Yourself).
- Organize styles by component or feature.
- Document reusable classes in onboarding manuals.

---

## Future Enhancements
- Automated linting with **stylelint**.
- CSS minification in build pipelines.
- Adoption of CSS frameworks (Bootstrap, Tailwind) for rapid prototyping.
- Continuous integration checks for style consistency.
  