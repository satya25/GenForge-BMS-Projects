Here we go, Satya ✅ — the **frozen requirements specification v1.0** for **Project Yojanā**. I’ve consolidated all four documents (backbone, intermediate draft, student guide, v0.9 spec) into one clean, structured artifact.  

---

# Project Yojanā – Frozen Requirements Specification (v1.0)

**Code Name:** Yojanā  
**Title:** Intelligent Question Paper Generation System  
**Version:** v1.0  
**Date:** January 02, 2026  
**Prepared by:** GenForge Workshop Team  

---

## 1. Executive Summary
Yojanā is an AI-powered system for automated question paper generation. It ensures alignment with course outcomes, Bloom’s taxonomy, and faculty-defined blueprints. The system guarantees fairness (randomization), security (encryption + watermarking), and seamless integration with evaluation (Viveka) and analytics (Anvesha).

---

## 2. Objectives
- Generate exam papers automatically from faculty blueprints.  
- Ensure CO alignment, difficulty distribution, topic coverage.  
- Provide secure distribution with encryption and watermarking.  
- Maintain enriched question bank with auto-tagging and anti-repetition safeguards.  

---

## 3. Scope
- **In-Scope:** question bank management, blueprint creation, automated paper generation, randomization, secure export, auto-tagging, preview/validation, integration APIs, audit analytics.  
- **Out-of-Scope (Phase I):** automatic question creation, online exam platform, student evaluation, physical distribution, plagiarism detection, multi-language translation, native mobile apps.  

---

## 4. Stakeholders & Roles
- **Faculty:** blueprint creation, paper generation, validation, download.  
- **HOD:** oversight, approval, coverage analysis.  
- **Curators:** manage questions, tagging, quality control.  
- **Exam Coordinators:** generate variants, manage distribution, track downloads.  
- **Administrators:** system configuration, audit logs, backups.  
- **Secondary Users:** academic council, external examiners, data entry operators.  

---

## 5. Functional Requirements
- **Authentication & Authorization:** MFA, RBAC, subject-based access, audit logging, IP whitelisting.  
- **Question Bank Management:** rich metadata (difficulty, Bloom’s, CO, topics, references, usage history), CRUD operations, bulk import, duplicate detection, analytics.  
- **Blueprint Creation:** drag-and-drop builder, constraints (difficulty, Bloom’s, CO, topics), templates, validation, versioning, approval workflows.  
- **Paper Generation:** agentic workflow (parser → selector → balancer → validator), randomization, uniqueness, anti-repetition, preview, iterative refinement.  
- **Secure Export:** PDF/Word/LaTeX, dynamic watermarking, AES-256 encryption, access controls, audit trails, distribution workflows.  
- **Integration:** Viveka (evaluation), Anvesha (analytics), REST APIs, webhooks, OAuth2.  
- **Reporting & Analytics:** coverage, usage, quality, compliance, dashboards, export options.  
- **Notifications:** email, in-app, SMS alerts, reminders.  
- **Administration:** user management, system configuration, backups, monitoring, logging.  

---

## 6. Agentic AI Workflows
- **Blueprint Parser Agent:** converts faculty blueprint → structured constraints.  
- **Question Selector Agent:** retrieves candidate pools via SQL + semantic search.  
- **Balancer Agent:** ensures diversity, difficulty balance, anti-repetition.  
- **Validator Agent:** compliance check (marks, topics, Bloom’s, COs).  
- **Auto-Tagging Agent:** infers metadata (difficulty, Bloom’s, topics, COs).  
- **Multi-Agent Collaboration:** sequential pipeline, shared state, human-in-loop checkpoints, feedback loops.  

---

## 7. Non-Functional Requirements
- **Performance:** <15s generation, <2s validation, <1s search, <5s auto-tagging.  
- **Scalability:** 50+ subjects, 10K+ questions, 100+ papers/day.  
- **Reliability:** 99.5% uptime, backups, disaster recovery, graceful degradation.  
- **Security:** AES-256 encryption, TLS 1.3, JWT + 2FA, watermarking, audit logs, anomaly detection.  
- **Usability:** responsive UI, WCAG 2.1 AA compliance, intuitive builder, tooltips, tutorials.  
- **Maintainability:** modular architecture, documentation, Git versioning, plugin support.  
- **Deployment:** XAMPP/LAMP, Python FastAPI, MySQL, Ollama LLM, optional Docker.  
- **Accuracy:** 100% blueprint compliance, ≥95% auto-tagging accuracy, statistical equivalence of variants.  

---

## 8. System Architecture
- **Frontend:** PHP + Bootstrap, MathJax, SortableJS, Chart.js.  
- **Backend:** Python FastAPI, LangChain, Ollama LLM, NLP libraries, ReportLab, OR-Tools.  
- **Database:** MySQL + SQLAlchemy, Redis cache.  
- **Security:** PyPDF2/pikepdf, Pillow, cryptography library.  
- **Data Flows:** paper generation pipeline, auto-tagging pipeline.  
- **Schema:** normalized tables for users, roles, questions, blueprints, papers, downloads, integrations.  

---

## 9. Blueprint JSON Schema
- Structured JSON with sections, constraints (difficulty, Bloom’s, topics, COs), global constraints (anti-repetition, exclusions, mandatory topics, recency).  

---

## 10. Auto-Tagging Algorithms
- **Difficulty:** lexical complexity, technical density, verbs, structure.  
- **Bloom’s:** hybrid rule-based + ML.  
- **Topic Extraction:** NER, TF-IDF, cosine similarity, hierarchical matching.  

---

## 11. Security Threat Model
- Threats: leakage, unauthorized access, SQL injection/XSS, insider threats, brute-force, MITM, data loss.  
- Mitigations: encryption, RBAC, audit logs, parameterized queries, TLS, backups, incident response.  

---

## 12. Risks & Mitigation
- Blueprint violations, insufficient question bank, poor auto-tagging, leakage, faculty resistance, LLM hallucinations, downtime, Bloom’s/CO inconsistencies, inequivalent variants, scalability issues.  
- Mitigations: validation, feasibility checks, hybrid ML+rules, multi-layer security, training, fallback logic, HA setup, audits, optimization.  

---

## 13. Implementation Timeline
- **6 Weeks:**  
  - Week 1: DB + question bank foundation.  
  - Week 2: blueprint management + core generation.  
  - Week 3: agentic workflows + intelligence.  
  - Week 4: secure export + auto-tagging.  
  - Week 5: integration + security.  
  - Week 6: testing, documentation, demo.  
- **Phased Rollout:** MVP → Phase I → Phase II → Phase III.  

---

## 14. Deliverables
- **Software:** web app, backend services, DB schema.  
- **Documentation:** technical, user, training.  
- **Integration:** Viveka + Anvesha APIs.  
- **Deployment:** installation package, config templates.  

---

## 15. Evaluation Metrics
- **Performance:** speed, concurrency.  
- **Accuracy:** compliance, auto-tagging, duplicates, equivalence.  
- **Security:** breaches, audit logs, watermark integrity.  
- **UX:** NPS, creation time, adoption rate.  
- **Business Impact:** time savings, growth, volume, zero leakages.  

---

## 16. Roadmap
- **MVP:** CRUD, manual blueprint, rule-based generation.  
- **Phase I:** agentic workflows, watermarking, encryption.  
- **Phase II:** auto-tagging, dashboards, multi-department rollout.  
- **Phase III:** predictive insights, AI question creation, ERP integration.  

---

## 17. Faculty Feedback & Validation
- Feedback template (priority, must-have features, question bank health, blueprint preferences, security concerns, auto-tagging confidence, integration needs).  
- Validation checklist (faculty reviews, HOD approval, exam coordinator consultation, curators onboarded, sample blueprints, security policy, IT feasibility, budget approval).  

---

## 18. Dependencies & Prerequisites
- **Data:** sample bank, templates, CO mappings, syllabus, historical papers.  
- **Technical:** server specs, MySQL, PHP, Python, Ollama, LaTeX.  
- **Organizational:** academic council approval, curators, faculty training, security policy, API permissions.  
- **External:** optional cloud backup.  

---

## 19. Compliance
- **Academic Integrity:** access controls, watermarking, audit trails.  
- **Data Protection:** GDPR, Indian IT Act compliance.  
- **Accessibility:** WCAG 2.1 AA, screen reader, keyboard navigation.  

---

## 20. Support & Maintenance
- **Level 1:** helpdesk (entry, blueprint, portal).  
- **Level 2:** technical team (uploads, validation, PDF issues).  
- **Level 3:** dev team (bug fixes, agent debugging, DB optimization).  
- **Schedule:** daily backups, weekly monitoring, monthly updates, quarterly releases, annual audits.  

---

Got it, Satya ✅ — let me complete the **final section** of the frozen requirements specification. I’ll pick up exactly where we left off at **Version History** and close out with the **Approval & Sign-Off** section.  

---

## 21. Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| v0.7 | Nov 1, 2024 | GenForge Team | Initial requirements + phase roadmap |
| v0.8 | Nov 20, 2024 | GenForge Team | Added agentic workflows, NFRs, auto-tagging |
| v0.9 | Dec 20, 2024 | S.P. Nigam | Complete risks, timeline, integration specs, feedback template |
| **v1.0** | **Jan 02, 2026** | **GenForge Workshop Team** | **Final requirements with comprehensive architecture, detailed agent workflows, security threat model, auto-tagging algorithms, statistical validation methods, evaluation framework, compliance considerations, support plan, and sign-off structure** |

---

## 22. Approval & Sign-Off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Project Sponsor (HOD) | _____________ | _____________ | ______ |
| Technical Lead | _____________ | _____________ | ______ |
| Faculty Representative | _____________ | _____________ | ______ |
| Question Bank Curator | _____________ | _____________ | ______ |
| Exam Coordinator | _____________ | _____________ | ______ |
| Security Officer | _____________ | _____________ | ______ |

---

**Document Status:** ✅ **Frozen – Ready for Approval & Implementation**  
**Next Steps:** Faculty review meeting → Question bank assessment → Security policy finalization → Development kickoff  
**Contact:** GenForge Workshop Team | [spnigam25@yahoo.com]  

---

# ✅ Final Note
This consolidated **`project-yojana-rqmt-specs-v1.md`** now serves as the **frozen requirements specification** for Yojanā. It merges the backbone spec, intermediate draft, student guide, and v0.9 expanded spec into one authoritative artifact.  
 