# Redback Systems — Staff Intranet

*This is a fictional company used for training purposes.*

---

## Company Profile

**Redback Systems Pty Ltd**  
ABN: 52 123 456 789  
200 St Georges Terrace, Perth WA 6000  
+61 8 9200 0000

Redback Systems provides managed IT services and software development to mid-market clients across Western Australia. Three offices: Perth CBD (HQ), Fremantle, Joondalup.

---

## IT Team Contacts

| Role | Name | Email | Phone |
|------|------|-------|-------|
| IT Manager | James Kowalski | j.kowalski@redbacksystems.com.au | ext 201 |
| Senior Sysadmin | Priya Nair | p.nair@redbacksystems.com.au | ext 202 |
| Network Engineer | Tom Brennan | t.brennan@redbacksystems.com.au | ext 203 |
| Helpdesk (you) | — | helpdesk@redbacksystems.com.au | ext 204 |
| Security (escalate) | SOC Team | soc@redbacksystems.com.au | ext 205 |

**Helpdesk hours:** Monday–Friday 07:30–17:30  
**Out of hours incidents:** soc@redbacksystems.com.au or call 0412 000 000

---

## Escalation Matrix

| Situation | First contact | Escalate to |
|-----------|--------------|-------------|
| Standard hardware/software | Helpdesk | IT Manager if unresolved 4h |
| Network outage | Network Engineer | IT Manager immediately |
| Suspected security incident | SOC Team | IT Manager + Management |
| Data breach (confirmed) | IT Manager | CEO + Legal + ACSC (within 30 days per NDB) |
| Ransomware | Isolate immediately, call SOC | Do not pay without management approval |

---

## Incident Report Template {#incident-report-template}

Copy this template for all written incident reports.

```markdown
# Incident Report

**Reference:**    RBS-[YEAR]-[NUMBER]
**Date:**         
**Reported by:**  
**Assigned to:**  
**Priority:**     Critical / High / Medium / Low
**Status:**       Open / In Progress / Resolved / Closed

---

## Executive Summary
[2-3 sentences. What happened, business impact, current status. No jargon.]

---

## Timeline

| Time (AWST) | Event |
|-------------|-------|
| | |

---

## Technical Analysis
[Detailed technical description for IT team. Tool output, findings, evidence.]

---

## Impact Assessment
- Systems affected:
- Data potentially accessed:
- Users affected:
- Business impact:

---

## Remediation Actions Taken
[What has already been done.]

---

## Recommendations
[Prioritised. Owner assigned. Timeline.]

| # | Recommendation | Priority | Owner | Due |
|---|----------------|----------|-------|-----|
| 1 | | | | |

---

## Evidence
[List of attached files, screenshots, PCAPs, logs.]
```

---

## Support Ticket Template

```
Ticket #:     RBS-T-[YYYYMMDD]-[NUM]
Date/Time:    
Reporter:     [name / dept / contact]
Assigned To:  
Priority:     Critical / High / Medium / Low

PROBLEM:
[What the user reported — their words]

INVESTIGATION:
[Steps taken, what was found]

RESOLUTION:
[What fixed it — step by step]

STATUS:       Open / Resolved / Escalated
Escalated To: [if applicable]
Closed:       [date/time]
```

---

## Password Policy

- Minimum 14 characters
- Mixed case, numbers, and symbols required
- No dictionary words as the base
- Unique password for every system (use password manager)
- Change required if suspected compromise
- MFA mandatory for all cloud services and VPN
- Approved password manager: Bitwarden (company licence)

---

## Acceptable Use Policy (Summary)

- Company devices for work purposes. Limited personal use acceptable.
- No installation of unapproved software
- No connecting to public WiFi without VPN active
- Report suspicious emails to helpdesk — do not click, do not delete
- Lost or stolen devices: report to IT within 1 hour
- Remote wipe will be initiated for lost devices with company data
