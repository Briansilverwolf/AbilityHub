## BUS-REQ-001 — Profile Creation and Management

id: BUS-REQ-001
type: business-requirement
derived-from: [BUS-NEED-001]
supports: [BUS-CAP-001, BUS-CAP-002]

The system shall allow users to upload their CV and create a searchable profile containing structured information about their qualifications, skills, experience, and education.

## Evidence:
- STORY-001 (Upload CV and create searchable profile)
- Addresses pain point: Job seekers must search online for job postings and manually send CVs to each opportunity (current-state.md)
- Supports business goal: Privacy-preserving matching (business-goals.md)

## BUS-REQ-002 — Qualification Search and Matching

id: BUS-REQ-002
type: business-requirement
derived-from: [BUS-NEED-001]
supports: [BUS-CAP-003, BUS-CAP-004]

The system shall enable businesses and opportunity seekers to search for specific qualifications and receive targeted candidate suggestions based on search criteria.

## Evidence:
- STORY-002 (Search for qualifications and get candidate suggestions)
- Addresses pain point: Businesses must advertise job openings and screen many unqualified applications (current-state.md)
- Supports business goal: Efficiency improvement and matching quality increase (business-goals.md)

## BUS-REQ-003 — Data Organization and System Constraints

id: BUS-REQ-003
type: business-requirement
derived-from: [BUS-NEED-001]
supports: [BUS-CAP-005, BUS-CAP-006]

The system shall implement job categorization for better organization and enforce reasonable limits on CV uploads to ensure predictable system performance.

## Evidence:
- STORY-003 (Implement job categorization and CV upload limits)
- Addresses user constraints: Need to consider job categories and set reasonable upload limits (story-card-003.md notes)
- Supports business goal: Matching quality increase (business-goals.md)

## BUS-REQ-004 — Profile Engagement and Feedback

id: BUS-REQ-004
type: business-requirement
derived-from: [BUS-NEED-001]
supports: [BUS-CAP-007]

The system shall provide insights about profile views and engagement, including who viewed the profile, when, what search terms led to views, and which job categories showed interest.

## Evidence:
- STORY-004 (View profile insights and analytics)
- STORY-005 (Receive notifications for profile views and interactions)
- Addresses user interest in visibility and timely engagement (story-card-004.md, story-card-005.md notes)
- Supports business goal: Improve matching quality through feedback (business-goals.md)

## BUS-REQ-005 — Notification System

id: BUS-REQ-005
type: business-requirement
derived-from: [BUS-NEED-001]
supports: [BUS-CAP-008]

The system shall notify users when their profile is viewed or when there is interest shown in their qualifications, with configurable privacy controls and delivery preferences.

## Evidence:
- STORY-005 (Receive notifications for profile views and interactions)
- Complements profile insights functionality (STORY-004)
- Supports business goal: Increase engagement and reduce friction in connections (business-goals.md)