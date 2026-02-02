# Project Sangrah – Deployment & Operations Guide

## 1. Introduction
This document outlines the deployment, operations, and maintenance strategy for Project Sangrah. It ensures smooth rollout of archival services, reliable performance for faculty and administrators, and secure operations across environments.

## 2. Deployment Architecture
- **Frontend:** Web dashboards for faculty, HODs, administrators hosted on Apache/Nginx.
- **Backend:** PHP (PDO) services deployed on application servers.
- **Database:** MySQL with application-enforced integrity.
- **Archival Service:** Python/Flask microservice containerized via Docker for version control and retrieval.
- **Integration APIs:** RESTful endpoints for Yojanā (paper generation), Viveka (evaluation), Anvesha (analytics).

## 3. Environment Setup
- **Development:** Local Docker containers seeded with sample papers and blueprints.
- **Staging:** Mirror of production with anonymized datasets for archival and retrieval testing.
- **Production:** High-availability cluster with load balancer and failover nodes.

## 4. CI/CD Pipeline
- **Source Control:** GitHub/GitLab with branching strategy.
- **Build:** Automated builds triggered on commit.
- **Test:** Unit, integration, and regression tests executed in staging.
- **Deploy:** Automated deployment to production via CI/CD pipeline.
- **Rollback:** Version-controlled rollback scripts available.

## 5. Backup & Recovery
- **Database Backups:** Daily incremental, weekly full backups.
- **File Backups:** Papers, blueprints, and usage logs archived securely.
- **Recovery:** Disaster recovery plan with RTO ≤ 4 hours, RPO ≤ 24 hours.

## 6. Monitoring & Logging
- **Monitoring Tools:** Prometheus + Grafana dashboards.
- **Metrics:** CPU, memory, API latency, archival throughput.
- **Logging:** Centralized log management with ELK stack.
- **Alerts:** Automated alerts for anomalies, downtime, or failed jobs.

## 7. Security & Compliance
- Role-based authentication with secure API tokens.
- HTTPS enforced across all endpoints.
- Audit logs maintained for all archival actions.
- Compliance with accreditation and institutional data protection standards.

## 8. Operations Checklist
- Verify environment readiness before deployment.
- Run smoke tests post-deployment.
- Monitor archival throughput and retrieval accuracy.
- Archive logs weekly.
- Conduct monthly security audits.

## 9. Maintenance Strategy
- Patch releases every 2 weeks.
- Major upgrades every semester.
- SLA: Critical issues resolved within 24 hours.
- Escalation matrix defined for faculty, HODs, administrators.

## 10. Deployment Schedule
- Development → Staging: Week 1
- Staging → Production: Week 2
- Monitoring & Feedback: Week 3
- Continuous Operations: Ongoing
