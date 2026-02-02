# Project Sangrah – Use Cases, User Stories, Actors, Workflows

## 1. Actors
- **Faculty:** Access historical papers and question usage data.
- **HODs:** Oversee department-level archival and compliance.
- **Exam Coordinators:** Trace paper variants and downloads.
- **Administrators:** Manage institute-wide archival policies.
- **Academic Council:** Review consolidated data for accreditation.

## 2. Use Cases
### UC-1: Archive Generated Paper
- **Actor:** System (triggered by Exam Coordinator)
- **Precondition:** Paper generated in Yojanā.
- **Steps:**
  1. Exam coordinator finalizes paper.
  2. System stores paper in Sangrah repository.
  3. Metadata (subject, blueprint ID, date) recorded.
- **Postcondition:** Paper archived with version control.

### UC-2: Retrieve Question Usage History
- **Actor:** Faculty
- **Precondition:** Faculty logged in with valid credentials.
- **Steps:**
  1. Navigate to archival dashboard.
  2. Select subject/course.
  3. View question usage history across semesters.
- **Postcondition:** Faculty gains insights into question repetition and coverage.

### UC-3: Generate Accreditation Data Report
- **Actor:** Administrator
- **Precondition:** Consolidated archival data available.
- **Steps:**
  1. Select reporting period.
  2. System compiles archival data.
  3. Export report to PDF/Excel.
- **Postcondition:** Accreditation-ready report generated.

## 3. User Stories
- As a **faculty member**, I want to access question usage history so that I can avoid repetition in future papers.  
- As an **exam coordinator**, I want papers archived automatically so that I can trace variants later.  
- As an **administrator**, I want consolidated archival reports so that I can prepare for audits.  

## 4. Workflows
### Workflow 1: Paper Archival
1. Exam coordinator finalizes paper in Yojanā.
2. System archives paper in Sangrah.
3. Metadata stored with version control.
4. Paper available for retrieval.

### Workflow 2: Question Usage Retrieval
1. Faculty logs in.
2. Selects subject/course.
3. System displays question usage history.
4. Faculty reviews and plans future papers.

### Workflow 3: Accreditation Report Generation
1. Administrator logs in.
2. Selects reporting period.
3. System consolidates archival data.
4. Report generated and exported.
