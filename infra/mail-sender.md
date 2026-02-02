# Component: Mail Sender

## Overview
The Mail Sender module provides a unified mechanism for sending emails across all projects. It is responsible for notifications, alerts, confirmations, and communication workflows. To ensure reliability and security, **PHPMailer** is the only recommended and supported library for this component.

## Features
- **Email Notifications**: Send automated alerts to users (e.g., registration confirmation, password reset).
- **Bulk Messaging**: Support for sending announcements to groups of students or faculty.
- **Attachments**: Ability to send files (PDFs, reports, etc.) securely.
- **HTML & Plain Text Support**: Rich formatting for emails while maintaining fallback plain text.
- **SMTP Integration**: Configurable to work with institutional mail servers or external providers (e.g., Gmail, Outlook).
- **Error Handling**: Graceful failure with logging via the Event Logger module.

## Architecture
- **Core Components**:
  - PHPMailer library (mandatory)
  - SMTP configuration manager
  - Mail queue (optional for bulk sending)
- **Dependencies**:
  - Event Logger (to record mail send attempts and failures)
  - Configuration Manager (to store SMTP credentials and settings)
- **Interfaces**:
  - PHP classes wrapping PHPMailer for standardized usage
  - REST API endpoints for triggering mail sends from other modules

## Usage Guidelines
- **Mandatory Standard**: All projects must use **PHPMailer**. No custom mail scripts or alternative libraries are allowed.
- **Configuration**:
  - Centralize SMTP settings in the Configuration Manager.
  - Use environment variables for credentials (never hardcode passwords).
- **Security**:
  - Enforce TLS/SSL for all SMTP connections.
  - Validate recipient addresses before sending.
- **Best Practices**:
  - Use HTML templates for consistent branding.
  - Provide plain text fallback for accessibility.
  - Log all send attempts and failures in the Event Logger.
  - Avoid sending bulk emails synchronously — use a queue if needed.

## Future Enhancements
- Integration with institutional mail servers for official communication.
- Support for templating engines (e.g., Twig) for dynamic email content.
- Scheduled mail delivery (via Scheduler/Task Runner).
- Tracking and analytics (open rates, bounce handling).
