# ROTO-CONTROL Color Palette

All 83 color index values valid for `colorScheme`, `ledOnColor`, and `ledOffColor` fields.

| Value | Name | Hex |
|-------|------|-----|
| 0 | Blush Pink | #F099A7 |
| 1 | Golden Apricot | #F2A948 |
| 2 | Mustard Gold | #C49B40 |
| 3 | Light Lemon | #F6F48D |
| 4 | Lime Zest | #BEFB00 |
| 5 | Neon Lime | #1DFF2D |
| 6 | Minty Aqua | #29FFA9 |
| 7 | Seafoam | #5CFFE8 |
| 8 | Baby Blue | #97C3FA |
| 9 | Royal Blue | #5E7FDD |
| 10 | Lavender Blue | #96A6F9 |
| 11 | Amethyst | #CA72DE |
| 12 | Fuchsia Rose | #D45D9E |
| 13 | White | #FFFFFF |
| 14 | Bright Red | #EB4A41 |
| 15 | Tangerine | #F66B02 |
| 16 | Rustic Brown | #91644F |
| 17 | Sunny Yellow | #FEF133 |
| 18 | Fresh Green | #A5FC7C |
| 19 | Kelly Green | #3DC302 |
| 20 | Turquoise | #03BFB0 |
| 21 | Aqua Blue | #18E9FF |
| 22 | Cerulean | #0EA5EE |
| 23 | Cobalt Blue | #027DC0 |
| 24 | Lavender Purple | #846DDD |
| 25 | Mauve | #AD7AC1 |
| 26 | Hot Magenta | #EB4CCE |
| 27 | Light Gray | #D0D0D0 |
| 28 | Rusty Clay | #D56F60 |
| 29 | Peach | #F2A77C |
| 30 | Antique Gold | #CDAE79 |
| 31 | Pastel Yellow | #F0FEB7 |
| 32 | Pistachio | #D5E3A0 |
| 33 | Olive | #BECF7F |
| 34 | Sage | #A3C392 |
| 35 | Mint Cream | #DCFCE3 |
| 36 | Icy Blue | #D4F0F7 |
| 37 | Periwinkle Blue | #BAC1E0 |
| 38 | Soft Lavender | #CABCE1 |
| 39 | Wisteria | #AA99E0 |
| 40 | Misty Mauve | #E3DCE1 |
| 41 | Gray | #A9A9A9 |
| 42 | Dusty Rose | #DA968E |
| 43 | Taupe | #AF845D |
| 44 | Earthy Taupe | #95846D |
| 45 | Olive Drab | #BEBA74 |
| 46 | Lime Green | #A7BD00 |
| 47 | Avocado Green | #88AF5A |
| 48 | Dusty Teal | #95C0BA |
| 49 | Slate Blue | #A0B2C2 |
| 50 | Steel Blue | #8BA4C4 |
| 51 | Pastel Periwinkle | #8692C8 |
| 52 | Dusty Lavender | #A296B3 |
| 53 | Orchid Mist | #BAA0BC |
| 54 | Rose Quartz | #B27594 |
| 55 | Medium Gray | #7B7B7B |
| 56 | Brick Red | #A13D38 |
| 57 | Burnt Sienna | #9E5639 |
| 58 | Chocolate | #6D5043 |
| 59 | Mustard Yellow | #DBC300 |
| 60 | Olive Grove | #889537 |
| 61 | Forest Green | #669D42 |
| 62 | Deep Teal | #089C8E |
| 63 | Navy | #356281 |
| 64 | Midnight Blue | #1F2E90 |
| 65 | Cobalt | #37519D |
| 66 | Indigo | #5E4CA7 |
| 67 | Vivid Violet | #9850A8 |
| 68 | Raspberry | #BC3D6D |
| 69 | Charcoal | #3C3C3C |
| 70 | Black | #000000 |
| 71 | Fire Red | #FF0000 |
| 72 | Neon Green | #00FF00 |
| 73 | Lemon Yellow | #FFFF00 |
| 74 | Vivid Blue | #0000FF |
| 75 | Vivid Magenta | #FF00FF |
| 76 | Aqua | #00FFFF |
| 77 | Deep Maroon | #800000 |
| 78 | Olive Brown | #808000 |
| 79 | Deep Forest Green | #008000 |
| 80 | Sea Teal | #008080 |
| 81 | Deep Navy | #000080 |
| 82 | Deep Plum | #800080 |

## Notes

- `13` (White) is the safe default for `colorScheme`
- `95` is the skeleton default for `ledOffColor`. This value is not in the standard table
  but is observed to produce a dim neutral inactive state. Use it as the default `ledOffColor`
  unless a specific inactive color is intentional.
- Valid range for standard colors: 0-82. Only use 95 for `ledOffColor`.

## Semantic Color Suggestions

| Function family | Suggested colors |
|---|---|
| Tone / filter | 5 Neon Lime, 18 Fresh Green, 19 Kelly Green, 61 Forest Green |
| Modulation | 8 Baby Blue, 21 Aqua Blue, 22 Cerulean, 7 Seafoam |
| Distortion / aggression | 14 Bright Red, 71 Fire Red, 56 Brick Red |
| FX / spatial | 15 Tangerine, 1 Golden Apricot, 24 Lavender Purple, 11 Amethyst |
| Mix / utility | 13 White, 27 Light Gray, 41 Gray |

## Color Vision Deficiency (CVD)

See `references/cvd-guidance.md` for CVD-safe color subsets, pairs to avoid,
and guidance for building accessible presets. If the user requests a
color-blind-friendly preset, draw colors exclusively from the safe palettes
documented there.