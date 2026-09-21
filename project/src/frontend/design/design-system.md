# AbilityHub Design System

## Overview
This document defines the visual design system for AbilityHub, ensuring consistency across all frontend components and pages. It builds upon the existing Tailwind CSS setup and Next.js Geist font integration.

## Foundation

### Color Palette
AbilityHub uses a professional, trustworthy color palette with excellent accessibility (WCAG AA compliance for text).

#### Primary Colors
- **Blue (Primary)**: Used for primary actions, links, and key brand elements
  - `blue-50`: #eff6ff
  - `blue-100`: #dbeafe
  - `blue-200`: #bfdbfe
  - `blue-300`: #93c5fd
  - `blue-400`: #60a5fa
  - `blue-500`: #3b82f6 (default primary)
  - `blue-600`: #2563eb
  - `blue-700`: #1d4ed8
  - `blue-800`: #1e40af
  - `blue-900`: #1e3a8a

#### Secondary Colors
- **Slate (Neutral)**: Used for backgrounds, text, and secondary elements
  - `slate-50`: #f8fafc
  - `slate-100`: #f1f5f9
  - `slate-200`: #e2e8f0
  - `slate-300`: #cbd5e1
  - `slate-400`: #94a3b8
  - `slate-500`: #64748b
  - `slate-600`: #475569
  - `slate-700`: #334155
  - `slate-800`: #1e293b
  - `slate-900`: #0f172a

#### Semantic Colors
- **Success**: For positive actions and confirmations
  - `green-500`: #22c55e
- **Warning**: For cautions and attention-needed states
  - `amber-500`: #f59e0b
- **Error**: For destructive actions and error states
  - `red-500`: #ef4444
- **Info**: For informational content
  - `sky-500`: #0ea5e9

#### Background Colors
- `background`: var(--background) (#ffffff light, #0a0a0a dark)
- `foreground`: var(--foreground) (#171717 light, #ededed dark)
- `muted-background`: `slate-50` (light) / `slate-900/50` (dark)
- `card-background`: `white` (light) / `slate-800` (dark)

### Typography
Uses Next.js Geist font family with a clear typographic hierarchy.

#### Font Families
- **Sans Serif**: `var(--font-geist-sans)` (Geist)
- **Mono Space**: `var(--font-geist-mono)` (Geist Mono)

#### Font Sizes (rem)
- `xs`: 0.75rem (12px)
- `sm`: 0.875rem (14px)
- `base`: 1rem (16px)
- `lg`: 1.125rem (18px)
- `xl`: 1.25rem (20px)
- `2xl`: 1.5rem (24px)
- `3xl`: 1.875rem (30px)
- `4xl`: 2.25rem (36px)
- `5xl`: 3rem (48px)
- `6xl`: 3.75rem (60px)
- `7xl`: 4.5rem (72px)
- `8xl`: 6rem (96px)
- `9xl`: 8rem (128px)

#### Font Weights
- `hairline`: 100
- `thin`: 200
- `light`: 300
- `normal`: 400
- `medium`: 500
- `semibold`: 600
- `bold`: 700
- `extrabold`: 800
- `black`: 900

#### Line Heights
- `tight`: 1.25
- `snug`: 1.375
- `normal`: 1.5
- `relaxed`: 1.625
- `loose`: 2

### Spacing System
Based on 4px grid (1 unit = 0.25rem = 4px)
- `0`: 0
- `px`: 0.0625rem (1px)
- `0.5`: 0.125rem (2px)
- `1`: 0.25rem (4px)
- `1.5`: 0.375rem (6px)
- `2`: 0.5rem (8px)
- `2.5`: 0.625rem (10px)
- `3`: 0.75rem (12px)
- `3.5`: 0.875rem (14px)
- `4`: 1rem (16px)
- `5`: 1.25rem (20px)
- `6`: 1.5rem (24px)
- `7`: 1.75rem (28px)
- `8`: 2rem (32px)
- `9`: 2.25rem (36px)
- `10`: 2.5rem (40px)
- `11`: 2.75rem (44px)
- `12`: 3rem (48px)
- `14`: 3.5rem (56px)
- `16`: 4rem (64px)
- `20`: 5rem (80px)
- `24`: 6rem (96px)
- `28`: 7rem (112px)
- `32`: 8rem (128px)
- `36`: 9rem (144px)
- `40`: 10rem (160px)
- `44`: 11rem (176px)
- `48`: 12rem (192px)
- `52`: 13rem (208px)
- `56`: 14rem (224px)
- `60`: 15rem (240px)
- `64`: 16rem (256px)
- `72`: 18rem (288px)
- `80`: 20rem (320px)
- `96`: 24rem (384px)

### Border Radius
- `none`: 0px
- `sm`: 0.125rem (2px)
- `DEFAULT`: 0.25rem (4px)
- `md`: 0.375rem (6px)
- `lg`: 0.5rem (8px)
- `xl`: 0.75rem (12px)
- `2xl`: 1rem (16px)
- `3xl`: 1.5rem (24px)
- `full`: 9999px

### Shadows
- `sm`: 0 1px 2px 0 rgba(0, 0, 0, 0.05)
- `DEFAULT`: 0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px -1px rgba(0, 0, 0, 0.1)
- `md`: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.1)
- `lg`: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.1)
- `xl`: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.1)
- `2xl`: 0 25px 50px -12px rgba(0, 0, 0, 0.25)
- `inner`: inset 0 2px 4px 0 rgba(0, 0, 0, 0.05)
- `none`: 0 0 #0000

### Opacity
- `0`: 0%
- `5`: 5%
- `10`: 10%
- `20`: 20%
- `25`: 25%
- `30`: 30%
- `40`: 40%
- `50`: 50%
- `60`: 60%
- `70`: 70%
- `75`: 75%
- `80`: 80%
- `90`: 90%
- `95`: 95%
- `100`: 100%

## Components

### Buttons
#### Primary Button
- Background: `blue-600`
- Text: `white`
- Hover: `blue-700`
- Active/Focus: `blue-800`
- Disabled: `slate-300` background, `slate-400` text
- Border Radius: `md` (0.375rem)
- Padding: `px-4 py-2` (sm), `px-6 py-3` (md), `px-8 py-4` (lg)
- Font Weight: `semibold` (600)
- Transition: `background-color 150ms ease-in-out`

#### Secondary Button
- Background: `transparent`
- Text: `blue-600`
- Border: `1px solid blue-300`
- Hover: `blue-50` background
- Active/Focus: `blue-100` background
- Disabled: `slate-200` border, `slate-400` text
- Same sizing, radius, and transition as primary

#### Outline Button
- Background: `transparent`
- Text: `foreground`
- Border: `1px solid slate-300`
- Hover: `slate-50` background (light) / `slate-800/50` (dark)
- Active/Focus: `slate-100` background (light) / `slate-800/30` (dark)
- Disabled: `slate-200` border, `slate-400` text
- Same sizing, radius, and transition

#### Icon Button
- Size: `h-10 w-10` (2.5rem square)
- Background: `transparent`
- Color: `slate-500`
- Hover: `slate-100` background (light) / `slate-800/50` (dark)
- Active: `slate-200` background (light) / `slate-800/30` (dark)
- Radius: `md`
- Transition: `background-color 150ms ease-in-out`

### Inputs & Form Elements
#### Text Input
- Background: `white` (light) / `slate-800` (dark)
- Border: `1px solid slate-300`
- Text: `foreground`
- Placeholder: `slate-400`
- Focus: `border-blue-300` + `ring-1 ring-blue-500`
- Error: `border-red-300` + `ring-1 ring-red-500`
- Disabled: `slate-50` background, `slate-300` border, `slate-400` text
- Border Radius: `md`
- Padding: `px-3 py-2` (sm), `px-4 py-3` (md)
- Font Size: `sm` (0.875rem)
- Transition: `border-color 150ms ease-in-out, box-shadow 150ms ease-in-out`

#### Textarea
Same as text input but with `min-h-[3.5rem]` and `resize-y`

#### Select
Same styling as text input, with dropdown arrow in `slate-400` color

#### Checkbox & Radio
- Size: `h-4 w-4` (1rem)
- Border: `1px solid slate-300`
- Background: `white` (light) / `slate-800` (dark)
- Checked: `background-blue-600` + `border-blue-600`
- Hover: `border-slate-400`
- Focus: `ring-2 ring-blue-500`
- Disabled: `slate-50` background, `slate-300` border
- Border Radius: `none` (square) or `rounded` (circle for radio)

#### File Upload
- Container: `border-2 border-dashed slate-300` background `slate-50`
- Hover: `border-blue-300` background `blue-50`
- Icon: `slate-500` (hover: `blue-600`)
- Text: `slate-600` (hover: `blue-600`)
- Border Radius: `lg`
- Transition: `all 150ms ease-in-out`

### Cards
#### Basic Card
- Background: `white` (light) / `slate-800` (dark)
- Border: `1px solid slate-200` (light) / `slate-700/50` (dark)
- Border Radius: `lg`
- Padding: `p-6`
- Shadow: `sm`
- Transition: `transform 150ms ease-in-out, box-shadow 150ms ease-in-out`
- Hover: `-translate-y-1` + `shadow-md`

#### Elevated Card
- Same as basic but with `shadow-md` default and `shadow-lg` hover

#### Interactive Card
- Same as basic card but with `cursor-pointer` and hover effects
- On click: `scale-95` active state

### Navigation
#### Top Navbar
- Background: `background` (with `bg-opacity-90` and `backdrop-blur-sm` for translucency)
- Border Bottom: `1px solid slate-200` (light) / `slate-700/50` (dark)
- Height: `h-14` (3.5rem)
- Padding: `px-4`
- Z-index: `50`

#### Sidebar
- Width: `w-64` (16rem)
- Background: `slate-50` (light) / `slate-900` (dark)
- Border Right: `1px solid slate-200` (light) / `slate-700/50` (dark)
- Padding: `pt-6`

#### Navigation Item
- Padding: `px-3 py-2`
- Border Radius: `md`
- Text: `foreground`
- Hover: `slate-100` background (light) / `slate-800/50` (dark)
- Active: `blue-50` background + `blue-600` text + `border-l-2 border-blue-500`
- Transition: `background-color 150ms ease-in-out, color 150ms ease-in-out`

### Profile Components
#### Profile Header
- Avatar: `h-12 w-12` (3rem) with `rounded-full` and `object-cover`
- Name: `text-lg font-semibold`
- Headline: `text-sm text-slate-500`
- Location: `text-xs text-slate-400` (optional)
- Action Buttons: `text-slate-600` hover `text-slate-700`

#### Profile Section
- Title: `text-base font-medium text-foreground mb-4`
- Content: `text-slate-600` (light) / `slate-300` (dark)
- Divider: `border-t border-slate-200` (light) / `slate-700/50` (dark) `my-6`

#### Skill Tag
- Background: `blue-50`
- Text: `text-blue-600 text-xs font-medium`
- Border Radius: `full`
- Padding: `px-2.5 py-0.5`
- Hover: `blue-100` background

#### Experience/Education Card
- Background: `white` (light) / `slate-800` (dark)
- Border: `1px solid slate-200` (light) / `slate-700/50` (dark)
- Border Radius: `lg`
- Padding: `p-4`
- Margin Bottom: `mb-3`
- Hover: `shadow-sm`

#### Qualification Badge
- Background: `slate-50`
- Text: `text-slate-600 text-xs`
- Border Radius: `md`
- Padding: `px-3 py-1`
- Hover: `slate-100` background

### Modals & Overlays
#### Modal Backdrop
- Background: `rgba(0, 0, 0, 0.5)`
- Transition: `opacity 150ms ease-in-out`

#### Modal Container
- Background: `white` (light) / `slate-800` (dark)
- Border: `1px solid slate-200` (light) / `slate-700/50` (dark)
- Border Radius: `xl`
- Padding: `p-6`
- Shadow: `xl`
- Max Width: `w-96` (24rem)
- Width: `full` (mobile)
- Transition: `transform 200ms ease-in-out, opacity 200ms ease-in-out`
- Scale: `scale-95` (closed) to `scale-100` (open)

#### Modal Header
- Title: `text-xl font-bold`
- Description: `text-slate-600 text-sm`
- Margin Bottom: `mb-4`

#### Modal Footer
- Border Top: `1px solid slate-200` (light) / `slate-700/50` (dark)
- Padding Top: `pt-4`
- Justify: `flex-end gap-3`

### Toasts & Notifications
#### Toast Container
- Position: `fixed top-4 right-4` (or other corners)
- Z-index: `50`
- Gap: `space-y-3`

#### Toast
- Background: `white` (light) / `slate-800` (dark)
- Border: `1px solid slate-200` (light) / `slate-700/50` (dark)
- Border Radius: `lg`
- Padding: `p-4`
- Shadow: `md`
- Flex: `flex items-start gap-3`
- Max Width: `w-64` (16rem)
- Animation: `slide-in-from-right 200ms ease-out`, `fade-out 200ms ease-in 200ms`

#### Toast Variants
- Success: `border-l-4 border-green-500 bg-green-50 text-green-800`
- Warning: `border-l-4 border-amber-500 bg-amber-50 text-amber-800`
- Error: `border-l-4 border-red-500 bg-red-50 text-red-800`
- Info: `border-l-4 border-sky-500 bg-sky-50 text-sky-800`

#### Toast Icon
- Size: `h-4 w-4`
- Color: Matches variant (green-600, amber-600, etc.)

#### Toast Title
- Font: `font-medium text-sm`

#### Toast Description
- Font: `text-slate-600 text-xs`

#### Toast Progress Bar
- Height: `h-0.5`
- Background: `slate-200`
- Animation: `width-full 0ms linear` (countdown)

#### Toast Close Button
- Size: `h-4 w-4`
- Color: `slate-400`
- Hover: `slate-500` background, `rounded-full`
- Transition: `background-color 150ms ease-in-out`

## Animations & Transitions

### Transition Durations
- `fast`: 75ms
- `normal`: 150ms (default for most interactions)
- `slow`: 200ms
- `slower`: 300ms

### Transition Easing
- `ease-in`: `cubic-bezier(0.4, 0, 1, 1)`
- `ease-out`: `cubic-bezier(0, 0, 0.2, 1)`
- `ease-in-out`: `cubic-bezier(0.4, 0, 0.2, 1)` (default)
- `ease-in-out-cubic`: `cubic-bezier(0.32, 0, 0.67, 0)`

### Specific Animations
#### Button Press
- Scale: `scale-95` (active state)
- Duration: `100ms`
- Easing: `ease-in-out`

#### Card Hover
- Lift: `-translate-y-1`
- Shadow: `sm` → `md`
- Duration: `150ms`
- Easing: `ease-in-out`

#### Modal Open/Close
- Open: `scale-95` → `scale-100` + `opacity-0` → `opacity-100`
- Close: `scale-100` → `scale-95` + `opacity-100` → `opacity-0`
- Duration: `200ms`
- Easing: `ease-in-out`

#### Toast Slide
- Enter: `translate-x-full` → `translate-x-0` + `opacity-0` → `opacity-100`
- Exit: `translate-x-0` → `translate-x-full` + `opacity-100` → `opacity-0`
- Duration: `200ms`
- Easing: `ease-out` (enter), `ease-in` (exit)

#### Page Transitions
- Fade: `opacity-0` → `opacity-100`
- Duration: `300ms`
- Easing: `ease-in-out`
- Applied via route transition in layout or using next-page-transponder

#### Skeleton Loader
- Background: `bg-gradient-to-r from-slate-200 via-slate-300 to-slate-200`
- Background Size: `200% 100%`
- Animation: `shimmer 1.5s infinite linear`
- Keyframes:
  ```
  0% { background-position: 200% 0 }
  100% { background-position: -200% 0 }
  ```

#### Pulse Animation
- Opacity: `opacity-100` → `opacity-75` → `opacity-100`
- Duration: `2s`
- Easing: `ease-in-out`
- Infinite

## Iconography
- **Library**: Heroicons (outline and solid variants)
- **Size**: 
  - Small: `h-4 w-4` (1rem)
  - Medium: `h-5 w-5` (1.25rem)
  - Large: `h-6 w-6` (1.5rem)
- **Color**: 
  - Default: `slate-500` (light) / `slate-400` (dark)
  - Active: `blue-600`
  - Danger: `red-500`
- **Style**: Consistent line weight, simple and recognizable

## Imagery Style
- **Photography**: 
  - Professional, diverse, authentic
  - Consistent lighting and tone
  - Slight warm bias for approachability
- **Illustrations**:
  - Line art with flat colors
  - Primary color accents
  - Rounded, friendly shapes
- **Icons**:
  - Outline style for UI elements
  - Solid style for emphasis and active states
- **Optimization**:
  - WebP format for browsers that support it
  - Proper sizing (don't overserve)
  - Lazy loading for below-the-fold images
  - AVIF fallback where supported

## Dark Mode
- Implemented via CSS custom properties and Tailwind's dark mode strategy (class)
- Toggled by adding/removing `dark` class on `<html>` element
- User preference respected via `localStorage` and system preference
- Automatic switch based on `prefers-color-scheme` media query

### Color Inversion Principles
- Backgrounds: Dark surfaces (`slate-900`, `slate-800`)
- Foregrounds: Light text (`slate-100`, `slate-200`)
- Primary colors: Slightly lighter tints for visibility on dark backgrounds
- Borders: Medium opacity (`slate-700/50`)
- Shadows: Darker with opacity (`rgba(0,0,0,0.4)`)

## Accessibility
### Color Contrast
- All text meets WCAG AA (4.5:1) for normal text, AAA (7:1) for large text
- Interactive elements meet WCAG AA for contrast and hit targets

### Focus Management
- Visible focus ring: `ring-2 ring-blue-500` on focus
- Never remove outline without providing equivalent visible indicator
- Logical tab order

### Touch Targets
- Minimum size: 44x44px (11 units)
- Recommended: 48x48px (12 units) for frequent actions

### Screen Reader Support
- Semantic HTML elements
- ARIA labels where needed
- Live regions for dynamic content
- Proper heading hierarchy

### Reduced Motion
- Respects `prefers-reduced-motion` media query
- Provides reduced animation alternatives
- Uses `motion-safe:` and `motion-reduce:` modifiers

## Implementation Guidelines

### Using Tailwind
- Utilize utility classes for consistency
- Extract repeating patterns into component classes (using `@apply` in CSS or create component functions)
- Leverage Tailwind's JIT compiler for optimal CSS output

### Component Architecture
- Follow atomic design principles: atoms → molecules → organisms → templates → pages
- Create reusable, composable components
- Separate presentation from logic where beneficial
- Use React hooks for state and side effects

### Performance
- Optimize images and fonts
- Use `next/image` for automatic optimization
- Implement code splitting and lazy loading
- Minimize re-renders with React.memo and useMemo/useCallback
- Prioritize above-the-fold content

### Documentation
- Document component props and usage
- Provide examples in Storybook or similar
- Maintain living style guide
- Version design system updates

## Files to Reference
- `/project/src/frontend/app/globals.css` - Base styles and CSS variables
- `/project/src/frontend/app/layout.tsx` - Root layout with font imports
- `/project/src/frontend/postcss.config.mjs` - PostCSS configuration
- `/project/src/frontend/next.config.ts` - Next.js configuration
- `/project/src/frontend/package.json` - Dependments (Tailwind, Next.js, etc.)

## Next Steps for Implementation
1. Create a Tailwind plugin or CSS file for custom component classes if needed
2. Build a component library (buttons, inputs, cards, etc.) following this spec
3. Create page templates using these components
4. Implement theme toggle for dark/light mode
5. Add animation utilities or use Framer Motion for complex animations
6. Set up Storybook or similar for component documentation and testing

This design system provides a solid foundation for building a professional, consistent, and accessible user interface for AbilityHub.