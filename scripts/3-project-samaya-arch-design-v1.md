# Project Samaya – System Architecture & Detailed Design

## 1. Architectural Overview
Samaya is the institute’s centralized academic scheduling and time management system. It streamlines exam scheduling, faculty deadlines, and academic calendar management, while integrating with Yojanā (paper generation), Anvesha (analytics), and Sangrah (archival).

**Layers:**
- **Presentation Layer:** Web dashboards for faculty, students, exam coordinators, administrators.
- **Application Layer:** Scheduling engine, deadline tracker, conflict detection service.
- **Data Layer:** Academic calendar repository, exam timetable records, faculty deadline logs.
- **Integration Layer:** APIs to Yojanā (paper readiness), Anvesha (analytics), Sangrah (archival).

## 2. Components
- **Calendar Module:** Centralized academic calendar with role-based views.
- **Scheduling Engine:** Exam timetable creation with conflict detection.
- **Deadline Tracker:** Faculty reminders for blueprint creation and paper generation.
- **Notification Service:** Automated alerts for students and faculty.
- **Integration APIs:** Connects with Yojanā for paper readiness, Anvesha for analytics, Sangrah for archival.

## 3. Data Flow
1. **Input:** Academic events from administrators; exam slots from coordinators; deadlines from faculty workflows.
2. **Processing:** Scheduling engine validates conflicts, deadline tracker generates reminders.
3. **Output:** Published academic calendar, exam timetables, faculty notifications.

## 4. Database Design (Application-managed integrity)
- **Tables:**
  - `academic_calendar` (event_id, event_type, subject_id, start_date, end_date, created_by)
  - `exam_schedule` (exam_id, subject_id, slot_id, coordinator_id, status)
  - `faculty_deadlines` (deadline_id, faculty_id, subject_id, task_type, due_date, reminder_sent)
  - `notifications` (notification_id, recipient_id, message, timestamp, status)

**Note:** No foreign key constraints; integrity enforced at application layer.

## 5. API Specifications
- **POST /calendar/create-event**
- **GET /calendar/view/{role}/{subject}**
- **POST /schedule/create-exam**
- **GET /schedule/view/{exam_id}**
- **GET /faculty/deadlines/{faculty_id}**
- **Integration APIs:** `/yojana/paper-status`, `/anvesha/analytics`, `/sangrah/archive`

## 6. Deployment Topology
- **Frontend:** Web dashboards for faculty, students, coordinators, administrators.
- **Backend:** PHP (PDO) services with transaction-wrapped queries.
- **Database:** MySQL with application-enforced integrity.
- **Notification Service:** Python/Node microservice for reminders and alerts.
- **Security:** Role-based authentication, secure API tokens, audit logs.

## 7. Design Constraints
- No foreign key constraints; integrity enforced in application logic.
- All DB writes wrapped in transactions + try–catch.
- Scheduling engine must guarantee conflict-free timetables.
- Modular design for integration with ERP in future phases.
