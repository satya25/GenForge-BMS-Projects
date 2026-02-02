
---

# GenAI Project 4  
**Code Name:** Sangrah  
**Title:** Intelligent Data Consolidation System  
**Version:** v1.0 (Baselined)  
**Date:** February 2026  
**Prepared By:** GenForge Workshop Team  

---

## 1. Executive Summary
Sangrah is an AI-powered data consolidation system designed to ingest heterogeneous institutional data (CSV, Excel, PDF, DOCX, ERP/LMS exports, cloud storage) and normalize it into a unified schema. It provides anomaly detection, correction suggestions, audit trails, and APIs for integration with other projects (Samaya, Anvesha, Viveka). Sangrah ensures high-quality, reliable, and secure consolidated datasets for analysis, reporting, and downstream applications.

---

## 2. Objectives
- Automate ingestion of multi-format institutional data.  
- Normalize and enrich data into a unified schema.  
- Detect anomalies and suggest corrections using AI agents.  
- Provide consolidated outputs for integration with other systems.  
- Enable monitoring dashboards and role-based access.  
- Ensure compliance with institutional and regulatory data policies.  

---

## 3. Scope
### In-Scope
- Multi-format ingestion (CSV, Excel, PDF, DOCX, text, ERP/LMS, cloud).  
- Schema normalization and metadata enrichment.  
- AI-driven anomaly detection and correction.  
- Consolidated repository with versioning and APIs.  
- Monitoring dashboards with role-based views.  

### Out-of-Scope (Phase I)
- Student-facing APIs (future).  
- Unstructured data ingestion (future).  
- BI tool integration (future).  

---

## 4. Stakeholders & Roles
- **Data Analysts/Faculty:** query consolidated data, view dashboards.  
- **Administrators:** manage ingestion, fix errors, audit trails.  
- **System Integrators:** API access for downstream systems.  
- **Students (future):** read-only API access.  

---

## 5. Functional Requirements
- **Data Sources & Ingestion:** batch (CSV, Excel, PDF, DOCX, text), real-time (ERP/LMS APIs, DB triggers), cloud (OneDrive, Google Drive), institutional sources.  
- **AI-Powered Normalization:** schema mapping, anomaly detection, correction suggestions, multilingual support.  
- **Consolidated Repository:** MySQL/PostgreSQL schema, metadata enrichment, versioned datasets, REST APIs.  
- **Monitoring Dashboard:** ingestion status, error trends, quality scores, role-based drill-down.  
- **Agentic Workflows:** Ingestion Agent, Mapper Agent, Quality Agent, Integration Agent.  

---

## 6. Non-Functional Requirements
- **Performance:** <30s per 10K rows; <5s API response.  
- **Deployment:** local XAMPP/MySQL; Docker optional; no GPU required.  
- **Security:** AES-256 encryption, JWT RBAC, data masking, audit logs.  
- **Scalability:** 30K students, 1M+ rows/year.  
- **Reliability:** 99.9% ingestion success; automated retries.  
- **Compliance:** GDPR principles, institutional data policies.  

---

## 7. Agent Architecture
```
+++
| LLM Core  | (Ollama - Schema Reasoning)
+++
   |
   v
+++
| Ingestion | -> File detection -> OCR/Parser -> Validation
+++
   |
   v
+++
| Tools     | (Tesseract OCR, Pandas, PDFMiner, MySQL)
+++
   |
   v
+++
| Mapper    | -> Schema inference -> Normalization -> Enrichment
+++
   |
   v
+++
| Quality   | -> Anomaly detection -> Correction suggestions -> Audit
+++
   |
   v
+++
| Action    | -> Store in MySQL -> API feeds -> Notifications
+++
```

---

## 8. Data Quality Metrics
- Ingestion success >99%.  
- Schema compliance >95%.  
- Anomaly detection precision >90%.  
- Duplicate rate <1%.  
- Processing speed <30s per 10K rows.  

---

## 9. Risks & Mitigations
- **Schema mapping failures:** human override + learning from corrections.  
- **OCR errors in PDFs:** confidence scoring + manual review queue.  
- **Data privacy breaches:** encryption + RBAC + masking.  
- **Performance bottlenecks:** indexing + batch optimization.  
- **Integration failures:** API contract testing + fallback modes.  

---

## 10. Deliverables
- Streamlit prototype with ingestion + dashboard.  
- Sample dataset collection (100+ files).  
- Central MySQL schema with sample consolidated data.  
- API documentation + integration guides.  
- Deployment scripts + data quality test suite.  

---

## 11. Evaluation Metrics
- Ingestion accuracy >99%.  
- Schema compliance >95%.  
- Processing efficiency <30s per 10K rows.  
- Data quality <1% duplicates, >90% anomaly detection precision.  
- Integration success with Samaya/Anvesha prototypes.  

---

## 12. Phase Roadmap & Timeline
- **MVP (2 weeks):** CSV/Excel/PDF ingestion + basic normalization.  
- **Phase I (4 weeks):** real-time APIs + cloud connectors + dashboards.  
- **Phase II (6 weeks):** AI schema mapping + anomaly detection.  
- **Phase III (future):** unstructured data, BI tool integration, student APIs.  

**Week-by-week milestones:**  
- Week 1 → schema + basic ingestion.  
- Week 2 → PDF/DOCX processing + Streamlit UI.  
- Week 3 → AI agents + schema mapping.  
- Week 4 → APIs + integration tests.  
- Week 5 → dashboard + security.  
- Week 6 → testing + demo.  

---

## 13. Faculty Feedback & Validation
- Template for project priority, must-have/nice-to-have features, data source concerns, integration requirements.  
- Validation checklist: faculty review, HOD approval, registrar consultation, IT feasibility, budget/timeline approval.  

---

## 14. Dependencies & Prerequisites
- **Data:** course catalog, faculty list, room/lab inventory, student sections, academic calendar, historical timetables.  
- **Technical:** server (8GB RAM, 20GB storage, 4-core CPU), MySQL 8.0+, PHP 8.1+, Python 3.10+, Ollama LLM, OR-Tools, SMTP server.  
- **Organizational:** academic council approval, test accounts, faculty training, system admin, change management plan.  
- **External:** Google/Microsoft calendar APIs, SMTP server.  

---

## 15. Compliance & Regulatory
- GDPR compliance (access, erasure, consent).  
- Indian IT Act 2000 (reasonable security practices, encryption).  
- Institutional academic policies.  
- Accessibility (WCAG 2.1 AA, multi-language support).  

---

## 16. Support & Maintenance
- **Level 1:** helpdesk (account access, exports, navigation).  
- **Level 2:** technical team (data upload, pipeline errors, sync issues).  
- **Level 3:** development team (bug fixes, optimization, agent debugging).  
- **Schedule:** daily backups, weekly monitoring, monthly updates, quarterly load testing, annual audits.  

---

## 17. Version History
- v0.7 → initial requirements + roadmap.  
- v0.8 → agentic workflows, NFRs, data quality metrics.  
- v0.9 → risks, timeline, integration specs, feedback template.  
- **v1.0 → February 2026 → frozen requirements baseline.**  

---

## 18. Approval & Sign-Off
| Role | Name | Signature | Date |
|------|------|-----------|------|
| Project Sponsor (HOD) | _____________ | _____________ | ______ |
| Technical Lead | _____________ | _____________ | ______ |
| Faculty Representative | _____________ | _____________ | ______ |
| IT Infrastructure Head | _____________ | _____________ | ______ |
| Academic Council Member | _____________ | _____________ | ______ |

---

**Document Status:** ✅ Ready for Approval & Implementation  
**Next Steps:** Faculty review → Technical demo → Pilot department selection → Development kickoff  
**Contact:** GenForge Workshop Team | [spnigam25@yahoo.com]  

---
 

