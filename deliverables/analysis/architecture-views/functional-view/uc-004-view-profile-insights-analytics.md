---
id: UC-004
type: use-case
derived-from: [REQ-004]
---

# View Profile Insights and Analytics

## General info

- **Primary actor:** Job Seeker
- **Secondary actors:** System (for tracking, storing, aggregating view events)
- **Trigger:** Job Seeker accesses the profile insights and analytics dashboard.
- **Preconditions:** 
  - Job Seeker has an active profile in the system
  - Profile insight tracking is enabled (or Job Seeker consents to enable it)
  - System has been collecting profile view events (viewer entity type, timestamp, search context)
  - System is operational and ready to retrieve analytics data
- **Postconditions:** 
  - Job Seeker views dashboard showing total profile views over time
  - Job Seeker sees breakdown of views by viewer type (business, opportunity seeker, etc.)
  - Job Seeker sees breakdown of views by job category/industry
  - Job Seeker sees search terms or qualifications that led to profile appearing in results
  - Job Seeker sees recent viewers with privacy-protected identifiers
  - Job Seeker can filter insights by date range
  - Job Seeker can export or summarize view data
  - Job Seeker can toggle insight collection on/off with clear explanation of data collected
- **Business rules:** 
  - BR-005: Profile insights and analytics collection is opt-in by default; user may enable/disable at any time
  - BR-006: Users can configure what information is shared in notifications (applies to insights as well)
  - BR-007: Insight data must comply with GDPR/CCPA regarding personal data handling
  - BR-008: Sensitive viewer information (specific company names, individual identifiers) must be protected/pseudonymized
  - BR-009: Authentication required to access profile insights
  - BR-010: Insight data retention subject to user account lifecycle and privacy requests

## Description

### Main flow

1. Job Seeker accesses profile insights and analytics section of their account
2. System verifies authentication and authorization for insights access
3. System checks if insight collection is enabled; if disabled, prompts to enable with explanation of what data is collected
4. If enabled, System retrieves aggregated profile view data from analytics storage
5. System calculates and displays total profile views over time (configurable time range)
6. System breaks down views by viewer type (business, opportunity seeker, etc.)
7. System breaks down views by job category/industry
8. System extracts and displays search terms or qualifications that led to profile appearing in search results
9. System displays recent viewers with privacy-protected identifiers (e.g., "Tech Company in SF" instead of specific name)
10. Job Seeker can apply date range filters to all analytics views
11. Job Seeker can export insights data (CSV, PDF) or view summary report
12. Job Seeker can toggle insight collection on/off; if turning off, System stops collecting new view events
13. System confirms any changes to insight collection settings

### Alternate flows

**A1 — Insight Collection Disabled**
- If insight collection is disabled at step 3:
  - System explains what data is collected for insights (viewer type, timestamp, search context, job category)
  - System provides opt-in toggle to enable insight collection
  - If Job Seeker enables, proceed to step 4
  - If Job Seeker declines, use case ends with no analytics displayed

**A2 — No View Data Available**
- If insufficient view data collected (e.g., new profile, low visibility):
  - System displays message indicating insufficient data for meaningful analytics
  - System suggests increasing profile visibility or waiting for more data
  - Use case ends after displaying available baseline metrics

**A3 — Date Range Filter Application**
- When Job Seeker applies date range filter:
  - System recalculates all analytics metrics for selected period
  - System updates displays accordingly
  - Use case continues with filtered views

**A4 — Export Request**
- When Job Seeker requests export of insights data:
  - System formats data according to selected format (CSV, PDF, etc.)
  - System provides download link or direct download
  - Use case ends after export completion

**A5 — Privacy Setting Change Impact**
- If Job Seeker changes privacy settings that affect what view data is collected:
  - System explains impact on future insight collection
  - System updates collection rules accordingly
  - Existing data remains unchanged unless manually purged

## Activity diagram

```mermaid
flowchart TD
    Start[Start] --> AccessInsights[Access Profile Insights]
    AccessInsights --> VerifyAuth[Verify Authentication & Authorization]
    VerifyAuth --> CheckCollection{Insight Collection Enabled?}
    CheckCollection -- No --> ExplainCollection[Explain Data Collected for Insights]
    ExplainCollection --> PromptEnable{Enable Insight Collection?}
    PromptEnable -- Yes --> EnableCollection[Enable Insight Collection]
    PromptEnable -- No --> EndNoData[End: No Insights Displayed]
    EnableCollection --> RetrieveData[Retrieve Aggregated View Data]
    CheckCollection -- Yes --> RetrieveData
    RetrieveData --> CalculateTotals[Calculate Total Profile Views Over Time]
    CalculateTotals --> BreakdownViewer[Breakdown Views by Viewer Type]
    BreakdownViewer --> BreakdownCategory[Breakdown Views by Job Category/Industry]
    BreakdownCategory --> ExtractSearchTerms[Extract Search Terms/Qualifications]
    ExtractSearchTerms --> DisplayRecent[Display Recent Viewers (Privacy-Protected)]
    DisplayRecent --> ApplyFilters{Apply Date Range Filters?}
    ApplyFilters -- Yes --> Recalculate[Recalculate Metrics for Date Range]
    Recalculate --> BreakdownViewer
    ApplyFilters -- No --> ExportRequest{Export Insights Data?}
    ExportRequest -- Yes --> FormatData[Format Data for Export]
    FormatData --> ProvideExport[Provide Export Download]
    ProvideExport --> End[End]
    ExportRequest -- No --> ToggleCollection{Toggle Insight Collection?}
    ToggleCollection -- Yes --> UpdateSetting[Update Collection Setting]
    UpdateSetting --> ConfirmChange[Confirm Setting Change]
    ConfirmChange --> End[End]
    ToggleCollection -- No --> End[End]
```