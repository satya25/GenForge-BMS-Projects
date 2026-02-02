# Project Yojanā – Test Plan & QA Strategy

## 1. Introduction
This Test Plan defines the scope, approach, resources, and schedule for testing Project Yojanā. It ensures blueprint-driven paper generation, compliance validation, and secure download workflows meet functional and non-functional requirements.

## 2. Objectives
- Verify paper generation engine produces valid papers from blueprints.
- Validate compliance checker accuracy for Bloom’s taxonomy and CO mappings.
- Ensure secure download manager delivers approved papers with watermark and metadata.
- Confirm integration with Sangrah (archival), Viveka (evaluation), and Anvesha (analytics).

## 3. Scope
**In-Scope Testing:**
- Functional testing of paper generation, compliance validation, variant generation, secure download.
- Integration testing with Sangrah, Viveka, Anvesha.
- Performance testing of paper generation engine under load.
- Security testing (role-based access, watermarking, audit logs).

**Out-of-Scope Testing:**
- Evaluation workflows (handled by Viveka).
- Scheduling (handled by Samaya).
- Adaptive learning (handled by Prabodha).

## 4. Test Approach
- **Unit Testing:** Validate paper generation engine, compliance validator, secure download manager.
- **Integration Testing:** Verify data flow between Yojanā and other systems.
- **System Testing:** End-to-end validation of paper generation, compliance, and download workflows.
- **User Acceptance Testing (UAT):** Faculty and exam coordinators validate usability.
- **Regression Testing:** Ensure new changes do not break existing functionality.

## 5. Test Environment
- **Frontend:** Web dashboards for faculty and exam coordinators.
- **Backend:** PHP (PDO) services.
- **Database:** MySQL with application-enforced integrity.
- **Test Data:** Sample blueprints, question banks, paper variants.

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
- **Risk:** Paper generation engine fails to meet blueprint rules.  
  **Mitigation:** Validate against manually curated papers.  
- **Risk:** Compliance checker miscalculates Bloom’s taxonomy coverage.  
  **Mitigation:** Cross-check with benchmark datasets.  
- **Risk:** Secure download fails or watermark missing.  
  **Mitigation:** Validate with multiple test accounts and audit logs.

## 9. Traceability Matrix
| Requirement ID | Test Case ID | Status |
|----------------|--------------|--------|
| YOJ-RQMT-01 (Paper Generation) | TC-YOJ-01 | Pending |
| YOJ-RQMT-02 (Compliance Validation) | TC-YOJ-02 | Pending |
| YOJ-RQMT-03 (Variant Generation) | TC-YOJ-03 | Pending |
| YOJ-RQMT-04 (Secure Download) | TC-YOJ-04 | Pending |

## 10. Schedule
- Test Case Design: Week 1
- Test Execution: Week 2–3
- Defect Fixes & Regression: Week 4
- UAT & Sign-off: Week 5
