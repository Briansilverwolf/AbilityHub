# Structural View — Rough Work (candidate classes, whole system)

This is a single running file. **Append a new dated section on each pass
rather than overwriting** — this preserves how the candidate list evolved
rather than losing history. Strike through anything dropped in a later
pass rather than deleting it outright, so the reasoning stays visible.

---

## 2026-09-10 — Pass 1: initial pass from use cases UC-001 through UC-005

### Textual analysis

- Profile (from UC-001) — common noun
- CV (from UC-001) — common noun
- Skill (from UC-001, UC-002) — common noun
- Experience (from UC-001, UC-002) — common noun
- Education (from UC-001, UC-002) — common noun
- Qualification (from UC-001, UC-002) — common noun
- Job Category (from UC-003) — common noun
- Upload Limit (from UC-003) — common noun
- View Event (from UC-004) — incident (event)
- Search Query (from UC-002) — incident (event)
- Notification (from UC-005) — incident (event)
- Viewer (from UC-004, UC-005) — role
- Job Seeker (from UC-001, UC-004, UC-005) — role (actor)
- Opportunity Seeker (from UC-002) — role (actor)
- Business/Hiring Entity (from UC-002) — role (actor)
- System Administrator (from UC-003) — role (actor)

### Brainstorming

- Database
- Search Engine
- Validation Service
- Extraction Service
- Notification Service
- Analytics Engine
- User Session
- Authentication Token
- API Gateway
- File Storage

### Common object lists

- **Physical/tangible things:** CV file, computer/server hardware
- **Incidents (events):** CV upload, file validation, data extraction, profile creation, search query execution, profile view, interaction (save/follow), notification sent, insight generated
- **Roles:** Job Seeker, Opportunity Seeker, Business/Hiring Entity, System Administrator, Viewer (of profile)
- **Interactions (transactions):** upload CV, validate file, extract data, store data, search profiles, rank results, view profile, send notification, generate insight
- **Other (places, organizations, records, catalogs, policies):** Job Categories (catalog), Privacy Policies, Terms of Service, GDPR/CCPA compliance policies

### Patterns

- None identified yet; will consider standard patterns like MVC, Repository, Service Layer during refinement.

### Candidates carried forward to CRC

- Profile
- CV
- Skill
- Experience
- Education
- Qualification
- JobCategory
- UploadLimit
- ViewEvent
- SearchQuery
- Notification
- Viewer
- JobSeeker
- OpportunitySeeker
- BusinessHiringEntity
- SystemAdministrator
- Database
- SearchEngine
- ValidationService
- ExtractionService
- NotificationService
- AnalyticsEngine
- UserSession
- AuthenticationToken
- FileStorage

---