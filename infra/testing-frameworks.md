# Testing Guidelines & Frameworks

## Overview
These guidelines define the testing standards for all GenForge projects. They ensure reliability, accuracy, and maintainability across PHP/XAMPP portals and Python AI services, while promoting automation and continuous integration.

---

## Principles
- **Consistency**: All projects must follow the same testing workflow.
- **Coverage**: Unit, integration, system, and AI-specific tests are mandatory.
- **Automation**: Tests must run automatically in CI/CD pipelines.
- **Documentation**: Each test suite must include usage instructions and expected outcomes.

---

## Unit Testing
- **PHP**: Use **PHPUnit** for backend logic.
- **Python**: Use **pytest** for AI services.
- **JavaScript**: Use **Jest** or **Mocha** for frontend scripts.
- **CSS/HTML**: Validate with **stylelint** and **HTMLHint**.

---

## Integration Testing
- **REST APIs**: Test endpoints with Postman/Newman collections.
- **Cross-Language Bridge**: Validate PHP ↔ Python communication using mock data.
- **Database**: Ensure CRUD operations work with prepared statements and transactions.

---

## System Testing
- Validate end-to-end workflows:
  - User login → dashboard → AI inference → report generation.
- Test role-based access control and session management.
- Verify notifications, schedulers, and data export/import pipelines.

---

## AI-Specific Testing
- **Metrics**: Accuracy, precision, recall, F1-score must be logged.
- **Drift Detection**: Monitor model performance over time.
- **Benchmarking**: Compare offline vs online transcription (Agent_4).
- **Validation**: Ensure reproducibility of results across environments.

---

## Automation & CI/CD
- **Pipeline Integration**: All tests must run before deployment.
- **Coverage Reports**: Generate and review coverage metrics.
- **Static Analysis**: Run linters (PHP_CodeSniffer, flake8, ESLint, stylelint).
- **Continuous Monitoring**: Integrate with dashboards for real-time test results.

---

## Best Practices
- Write tests alongside code, not after.
- Keep tests small, independent, and reproducible.
- Use mock data for external dependencies.
- Document test cases in companion `.md` files.
- Review and update test suites regularly.

---

## Future Enhancements
- Automated regression testing for infra updates.
- AI-driven test case generation.
- Centralized test repository for department-wide reuse.
- Continuous improvement loop with student/faculty feedback.
