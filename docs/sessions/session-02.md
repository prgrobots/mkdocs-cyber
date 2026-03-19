# Week 2 — OS Deep Dive

<div class="session-meta">
  <span>📅 Week 2</span>
  <span>⏱ 2 Hours</span>
  <span>🔵 Phase 1 — Reconnaissance</span>
  <span>📋 ICTICT213</span>
</div>

---

!!! danger "MISSION BRIEF"
    **Incident Reference:** RBS-2025-002  
    A Redback Systems staff member reports their machine is "acting weird" — slow, 
    unexpected popups, unknown processes running. Before you can diagnose anything,
    you need to understand what *normal* looks like. Today you go deeper into OS 
    internals: processes, file systems, users, and permissions.

---

## Learning Objectives

- [ ] Navigate the Windows and Linux file systems
- [ ] Explain file permissions in both Windows and Linux
- [ ] Identify running processes and what they tell you
- [ ] Describe user account types and why they matter for security
- [ ] Use basic command line tools on both platforms

---

## 1. File Systems

=== "Windows (NTFS)"
    ```
    C:\
    ├── Windows\        ← OS files — don't touch
    ├── Program Files\  ← installed applications
    ├── Users\          ← user profiles and data
    │   └── sarah\
    │       ├── Desktop\
    │       ├── Documents\
    │       └── AppData\  ← hidden — often where malware hides
    └── Temp\           ← temporary files — frequent malware staging ground
    ```
    
    **Security relevance:** Malware commonly hides in `AppData\Roaming`, `AppData\Local\Temp`, 
    and `C:\Windows\Temp`. Know these paths.

=== "Linux (ext4)"
    ```
    /
    ├── etc/        ← system config files
    ├── home/       ← user home directories
    ├── var/        ← logs, databases, mail
    │   └── log/    ← check here first in an incident
    ├── tmp/        ← temporary — world-writable, malware staging
    ├── bin/        ← essential binaries
    └── proc/       ← virtual filesystem — running processes as files
    ```
    
    **Security relevance:** `/tmp` is world-writable and often used to stage attacks.
    `/var/log` is your first stop in any investigation.

---

## 2. Permissions

### Linux permissions

```bash
# View permissions
ls -la /home/sarah/

# Output example:
-rwxr-xr-- 1 sarah staff 4096 Mar 10 09:22 report.pdf
```

Breaking down `-rwxr-xr--`:

| Position | Meaning |
|----------|---------|
| `-` | file type (- = file, d = directory) |
| `rwx` | owner: read, write, execute |
| `r-x` | group: read, no write, execute |
| `r--` | others: read only |

```bash
# Change permissions
chmod 750 script.sh     # owner=rwx, group=rx, others=none
chown sarah:staff file  # change owner
```

### Windows permissions

Managed via ACLs (Access Control Lists). Right-click → Properties → Security tab.

Key permission levels: Full Control, Modify, Read & Execute, Read, Write.

---

## 3. Processes

### Windows

```powershell
# List all processes
Get-Process

# Find a specific process
Get-Process | Where-Object {$_.Name -like "*chrome*"}

# Kill a process
Stop-Process -Name "malware.exe" -Force
```

Task Manager (Ctrl+Shift+Esc) → Details tab shows PID, CPU, memory, file path.

### Linux

```bash
# List processes
ps aux

# Live process viewer
top
htop   # nicer version

# Find a process by name
pgrep -l firefox

# Kill a process
kill -9 <PID>
```

!!! warning "SUSPICIOUS PROCESSES"
    In an investigation, look for processes with:
    
    - Random or misspelled names (`svch0st.exe`, `svchost32.exe`)
    - Running from unusual paths (`C:\Users\Public\`, `/tmp/`)
    - High CPU/memory with no obvious function
    - No parent process (orphaned)

---

## 4. User Accounts

### Principle of Least Privilege

**The single most important access control concept.** Every user and process should have only the minimum permissions needed to do their job. Nothing more.

Why it matters: if a standard user account gets compromised, the attacker is limited. If an admin account gets compromised, it's game over.

| Account Type | Windows | Linux | Risk Level |
|---|---|---|---|
| Standard user | User | Regular user | Low |
| Local admin | Administrator | sudo user | High |
| Domain admin | Domain Admin | root | Critical |
| Service account | SYSTEM/Network Service | www-data, nobody | Medium-High |

---

## Lab Task

!!! example "TASK 2.1 — OS Navigation"

    **On your Parrot OS machine:**
    
    ```bash
    # 1. List the contents of /var/log with permissions
    ls -la /var/log/
    
    # 2. Find your own user's home directory
    echo $HOME
    ls -la ~/
    
    # 3. Check who is logged in
    who
    whoami
    id
    
    # 4. View running processes and find the top 5 by CPU
    ps aux --sort=-%cpu | head -6
    
    # 5. Check what sudo access you have
    sudo -l
    ```
    
    Screenshot each command and its output for your AT1 portfolio.

!!! example "TASK 2.2 — Investigate the 'suspicious' machine"

    Your lecturer will demonstrate a Windows VM with a simulated suspicious process running.
    
    Using Task Manager and PowerShell:
    
    - [ ] Identify the suspicious process (name, PID, file path)
    - [ ] Document your findings as a brief investigation note
    - [ ] Recommend whether to kill the process and why

---

## Unit Mapping

??? info "Assessment Mapping — click to expand"

    | Activity | Unit | Element |
    |----------|------|---------|
    | File system navigation | ICTICT213 | 1.4 |
    | Permissions | ICTICT213 | 1.4, 2.1 |
    | Process investigation | ICTICT213 | 1.4, 2.3 |

---

## Resources

- [Linux File System Hierarchy Standard](https://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html)
- [Windows Sysinternals Process Explorer](https://learn.microsoft.com/en-us/sysinternals/downloads/process-explorer)
