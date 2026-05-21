---
name: ai-html-deck-builder
description: "build, redesign, and refine chinese html presentation decks as 16:9 windows training slides. use when the user provides an outline, rough text, page list, or existing html template and wants a staged workflow: first clarify needs and plan pages, then choose or demo one of four bundled visual templates, then render pages one by one or in batches, and finally assemble a polished single html deck with navigation, progress, light interactions, large readable typography, minimal whitespace, and no truncation."
---

# AI HTML Deck Builder

## Purpose
Create polished HTML presentation decks for training, sharing, or internal presentations. Prioritize a staged working style: plan first, confirm the style demo, render page by page, then assemble and QA the final deck.

Use Chinese by default unless the user asks otherwise.

## Required Workflow

### Step 1. Plan the content before rendering
Start by turning the user's rough idea, outline, transcript, or pasted text into a clear production plan.

Return a planning draft with:
- Presentation goal and audience
- Suggested page count
- Part or chapter structure
- Per-page title and page intent
- Suggested page type, such as cover, directory, chapter divider, comparison, process, matrix, table, image showcase, summary, ending
- Risk notes, such as pages likely to be too dense or needing source material

Pause for confirmation before building pages unless the user explicitly asks to skip confirmation.

### Step 2. Select and confirm the visual demo
Before generating the full deck, select a visual template from `references/template-catalog.md` and make a small demo.

Default demo options:
- One cover page plus one content page, or
- One representative page based on the densest content, or
- A short standalone HTML style demo

Ask the user to confirm the style direction before full rendering. If the user wants a different style, revise the demo first.

### Step 3. Render pages progressively
Render one page at a time or in small batches. For every page:
- Keep each page close to one 16:9 screen
- Use large readable Chinese typography
- Avoid bottom truncation
- Avoid excessive whitespace
- Keep the same background, card language, typography rhythm, and interaction system within the selected template
- Adjust density by changing layout first, not by shrinking text too much
- For dense pages, split content or simplify hierarchy instead of forcing everything into tiny type

When the user is actively reviewing, provide complete HTML for the page or batch so it can be pasted directly.

### Step 4. Assemble the final deck
After pages are accepted, combine them into one final HTML file.

The final deck should include:
- 16:9 page sections
- Keyboard navigation where appropriate
- Necessary scroll or page snapping only
- Anchor jumps for directory or chapter navigation when the deck has chapters
- Current chapter or page highlight when useful
- Lightweight progress indicator
- Light hover or click feedback on content cards
- No complex animation that distracts from the presentation

### Step 5. QA and fix
Before returning final output, check for:
- Any bottom, top, or side truncation
- Font sizes that are too small for projection
- Overlarge whitespace on sparse pages
- Text blur caused by excessive transform scale or filter effects
- Inconsistent title sizes or card spacing
- Broken directory links, keyboard navigation, or progress indicators

Use `scripts/audit_html_deck.py` when a quick structural audit is useful.

## Design Standards

### 16:9 screen standard
Design for a Windows browser projected or shared on screen:
- Target a 16:9 canvas such as 1600 by 900
- Use `aspect-ratio: 16 / 9` where possible
- Use one page per screen
- Avoid relying on hidden overflow to solve density problems
- Keep page padding balanced, generally 24 to 60 px depending on density

### Typography standard
- Main titles should be visually strong and consistent
- Content text should remain readable at presentation distance
- Do not shrink dense pages below comfortable reading size unless the user accepts it
- Prefer fewer words, stronger hierarchy, and better spacing over tiny text

### Interaction standard
Use only necessary presentation interactions:
- Directory or chapter anchor jump
- Current page or chapter highlight
- Lightweight progress indicator
- Keyboard navigation or snap scroll
- Subtle card hover or click animation

Avoid:
- Large whole-page scaling animations that make text blurry
- Constant moving backgrounds that distract
- Complex interactive controls unless the user specifically asks

## Template Selection
Use `references/template-catalog.md` to choose among the four bundled templates:
- `assets/templates/template-0-final-course.html`
- `assets/templates/template-1-blue-pink.html`
- `assets/templates/template-2-blue-white.html`
- `assets/templates/template-3-white-pink.html`

If no style is specified, default to template 0 for formal internal training decks.

## Output Modes

### Planning output
Use this structure:

```markdown
## 课程/展示规划
### 目标与受众
### 建议结构
### 每页规划
| 页码 | 标题 | 页面类型 | 核心信息 | 展示建议 |
### 需要确认的问题
```

### Style demo output
Return complete paste-ready HTML when the user asks for code or HTML. Keep demo short and self-contained.

### Final output
Return a single complete HTML file or a downloadable artifact when file generation is available. If returning code in chat, include the complete HTML from `<!DOCTYPE html>` through `</html>`.

## Important Reminders
- Do not jump directly to full production when the user has not confirmed the outline and visual style.
- If user content is too long for one page, tell them and propose splitting or simplifying.
- If the user requests updates to an existing HTML deck, preserve the accepted style and modify only the relevant pages unless they ask for a full redesign.
- Keep the user's language, tone, and training context. For this user's decks, prefer practical, direct, non-technical wording.
