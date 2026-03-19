# Glossary

---

**ACL** — Access Control List. A set of rules defining who can access a resource and what they can do.

**ARP** — Address Resolution Protocol. Maps IP addresses to MAC addresses on a local network. Has no authentication — vulnerable to poisoning.

**BitLocker** — Microsoft's full-disk encryption tool. Protects data if a device is lost or stolen.

**BIOS** — Basic Input/Output System. Firmware that runs before the OS. Modern systems use UEFI instead.

**C2 / C&C** — Command and Control. Infrastructure used by attackers to communicate with compromised machines.

**CVE** — Common Vulnerabilities and Exposures. Standardised identifier for known security vulnerabilities (e.g., CVE-2021-44228).

**Deauthentication attack** — Sending forged 802.11 management frames to disconnect a client from a WiFi network. Used to force reconnection to a rogue AP.

**Evil twin** — A rogue access point with the same SSID as a legitimate network, used to intercept traffic.

**Firewall** — Controls what network traffic is allowed in and out of a system or network.

**Hash / Hashing** — A one-way mathematical function that produces a fixed-length fingerprint of data. Same input always produces same output. Cannot be reversed.

**IDS** — Intrusion Detection System. Monitors network or system traffic for suspicious activity and alerts.

**IPS** — Intrusion Prevention System. Like an IDS but actively blocks detected threats.

**Least privilege** — Security principle: every user and process should have only the minimum access needed to do their job.

**Malware** — Malicious software. Includes viruses, trojans, ransomware, spyware, keyloggers, and worms.

**MFA / 2FA** — Multi-Factor Authentication / Two-Factor Authentication. Requires two or more forms of verification to log in.

**Monitor mode** — WiFi adapter mode that captures all packets in range, not just those addressed to the adapter.

**NDB** — Notifiable Data Breach. Australian legislative scheme requiring notification of eligible data breaches to the OAIC and affected individuals.

**NTLM** — NT LAN Manager. Windows authentication protocol. NTLM hashes are commonly targeted in password cracking.

**OSINT** — Open Source Intelligence. Information gathered from publicly available sources.

**Payload** — The part of malware or an exploit that does the damage, after gaining access.

**Penetration testing** — Authorised, simulated attack on a system to find vulnerabilities before real attackers do.

**Phishing** — Fraudulent email (or SMS, voice call) designed to trick recipients into revealing credentials or installing malware.

**PII** — Personally Identifiable Information. Data that can identify a specific individual (name, DOB, TFN, passport number, etc.).

**PMF** — Protected Management Frames (802.11w). WiFi standard that authenticates management frames — prevents deauth attacks. Required by WPA3.

**PCAP** — Packet capture file. A recording of network traffic.

**Privilege escalation** — Gaining higher-level access than initially authorised. Horizontal (same level, different user) or vertical (standard user to admin/root).

**Ransomware** — Malware that encrypts files and demands payment for the decryption key.

**Reverse shell** — A connection initiated by the target machine back to the attacker, bypassing firewall rules that block inbound connections.

**SIEM** — Security Information and Event Management. System that aggregates and analyses security logs from across an environment.

**SMTP** — Simple Mail Transfer Protocol. The protocol used to send email. Has no built-in authentication of senders — enables email spoofing.

**Snort** — Open-source network intrusion detection/prevention system. Uses rule-based detection.

**Social engineering** — Manipulating people into revealing information or taking actions that compromise security. Phishing is a subset.

**SOC** — Security Operations Centre. Team responsible for monitoring, detecting, and responding to security incidents.

**Spear phishing** — Targeted phishing using personal details about the victim to increase credibility.

**SQL injection** — Attack that inserts malicious SQL code into a web form to manipulate a database.

**Steganography** — Hiding data inside another file (e.g., text inside an image) to conceal its existence.

**Threat actor** — Any person or group that conducts an attack. Ranges from script kiddies to nation-states.

**TPM** — Trusted Platform Module. Hardware chip that stores cryptographic keys. Used by BitLocker.

**UEFI** — Unified Extensible Firmware Interface. Modern replacement for BIOS. Supports Secure Boot.

**VPN** — Virtual Private Network. Encrypts network traffic between a device and a server, protecting it from interception on untrusted networks.

**Vulnerability** — A weakness in a system that can be exploited. Different from a threat (what might exploit it) or risk (likelihood × impact).

**Zero-day** — A vulnerability that is unknown to the vendor and has no patch available.
