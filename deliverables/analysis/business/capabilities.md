## BUS-CAP-001 — CV Ingestion and Profiling

id: BUS-CAP-001
type: business-capability
derived-from: [BUS-REQ-001]

The system shall ingest CVs in common formats, extract structured qualification data, and create/maintain searchable user profiles.

## BUS-CAP-002 — Profile Data Management

id: BUS-CAP-002
type: business-capability
derived-from: [BUS-REQ-001]

The system shall store, update, and manage user profile data, allowing users to review, correct, and supplement auto-extracted information.

## BUS-CAP-003 — Qualification Search and Matching

id: BUS-CAP-003
type: business-capability
derived-from: [BUS-REQ-002]

The system shall provide search functionality for qualifications, skills, experience, and education, returning ranked candidate suggestions based on search criteria.

## BUS-CAP-004 — Search Refinement and Alerting

id: BUS-CAP-004
type: business-capability
derived-from: [BUS-REQ-002]

The system shall allow filtering and refinement of search results, saving of search queries, and setting up alerts for new matching candidates.

## BUS-CAP-005 — Job Categorization System

id: BUS-CAP-005
type: business-capability
derived-from: [BUS-REQ-003]

The system shall implement a job categorization/classification system (e.g., by industry, role type, skill domain) and allow browsing/searching opportunities by category.

## BUS-CAP-006 — CV Upload Constraint Enforcement

id: BUS-CAP-006
type: business-capability
derived-from: [BUS-REQ-003]

The system shall define and enforce limits on CV uploads (maximum file size and pages), validate during upload, and provide clear error messages when limits are exceeded.

## BUS-CAP-007 — Profile Analytics and Insights

id: BUS-CAP-007
type: business-capability
derived-from: [BUS-REQ-004]

The system shall track, store, and provide insights about profile views, including viewer type, timestamp, search context, job category interest, and search terms that led to views.

## BUS-CAP-008 — Notification Generation and Delivery

id: BUS-CAP-008
type: business-capability
derived-from: [BUS-REQ-004, BUS-REQ-005]

The system shall generate and deliver notifications for profile views and interactions, with configurable privacy controls, delivery preferences, and notification history.

## BUS-CAP-009 — Privacy-Protected Information Handling

id: BUS-CAP-009
type: business-capability
derived-from: [BUS-REQ-004, BUS-REQ-005]

The system shall ensure sensitive information is protected in search results, insights, and notifications, showing only privacy-protected identifiers unless explicit consent is given.