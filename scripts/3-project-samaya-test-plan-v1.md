# Project Samaya – Test Plan & QA Strategy

## 1. Introduction
This Test Plan defines the scope, approach, resources, and schedule for testing Project Samaya. It ensures academic calendar creation, exam scheduling, and faculty deadline tracking features meet functional and non-functional requirements.

## 2. Objectives
- Verify academic calendar creation and publishing works correctly.
- Validate exam scheduling with conflict detection.
- Ensure faculty deadline tracking and reminders function reliably.
- Confirm integration with Yojanā (paper readiness), Anvesha (analytics), and Sangrah (archival).

## 3. Scope
**In-Scope Testing:**
- Functional testing of calendar module, scheduling engine, deadline tracker.
- Integration testing with Yojanā, Anvesha, Sangrah.
- Performance testing of scheduling engine under load.
- Security testing (role-based access, audit logs).

**Out-of-Scope Testing:**
- Paper generation (handled by Yojanā).
- Evaluation workflows (handled by Viveka).
- Adaptive learning (handled by Prabodha).

## 4. Test Approach
- **Unit Testing:** Validate calendar module, scheduling engine, deadline tracker.
- **Integration Testing:** Verify data flow between Samaya and other systems.
- **System Testing:** End-to-end validation of calendar creation, scheduling, and reminders.
- **User Acceptance Testing (UAT):** Faculty, exam coordinators, and administrators validate usability.
- **Regression Testing:** Ensure new changes do not break existing functionality.

## 5. Test Environment
- **Frontend:** Web dashboards for faculty, students, coordinators, administrators.
- **Backend:** PHP (PDO) services.
- **Database:** MySQL with application-enforced integrity.
- **Test Data:** Sample academic events, exam slots, faculty deadlines.

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
- UAT sign-off from faculty, coordinators, and administrators.

## 8. Risk Analysis
- **Risk:** Scheduling conflicts not detected.  
  **Mitigation:** Stress test conflict detection with overlapping slots.  
- **Risk:** Deadline reminders not delivered.  
  **Mitigation:** Validate notification service with multiple test accounts.  
- **Risk:** Calendar not syncing across roles.  
  **Mitigation:** Role-based testing with faculty, coordinators, administrators.

## 9. Traceability Matrix
| Requirement ID | Test Case ID | Status |
|----------------|--------------|--------|
| SAM-RQMT-01 (Calendar Creation) | TC-SAM-01 | Pending |
| SAM-RQMT-02 (Exam Scheduling) | TC-SAM-02 | Pending |
| SAM-RQMT-03 (Deadline Tracking) | TC-SAM-03 | Pending |
| SAM-RQMT-04 (Integration) | TC-SAM-04 | Pending |

## 10. Schedule
- Test Case Design: Week 1
- Test Execution: Week 2–3
- Defect Fixes & Regression: Week 4
- UAT & Sign-off: Week 5
