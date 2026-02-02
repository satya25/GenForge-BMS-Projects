# Project Prabodha – Test Plan & QA Strategy

## 1. Introduction
This Test Plan defines the scope, approach, resources, and schedule for testing Project Prabodha. It ensures adaptive practice sessions, feedback generation, and faculty monitoring features meet functional and non-functional requirements.

## 2. Objectives
- Verify adaptive difficulty adjustment works correctly.
- Validate student practice sessions and feedback accuracy.
- Ensure faculty dashboards display progress metrics reliably.
- Confirm integration with Yojanā (question bank) and Anvesha (analytics).

## 3. Scope
**In-Scope Testing:**
- Functional testing of practice modules, adaptive engine, feedback service.
- Integration testing with Yojanā and Anvesha.
- Performance testing of adaptive engine under load.
- Security testing (role-based access, audit logs).

**Out-of-Scope Testing:**
- Paper generation (handled by Yojanā).
- Evaluation workflows (handled by Viveka).
- Archival (handled by Sangrah).

## 4. Test Approach
- **Unit Testing:** Validate adaptive engine, feedback service, progress tracker.
- **Integration Testing:** Verify data flow between Prabodha, Yojanā, and Anvesha.
- **System Testing:** End-to-end validation of practice sessions and dashboards.
- **User Acceptance Testing (UAT):** Students and faculty validate usability.
- **Regression Testing:** Ensure new changes do not break existing functionality.

## 5. Test Environment
- **Frontend:** Web/mobile practice interface.
- **Backend:** PHP (PDO) services.
- **Database:** MySQL with application-enforced integrity.
- **Test Data:** Sample question sets, student profiles, practice sessions.

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
- UAT sign-off from students and faculty.

## 8. Risk Analysis
- **Risk:** Adaptive engine misclassifies difficulty.  
  **Mitigation:** Validate against benchmark datasets.  
- **Risk:** Feedback not aligned with learning outcomes.  
  **Mitigation:** Faculty review of feedback templates.  
- **Risk:** Dashboard performance issues.  
  **Mitigation:** Load testing and optimization.

## 9. Traceability Matrix
| Requirement ID | Test Case ID | Status |
|----------------|--------------|--------|
| PRA-RQMT-01 (Practice Module) | TC-PRA-01 | Pending |
| PRA-RQMT-02 (Adaptive Engine) | TC-PRA-02 | Pending |
| PRA-RQMT-03 (Feedback Service) | TC-PRA-03 | Pending |
| PRA-RQMT-04 (Faculty Dashboard) | TC-PRA-04 | Pending |

## 10. Schedule
- Test Case Design: Week 1
- Test Execution: Week 2–3
- Defect Fixes & Regression: Week 4
- UAT & Sign-off: Week 5
