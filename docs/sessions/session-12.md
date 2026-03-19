# Week 12 — IDS with Snort

<div class="session-meta">
  <span>📅 Week 12</span>
  <span>⏱ 2 Hours</span>
  <span>🟠 Phase 3 — Incident Response</span>
  <span>📋 ICTSAS214 · ICTSAS305</span>
</div>

---

!!! danger "MISSION BRIEF"
    **Incident Reference:** RBS-2025-012  
    You've spent the last four weeks being the attacker. Now you're on defence.
    Redback Systems is deploying an IDS on their network and you need to configure it.
    Today: Snort, rules, and watching your own previous attacks trigger alerts.

---

## Learning Objectives

- [ ] Explain what an IDS is and the difference between IDS and IPS
- [ ] Install and configure Snort in detection mode
- [ ] Write basic Snort rules
- [ ] Generate traffic that triggers alerts
- [ ] Read and interpret Snort alert output

---

## 1. IDS vs IPS

| | IDS | IPS |
|---|---|---|
| **Full name** | Intrusion Detection System | Intrusion Prevention System |
| **Action** | Alerts — passive | Blocks — active |
| **Placement** | Monitors a copy of traffic | Inline — traffic passes through it |
| **Risk** | False negatives missed | False positives block legit traffic |
| **Use case** | Monitoring, forensics | Active defence |

Snort can operate as either. Today: IDS mode — watch and alert, don't block.

---

## 2. Snort Installation

```bash
# Install Snort
sudo apt update
sudo apt install snort -y

# During install: enter your network range
# e.g., 192.168.56.0/24 for our lab network

# Verify installation
snort --version

# Test config
sudo snort -T -c /etc/snort/snort.conf
```

---

## 3. Snort Rule Syntax

```
action  protocol  src_ip  src_port  direction  dst_ip  dst_port  (options)

alert   tcp       any     any       ->         any     80        (msg:"HTTP traffic detected"; sid:1000001;)
```

| Field | Meaning |
|-------|---------|
| `action` | alert / log / drop / reject |
| `protocol` | tcp / udp / icmp / ip |
| `src_ip` | source IP or `any` |
| `src_port` | source port or `any` |
| `->` | direction (or `<>` for bidirectional) |
| `dst_ip` | destination IP or `any` |
| `dst_port` | destination port or `any` |
| `msg` | alert message text |
| `sid` | unique rule ID (your custom rules: 1000000+) |

### Practical rules

```bash
# Detect nmap ping sweep
alert icmp any any -> $HOME_NET any (msg:"ICMP Ping Sweep"; itype:8; sid:1000001;)

# Detect nmap SYN scan
alert tcp any any -> $HOME_NET any (flags:S; msg:"SYN Scan Detected"; threshold:type both,track by_src,count 20,seconds 5; sid:1000002;)

# Detect FTP login attempts
alert tcp any any -> $HOME_NET 21 (msg:"FTP Login Attempt"; content:"USER"; sid:1000003;)

# Detect vsftpd backdoor trigger (the smiley face)
alert tcp any any -> $HOME_NET 21 (msg:"vsftpd Backdoor Trigger"; content:":)"; sid:1000004;)
```

---

## 4. Running Snort

```bash
# Run in alert mode, watching interface
sudo snort -A console -i eth0 -c /etc/snort/snort.conf

# Run against a PCAP file (replay mode)
sudo snort -A console -r capture.pcap -c /etc/snort/snort.conf

# Alerts saved to:
/var/log/snort/alert
```

---

## Lab Task

!!! example "TASK 12.1 — Write and Test IDS Rules"

    **Part A — Configure Snort:**
    
    - [ ] Add your custom rules to `/etc/snort/rules/local.rules`
    - [ ] Add the 4 example rules above
    - [ ] Test config: `sudo snort -T -c /etc/snort/snort.conf`
    
    **Part B — Trigger your own alerts:**
    
    From your Parrot machine, run nmap against Metasploitable:
    
    ```bash
    nmap -sS [metasploitable-ip]   # SYN scan
    ping -c 5 [metasploitable-ip]  # ICMP
    ```
    
    - [ ] Screenshot Snort alert output as the scans run
    - [ ] How many alerts fired? What triggered each one?
    
    **Part C — Replay last week's PCAP through Snort:**
    
    ```bash
    sudo snort -A console -r week11-scan.pcap -c /etc/snort/snort.conf
    ```
    
    - [ ] What alerts fired on last week's exploitation traffic?
    - [ ] Write one NEW rule that would detect the vsftpd exploit specifically
    
    Submit rule file + screenshots + written answers to AT1 portfolio.

---

## Unit Mapping

??? info "Assessment Mapping — click to expand"

    | Activity | Unit | Element |
    |----------|------|---------|
    | Snort installation and config | ICTSAS214 | 3.1, 3.2 |
    | Rule writing | ICTSAS214 | 3.1, 3.2 |
    | Alert analysis | ICTSAS305 | 1.1, 1.2, 1.3 |
