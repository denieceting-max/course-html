# Page Standards

## 16:9 canvas
Default target:
- 1600 x 900 style canvas
- 16:9 aspect ratio
- one slide per screen
- presentation-friendly reading distance

Good CSS patterns:
```css
.deck, .slide-stage {
  width: min(100vw, calc(100vh * 16 / 9), 1600px);
  height: min(100vh, calc(100vw * 9 / 16), 900px);
  aspect-ratio: 16 / 9;
  overflow: hidden;
}
```

## Font size guidance
Use these as approximate ranges, then adapt by density:
- Cover title: 64 to 96 px
- Chapter title: 60 to 86 px
- Content page title: 44 to 64 px
- Card title: 26 to 38 px
- Body text: 18 to 26 px
- Supporting label: 13 to 18 px

## Density handling
If a page is too dense:
1. Simplify wording
2. Split into two pages
3. Change layout from paragraph to cards or table
4. Reduce decorative elements
5. Only then reduce font size slightly

## Truncation prevention
Avoid hidden clipping caused by:
- excessive fixed heights
- too many cards in one row
- large margins stacked vertically
- bottom summary bars with no reserved space
- using `overflow: hidden` on internal content blocks

## Text clarity
Avoid using large `transform: scale()` on full pages or content wrappers because browser text can become blurry. Prefer recalculating font, spacing, and card sizes.

Small hover effects are okay:
```css
.card:hover { transform: translateY(-2px); }
```
