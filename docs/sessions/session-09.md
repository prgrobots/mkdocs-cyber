# Week 9 — Wireshark & Traffic Analysis

<div class="session-meta">
  <span>📅 Week 9</span>
  <span>⏱ 2 Hours</span>
  <span>🔴 Phase 2 — Active Threat</span>
  <span>📋 ICTSAS214</span>
</div>

---

!!! danger "MISSION BRIEF"
    **Incident Reference:** RBS-2025-009  
    Last week you ran the evil twin attack. This week you watch it happen in the wire.
    A staff member reports their credentials "might have been captured" at a café.
    You have a PCAP from the Redback Systems network from that morning.
    Find the evidence.

---

## Learning Objectives

- [ ] Capture live traffic with Wireshark on the lab network
- [ ] Apply display filters to isolate traffic of interest
- [ ] Identify cleartext credentials in HTTP traffic
- [ ] Reconstruct a TCP stream
- [ ] Explain what an attacker sees vs what a defender sees in the same capture

---

## 1. Wireshark Basics

Wireshark captures every packet your network interface sees. In monitor mode (on WiFi), that means every packet in range.

```
Start capture:   Interface → select wlan0 or eth0 → Start
Stop capture:    Red square button
Save capture:    File → Save As → .pcap or .pcapng
Open a PCAP:     File → Open
```

### The display

| Pane | Shows |
|------|-------|
| Top | Packet list — one row per packet |
| Middle | Protocol breakdown — expand to see fields |
| Bottom | Raw bytes — hex on left, ASCII on right |

---

## 2. Display Filters

Wireshark captures everything. Filters show you only what matters.

```
# Filter by protocol
http
dns
tcp
arp

# Filter by IP
ip.addr == 192.168.1.105
ip.src == 10.0.0.1
ip.dst == 10.0.0.2

# Filter by port
tcp.port == 80
tcp.port == 443

# Filter by content (slow on large captures)
http contains "password"
frame contains "login"

# Combine filters
http and ip.src == 192.168.1.105
tcp.port == 80 or tcp.port == 8080

# Show only DNS queries
dns.flags.response == 0
```

---

## 3. Following a Stream

A single conversation spans many packets. Right-click any packet → Follow → TCP Stream.

This reassembles the conversation into readable text. For unencrypted HTTP, you see everything — including form submissions with usernames and passwords.

```
Example of what you see in a HTTP POST login:
----------------------------------------------
POST /login HTTP/1.1
Host: intranet.redbacksystems.com
Content-Type: application/x-www-form-urlencoded

username=sarah.chen&password=Welcome2024!
----------------------------------------------
```

!!! warning "THIS IS WHY HTTPS MATTERS"
    The above is completely readable to anyone on the network.
    HTTPS encrypts this. On a plaintext HTTP site, your credentials 
    are visible to anyone with Wireshark and a network connection.

---

## 4. ARP Poisoning — What it Looks Like

ARP (Address Resolution Protocol) maps IP addresses to MAC addresses. It has no authentication — anyone can send a fake ARP reply.

```
# Legitimate ARP:
10.0.0.1 is at AA:BB:CC:DD:EE:FF

# ARP Poisoning — attacker says:
10.0.0.1 is at 11:22:33:44:55:66   ← attacker's MAC

# Now traffic meant for the router goes to the attacker instead
# Filter to spot this:
arp
```

Look for: duplicate ARP replies for the same IP, MAC address that wasn't previously associated with that IP.

---

## Lab Task

!!! example "TASK 9.1 — Live Capture"
    
    On the lab network (isolated, not TAFE wifi):
    
    ```bash
    # Start Wireshark on your interface
    # Browse to the lab HTTP site your lecturer sets up
    # Submit a test login form
    # Stop capture
    ```
    
    - [ ] Apply filter `http.request.method == "POST"` — find your login
    - [ ] Follow the TCP stream — screenshot the credentials in plaintext
    - [ ] Apply filter `dns` — what domains did your browser query?
    - [ ] Save the PCAP as `week9-capture-[yourname].pcap`

!!! example "TASK 9.2 — PCAP Investigation"

    Your lecturer will provide `redback-incident-sept.pcap` — a capture from the 
    morning of the café incident.
    
    **Your investigation questions:**
    
    - [ ] What devices are communicating? (Statistics → Endpoints)
    - [ ] Is there any HTTP traffic? What was submitted?
    - [ ] Are there any DNS queries to suspicious domains?
    - [ ] Can you identify the moment credentials were captured?
    
    Write a 1-paragraph incident summary: what happened, when, what was captured.
    This goes into your AT1 portfolio as investigation evidence.

---

## Unit Mapping

??? info "Assessment Mapping — click to expand"

    | Activity | Unit | Element |
    |----------|------|---------|
    | Live packet capture | ICTSAS214 | 1.1, 1.2, 1.3 |
    | PCAP analysis | ICTSAS214 | 1.4, 1.5 |
    | Incident summary | ICTSAS214 | 2.1, 2.2 |

---

## Resources

- [Wireshark Display Filter Reference](https://www.wireshark.org/docs/dfref/)
- [Wireshark Sample Captures](https://wiki.wireshark.org/SampleCaptures)
