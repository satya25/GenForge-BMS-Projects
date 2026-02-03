# Coding Standards: PHP

## Overview
These standards define how PHP code should be written and maintained across all GenForge projects. They ensure consistency, readability, and maintainability, while aligning with industry best practices.

## General Principles
- Follow **PSR-12** coding style guidelines.
- Use **namespaces** and **autoloading** for all classes.
- Enforce **strict typing** wherever possible (`declare(strict_types=1);`).
- Centralize error handling via `error-exception-handler.md`.

---

## Naming Conventions
- **Classes**: `PascalCase` (e.g., `UserManager`, `SessionHandler`).
- **Methods & Variables**: `camelCase` (e.g., `getUserData`, `userEmail`).
- **Constants**: `UPPER_CASE` with underscores (e.g., `MAX_RETRIES`).
- **Files**: descriptive lowercase with hyphens (e.g., `user-management.php`).

---

## Code Structure
- **Indentation**: 4 spaces, no tabs.
- **Line Length**: max 120 characters.
- **Braces**: opening brace on the same line.
- **Comments**: use PHPDoc for functions and classes.

Example:
```php
/**
 * Get user details by ID.
 *
 * @param int $id
 * @return array
 */
public function getUserById(int $id): array {
    // Fetch user from database
}
```

---

## Security Standards
- Always use **prepared statements** for SQL queries.
- Escape all user inputs before rendering in HTML.
- Enforce **role-based access control**.
- Store passwords using `password_hash()` and `password_verify()`.

---

## Error & Logging
- Use centralized error handling (`error-exception-handler.md`).
- Log at appropriate levels: `info`, `warning`, `error`.
- Never expose sensitive data in error messages.

---

## Best Practices
- Keep functions small and focused.
- Avoid global variables.
- Use dependency injection for services.
- Write unit tests with **PHPUnit**.
- Document all public APIs.

---

## Future Enhancements
- Automated linting with **PHP_CodeSniffer**.
- Static analysis with **PHPStan**.
- Continuous integration checks for coding style.

---


