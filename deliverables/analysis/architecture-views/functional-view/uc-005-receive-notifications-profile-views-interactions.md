---
id: UC-005
type: use-case
derived-from: [REQ-005]
---

# Receive Notifications for Profile Views and Interactions

## General info

- **Primary actor:** Job Seeker
- **Secondary actors:** System (for tracking events, generating notifications), Notification Service (email, in-app)
- **Trigger:** System detects a profile view, search result appearance, or interaction (save/follow) involving the Job Seeker's profile.
- **Preconditions:** 
  - Job Seeker has an active profile in the system
  - Notification system is operational and configured
  - Job Seeker has accessed notification preferences to configure channels and frequency
  - System is tracking profile view events and interactions (as per UC-004)
  - Authentication is required to access notification settings
- **Postconditions:** 
  - Job Seeker receives notification when profile is viewed, appears in search results, or receives interaction (save/follow)
  - Job Seeker can configure notification preferences (email, in-app, frequency)
  - Job Seeker can choose digest notifications (daily/weekly summary) vs immediate alerts
  - Job Seeker can set privacy controls on what information is shared in notifications
  - Job Seeker can view notification history/log
  - Job Seeker can mute or temporarily disable notifications
  - Notifications respect user privacy settings (do not reveal sensitive information without consent)
- **Business rules:** 
  - BR-006: Users can configure what information is shared in notifications (e.g., hide specific viewer identifiers)
  - BR-007: Notification content must comply with GDPR/CCPA regarding personal data
  - BR-008: Sensitive viewer information not shared in notifications without explicit consent
  - BR-009: Authentication required to access notification preferences
  - BR-010: Notification history retention subject to user preferences and privacy policies
  - BR-011: System shall provide option to receive digest notifications vs immediate alerts
  - BR-012: Job Seeker can mute or temporarily disable notifications

## Description

### Main flow

1. System detects a profile view event (viewer entity type, timestamp, search context)
2. System detects a profile appearance in search results for a given query
3. System detects an interaction (save/follow) on the Job Seeker's profile
4. System checks Job Seeker's notification preferences for event type and channel
5. System determines whether to send immediate alert or include in digest based on frequency setting
6. System constructs notification message respecting privacy controls (what information to share)
7. System sends notification via configured channel(s) (email, in-app, etc.)
8. System logs notification in Job Seeker's notification history
9. Job Seeker receives notification and can act accordingly (view profile, respond, etc.)
10. Job Seeker can access notification history/log to review past notifications
11. Job Seeker can mute or temporarily disable notifications via settings
12. Job Seeker can adjust notification preferences at any time

### Alternate flows

**A1 — Notification Disabled for Event Type**
- If Job Seeker has disabled notifications for a specific event type (e.g., profile views):
  - System logs event but does not generate notification
  - Use case ends for that event type

**A2 — Privacy Settings Limit Shared Information**
- If Job Seeker has configured privacy settings to hide specific identifiers:
  - System replaces specific viewer/opportunity details with generic descriptions (e.g., "Tech Company in SF")
  - System includes only non-sensitive information permitted by privacy settings
  - Notification proceeds with limited information

**A3 — Notification Service Failure**
- If email or in-app notification service fails:
  - System logs error and retries after backoff period
  - System may switch to alternative channel if primary repeatedly fails
  - System alerts administrator of persistent notification failures
  - Use case ends after retry attempts exhausted

**A4 — Digest Notification Generation**
- When digest frequency (daily/weekly) is selected:
  - System accumulates notification events over the digest period
  - At scheduled time, System compiles summary of events (counts, categories, sample items)
  - System sends digest notification via configured channel
  - Use case ends after digest delivery

**A5 — Mute/Temporarily Disable Notifications**
- When Job Seeker activates mute or temporary disable:
  - System suspends notification generation for specified duration or until manually re-enabled
  - System continues to log events for history but does not send notifications
  - After mute period ends, notifications resume according to preferences
  - Use case ends after setting change confirmation

## Activity diagram

```mermaid
flowchart TD
    Start[Start] --> DetectEvent[Detect Profile View/Search Appearance/Interaction]
    DetectEvent --> CheckPrefs[Check Notification Preferences for Event Type]
    CheckPrefs --> EnabledEvent{Event Type Enabled?}
    EnabledEvent -- No --> LogEventOnly[Log Event Only (No Notification)]
    LogEventOnly --> End[End]
    EnabledEvent -- Yes --> GetPrefs[Get Notification Channel & Frequency Settings]
    GetPrefs --> ImmediateOrDigest{Immediate Alert or Digest?}
    ImmediateOrDigest -- Immediate --> ConstructNotice[Construct Notification Message]
    ImmediateOrDigest -- Digest --> AccumulateEvent[Accumulate Event for Digest]
    AccumulateEvent --> WaitDigest{Time for Digest?}
    WaitDigest -- No --> DetectEvent
    WaitDigest -- Yes --> ConstructNotice
    ConstructNotice --> ApplyPrivacy[Apply Privacy Controls to Message]
    ApplyPrivacy --> SendNotice[Send Notification via Channel(s)]
    SendNotice --> LogNotice[Log Notification in History]
    LogNotice --> End[End]
```