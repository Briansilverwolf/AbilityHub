# UC‑001 Partitioned Design (Mermaid)

```mermaid
graph TD
    %% ==== Modules (components) ====
    subgraph UC001_UploadCV[UC‑001 Upload CV & Create Searchable Profile]
        direction TB

        %% Orchestrator
        UC001[UploadOrchestrator<br/>(System/Controller)]:::orchestrator

        %% Core services
        VAL[ValidationService]:::service
        EXT[ExtractionService]:::service
        PROF[ProfileFactory/Builder]:::factory
        REV[ReviewAndCorrectionUI]:::ui
        PRIV[PrivacyService]:::service
        REPO[PersistenceRepository]:::repository
        SEARCH[SearchIndexer (SearchService)]:::service
        ERR[ErrorHandler]:::service
        LIMIT[UploadLimit (config)]:::config

        %% ==== Interfaces (exposed contracts) ====
        %% Orchestrator depends on all services
        UC001 -->|uses| VAL
        UC001 -->|uses| EXT
        UC001 -->|uses| PROF
        UC001 -->|uses| REV
        UC001 -->|uses| PRIV
        UC001 -->|uses| REPO
        UC001 -->|uses| SEARCH
        UC001 -->|uses| ERR
        UC001 -->|reads| LIMIT

        %% Service‑to‑service collaborations (from structural/behavioral views)
        VAL -->|gets limits| LIMIT
        EXT -->|produces| PROF
        PROF -->|creates| PROF2[Profile<br/>(domain object)]:::domain
        PROF2 -->|holds| SKILL[Skill]:::domain
        PROF2 -->|holds| EXP[Experience]:::domain
        PROF2 -->|holds| EDU[Education]:::domain
        PROF2 -->|holds| QUAL[Qualification]:::domain
        PROF2 -->|aggregates| PRIVSET[PrivacySettings]:::domain
        PROF2 -->|belongs to| USER[User]:::domain

        REPO -->|stores| PROF2
        REPO -->|stores| SKILL
        REPO -->|stores| EXP
        REPO -->|stores| EDU
        REPO -->|stores| QUAL

        PRIV -->|applies| PRIVSET
        SEARCH -->|indexes| PROF2

        %% Error handling is invoked by the orchestrator on validation failure
        UC001 -->|on validation error| ERR
        ERR -->|shows message| JS[Job Seeker]:::actor

        %% UI interaction (review/correct & manual entry)
        REV -->|displays/edits| PROF2
        REV -->|accepts manual input| PROF2
    end

    %% ==== Styling ====
    classDef orchestrator fill:#ffeb3b,stroke:#333,stroke-width:1.5px;
    classDef service fill:#90caf9,stroke:#333,stroke-width:1px;
    classDef factory fill:#a5d6a7,stroke:#333,stroke-width:1px;
    classDef ui fill:#fff59d,stroke:#333,stroke-width:1px;
    classDef repository fill:#ce93d8,stroke:#333,stroke-width:1px;
    classDef config fill:#e0e0e0,stroke:#333,stroke-width:1px;
    classDef domain fill:#ffffff,stroke:#333,stroke-width:1px;
    classDef actor fill:#ffccbc,stroke:#333,stroke-width:1px;
```