# Module 6 — Troubleshooting Print Quality Issues

<div class="session-meta">
  <span>🖨️ Module 6</span>
  <span>⏱ ~30 min</span>
  <span>🟠 Ongoing</span>
</div>

*Content adapted from the Original Prusa MK4S / MK3.9S Handbook §11 and the Original Prusa i3
MK3S Handbook §13.7–13.8. © Prusa Research s.r.o. — used for educational purposes.*

If prints are not quite up to your expectations or even have major flaws (**shifted layers,
ghosting, under-extrusion**), it is necessary to find the cause of the issue and address it.

!!! tip "The first place to look"
    On **help.prusa3d.com** you will find troubleshooting guides for 3D printing quality issues,
    including pictures and specific advice for different types of printers.

---

## 6.1 The systematic approach

Before changing anything:

1. **Print a known-good model** — the supplied sample files (e.g. the Prusa Logo Keychain).
   - Sample prints fine but your model doesn't → the problem is in the **slicing** (see 6.2).
   - Sample prints badly too → the problem is **mechanical or material** (see 6.3).
2. Change **one variable at a time**, and keep notes.

## 6.2 Slicing-related causes

If your custom print fails while the sample files print correctly, re-slice with the default
PrusaSlicer settings and check for:

- Incorrect printer/nozzle profile (default nozzle is **0.4 mm**)
- Incorrect material settings
- Missing supports
- Incorrectly configured infill
- The model is not in contact with the print sheet

Always inspect the **Preview** before exporting the G-code.

## 6.3 Common print defects and fixes

=== "First layer peeling off the bed"
    - Greasy bed → degrease with isopropyl alcohol (or warm water + dish soap)
    - Wrong material/sheet combination (e.g. PLA on textured) → see the Material Guide
    - Small contact area → use a **brim** in PrusaSlicer

=== "Layers break and split (often ABS)"
    ABS has higher thermal expansion than other materials. Print in an **enclosure**, away from
    drafts. For larger models consider PETG, HIPS or PLA instead.

=== "Too much or too little filament"
    Adjust the **flow** during the print: **LCD Menu → Tune → Flow** (e.g. 95 % or 105 %).
    Remember the setting persists for the next print unless you change it again or reset.

=== "Model breaks or is easily damaged"
    Typical of larger ABS prints. Check the temperature settings, keep the printer away from
    drafts, and consider a stronger material (PETG or PLA — though PLA has low heat resistance).
    For a temporary fix, superglue works well on plastics.

=== "Nozzle stops extruding mid-print"
    - Filament tangled on the spool → fix the tangle (Module 1)
    - Clogged/blocked nozzle → cold pull or needle cleaning (Module 4)
    - Deformed steel filament guide (MK4S) → check the thumbscrews aren't overtightened

---

## 6.4 When to escalate

- The error screen on the printer shows a QR code / link → follow it to the specific help article
- Component-level repairs (hotend removal, gearbox, belts) → the **assembly manual** and
  **help.prusa3d.com**
- If the machine worked before and nothing was changed, ask: what changed? A different filament,
  a moved printer, a new sheet, a firmware update?

---

## In your words — Module 6 reflection

- [ ] You see stringing on a PETG print. List two settings to change.
- [ ] A print has shifted layers partway up. Is this more likely slicing or mechanical, and why?
- [ ] Why is it useful to keep a known-good sample file on your USB drive / SD card?
