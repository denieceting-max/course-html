# Production Workflow

## 1. Requirement planning
Do not begin page rendering immediately. First produce a concise plan and ask for confirmation.

Planning checklist:
- What is the topic?
- Who is the audience?
- Is the tone formal, practical, motivational, technical, or introductory?
- How many pages are expected?
- Does the deck need chapters or only sequential pages?
- Will the output be pasted into a text-to-HTML workflow or delivered as a file?
- Are there images, screenshots, or data tables that must be included?

## 2. Page planning
Create a page map before generating HTML.

Recommended page types:
- cover
- table of contents
- chapter divider
- comparison
- matrix
- process flow
- checklist
- table
- image showcase
- data dashboard mockup
- summary
- ending

## 3. Style demo
Select one template and produce a small demo first. Use the densest expected page as the demo when possible, because it tests font size, whitespace, and truncation risk.

Ask for confirmation after the demo:
- style accepted
- font size accepted
- page density accepted
- interaction accepted

## 4. Page rendering
After confirmation, render pages one by one or in small batches. Each page should be complete and paste-ready if the user is manually assembling pages.

For every page, decide:
- main message
- layout pattern
- visual hierarchy
- where the eye should land first
- what can be shortened
- what must not be omitted

## 5. Final assembly
Combine accepted pages into a single HTML deck.

Include only necessary presentation interactions:
- page scroll or snap
- keyboard navigation
- table of contents anchor links
- current page or chapter highlight
- progress bar
- subtle hover or click feedback

## 6. QA pass
Check the final deck for:
- bottom truncation
- top truncation
- side clipping
- tiny text
- excessive whitespace
- blurry text from transform scale or filters
- inconsistent page title size
- broken links or navigation

Use the audit script when helpful, then manually reason through the visual risk pages.
