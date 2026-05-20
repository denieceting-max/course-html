# Style Guide

## Overall look

Use a clean white business-tech style:

- Background: `#f1f5f9` outside, white slide canvas inside.
- Main slide: rounded `3xl`, subtle border, soft shadow.
- Decorative gradients: pale blue, teal, purple, orange depending on section.
- Avoid dark backgrounds unless explicitly requested.
- Avoid strong neon glow, dense graphics, and complex cyberpunk effects.

## Typography

Recommended hierarchy:

- Page label: `text-sm xl:text-base`, blue, bold, letter spacing.
- Main title: `text-[34px] xl:text-[50px]` for content pages.
- Cover title: `text-[64px] xl:text-[88px]` if space allows.
- Chapter title: `text-[54px] xl:text-[76px]` if only one chapter title.
- Body text: `text-base xl:text-lg`; shrink only for dense content.
- Emphasis: use blue / teal / purple spans, not all caps.

## Layout

Standalone page shell:

```html
<body class="min-h-screen flex flex-col items-center justify-center p-2 xl:p-4 overflow-x-auto relative">
  <div id="slideContent" class="w-full max-w-[1536px] aspect-[16/9] bg-white rounded-3xl shadow-xl border border-slate-200/70 p-5 xl:p-6 shrink-0 relative overflow-hidden flex flex-col">
    <!-- content -->
  </div>
</body>
```

Content pages should normally use:

- Header at top, compact.
- Main card in the middle, flex-1 when possible.
- Optional footer/summary at bottom with enough margin.

## Visual elements

Use cards and chips:

- Main card: rounded `[30px]`, gradient from blue-50/white/teal-50.
- Content card: white/95, border slate-200, subtle shadow.
- Keyword chip: rounded-full, colored light background, bold text.
- Icons: lucide icons, simple and consistent.

## Avoid clipping

Before finalizing:

- Do not rely on fixed huge heights if content is dense.
- Use `flex-1 min-h-0` for central content where possible.
- Reduce margins before shrinking font too much.
- If a footer is clipped, first reduce main card padding/gaps, then reduce footer height.
