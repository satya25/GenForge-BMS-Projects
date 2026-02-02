# Project Viveka – Use Cases, User Stories, Actors, Workflows

## 1. Actors
- **Faculty:** Evaluate exam papers, track grading consistency, and access dashboards.
- **Exam Coordinators:** Oversee evaluation workflows and timelines.
- **HODs:** Monitor department-level grading and compliance.
- **Administrators:** Ensure secure storage and retrieval of evaluated papers.
- **Academic Council:** Review evaluation consistency for accreditation.

## 2. Use Cases
### UC-1: Automated Grading of Objective Questions
- **Actor:** Faculty
- **Precondition:** Exam papers uploaded into Viveka.
- **Steps:**
  1. Faculty selects paper batch.
  2. System auto-grades objective questions.
  3. Faculty reviews and confirms results.
- **Postcondition:** Objective questions graded automatically and verified.

### UC-2: Faculty Dashboard Access
- **Actor:** Faculty
- **Precondition:** Faculty logged in with valid credentials.
- **Steps:**
  1. Navigate to evaluation dashboard.
  2. View grading consistency metrics.
  3. Identify discrepancies across evaluators.
- **Postcondition:** Faculty gains insights into grading consistency.

### UC-3: Secure Storage of Evaluated Papers
- **Actor:** Administrator
- **Precondition:** Papers evaluated and finalized.
- **Steps:**
  1. Administrator initiates archival.
  2. System stores evaluated papers securely with audit logs.
  3. Papers tagged with metadata (subject, date, evaluator).
- **Postcondition:** Evaluated papers securely stored and retrievable.

## 3. User Stories
- As a **faculty member**, I want automated grading for objective questions so that I can save time and focus on subjective evaluation.  
- As an **exam coordinator**, I want to oversee evaluation workflows so that timelines are met.  
- As an **administrator**, I want secure storage of evaluated papers so that audits are seamless.  

## 4. Workflows
### Workflow 1: Automated Grading
1. Faculty uploads exam papers.
2. System auto-grades objective questions.
3. Faculty reviews and confirms results.
4. Grades stored in system.

### Workflow 2: Faculty Dashboard Access
1. Faculty logs in.
2. Dashboard displays grading consistency metrics.
3. Faculty reviews discrepancies.
4. Faculty adjusts evaluation as needed.

### Workflow 3: Secure Archival
1. Administrator logs in.
2. Initiates archival of evaluated papers.
3. System stores papers securely with metadata.
4. Papers retrievable for audits and accreditation.
