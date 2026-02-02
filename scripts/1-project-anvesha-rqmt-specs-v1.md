
---

# GenAI Project 1  
**Code Name:** Anvesha  
**Title:** Intelligent Result Analysis & Backlog Tracking System  
**Version:** v1.0 (Baselined)  
**Date:** Jan 02, 2026  
**Prepared By:** GenForge Workshop Team  

---

## 1. Executive Summary
An AI-powered system for comprehensive student result analysis, backlog tracking, and predictive academic insights for engineering institutions. The system combines traditional database operations with Generative AI capabilities to provide natural language query interfaces, automated trend analysis, and proactive student progress monitoring.

---

## 2. Objective
Develop a Generative AI–enabled system to analyze student academic results, track backlog clearance patterns, and provide actionable insights for students, faculty, and administrators. Initial deployment targets the CSE Department with planned scalability to institute-wide operations.

---

## 3. Scope
### 3.1 In-Scope
- Result analysis across subjects, semesters, batches, and years  
- Backlog tracking with attempt history and clearance patterns  
- Paper clearance history with audit trails  
- Predictive analytics for backlog clearance probability  
- Natural language query interface  
- Multi-format data ingestion (ERP, Excel, PDFs, handwriting)  
- Role-based dashboards for students, faculty, HODs, administrators  
- Automated reporting  

### 3.2 Out-of-Scope
- Grade modification or ERP write-back  
- Real-time exam evaluation  
- Attendance tracking  
- Financial data  
- Placement tracking  
- Native mobile apps (web-responsive only)  

---

## 4. Stakeholders & User Roles
### 4.1 Primary Users
- **Students** → personal backlog status, progress trends, risk scores  
- **Faculty** → section performance, at-risk student monitoring  
- **HODs** → department analytics, cohort comparisons  
- **Administrators** → institute-wide analytics, policy insights  
- **Lab Staff** → read-only support  

### 4.2 Secondary Users
- Academic Council (policy insights)  
- Data Entry Operators (batch uploads)  

---

## 5. Functional Requirements
### 5.1 Authentication & Authorization
- Multi-factor authentication, RBAC, session management, audit logging  

### 5.2 Data Ingestion & Processing
- Multi-format input (CSV, PDF, handwriting OCR)  
- Incremental updates, validation rules, OCR confidence scoring  

### 5.3 Backlog Tracking
- Real-time backlog status, historical attempts, categorization, alerts  

### 5.4 Query & Search Interface
- Structured search, NLQ interface, voice-to-text queries, query history  

### 5.5 Analytics & Insights
- Student dashboards (CGPA trends, risk scores)  
- Faculty dashboards (section performance, teaching effectiveness)  
- Department dashboards (cohort analysis, resource allocation, trends)  

### 5.6 Reporting & Visualization
- Pre-built templates, custom report builder, interactive charts, export options  

### 5.7 Agentic AI Workflows
- **Analyzer Agent** → OCR, validation, anomaly detection  
- **Query Agent** → NLQ parsing, SQL generation, conversational responses  
- **Predictor Agent** → trajectory modeling, risk assessment, explainability  
- **Multi-Agent Collaboration** → orchestration, workflow automation, human-in-loop  

### 5.8 Notifications
- Multi-channel alerts (in-app, email, SMS), configurable rules, preferences  

### 5.9 Data Management & Administration
- Academic calendar, subject catalog, user management, system config, archival  

---

## 6. Non-Functional Requirements
- **Performance** → <2s simple queries, <5s NLQ, <10s batch analysis  
- **Scalability** → 10,000+ records, 10+ years retention, partitioning  
- **Reliability** → 99% uptime, backups, disaster recovery  
- **Security** → AES-256, TLS 1.3, JWT, GDPR compliance  
- **Usability** → WCAG 2.1 AA, multilingual, responsive UI  
- **Maintainability** → modular architecture, documentation, logging  
- **Deployment** → XAMPP/LAMP, FastAPI, MySQL, optional Docker  
- **Accuracy** → ≥95% OCR, ≥80% predictive precision  

---

## 7. System Architecture
- **Frontend:** PHP + Bootstrap + Chart.js  
- **Middleware:** FastAPI + LangChain + Ollama  
- **Database:** MySQL + SQLAlchemy + Redis (optional)  
- **AI/ML:** Tesseract, TrOCR, Whisper, Scikit-learn, LightGBM  

### Agent Specifications
- Analyzer Agent → OCR + validation  
- Query Agent → NLQ + SQL generation  
- Predictor Agent → ML forecasts + explainability  
- Action Agent → reports + notifications  

---

## 8. OCR Implementation Strategy
- **Phase I:** Printed PDFs via Tesseract, manual fallback  
- **Phase II:** Handwriting OCR via TrOCR + LLM validation  

---

## 9. Database Schema
- **Users & Roles** → users, roles, audit_log  
- **Academic Structure** → students, subjects, faculty, mappings  
- **Results & Performance** → results, backlogs, cgpa_history  
- **AI/Analytics** → predictions, queries_log, alerts  
- **System Config** → academic_calendar, system_config, ocr_jobs  

---

## 10. Risks & Mitigation
- OCR accuracy, LLM hallucinations, privacy breaches, scalability, adoption resistance, performance degradation, data inconsistency, infrastructure limits, prediction errors.  

---

## 11. Implementation Timeline
- **Weeks 1–6:** DB setup, OCR pipeline, agents, analytics, security, testing  
- **Weeks 7–12:** Bug fixes, Phase II planning, institute-wide rollout prep  

---

## 12. Deliverables
- **Software:** Web app, backend services, database schema  
- **Documentation:** Technical, user, development docs  
- **Training:** Faculty workshops, admin guides  
- **Deployment:** Installation scripts, configs, environment setup  

---

## 13. Evaluation Metrics
- Technical performance (OCR, query speed, prediction accuracy)  
- User experience (NPS, adoption, support tickets)  
- Business impact (time saved, backlog clearance improvement)  
- Model performance (handwriting OCR, NLQ intent accuracy)  

---

## 14. Phase I vs Phase II
- Phase I → CSE only, printed PDFs, single server  
- Phase II → Institute-wide, handwriting OCR, distributed infra, fine-tuned models  

---

## 15. Faculty Feedback & Validation
- Feedback template, validation checklist (faculty, HOD, IT, privacy officer)  

---

## 16. Dependencies & Prerequisites
- Data (student master, results, subjects)  
- Technical (server, MySQL, PHP, Python, OCR, LLMs)  
- Organizational (approvals, test accounts, training sessions)  

---

## 17. Compliance
- GDPR, Indian IT Act, academic integrity, accessibility standards  

---

## 18. Support & Maintenance
- Tiered support (student helpdesk, technical team, dev team)  
- Maintenance schedule (daily, weekly, monthly, quarterly, annual)  

---

## 19. Version History
- v0.7 → Initial requirements  
- v0.8 → Added workflows, NFRs, OCR strategy  
- v0.9 → Risks, timeline, metrics, feedback template  
- **v1.0 → Final requirements with full specifications**  

---

## 20. Approval & Sign-Off
| Role | Name | Signature | Date |
|------|------|-----------|------|
| Project Sponsor (HOD) | _____________ | _____________ | ______ |
| Technical Lead | _____________ | _____________ | ______ |
| Faculty Representative | _____________ | _____________ | ______ |
| IT Infrastructure Head | _____________ | _____________ | ______ |
| Data Privacy Officer | _____________ | _____________ | ______ |

---

**Document Status:** ✅ Ready for Approval & Implementation  
**Next Steps:** Faculty review → Technical feasibility → Development kickoff  

---

This is the **complete frozen requirements spec for Anvesha v1.0**.  

👉 Shall I now prepare the same consolidation workflow for **Samaya** next, so we can start populating `/frozen-requirements/` with the second baselined document?


