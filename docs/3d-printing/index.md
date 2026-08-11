# 3D Printing Fundamentals — FDM Printers

A beginner-to-intermediate course in fused deposition modelling (FDM / FFF) 3D printing, built
from the official manufacturer handbooks.

This course follows the workflow of the **Original Prusa MK4S / MK3.9S** — from unpacking the
printer through to diagnosing print quality issues. Where a second (or third) machine behaves
differently, the instructions are shown side by side in expandable tabs so you can follow the
printer in front of you.

<div class="session-meta">
  <span>🖨️ FDM / FFF Printing</span>
  <span>🧭 6 Modules</span>
  <span>⚙️ MK4S · MK3.9S · MK3S</span>
  <span>➕ Ender 3 SE (coming soon)</span>
</div>

---

## What you will learn

By the end of this course you will be able to:

- [ ] Operate a 3D printer from the front panel and prepare the print sheet correctly
- [ ] Run the initial calibration (Selftest / Calibration Wizard) on your printer
- [ ] Load and unload filament safely and without tangles
- [ ] Start your first print and remove the finished object safely
- [ ] Source 3D models, slice them in PrusaSlicer, and export print-ready G-code
- [ ] Choose the right material and print-sheet combination for a job
- [ ] Perform routine maintenance (sheets, bearings, fans, nozzle)
- [ ] Diagnose and fix common printer errors
- [ ] Troubleshoot print quality problems systematically

---

## Modules

| # | Module | Covers |
|---|--------|--------|
| 1 | [Your First Print](first-print.md) | Controls, print sheets, calibration, loading filament, the first print, troubleshooting |
| 2 | [Printing Your Own Models](printing-own-models.md) | Finding & creating models, G-code, PrusaSlicer, supports, infill, brim, multicolor |
| 3 | [Material Guide](material-guide.md) | PLA, PETG, ASA/ABS, PC, PVB, Flexible, PA and more |
| 4 | [Regular Maintenance](maintenance.md) | Print sheets, cleaning, bearings, fans, nozzle care |
| 5 | [FAQ — Basic Troubleshooting](faq.md) | Mesh leveling, USB drives, belts, homing, heating & fan errors |
| 6 | [Troubleshooting Print Quality](print-quality.md) | Identifying and fixing common print defects |

---

## How this course was built

The content is adapted — combined, renumbered and re-sourced — from the two official Prusa
handbooks, with the text of each section reproduced as closely as possible so you can always
return to the original manual for the authoritative detail. Where the two printers differ, the
instructions are shown in tabs.

### Sources

| Document | Version | Publisher | Copyright | Download |
|----------|---------|-----------|-----------|----------|
| Original Prusa MK4S / MK3.9S Handbook | 1.0.1 (EN) | Prusa Research s.r.o. | © Prusa Research s.r.o. | [prusa3d.com/drivers](https://www.prusa3d.com/drivers/) |
| Original Prusa i3 MK3S Handbook | 3.11 (EN) | Prusa Research s.r.o. | © Prusa Research s.r.o. | [prusa3d.com/drivers](https://www.prusa3d.com/drivers/) |

!!! note "Attribution & copyright"
    **Text and images** in this course are reproduced from the Original Prusa handbooks and are
    © **Prusa Research s.r.o.** They are used here for **educational and training purposes only**
    with attribution. This is not an official Prusa product or endorsement. All trademarks belong
    to their respective owners.

    Each figure caption records the source manual and page so it can be traced back to the
    original document. Where content was written for this course (comparison tables, tabs, the
    "in your words" activities), it is original material and not covered by the above copyright.

### Why the tabbed comparisons?

The three printers covered in this course are different generations:

- **MK4S / MK3.9S** — current generation. Touchscreen + rotary knob, Nextruder with LoadCell
  sensor, USB drive printing, 250 × 210 × 220 mm build volume.
- **MK3S** — previous generation. LCD + rotary knob only, PINDA induction probe, SD card
  printing, 250 × 210 × 200 mm build volume, the "kit" classic.
- **Ender 3 SE** *(added later)* — a third-party printer using the **Creality / Cura** slicing
  workflow rather than PrusaSlicer.

When the instructions are the same for all printers, they are written once. When they diverge,
use the tabbed sections:

=== "MK4S / MK3.9S"
    Instructions for the current-generation Prusa printer.

=== "MK3S"
    Instructions for the older Prusa printer.

=== "Ender 3 SE"
    Instructions for the Creality printer *(to be added)*.

---

## Safety first

!!! warning "Before you start"
    A 3D printer runs on **mains electricity**, has a **nozzle that exceeds 200 °C**, a **heated
    bed that can exceed 100 °C**, and **moving parts** driven by stepper motors.

    - Never touch the nozzle, heater block, or hot heatbed with bare skin
    - Keep the printer on a flat, stable surface away from drafts
    - Ventilate the room when printing ABS/ASA or other styrene-based materials
    - Never leave a preheated, idle printer unattended for long periods
    - Keep fingers clear of the moving X/Y/Z axes and the filament feed gear

---

## Quick links

- [help.prusa3d.com](https://help.prusa3d.com) — official knowledge base (troubleshooting, maintenance, materials)
- [prusaslicer.com](https://www.prusaslicer.com) — PrusaSlicer download
- [printables.com](https://www.printables.com) — free 3D models
- [prusa3d.com/category/prusa-academy](https://www.prusa3d.com/category/prusa-academy) — official tutorials
