# Project Sangrah – Test Plan & QA Strategy

## 1. Introduction
This Test Plan defines the scope, approach, resources, and schedule for testing Project Sangrah. It ensures archival, version control, and retrieval features meet functional and non-functional requirements, supporting accreditation and compliance.

## 2. Objectives
- Verify archival of papers and blueprints with metadata.
- Validate retrieval engine for question usage history.
- Ensure version control maintains document integrity.
- Confirm integration with Yojanā (paper generation), Viveka (evaluation), and Anvesha (analytics).

## 3. Scope
**In-Scope Testing:**
- Functional testing of archival module, retrieval engine, usage tracker.
- Integration testing with Yojanā, Viveka, Anvesha.
- Performance testing of archival and retrieval under load.
- Security testing (role-based access, audit logs).

**Out-of-Scope Testing:**
- Paper generation (handled by Yojanā).
- Evaluation workflows (handled by Viveka).
- Scheduling (handled by Samaya).

## 4. Test Approach
- **Unit Testing:** Validate archival module, retrieval engine, usage tracker.
- **Integration Testing:** Verify data flow between Sangrah and other systems.
- **System Testing:** End-to-end validation of archival, retrieval, and reporting.
- **User Acceptance Testing (UAT):** Faculty, HODs, administrators validate usability.
- **Regression Testing:** Ensure new changes do not break existing functionality.

## 5. Test Environment
- **Frontend:** Web dashboards for faculty, HODs, administrators.
- **Backend:** PHP (PDO) services.
- **Database:** MySQL with application-enforced integrity.
- **Test Data:** Sample papers, blueprints, question usage logs.

## 6. Test Deliverables
- Test cases and scripts.
- Test execution logs.
- Defect reports.
- Test summary report.

## 7. Entry & Exit Criteria
**Entry Criteria:**
- Requirements and design documents approved.
- Test environment ready.
- Test data prepared.

**Exit Criteria:**
- All critical defects resolved.
- ≥95% test case pass rate.
- UAT sign-off from faculty, HODs, administrators.

## 8. Risk Analysis
- **Risk:** Papers not archived correctly.  
  **Mitigation:** Validate archival with checksum and metadata verification.  
- **Risk:** Retrieval engine fails under load.  
  **Mitigation:** Conduct stress testing with large datasets.  
- **Risk:** Version control errors.  
  **Mitigation:** Validate rollback and history tracking.

## 9. Traceability Matrix
| Requirement ID | Test Case ID | Status |
|----------------|--------------|--------|
| SAN-RQMT-01 (Paper Archival) | TC-SAN-01 | Pending |
| SAN-RQMT-02 (Blueprint Archival) | TC-SAN-02 | Pending |
| SAN-RQMT-03 (Retrieval Engine) | TC-SAN-03 | Pending |
| SAN-RQMT-04 (Usage Tracker) | TC-SAN-04 | Pending |

## 10. Schedule
- Test Case Design: Week 1
- Test Execution: Week 2–3
- Defect Fixes & Regression: Week 4
- UAT & Sign-off: Week 5
