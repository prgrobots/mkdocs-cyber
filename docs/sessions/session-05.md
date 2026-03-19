# Week 5 — Hardened OS Build

<div class="session-meta">
  <span>📅 Week 5</span>
  <span>⏱ 2 Hours</span>
  <span>🔵 Phase 1 — Reconnaissance</span>
  <span>📋 ICTICT213</span>
</div>

---

!!! danger "MISSION BRIEF"
    **Incident Reference:** RBS-2025-005  
    The compromised laptop hardware has been cleared. Now you need to rebuild it.
    But you're not just doing a default install — you're building a **hardened image**
    that Redback Systems can use as a baseline for all staff machines.
    Every decision you make needs to be justified to your manager.

---

## Learning Objectives

- [ ] Install Windows from installation media
- [ ] Explain and apply OS hardening steps during and after install
- [ ] Configure user accounts with least privilege
- [ ] Enable and verify BitLocker encryption
- [ ] Document the build decisions for handover to the client

---

## 1. OS Installation — Security Decisions

Every choice during install has a security implication. This is not just clicking Next.

### During install

| Decision | Secure Choice | Reason |
|----------|--------------|--------|
| Partition scheme | Single OS partition + separate data partition | Limits blast radius if OS is compromised |
| Account type | Local account (not Microsoft account) for first admin | No cloud sync of credentials during build |
| Privacy settings | Disable all telemetry | Limits data exfiltration surface |
| Auto-updates | Enable immediately | Patch gap is your biggest vulnerability window |

### First boot checklist

```
[ ] Windows Update — run until no updates remain
[ ] Enable BitLocker on C:\ — document recovery key
[ ] Enable Windows Defender — confirm real-time protection on
[ ] Windows Firewall — confirm enabled on all profiles
[ ] Remove bloatware — uninstall all pre-installed junk
[ ] Create standard user account for daily use
[ ] Set admin account password — strong, unique, documented in password manager
[ ] Enable audit logging — Group Policy > Audit Policy
```

---

## 2. BitLocker

BitLocker encrypts the entire drive. If the laptop is stolen, the data is unreadable without the key.

```powershell
# Check BitLocker status
Get-BitLockerVolume

# Enable BitLocker on C:\ (saves recovery key to AD if joined, or prompt for location)
Enable-BitLocker -MountPoint "C:" -EncryptionMethod XtsAes256 -UsedSpaceOnly

# Back up recovery key to file (for our lab)
(Get-BitLockerVolume -MountPoint "C:").KeyProtector | 
  Where-Object {$_.KeyProtectorType -eq 'RecoveryPassword'} |
  Select-Object RecoveryPassword | 
  Out-File C:\BitLockerKey.txt
```

!!! warning "Recovery Key Storage"
    In the real world: **never** store the recovery key on the same machine.
    Store in Active Directory, Azure AD, or a password manager.
    A laptop with BitLocker and the recovery key in a text file on the same laptop is 
    not encrypted — it's just slow to read.

---

## 3. User Accounts — Least Privilege

```powershell
# Create a standard user for daily use
New-LocalUser -Name "sarah.chen" -Description "Standard user - Sarah Chen"
Add-LocalGroupMember -Group "Users" -Member "sarah.chen"

# The admin account should NOT be used day-to-day
# Rename the default Administrator account
Rename-LocalUser -Name "Administrator" -NewName "rbsadmin"
```

Daily work happens as `sarah.chen` (standard user).  
Admin tasks require UAC elevation or switching to `rbsadmin`.  
This means malware running as Sarah can't install system-level components.

---

## 4. Documenting the Build

Part of your job is writing this up for the client. They need to know:

- What was installed
- What decisions were made and why
- How to maintain the machine going forward
- Where the BitLocker recovery key is stored

This is your first piece of client documentation for ICTSAS305.

---

## Lab Task

!!! example "TASK 5.1 — Hardened Windows Install (AT1 Practical Task 2)"

    Install Windows on the physical lab PC (your lecturer will provide installation media).
    
    **During install, document every decision you make and why.**
    
    **Post-install checklist — screenshot evidence required for each:**
    
    - [ ] Windows Update — show 0 pending updates
    - [ ] BitLocker enabled on C:\
    - [ ] Windows Defender — real-time protection on
    - [ ] Standard user account created
    - [ ] Admin account renamed
    - [ ] Firewall status — all profiles enabled
    
    **Written deliverable:** 1-page build document as if handing the machine back to a client.
    Write it for a non-technical reader. No jargon without explanation.
    
    Submit screenshots + build document to AT1 portfolio.

---

## Unit Mapping

??? info "Assessment Mapping — click to expand"

    | Activity | Unit | Element |
    |----------|------|---------|
    | OS installation | ICTICT213 | 1.4, 2.2, 2.3 |
    | Hardening decisions | ICTICT213 | 2.3, 2.4 |
    | Client build document | ICTSAS305 | 2.2, 2.9 |
