---
theme: default
title: Week 7 — ParrotOS, Steganography & Hashing
colorSchema: dark
transition: slide-left
---

# Week 7 — ParrotOS, Steganography & Hashing

**Incident Reference:** RBS-2025-007

Data exfiltration via steganography. Files hidden inside images. Hashes prove modification.

---

# Mission Brief

Intelligence suggests a **Redback Systems insider** may be exfiltrating data by hiding it inside ordinary image files.

**The Problem:**
- Files look unchanged to the naked eye
- File size changes slightly  
- Hashes reveal the truth

**Your Role:** Learn both attack and defense

---

# Learning Objectives

- [ ] Navigate ParrotOS and key security tools
- [ ] Use steghide to embed and extract hidden data
- [ ] Generate and verify file hashes (MD5, SHA256)
- [ ] Explain why filename + size ≠ unchanged file
- [ ] Connect steganography detection to data integrity

---

# ParrotOS — Your Platform

**Debian-based Linux distribution** built for security work

Key pre-installed tools:
- `aircrack-ng` — WiFi security
- `wireshark` — Packet analysis
- `hashcat` — Password cracking
- `metasploit` — Exploitation framework
- `steghide` — Steganography
- `nmap` — Network scanning
- `set` — Social Engineering Toolkit

**Terminal is your new best friend** → everything from Week 8 onwards

---

# File Hashing — Proving Integrity

**Hash = Mathematical fingerprint of a file**

Same file → Same hash  
Change 1 byte → Hash completely different

```bash
# Generate SHA256 hash
$ sha256sum image.jpg
a3f4c8d2e1b9...  image.jpg

# Verify against known hash
$ echo "a3f4c8d2e1b9...  image.jpg" | sha256sum --check
image.jpg: OK
```

---

# Why Hashing Matters (Evidence)

When you receive evidence:
1. Immediately hash it
2. Store the hash separately
3. If questioned: prove the hash matches

This is **chain of custody** for digital evidence

---

# Steganography with `steghide`

**Steganography** = hiding data inside other data

A JPEG has enough redundant information to hide files without visible changes

```bash
# Embed a secret file inside an image
$ steghide embed -cf cover.jpg -sf secret.txt -p "password123"

# The output JPEG looks identical
# File size changes slightly ← DETECTABLE

# Extract hidden data (need password)
$ steghide extract -sf image.jpg -p "password123"

# Check if file contains hidden data
$ steghide info image.jpg
```

---

# Detection — The Hash Gives It Away

Before embedding:
```bash
$ sha256sum original.jpg
b7e2a1c4f8d3...  original.jpg
```

After embedding:
```bash
$ sha256sum modified.jpg
c6f9d5a2k1e7...  modified.jpg
```

**Same file, different hash.**  
This proves modification → evidence of exfiltration.

---

# Lab Task

**TASK 7.1 — Steganography & Hashing**

1. Generate sha256 hash of a clean image
2. Embed a text file inside it using steghide
3. Verify the hash changed
4. Extract the hidden file
5. Document the process with screenshots
6. Write a brief analysis: "How would you detect this in your SOC?"

Submit to AT1 portfolio

---

# Unit Mapping

| Activity | Unit | Element |
|----------|------|---------|
| File hashing | ICTICT213 | 1.4, 2.3 |
| Steganography tools | ICTICT213 | 2.2, 2.3 |
| Data integrity concepts | ICTSAS214 | 1.1, 1.2 |

---

# Key Takeaways

✅ **Hashes prove file integrity**  
✅ **Steganography is invisible to the eye but not to hashes**  
✅ **Compare hashes before/after = proof of modification**  
✅ **This is how insiders exfiltrate data**  
✅ **This is how you catch them**

---

# Resources

- [steghide documentation](http://steghide.sourceforge.net/documentation.php)
- [ACSC — Detecting Data Exfiltration](https://www.cyber.gov.au)
- ParrotOS terminal reference: `man steghide`
