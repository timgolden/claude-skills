# ROTO-CONTROL Schema Field Reference

## Top-Level Preset Fields

| Field | Type | Notes |
|-------|------|-------|
| `version` | integer | Always `1` in current firmware |
| `type` | string | Always `"MIDI"` for MIDI presets |
| `name` | string | Displayed as Setup name in Roto-Setup App and on device |
| `index` | integer | Preset slot 0–63; importing overwrites that slot |

Set `index` deliberately. Importing will overwrite whatever is currently in that slot.

---

## Per-Control Fields

### nrpnAddress

Required on every knob and button. Set to `0` unless NRPN mode is in use.
Do not omit — some importers may reject entries without it.

```json
"nrpnAddress": 0
```

### controlMode

| Value | Confirmed meaning |
|-------|------------------|
| 0 | CC coarse (default; all controls in skeleton) |
| 1 | Likely CC fine or NRPN; not fully documented |

The relationship between `controlMode` and PUSH/TOGGLE/KNOB/STEP is not confirmed from
available documentation. Use `controlMode: 0` as the safe default and configure TYPE in
the Roto-Setup App after import.

### controlChannel

MIDI channel 1–16. Must match the target device's receive channel. Skeleton defaults to 1.
If controlling multiple devices from one preset, assign different channels per page or group.

---

## Knob-Specific Fields

### hapticMode (knobs)

Controls motor resistance feel, not detent placement.

| Value | Behavior |
|-------|----------|
| 0 | Default knob feel; used on all knobs in production presets |

Additional values may exist but are not confirmed.

### hapticIndent1 and hapticIndent2 (knobs) — CRITICAL

Place physical haptic detent positions on knob rotation.

| Value | Meaning |
|-------|---------|
| 255 | No indent (disabled) — default |
| 0–127 | Indent at this position (64 = center/midpoint) |

Both default to 255. Both are required fields on every knob. Set to 255 when unused.

**Use a center indent (`hapticIndent1: 64`) only when center has a meaningful zero/neutral value:**
pan, detune, blend, stereo width, FX wet/dry.

Do not add a center indent to parameters where center has no special meaning (level, cutoff, rate).

`hapticIndent2` is available for a second detent. Use only when two positions are genuinely meaningful.

### hapticSteps (knobs)

Always `0` on knobs. Knobs do not use step cycling.

---

## Button-Specific Fields

### ledOnColor / ledOffColor

LED color when button is active/on and inactive/off respectively.
Valid range: 0–82, plus 95 for `ledOffColor` (dim neutral, skeleton default).
See `color-palette.md` for the full table.

Do not add these fields to knob entries.

### hapticMode (buttons)

| Value | Behavior |
|-------|----------|
| 0 | No haptic feedback |
| 1 | Haptic click on press; skeleton default |

### hapticSteps (buttons)

- `0` for PUSH/single-action buttons
- Set to count of non-empty `stepNames` entries for TOGGLE/cycling buttons

Example: a 3-state selector has `hapticSteps: 3`.
The value must always equal the count of non-empty entries in `stepNames`.

---

## NRPN and Fine Resolution

When fine or NRPN resolution is needed:
- Set `maxValue` to 16383 (not 127)
- Set CC MSB in `controlParam`; LSB is assigned automatically by the device

Only use when the target device meaningfully responds to sub-128 resolution.

---

## Field Asymmetry Summary

| Field | Knobs | Buttons |
|-------|-------|---------|
| `hapticIndent1` | Required (255 = off) | Not present |
| `hapticIndent2` | Required (255 = off) | Not present |
| `hapticSteps` | Required, always 0 | Required, 0 or step count |
| `ledOnColor` | Not present | Required |
| `ledOffColor` | Not present | Required |
| `nrpnAddress` | Required (0) | Required (0) |
