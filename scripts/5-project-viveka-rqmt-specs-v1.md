Excellent, Satya ✅ — here’s the **frozen consolidated requirements specification v1.0** for **Project Viveka**, ready to be placed in `/frozen-requirements/project-viveka-rqmt-specs-v1.md`.  

---

# GenAI Project 3  
**Code Name:** Viveka  
**Title:** Automated Evaluation of Continuous Internal Evaluation (CIE) & End-Semester Examinations  
**Version:** v1.0 (Baselined)  
**Date:** February 2026  
**Prepared By:** GenForge Workshop Team  

---

## 1. Executive Summary
Viveka is an AI-powered automated evaluation system designed to assess student submissions across multiple modalities (text, code, images, diagrams) using faculty-defined rubrics aligned with course outcomes and Bloom’s taxonomy. It ensures consistency, fairness, efficiency, and transparency in grading, with personalized feedback, integrated plagiarism detection, and comprehensive analytics. Faculty oversight is preserved through review and override workflows.

---

## 2. Objectives
- Automate evaluation of CIE and end-semester submissions.  
- Ensure consistency and fairness across large cohorts.  
- Deliver efficiency (<10s per submission).  
- Support multimodal evaluation (text, code, images, mixed).  
- Provide explainable AI scoring with reasoning.  
- Detect plagiarism in-house (text + code).  
- Generate personalized, constructive feedback.  
- Enable analytics dashboards for faculty and HODs.  

---

## 3. Scope
### In-Scope
- Automated evaluation of multimodal submissions.  
- Test & quiz design with rubrics and randomization.  
- Rubric management aligned with Bloom’s taxonomy and COs.  
- Feedback generation (AI + faculty).  
- Plagiarism detection (text + code).  
- Faculty review workflow (override, feedback approval).  
- Result consolidation and grade normalization.  
- Analytics dashboards (performance trends, difficulty analysis).  
- Integration APIs (Yojanā, Anvesha).  

### Out-of-Scope (Phase I)
- Automatic question generation.  
- Proctoring or exam supervision.  
- Video/audio evaluation.  
- Handwriting recognition (Phase II).  
- External plagiarism services (Turnitin, Moss).  
- Native mobile apps.  
- Real-time collaborative grading.  

---

## 4. Stakeholders & Roles
- **Students:** submit work, view scores/feedback, plagiarism reports, progress dashboards.  
- **Faculty:** design tests/quizzes, define rubrics, review/override AI scores, monitor plagiarism, generate reports, provide manual feedback.  
- **HODs/Management:** view department analytics, performance trends.  
- **Administrators:** audit logs, compliance monitoring, configure system settings.  

---

## 5. Functional Requirements
- **Submission Types:** essays, MCQs, code files (Python/C/Java/C++), images, mixed multimodal.  
- **Evaluation Logic:** multimodal LLM agents, rubric parsing, Bloom’s taxonomy alignment, faculty override learning loop.  
- **Feedback Generation:** contextual, annotated, faculty approval workflow.  
- **Plagiarism Detection:** text (TF-IDF + embeddings), code (AST + token similarity), configurable thresholds, in-house engine.  
- **Agentic Workflows:** Evaluator Agent, Plagiarism Agent, Analytics Agent, Feedback Agent.  
- **Analytics:** grade normalization, outlier detection, trend analysis, CO achievement.  
- **Integration:** APIs for Yojanā (question papers) and Anvesha (analytics).  

---

## 6. Non-Functional Requirements
- **Performance:** <10s evaluation per submission; <2s dashboard refresh.  
- **Deployment:** local XAMPP/MySQL; Docker optional; no GPU required.  
- **Security:** anonymization, AES-256 encryption, JWT RBAC, audit trails.  
- **Scalability:** 5K students, 50K submissions/semester.  
- **Accuracy:** >90% agreement with faculty scores; <5% false plagiarism positives.  
- **Compliance:** institutional data policies, WCAG 2.1 accessibility.  

---

## 7. User Stories & Use Cases
- **Students:** submit assignments, take quizzes, view scores/feedback, check plagiarism reports, track progress.  
- **Faculty:** design tests/quizzes, define rubrics, review AI scores, monitor plagiarism, generate reports, provide manual feedback.  
- **HOD/Admin:** view analytics, audit logs, configure system settings.  

**Detailed Use Case (UC-01: Submit & Evaluate Assignment):**  
Student submits → AI evaluator scores + feedback → plagiarism agent checks → faculty reviews/overrides → student notified.  
Alternative flows: late submission, plagiarism flagged, AI evaluation failure.  

---

## 8. Use Case Diagrams
Actors: Students, Faculty, HOD/Admin, AI Evaluator Agent.  
Interactions: submission, evaluation, plagiarism detection, feedback, analytics, configuration.  

---

## 9. System Architecture
- **Presentation Layer:** PHP + Bootstrap 5 UIs (student, faculty, admin).  
- **Application Layer:** controllers for submission, evaluation, analytics.  
- **Business Logic Layer:** services for submission, evaluation, rubric, plagiarism, notifications, analytics.  
- **AI Processing Layer:** Python (FastAPI + LangChain + Ollama), agents (Evaluator, Plagiarism, Feedback, Analytics).  
- **Tool Layer:** text parser (NLP), code parser (AST), image OCR (Tesseract), semantic search (embeddings).  
- **Data Access Layer:** PHP repositories.  
- **Database Layer:** MySQL 8.0+ (submissions, evaluations, rubrics, tests, questions, plagiarism results).  
- **File Storage Layer:** submissions, rubrics (JSON), feedback (reports).  

---

## 10. Component Interaction Flow
Submission → stored in DB → evaluation job queued → Python worker → Evaluator Agent (rubric-based scoring + feedback) → Plagiarism Agent (similarity checks) → faculty review → student notified.  

---

## 11. Database Schema
- **Assignments:** metadata, deadlines, instructions.  
- **Rubrics & Criteria:** detailed scoring rules, Bloom’s taxonomy, CO mapping.  
- **Submissions:** student uploads, metadata, status, plagiarism flags, anonymized IDs, versioning.  
- **Evaluations:** AI + faculty scores, reasoning, feedback, overrides, final score.  
- **Evaluation Rubric Scores:** per-criterion breakdown.  
- **Plagiarism Results:** similarity scores, type (text/code).  
- **Tests & Quizzes:** tests, questions, options, student attempts, answers.  

---

## 12. Risks & Mitigations
- AI scoring bias → faculty override learning + rubric validation.  
- False plagiarism positives → manual review workflow + adjustable thresholds.  
- Multimodal accuracy issues → RAG + sample validation.  
- Privacy breaches → anonymization + encryption + zero-trust access.  
- Faculty resistance → transparent explanations + override controls.  

---

## 13. Deliverables
- Streamlit prototype with submission/evaluation workflow.  
- Sample dataset (500 submissions).  
- In-house plagiarism engine.  
- Documentation (UML, API specs, deployment guide).  
- Faculty training materials + demo dataset.  

---

## 14. Evaluation Metrics
- Scoring accuracy >90% agreement with faculty.  
- Consistency <5% variance across repeated evaluations.  
- Feedback quality NPS >8/10.  
- Plagiarism detection >95% precision/recall.  
- Efficiency: 100 submissions/minute on 8GB RAM.  

---

## 15. Phase Roadmap & Timeline
- **Phase I (6 weeks):** CSE dept, basic multimodal eval + plagiarism.  
- **Phase II:** institute-wide, advanced analytics + adaptive learning.  

**Week-by-week milestones:**  
1. Schema + submission types.  
2. Multimodal evaluator agent.  
3. Streamlit UI + rubric builder.  
4. Plagiarism engine + analytics.  
5. Security + faculty review flow.  
6. Testing + demo.  

---

## 16. Faculty Feedback & Validation
Template for project priority, must-have/nice-to-have features, plagiarism concerns, scoring accuracy requirements.  
Validation checklist: faculty review, HOD approval, registrar consultation, IT feasibility, budget/timeline approval.  

---

## 17. Dependencies & Prerequisites
- **Data:** rubrics, question banks, sample submissions.  
- **Technical:** server (8GB RAM, 20GB storage, 4-core CPU), MySQL 8.0+, PHP 8.1+, Python 3.10+, Ollama LLM, FastAPI, LangChain.  
- **Organizational:** academic council approval, test accounts, faculty training, system admin.  
- **External:** SMTP server, integration APIs (Yojanā, Anvesha).  

---

## 18. Compliance & Regulatory
- GDPR compliance (access, erasure, consent).  
- Indian IT Act 2000 (reasonable security practices, encryption).  
- Institutional academic policies.  
- Accessibility (WCAG 2.1 AA).  

---

## 19. Support & Maintenance
- **Level 1:** helpdesk (account access, navigation).  
- **Level 2:** technical team (submission issues, pipeline errors).  
- **Level 3:** development team (bug fixes, optimization).  
- **Schedule:** daily backups, weekly monitoring, monthly updates, quarterly load testing, annual audits.  

---

## 20. Version History
- v0.7 → initial requirements + plagiarism appendix.  
- v0.8 → agentic workflows, NFRs, in-house plagiarism.  
- v0.9 → risks

