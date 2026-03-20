# Week 7 — ParrotOS, Steganography & Hashing

<div class="session-meta">
  <span>📅 Week 7</span>
  <span>⏱ 2 Hours</span>
  <span>🔵 Phase 1 — Reconnaissance</span>
  <span>📋 ICTICT213 · ICTSAS214</span>
</div>

---

!!! danger "MISSION BRIEF"
    **Incident Reference:** RBS-2025-007  
    Intelligence suggests a Redback Systems insider may be exfiltrating data by
    hiding it inside ordinary image files — a technique called steganography.
    The files look unchanged. The hashes say otherwise.
    Today you learn both sides: how to hide data, and how to prove a file has been modified.

[📊 View Slides](../../slides/){.md-button .md-button--primary}

---

## Learning Objectives

- [ ] Navigate ParrotOS and key security tools
- [ ] Use steghide to embed and extract hidden data
- [ ] Generate and verify file hashes (MD5, SHA256)
- [ ] Explain why a matching filename and size does not mean an unchanged file
- [ ] Connect steganography detection to data integrity concepts

---

## 1. ParrotOS — Your Platform

Parrot Security OS is a Debian-based Linux distribution built for security work.

```bash
# Key tools already installed:
aircrack-ng    # WiFi security (Week 8)
wireshark      # Packet analysis (Week 9)
hashcat        # Password cracking (Week 10)
metasploit     # Exploitation framework (Week 11)
steghide       # Steganography
nmap           # Network scanning
set            # Social Engineering Toolkit (Week 14)
```

Get comfortable with the terminal now. Everything from Week 8 onwards happens here.

---

## 2. File Hashing — Proving Integrity

A hash is a mathematical fingerprint of a file. The same file always produces the same hash. Change one byte, the hash completely changes.

```bash
# Generate SHA256 hash of a file
sha256sum image.jpg

# Output:
# a3f4c8d2e1b9... image.jpg

# MD5 (faster, weaker — don't use for security, fine for integrity checks)
md5sum image.jpg

# Verify a file against a known hash
echo "a3f4c8d2e1b9...  image.jpg" | sha256sum --check
```

### Why this matters

When you receive evidence, you hash it immediately. If anyone questions whether you modified it, you can prove the hash matches. This is chain of custody for digital evidence.

---

## 3. Steganography with steghide

Steganography = hiding data inside other data. A JPEG file has enough redundant information to hide a text file without visibly changing the image.

```bash
# Embed a secret file inside an image
steghide embed -cf cover_image.jpg -sf secret.txt -p "password123"

# The output image.jpg looks identical to the original
# File size changes slightly — this is detectable

# Extract hidden data
steghide extract -sf image.jpg -p "password123"

# Check if a file contains hidden data (without password)
steghide info image.jpg
```

### The detection problem

```bash
# Before embedding:
sha256sum original.jpg
# b7e2a1c4f8d3...  original.jpg

# After embedding:
sha256sum modified.jpg  
# 9f3c7a2e1b4d...  modified.jpg   ← DIFFERENT HASH

# File size:
ls -la original.jpg modified.jpg
# -rw-r--r-- 1 user user 148392 original.jpg
# -rw-r--r-- 1 user user 152847 modified.jpg  ← slightly larger
```

The file looks the same. The filename is the same. But the hash never lies.

!!! note "CONNECTING TO THE MORNING CLASS"
    This is exactly what BSBXCS303 covers — data integrity, detecting unauthorised 
    modification, and protecting information. The hash IS the integrity check.
    A file that has been steganographically modified has failed its integrity check.

---

## 4. Detection Techniques

```bash
# stegdetect — statistical analysis for hidden content
stegdetect -t jopi image.jpg

# binwalk — look for embedded files of any type
binwalk image.jpg

# exiftool — check metadata anomalies
exiftool image.jpg
```

---

## Lab Task

!!! example "TASK 7.1 — Steganography Lab"

    **Part A — Hide data:**
    
    ```bash
    # 1. Create a secret message
    echo "Redback Systems Confidential: Q3 Revenue = $4.2M" > secret.txt
    
    # 2. Get a cover image (any JPEG)
    # Ask your lecturer for the lab image pack
    
    # 3. Embed the secret
    steghide embed -cf cover.jpg -sf secret.txt -p "redback2025"
    
    # 4. Hash BOTH files and record the hashes
    sha256sum cover.jpg
    sha256sum cover.jpg  # after embedding — rename first
    ```
    
    **Part B — Detect and extract:**
    
    Your lecturer will give you a folder of images. Some contain hidden data, some don't.
    
    - [ ] Hash all images and record hashes
    - [ ] Use steghide info to probe each file
    - [ ] For any that contain data: extract it
    - [ ] Document which files were modified and how you know
    
    **Part C — Write up:**
    
    Brief paragraph: "How would Redback Systems detect an insider using steganography 
    to exfiltrate data?" Max 150 words. Plain English.
    
    Submit all hash records + written paragraph to AT1 portfolio.

---

## Unit Mapping

??? info "Assessment Mapping — click to expand"

    | Activity | Unit | Element |
    |----------|------|---------|
    | File hashing | ICTICT213 | 1.4, 2.3 |
    | Steganography tools | ICTICT213 | 2.2, 2.3 |
    | Data integrity concepts | ICTSAS214 | 1.1, 1.2 |

---

## Resources

- [steghide documentation](http://steghide.sourceforge.net/documentation.php)
- [ACSC — Detecting Data Exfiltration](https://www.cyber.gov.au)
