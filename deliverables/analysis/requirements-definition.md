# Requirements Definition — Job/CV Matching Platform

A straightforward outline of what the system must do (functional) and what characteristics it must have (nonfunctional). See the coverage note at the bottom before treating this as final.

## Functional Requirements

### 1. Profile Management

id: REQ-001
type: functional-requirement
derived-from: [STORY-001]
priority: High

- 1.1. Accept CV upload in common formats (PDF, DOC, DOCX, TXT)
- 1.2. Extract structured information from CV (skills, experience, education, qualifications)
- 1.3. Store extracted data in a searchable database format
- 1.4. Allow user to review and correct auto-extracted information.
- 1.5. Provide option for manual information entry alongside/ instead of auto-extraction
- 1.6. Create a user profile from the captured/entered information
- 1.7. Enable profile updates, deletion, and deactivation
- 1.8. Ensure deactivated profiles are not visible to businesses/opportunity seekers
- 1.9. Restrict profile viewing to the owning user only

### 2. Candidate Search and Matching

id: REQ-002
type: functional-requirement
derived-from: [STORY-002]
priority: High

2.1. Provide search interface for qualifications, skills, experience, education criteria
2.2. Query the candidate profile database based on search criteria
2.3. Return ranked suggestions of matching candidates
2.4. Allow filtering and refinement of search results
2.5. Display candidate profile summaries (with privacy-protected sensitive information)
2.6. Enable initiating contact or viewing full profile (subject to privacy settings)
2.7. Save and reuse search queries
2.8. Set up alerts for new matching candidates

### 3. System Organization and Constraints

id: REQ-003
type: functional-requirement
derived-from: [STORY-003]
priority: Medium

3.1. Implement job categorization/classification system (e.g., by industry, role type, skill domain)
3.2. Allow users to browse/search opportunities by job category
3.3. Define and enforce CV upload limits (maximum file size, e.g., 5 MB; maximum pages, e.g., 5 pages)
3.4. Validate file size and page count during upload
3.5. Provide clear error messages when upload limits are exceeded
3.6. Support common CV formats (PDF, DOC, DOCX, TXT) within the defined limits
3.7. Offer guidance to users on how to reduce CV size if needed (e.g., compress images, remove unnecessary pages)

### 4. Profile Insights and Analytics

id: REQ-004
type: functional-requirement
derived-from: [STORY-004]
priority: Medium

4.1. Track and store profile view events (viewer entity type, timestamp, search context)
4.2. Provide dashboard showing total profile views over time
4.3. Breakdown of views by viewer type (business, opportunity seeker, etc.)
4.4. Breakdown of views by job category/industry
4.5. Show search terms or qualifications that led to profile appearing in results
4.6. Display recent viewers with privacy-protected identifiers (e.g., "Tech Company in SF" rather than specific name)
4.7. Allow filtering insights by date range
4.8. Provide export or summary view of insights
4.9. Include toggle to enable/disable insight collection (with clear explanation of what data is collected)

### 5. Notifications and Engagement

id: REQ-005
type: functional-requirement
derived-from: [STORY-005]
priority: Medium

5.1. Implement notification system for profile view events
5.2. Allow users to configure notification preferences (email, in-app, frequency)
5.3. Notify when: profile viewed, search result appearance, interest shown (save/follow)
5.4. Provide option to receive digest notifications (daily/weekly summary) vs immediate alerts
5.5. Include privacy controls: users can choose what information is shared in notifications
5.6. Provide notification history/log
5.7. Allow muting or temporarily disabling notifications
5.8. Ensure notifications respect user privacy settings (don't reveal sensitive information without consent)

## Nonfunctional Requirements

### 1. Operational Requirements

id: REQ-010
type: nonfunctional-requirement
category: operational
derived-from: [STORY-001, STORY-002, STORY-003, STORY-004, STORY-005]
priority: Medium

1.1. The system shall support common CV formats (PDF, DOC, DOCX, TXT) for upload and processing.
1.2. The system shall provide a web-based interface accessible via standard browsers.
1.3. The system shall operate in a multi-tenant environment supporting multiple concurrent users.
1.4. The system shall provide administrative interfaces for system configuration and monitoring.

### 2. Performance Requirements

id: REQ-011
type: nonfunctional-requirement
category: performance
derived-from: [STORY-001, STORY-002]
priority: High

2.1. CV upload and processing shall complete within 30 seconds for files up to 5 MB.
2.2. Search queries shall return results within 2 seconds for databases up to 100,000 profiles.
2.3. The system shall support at least 1,000 concurrent active users.
2.4. Profile updates shall be reflected in search results within 5 seconds.

### 3. Security and Access Requirements

id: REQ-012
type: nonfunctional-requirement
category: security
derived-from: [STORY-001, STORY-002, STORY-004, STORY-005]
priority: High

3.1. User profiles shall be accessible only to the owning user unless explicitly shared via search results.
3.2. Deactivated profiles shall not be visible in search results or accessible via direct links.
3.3. Sensitive personal information (e.g., contact details, identification numbers) shall be protected and not displayed in search results without explicit user consent.
3.4. The system shall implement role-based access control (job seeker, business/opportunity seeker, administrator).
3.5. All data transmissions shall be encrypted using HTTPS/TLS.
3.6. The system shall implement secure authentication mechanisms (password-based, with optional multi-factor authentication).
3.7. Regular security audits and vulnerability assessments shall be conducted.

### 4. Cultural and Political Requirements

id: REQ-013
type: nonfunctional-requirement
category: cultural-political
derived-from: [STORY-001, business-goals.md]
priority: Medium

4.1. The system shall comply with relevant data protection regulations (GDPR, CCPA) regarding personal data collection, storage, and processing.
4.2. Users shall have the right to access, correct, and delete their personal data upon request.
4.3. The system shall provide clear privacy notices explaining what data is collected and how it is used.
4.4. The system shall obtain explicit user consent before processing CV data for matching purposes.
4.5. The system shall support multiple languages for interface and CV parsing (starting with English, with extensibility for additional languages).

## Coverage Check

Unmapped discovery items (in discovery, no matching requirement):
- None identified. All stakeholders, pain points, business goals, and story cards have been mapped to requirements.

Unfounded requirements (in report, no discovery source):
- None identified. All requirements trace back to discovery items.

Everything maps cleanly both directions as of 2026-09-10.