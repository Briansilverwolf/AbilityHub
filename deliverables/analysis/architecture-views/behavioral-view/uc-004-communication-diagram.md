---
use-case: UC-004
view: behavioral
type: communication
---
# View Profile Insights and Analytics — Communication Diagram

```mermaid
flowchart LR
    %% Nodes
    UJ[User `Job Seeker`]
    Sys[System `Insight Controller`]
    Auth[AuthenticationService]
    Prof[Profile]
    Sett[InsightSettings]
    Dash[InsightDashboard]
    AnaSvc[AnalyticsService]
    Repo[ViewEventRepository]
    Priv[PrivacyService]
    ExpSvc[ExportService]
    DRF[DateRangeFilter]
    VE[ViewEvent]
    JC[JobCategory]
    AnaRes[AnalyticsResult]
    %% Message flow `solid lines`
    UJ -->|login| Auth
    Auth -->|auth ok| Sys
    UJ -->|access insights dashboard| Sys
    Sys -->|display dashboard| UJ
    UJ -->|set date range? `optional`| Sys
    Sys -->|create DateRangeFilter| DRF
    UJ -->|request insights for profile & range| Sys
    Sys -->|getInsights`profileId, dateRange`| AnaSvc
    AnaSvc -->|get InsightSettings for profile| Sett
    Sett -->|InsightSettings `flags`| AnaSvc
    AnaSvc -->|findByProfileIdAndRange`profileId, dateRange`| Repo
    Repo -->|List<ViewEvent>| AnaSvc
    AnaSvc -->|for each ViewEvent, hash viewerId `if needed`| Priv
    Priv -->|hashed viewerId| AnaSvc
    AnaSvc -->|aggregate data `total views, breakdowns, top terms, recent viewers`| AnaSvc
    AnaSvc -->|mask recent viewer info| Priv
    Priv -->|masked viewer info| AnaSvc
    AnaSvc -->|return AnalyticsResult| Sys
    Sys -->|render charts & recent viewers| UJ
    %% Toggle insight collection
    UJ -->|toggle insight collection? `optional`| Sys
    Sys -->|toggleCollection`profileId, enable`| Sett
    Sett -->|updated InsightSettings| Sys
    %% Export insights
    UJ -->|request export? `optional`| Sys
    Sys -->|export`profileId, format`| ExpSvc
    ExpSvc -->|exportCSV/PDF`AnalyticsResult`| AnaSvc
    AnaSvc -->|AnalyticsResult| ExpSvc
    ExpSvc -->|downloadable file| UJ
    %% Structural links `dashed`
    Auth ---.dependency.--- Sys
    Sys ---.uses.--- Prof
    Prof ---.has_one.--- Sett
    Prof ---.has_many.--- VE
    VE ---.belongs_to.--- Prof
    VE ---.categorized_by.--- JC
    AnaSvc ---.queries.--- Repo
    AnaSvc ---.masks_data.--- Priv
    AnaSvc ---.reads_flags.--- Sett
    Dash ---.gets_data.--- AnaSvc
    Dash ---.exports_via.--- ExpSvc
    Dash ---.masks_recent_viewers.--- Priv
    Dash ---.toggles_collection.--- Sett
    Dash ---.applies_filter.--- DRF
    ExpSvc ---.serves.--- Dash
    Priv ---.hashes_viewerId.--- VE
    Priv ---.masks_recent.--- Dash
```
```