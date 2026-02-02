 
# Component: Scheduler / Task Runner

## Overview
The Scheduler / Task Runner module provides a unified mechanism for automating recurring tasks across all projects. It ensures consistency, reliability, and maintainability by centralizing scheduled operations such as report generation, email notifications, data backups, and system cleanups.

## Features
- **Recurring Jobs**: Automate tasks at fixed intervals (daily, weekly, monthly).
- **Cron Integration**: Use system cron jobs for lightweight scheduling.
- **Task Queue**: Support queued execution for bulk or long-running jobs.
- **Error Handling**: Log failures and retry tasks where appropriate.
- **Role-Based Control**: Restrict scheduling capabilities to admin roles.
- **Audit Logging**: Record task execution, success, and failure events.

## Architecture
- **Core Components**:
  - Task Runner (executes defined jobs)
  - Scheduler (cron or in-app scheduler)
  - Job Registry (list of available tasks)
- **Dependencies**:
  - Event Logger (records task execution)
  - Configuration Manager (defines schedules and limits)
  - Mail Sender (for notifications on task completion/failure)
- **Interfaces**:
  - PHP: Cron jobs invoking PHP scripts
  - Python: APScheduler / Celery for distributed scheduling

---

## Usage Guidelines
- **Consistency**:
  - All projects must use the shared scheduler for recurring tasks.
  - No ad-hoc cron scripts outside the framework.
- **Security**:
  - Restrict task creation/modification to admin roles.
  - Validate task definitions before execution.
- **Error Handling**:
  - Log all task failures in Event Logger.
  - Implement retries for transient errors.
- **Best Practices**:
  - Keep tasks modular and reusable.
  - Avoid long-running tasks in cron — use queues instead.
  - Document all scheduled jobs in project onboarding manuals.

---

## Example: PHP (Cron Job)
```bash
# Cron entry to run cleanup.php every day at midnight
0 0 * * * php /var/www/project/scripts/cleanup.php >> /var/log/cleanup.log 2>&1
```

```php
// cleanup.php
try {
    $pdo->beginTransaction();
    $stmt = $pdo->prepare("DELETE FROM sessions WHERE expiry < NOW()");
    $stmt->execute();
    $pdo->commit();
    $eventLogger->info("Expired sessions cleaned successfully");
} catch (Exception $e) {
    $pdo->rollBack();
    $eventLogger->error("Cleanup failed: " . $e->getMessage());
}
```

---

## Example: Python (APScheduler)
```python
from apscheduler.schedulers.background import BackgroundScheduler
import logging

scheduler = BackgroundScheduler()

def cleanup_sessions():
    try:
        # Example DB cleanup logic
        logging.info("Expired sessions cleaned successfully")
    except Exception as e:
        logging.error(f"Cleanup failed: {e}")

scheduler.add_job(cleanup_sessions, 'cron', hour=0, minute=0)
scheduler.start()
```

---

## Best Practices
- Use cron for lightweight jobs, APScheduler/Celery for complex workflows.
- Always log task execution results.
- Keep job definitions centralized in a registry.
- Monitor task performance and optimize schedules.
- Provide notification on critical task failures.

---

## Future Enhancements
- Distributed task execution with Celery/RabbitMQ.
- Web-based dashboard for managing scheduled jobs.
- Dynamic scheduling via REST API.
- AI-driven optimization of task schedules.
 
---
 

