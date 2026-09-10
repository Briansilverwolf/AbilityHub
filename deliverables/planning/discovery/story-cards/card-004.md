---
id: STORY-004
type: story-card
importance: Medium
risk: Low
---

# STORY-004 — View profile insights and analytics

**As a** job seeker,
**I want to** see insights about who has viewed my profile, when they viewed it, what they searched for, and which job categories showed interest,
**so that** I can understand my visibility and effectiveness in the platform and adjust my profile or search strategy accordingly.

## Task list
- Track and store profile view events (viewer entity type, timestamp, search context)
- Provide dashboard showing total profile views over time
- Breakdown of views by viewer type (business, opportunity seeker, etc.)
- Breakdown of views by job category/industry
- Show search terms or qualifications that led to profile appearing in results
- Display recent viewers with privacy-protected identifiers (e.g., "Tech Company in SF" rather than specific name)
- Allow filtering insights by date range
- Provide export or summary view of insights
- Include toggle to enable/disable insight collection (with clear explanation of what data is collected)

## Notes
- Addresses user interest in seeing "how many people/entities have seen there work, on which job categories"
- Enhances job seeker ability to understand their market visibility
- Supports business goal: Improve matching quality by giving feedback to job seekers on what attracts views
- Relates to stakeholder: Job Seekers (stakeholders.md)
- Can be implemented after core matching functionality (STORY-001, STORY-002) is validated