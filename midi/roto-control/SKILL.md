---
name: roto-control-preset
description: >
  Design, author, and review Melbourne Instruments ROTO-CONTROL MIDI preset JSON files.
  Covers schema rules, label limits, haptic detents, LED colors, page layout, and CC allocation.
---

# ROTO-CONTROL Preset Authoring

Reference files in `references/` contain the full color palette, schema field reference,
and validation checklist. Load them when needed.

---

## Hardware Model

8 knobs × 8 buttons × 4 pages = **32 knobs + 32 buttons** per preset.

Page layout (controlIndex ranges):

| Page | Knobs | Buttons |
|------|-------|---------|
| 1 | 0–7 | 0–7 |
| 2 | 8–15 | 8–15 |
| 3 | 16–23 | 16–23 |
| 4 | 24–31 | 24–31 |

Each physical column (1–8) has one knob above and one button below. Design columns as a
single coherent concept (e.g., filter knob + filter mode button).

---

## Label Rules

- `controlName` and all `stepNames` entries: **12 characters maximum, no exceptions**
- Use the full budget — don't shorten unnecessarily
- Shortening order: remove spaces first, preserve the main concept, shorten least-important suffix last

Good: `FilterCutof`, `PitchSmooth`, `StereoWidth`
Bad: `Cut`, `Mod`, `FX1`

---

## Button Display Behavior (CRITICAL)

- Button **without steps**: screen shows `controlName`
- Button **with steps**: screen shows the **current step name** — `controlName` is hidden during use

For any button with steps, make `stepNames` fully self-contained. Do not rely on `controlName`
to explain what a step means.

Good step names: `Stereo Out` / `Mono Out`, `Bass Input` / `Seq Input`
Bad step names: `On` / `Off`, `A` / `B`, `1` / `2`

---

## Button Categories

**Simple toggle (2 steps):** two states cycling on press. Set `hapticSteps: 2`.

**Multi-step selector (3+ steps):** discrete mode selector. Set `hapticSteps` to step count.

**Single-action / utility (no steps):** not stateful — leave all `stepNames` as `""`,
set `hapticSteps: 0`, and let `controlName` be shown.

---

## PUSH vs. TOGGLE

| Type | Behavior | Use when |
|------|----------|----------|
| PUSH | Fires on press, no state held | Triggers, one-shots, momentary |
| TOGGLE | Cycles steps, holds state | Mode selects, on/off, multi-state |
| KNOB | Continuous CC | Smoothly varying parameters |
| STEP | Stepped CC with detents | Small number of named positions |

The JSON encoding of TYPE is not fully documented. The skeleton always uses `controlMode: 0`.
Express design intent through `stepNames` and `hapticSteps`, then confirm TYPE in Roto-Setup
App before deployment. Do not assume `controlMode: 1` = TOGGLE without testing.

---

## Stepped Knobs

Continuous knob: `stepNames` all empty, any smoothly varying parameter.

Stepped knob: `stepNames` populated with up to 16 named positions; acts as a rotary selector.

Good use: waveform selector, filter type, octave. Bad use: any parameter benefiting from
fine resolution, or anything with more than 16 meaningful states.

Same 12-character label limit applies to knob `stepNames`.

---

## stepNames Array (CRITICAL)

Always **exactly 16 entries** regardless of how many steps are active.
Active names come first; unused positions use `""`.

```json
"stepNames": ["Stereo Out", "Mono Out", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
```

---

## One-Control-One-Function

Each knob or button sends exactly one MIDI control. Buttons cannot perform macros.
Complex behavior must be handled by the target system or an external routing layer.

Do not create fake scene or macro buttons unless the target truly maps that CC to one action.

---

## Page Design

- **Page 1:** live performance controls — primary tone, mix, most critical mode toggles.
  Must be understandable without memory.
- **Page 2:** routing and secondary controls — source blend, smoothing, alt levels
- **Page 3:** detail / engine / device-specific controls
- **Page 4:** advanced, setup-only, rarely used, or future expansion

---

## Naming Consistency

Use noun phrases for knobs, visible state descriptions for button steps.
Pick one term and use it everywhere: `Level` or `Gain`, not both; `Dist` or `Drive`, not both.

---

## Color Rules

Use semantically consistent color families across the preset:
- tone/filter → green family
- modulation/movement → blue or cyan family
- distortion/aggression → red family
- FX/spatial → orange or purple family
- mix/utility → neutral/light family

Use `13` (White) as a safe default for `colorScheme`.
Use `95` as the default `ledOffColor` (dim/inactive state; skeleton default).
See `references/color-palette.md` for all 83 color values.
See `references/cvd-guidance.md` for color-blind-safe subsets and pairs to avoid.
If the user requests an accessible or color-blind-friendly preset, use only colors
from the CVD-safe palettes documented there.

---

## CC Allocation

| Control type | Safe CC range |
|---|---|
| Knobs | 20–51 |
| Buttons | 80–111 |

The manual states some CCs are reserved for internal use but does not enumerate them.
The skeleton's ranges are confirmed safe. Avoid values outside these unless verified.

---

## Min/Max Values

Defaults (0 and 127) work for most targets. Verify against your target device:
- Some devices expect ON = 64, not 127
- NRPN mode may require `maxValue: 16383`

---

## Schema Quick Reference

See `references/schema-field-reference.md` for full field documentation.

**Knob required fields:** `controlIndex`, `controlMode`, `controlChannel`, `controlParam`,
`nrpnAddress` (0), `minValue`, `maxValue`, `controlName`, `colorScheme`, `hapticMode`,
`hapticIndent1` (255 = off), `hapticIndent2` (255 = off), `hapticSteps` (always 0), `stepNames` (16 entries)

**Button required fields:** all knob fields except `hapticIndent1`/`hapticIndent2`, plus
`ledOnColor`, `ledOffColor`

Knobs never have `ledOnColor`/`ledOffColor`. Buttons never have `hapticIndent1`/`hapticIndent2`.

See `references/validation-checklist.md` before finalizing any preset.

---

## Anti-Patterns

- Any label > 12 characters
- `On` / `Off` step names when something descriptive would fit
- Relying on `controlName` to explain a stepped button
- Fake macro or scene buttons
- Unrelated knob and button in the same column
- Fewer than 16 entries in any `stepNames` array
- `ledOnColor`/`ledOffColor` on a knob entry
- `hapticIndent1`/`hapticIndent2` on a button entry
- `hapticSteps` other than 0 on a knob
- Color index values outside 0–82 (except 95 for `ledOffColor`)
- CC numbers outside confirmed safe range without explicit intent

---

## Design Goal

A good preset lets a performer answer at a glance:
1. What does this knob control?
2. What state is this button currently in?
3. What is this page for?
4. Which controls are related?