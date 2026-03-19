# Week 14 — Phishing Lab & Client Communication

<div class="session-meta">
  <span>📅 Week 14</span>
  <span>⏱ 2 Hours</span>
  <span>🟠 Phase 3 — Incident Response</span>
  <span>📋 ICTSAS305</span>
</div>

---

!!! danger "MISSION BRIEF"
    **Incident Reference:** RBS-2025-014  
    A Redback Systems staff member clicked a link in an email and entered their 
    Microsoft 365 credentials on what they thought was a login page.
    Two parts today: first you build the fake login page so you understand exactly 
    how this works. Then you pick up the phone to the staff member and explain 
    what happened — without making them feel stupid.

---

## Learning Objectives

- [ ] Use SET (Social Engineering Toolkit) to clone a login page
- [ ] Capture credentials on an isolated lab network
- [ ] Explain phishing techniques to a non-technical person clearly
- [ ] Handle a distressed client call professionally
- [ ] Use the AI helpdesk client to practice communication skills

---

## 1. How Phishing Works

The attack chain:

```
1. Attacker registers lookalike domain
   (e.g., micros0ft-login.com, redbacksystems-portal.net)

2. Sends email with urgent pretext
   "Your account will be suspended in 24 hours — click to verify"

3. Link goes to cloned login page (looks identical to real one)

4. Victim enters credentials → captured by attacker

5. Attacker uses credentials immediately (or sells them)

6. Victim redirected to real site — often doesn't notice
```

---

## 2. SET — Social Engineering Toolkit

```bash
# Launch SET
sudo setoolkit

# Navigate:
1) Social-Engineering Attacks
2) Website Attack Vectors  
3) Credential Harvester Attack Method
2) Site Cloner

# Enter your machine's IP (where credentials will be sent)
# Enter URL to clone: https://login.microsoftonline.com

# SET clones the page and starts a listener
# Credentials submitted go to: /root/.set/reports/
```

!!! warning "LAB NETWORK ONLY"
    Your SET listener is running on your machine's IP.
    This only works on the isolated lab network.
    Do not clone real sites and expose them to the internet.
    That is a criminal offence under the Criminal Code Act 1995 (Cth).

---

## 3. Spotting Phishing — The Other Side

Teach your clients to check:

| Check | Legitimate | Phishing |
|-------|-----------|---------|
| **URL** | login.microsoftonline.com | micros0ft-login.com |
| **HTTPS** | Padlock present | May or may not have padlock — padlock ≠ safe |
| **Sender email** | @microsoft.com | @micros0ft.com, @microsoft.support-desk.net |
| **Urgency** | Normal comms | "Act NOW or account deleted" |
| **Hover before click** | URL matches text | URL is different from display text |
| **MFA** | Prompts for second factor | Only asks for password |

**The single best defence:** MFA. Even if credentials are stolen, the attacker can't log in without the second factor.

---

## 4. AI Helpdesk — Client Communication Practice

The staff member who clicked the phishing link is scared they're in trouble. They're not technical. They need help — not a lecture.

!!! example "TASK 14.2 — AI Helpdesk: Phishing Incident Call"

    Open the helpdesk client below. You are the IT support technician.
    The client (Sarah Chen) has just reported clicking a suspicious link.
    
    **Your goals:**
    
    - Find out exactly what happened (what site, what credentials entered)
    - Advise what to do immediately (password change, which accounts affected)
    - Explain what a phishing attack is in plain English
    - Make them feel supported, not blamed
    - End the call with clear next steps
    
    **The AI will play Sarah — confused, worried, not technical.**  
    At the end it will rate your communication skills out of 5 and give specific feedback.
    
    Screenshot your final rating + comments for AT1 portfolio.

<iframe 
  src="../assets/helpdesk.html?scenario=phishing&client=Sarah+Chen&issue=clicked+suspicious+link+and+entered+Microsoft+365+password"
  width="100%" 
  height="650px"
  style="border:1px solid #1f2f1f; background:#0d0d0d;"
></iframe>

---

## Lab Task

!!! example "TASK 14.1 — Credential Harvester (AT1 Practical Task)"

    On the isolated lab network:
    
    - [ ] Launch SET and clone a login page (use a benign site — your lecturer will specify)
    - [ ] Have a classmate submit fake credentials to your page
    - [ ] Screenshot the captured credentials in SET output
    - [ ] Screenshot the cloned page in browser (showing URL is localhost/your IP)
    
    **Written task:** Write a 200-word staff awareness email from Redback Systems IT team 
    warning staff about phishing. Write it for non-technical readers. 
    No jargon. Actionable steps. Not scary.

---

## Unit Mapping

??? info "Assessment Mapping — click to expand"

    | Activity | Unit | Element |
    |----------|------|---------|
    | Phishing lab | ICTSAS214 | 1.1, 1.2, 1.3 |
    | Client communication (AI helpdesk) | ICTSAS305 | 1.4, 2.1, 2.6, 2.7, 2.8 |
    | Staff awareness email | ICTSAS305 | 2.9 |
