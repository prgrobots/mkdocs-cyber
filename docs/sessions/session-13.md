# Week 13 — SOC Exercise: PCAP Replay

<div class="session-meta">
  <span>📅 Week 13</span>
  <span>⏱ 2 Hours</span>
  <span>🟠 Phase 3 — Incident Response</span>
  <span>📋 ICTSAS305</span>
</div>

---

!!! danger "MISSION BRIEF"
    **Incident Reference:** RBS-2025-013  
    Redback Systems was attacked three months ago. The SOC captured everything.
    The PCAP file has been sitting in an evidence locker since.
    Today you open the case. You're given the raw capture and nothing else.
    No hints. No answers. Work out what happened.

---

## Learning Objectives

- [ ] Approach an unknown PCAP systematically
- [ ] Use Wireshark statistics to get an overview of a capture
- [ ] Identify the attack type from traffic patterns
- [ ] Reconstruct the attacker's actions step by step
- [ ] Write a post-incident report from raw evidence

---

## 1. PCAP Triage — Start Here

When you open an unknown PCAP, resist the urge to start filtering immediately. Get the overview first.

```
Statistics → Capture File Properties    ← how long, how many packets
Statistics → Protocol Hierarchy         ← what protocols, what proportion
Statistics → Conversations              ← who talked to who, how much
Statistics → Endpoints                  ← all IPs, ports in capture
Statistics → IO Graph                   ← traffic volume over time (spikes = events)
```

The IO graph is your timeline. Spikes in traffic correspond to events. Flat then sudden spike = something happened at that moment.

---

## 2. Systematic Investigation

Work through this checklist on any unknown capture:

```
[ ] 1. What is the time range of the capture?
[ ] 2. How many unique IPs? Which ones communicated most?
[ ] 3. What protocols are present? Any unusual ones?
[ ] 4. Is there any DNS traffic? What domains were queried?
[ ] 5. Is there any HTTP? What was requested?
[ ] 6. Are there port scan patterns? (many ports, same source)
[ ] 7. Are there large data transfers? (exfiltration?)
[ ] 8. Are there any cleartext credentials?
[ ] 9. Is there any known malicious traffic (C2 patterns, exploit traffic)?
[ ] 10. What is the timeline of events?
```

---

## 3. Useful Filters for Investigation

```
# Find all DNS queries
dns.flags.response == 0

# Find HTTP POST (form submissions, logins)
http.request.method == "POST"

# Find large transfers (potential exfiltration)
tcp.len > 1000

# Find failed connections (scanning/probing)
tcp.flags.reset == 1

# Find unusual ports
not (tcp.port == 80 or tcp.port == 443 or tcp.port == 53)

# Find traffic to/from a specific IP
ip.addr == [suspicious IP]

# Reconstruct what files were transferred via HTTP
File → Export Objects → HTTP
```

---

## 4. Writing the Post-Incident Report

Your report needs to answer five questions:

1. **What happened?** (Plain English, one paragraph)
2. **When?** (Timeline of key events with timestamps)
3. **How?** (Technical explanation of the attack method)
4. **What was affected?** (Systems, data, accounts)
5. **What should happen now?** (Remediation steps)

Two versions: one technical (for IT team), one plain English (for management).

---

## Lab Task

!!! example "TASK 13.1 — Boss of the SOC (AT1 Practical Task 9)"

    Your lecturer will provide `redback-incident-bots.pcap` — a real-world style 
    capture of a complete attack chain.
    
    **You have 90 minutes. Work independently or in pairs.**
    
    Questions to answer:
    
    - [ ] What was the attacker's IP address?
    - [ ] What was the target IP address?
    - [ ] What reconnaissance did the attacker perform?
    - [ ] What vulnerability did they exploit?
    - [ ] Did they achieve a shell or access? Evidence?
    - [ ] Was any data exfiltrated? What?
    - [ ] What was the complete timeline (with timestamps)?
    
    **Deliverable:** Written incident report, two versions:
    
    - Technical version (for IT team) — 300-500 words + timeline table
    - Executive summary (for management) — max 150 words, no jargon
    
    **At the end of the session:** each pair presents their findings to the class.
    Your lecturer will reveal the full answer — compare your investigation with the ground truth.
    
    Submit both versions to AT1 portfolio.

---

## Unit Mapping

??? info "Assessment Mapping — click to expand"

    | Activity | Unit | Element |
    |----------|------|---------|
    | PCAP investigation | ICTSAS305 | 1.1, 1.2, 1.3 |
    | Incident report (technical) | ICTSAS305 | 1.3, 1.4, 2.2, 2.3 |
    | Executive summary | ICTSAS305 | 1.4, 2.8 |
    | Class presentation | ICTSAS305 | 1.4, 2.6 |

---

## Resources

- [Wireshark Statistics Menu Guide](https://www.wireshark.org/docs/wsug_html_chunked/ChStatistics.html)
- [Malware Traffic Analysis — sample PCAPs](https://www.malware-traffic-analysis.net/)
