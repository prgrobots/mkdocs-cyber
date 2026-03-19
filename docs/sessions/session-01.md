# Week 1 — OS Fundamentals & Threat Landscape

<div class="session-meta">
  <span>📅 Week 1</span>
  <span>⏱ 2 Hours</span>
  <span>🔵 Phase 1 — Reconnaissance</span>
  <span>📋 ICTICT213</span>
</div>

---

!!! danger "MISSION BRIEF"
    **Incident Reference:** RBS-2025-001  
    You have just been onboarded at **Redback Systems** as a junior SOC analyst.
    Before you touch anything on the network, you need to understand the battlefield.
    Today is orientation: operating systems, what they do, and why attackers care about them.

---

## Learning Objectives

By the end of this session you will be able to:

- [ ] Identify the main functions of an operating system
- [ ] Compare Windows, Linux and macOS at a high level
- [ ] Explain why OS choice matters from a security perspective
- [ ] Describe the current cyber threat landscape in Australia
- [ ] Navigate Blackboard and this course site

---

## 1. What is an Operating System?

The OS is the software layer between hardware and everything else. It manages:

- **Processes** — what runs, when, and with what priority
- **Memory** — who gets RAM and how much
- **File system** — how data is stored and retrieved
- **Users & permissions** — who can do what
- **Networking** — sending and receiving data

From a security perspective, the OS is the **most critical attack surface** on any device. Compromise the OS, you own the machine.

---

## 2. The Big Three

=== "Windows"
    - Dominant in enterprise environments (~75% of desktops)
    - Most targeted OS by malware — largest attack surface
    - Active Directory, Group Policy, PowerShell — huge admin toolset
    - Most of your helpdesk work will involve Windows
    
    **Key security features:** Windows Defender, BitLocker, UAC, Windows Firewall

=== "Linux"
    - Dominates servers, networking gear, cloud infrastructure
    - Most web servers run Linux
    - ParrotOS (your attack platform) is Linux-based
    - Heavily used in security tooling — Kali, Parrot, Ubuntu
    
    **Key security features:** file permissions, sudo model, SELinux/AppArmor, iptables

=== "macOS"
    - Unix-based, shares DNA with Linux
    - Growing enterprise presence (especially creative/tech companies)
    - Historically lower malware volume — but this is changing
    
    **Key security features:** Gatekeeper, SIP (System Integrity Protection), FileVault

---

## 3. The Threat Landscape — Australia 2025

!!! warning "ACSC Key Stats"
    The Australian Cyber Security Centre (ACSC) reports a cybercrime report is made
    every **6 minutes** in Australia. Average cost of a cybercrime to a small business:
    over **$46,000**.

The most common threats Redback Systems faces:

| Threat | Description | Frequency |
|--------|-------------|-----------|
| Phishing | Fake emails to steal credentials | Very high |
| Ransomware | Encrypts files, demands payment | High |
| Business Email Compromise | Impersonates executives | High |
| Malware | Malicious software on endpoints | High |
| Credential theft | Stolen usernames/passwords | Very high |
| Rogue WiFi | Fake access points | Medium |

---

## 4. Your Tools

For this course you will use:

| Tool | Purpose | Platform |
|------|---------|----------|
| **Parrot OS** | Attack platform, security tooling | Bare metal lab PC |
| **VMware** | Isolated virtual machines | Lab PC |
| **Wireshark** | Packet capture and analysis | Both |
| **Metasploitable** | Intentionally vulnerable target VM | VMware |
| **Groq AI client** | Simulated helpdesk customer | Browser |

---

## Lab Task — Course Setup

!!! example "TASK 1.1 — Enrol and Orient"

    - [ ] Log in to Blackboard and confirm enrolment
    - [ ] Bookmark this course site
    - [ ] Find and read the [Assessment Overview](../assessments/overview.md)
    - [ ] Boot your Parrot OS machine and confirm it loads
    - [ ] Open a terminal and run `uname -a` — screenshot the output

    **No submission required this week.** This evidence goes into your AT1 portfolio.

---

## Unit Mapping

??? info "Assessment Mapping — click to expand"

    | Activity | Unit | Element |
    |----------|------|---------|
    | OS comparison | ICTICT213 | 1.1, 1.2, 1.3 |
    | Threat landscape | ICTICT213 | 1.4, 2.1 |
    | Course setup | ICTICT213 | 1.1 |

---

## Resources

- [ACSC Annual Cyber Threat Report](https://www.cyber.gov.au/about-us/reports-and-statistics/acsc-annual-cyber-threat-report)
- [Parrot OS Documentation](https://parrotsec.org/docs/)
