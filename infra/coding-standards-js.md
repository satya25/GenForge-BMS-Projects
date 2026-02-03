
# Coding Standards: JavaScript

## Overview
These standards define how JavaScript code should be written and maintained across all GenForge projects. They ensure readability, consistency, and maintainability, while aligning with modern ES6+ best practices.

## General Principles
- Use **ES6+ syntax** (arrow functions, `let`/`const`, template literals).
- Prefer **modular code** (split into reusable functions and modules).
- Avoid global variables; encapsulate logic in functions or classes.
- Always lint code before committing.

---

## Naming Conventions
- **Variables & Functions**: `camelCase` (e.g., `getUserData`, `userEmail`).
- **Classes**: `PascalCase` (e.g., `UserManager`, `SessionHandler`).
- **Constants**: `UPPER_CASE` with underscores (e.g., `MAX_RETRIES`).
- **Files**: descriptive lowercase with hyphens (e.g., `user-management.js`).

---

## Code Structure
- **Indentation**: 2 spaces.
- **Line Length**: max 100 characters.
- **Semicolons**: mandatory at the end of statements.
- **Braces**: opening brace on the same line.
- **Comments**: use `//` for inline, `/** ... */` for block documentation.

Example:
```javascript
/**
 * Fetch user details by ID.
 * @param {number} id - User ID
 * @returns {Promise<Object>} User details
 */
async function getUserById(id) {
  const response = await fetch(`/api/users/${id}`);
  return response.json();
}
```

---

## Security Standards
- Sanitize all user inputs before processing.
- Escape dynamic content before injecting into DOM.
- Avoid `eval()` and other unsafe functions.
- Use HTTPS for all API calls.

---

## Error & Logging
- Use `try...catch` for error handling in async code.
- Log errors with context, but avoid exposing sensitive data.
- Use centralized logging utilities where possible.

---

## Best Practices
- Use `const` for values that don’t change, `let` otherwise.
- Prefer arrow functions for callbacks.
- Keep functions small and focused.
- Write unit tests with **Jest** or **Mocha**.
- Document APIs with JSDoc.

---

## Future Enhancements
- Automated linting with **ESLint**.
- Code formatting with **Prettier**.
- Continuous integration checks for style and tests.
- Coverage reports integrated into CI/CD pipelines.

---

