---
id: STORY-003
type: story-card
importance: Medium
risk: Low
---

# STORY-003 — Implement job categorization and CV upload limits

**As a** system user,
**I want to** have jobs categorized for better organization and have clear limits on CV uploads (e.g., 5 pages or 5 MB max),
**so that** I can efficiently organize opportunities and ensure the system handles CVs within reasonable, predictable constraints.

## Task list
- Implement job categorization/classification system (e.g., by industry, role type, skill domain)
- Allow users to browse/search opportunities by job category
- Define and enforce CV upload limits (maximum file size, e.g., 5 MB; maximum pages, e.g., 5 pages)
- Validate file size and page count during upload
- Provide clear error messages when upload limits are exceeded
- Support common CV formats (PDF, DOC, DOCX, TXT) within the defined limits
- Offer guidance to users on how to reduce CV size if needed (e.g., compress images, remove unnecessary pages)

## Notes
- Addresses user constraint: Need to consider categories of jobs a job seeker can be identified with
- Addresses user constraint: Need to set reasonable limits on CV upload size (e.g., 5 pages, 5 MB max) instead of handling arbitrarily large files
- Supports business goal: Improve matching quality by focusing on specific qualifications (business-goals.md)
- Enhances desired future state: Better organization and predictable handling of CVs within defined limits (Phase 4)
- Changes from original: Removed requirements for handling large files; replaced with explicit upload limits for system predictability and user clarity