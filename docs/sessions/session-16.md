# Week 16 — Helpdesk Roleplay & Incident Tickets

<div class="session-meta">
  <span>📅 Week 16</span>
  <span>⏱ 2 Hours</span>
  <span>🟢 Phase 4 — Debrief</span>
  <span>📋 ICTSAS305</span>
</div>

---

!!! danger "MISSION BRIEF"
    **Incident Reference:** RBS-2025-016  
    The Redback Systems helpdesk is fielding calls. Three staff members have issues.
    One has a printer that won't work. One got a suspicious email. One can't log in.
    You are on helpdesk. Every call gets a ticket. Every ticket gets closed properly.
    The AI will score your communication. Your lecturer will score your tickets.

---

## Learning Objectives

- [ ] Handle a helpdesk call with a non-technical client professionally
- [ ] Ask targeted diagnostic questions without using jargon
- [ ] Log a complete support ticket with all required fields
- [ ] Escalate appropriately when a problem is outside your scope
- [ ] Give clear, step-by-step instructions to a client over the phone

---

## 1. The Helpdesk Ticket

Every interaction gets a ticket. A good ticket means the next technician can pick it up with no handover conversation.

```
Ticket #: RBS-T-[date]-[number]
Date/Time: 
Reporter: [name, department, contact]
Assigned To: 
Priority: Critical / High / Medium / Low

PROBLEM DESCRIPTION:
[What the user reported, in their words]

INVESTIGATION:
[What you checked, what you found]
[Commands run, output observed]

RESOLUTION:
[What fixed it. Step by step. Reproducible.]

STATUS: Open / In Progress / Resolved / Escalated
Escalated To: [if applicable]
Resolution Time:
```

---

## 2. Diagnostic Questions — Asking Without Jargon

Avoid: "Is the IP configured correctly on the NIC?"  
Use: "When you look at the little internet icon in the corner of the screen, does it show you're connected?"

Avoid: "Have you checked the DHCP lease?"  
Use: "Has anyone changed the network settings recently? Did it used to work on this same connection?"

The diagnostic process is the same. The language changes based on your audience.

---

## 3. Escalation Criteria

Know when to hand off:

| Situation | Action |
|-----------|--------|
| Security incident (breach, active malware) | Escalate to senior analyst immediately |
| Hardware fault requiring repair | Log ticket, escalate to hardware team |
| Account locked out — needs domain admin | Escalate to sysadmin |
| Problem outside your knowledge | Log what you've tried, escalate honestly |
| User distressed or aggressive | Remain calm, escalate to senior if needed |

Escalating is not failure. Escalating without documenting what you tried is.

---

## Lab Task

!!! example "TASK 16.1 — AI Helpdesk: Three Scenarios (AT1 Practical Task 8)"

    Complete all three helpdesk scenarios. Each one is a separate chat session.
    Screenshot your final satisfaction score for each.

    **Scenario A — Printer not working**

<iframe 
  src="../assets/helpdesk.html"
  width="100%" 
  height="600px"
  style="border:1px solid #1f2f1f;"
></iframe>

    **Scenario B — Suspicious email received**
    
    Your lecturer will provide a second helpdesk instance with a different scenario.
    
    **Scenario C — Can't log in to email**
    
    Your lecturer will provide a third helpdesk instance.
    
    **For each scenario:**
    
    - [ ] Screenshot final satisfaction score and AI feedback
    - [ ] Write up a support ticket (use the template above) based on the conversation

!!! example "TASK 16.2 — Ticket Submission (AT1 Practical Task 9)"

    Submit all three completed tickets to your AT1 portfolio folder.
    
    Each ticket must have:
    
    - [ ] All fields complete
    - [ ] Problem description in user's own words (not your interpretation)
    - [ ] Your investigation steps
    - [ ] Resolution or escalation with reason
    - [ ] Realistic timestamps

---

## Unit Mapping

??? info "Assessment Mapping — click to expand"

    | Activity | Unit | Element |
    |----------|------|---------|
    | AI helpdesk scenarios | ICTSAS305 | 1.4, 1.5, 2.1, 2.4, 2.6, 2.7, 2.8 |
    | Support ticket writing | ICTSAS305 | 1.3, 1.4, 2.2, 2.5 |
    | Escalation decisions | ICTSAS305 | 2.3, 2.4 |
