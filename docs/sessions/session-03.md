# Week 3 — Hardware & Physical Security

<div class="session-meta">
  <span>📅 Week 3</span>
  <span>⏱ 2 Hours</span>
  <span>🔵 Phase 1 — Reconnaissance</span>
  <span>📋 ICTICT213</span>
</div>

---

!!! danger "MISSION BRIEF"
    **Incident Reference:** RBS-2025-003  
    A Redback Systems laptop was returned from a conference. The owner says it's
    "running differently." You've been asked to inspect it before connecting it
    back to the corporate network. Today you learn what's inside a PC,
    what each component does, and what an attacker can do with physical access.

---

## Learning Objectives

- [ ] Identify the main hardware components of a PC
- [ ] Explain what each component does and its role in security
- [ ] Describe physical attack vectors (evil maid, cold boot, USB attacks)
- [ ] Explain BIOS/UEFI and Secure Boot
- [ ] Understand why physical access = game over (mostly)

---

## 1. PC Hardware Components

| Component | Function | Security Relevance |
|-----------|----------|-------------------|
| **CPU** | Executes instructions | Spectre/Meltdown vulnerabilities live here |
| **RAM** | Short-term memory | Cold boot attack — encryption keys survive brief power loss |
| **Storage (HDD/SSD)** | Long-term storage | Encryption essential — unencrypted drives are trivially read |
| **Motherboard** | Connects everything | BIOS chip, firmware attacks |
| **NIC** | Network connectivity | MAC address spoofing, hardware-level monitoring |
| **GPU** | Graphics processing | Also used for password cracking (you'll use this in Week 10) |
| **PSU** | Power | Power analysis attacks (advanced) |
| **TPM chip** | Security co-processor | Stores BitLocker keys, enables Secure Boot verification |

---

## 2. BIOS / UEFI

**BIOS** (Basic Input/Output System) and its modern replacement **UEFI** (Unified Extensible Firmware Interface) run before the OS. They:

- Perform POST (Power-On Self Test)
- Detect and initialise hardware
- Load the bootloader
- Control boot order

### Why attackers care about BIOS/UEFI

- **Boot order manipulation** — boot from USB to bypass OS login entirely
- **BIOS password bypass** — remove CMOS battery, reset jumper, or in older machines trivially bypass
- **UEFI rootkits** — malware that lives in firmware, survives OS reinstall
- **Secure Boot** — UEFI feature that verifies bootloader is signed and trusted

!!! warning "Secure Boot is not optional in a secure environment"
    If Secure Boot is disabled, someone with brief physical access can boot a 
    live USB, mount your drives, and read everything — even if you have a Windows login password.

---

## 3. Physical Attack Vectors

### Evil Maid Attack

Named after the hotel maid who has unsupervised access to your room while you're at breakfast. With 5-10 minutes of physical access an attacker can:

- Boot from USB and dump the hard drive
- Install a hardware keylogger between keyboard and PC
- Extract BitLocker key from RAM (cold boot)
- Plant a hardware implant on the motherboard

### Cold Boot Attack

RAM retains data for seconds to minutes after power is removed — longer if cooled (frozen). An attacker can:

1. Freeze the RAM sticks (extends retention to minutes)
2. Remove RAM and insert into attack machine
3. Dump contents — encryption keys may be present

**Mitigation:** Enable BitLocker PIN at startup (keys not loaded into RAM until PIN entered).

### Malicious USB (BadUSB)

A USB device that presents itself as a keyboard and types commands at machine speed. Plug it in, walk away. Within 30 seconds it can create a backdoor user, exfiltrate files, or install malware.

---

## 4. What Redback Systems Should Do

!!! note "PHYSICAL SECURITY CONTROLS"
    
    - **Encrypt all drives** with BitLocker (Windows) or LUKS (Linux)
    - **BIOS password** on all managed devices
    - **Secure Boot enabled** on all managed devices
    - **USB port control** via endpoint policy — only authorised devices
    - **Cable locks** for fixed workstations in shared spaces
    - **Device tracking** — know where every asset is at all times
    - **Incident procedure** for returned/lost devices — do not reconnect without inspection

---

## Lab Task

!!! example "TASK 3.1 — Hardware Identification"

    Inspect the lab PC at your station **without powering it on**.
    
    - [ ] Identify: CPU, RAM sticks (how many, what type), storage device(s), NIC
    - [ ] Note the make and model of the motherboard (usually printed on board)
    - [ ] Find the CMOS battery — what would happen if you removed it?
    - [ ] Find the TPM chip if present (small chip near the 24-pin power connector area)
    - [ ] Photograph your findings and label them

!!! example "TASK 3.2 — BIOS Inspection"

    Boot the lab PC into BIOS/UEFI (usually Del or F2 at POST).
    
    - [ ] Is Secure Boot enabled or disabled?
    - [ ] What is the current boot order?
    - [ ] Is there a BIOS password set?
    - [ ] Note the firmware version — is it current? (Check manufacturer site)
    
    **Do not change any settings.** Document what you find.

---

## Unit Mapping

??? info "Assessment Mapping — click to expand"

    | Activity | Unit | Element |
    |----------|------|---------|
    | Hardware identification | ICTICT213 | 1.4 |
    | BIOS/UEFI inspection | ICTICT213 | 2.3 |
    | Physical security discussion | ICTICT213 | 1.4, 2.1 |
