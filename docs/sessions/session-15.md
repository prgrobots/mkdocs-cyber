# Week 15 — Client Documentation

<div class="session-meta">
  <span>📅 Week 15</span>
  <span>⏱ 2 Hours</span>
  <span>🟠 Phase 3 — Incident Response</span>
  <span>📋 ICTSAS305</span>
</div>

---

!!! danger "MISSION BRIEF"
    **Incident Reference:** RBS-2025-015  
    The Redback Systems incident is being written up for the board.
    You've run the investigations, cracked the passwords, traced the packets.
    Now you have to communicate all of it — to technical and non-technical audiences.
    Documentation is half the job. Bad documentation makes the technical work meaningless.

---

## Learning Objectives

- [ ] Produce a complete incident report with technical and executive sections
- [ ] Write client-facing support documentation in plain English
- [ ] Create a how-to guide a non-technical user can actually follow
- [ ] Use the correct structure for helpdesk tickets and change requests

---

## 1. Document Types You Will Write

| Document | Audience | Tone |
|----------|----------|------|
| **Incident Report** | IT team + management | Technical detail + executive summary |
| **Support ticket** | Internal IT record | Factual, concise, timestamped |
| **User guide / how-to** | End users | Plain English, step-by-step, no jargon |
| **Change request** | Management approval | Business justification + risk + rollback plan |
| **Advisory email** | All staff | Brief, actionable, not alarming |

---

## 2. Incident Report Structure

```markdown
# Incident Report — RBS-2025-[ref]

## Executive Summary
[2-3 sentences. What happened, when, what was the impact. No jargon.]

## Timeline
| Time | Event |
|------|-------|
| 09:14 | Attacker initiates scan from 192.168.1.88 |
| 09:17 | vsftpd exploit triggered |
| 09:19 | Root shell established |

## Technical Analysis
[Detail for IT team. What was found, how, tool output.]

## Impact Assessment
[What systems/data/users were affected.]

## Remediation
[What was done. What still needs to be done.]

## Recommendations
[How to prevent recurrence. Prioritised. Costed if possible.]
```

---

## 3. Writing for Non-Technical Readers

Rules:

- Replace every acronym with the full term on first use
- No tool names unless you explain what they are
- Use analogies: "the firewall is like a security guard checking IDs at the door"
- Active voice: "the attacker accessed the server" not "the server was accessed"
- Concrete impact: "could have accessed customer payment data" not "data exposure risk"
- End every document with clear next steps with owners and dates

---

## Lab Task

!!! example "TASK 15.1 — Complete Incident Report (AT1 Practical Task 7)"

    Using your findings from Weeks 9-13, write a complete incident report for 
    the Redback Systems breach.
    
    **Required sections:**
    
    - [ ] Executive summary (max 150 words, no jargon)
    - [ ] Timeline table (at least 6 timestamped events)
    - [ ] Technical analysis (your Wireshark and Metasploit findings)
    - [ ] Impact assessment (what could the attacker have accessed?)
    - [ ] 5 prioritised remediation recommendations

!!! example "TASK 15.2 — Staff How-To Guide"

    Write a 1-page guide for Redback Systems staff: 
    **"How to identify and report a phishing email"**
    
    Requirements:
    
    - [ ] Written for someone with no IT knowledge
    - [ ] 5-7 concrete steps with examples
    - [ ] What to do if you already clicked (no blame, just steps)
    - [ ] Contact details section (use fictional IT team contacts)
    - [ ] Could be printed and put on a noticeboard

---

## Unit Mapping

??? info "Assessment Mapping — click to expand"

    | Activity | Unit | Element |
    |----------|------|---------|
    | Incident report | ICTSAS305 | 1.3, 1.4, 2.2, 2.3 |
    | Executive summary | ICTSAS305 | 1.4, 2.8 |
    | Staff how-to guide | ICTSAS305 | 2.9 |
    | Plain English writing | ICTSAS305 | 2.8, 2.9 |
