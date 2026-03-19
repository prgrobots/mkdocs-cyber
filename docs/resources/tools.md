# Tools & References

---

## Parrot OS Tools — Quick Reference

| Tool | Command | Purpose |
|------|---------|---------|
| airmon-ng | `sudo airmon-ng start wlan1` | Enable monitor mode |
| airodump-ng | `sudo airodump-ng wlan1mon` | Scan for WiFi networks |
| aireplay-ng | `sudo aireplay-ng --deauth 10 -a [AP] wlan1mon` | Send deauth frames |
| hostapd | `sudo hostapd config.conf` | Create access point |
| wireshark | `sudo wireshark` | GUI packet capture |
| tcpdump | `sudo tcpdump -i eth0 -w capture.pcap` | CLI packet capture |
| nmap | `nmap -sV -A [target]` | Network scanner |
| msfconsole | `sudo msfconsole` | Metasploit framework |
| hashcat | `hashcat -m 1000 hashes.txt wordlist.txt` | Password cracking |
| john | `john --wordlist=rockyou.txt hashes.txt` | Password cracking |
| steghide | `steghide embed -cf image.jpg -sf secret.txt` | Steganography |
| setoolkit | `sudo setoolkit` | Social Engineering Toolkit |
| snort | `sudo snort -A console -i eth0 -c /etc/snort/snort.conf` | IDS |
| hashid | `hashid [hash]` | Identify hash type |
| binwalk | `binwalk [file]` | Embedded file analysis |

---

## Wordlists on Parrot OS

| List | Path | Size |
|------|------|------|
| rockyou | `/usr/share/wordlists/rockyou.txt` | 14M passwords |
| dirb common | `/usr/share/dirb/wordlists/common.txt` | Web directories |
| Hashcat rules | `/usr/share/hashcat/rules/` | Password mangling rules |

---

## Key References

- [ACSC — Australian Cyber Security Centre](https://www.cyber.gov.au)
- [ACSC Small Business Guide](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/small-business-cyber-security-guide)
- [CVE Database](https://cve.mitre.org)
- [Exploit Database](https://www.exploit-db.com)
- [Wireshark Display Filters](https://www.wireshark.org/docs/dfref/)
- [Hashcat Example Hashes](https://hashcat.net/wiki/doku.php?id=example_hashes)
- [Metasploit Modules](https://www.rapid7.com/db/)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)

---

## Legislation

| Act | Relevance |
|-----|-----------|
| Criminal Code Act 1995 (Cth) | Unauthorised computer access — s477 |
| Cybercrime Act 2001 (Cth) | Unauthorised data modification |
| Privacy Act 1988 (Cth) | Handling of personal information |
| Notifiable Data Breaches scheme | Mandatory breach reporting obligations |
| Spam Act 2003 (Cth) | Commercial electronic messages |
