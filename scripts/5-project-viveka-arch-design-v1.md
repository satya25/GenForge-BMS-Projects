# Project Viveka – System Architecture & Detailed Design

## 1. Architectural Overview
Viveka is the institute’s evaluation and grading system. It automates objective grading, supports faculty in subjective evaluation, and ensures secure storage of evaluated papers. It integrates with Yojanā (paper generation), Sangrah (archival), and Anvesha (analytics) for end-to-end exam lifecycle management.

**Layers:**
- **Presentation Layer:** Faculty dashboards, exam coordinator views, administrator portals.
- **Application Layer:** Automated grading engine, evaluation workflow manager, consistency checker.
- **Data Layer:** Evaluated papers repository, grading metrics, audit logs.
- **Integration Layer:** APIs to Yojanā (papers), Sangrah (archival), Anvesha (analytics).

## 2. Components
- **Grading Engine:** Automates evaluation of objective-type questions.
- **Evaluation Workflow Manager:** Tracks progress of paper evaluation and timelines.
- **Consistency Checker:** Ensures grading uniformity across evaluators.
- **Faculty Dashboard:** Displays grading metrics and discrepancies.
- **Archival Connector:** Pushes finalized papers into Sangrah.
- **Integration APIs:** Connects with Yojanā for paper metadata and Anvesha for analytics.

## 3. Data Flow
1. **Input:** Papers generated in Yojanā; student responses uploaded.
2. **Processing:** Grading engine evaluates objective questions; faculty completes subjective evaluation.
3. **Output:** Evaluated papers stored securely; dashboards updated; archival triggered.

## 4. Database Design (Application-managed integrity)
- **Tables:**
  - `evaluated_papers` (eval_id, paper_id, subject_id, evaluator_id, date, file_path)
  - `grading_results` (result_id, eval_id, question_id, score, correctness, comments)
  - `consistency_metrics` (metric_id, eval_id, variance_score, flagged)
  - `audit_logs` (log_id, action, user_id, timestamp)

**Note:** No foreign key constraints; integrity enforced at application layer.

## 5. API Specifications
- **POST /grading/auto-evaluate/{paper_id}**
- **POST /grading/submit/{eval_id}**
- **GET /dashboard/faculty/{subject_id}**
- **GET /consistency/{eval_id}**
- **Integration APIs:** `/yojana/papers`, `/sangrah/archive`, `/anvesha/analytics`

## 6. Deployment Topology
- **Frontend:** Web dashboards for faculty, coordinators, administrators.
- **Backend:** PHP (PDO) services with transaction-wrapped queries.
- **Database:** MySQL with application-enforced integrity.
- **Grading Engine:** Python microservice for automated evaluation.
- **Security:** Role-based authentication, secure API tokens, audit logs.

## 7. Design Constraints
- No foreign key constraints; integrity enforced in application logic.
- All DB writes wrapped in transactions + try–catch.
- Automated grading accuracy ≥95% required for objective questions.
- Modular design for predictive analytics integration in future phases.
