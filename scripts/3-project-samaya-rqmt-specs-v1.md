
---

# GenAI Project 1  
**Code Name:** Samaya  
**Title:** Intelligent Timetable & Resource Management System  
**Version:** v1.0 (Baselined)  
**Date:** Feb 2026  
**Prepared By:** GenForge Workshop Team  

---

## 1. Executive Summary
Samaya is an AI-powered timetable and resource management system designed to automate academic scheduling, track real-time occupancy of classrooms and labs, and intelligently resolve conflicts. It leverages agentic AI workflows (Planner, Resolver, Query, Notifier) with CSP solvers and LLM orchestration to deliver personalized timetables (personalTT), optimized resource utilization, and institute-wide scalability.

---

## 2. Objectives
- Automate department-wide timetable generation.  
- Provide personalized timetables for students and faculty.  
- Track and visualize room/lab occupancy in real time.  
- Enable resource reuse/exchange requests with AI-powered conflict resolution.  
- Integrate with external calendars and notification systems.  

---

## 3. Scope
### In-Scope
- Automated timetable generation with multi-constraint optimization.  
- PersonalTT export (PDF, ICS, CSV, JSON).  
- Occupancy dashboards with heatmaps.  
- Resource reuse requests and conflict resolution.  
- Calendar integration (Google, Outlook, Apple).  
- Notifications and analytics dashboards.  

### Out-of-Scope (Phase I)
- Examination timetables.  
- Attendance tracking.  
- Course registration/enrollment.  
- Faculty workload compensation.  
- Transport/hostel scheduling.  
- IoT sensor integration (Phase II).  
- Native mobile apps (web-responsive only).  

---

## 4. Stakeholders & Roles
- **Primary Users:** Students, Faculty, Lab Staff, HOD, Office Staff, Management, Administrators.  
- **Secondary Users:** Visiting faculty, Professors of Practice, Guest lecturers, Academic Council, Maintenance staff.  

---

## 5. Functional Requirements
- **Authentication & RBAC:** MFA, JWT, audit logs, delegation.  
- **Data Input:** Web forms, Excel/CSV import, MySQL sync, academic calendar management.  
- **Faculty Availability:** weekly calendars, preferences, exceptions.  
- **Resource Management:** room/lab master data, facilities, availability, prioritization rules.  
- **Timetable Generation:** hard constraints (no double-booking, availability, capacity, working hours), soft constraints (minimize gaps, preferences, distribution, optimization).  
- **Conflict Detection & Resolution:** real-time alerts, batch validation, AI-powered resolution with negotiation workflows.  
- **PersonalTT:** individualized timetables, responsive UI, multi-format export, calendar sync, sharing.  
- **Occupancy Management:** live dashboards, queries, utilization analytics, lab-specific booking/maintenance.  
- **Reuse Requests:** submission, AI-powered processing, approval workflows, tracking, analytics.  
- **Agentic Workflows:** Planner, Resolver, Query, Notifier agents orchestrated via LangChain.  
- **Notifications:** multi-channel alerts (email, in-app, SMS), templates, preferences, history.  
- **Reporting & Analytics:** pre-built reports, custom builder, visualizations, exports, scheduled reports.  
- **Administration:** system config, user management, archival, backup/recovery.  

---

## 6. Non-Functional Requirements
- **Performance:** timetable generation <5s, occupancy queries <1s, conflict detection <2s.  
- **Scalability:** 5K+ students, 500+ faculty, 100+ rooms/labs, 5+ years archives.  
- **Reliability:** 99.5% uptime, daily backups, disaster recovery RPO <24h, RTO <4h.  
- **Security:** AES-256 encryption, TLS 1.3, bcrypt passwords, audit logs retained 2 years, anonymization.  
- **Usability:** WCAG 2.1 AA compliance, responsive design, multi-language support, contextual help.  
- **Maintainability:** modular architecture, documentation, semantic versioning, structured logging, plugin support.  
- **Deployment:** local XAMPP/LAMP, MySQL 8.0+, Python FastAPI, Ollama LLM, optional Docker.  
- **Accuracy:** 100% conflict-free timetables, ≥80% soft constraint satisfaction, ≥90% NLQ accuracy.  

---

## 7. System Architecture
- **Frontend:** PHP 8.1 MVC, Bootstrap 5, Chart.js, FullCalendar.js.  
- **Backend:** Python FastAPI, LangChain, Ollama (Mistral/Llama), OR-Tools CSP solver.  
- **Database:** MySQL 8.0+, SQLAlchemy ORM.  
- **Integration:** Google/Microsoft calendar APIs, SMTP, Twilio (optional), Excel/CSV parsers.  
- **Agentic AI Architecture:** Planner, Resolver, Query, Notifier agents orchestrated via LangChain.  
- **Data Flows:** defined for timetable generation and resource reuse requests.  

---

## 8. Database Schema
- **Users & Roles:** users, roles, audit_log.  
- **Academic Structure:** departments, courses, sections, faculty, faculty_courses.  
- **Resources:** buildings, rooms, labs, room_availability.  
- **Timetables:** timetables, timetable_slots, faculty_availability.  
- **Requests & Approvals:** reuse_requests, request_approvals, affected_entities.  
- **System Config:** academic_calendar, system_config, notifications, notification_preferences.  
- **Indexes:** composite indexes for timetable slots, faculty availability, room occupancy, notifications, full-text search.  

---

## 9. CSP Implementation
- **Hard Constraints:** no double-booking, availability, capacity, duration, working hours, lab exclusivity.  
- **Soft Constraints:** minimize gaps, faculty preferences, distribution, avoid back-to-back, morning core courses, minimize transitions, room size optimization, lab contiguity.  
- **Solving Strategy:** OR-Tools for hard constraints, simulated annealing for soft optimization, LLM-assisted decomposition, iterative relaxation.  

---

## 10. Calendar Integration
- Supported platforms: Google, Outlook, Apple, ICS.  
- Features: one-time export, sync-enabled export, bidirectional sync (Phase II).  
- Event details: course, section, room, faculty, recurrence, reminders, color coding.  

---

## 11. Notifications
- Templates for schedule changes, reuse approvals, conflict warnings.  
- Multi-channel delivery (email, in-app, SMS).  
- Preferences and history tracking.  

---

## 12. Risks & Mitigations
- LLM hallucinations → validation + fallback logic.  
- CSP solver failures → iterative relaxation, partial solutions.  
- Data import inconsistencies → strict validation, error highlighting.  
- Scalability → Docker scaling, phased rollout.  
- Faculty resistance → training, manual overrides, pilot adoption.  
- API rate limits → batching, fallback to ICS.  
- Downtime → load balancing, stress testing, manual fallback.  
- Data loss → version control, undo/redo, backups.  
- Suboptimal swaps → multiple alternatives, transparent scoring.  
- Hardware limits → quantized models, smaller LLMs, optional GPU/cloud.  

---

## 13. Deliverables
- **Software Artifacts:** web app, backend services, database schema, sample datasets.  
- **Documentation:** technical (architecture, schema, API, CSP), user manuals, tutorials, guides.  
- **Training Materials:** slides, exercises, cheat sheets, demo video.  
- **Deployment Artifacts:** installation packages, Docker Compose, requirements.txt, SQL scripts, Ollama model download, config templates.  

---

## 14. Evaluation Metrics
- **Technical Performance:** generation speed, conflict-free rate, soft constraint satisfaction, query response, page load, concurrent users, DB performance.  
- **Functional Accuracy:** conflict detection, calendar export, faculty availability, room capacity, NLQ classification.  
- **User Experience:** NPS, task completion, personalTT downloads, generation time, support ticket volume.  
- **Business Impact:** room utilization, faculty time savings, schedule stability, reuse resolution time.  

---

## 15. Phase I vs Phase II
- Phase I → CSE-only, core features, semi-automated conflict resolution, one-way calendar export.  
- Phase II → institute-wide, IoT sensors, advanced analytics, bidirectional sync, fully automated resolution, multi-server/cloud deployment, fine-tuned LLMs.  

---

## 16. Faculty Feedback & Validation
- Structured template for feature priorities, preferences, concerns, calendar integration, reuse requests.  
- Validation checklist: faculty review, HOD approval, registrar consultation, IT feasibility, budget/timeline approval, sample data secured.  

---

## 17. Dependencies & Prerequisites
- **Data:** course catalog, faculty list, room/lab inventory, student sections, academic calendar, historical timetables.  
- **Technical:** server specs, MySQL, PHP, Python, Ollama, OR-Tools, SMTP, Google Cloud project (optional).  
- **Organizational:** academic council approval, test accounts, faculty training, system admin, change management plan.  
- **External:** Google/Microsoft calendar APIs, SMTP server.  

---

## 18. Compliance & Regulatory
- GDPR (access, erasure, consent).  
- Indian IT Act 2000 (