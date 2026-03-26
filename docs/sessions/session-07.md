# Week 7 — Steganography, Hashing & Malware Scanning

<div class="session-meta">
  <span>📅 Week 7</span>
  <span>⏱ 2 Hours</span>
  <span>🔵 Lab — Parrot OS (bare metal)</span>
  <span>📋 ICTSAS214</span>
</div>

---

!!! danger "MISSION BRIEF"
    **Incident Reference:** RBS-2025-007  
    A Redback Systems staff member received an image file via email from an unknown
    sender. It looks like a normal photo. Your job: prove whether the file has been
    tampered with, scan it for malware, and find out whether your antivirus would
    even catch something hidden inside it.

[📊 View Slides](/mkdocs-cyber/slides/week-07/){.md-button .md-button--primary}

---

## Today's Plan

1. **Dongles in** — install ClamAV + test files, run freshclam (~10 min)
2. **Dongles out** — air-gapped for the rest
3. Steganography hands-on — hide a file, prove it changed the hash
4. ClamAV baseline scan
5. EICAR — scan the test file that came with the install
6. Hide EICAR inside an image — does ClamAV catch it?
7. VirusTotal demo — name vs hash

---

## Part 1 — ClamAV Install & Update (dongles in)

Plug in your dongle. About 10 minutes for this part.

```bash
# Install ClamAV and the test files package
sudo apt update && sudo apt install clamav clamav-daemon clamav-testfiles -y

# Update virus definitions
sudo freshclam

# When done you'll see: main.cvd is up to date
```

!!! note "clamav-testfiles"
    This package installs test files to `/usr/share/clamav-testfiles/` — including
    EICAR. You didn't have to create it. It came with the install. We'll use it shortly.

**Dongles out once freshclam completes.**

---

## Part 2 — Steganography & Hashing

Last week you saw how to hide data inside an image. Today you prove mathematically
that the file was modified — even though it looks identical.

```bash
# Hash your original image
sha256sum original.jpg

# Embed a secret file inside it
steghide embed -cf original.jpg -sf secret.txt -p "redback2025"

# Hash it again
sha256sum original.jpg
```

The hashes are completely different. The image looks the same. The hash doesn't lie.

```bash
# This works for any file change — even one byte
echo "original" > test.txt && sha256sum test.txt
echo "changed"  >> test.txt && sha256sum test.txt
# Completely different hash from one added word
```

!!! note "Why hashing matters"
    This is how digital forensics maintains chain of custody. Hash the evidence
    when you collect it. If anyone questions whether you modified it —
    the hash proves you didn't.

---

## Part 3 — ClamAV: Clean Baseline Scan

```bash
# Scan your home directory
clamscan -r /home/

# -r = recursive — scans all subdirectories
# Look for this at the end:
# Infected files: 0
```

Screenshot the summary. This is your clean baseline.

---

## Part 4 — Scan the EICAR Test File

EICAR is an industry-standard test file. Completely harmless — just a text string —
but every antivirus on earth is trained to detect it.
It came with the `clamav-testfiles` package.

```bash
# See what test files you have
ls /usr/share/clamav-testfiles/

# Scan them
clamscan /usr/share/clamav-testfiles/

# Output will include:
# clam.exe: Clamav.Test.File-6 FOUND
# Infected files: 1
```

Screenshot the output showing `FOUND` with the signature name visible.

---

## Part 5 — Hide EICAR Inside an Image

You've seen ClamAV detect EICAR directly. Now hide it inside a JPEG and see
if ClamAV still catches it.

```bash
# Copy EICAR to work with
cp /usr/share/clamav-testfiles/clam.exe /tmp/eicar-test.exe

# Hide it inside your image
steghide embed -cf original.jpg -ef /tmp/eicar-test.exe -p "redback2025" -sf output.jpg

# Scan the image
clamscan output.jpg
```

**Write down your prediction before running the scan.**

```
# Almost certainly what you'll see:
# Infected files: 0   ← ClamAV missed it
```

Now extract it back out and scan:

```bash
steghide extract -sf output.jpg -p "redback2025"
clamscan eicar-test.exe
# Infected files: 1   ← found immediately
```

Same content. Two completely different results.

---

## Part 6 — VirusTotal: Name vs Hash (lecturer demo)

Look at the ClamAV output — it called the file `Clamav.Test.File-6`.
Every AV vendor names the same file differently:

| Vendor | Name |
|--------|------|
| ClamAV | `Clamav.Test.File-6` |
| Kaspersky | `EICAR-Test-File` |
| Sophos | `Eicar_test_file` |
| Malwarebytes | `Trojan.Eicar` |
| Windows Defender | `Virus:DOS/EICAR_Test_File` |

All different names. Same SHA256 hash:
```
275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f
```

Search that hash on [virustotal.com](https://virustotal.com) — 70+ detections, 70+ different names.

**The name is just a label. The hash is the identity.**

Renaming `eicar.exe` → `invoice.pdf` doesn't change the hash — AV still detects it.
Modifying even one byte → new hash → AV misses it entirely. This is how malware
authors evade detection.

!!! warning "ClamAV missed the hidden EICAR — and that's the point"
    ClamAV uses signature-based detection — it looks for known byte patterns.
    When steghide embeds EICAR inside a JPEG, those patterns are fragmented and
    scattered across the image data. ClamAV scans the file and sees a JPEG.

    This is not a bug. It is a fundamental limitation of all signature-based AV.
    AV is one layer of defence — not the whole answer.

---

## Lab Task — AT1 Evidence

!!! example "TASK 7.1 — Document Your Findings"

    **Screenshots required:**

    - [ ] `freshclam` — definitions updated
    - [ ] Hash of original image vs stego-modified — different hashes
    - [ ] ClamAV clean scan — `Infected files: 0`
    - [ ] ClamAV scan of EICAR — `FOUND` with signature name
    - [ ] ClamAV scan of image with hidden EICAR — result
    - [ ] ClamAV scan of extracted EICAR — `FOUND`
    - [ ] VirusTotal results (lecturer screen ok)

    **Written answers (2-3 sentences each):**

    1. What is a hash and why can't you tell by looking if a file was modified?
    2. ClamAV missed EICAR hidden in the image but found it immediately when extracted. Why?
    3. What does this tell you about relying on AV as your only security control?

    Submit to AT1 portfolio.

---

## Unit Mapping

??? info "Assessment Mapping — click to expand"

    | Activity | Unit | Element |
    |----------|------|---------|
    | Steganography + hashing | ICTSAS214 | 1.1, 1.2, 1.3 |
    | ClamAV install and update | ICTSAS214 | 2.1, 2.2 |
    | Baseline scan | ICTSAS214 | 2.3, 2.4 |
    | EICAR detection | ICTSAS214 | 2.5, 3.1 |
    | Steghide evasion + VirusTotal | ICTSAS214 | 3.1, 3.2 |