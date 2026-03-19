#!/usr/bin/env python3
"""
generate_brief.py
─────────────────
Generates the URL for a terminal-brief.html mission page.

Usage:
    python generate_brief.py

Or import and call generate_url() from your own scripts.
"""

import base64
import json
import urllib.parse

# ── Edit your brief here ───────────────────────────────────────────────────────

SITE_BASE  = "https://yoursite.com/cyber-course"   # change to your deployed URL
BRIEF_HTML = "assets/terminal-brief.html"

SESSIONS = {
    "08": {
        "id":    "RBS-2025-008",
        "class": "TRAINING // CONTROLLED LAB",
        "lab":   "sessions/session-08/",
        "brief": [
            "## MISSION BRIEF — WEEK 8",
            "",
            "Redback Systems management has received a report that an employee's",
            "laptop may have been compromised via a rogue access point at a local café.",
            "",
            "> OBJECTIVE 1: Replicate the deauthentication attack in the isolated lab",
            "> OBJECTIVE 2: Stand up an evil twin AP and capture a client reconnect",
            "> OBJECTIVE 3: Document your findings as an incident report",
            "",
            "You are the attacker today.",
            "Next week, you write the advisory.",
            "",
            "## RULES OF ENGAGEMENT",
            "",
            "> Lab network ONLY. Dongles stay off TAFE wifi.",
            "> Document everything. If it isn't written down, it didn't happen.",
            "> SPACEBAR to skip this sequence. ENTER to proceed after.",
        ]
    },
    "09": {
        "id":    "RBS-2025-009",
        "class": "TRAINING // CONTROLLED LAB",
        "lab":   "sessions/session-09/",
        "brief": [
            "## MISSION BRIEF — WEEK 9",
            "",
            "Last week you ran the attack. This week you watch it.",
            "",
            "A packet capture from the evil twin exercise has been recovered.",
            "Your job is to analyse the traffic and identify what an attacker",
            "could have extracted from a compromised session.",
            "",
            "> OBJECTIVE 1: Install and configure Wireshark on your Parrot machine",
            "> OBJECTIVE 2: Open the provided PCAP and identify credentials in transit",
            "> OBJECTIVE 3: Write a traffic analysis report for the client",
            "",
            "## NOTE",
            "",
            "Everything you find in this PCAP is simulated training data.",
            "Capturing real network traffic without authorisation is a criminal offence.",
        ]
    },
    "10": {
        "id":    "RBS-2025-010",
        "class": "TRAINING // CONTROLLED LAB",
        "lab":   "sessions/session-10/",
        "brief": [
            "## MISSION BRIEF — WEEK 10",
            "",
            "A Redback Systems server backup has been recovered from a suspected",
            "compromised machine. The /etc/shadow file was extracted.",
            "",
            "Your task: determine whether any passwords in this file are weak",
            "enough to be cracked with commodity hardware in under an hour.",
            "",
            "> OBJECTIVE 1: Use hashcat on your Parrot machine to crack the shadow file",
            "> OBJECTIVE 2: Identify which accounts had weak passwords",
            "> OBJECTIVE 3: Draft a password policy recommendation for Redback Systems",
            "",
            "## REMINDER",
            "",
            "The shadow file provided is synthetic training data.",
            "Cracking hashes you do not have authorisation to crack is illegal.",
        ]
    },
}

# ── Generator ──────────────────────────────────────────────────────────────────

def generate_url(week_key: str, base: str = SITE_BASE) -> str:
    session = SESSIONS.get(week_key)
    if not session:
        raise ValueError(f"No session defined for week '{week_key}'")

    brief_b64 = base64.b64encode(
        json.dumps(session["brief"]).encode()
    ).decode()

    lab_url = f"{base}/{session['lab']}"

    params = urllib.parse.urlencode({
        "brief": brief_b64,
        "lab":   lab_url,
        "week":  week_key,
        "id":    session["id"],
        "class": session["class"],
    })

    return f"{base}/{BRIEF_HTML}?{params}"


def generate_markdown_link(week_key: str, base: str = SITE_BASE) -> str:
    url = generate_url(week_key, base)
    return f"[▶ OPEN MISSION BRIEF]({url}){{.md-button .md-button--primary}}"


if __name__ == "__main__":
    print("\n=== REDBACK SYSTEMS // MISSION URL GENERATOR ===\n")
    for week in SESSIONS:
        url = generate_url(week)
        print(f"Week {week}:")
        print(f"  {url[:120]}{'...' if len(url) > 120 else ''}")
        print()
    print("Tip: Copy the URL into your session .md file as an iframe or button link.")
    print("     Or use generate_markdown_link('08') to get a ready-made mkdocs button.\n")
