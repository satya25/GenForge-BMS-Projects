# Project Samaya – Use Cases, User Stories, Actors, Workflows

## 1. Actors
- **Faculty:** Manage deadlines for blueprint creation and paper generation.
- **Students:** Access exam schedules and preparation timelines.
- **HODs:** Oversee department-level scheduling and compliance.
- **Exam Coordinators:** Manage exam timetables and logistics.
- **Administrators:** Maintain institute-wide academic calendar.

## 2. Use Cases
### UC-1: Create Academic Calendar
- **Actor:** Administrator
- **Precondition:** Administrator logged in with valid credentials.
- **Steps:**
  1. Navigate to calendar management.
  2. Add academic events (classes, exams, deadlines).
  3. Save and publish calendar.
- **Postcondition:** Academic calendar available to all stakeholders.

### UC-2: Faculty Deadline Tracking
- **Actor:** Faculty
- **Precondition:** Faculty logged in with valid credentials.
- **Steps:**
  1. Access faculty dashboard.
  2. View upcoming deadlines for blueprint creation and paper generation.
  3. Receive automated reminders.
- **Postcondition:** Faculty stays on track with deadlines.

### UC-3: Exam Scheduling
- **Actor:** Exam Coordinator
- **Precondition:** Exam timetable needs to be created.
- **Steps:**
  1. Access scheduling module.
  2. Select courses and exam slots.
  3. System checks for conflicts.
  4. Publish exam schedule.
- **Postcondition:** Exam schedule available to students and faculty.

## 3. User Stories
- As a **faculty member**, I want reminders for deadlines so that I can prepare papers on time.  
- As a **student**, I want clear exam schedules so that I can plan my preparation.  
- As an **exam coordinator**, I want conflict detection so that exam timetables are error-free.  

## 4. Workflows
### Workflow 1: Academic Calendar Creation
1. Administrator logs in.
2. Adds academic events.
3. System validates entries.
4. Calendar published to all stakeholders.

### Workflow 2: Faculty Deadline Tracking
1. Faculty logs in.
2. Dashboard displays upcoming deadlines.
3. System sends automated reminders.
4. Faculty prepares papers accordingly.

### Workflow 3: Exam Scheduling
1. Exam coordinator logs in.
2. Selects courses and slots.
3. System checks for conflicts.
4. Schedule published.
5. Students and faculty notified.
