# Project Anvesha – Use Cases, User Stories, Actors, Workflows

## 1. Actors
- **Faculty:** Review analytics on question usage, blueprint compliance, and student performance.
- **HODs:** Monitor department-level analytics and ensure syllabus coverage.
- **Exam Coordinators:** Validate paper fairness and statistical equivalence.
- **Administrators:** Track institute-wide adoption and compliance.
- **Academic Council:** Review analytics for accreditation and policy decisions.

## 2. Use Cases
### UC-1: View Faculty Dashboard
- **Actor:** Faculty
- **Precondition:** Faculty logged in with valid credentials.
- **Steps:**
  1. Navigate to dashboard.
  2. Select subject/course.
  3. View analytics on question usage, Bloom’s taxonomy coverage, and student performance.
- **Postcondition:** Faculty gains insights into teaching effectiveness.

### UC-2: Validate Blueprint Compliance
- **Actor:** Exam Coordinator
- **Precondition:** Blueprint and generated paper available in system.
- **Steps:**
  1. Select paper variant.
  2. Run compliance check.
  3. Review Bloom’s taxonomy and CO mapping results.
- **Postcondition:** Paper validated for compliance.

### UC-3: Generate Accreditation Report
- **Actor:** Administrator
- **Precondition:** Consolidated data available in Sangrah.
- **Steps:**
  1. Select reporting period.
  2. Generate compliance and analytics report.
  3. Export to PDF/Excel.
- **Postcondition:** Report ready for accreditation submission.

## 3. User Stories
- As a **faculty member**, I want to see question usage analytics so that I can identify gaps in syllabus coverage.  
- As an **exam coordinator**, I want to validate blueprint compliance so that papers meet accreditation standards.  
- As an **administrator**, I want to generate institute-wide reports so that I can prepare for audits.  

## 4. Workflows
### Workflow 1: Faculty Dashboard Access
1. Faculty logs in.
2. System authenticates credentials.
3. Faculty selects subject/course.
4. Dashboard displays analytics (question usage, Bloom’s taxonomy, student performance).

### Workflow 2: Paper Compliance Validation
1. Exam coordinator logs in.
2. Selects paper variant.
3. System runs compliance check.
4. Results displayed with compliance percentage.
5. Coordinator approves or flags paper.

### Workflow 3: Accreditation Report Generation
1. Administrator logs in.
2. Selects reporting period.
3. System consolidates data from Sangrah.
4. Report generated and exported.
