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

## 2026-09-11 — Pass 2: refinement via CRC cards and structural-view files

### Outcomes of this pass
- Created CRC cards and class‑diagram slices for each use case (UC‑001 through UC‑005) in the structural‑view directory.
- Verified each candidate class against the detailed flow of its use case; retained only those that actually participate.
- Introduced several service‑ and infrastructure‑level classes that emerged from the analysis (e.g., `ConfigurationService`, `ValidationService`, `FileStorage`, `AnalyticsService`, `NotificationService`, `DigestScheduler`, `PrivacyService`, `ExportService`, `GuidanceService`).
- Refined role classes: kept `User` as a single concrete class with a `role` attribute; the specific actor types (Job Seeker, Opportunity Seeker, Business/Hiring Entity, System Administrator) are now represented as values of that attribute rather than separate classes.
- Refined event modelling: kept `ViewEvent`, added `SearchAppearanceEvent` and `InteractionEvent` as specializations of a base `NotificationEvent` (or `EventBase`) to support UC‑004 and UC‑005.
- Updated the list of carried‑forward candidates (see below).

### Candidates carried forward to next refinement (strike‑through = dropped in this pass)

- Profile  
- CV  
- Skill  
- Experience  
- Education  
- Qualification  
- JobCategory  
- UploadLimit  
- ViewEvent  
- SearchAppearanceEvent *(new)*  
- InteractionEvent *(new)*  
- NotificationPreference  
- NotificationHistory  
- NotificationService  
- DigestScheduler  
- PrivacyService  
- AnalyticsService  
- ValidationService  
- ExtractionService  
- FileStorage  
- ConfigurationService  
- GuidanceService  
- ExportService  
- User *(replaces JobSeeker, OpportunitySeeker, BusinessHiringEntity, SystemAdministrator as role‑specific instances)*  
- Database *(kept as infrastructure placeholder)*  
- SearchEngine *(represented indirectly via SearchService; kept for completeness)*  
- AuthenticationToken *(implicit in User/AuthenticationService; kept as placeholder)*  
- UserSession *(implicit in security context; kept as placeholder)*  

### Dropped candidates (struck)
- ~~SearchQuery~~ (replaced by `searchContext` string inside events)  
- ~~Viewer~~ (role absorbed into `userType` enum on `ViewEvent` and `initiatorIdHash` on `InteractionEvent`)  
- ~~Notification~~ (generic concept replaced by concrete event types and notification‑service infrastructure)  
- ~~OpportunitySeeker~~, ~~Business/Hiring Entity~~, ~~System Administrator~~, ~~Job Seeker~~ (merged into `User.role`)  

Next pass will focus on reviewing the CRC cards for consistency, checking for missing responsibilities/collaborators, and beginning the behavioural view for the selected complex use cases.