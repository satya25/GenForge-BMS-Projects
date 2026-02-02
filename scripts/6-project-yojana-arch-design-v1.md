# Project Yojanā – System Architecture & Detailed Design

## 1. Architectural Overview
Yojanā is the GenAI-enabled exam paper generation system. It automates blueprint-driven paper creation, ensures compliance with Bloom’s taxonomy and CO mappings, and provides secure workflows for validation and download. It integrates with Sangrah (archival), Viveka (evaluation), and Anvesha (analytics) for full exam lifecycle management.

**Layers:**
- **Presentation Layer:** Faculty and exam coordinator dashboards.
- **Application Layer:** Paper generation engine, compliance validator, secure download manager.
- **Data Layer:** Question bank repository, blueprint metadata, compliance logs.
- **Integration Layer:** APIs to Sangrah (archival), Viveka (evaluation), Anvesha (analytics).

## 2. Components
- **Paper Generation Engine:** Creates exam papers from curated question banks based on blueprint rules.
- **Compliance Validator:** Checks Bloom’s taxonomy coverage and CO mappings.
- **Variant Generator:** Produces multiple statistically equivalent paper variants.
- **Secure Download Manager:** Ensures approved papers are delivered with watermark and metadata.
- **Integration APIs:** Connects with Sangrah for archival, Viveka for evaluation, and Anvesha for analytics.

## 3. Data Flow
1. **Input:** Blueprint and question bank metadata from faculty and Yojanā repository.
2. **Processing:** Paper generation engine selects questions, compliance validator checks coverage, variant generator produces alternatives.
3. **Output:** Validated exam papers securely downloadable and archived in Sangrah.

## 4. Database Design (Application-managed integrity)
- **Tables:**
  - `question_bank` (question_id, subject_id, bloom_level, CO_mapping, difficulty, status)
  - `blueprints` (blueprint_id, subject_id, created_by, created_on, rules_json)
  - `generated_papers` (paper_id, blueprint_id, variant_no, compliance_score, created_on)
  - `download_logs` (download_id, paper_id, faculty_id, timestamp, watermark_id)

**Note:** No foreign key constraints; integrity enforced at application layer.

## 5. API Specifications
- **POST /papers/generate/{blueprint_id}**
- **GET /papers/validate/{paper_id}**
- **GET /papers/download/{paper_id}**
- **GET /papers/variants/{blueprint_id}**
- **Integration APIs:** `/sangrah/archive`, `/viveka/evaluations`, `/anvesha/analytics`

## 6. Deployment Topology
- **Frontend:** Web dashboards for faculty and exam coordinators.
- **Backend:** PHP (PDO) services with transaction-wrapped queries.
- **Database:** MySQL with application-enforced integrity.
- **Generation Engine:** Python microservice for blueprint-driven paper creation.
- **Security:** Role-based authentication, secure API tokens, watermarking, audit logs.

## 7. Design Constraints
- No foreign key constraints; integrity enforced in application logic.
- All DB writes wrapped in transactions + try–catch.
- Compliance validator must guarantee ≥95% blueprint adherence.
- Modular design for predictive paper generation in future phases.
