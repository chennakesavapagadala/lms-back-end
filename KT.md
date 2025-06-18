KT Document: Scalable Backend for Learning Management System (LMS)

Prepared by: Pagadala Chennakesava.
Company: Arkhya Tech India Pvt. Ltd.
Role: Backend Developer
Experience: 1.6 Years
Project Duration: Nov 2023 – Apr 2025
Date of Handover: April 23, 2025

1. Project Overview
Project Name: Scalable Backend for Learning Management System (LMS)

Purpose: Manage course content, users, assignments, and progress tracking for an internal/external ed-tech platform.

Key Stakeholders: Product Manager, Tech Lead, QA Lead

Tech Stack
Language: Python

Framework: Django REST Framework

Database: PostgreSQL 14

Deployment: Docker, AWS EC2

CI/CD: GitHub Actions

2. System Architecture
Microservice-based structure with modular apps:

User Service: Authentication, roles, profiles

Course Service: Creation, listing, enrollment

Assignment Service: Submissions and results

API Gateway: NGINX reverse proxy

Database: PostgreSQL (separate schemas per service)

Caching: Redis

Task Queue: Celery (planned)

3. Codebase Walkthrough
Repository: github.com/arkhyatech/lms-backend

Branch Strategy:

main: Production

develop: Active development

Key Folders
apps/ – Django apps (users, courses, assignments)

utils/ – Common helpers

configs/ – Environment-based settings

Local Setup
bash
Copy
Edit
git clone https://github.com/arkhyatech/lms-backend.git
cp .env.example .env
docker-compose up --build
4. Database
PostgreSQL 14

Schema image: docs/db_schema.png

Alembic used for migrations (for compatibility with other services)

5. API Design
Swagger docs hosted at: https://lms-api.arkhyatech.com/docs

Authentication: JWT (SimpleJWT)

Rate Limiting: 100 requests/min/user (NGINX + DRF throttling)

6. CI/CD & Deployment
GitHub Actions for:

Test → Build Docker Image → Deploy to EC2

Docker Compose used for local, staging

Production hosted on AWS EC2 + NGINX

7. Monitoring
Logs: AWS CloudWatch

Error Tracking: Sentry

Dashboard: Grafana + Prometheus

8. Security
Secrets managed via AWS Secrets Manager

HTTPS enforced (NGINX + Let's Encrypt)

SQL Injection and XSS prevention via Django ORM/Serializers

9. Testing
pytest with factory_boy

Coverage: ~85%

Integration tests auto-run before deploy to staging

10. Documentation
README.md – Project Overview

docs/dev_onboarding.md – Developer onboarding

Swagger – API Reference

To Do: Update quiz logic diagrams

11. Known Issues
Mobile pagination inconsistency in courses list

Celery retries fail silently if worker restarts during execution

12. Contacts
Tech Lead: Priya Sharma – priya@arkhyatech.com

QA Lead: Rakesh Mehta – rakesh@arkhyatech.com

DevOps: Anjali Rao – anjali@arkhyatech.com


