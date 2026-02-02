# Project Sangrah – System Architecture & Detailed Design

## 1. Architectural Overview
Sangrah is the institute’s centralized data consolidation and archival system. It unifies exam papers, blueprints, and question usage history into a structured repository. Sangrah ensures reliable, version-controlled access for faculty, administrators, and accreditation bodies.

**Layers:**
- **Presentation Layer:** Dashboards for faculty, HODs, administrators.
- **Application Layer:** Archival service, version control, retrieval engine.
- **Data Layer:** Repository of papers, blueprints, and metadata.
- **Integration Layer:** APIs to Yojanā (paper generation), Viveka (evaluation), Anvesha (analytics).

## 2. Components
- **Archival Module:** Stores papers, blueprints, and metadata.
- **Version Control Service:** Tracks changes and maintains history.
- **Retrieval Engine:** Enables search and access by subject, semester, or coordinator.
- **Usage Tracker:** Logs question usage across semesters.
- **Integration APIs:** Connects with Yojanā, Viveka, and Anvesha.

## 3. Data Flow
1. **Input:** Papers and blueprints from Yojanā; evaluation results from Viveka.
2. **Processing:** Archival module stores documents; usage tracker logs metadata.
3. **Output:** Dashboards and reports for faculty, HODs, administrators.

## 4. Database Design (Application-managed integrity)
- **Tables:**
  - `papers_archive` (paper_id, subject_id, blueprint_id, date, coordinator_id, file_path)
  - `blueprints_archive` (blueprint_id, subject_id, created_on, created_by, file_path)
  - `question_usage` (usage_id, question_id, subject_id, semester, frequency)
  - `audit_logs` (log_id, action, user_id, timestamp)

**Note:** No foreign key constraints; integrity enforced at application layer.

## 5. API Specifications
- **POST /archive/paper**
- **POST /archive/blueprint**
- **GET /archive/papers/{subject_id}**
- **GET /usage/{question_id}**
- **Integration APIs:** `/yojana/papers`, `/viveka/evaluations`, `/anvesha/analytics`

## 6. Deployment Topology
- **Frontend:** Web dashboards for faculty, HODs, administrators.
- **Backend:** PHP (PDO) services with transaction-wrapped queries.
- **Database:** MySQL with application-enforced integrity.
- **Archival Service:** Python/Flask microservice for version control and retrieval.
- **Security:** Role-based authentication, secure API tokens, audit logs.

## 7. Design Constraints
- No foreign key constraints; integrity enforced in application logic.
- All DB writes wrapped in transactions + try–catch.
- Archival must guarantee 100% coverage of generated papers and blueprints.
- Modular design for scalability and compliance reporting.
