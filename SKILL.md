---
name: ai-course-html-generator
description: generate chinese ai course html slide pages and scrolling course pages from outlines or rough content. use when the user provides ideas, an outline, lesson notes, page content, or asks to create a white, soft, minimal tech style 16:9 html presentation page, chapter page, cover page, ending page, directory page, or integrated scrolling html deck with anchor navigation, current-page highlight, lightweight progress, and content-level click animation.
---

# AI Course HTML Generator

Use this skill to turn Chinese course ideas, outlines, notes, or page-level content into reusable HTML presentation pages in a consistent **white, soft, minimal tech style**.

## Core workflow

Always follow this two-step workflow unless the user explicitly asks to skip planning.

### Step 1: Plan first and wait for confirmation

When the user provides a rough idea, topic, outline, or long text, first produce a planning draft in Chinese and stop.

The planning draft must include:

1. **课程定位**：一句话说明这套内容要解决什么问题。
2. **目标受众**：谁会看这套页面。
3. **整体结构**：建议分为哪些 PART 或章节。
4. **逐页规划表**：每页包含页码、标题、核心信息、建议视觉形式。
5. **确认问题**：请用户回复“同意”或提出修改意见后再进入 HTML 生成。

Do not generate the full HTML pages before the user confirms the plan.

### Step 2: Generate HTML after confirmation

After the user confirms the plan, generate the requested HTML.

Default output options:

- **Single page HTML**：when the user asks for one page or a specific page.
- **Multiple page HTML blocks**：when the user asks for several individual HTML files/pages.
- **Integrated scrolling HTML**：when the user asks to combine many pages into one scrolling page.

## Visual style requirements

Follow `references/style-guide.md` for all pages.

Default style keywords:

- white background
- soft blue / teal / purple gradients
- rounded 3xl cards
- light borders and shadows
- clean business tech style
- Chinese typography with bold titles
- 16:9 layout for Windows / projector display
- no dark cyberpunk style
- no overly complex glowing effects

## Page types

Use `references/page-patterns.md` to choose the page layout.

Common page types:

- Cover page
- Directory page
- Chapter divider page
- Content page
- Comparison page
- Matrix page
- Process / flow page
- Table page
- Image showcase page
- Ending page
- Integrated scrolling deck

## HTML generation rules

1. Return complete, copyable HTML code in a fenced `html` code block when the user asks for code.
2. Use Tailwind CDN and lucide icons by default:
   - `https://cdn.tailwindcss.com`
   - `https://unpkg.com/lucide@latest`
3. Use `html2canvas` download button only when the user wants an image export button, or when consistent with prior pages.
4. Design each standalone page as a 16:9 canvas:
   - outer container: `max-w-[1536px] aspect-[16/9]`
   - rounded white card background
   - avoid content being clipped at top or bottom
5. Keep title sizes consistent across pages, but allow body text to shrink when content is dense.
6. Prefer fewer, clearer elements over many decorative icons.
7. Do not add extra concepts not provided by the user unless explicitly asked to expand.
8. Keep all visible text and code comments in Chinese when the user works in Chinese.

## Integrated scrolling deck rules

When combining many HTML pages into one file:

1. Preserve the original 16:9 page designs by embedding each page as an iframe or equivalent isolated slide section.
2. Each section should behave like one presentation screen.
3. Provide only necessary interactions:
   - top lightweight progress bar
   - anchor navigation
   - current page highlight
   - keyboard page navigation
   - content-level click animation
4. Do not add heavy animations that distract from the course content.
5. For stable scrolling, use the final alignment logic in `references/integrated-deck.md`.
6. If iframes are used, allow iframe content to receive clicks so content-level click animation works.
7. Ensure keyboard navigation still jumps directly to the next full page after clicking inside an iframe.

## Content-level animation rules

Use the animation from `references/integrated-deck.md` when the user asks for “点哪里哪里轻微放大” or similar.

Expected behavior:

- Clicking a card, icon, keyword, image module, or content block makes that element subtly scale up.
- A small soft ripple appears at the click location.
- The whole screen should not scale.
- The animation must not break keyboard page navigation or scroll behavior.

## Quality checklist before final output

Before returning HTML, check:

- [ ] The page title is clear and not clipped.
- [ ] Main content fits inside the 16:9 canvas.
- [ ] Bottom summary or footer is not cut off.
- [ ] Large pages still look balanced and not overcrowded.
- [ ] The style matches the white, soft, minimal tech look.
- [ ] Navigation and animations do not conflict in integrated pages.
- [ ] Chinese text is natural and concise.

## Usage tutorial for the user

If the user asks how to use this skill, summarize `references/usage-tutorial.md`.
