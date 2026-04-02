# Color vision deficiency (CVD) guidance

The 83-color ROTO-CONTROL palette was not designed with color-blindness in mind.
Many pairs that look obviously different under normal vision become nearly
identical under deuteranopia, protanopia, or tritanopia. This section provides
curated subsets and avoidance rules so preset authors can build accessible
color schemes.

Analysis method: Machado et al. (2009) CVD simulation at full severity (100),
with pairwise CIE76 delta-E computed in CIELAB space across normal vision and
all three dichromacy types.

---

## Universal CVD-safe palettes

These subsets remain mutually distinguishable under **all three** dichromacy
types (deuteranopia, protanopia, tritanopia) as well as normal vision.

### Strict (min pair-wise ΔE > 25) -- 10 colors

Best for presets where misidentifying a color could cause real confusion (e.g.
page-per-function layouts where color is the primary navigation cue).

| Value | Name | Hex |
|-------|------|-----|
| 70 | Black | `#000000` |
| 13 | White | `#FFFFFF` |
| 0 | Blush Pink | `#F099A7` |
| 5 | Neon Lime | `#1DFF2D` |
| 8 | Baby Blue | `#97C3FA` |
| 14 | Bright Red | `#EB4A41` |
| 24 | Lavender Purple | `#846DDD` |
| 63 | Navy | `#356281` |
| 69 | Charcoal | `#3C3C3C` |
| 77 | Deep Maroon | `#800000` |

### Moderate (min pair-wise ΔE > 20) -- 13 colors

Good default for most presets. Colors are clearly separable under all CVD
conditions, though close inspection on a small LED ring may require attention
in dim lighting.

| Value | Name | Hex |
|-------|------|-----|
| 70 | Black | `#000000` |
| 13 | White | `#FFFFFF` |
| 0 | Blush Pink | `#F099A7` |
| 4 | Lime Zest | `#BEFB00` |
| 8 | Baby Blue | `#97C3FA` |
| 9 | Royal Blue | `#5E7FDD` |
| 12 | Fuchsia Rose | `#D45D9E` |
| 14 | Bright Red | `#EB4A41` |
| 46 | Lime Green | `#A7BD00` |
| 58 | Chocolate | `#6D5043` |
| 64 | Midnight Blue | `#1F2E90` |
| 74 | Vivid Blue | `#0000FF` |
| 77 | Deep Maroon | `#800000` |

### Relaxed (min pair-wise ΔE > 15) -- 16 colors

Usable when color is supplemented by position, label, or context (e.g. knobs
on different pages that are never viewed side-by-side).

| Value | Name | Hex |
|-------|------|-----|
| 70 | Black | `#000000` |
| 13 | White | `#FFFFFF` |
| 0 | Blush Pink | `#F099A7` |
| 2 | Mustard Gold | `#C49B40` |
| 4 | Lime Zest | `#BEFB00` |
| 6 | Minty Aqua | `#29FFA9` |
| 8 | Baby Blue | `#97C3FA` |
| 9 | Royal Blue | `#5E7FDD` |
| 12 | Fuchsia Rose | `#D45D9E` |
| 16 | Rustic Brown | `#91644F` |
| 45 | Olive Drab | `#BEBA74` |
| 64 | Midnight Blue | `#1F2E90` |
| 69 | Charcoal | `#3C3C3C` |
| 74 | Vivid Blue | `#0000FF` |
| 77 | Deep Maroon | `#800000` |
| 79 | Deep Forest Green | `#008000` |

---

## Pairs to never use together

The following pairs collapse to nearly identical colors (simulated ΔE < 5)
under at least one CVD type, despite being clearly distinct under normal vision
(normal ΔE > 25). Avoid assigning these to knobs or pages where they must be
told apart.

### Protanopia (red-blind) -- worst collisions

| Color A | Color B | Notes |
|---------|---------|-------|
| `0` Blush Pink | `41` Gray | Become indistinguishable (ΔE 0.6) |
| `4` Lime Zest | `17` Sunny Yellow | Both shift to the same yellow (ΔE 0.7) |
| `19` Kelly Green | `46` Lime Green | Merge (ΔE 0.9) |
| `5` Neon Lime | `17` Sunny Yellow | Merge (ΔE 1.4) |
| `17` Sunny Yellow | `72` Neon Green | Both become yellow (ΔE 1.7) |
| `4` Lime Zest | `5` Neon Lime | Merge (ΔE 2.0) |
| `36` Icy Blue | `76` Aqua | Become near-white (ΔE 2.3) |
| `78` Olive Brown | `79` Deep Forest Green | Merge (ΔE 3.9) |

### Deuteranopia (green-blind) -- worst collisions

| Color A | Color B | Notes |
|---------|---------|-------|
| `14` Bright Red | `60` Olive Grove | Both become olive-brown (ΔE 1.9) |
| `29` Peach | `45` Olive Drab | Merge (ΔE 2.2) |
| `26` Hot Magenta | `51` Pastel Periwinkle | Both become blue-gray (ΔE 2.3) |
| `28` Rusty Clay | `43` Taupe | Merge (ΔE 2.5) |
| `54` Rose Quartz | `62` Deep Teal | Merge (ΔE 2.5) |
| `20` Turquoise | `53` Orchid Mist | Both become gray-mauve (ΔE 3.0) |
| `22` Cerulean | `75` Vivid Magenta | Both become blue (ΔE 4.1) |

### Tritanopia (blue-blind) -- worst collisions

| Color A | Color B | Notes |
|---------|---------|-------|
| `1` Golden Apricot | `29` Peach | Merge to same pink-salmon (ΔE 3.3) |
| `7` Seafoam | `21` Aqua Blue | Both become cyan (ΔE 4.2) |
| `35` Mint Cream | `36` Icy Blue | Nearly identical pale wash (ΔE 4.3) |
| `3` Light Lemon | `73` Lemon Yellow | Both become warm cream (ΔE 4.4) |
| `3` Light Lemon | `17` Sunny Yellow | Merge (ΔE 4.6) |

---

## Quick rules for preset authors

1. **When in doubt, pick from the Strict 10.** These are safe for everyone.

2. **Never rely on red vs. green alone.** The classic red/green confusion
   affects both deuteranopia and protanopia, which together account for roughly
   8% of men. If you need a go/stop or on/off pair, use `74` Vivid Blue +
   `73` Lemon Yellow, or `70` Black + `13` White.

3. **Vary lightness, not just hue.** CVD collapses hue differences but
   preserves lightness. A dark blue (`64` Midnight Blue) and a light blue
   (`8` Baby Blue) remain distinguishable under all conditions.

4. **Supplement color with position.** If a preset uses color to indicate
   page identity, also use consistent knob positions or page ordering so
   color is not the only cue.

5. **Test with the Relaxed 16 first.** If you need more than 10 colors and
   cannot use the Strict set, the Relaxed set at ΔE > 15 gives you 16 options
   that are still reliably separable when context helps.