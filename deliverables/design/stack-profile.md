# Stack Profile

Written once at the start of design. Revisit only if the stack itself changes.

## Backend

- **Framework:** Django 4.x
- **Layout:** models/ selectors/ services/ policies/ api/ infrastructure/
- **What each bucket is for:**
  - `models/` — Django ORM entities (Profile, Skill, Experience, Education, Qualification, PrivacySettings, User, UploadLimit, CV (if persisted), etc.)
  - `selectors/` — Non-trivial reads (e.g., complex profile search queries, aggregations for analytics)
  - `services/` — Business operations with real logic (CV validation, data extraction, profile creation, privacy application, search indexing, notification handling)
  - `policies/` — Authorization rules (e.g., who can view/upload profiles, role-based access)
  - `api/` — Views/serializers, the HTTP boundary (REST endpoints, file upload handling)
  - `infrastructure/` — External systems: file storage (local/media or S3), email service, search engine (if using Elasticsearch), payment gateway (if any)

## Frontend

- **Framework:** React 18 (with Create React App or Vite)
- **Layout:** src/ (components/, hooks/, pages/, services/, api/)
  - Components organized by feature (UploadProfile, ProfileSearch, ProfileView, Notifications, etc.)
  - Custom hooks for data fetching and business logic
  - API service layer for communicating with backend

## Credited abstractions

Things a framework or library already handles well — referenced by use-case design files instead of re-justified each time.

| Library/framework | Credited for |
|---|---|
| Django ORM | persistence, relationships, migrations, basic query optimization |
| Django REST Framework | request/response serialization, validation, standard viewset CRUD, browsable API |
| Django auth/permission framework | standard authentication (session/token), simple role/permission checks |
| React | component lifecycle, state management, standard routing (via React Router) |
| Axios / fetch | HTTP client for REST calls |
| Django's file handling | multipart file upload parsing, temporary storage |
| Pillow (if used) | image processing (not needed here) |
| python-docx / PyPDF2 (if used) | Actually, these are **custom** extraction libraries; they will be noted in services. |
| Elasticsearch (if used) | full-text search, indexing (if chosen) — otherwise Django ORM search credited for basic search |

## Deployment / infrastructure

Standard managed hosting (e.g., AWS Ec2) needs nothing more than:
- sqlite database (managed service like RDS)
- Environment variables for secrets
- Only expand if there's something genuinely custom about the deployment (e.g., custom CI/CD pipelines, specialized compliance logging).