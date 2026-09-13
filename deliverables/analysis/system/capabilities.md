## SYS-CAP-001 — CV Ingestion and Profiling Support

id: SYS-CAP-001
type: system-capability
title: CV Ingestion and Profiling Support
derived-from: [BUS-CAP-001]

## In scope for system support
- Accept CV uploads in common formats (PDF, DOC, DOCX, TXT)
- Extract structured qualification data (skills, experience, education, qualifications)
- Create searchable candidate profiles from extracted information

## Out of scope
- Advanced document parsing for non-standard CV formats
- Machine learning-based skill inference beyond explicit CV content

## SYS-CAP-002 — Profile Data Management Support

id: SYS-CAP-002
type: system-capability
title: Profile Data Management Support
derived-from: [BUS-CAP-002]

## In scope for system support
- Store, update, and manage user profile data
- Allow users to review and correct auto-extracted information
- Support manual information entry alongside or instead of auto-extraction

## Out of scope
- Real-time collaboration editing of profiles
- Integration with external professional networking platforms for auto-sync

## SYS-CAP-003 — Qualification Search and Matching Support

id: SYS-CAP-003
type: system-capability
title: Qualification Search and Matching Support
derived-from: [BUS-CAP-003]

## In scope for system support
- Provide search interface for qualifications, skills, experience, and education criteria
- Query the candidate profile database based on search criteria
- Return ranked suggestions of matching candidates

## Out of scope
- Natural language processing for semantic query understanding
- AI-based candidate ranking beyond basic qualification matching

## SYS-CAP-004 — Search Refinement and Alerting Support

id: SYS-CAP-004
type: system-capability
title: Search Refinement and Alerting Support
derived-from: [BUS-CAP-004]

## In scope for system support
- Allow filtering and refinement of search results
- Enable saving and reuse of search queries
- Set up alerts for new matching candidates

## Out of scope
- Real-time push notifications for alert delivery (relying on polling or periodic checks)
- Advanced machine learning for predicting candidate interest in job opportunities

## SYS-CAP-005 — Job Categorization System Support

id: SYS-CAP-005
type: system-capability
title: Job Categorization System Support
derived-from: [BUS-CAP-005]

## In scope for system support
- Implement a job categorization/classification system (e.g., by industry, role type, skill domain)
- Allow users to browse/search opportunities by job category

## Out of scope
- Dynamic, AI-driven taxonomy generation from job descriptions
- Multi-level hierarchical categorization with infinite depth

## SYS-CAP-006 — CV Upload Constraint Enforcement Support

id: SYS-CAP-006
type: system-capability
title: CV Upload Constraint Enforcement Support
derived-from: [BUS-CAP-006]

## In scope for system support
- Define and enforce limits on CV uploads (maximum file size, e.g., 5 MB; maximum pages, e.g., 5 pages)
- Validate file size and page count during upload
- Provide clear error messages when upload limits are exceeded
- Support common CV formats (PDF, DOC, DOCX, TXT) within the defined limits

## Out of scope
- Automatic CV compression or optimization to fit within limits
- Streaming upload for extremely large files with progress indication

## SYS-CAP-007 — Profile Analytics and Insights Support

id: SYS-CAP-007
type: system-capability
title: Profile Analytics and Insights Support
derived-from: [BUS-CAP-007]

## In scope for system support
- Track and store profile view events (viewer entity type, timestamp, search context)
- Provide dashboard showing total profile views over time
- Breakdown of views by viewer type (business, opportunity seeker, etc.)
- Breakdown of views by job category/industry
- Show search terms or qualifications that led to profile appearing in results
- Display recent viewers with privacy-protected identifiers
- Allow filtering insights by date range
- Provide export or summary view of insights

## Out of scope
- Real-time analytics dashboard with live updating
- Predictive analytics for forecasting future profile views

## SYS-CAP-008 — Notification Generation and Delivery Support

id: SYS-CAP-008
type: system-capability
title: Notification Generation and Delivery Support
derived-from: [BUS-CAP-008]

## In scope for system support
- Implement notification system for profile view events
- Allow users to configure notification preferences (email, in-app, frequency)
- Notify when: profile viewed, search result appearance, interest shown (save/follow)
- Provide option to receive digest notifications (daily/weekly summary) vs immediate alerts
- Include privacy controls: users can choose what information is shared in notifications
- Provide notification history/log
- Allow muting or temporarily disabling notifications
- Ensure notifications respect user privacy settings (don't reveal sensitive information)

## Out of scope
- Real-time WebSocket-based notification delivery
- Integration with third-party messaging platforms (Slack, WhatsApp, etc.) for notifications

## SYS-CAP-009 — Privacy-Protected Information Handling Support

id: SYS-CAP-009
type: system-capability
title: Privacy-Protected Information Handling Support
derived-from: [BUS-CAP-009]

## In scope for system support
- Ensure sensitive information is protected in search results (displaying only privacy-protected identifiers unless explicit consent is given)
- Protect sensitive information in insights (showing aggregated or anonymized data)
- Protect sensitive information in notifications (users can choose what information is shared)

## Out of scope
- End-to-end encryption of all profile data
- Advanced anonymization techniques like differential privacy