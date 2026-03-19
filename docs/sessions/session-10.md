# Week 10 — Password Cracking Lab

<div class="session-meta">
  <span>📅 Week 10</span>
  <span>⏱ 2 Hours</span>
  <span>🔴 Phase 2 — Active Threat</span>
  <span>📋 ICTSAS214</span>
</div>

---

!!! danger "MISSION BRIEF"
    **Incident Reference:** RBS-2025-010  
    During the PCAP analysis you found a hashed password file on an exposed SMB share.
    The hashes are NTLM. Redback Systems needs to know how long it would take an attacker
    to crack their staff passwords — so they can enforce a better password policy.
    Today you find out exactly how weak most passwords are.

---

## Learning Objectives

- [ ] Explain the difference between hashing and encryption
- [ ] Identify common hash types (MD5, NTLM, SHA256, bcrypt)
- [ ] Use Hashcat to crack hashes with wordlists and rules
- [ ] Use John the Ripper as an alternative
- [ ] Write a password policy recommendation based on what you find

---

## 1. Hashing vs Encryption

| | Hashing | Encryption |
|---|---|---|
| **Reversible?** | No (one-way) | Yes (with key) |
| **Purpose** | Verify integrity / store passwords | Protect data in transit/rest |
| **Examples** | MD5, SHA256, bcrypt, NTLM | AES, RSA, TLS |

Passwords should never be stored in plaintext. They are hashed. When you log in, your input is hashed and compared to the stored hash.

**The problem:** common passwords have known hashes. A lookup table (rainbow table) or wordlist + GPU can crack weak passwords in seconds.

---

## 2. Hash Identification

```bash
# hashid — identify a hash type
hashid '$1$abc$XYZ...'   # → MD5crypt
hashid 'aad3b435b51404ee...'  # → NTLM

# hash-identifier (alternative)
hash-identifier
```

Common hash formats for Hashcat:

| Type | Hashcat Mode | Example Length |
|------|-------------|----------------|
| MD5 | 0 | 32 chars |
| NTLM | 1000 | 32 chars |
| SHA256 | 1400 | 64 chars |
| bcrypt | 3200 | 60 chars (starts with $2) |
| SHA512crypt | 1800 | starts with $6$ |

---

## 3. Hashcat

```bash
# Basic dictionary attack
hashcat -m 1000 hashes.txt /usr/share/wordlists/rockyou.txt

# With rules (mangling — adds numbers, capitalises, etc)
hashcat -m 1000 hashes.txt rockyou.txt -r /usr/share/hashcat/rules/best64.rule

# Brute force — all 6-char lowercase
hashcat -m 1000 hashes.txt -a 3 ?l?l?l?l?l?l

# Show cracked passwords
hashcat -m 1000 hashes.txt --show

# Options:
# -m  hash type
# -a  attack mode (0=dictionary, 3=brute force, 6=hybrid)
# -o  output file
# --force  ignore GPU warnings (use in VM)
```

!!! note "rockyou.txt"
    The rockyou.txt wordlist contains 14 million real passwords from a 2009 data breach.
    It's on your Parrot machine at `/usr/share/wordlists/rockyou.txt`.
    If a password is in this list, it will be cracked in under a second.

---

## 4. What This Means for Policy

After you run the lab, you'll have concrete data on how long cracking takes. Use it.

**Password policy recommendation template:**

```
Current state:    [X/10] hashes cracked in [time]
Weakest pattern:  [e.g., "word + 4 digits" cracked in < 1 min]
Recommendation:   Minimum 12 characters, mixed case, numbers, symbols
                  Prohibit dictionary words as base
                  Enforce MFA for all accounts
                  Password manager for staff
```

---

## Lab Task

!!! example "TASK 10.1 — Crack the Hashes (AT1 Practical Task 5)"

    Your lecturer will provide `redback-hashes.txt` containing NTLM hashes from 
    the "compromised" server.
    
    ```bash
    # Step 1 — identify hash type
    hashid redback-hashes.txt
    
    # Step 2 — dictionary attack
    hashcat -m 1000 redback-hashes.txt /usr/share/wordlists/rockyou.txt
    
    # Step 3 — rules attack on any remaining
    hashcat -m 1000 redback-hashes.txt rockyou.txt -r best64.rule
    
    # Step 4 — show results
    hashcat -m 1000 redback-hashes.txt --show
    ```
    
    **Document:**
    - [ ] How many hashes total
    - [ ] How many cracked (and in what time)
    - [ ] What were the cracked passwords — identify the pattern
    - [ ] One paragraph: password policy recommendation for Redback Systems

---

## Unit Mapping

??? info "Assessment Mapping — click to expand"

    | Activity | Unit | Element |
    |----------|------|---------|
    | Hash identification | ICTSAS214 | 2.1, 2.2 |
    | Password cracking | ICTSAS214 | 2.2, 2.3 |
    | Policy recommendation | ICTSAS214 | 3.1, 3.2 |
