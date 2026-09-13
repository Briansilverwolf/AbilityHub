## CAP-REQ-006 — CV Upload Constraint Enforcement Requirement

id: CAP-REQ-006
type: capability-requirement
supports: [SYS-CAP-006]
derived-from: [BUS-REQ-003]
realized-by: [UC-001]

The system shall define and enforce limits on CV uploads (maximum file size, e.g., 5 MB; maximum pages, e.g., 5 pages), validate file size and page count during upload, provide clear error messages when upload limits are exceeded, and support common CV formats (PDF, DOC, DOCX, TXT) within the defined limits.