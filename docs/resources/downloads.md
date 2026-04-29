# Lab Datasets & Downloads

---

## Password Cracking Lab Files

### Redback Systems Hash Database

Two versions of the NTLM hashes from the compromised Redback Systems server.

| File | Purpose |
|------|---------|
| [redback-hashes.txt](../resources/redback-hashes.txt) | Standard NTLM hashes for cracking (Week 10 lab) |
| [redback-hashes-leet.txt](../resources/redback-hashes-leet.txt) | Leetspeak variant hashes (advanced challenge) |

**Format:** NTLM hashes (MD4)  
**Count:** 10 users per file  
**Difficulty:** rockyou.txt should crack most within seconds  

---

## Usage in Week 10 — Password Cracking

Download the appropriate hash file and follow the lab instructions:

```bash
# Download and verify
wget https://yoursite.com/resources/redback-hashes.txt

# Identify hash type
hashid redback-hashes.txt

# Dictionary attack
hashcat -m 1000 redback-hashes.txt /usr/share/wordlists/rockyou.txt

# Show results
hashcat -m 1000 redback-hashes.txt --show
```

See [Week 10 — Password Cracking Lab](../sessions/session-10.md) for full task details.
