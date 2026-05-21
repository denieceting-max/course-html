#!/usr/bin/env python3
"""Quick structural audit for HTML presentation decks."""

from __future__ import annotations

import re
import sys
from pathlib import Path


def count(pattern: str, text: str) -> int:
    return len(re.findall(pattern, text, flags=re.IGNORECASE | re.DOTALL))


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: audit_html_deck.py <deck.html>")
        return 2

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"ERROR: file not found: {path}")
        return 1

    text = path.read_text(encoding="utf-8", errors="replace")
    lower = text.lower()

    slide_count = max(
        count(r'class=["\'][^"\']*(?:slide-section|\bslide\b)[^"\']*["\']', text),
        count(r'<section\b', text),
    )

    warnings: list[str] = []

    if "aspect-ratio" not in lower and "16 / 9" not in lower and "16/9" not in lower:
        warnings.append("No obvious 16:9 aspect-ratio rule found.")

    tiny_px = [int(x) for x in re.findall(r'font-size\s*:\s*(\d+)px', lower)]
    tiny_px = [x for x in tiny_px if x < 13]
    if tiny_px:
        warnings.append(f"Found {len(tiny_px)} font-size values below 13px; check projection readability.")

    small_rem = [float(x) for x in re.findall(r'font-size\s*:\s*(\d+(?:\.\d+)?)rem', lower)]
    small_rem = [x for x in small_rem if x < 0.85]
    if small_rem:
        warnings.append(f"Found {len(small_rem)} font-size values below 0.85rem; check readability.")

    scale_count = count(r'transform\s*:[^;]*scale\(', lower) + count(r'\.style\.transform\s*=\s*`?scale\(', lower)
    if scale_count > 6:
        warnings.append("Many scale transforms found; large whole-page scaling may blur text.")

    if "overflow: hidden" in lower and slide_count == 0:
        warnings.append("overflow:hidden is used, but no slide structure was detected.")

    print("HTML deck audit")
    print(f"File: {path}")
    print(f"Detected slide/section count: {slide_count}")
    print(f"CSS/JS scale transform occurrences: {scale_count}")
    if warnings:
        print("Warnings:")
        for item in warnings:
            print(f"- {item}")
    else:
        print("No major structural warnings found.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
