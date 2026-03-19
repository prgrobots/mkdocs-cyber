# Week 4 — Forensic Recovery: PC Teardown

<div class="session-meta">
  <span>📅 Week 4</span>
  <span>⏱ 2 Hours</span>
  <span>🔵 Phase 1 — Reconnaissance</span>
  <span>📋 ICTICT213</span>
</div>

---

!!! danger "MISSION BRIEF"
    **Incident Reference:** RBS-2025-004  
    The laptop returned from the conference has been flagged as potentially compromised.
    Before imaging or rebuilding, you need to **document the hardware state** — what's 
    inside, whether anything has been tampered with, and whether the drive needs to be
    pulled before powering on. This is a forensic teardown. Document everything.

---

## Learning Objectives

- [ ] Safely disassemble and reassemble a desktop PC
- [ ] Apply ESD (electrostatic discharge) precautions
- [ ] Document hardware findings methodically
- [ ] Identify signs of physical tampering
- [ ] Reassemble and POST test

---

## Before You Touch Anything

!!! warning "ESD — Electrostatic Discharge"
    Static electricity from your body can destroy components. Always:
    
    - Wear an anti-static wrist strap connected to the case ground
    - Work on an anti-static mat if available
    - Touch the case before touching any component
    - Never work on carpet

### Forensic mindset

In a real incident, you photograph **before** you move anything. Today you are doing the same. Your documentation is evidence.

---

## Teardown Procedure

### Step 1 — Pre-teardown documentation

Before opening the case:

- [ ] Photograph the external condition of the machine
- [ ] Note any damage, unusual marks, or signs of tampering
- [ ] Record the asset tag, serial number, make and model
- [ ] Note whether the machine is powered on or off when received

### Step 2 — Open the case

```
Tools needed:
- Phillips head screwdriver (usually #2)
- Anti-static wrist strap
- Torch (for seeing inside)
- Camera or phone for photos
```

Most desktop cases: remove 2 thumbscrews on rear panel, slide panel towards you.

### Step 3 — Internal inspection

Before touching anything, photograph the inside in its current state. Then check:

- [ ] Are all cables properly seated? Any loose connectors?
- [ ] Any dust buildup indicating age or neglect?
- [ ] Any components that look out of place or recently disturbed?
- [ ] Any burn marks, capacitor bulging, or corrosion?
- [ ] Any foreign objects (hardware keyloggers between keyboard header and board)?

!!! warning "TAMPER INDICATORS"
    Signs a machine may have been physically accessed:
    
    - Scratches around screw heads (tool marks)
    - Disturbed dust patterns inside the case
    - CMOS battery recently replaced (battery date codes)
    - Additional USB headers or PCIe cards that aren't in the asset register
    - BIOS settings changed from known-good baseline

### Step 4 — Component removal (in order)

Remove and photograph each component:

1. **GPU** (if present) — release PCIe latch, pull straight out
2. **RAM** — press tabs simultaneously, pull straight up  
3. **Storage** — disconnect data and power cables, unscrew or release bracket
4. **CPU cooler** — unscrew/unlatch, lift straight up (twist slightly if stuck)
5. **CPU** — lift retention arm, lift CPU straight up — **do not touch the pins/pads**

Place each component on the anti-static mat. Label your photos.

### Step 5 — Reassembly

Reverse the teardown order:

1. CPU → cooler → RAM → storage → GPU → cables

Apply fresh thermal paste to CPU if cooler was removed (thin pea-sized amount, centre of IHS).

### Step 6 — POST test

Power on. Does the machine POST? Do you see BIOS splash screen?

If no POST: reseat RAM first (most common cause), then GPU, then check 24-pin power connector.

---

## Lab Task

!!! example "TASK 4.1 — Documented Teardown (AT1 Practical Task 1)"
    
    Complete the full teardown and reassembly of the lab PC at your station.
    
    **Your documentation must include:**
    
    - [ ] Pre-teardown photos (external)
    - [ ] Internal condition photo (before any removal)
    - [ ] Photo of each component removed, labelled with component name
    - [ ] Written inventory: list every component with make/model/specs where visible
    - [ ] Note any anomalies found
    - [ ] Post-reassembly: confirm machine POSTs
    - [ ] Brief written summary: "would this machine be safe to return to service?" + justification

    Submit photos + written summary to your AT1 portfolio folder.

---

## Unit Mapping

??? info "Assessment Mapping — click to expand"

    | Activity | Unit | Element |
    |----------|------|---------|
    | Hardware teardown and documentation | ICTICT213 | 1.4, 2.3 |
    | POST verification | ICTICT213 | 2.3 |
    | Anomaly identification | ICTICT213 | 1.4 |
