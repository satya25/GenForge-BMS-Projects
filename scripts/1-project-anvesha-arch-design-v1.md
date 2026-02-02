# Project Anvesha – System Architecture & Detailed Design

## 1. Architectural Overview
Anvesha is built as a modular analytics engine integrated into the GenAI ecosystem. It consolidates exam performance data, question usage statistics, and blueprint compliance into dashboards for faculty and administrators.

**Layers:**
- **Presentation Layer:** Web-based dashboards (faculty, HOD, admin).
- **Application Layer:** Analytics services, compliance checker, reporting engine.
- **Data Layer:** Consolidated repository (via Sangrah), question bank metadata (via Yojanā).
- **Integration Layer:** APIs to Viveka (evaluation), Yojanā (paper generation), Samaya (scheduling).

## 2. Components
- **Dashboard Module:** Role-based views for faculty, HODs, administrators.
- **Analytics Engine:** Statistical equivalence testing, Bloom’s taxonomy coverage, CO mapping.
- **Compliance Checker:** Automated validation of blueprint adherence.
- **Reporting Service:** Exportable reports (PDF/Excel) for accreditation.
- **Integration APIs:** RESTful endpoints for data exchange with Sangrah, Viveka, Yojanā.

## 3. Data Flow
1. **Input:** Exam papers and metadata from Sangrah; evaluation results from Viveka.
2. **Processing:** Analytics engine computes usage statistics, compliance metrics.
3. **Output:** Dashboards and reports for stakeholders.

## 4. Database Design (Application-managed integrity)
- **Tables:**
  - `questions_metadata` (question_id, subject_id, bloom_level, CO_mapping, usage_count)
  - `exam_papers` (paper_id, subject_id, blueprint_id, date, coordinator_id)
  - `analytics_results` (result_id, paper_id, compliance_score, difficulty_distribution)
  - `reports` (report_id, type, generated_by, generated_on, file_path)

**Note:** No foreign key constraints; integrity enforced at application layer.

## 5. API Specifications
- **GET /analytics/dashboard/{role}/{subject}**
- **POST /analytics/compliance-check/{paper_id}**
- **GET /reports/{report_id}/download**
- **Integration APIs:** `/viveka/results`, `/yojana/papers`, `/sangrah/archive`

## 6. Deployment Topology
- **Frontend:** React/Angular dashboards.
- **Backend:** PHP (PDO) services with transaction-wrapped queries.
- **Database:** MySQL with application-enforced integrity.
- **Hosting:** Streamlit/Flask-based microservices for analytics (optional).
- **Security:** Role-based authentication, secure API tokens, audit logs.

## 7. Design Constraints
- No foreign key constraints; integrity enforced in application logic.
- All DB writes wrapped in transactions + try–catch.
- Modular architecture for future scalability.


