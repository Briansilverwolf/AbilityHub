# Analysis Summary Report
## Job/CV Matching Platform Project

### 1. Project Overview
This project aims to develop a privacy-preserving job/CV matching platform that connects three primary stakeholder groups: Job Seekers, Opportunity Seekers (recruiters/headhunters), and Businesses/Hiring Entities. The platform addresses fundamental inefficiencies in the current job matching process by enabling proactive visibility of qualifications and targeted matching based on specific qualifications rather than manual searching and advertising.

### 2. Stakeholder Analysis

#### 2.1 Job Seekers
- **Role**: Individuals seeking employment who upload their CVs to the system
- **Primary Activities**: Create and maintain professional profiles/CVs, upload them to the platform, update qualifications/experience
- **Key Benefits Sought**: 
  - Increased visibility to relevant opportunities without active searching
  - Streamlined job search process
  - Reduced time spent on manual applications
  - Better recognition of their qualifications

#### 2.2 Opportunity Seekers
- **Role**: People or businesses looking for specific qualifications who get candidate suggestions
- **Primary Activities**: Search for candidates based on specific qualifications, review suggested matches, initiate contact with potential candidates
- **Key Benefits Sought**:
  - Access to targeted candidate suggestions
  - Reduced time spent filtering unqualified applicants
  - Improved matching efficiency
  - Ability to find passive candidates not actively applying

#### 2.3 Businesses/Hiring Entities
- **Role**: Organizations seeking particular conditions/qualifications who want to connect with qualified candidates
- **Primary Activities**: Define qualification requirements, review candidate suggestions, engage with potential hires
- **Key Benefits Sought**:
  - More efficient candidate sourcing
  - Better quality matches based on specific qualifications
  - Reduced recruitment cycle time
  - Lower advertising and screening costs

### 3. Current State & Pain Points

#### 3.1 How the Current Process Works
- **Job Seekers**: Must search online for job postings and manually send their CVs to each opportunity
- **Businesses/Hiring Entities**: Must advertise job openings or send out notices to attract candidates
- **Opportunity Seekers**: Rely on existing job boards, networking, or direct applications to find matches

#### 3.2 Detailed Pain Points

**For Job Seekers:**
- Time-consuming: Must search multiple sources and manually apply to each opportunity
- Low recognition chance: Difficulty standing out among many applicants for the same posting
- Inefficient matching: May miss relevant opportunities that aren't actively searched for
- Reactive approach: Wait for job postings rather than having capabilities proactively visible

**For Businesses/Hiring Entities:**
- Advertising overhead: Must spend resources on job ads and outreach to attract candidates
- Screening burden: Receive many unqualified applications requiring time to filter
- Limited visibility: Difficulty finding passive candidates who aren't actively applying
- Slow process: Time lag between job posting and receiving qualified applications

**For Opportunity Seekers:**
- Scattered search: Must check multiple platforms/sources for relevant opportunities
- Manual filtering: Need to review many irrelevant options to find suitable matches
- Delayed response: May miss time-sensitive opportunities due to search latency

#### 3.3 Core Problems Identified
1. **Inefficient discovery process** - Both seekers and opportunity providers struggle to find each other efficiently
2. **High friction in matching** - Multiple manual steps slow down the connection process
3. **Poor signal-to-noise ratio** - Many irrelevant interactions waste time for all parties
4. **Lack of proactive visibility** - Qualifications and needs aren't easily discoverable without active searching

### 4. Business Goals & Drivers

#### 4.1 Why Solve This Now
- **Privacy & trust concerns**: Prevent sending information to untrusted parties
- **Market inefficiency**: Current job matching processes are slow and fragmented
- **Competitive pressure**: Need for faster, more targeted talent acquisition
- **Technology enablement**: Modern matching algorithms make this feasible at scale

#### 4.2 What "Better" Looks Like
- **For job seekers**: Increased visibility to relevant opportunities without active searching
- **For businesses**: Faster access to qualified candidates matching specific requirements
- **For opportunity seekers**: Efficient discovery of suitable matches based on qualifications
- **Overall**: Reduced friction in the job matching process, higher quality connections

#### 4.3 Key Business Goals
1. **Privacy-preserving matching**: Enable connections without exposing sensitive information to untrusted parties
2. **Efficiency improvement**: Reduce time and effort required for job seekers to find opportunities and for businesses to find candidates
3. **Matching quality increase**: Improve relevance of connections by focusing on specific qualifications rather than keyword matching
4. **Accessibility enhancement**: Make professional qualifications easily discoverable by those seeking them

#### 4.4 Success Metrics
- **Job seeker perspective**: CV becomes visible in relevant searches without manual application to each posting
- **Business perspective**: Ability to search for specific qualifications and receive targeted candidate suggestions
- **Process efficiency**: Reduction in time from qualification expression to connection establishment
- **Match quality**: Increase in relevant connections per search/interaction
- **User adoption**: Number of active CVs uploaded and searches performed

### 5. Discovery Findings Summary

Through a phased requirements discovery process, the following certified artifacts were produced:

#### 5.1 Stakeholders Identification
Confirmed three primary stakeholder groups with clearly defined roles, activities, and impact areas.

#### 5.2 Current State Documentation
Documented the existing manual, fragmented job matching process and identified specific pain points for each stakeholder group.

#### 5.3 Business Goals Definition
Established four key business goals aligned with stakeholder needs and market opportunities.

#### 5.4 User Story Cards (Functional Requirements)
Five prioritized user stories were identified:

**STORY-001: Upload CV and create searchable profile** (High importance, Medium risk)
- As a job seeker, I want to upload my CV and have the system extract relevant information to create a searchable profile, so that I can be discovered by businesses and opportunity seekers without manually applying to each posting.

**STORY-002: Search for qualifications and get candidate suggestions** (High importance, Medium risk)
- As a business or opportunity seeker, I want to search for specific qualifications and receive targeted candidate suggestions, so that I can efficiently find qualified candidates without advertising or screening unqualified applicants.

**STORY-003: Implement job categorization and CV upload limits** (Medium importance, Low risk)
- As a system user, I want to have jobs categorized for better organization and have clear limits on CV uploads (e.g., 5 pages or 5 MB max), so that I can efficiently organize opportunities and ensure the system handles CVs within reasonable, predictable constraints.

**STORY-004: View profile insights and analytics** (Medium importance, Low risk)
- As a job seeker, I want to see insights about who has viewed my profile, when they viewed it, what they searched for, and which job categories showed interest, so that I can understand my visibility and effectiveness in the platform and adjust my profile or search strategy accordingly.

**STORY-005: Receive notifications for profile views and interactions** (Medium importance, Low risk)
- As a job seeker, I want to receive notifications when someone views my profile or shows interest in my qualifications, so that I can timely respond to potential opportunities and engage with interested parties.

#### 5.5 Open Questions & Future Considerations
The discovery process captured unresolved questions about CV parsing techniques, privacy mechanisms, search ranking algorithms, and potential future enhancements for consideration in later phases.

### 6. Proposed Solution Overview

Based on the discovery findings, the platform will provide:

#### 6.1 Core Matching Functionality
- CV upload and information extraction to create searchable profiles
- Qualification-based search with targeted candidate suggestions
- Privacy-preserving matching that shares only necessary information
- Job categorization system for better organization
- CV upload limits to ensure system predictability

#### 6.2 User Experience Enhancements
- Profile insights and analytics dashboard
- Notification system for profile views and interactions
- Privacy controls for information sharing
- Configurable notification preferences (email, in-app, frequency)

#### 6.3 Technical Approach
- Structured data extraction from CVs (PDF, DOC, DOCX, TXT)
- Searchable database for candidate profiles
- Qualification matching algorithms
- Privacy-protected profile summaries for search results
- Audit trail for profile views and interactions

### 7. Scope & Boundaries

#### 7.1 In Scope
- CV upload, parsing, and profile creation
- Qualification-based search and matching
- Profile visibility controls and privacy settings
- Basic analytics and insights for job seekers
- Notification system for engagement tracking
- Job categorization system
- CV upload limits (size and page count)

#### 7.2 Out of Scope (for Initial Release)
- Advanced AI-powered semantic matching beyond qualification matching
- Video interviewing or assessment integration
- Payroll or HRIS system integrations
- Multi-language support beyond English
- Mobile application (initial web-based focus)
- Salary negotiation or job offer management features

### 8. Next Steps

The certified discovery output provides a solid foundation for the requirements definition phase. Immediate next steps include:

1. **Requirements Definition**: Transform the discovery artifacts into a formal Requirements Definition Report and Business Rules document
2. **Architecture Modeling**: Develop functional, structural, and behavioral views of the system based on the requirements
3. **Validation & Review**: Conduct checkpoints with stakeholders to ensure requirements accurately reflect needs
4. **Planning**: Define iterations, work packages, and resource allocation based on the defined scope

### 9. Conclusion
The requirements discovery phase has successfully captured the essential needs of Job Seekers, Opportunity Seekers, and Businesses/Hiring Entities regarding a job/CV matching platform. The identified problems of inefficient discovery, high friction, poor signal-to-noise ratio, and lack of proactive visibility are well-understood, and the proposed solution directly addresses these through privacy-preserving, qualification-based matching with enhanced visibility and analytics capabilities.

The five prioritized user stories provide a clear, achievable scope for an initial release that delivers significant value while establishing a foundation for future enhancements. The certification of this discovery work (approved by Brian on 9/10/2026) confirms that the project team has a shared understanding of the problem space and desired outcomes, enabling confident progression to the requirements definition phase.

---
*Report generated based on certified discovery artifacts completed on 9/10/2026*