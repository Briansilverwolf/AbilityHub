# Structural View

This directory contains the structural (static) models of the system, derived from CRC card sessions and refined for each use case.

## Files

- `rough-work.md` – Initial brainstorming and candidate classes discovered during early analysis.
- `uc-001-upload-cv-create-searchable-profile.md` – Structural view for UC‑001 (classes: CV, ValidationService, ExtractionService, Database, Profile, Skill, Experience, Education, Qualification, PrivacySettings, User, UploadLimit).
- `uc-002-search-qualifications-get-candidate-suggestions.md` – Structural view for UC‑002 (classes: SearchService, Database, Profile, Skill, Experience, Education, Qualification, PrivacySettings, SearchQuery, NotificationService, Notification, RankingAlgorithm, AnalyticsEngine, User).
- `uc-003-implement-job-categorization-cv-upload-limits.md` – Structural view for UC‑003 (classes: User (Admin), ConfigurationService, JobCategoryCatalog, JobCategory, UploadLimit, ValidationService, FileStorage, GuidanceService, CV).
- `uc-004-view-profile-insights-analytics.md` – Structural view for UC‑004 (classes: User (Job Seeker), Profile, InsightSettings, ViewEvent, AnalyticsService, ViewEventRepository, InsightDashboard, ExportService, PrivacyService, DateRangeFilter, AnalyticsResult, ViewerType, ExportFormat).
- `uc-005-receive-notifications-profile-views-interactions.md` – Structural view for UC‑005 (classes: User (Job Seeker), Profile, NotificationPreference, NotificationService, DigestScheduler, NotificationEvent/ViewEvent/SearchAppearanceEvent/InteractionEvent, NotificationHistory, EmailChannel, InAppChannel, PrivacyService, plus enumerations).

Each file includes:
- CRC cards (responsibilities & collaborators) for each class
- A class diagram (Mermaid syntax) showing attributes, methods, and relationships (associations, dependencies, generalizations, etc.)

These models capture the static structure of the system: the objects, their data, and how they relate to one another.