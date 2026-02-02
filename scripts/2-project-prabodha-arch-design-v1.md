# Project Prabodha – System Architecture & Detailed Design

## 1. Architectural Overview
Prabodha is designed as the adaptive learning companion for students. It provides guided practice, personalized feedback, and adaptive learning pathways, while enabling faculty to monitor progress. It integrates with Yojanā (question bank) and Anvesha (analytics) to ensure alignment with course outcomes.

**Layers:**
- **Presentation Layer:** Student practice interface, faculty dashboards.
- **Application Layer:** Adaptive learning engine, feedback generator, progress tracker.
- **Data Layer:** Question bank metadata (via Yojanā), student performance logs.
- **Integration Layer:** APIs to Anvesha (analytics) and Samaya (scheduling).

## 2. Components
- **Practice Module:** Student-facing interface for MCQs, short answers, problem-solving.
- **Adaptive Engine:** Adjusts difficulty dynamically based on student performance.
- **Feedback Service:** Provides hints, explanations, and corrective guidance.
- **Progress Tracker:** Logs student attempts, maps progress against Bloom’s taxonomy and COs.
- **Faculty Dashboard:** Displays student progress and engagement metrics.
- **Integration APIs:** Connects with Yojanā for question bank access and Anvesha for analytics.

## 3. Data Flow
1. **Input:** Question metadata from Yojanā; student responses from practice sessions.
2. **Processing:** Adaptive engine evaluates performance, adjusts difficulty, generates feedback.
3. **Output:** Student progress reports, faculty dashboards, analytics integration.

## 4. Database Design (Application-managed integrity)
- **Tables:**
  - `students` (student_id, name, course_id, login_credentials)
  - `practice_sessions` (session_id, student_id, subject_id, start_time, end_time)
  - `responses` (response_id, session_id, question_id, answer, correctness, feedback)
  - `progress_metrics` (metric_id, student_id, bloom_level, CO_mapping, score, timestamp)

**Note:** No foreign key constraints; integrity enforced at application layer.

## 5. API Specifications
- **POST /practice/start/{student_id}/{subject_id}**
- **POST /practice/submit-response/{session_id}/{question_id}**
- **GET /progress/{student_id}**
- **GET /faculty-dashboard/{course_id}**
- **Integration APIs:** `/yojana/questions`, `/anvesha/analytics`

## 6. Deployment Topology
- **Frontend:** Web/mobile interface for students and faculty.
- **Backend:** PHP (PDO) services with transaction-wrapped queries.
- **Database:** MySQL with application-enforced integrity.
- **Adaptive Engine:** Python microservice for difficulty scaling and feedback generation.
- **Security:** Role-based authentication, secure API tokens, audit logs.

## 7. Design Constraints
- No foreign key constraints; integrity enforced in application logic.
- All DB writes wrapped in transactions + try–catch.
- Adaptive engine modularized for future AI enhancements.
