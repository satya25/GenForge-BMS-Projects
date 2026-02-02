
---

# GenAI Project 2  
**Code Name:** Prabodha (प्रबोध – Enlightenment)  
**Title:** Adaptive Learning & Assessment System  
**Version:** v1.0 (Baselined)  
**Date:** Jan 2026  
**Prepared By:** GenForge Workshop Team  

---

## 1. Executive Summary
Prabodha is an intelligent educational ecosystem designed to eliminate “one-size-fits-all” learning. By leveraging Local LLMs (Ollama) and agentic workflows, the system dynamically assesses student understanding of topics, prescribes remedial learning paths, and recommends personalized study materials. It acts as a **Personal Tutor** within the AIAlchemy One portal.

---

## 2. Objectives
- Generate adaptive assessments after topic completion.  
- Recommend personalized resources (videos, PDFs, practice problems).  
- Track student progress and adjust difficulty dynamically.  
- Provide dashboards for students and faculty with actionable insights.  

---

## 3. Scope
### In-Scope
- Adaptive quiz generation aligned to topics.  
- Personalized resource recommendations.  
- Dynamic difficulty adjustment.  
- Student dashboards and faculty heatmaps.  
- Exportable reports.  

### Out-of-Scope (Phase I)
- Mobile native apps (web-responsive only).  
- Full multi-language support (planned Phase II).  
- Institute-wide rollout (initially CSE Department).  

---

## 4. System Architecture & Tech Stack
- **Frontend:** Streamlit / React for student dashboard & quiz UI.  
- **Backend:** Python FastAPI + LangChain + Ollama (local Llama 3/Mistral).  
- **Admin & Persistence:** PHP 8.x + MySQL (BMS Intelligence Portal integration).  
- **Storage:** Supabase / local storage for PDFs, videos, notes.  

---

## 5. Agentic Workflow
- **Quiz Generator Agent** → transforms topic metadata into Bloom’s Taxonomy-aligned MCQs.  
- **Evaluator Agent** → gap analysis, categorizes weak areas.  
- **Recommender Agent** → maps deficiencies to resource bank.  
- **Progress Agent** → tracks longitudinal progress, adjusts difficulty multipliers.  

---

## 6. Functional Requirements
- **Adaptive Learning Path:** quizzes generated instantly after topic completion; difficulty adjusted based on score thresholds.  
- **Resource Recommendation Engine:** multi-modal suggestions (video, document, practice problem); targeted feedback loop.  
- **Analytics & Reporting:** student radar charts, faculty heatmaps, class-wide performance reports.  
- **Dashboards:** personalized student progress visualization; faculty PDF exports.  
- **Admin Content Management (Phase II):** upload topics/resources, auto-tagging difficulty levels.  

---

## 7. Database Schema (Core Tables)
```sql
students(student_id, name, current_level)
topics(topic_id, subject_code, title)
resources(res_id, topic_id, type, url)
quizzes(quiz_id, topic_id, content JSON)
attempts(attempt_id, student_id, quiz_id, score, weak_areas JSON)
```

---

## 8. Deliverables
- Functional prototype (adaptive assessments + recommendations).  
- Sample dataset (topics, quizzes, resources).  
- Documentation (system design, usage guide, test cases).  
- GitHub repo + demo video.  

---

## 9. Implementation Roadmap (MVP – 6 Weeks)
- **Week 1–2:** MySQL schema, student login, topic repository.  
- **Week 3–4:** FastAPI + Ollama integration for quiz generation/scoring.  
- **Week 5:** Recommendation logic (weak areas → resources).  
- **Week 6:** Faculty dashboard, PDF reports, demo.  

---

## 10. Evaluation Metrics
- Quiz relevance ≥90% topic alignment.  
- Quiz generation latency <3 seconds.  
- Recommendation accuracy ≥85%.  
- Dashboard load <2 seconds.  
- Student NPS ≥8/10.  
- Improvement index: ≥15% score increase after remedial path.  

---

## 11. Success Criteria
- Students receive adaptive quizzes and targeted resources.  
- Faculty gain actionable insights into class weaknesses.  
- Demonstrated improvement in student performance.  
- Usability validated via demo day acceptance criteria.  

---

## 12. Version History
- v0.9 → Draft requirements and scope.  
- v1.0 → Consolidated requirements, architecture, student guide, evaluation metrics.  

---

## 13. Approval & Sign-Off
| Role | Name | Signature | Date |
|------|------|-----------|------|
| Project Sponsor (HOD) | _____________ | _____________ | ______ |
| Technical Lead | _____________ | _____________ | ______ |
| Faculty Representative | _____________ | _____________ | ______ |
| IT Infrastructure Head | _____________ | _____________ | ______ |

---

**Document Status:** ✅ Ready for Approval & Implementation  
**Next Steps:** Faculty validation → Technical feasibility → Development kickoff  

---

#
