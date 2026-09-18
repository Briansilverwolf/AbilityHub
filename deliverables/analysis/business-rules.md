# Business Rules

## 1. Purpose
This document captures the business rules that govern the operation of the Job/CV Matching Platform, derived from stakeholder requirements, privacy considerations, and operational constraints identified during discovery.

## 2. Rules

### BR-001 - Profile Access Control
**Statement**
Only the profile owner can view their own full profile; other users can only see profile summaries in search results unless explicit consent is given for full profile access.
**Rationale**
Protects user privacy and ensures users control who can see their detailed CV information.
**Applied to**
- Profile viewing functionality (STORY-001)
- Search result display (STORY-002)
- Privacy settings

### BR-002 - Deactivated Profile Visibility
**Statement**
Deactivated profiles shall not be visible in search results, accessible via direct links, or included in any analytics or reporting.
**Rationale**
Respects user choice to remove themselves from the platform and prevents stale data from affecting matching quality.
**Applied to**
- Profile deactivation (STORY-001)
- Search queries (STORY-002)
- Analytics and insights (STORY-004)

### BR-003 - CV Upload Limits
**Statement**
CV uploads shall be limited to a maximum file size of 5 MB and a maximum of 5 pages. The system shall reject uploads exceeding these limits.
**Rationale**
Ensures system predictability, prevents excessive resource consumption, and provides clear user expectations.
**Applied to**
- CV upload functionality (STORY-001, STORY-003)
- File validation processes

### BR-004 - Data Correction Rights
**Statement**
Users shall have the ability to review, edit, and correct any information auto-extracted from their CVs before it is stored in their profile.
**Rationale**
Ensures data accuracy and gives users control over their professional representation on the platform.
**Applied to**
- CV information extraction (STORY-001)
- Profile creation and editing workflows

### BR-005 - Insight Collection Consent
**Statement**
Profile insights and analytics collection (tracking views, search terms, viewer types) shall be opt-in by default, and users may enable or disable this collection at any time via privacy settings.
**Rationale**
Balances the value of analytics with user privacy preferences and regulatory compliance requirements.
**Applied to**
- Profile insights and analytics (STORY-004)
- Privacy settings and user controls

### BR-006 - Notification Privacy Controls
**Statement**
Users shall be able to configure what information is shared in notifications (e.g., hide specific viewer identifiers, show only generic information like "Tech Company in SF").
**Rationale**
Protects user privacy while still providing valuable engagement feedback.
**Applied to**
- Notification system (STORY-005)
- User preference settings

### BR-007 - Data Protection Compliance
**Statement**
The system shall comply with GDPR and CCPA requirements regarding personal data collection, storage, processing, and user rights including access, correction, deletion, and data portability.
**Rationale**
Meets legal obligations and builds user trust through responsible data handling practices.
**Applied to**
- All personal data handling processes
- User account management
- Data storage and backup systems

### BR-008 - Search Result Privacy
**Statement**
Sensitive personal information (such as contact details, identification numbers, current salary) shall not be displayed in search results unless the profile owner has explicitly opted to share that information.
**Rationale**
Prevent unintentional exposure of sensitive data while still allowing meaningful matching based on qualifications.
**Applied to**
- Search result display (STORY-002)
- Profile summary generation
- Privacy consent management

### BR-009 - Authentication Requirement
**Statement**
All users must authenticate (login) to access any functionality beyond the public landing page. Authentication shall be required for profile creation, editing, searching, and viewing any user-specific data.
**Rationale**
Ensures accountability, protects user data, and enables personalized experiences.
**Applied to**
- All user-accessible system functions
- Session management
- Access control systems

### BR-010 - Data Retention and Deletion
**Statement**
User data shall be retained only as long as the user maintains an active account or as required by law. Upon account deletion or user request, personal data shall be permanently deleted from all systems within 30 days.
**Rationale**
Respects user autonomy over their data and minimizes long-term privacy risks.
**Applied to**
- Account lifecycle management
- Data backup and archival systems
- Data deletion procedures