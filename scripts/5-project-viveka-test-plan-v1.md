# Project Viveka – Test Plan & QA Strategy

## 1. Introduction
This Test Plan defines the scope, approach, resources, and schedule for testing Project Viveka. It ensures automated grading, evaluation workflows, and secure archival of evaluated papers meet functional and non-functional requirements.

## 2. Objectives
- Verify automated grading engine accuracy for objective questions.
- Validate faculty dashboards for grading consistency.
- Ensure secure storage and retrieval of evaluated papers.
- Confirm integration with Yojanā (paper generation), Sangrah (archival), and Anvesha (analytics).

## 3. Scope
**In-Scope Testing:**
- Functional testing of grading engine, evaluation workflow manager, consistency checker.
- Integration testing with Yojanā, Sangrah, Anvesha.
- Performance testing of grading engine under load.
- Security testing (role-based access, audit logs).

**Out-of-Scope Testing:**
- Paper generation (handled by Yojanā).
- Scheduling (handled by Samaya).
- Adaptive learning (handled by Prabodha).

## 4. Test Approach
- **Unit Testing:** Validate grading engine, workflow manager, consistency checker.
- **Integration Testing:** Verify data flow between Viveka and other systems.
- **System Testing:** End-to-end validation of grading, dashboards, archival.
- **User Acceptance Testing (UAT):** Faculty and exam coordinators validate usability.
- **Regression Testing:** Ensure new changes do not break existing functionality.

## 5. Test Environment
- **Frontend:** Web dashboards for faculty, coordinators, administrators.
- **Backend:** PHP (PDO) services.
- **Database:** MySQL with application-enforced integrity.
- **Test Data:** Sample papers, student responses, evaluation logs.

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
- UAT sign-off from faculty and exam coordinators.

## 8. Risk Analysis
- **Risk:** Automated grading misclassifies answers.  
  **Mitigation:** Benchmark against manually graded papers.  
- **Risk:** Faculty dashboard shows inconsistent metrics.  
  **Mitigation:** Validate with controlled datasets.  
- **Risk:** Archival failures.  
  **Mitigation:** Verify archival with checksum and metadata validation.

## 9. Traceability Matrix
| Requirement ID | Test Case ID | Status |
|----------------|--------------|--------|
| VIV-RQMT-01 (Automated Grading) | TC-VIV-01 | Pending |
| VIV-RQMT-02 (Faculty Dashboard) | TC-VIV-02 | Pending |
| VIV-RQMT-03 (Consistency Checker) | TC-VIV-03 | Pending |
| VIV-RQMT-04 (Secure Archival) | TC-VIV-04 | Pending |

## 10. Schedule
- Test Case Design: Week 1
- Test Execution: Week 2–3
- Defect Fixes & Regression: Week 4
- UAT & Sign-off: Week 5
