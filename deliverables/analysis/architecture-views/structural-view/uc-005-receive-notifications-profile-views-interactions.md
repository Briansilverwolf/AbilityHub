---
use-case: UC-005
view: structural
---
# Receive Notifications for Profile Views and Interactions — Structural View

Classes touched by this use case, refined from `rough-work.md` and verified by role-playing this use case's main flow against each card.

## CRC Cards

### User (as Job Seeker)
**Type:** Concrete, Domain  
**Description:** Actor who owns a profile and receives notifications about activity on that profile.  
**Associated Use Cases:** UC-001, UC-002, UC-003, UC-004, UC-005  

| Responsibilities | Collaborators |
|---|---|
| Authenticate via credentials | AuthenticationService |
| Access notification preferences | NotificationPreferenceService |
| View notification history | NotificationHistory |
| Mute or temporarily disable notifications | NotificationPreferenceService |

**Attributes:** userId(string), email(string), role(enum), passwordHash(string), createdAt(dateTime)  
**Relationships:**  
- One-to-one: Profile  
- One-to-one: NotificationPreference  
- Dependency: AuthenticationService, NotificationPreferenceService, NotificationHistory  

### Profile
**Type:** Concrete, Domain  
**Description:** Represents a job seeker’s professional profile; source of view/interaction events.  
**Associated Use Cases:** UC-001, UC-004, UC-005  

| Responsibilities | Collaborators |
|---|---|
| Store identifier for linking events | NotificationEvent, ViewEvent |
| Hold basic profile data (skills, experience, etc.) | — |

**Attributes:** profileId(string), userId(string), headline(string), summary(string), updatedAt(dateTime)  
**Relationships:**  
- One-to-one: User  
- One-to-many: ViewEvent (as the profile being viewed)  
- One-to-many: InteractionEvent (save/follow)  

### NotificationPreference
**Type:** Concrete, Domain  
**Description:** Stores a user’s choices for which event types trigger notifications, which channels are used, and frequency (immediate vs digest).  
**Associated Use Cases:** UC-005  

| Responsibilities | Collaborators |
|---|---|
| Indicate whether profile‑view notifications are enabled | NotificationService |
| Indicate whether search‑appearance notifications are enabled | NotificationService |
| Indicate whether interaction (save/follow) notifications are enabled | NotificationService |
| Store preferred channels (email, in‑app, SMS) | NotificationService |
| Store frequency setting (immediate, daily digest, weekly digest) | NotificationService |
| Store privacy masking preferences (hide viewer IDs, etc.) | PrivacyService |

**Attributes:** preferenceId(string), userId(string), viewNotificationsEnabled(boolean), appearanceNotificationsEnabled(boolean), interactionNotificationsEnabled(boolean), channelSet(Set<NotificationChannel>), frequency(NotificationFrequency), privacyMaskLevel(enum: NONE, BASIC, FULL), updatedAt(dateTime)  
**Relationships:**  
- Belongs to: User  
- Used by: NotificationService, PrivacyService  

### NotificationService
**Type:** Concrete, Service  
**Description:** Responsible for evaluating events, building messages, applying privacy controls, and delivering notifications via configured channels.  
**Associated Use Cases:** UC-005  

| Responsibilities | Collaborators |
|---|---|
| Listen for ViewEvent, SearchAppearanceEvent, InteractionEvent | EventListener (internal) |
| Retrieve user’s NotificationPreference | NotificationPreference |
| Determine if event should trigger immediate or digest notification | DigestScheduler |
| Build base notification message (event type, timestamp, etc.) | — |
| Apply privacy controls to message (mask identifiers, etc.) | PrivacyService |
| Send notification via each selected channel (email, in‑app, etc.) | EmailChannel, InAppChannel, etc. |
| Log sent notification in history | NotificationHistory |

**Attributes:** none  
**Relationships:**  
- Depends on: NotificationPreference, DigestScheduler, PrivacyService  
- Uses: EmailChannel, InAppChannel, NotificationHistory  
- Listens to: ViewEvent, SearchAppearanceEvent, InteractionEvent  

### DigestScheduler
**Type:** Concrete, Service  
**Description:** Accumulates events for users who have selected digest frequency and sends periodic summaries.  
**Associated Use Cases:** UC-005  

| Responsibilities | Collaborators |
|---|---|
| Store incoming events awaiting digest | — |
| Trigger digest generation at configured interval (daily/weekly) | — |
| Compile digest data (counts, categories, sample items) | NotificationService |
| Initiate digest send via NotificationService | NotificationService |

**Attributes:** none  
**Relationships:**  
- Used by: NotificationService  
- Manages: queued NotificationEvent objects  

### NotificationEvent
**Type:** Concrete, Domain  
**Description:** Abstract base class for all event types that can trigger a notification (view, appearance, interaction).  
**Associated Use Cases:** UC-005  

| Responsibilities | Collaborators |
|---|---|
| Provide timestamp of occurrence | — |
| Provide reference to affected profile | Profile |
| Provide optional details (viewer info, search context, interaction type) | — |

**Attributes:** eventId(string), profileId(string), timestamp(dateTime)  
**Relationships:**  
- Subclassed by: ViewEvent, SearchAppearanceEvent, InteractionEvent  

### ViewEvent (reused)
**Type:** Concrete, Domain  
**Description:** Record of a profile view (same as used in UC-004).  
**Associated Use Cases:** UC-004, UC-005  

| Responsibilities | Collaborators |
|---|---|
| Capture viewer identifier (hashed/pseudonymized) | PrivacyService |
| Record timestamp of view | — |
| Record search context (keywords/qualifications) | — |
| Record job category of viewer’s search (if applicable) | JobCategory |
| Link to viewed profile | Profile |

**Attributes:** eventId(string), profileId(string), viewerIdHash(string), viewerType(enum: BUSINESS, OPPORTUNITY_SEEKER, JOB_SEEKER, SYSTEM), searchContext(string), jobCategoryId(string, optional)  
**Relationships:**  
- Many-to-one: Profile  
- Many-to-one (optional): JobCategory  

### SearchAppearanceEvent
**Type:** Concrete, Domain  
**Description:** Record that a profile appeared in search results for a particular query.  
**Associated Use Cases:** UC-005  

| Responsibilities | Collaborators |
|---|---|
| Record the search query or qualifications that triggered appearance | — |
| Record timestamp of appearance | — |
| Link to viewed profile | Profile |
| Optionally record position in results | — |

**Attributes:** eventId(string), profileId(string), timestamp(dateTime), searchQuery(string), positionInResult(int, optional)  
**Relationships:**  
- Many-to-one: Profile  

### InteractionEvent
**Type:** Concrete, Domain  
**Description:** Record of an interaction (save or follow) on a profile.  
**Associated Use Cases:** UC-005  

| Responsibilities | Collaborators |
|---|---|
| Record interaction type (SAVE, FOLLOW) | — |
| Record timestamp of interaction | — |
| Link to interacting user (if known and allowed) | User (hashed/pseudonymized via PrivacyService) |
| Link to target profile | Profile |

**Attributes:** eventId(string), profileId(string), timestamp(dateTime), interactionType(enum: SAVE, FOLLOW), initiatorIdHash(string, optional)  
**Relationships:**  
- Many-to-one: Profile  
- Many-to-one (optional): User (initiator)  

### NotificationHistory
**Type:** Concrete, Domain  
**Description:** Immutable log of notifications sent to a user, useful for audit and UI history view.  
**Associated Use Cases:** UC-005  

| Responsibilities | Collaborators |
|---|---|
| Store notification identifier, timestamp, channel, and rendered message | — |
| Provide list of past notifications for UI | — |
| Support pagination / filtering by date or type | — |

**Attributes:** historyId(string), userId(string), notificationId(string), channel(NotificationChannel), timestamp(dateTime), message(string)  
**Relationships:**  
- Belongs to: User  

### EmailChannel
**Type:** Concrete, Infrastructure  
**Description:** Sends notifications via SMTP/email provider.  
**Associated Use Cases:** UC-005  

| Responsibilities | Collaborators |
|---|---|
| Render notification message with appropriate subject line | — |
| Send email to user’s registered address | — |
| Handle transient failures with retry logic | — |

**Attributes:** smtpHost(string), smtpPort(int), fromAddress(string)  
**Relationships:**  
- Used by: NotificationService  

### InAppChannel
**Type:** Concrete, Infrastructure  
**Description:** Posts notifications to the user’s in‑app notification centre.  
**Associated Use Cases:** UC-005  

| Responsibilities | Collaborators |
|---|---|
| Insert notification record into in‑app store | — |
| Signal UI to show badge/new item | — |

**Attributes:** none  
**Relationships:**  
- Used by: NotificationService  

### PrivacyService (reused)
**Type:** Concrete, Service  
**Description:** Applies pseudonymization and masking to protect personally identifiable information in notifications.  
**Associated Use Cases:** UC-004, UC-005  

| Responsibilities | Collaborators |
|---|---|
| Hash or pseudonymize viewer/company identifiers | — |
| Mask sensitive details in notification text | — |
| Ensure GDPR/CCPA compliance | — |

**Attributes:** none  
**Relationships:**  
- Used by: NotificationService, ViewEvent, InteractionEvent  

## Class diagram (this use case's slice)
```mermaid
classDiagram
    class User {
        <<Domain>>
        +string userId
        +string email
        +string role
        +string passwordHash
        +DateTime createdAt
    }
    class Profile {
        +string profileId
        +string userId
        +string headline
        +string summary
        +DateTime updatedAt
    }
    class NotificationPreference {
        +string preferenceId
        +string userId
        +boolean viewNotificationsEnabled
        +boolean appearanceNotificationsEnabled
        +boolean interactionNotificationsEnabled
        +Set<NotificationChannel> channelSet
        +NotificationFrequency frequency
        +PrivacyMaskLevel privacyMaskLevel
        +DateTime updatedAt
    }
    class NotificationService {
        +void handleEvent(ViewEvent ve)
        +void handleEvent(SearchAppearanceEvent sae)
        +void handleEvent(InteractionEvent ie)
        +NotificationPreference getPreference(string userId)
        +boolean isImmediate(NotificationFrequency freq)
        +void send(string userId, string message, Set<NotificationChannel> channels)
        +void logHistory(string userId, NotificationHistoryEntry entry)
    }
    class DigestScheduler {
        +void enqueue(EventBase eb)
        +void triggerDigest()
        +List<EventBase> getQueued(string userId)
    }
    class NotificationEvent {
        <<abstract>>
        +string eventId
        +string profileId
        +DateTime timestamp
    }
    class ViewEvent {
        +string viewerIdHash
        +string viewerType
        +string searchContext
        +string? jobCategoryId
    }
    class SearchAppearanceEvent {
        +string searchQuery
        +int? positionInResult
    }
    class InteractionEvent {
        +InteractionType interactionType
        +string? initiatorIdHash
    }
    class NotificationHistory {
        +string historyId
        +string userId
        +string notificationId
        +NotificationChannel channel
        +DateTime timestamp
        +string message
    }
    class EmailChannel {
        +void send(string toAddress, string subject, string body)
    }
    class InAppChannel {
        +void post(string userId, NotificationHistoryEntry entry)
    }
    class PrivacyService {
        +string hashIdentifier(string raw)
        +string mask(string text, PrivacyMaskLevel level)
    }
    class NotificationChannel {
        <<enumeration>> 
        EMAIL
        IN_APP
        SMS 
    }
    class NotificationFrequency { 
        <<enumeration>> 
        IMMEDIATE
        DAILY_DIGEST 
        WEEKLY_DIGEST 
        }

    class PrivacyMaskLevel { 
        <<enumeration>>
        NONE
        BASIC
        FULL 
        }
    class InteractionType {
         <<enumeration>>
        SAVE 
        FOLLOW 
    }
    class ViewerType { 
        <<enumeration>> 
        BUSINESS 
        OPPORTUNITY_SEEKER
        JOB_SEEKER 
        SYSTEM 
    }

    User "1" -- "1" Profile : owns
    User "1" -- "1" NotificationPreference : has
    NotificationPreference "1" -- "1" User : belongs to
    Profile "1" -- "1" User : belongs to
    Profile "1" -- "*" ViewEvent : source of
    Profile "1" -- "*" SearchAppearanceEvent : source of
    Profile "1" -- "*" InteractionEvent : source of
    NotificationService "1" -- "1" NotificationPreference : reads
    NotificationService "1" -- "1" DigestScheduler : uses for frequency
    NotificationService "1" -- "1" PrivacyService : applies masking
    NotificationService "1" -- "1" EmailChannel : sends via
    NotificationService "1" -- "1" InAppChannel : sends via
    NotificationService "1" -- "1" NotificationHistory : logs
    DigestScheduler "1" -- "*" NotificationEvent : queues
    NotificationHistory "1" -- "1" User : belongs to
    ViewEvent "1" -- "1" Profile : belongs to
    SearchAppearanceEvent "1" -- "1" Profile : belongs to
    InteractionEvent "1" -- "1" Profile : belongs to
    InteractionEvent "1" -- "0..1" User : initiator (hashed)
```