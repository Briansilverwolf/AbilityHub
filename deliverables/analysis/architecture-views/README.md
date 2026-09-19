# Architectural Views

This directory aggregates the three classic architectural views (functional, structural, behavioral) for the system, following a use‑case‑centric approach inspired by the Unified Process.

## Directory Structure

- `functional-view/` – Use‑case specifications (what the system does).
  - Contains one markdown file per use case (UC‑001 through UC‑005) plus a use‑case diagram.
- `structural-view/` – Static structure (what the system is made of).
  - Contains CRC cards and class diagrams for each use case, plus initial rough‑work notes.
- `behavioral-view/` – Dynamic behavior (how the system works over time).
  - Contains sequence diagrams, communication diagrams, and a state diagram for the profile lifecycle.

## How to Use

1. **Start with the functional view** to understand the system’s external behavior from the user’s perspective.
2. **Consult the structural view** to see the classes, attributes, and relationships that realize each use case.
3. **Examine the behavioral view** to see the detailed interactions (sequence/communication) and state changes (profile lifecycle) that occur during execution.

Each view is independent yet complementary; together they provide a complete picture of the system’s architecture.

## Traceability

- Each use case (e.g., UC‑001) has a corresponding file in all three views:
  - Functional: `functional-view/uc-001-upload-cv-create-searchable-profile.md`
  - Structural: `structural-view/uc-001-upload-cv-create-searchable-profile.md`
  - Behavioral: `behavioral-view/uc-001-sequence-diagram.md` and `behavioral-view/uc-001-communication-diagram.md`
- The profile lifecycle state diagram (`behavioral-view/profile-lifecycle-state-diagram.md`) spans multiple use cases (creation, update, deactivation).

## Diagram Notation

All diagrams use Mermaid syntax (`.md` files contain fenced code blocks). They can be viewed directly in Mermaid‑enabled editors or rendered with tools like the Mermaid Live Editor.

---

*Generated as part of the analysis phase. These documents serve as the foundation for detailed design and implementation.*