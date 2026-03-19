# Week 6 — Virtualisation & Isolated Environments

<div class="session-meta">
  <span>📅 Week 6</span>
  <span>⏱ 2 Hours</span>
  <span>🔵 Phase 1 — Reconnaissance</span>
  <span>📋 ICTICT213</span>
</div>

---

!!! danger "MISSION BRIEF"
    **Incident Reference:** RBS-2025-006  
    Redback Systems wants to test suspicious software before allowing it near the 
    corporate network. You need to build isolated virtual environments for safe analysis.
    Today: VMs, snapshots, and network isolation. These environments will be your 
    lab throughout the rest of the course.

---

## Learning Objectives

- [ ] Explain what virtualisation is and why it matters for security
- [ ] Create a VM in VMware
- [ ] Configure VM network settings for isolation
- [ ] Take and restore snapshots
- [ ] Install and configure Metasploitable as a target VM

---

## 1. Why Virtualisation?

A VM is a computer running inside your computer. From a security perspective:

- **Isolation** — malware in a VM (usually) can't affect the host
- **Snapshots** — break something, roll back instantly
- **Lab environments** — run intentionally vulnerable systems safely
- **Malware analysis** — detonate malware in a sandbox and watch what it does
- **Multiple OS** — run Linux tools on a Windows host

---

## 2. VMware Network Modes

This is critical for our labs. Get this wrong and your attack traffic hits the real network.

| Mode | What it does | Use when |
|------|-------------|----------|
| **Bridged** | VM gets IP on real network | You need internet in VM |
| **NAT** | VM shares host's IP | General VM use |
| **Host-only** | VM talks only to host | Safe isolated analysis |
| **Custom (VMnet)** | VMs on isolated private segment | Multi-VM lab environments |

!!! danger "USE HOST-ONLY OR CUSTOM FOR ALL LAB WORK"
    Never run attack tools in a VM set to Bridged mode.
    You will be running traffic on the real TAFE network.
    This will get you noticed. Not the good kind of noticed.

---

## 3. Snapshots

Before you do anything risky in a VM: **take a snapshot.**

- VMware: VM menu → Snapshot → Take Snapshot
- Name it clearly: `clean-install-pre-lab` not `snapshot1`
- After the lab: you can revert to clean state in seconds

```
Snapshot workflow:
1. Fresh VM installed and configured
2. SNAPSHOT: "baseline-clean"
3. Run lab / do the thing
4. SNAPSHOT: "post-lab-8" (keep evidence)
5. Revert to "baseline-clean" for next time
```

---

## 4. Metasploitable

Metasploitable is a Linux VM deliberately full of vulnerabilities. It is your target for exploitation labs in Weeks 11-12. **It must never have internet access.**

Download: your lecturer will provide the VM image.

```
Metasploitable setup:
1. Import OVA into VMware
2. Network: Host-only ONLY
3. Take snapshot: "baseline-metasploitable"
4. Do not install updates (updates fix the vulnerabilities)
5. Note the IP address: login as msfadmin/msfadmin, run: ip addr
```

---

## Lab Task

!!! example "TASK 6.1 — VM Creation (AT1 Practical Task 3)"

    Create two VMs:
    
    **VM 1: Windows 10/11 (analysis sandbox)**
    
    - [ ] Install Windows in VMware
    - [ ] Network: NAT (for updates), then switch to Host-only after updates
    - [ ] Take snapshot: "baseline-windows-sandbox"
    - [ ] Screenshot: VM settings showing network adapter
    
    **VM 2: Metasploitable (target)**
    
    - [ ] Import provided Metasploitable OVA
    - [ ] Network: Host-only ONLY
    - [ ] Boot and confirm IP address
    - [ ] Take snapshot: "baseline-metasploitable"
    - [ ] Screenshot: IP address showing, network mode showing Host-only
    
    Submit screenshots to AT1 portfolio.

---

## Unit Mapping

??? info "Assessment Mapping — click to expand"

    | Activity | Unit | Element |
    |----------|------|---------|
    | VM creation | ICTICT213 | 2.2, 2.3, 2.4 |
    | Network isolation | ICTICT213 | 2.2, 2.3 |
    | Snapshot management | ICTICT213 | 2.4 |
