# Integrated Scrolling Deck

Use this when the user wants many standalone HTML pages combined into one scrolling HTML page.

## Required behavior

- Each page behaves like a 16:9 presentation screen.
- Top navigation contains page anchors and current-page highlight.
- A lightweight top progress bar shows scroll progress.
- Keyboard navigation moves directly to previous/next full page.
- Content-level click animation works inside each page.
- Do not add complex animations.

## Parent page layout guidance

Use a fixed top nav and one section per page.

Important alignment rule:

- If `main` has `padding-top: var(--nav-h)`, keyboard scroll target should be `section.offsetTop - navHeight()`.
- Do not additionally change section heights or scroll-snap unless tested; it can cause over-scroll or under-scroll.
- Keep the accepted stable version: original 16:9 iframe layout + precise keyboard navigation + iframe pointer events enabled.

Core parent CSS:

```css
:root { --nav-h: 58px; }
main { padding-top: var(--nav-h); }
.slide-section {
  min-height: calc(100vh - var(--nav-h));
  scroll-margin-top: var(--nav-h);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 10px clamp(8px, 1.2vw, 16px) 16px;
  position: relative;
}
.iframe-wrap {
  width: min(1536px, calc((100vh - var(--nav-h) - 26px) * 16 / 9), calc(100vw - 20px));
  aspect-ratio: 16 / 9;
  border-radius: 24px;
  overflow: hidden;
}
.slide-iframe {
  width: 100%;
  height: 100%;
  border: 0;
  display: block;
  background: #fff;
  pointer-events: auto;
}
```

Core keyboard logic:

```js
(function () {
  const sections = Array.from(document.querySelectorAll('.slide-section'));
  let lock = false;

  function navHeight() {
    return parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--nav-h')) || 58;
  }

  function targetTop(index) {
    const section = sections[index];
    if (!section) return 0;
    return Math.max(0, section.offsetTop - navHeight());
  }

  function currentIndex() {
    const y = window.scrollY + navHeight() + 4;
    let bestIndex = 0;
    let bestDistance = Infinity;
    sections.forEach((section, index) => {
      const distance = Math.abs(section.offsetTop - y);
      if (distance < bestDistance) {
        bestDistance = distance;
        bestIndex = index;
      }
    });
    return bestIndex;
  }

  function goTo(index) {
    const next = Math.max(0, Math.min(sections.length - 1, index));
    lock = true;
    window.scrollTo({ top: targetTop(next), behavior: 'smooth' });
    window.setTimeout(() => { lock = false; }, 680);
  }

  function go(direction) {
    if (lock) return;
    goTo(currentIndex() + direction);
  }

  document.addEventListener('keydown', event => {
    const nextKeys = ['ArrowDown', 'ArrowRight', 'PageDown', ' '];
    const prevKeys = ['ArrowUp', 'ArrowLeft', 'PageUp'];
    if (![...nextKeys, ...prevKeys].includes(event.key)) return;
    event.preventDefault();
    event.stopImmediatePropagation();
    if (nextKeys.includes(event.key)) go(1);
    if (prevKeys.includes(event.key)) go(-1);
  }, true);

  window.addEventListener('message', event => {
    if (!event.data || event.data.type !== 'ai-course-page-key') return;
    if (event.data.direction === 'next') go(1);
    if (event.data.direction === 'prev') go(-1);
  });
})();
```

## Content-level click animation for child pages

Inject into each child HTML page if using iframe `srcdoc`.

Expected result: clicking a card, icon, chip, image, or content block gently scales that element, not the whole screen.

```css
.ai-content-pop {
  transition: transform 180ms cubic-bezier(.2,.8,.2,1), box-shadow 180ms ease, filter 180ms ease;
  transform-origin: center center;
  will-change: transform;
  cursor: pointer;
}
.ai-content-pop.is-pop-active {
  transform: scale(1.065);
  filter: saturate(1.06);
  box-shadow: 0 18px 42px -28px rgba(37,99,235,.45), 0 8px 20px -18px rgba(20,184,166,.35);
  z-index: 30;
  position: relative;
}
.ai-content-ripple {
  position: fixed;
  width: 14px;
  height: 14px;
  pointer-events: none;
  border-radius: 999px;
  z-index: 9999;
  transform: translate(-50%, -50%) scale(.4);
  background: radial-gradient(circle, rgba(37,99,235,.30) 0%, rgba(20,184,166,.18) 48%, rgba(37,99,235,0) 74%);
  animation: aiContentRipple 520ms ease-out forwards;
}
@keyframes aiContentRipple {
  0% { opacity: .9; transform: translate(-50%, -50%) scale(.4); }
  70% { opacity: .34; }
  100% { opacity: 0; transform: translate(-50%, -50%) scale(7); }
}
```

Child page should forward keyboard events to parent:

```js
document.addEventListener('keydown', function (event) {
  var nextKeys = ['ArrowDown', 'ArrowRight', 'PageDown', ' '];
  var prevKeys = ['ArrowUp', 'ArrowLeft', 'PageUp'];
  if (nextKeys.indexOf(event.key) === -1 && prevKeys.indexOf(event.key) === -1) return;
  event.preventDefault();
  event.stopPropagation();
  window.parent.postMessage({
    type: 'ai-course-page-key',
    direction: nextKeys.indexOf(event.key) !== -1 ? 'next' : 'prev'
  }, '*');
}, true);
```
