# Project Yojanā – Use Cases, User Stories, Actors, Workflows

## 1. Actors
- **Faculty:** Generate exam papers, validate compliance, and download securely.
- **Exam Coordinators:** Oversee paper generation workflows and approvals.
- **HODs:** Monitor blueprint compliance and syllabus coverage.
- **Administrators:** Ensure secure paper generation and archival.
- **Academic Council:** Review compliance for accreditation and audits.

## 2. Use Cases
### UC-1: Generate Exam Paper
- **Actor:** Faculty
- **Precondition:** Blueprint defined and question bank available.
- **Steps:**
  1. Faculty logs in.
  2. Selects blueprint and subject.
  3. System generates paper variant.
  4. Faculty reviews compliance results.
- **Postcondition:** Exam paper generated and validated.

### UC-2: Validate Paper Compliance
- **Actor:** Exam Coordinator
- **Precondition:** Paper generated and available in system.
- **Steps:**
  1. Coordinator selects paper variant.
  2. System runs compliance check (Bloom’s taxonomy, CO mappings).
  3. Results displayed with compliance percentage.
  4. Coordinator approves or flags paper.
- **Postcondition:** Paper validated for compliance.

### UC-3: Secure Paper Download
- **Actor:** Faculty
- **Precondition:** Paper approved by coordinator.
- **Steps:**
  1. Faculty requests download.
  2. System verifies approval and credentials.
  3. Paper securely downloaded with watermark and metadata.
- **Postcondition:** Paper securely delivered to faculty.

## 3. User Stories
- As a **faculty member**, I want to generate compliant exam papers so that I can save time and ensure fairness.  
- As an **exam coordinator**, I want to validate compliance so that accreditation standards are met.  
- As an **administrator**, I want secure paper workflows so that audit requirements are fulfilled.  

## 4. Workflows
### Workflow 1: Paper Generation
1. Faculty logs in.
2. Selects blueprint and subject.
3. System generates paper variant.
4. Faculty reviews compliance results.

### Workflow 2: Compliance Validation
1. Exam coordinator logs in.
2. Selects paper variant.
3. System runs compliance check.
4. Coordinator approves or flags paper.

### Workflow 3: Secure Download
1. Faculty requests paper download.
2. System verifies approval and credentials.
3. Paper downloaded securely with watermark.
4. Metadata stored in Sangrah for archival.
