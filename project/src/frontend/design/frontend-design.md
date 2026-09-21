# AbilityHub Frontend Design

## Overview
This document outlines the frontend design for the AbilityHub application, a platform for creating and managing professional profiles from CV/resume data. The frontend is built with Next.js 13+ (App Router), React, and Tailwind CSS.

## Pages

### 1. Landing Page (`/`)
- **Purpose**: Introduce the service, highlight key features, and encourage sign-ups.
- **Content**:
  - Hero section with headline, subheading, and primary call-to-action (CTA) button.
  - Features section (3-4 icons with descriptions): CV upload, skill extraction, privacy controls, job matching.
  - How it works section (3 steps): Upload CV, review extracted data, publish profile.
  - Testimonials or trust badges (optional).
  - Footer with links.

### 2. Authentication Pages
Since we have a Django backend, we can either:
- Use Django's authentication views (server-rendered) and redirect to/from Next.js pages.
- Implement authentication in Next.js using NextAuth.js and have the frontend communicate with Django via API (recommended for SPA experience).

We'll assume we are building a SPA that communicates with a Django REST API (to be built). Therefore, we need:
#### 2.1 Sign In (`/login`)
- Form: Email/username and password.
- Links: Forgot password, Sign up.
- Validation and error handling.

#### 2.2 Sign Up (`/register`)
- Form: Name, email, password, confirm password.
- Validation and error handling.
- Option: Sign in instead.

#### 2.3 Forgot Password (`/forgot-password`)
- Form: Email to reset password.
#### 2.4 Reset Password (`/reset-password?token=...`)
- Form: New password, confirm password.

### 3. Dashboard (`/dashboard`)
- **Purpose**: Central hub after login, showing user's profiles and quick actions.
- **Content**:
  - Welcome message with user's name.
  - List of user's profiles (cards) with actions: View, Edit, Duplicate, Delete.
  - Button: "Create New Profile" (primary CTA).
  - Quick stats: Profile completeness, profile views (if available).
  - Navigation sidebar (optional) for easy access to pages.

### 4. Profile Creation (`/profiles/create`)
- **Purpose**: Upload CV and create a new profile (UC-001 flow).
- **Content**:
  - Stepper or wizard interface (3 steps):
    1. **Upload CV**: Drag-and-drop area or file selector, accepted formats (PDF, DOC, DOCX, image), max size.
    2. **Review Extracted Data**: Display extracted information in editable sections:
       - Skills (list, with ability to add/edit/delete)
       - Experience (list of jobs, with ability to add/edit/delete)
       - Education (list of educations, with ability to add/edit-delete)
       - Qualifications/Certifications (list, with ability to add/edit-delete)
    3. **Privacy Settings**: Toggle switches for:
       - Show to everyone
       - Show to recruiters only
       - Hide contact information
       - (Optional: more granular controls)
  - Buttons: Previous, Next (or Skip), Submit (on final step).
  - On successful submission: Redirect to profile view page with success message.

### 5. Profile View (`/profiles/:id`)
- **Purpose**: Display a user's profile (read-only).
- **Content**:
  - Profile header: Name (if public), headline, location (if public).
  - Sections:
    - About/Summary (from CV or user-editable bio).
    - Skills (list with proficiency levels).
    - Experience (reverse chronological, with job title, company, dates, description).
    - Education (reverse chronological, with institution, degree, field, dates, grade).
    - Qualifications/Certifications (list with issuing organization, dates, credential ID).
  - Privacy notice: Indicate what information is visible based on privacy settings (if viewing own profile, show all; if viewing another's, show only allowed).
  - Actions (if viewing own profile): Edit Profile, Update Privacy, Download PDF, Share link.
  - If viewing another user's profile: Send message (if enabled), Save/Save for later (if applicable).

### 6. Profile Edit (`/profiles/:id/edit`)
- **Purpose**: Edit an existing profile.
- **Content**: Similar to profile creation step 2 (Review Extracted Data) but pre-populated with current data and without the upload step.
  - Sections: Skills, Experience, Education, Qualifications (all editable).
  - Buttons: Cancel, Save Changes.
  - On save: Show success message and redirect to profile view.

### 7. Privacy Settings (`/profiles/:id/privacy`)
- **Purpose**: Manage privacy settings for a profile.
- **Content**:
  - Explanation of what each setting controls.
  - Toggle switches:
    - Profile visibility: Public, Recruiters only, Private (only me).
    - Contact information visibility: Show email/phone, Hide contact info.
    - Individual section visibility: Skills, Experience, Education, Qualifications (each can be toggled).
  - Preview: Show how the profile will appear to different viewers (public, recruiter, private).
  - Buttons: Cancel, Save Settings.

### 8. Not Found (`/404`)
- Custom 404 page.

### 9. Error Page (`/500`)
- Custom error page.

## Components

### UI Components (Reusable)
- **Button**: Primary, secondary, outline, icon-only, loading state.
- **Input**: Text, email, password, textarea, with label, helper text, error state.
- **FileUpload**: Drag-and-drop area, file picker, progress indicator, accepted formats, max size.
- **Card**: For displaying profile snippets, features, etc.
- **Badge**: For skill proficiency, labels, etc.
- **Accordion**: For collapsible sections (e.g., in profile view).
- **Stepper**: For multi-step flows (profile creation).
- **ToggleSwitch**: For privacy settings.
- **Modal**: For confirmations, prompts.
- **Toast**: For notifications (success, error, warning).
- **Spinner**: Loading indicator.
- **Navigation**: Sidebar, top navbar, breadcrumbs.

### Domain-Specific Components
- **ProfileHeader**: Displays user's name, headline, avatar, and actions.
- **SkillList**: List of skills with ability to add/edit/delete (used in creation/edit).
- **ExperienceList**: List of experience entries.
- **EducationList**: List of education entries.
- **QualificationList**: List of qualification entries.
- **PrivacySettingsForm**: Form with toggles for privacy options.
- **ProfileSection**: Generic section component for About, Skills, Experience, etc. (used in profile view).

## Data Flow and API Endpoints

We assume the Django backend will provide a REST API (or GraphQL) for the frontend to consume. Based on the models and services we have, we can anticipate the following endpoints:

### Authentication (using Django REST Framework or custom)
- `POST /api/auth/register/` - user registration
- `POST /api/auth/login/` - obtain access token (JWT or session)
- `POST /api/auth/logout/` - invalidate token
- `POST /api/auth/password-reset/` - request password reset
- `POST /api/auth/password-reset-confirm/` - confirm password reset with token

### Profiles
- `GET /api/profiles/` - list profiles for the logged-in user (with pagination)
- `POST /api/profiles/` - create a new profile (UC-001 flow: upload CV and process)
  - Might accept multipart/form-data with CV file and optional privacy preferences.
  - Alternatively, split into: upload CV, then process with extracted data.
- `GET /api/profiles/:id/` - retrieve a specific profile (if permitted)
- `PATCH /api/profiles/:id/` - update profile (skills, experience, education, qualifications)
- `PUT /api/profiles/:id/privacy/` - update privacy settings
- `DELETE /api/profiles/:id/` - delete profile

### Related Objects (if needed separately)
- Skills, Experience, Education, Qualification might be nested under profile endpoints.

### File Handling
- CV upload endpoint: `POST /api/cv/upload/` (returns a temporary ID or processes directly).

## State Management and Data Fetching
- We can use React Query (TanStack Query) or SWR for data fetching, caching, and mutation.
- For form state, we can use React Hook Form or Zustand.
- Authentication state can be managed with a custom context or Zustand.

## Styling and UI Considerations
- **Tailwind CSS**: Already configured. We'll use utility classes for styling.
- **Dark Mode**: Next.js with Tailwind supports dark mode via class strategy. We'll implement dark mode toggle.
- **Responsive Design**: Mobile-first approach. All pages should work on mobile, tablet, and desktop.
- **Accessibility**: Follow WCAG guidelines: proper labeling, keyboard navigation, ARIA attributes, color contrast.
- **Animations**: Use Framer Motion or CSS transitions for enhanced UX (optional).

## Authentication Approach
We'll use JWT (JSON Web Tokens) for authentication:
- On login, store access token in HTTP-only cookie (for CSRF protection) or in localStorage (with caution).
- On each API request, include token in Authorization header.
- Use middleware to protect routes that require authentication.
- Implement refresh token rotation for security.

## User Flows

### 1. Visitor to Registered User
1. Visitor lands on landing page.
2. Clicks "Sign Up" (or "Get Started").
3. Fills out registration form and submits.
4. On success, redirected to login page or directly to dashboard (if auto-login).
5. Completes profile setup (if not done during registration).

### 2. Profile Creation Flow (UC-001)
1. User logs in and navigates to dashboard.
2. Clicks "Create New Profile".
3. Uploads CV file (drag-and-drop or browse).
4. System processes CV (placeholder extraction) and shows extracted data in editable form.
5. User reviews and edits extracted data as needed.
6. User sets privacy preferences.
7. User submits final profile.
8. System saves profile and redirects to profile view page.
9. User sees success message and can view/edit profile.

### 3. Viewing and Editing Profile
1. From dashboard, user clicks on a profile card to view.
2. Views profile in read-only mode.
3. Clicks "Edit Profile" to modify sections.
4. Makes changes and saves.
5. Sees success message and returns to view mode.

### 4. Updating Privacy Settings
1. From profile view, user clicks "Update Privacy".
2. Adjusts toggles for visibility.
3. Sees preview of how profile appears to different audiences.
4. Saves changes.
5. Sees success message.

## Which Page to Begin With?
Given that we have just built the backend models and service for profile creation (UC-001), we should begin with the **Profile Creation page** (`/profiles/create`). This will allow us to:
1. Test the frontend-backend integration for the core functionality.
2. Develop the file upload and data display components.
3. Implement the privacy settings form.
4. Create the profile model submission logic.

After the profile creation flow is working, we can move on to authentication and dashboard.

### Steps to Begin:
1. Set up API service layer (using fetch or axios) to communicate with Django endpoints.
2. Create the file upload component.
3. Create the profile creation wizard/stepper.
4. Connect to the backend's profile creation endpoint (to be built).
5. Implement privacy settings form.
6. Handle success and error states.

## Next Steps
1. Define the exact API endpoints with the backend team (or decide on the contract if working solo).
2. Implement authentication (if not relying on Django's built-in views).
3. Create the layout and navigation components (header, footer, sidebar).
4. Develop the profile creation page as described.
5. Test with dummy data, then connect to actual backend.

## Open Questions
- Will we use Django's built-in authentication views or implement our own in Next.js?
- How will we handle file uploads and data extraction on the backend? (We have placeholders in the service.)
- Will we use Django REST Framework or build custom API views?
- Do we need to implement real CV parsing (using libraries like pdfminer, python-docx, or OCR for images) or is the placeholder sufficient for now?

## Conclusion
This design provides a comprehensive blueprint for the AbilityHub frontend. By starting with the profile creation page, we can quickly validate the core user journey and iterate based on feedback.