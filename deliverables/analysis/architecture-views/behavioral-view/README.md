# Behavioral View

This directory contains the dynamic models of the system — how objects interact over time to fulfill the use cases.

## Files

- `uc-001-sequence-diagram.md` – Sequence diagram for UC‑001 (Upload CV and create searchable profile).
- `uc-002-sequence-diagram.md` – Sequence diagram for UC‑002 (Search for qualifications and get candidate suggestions).
- `uc-005-sequence-diagram.md` – Sequence diagram for UC‑005 (Receive notifications for profile views and interactions).
- `uc-001-communication-diagram.md` – Communication diagram for UC‑001 (object‑centric view of the same interactions).
- `uc-002-communication-diagram.md` – Communication diagram for UC‑002.
- `uc-003-communication-diagram.md` – Communication diagram for UC‑003.
- `uc-004-communication-diagram.md` – Communication diagram for UC‑004.
- `uc-005-communication-diagram.md` – Communication diagram for UC‑005.
- `profile-lifecycle-state-diagram.md` – State diagram showing the lifecycle of a Profile (draft → active → deactivated, with events such as upload, update, deactivate, reactivate).

### Diagram Types
- **Sequence diagrams** – Emphasize temporal ordering of messages between objects/actors.
- **Communication diagrams** – Emphasize the links (associations) between objects; show the same interactions but focus on which objects communicate with which.
- **State diagram** – Shows the states an object (Profile) can be in and the transitions triggered by events.

All diagrams are written in Mermaid syntax and can be rendered with any Mermaid‑compatible tool.

These behavioral models complement the structural views by illustrating how the system behaves at runtime.