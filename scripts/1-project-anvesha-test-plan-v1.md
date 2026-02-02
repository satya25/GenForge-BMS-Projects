# Project Anvesha – Test Plan & QA Strategy

## 1. Introduction
This Test Plan defines the scope, approach, resources, and schedule for testing Project Anvesha. It ensures that analytics, compliance validation, and reporting features meet functional and non-functional requirements.

## 2. Objectives
- Verify blueprint compliance validation accuracy.
- Validate dashboards for faculty, HODs, administrators.
- Ensure integration with Sangrah, Viveka, and Yojanā works seamlessly.
- Confirm reporting accuracy for accreditation.

## 3. Scope
**In-Scope Testing:**
- Functional testing of dashboards, compliance checker, reporting service.
- Integration testing with Sangrah, Viveka, Yojanā.
- Performance testing of analytics engine.
- Security testing (role-based access, audit logs).

**Out-of-Scope Testing:**
- Paper generation (handled by Yojanā).
- Evaluation workflows (handled by Viveka).
- Scheduling (handled by Samaya).

## 4. Test Approach
- **Unit Testing:** Validate individual modules (analytics engine, compliance checker).
- **Integration Testing:** Verify data flow between Anvesha and other systems.
- **System Testing:** End-to-end validation of dashboards and reporting.
- **User Acceptance Testing (UAT):** Faculty and administrators validate usability.
- **Regression Testing:** Ensure new changes do not break existing functionality.

## 5. Test Environment
- **Frontend:** Web dashboards (React/Angular).
- **Backend:** PHP (PDO) services.
- **Database:** MySQL with application-enforced integrity.
- **Test Data:** Sample papers, blueprints, evaluation results.

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
- UAT sign-off from faculty and administrators.

## 8. Risk Analysis
- **Risk:** Incorrect compliance validation.  
  **Mitigation:** Cross-check with manual validation.  
- **Risk:** Integration failures with Sangrah/Viveka/Yojanā.  
  **Mitigation:** Early integration testing.  
- **Risk:** Performance bottlenecks in analytics engine.  
  **Mitigation:** Load testing and optimization.

## 9. Traceability Matrix
| Requirement ID | Test Case ID | Status |
|----------------|--------------|--------|
| ANV-RQMT-01 (Dashboard) | TC-ANV-01 | Pending |
| ANV-RQMT-02 (Compliance Check) | TC-ANV-02 | Pending |
| ANV-RQMT-03 (Reporting) | TC-ANV-03 | Pending |
| ANV-RQMT-04 (Integration) | TC-ANV-04 | Pending |

## 10. Schedule
- Test Case Design: Week 1
- Test Execution: Week 2–3
- Defect Fixes & Regression: Week 4
- UAT & Sign-off: Week 5
