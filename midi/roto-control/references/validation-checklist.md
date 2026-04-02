# ROTO-CONTROL Preset Validation Checklist

Run through this before finalizing any preset.

## Hardware / Layout

- [ ] Exactly 32 knobs defined (`controlIndex` 0–31)
- [ ] Exactly 32 buttons defined (`controlIndex` 0–31)
- [ ] `index` is set to the intended slot — importing overwrites that slot
- [ ] Page 1 is the live performance page
- [ ] Each column's knob and button are conceptually related

## Schema Integrity

- [ ] Every `stepNames` array has exactly 16 entries
- [ ] Active step names are at the front; trailing entries are `""`
- [ ] All knob entries include `nrpnAddress`, `hapticIndent1`, `hapticIndent2`, `hapticSteps`
- [ ] All knob entries do NOT contain `ledOnColor` or `ledOffColor`
- [ ] All button entries include `ledOnColor`, `ledOffColor`, and `hapticSteps`
- [ ] All button entries do NOT contain `hapticIndent1` or `hapticIndent2`
- [ ] `hapticSteps` on every knob is `0`
- [ ] `hapticSteps` on each button matches the count of non-empty step names
- [ ] `hapticIndent1` and `hapticIndent2` are `255` unless a detent is intentional
- [ ] `controlChannel` matches the target device
- [ ] No CC numbers outside 20–51 (knobs) or 80–111 (buttons) unless explicitly intentional

## Labels

- [ ] Every `controlName` is 12 characters or fewer
- [ ] Every visible `stepName` is 12 characters or fewer
- [ ] Labels are descriptive, not cryptic abbreviations

## Buttons

- [ ] PUSH vs. TOGGLE intent is decided for each button
- [ ] Stepped buttons have meaningful state labels (not `On`/`Off`, `A`/`B`, `1`/`2`)
- [ ] Non-stateful buttons have no step names and `hapticSteps: 0`
- [ ] No fake macro or scene buttons

## Colors

- [ ] Only color index values 0–82 are used (plus 95 for `ledOffColor`)
- [ ] `ledOffColor` is a dim/neutral value for inactive contrast
- [ ] Color families are consistent with control function

## Consistency

- [ ] Naming style is uniform across the preset
- [ ] Term choices are consistent (one term for Level/Gain, Dist/Drive, etc.)
- [ ] Related controls share a color family

## Usability

- [ ] Page 1 is immediately understandable without prior knowledge
- [ ] No hidden meanings required
- [ ] Display text communicates the control's function or current state
