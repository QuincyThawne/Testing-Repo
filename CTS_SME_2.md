# CTS SME 2 Summary

## Session Details
- **Date & Time:** 09:56 AM, 04-04-2025

---

## Speakers
- **Chandrasekaran:** Senior Project Manager, Cognizant (21+ years)
- **Vignesh:** Cybersecurity Specialist (14+ years)

---

## Key Facts & Concepts
- Microsoft releases patches every second Tuesday of the month
- Attack vectors identified for Anti-Virus apps
- EDR (End-Point Detection and Response) uses AI for virus/malware detection
- Crown Jewel Application: Most critical asset of an organization
- HIPAA: GRC framework for healthcare
- BYoD: Bring Your Own Device
- CISO: Chief Information Security Officer
- CIO: Chief Information Officer
- CEO: Final decision maker after CISO → CIO → CEO
- Playbook: Pre-defined procedures for incident response
- Mossad: Israel's intelligence agency
- UEBA: User and Entity Behavior Analytics
- Email Security Protocols: SPF, DKIM, DMARC
- KPI: Key Performance Indicators

---

## Agenda
- Security triad
- Defense in depth
- Key cybersecurity practices
- CNI overview
- Firewall and WAF
- Proxy and VPN
- Endpoint and email security
- SIEM and SOC
- Cloud basics and security
- IRIL

---

## Cybersecurity Categories
- IAM (MFA, SSO, passwords)
- Data Protection & Privacy (encryption, data masking, DLP)
- CNI (Cloud Infra & Network Security, web-app, email)
- GRC
- Threat & Vulnerability Management

---

## Cybersecurity Definition
Cybersecurity is the body of technologies, processes, and practices designed to protect networks, computers, programs, and data from attack, damage, or unauthorized access.

### Security Triad
- **Confidentiality:** Protect info from unauthorized disclosure
- **Integrity:** Protect info from unauthorized modification
- **Availability:** Ensure info is available to authorized parties when needed

---

## Defense in Depth
- **Policies, Procedures & Awareness:** Passwords, policies, data classification
    - Example: Mock phishing tests for employees
- **Physical:** Locks, fences, security guards
    - Example: Multiple biometrics, access cards
- **Perimeter:** Firewall, VPN, packet filters
    - Example: DMZ zones for network filtering
- **Internal Network:** Firewall, intrusion detection, encryption
- **Host:** OS, patches, malware protection
- **App:** SSO, authentication, authorization
- **Data:** Database, content, message security

---

## Key Cybersecurity Practices
- IDAM (Identity & Access Management)
- CNI (Cloud, Network & Infra Security)
- TVM (Threat & Vulnerability Management)
- GRC (Governance, Risk & Compliance)
- DPP (Data Protection & Privacy)

---

## DoS vs DDoS
- **DoS:** Single source, easier to block
- **DDoS:** Multiple sources, harder to block

---

## Cloud, Network & Infra Security Overview
### Cloud Security
- App on Cloud: CSPM
- Hybrid/Multi Cloud: CWPP
- Cloud Migrate/Operate: IaaS/PaaS/SaaS

### Network Security
- Network Protect: Firewall
- Access Protect: NAC
- Web Protect: Proxy
- Policy/Platform App: Intrusion

### Infra Security
- Host Protect: Malware
- Email Protect: Emails
- Microsegmentation: Zero Trust
- FIM: Unauthorized Access

### SIEM/SOAR/Threat Intel/Threat Hunting/UEBA
- Monitoring, IR, Orchestration & Automation
- Threat Management

### Enablers
- Control assessment
- Automation & orchestration
- AI/ML
- Ticketing tool
- Delivery excellence

### Acronyms
- CSPM: Cloud Security Posture Management
- CWPP: Cloud Workload Platform Protection
- SIEM: Security Information and Event Management
- CASB: Cloud Access Security Broker
- UEBA: User Entity Behavior Analysis
- SOAR: Security Orchestration, Automation & Response
- AI: Artificial Intelligence
- ML: Machine Learning
- IoT: Internet of Things
- OT: Orchestration Tool

---

## Firewall & WAF
### Firewall
- Controls traffic flow into/out of a network
- Prevents attacks
- Acts as buffer between public and private networks
- Placed at perimeter/entry point

#### Types of Firewalls
- Packet filtering
- Circuit level gateways
- Application level gateway (proxy)
- Stateful multilayer inspection (SMLI)
- Next Gen Firewalls
- Cloud Firewalls
- Unified Threat Management (UTM)

#### Vendors
- Palo Alto
- Fortinet
- Cisco
- Check Point
- Barracuda
- Juniper Networks

### Web Application Firewall (WAF)
- Defends layer 7 perimeter from malicious traffic
- Secures business-critical apps from OWASP Top 10, zero-day threats, known/unknown vulnerabilities
- Protects web servers from external attacks and data leakage
- Monitors, filters, and blocks data packets

#### Attack Types Protected by WAF
- Bots (good: search engines, bad: DoS, fraud)
- Malicious uploads (malware payloads)

#### Vendors
- Akamai
- Barracuda
- Fortinet
- F5 (market lead)
- Cloudflare
- Imperva

---

## Proxy
A proxy server acts as a gateway between you and the internet, separating end users.

- **Forward Proxy:** Transmits data for internal users; assesses data before connection
- **Reverse Proxy:** Sits in front of web servers; directs requests from browsers to servers

### Deployment Methods
- **On-prem Proxy:** Org's servers, hardware required, limited scalability, periodic updates, SLA guarantees
- **Cloud Proxy:** Globally distributed servers, outsourced, unlimited scalability, real-time updates, higher SLA

#### Vendors
- Microsoft (cloud)
- Zscaler
- Forcepoint (on-prem)
- Broadcom

---

## VPN
A VPN creates a secure, encrypted connection between your device and a remote server, masking your IP and protecting online activity.

- Uses public telecommunication (Internet) instead of leased lines
- Popular for remote work

### Types
- Site-to-Site VPN
- Remote Access VPN
- Cloud VPN
- SSL VPN

---

## Antivirus Actions
- **Delete:** Remove from device
- **Quarantine:** Isolate and await admin action
- **Clean:** Remove malware
- **Pass:** Record and monitor
- **Deny Access:** Block access

---

## Data States & Protection
- **Data in use**
- **Data in transit**
- **Data at rest**

### Data Loss Prevention
- Data discovery
- Data classification
- Data protection

---

## Whitelisting
Approves a list of email addresses, IPs, domains, or apps, denying all others. Trust-centric, but risky if wrong user is whitelisted.

---

## Email Security
- Widely used network service
- Prevents unauthorized access

### Key Elements
- DMARC, DKIM, SPF: Prevent spammers, phishers
- DKIM/SPF: Demonstrate legitimacy
- DMARC: Marks as spam if others fail

#### Vendors
- Broadcom
- Cisco
- Crowdstrike
- Forcepoint
- Microsoft
- Proofpoint
- SentinelOne
- Trend Micro
- Trellix

---

## SOC (Security Operation Center)
Centralized team monitoring/responding to cyber threats, staffed 24/7.

### Functions
- Detect, analyze, respond, prevent threats
- Report incidents

### Users
- Large organizations
- Educational institutions
- Transportation agencies

### SOC Team Roles
- **Tier 1 Analyst:** Alert triage, incident detection, false positive elimination, classify alerts, update tracker
- **Tier 2 Analyst:** Review tickets, incident response, vendor support, governance meetings, coordinate remediation
- **Tier 3 Analyst:** All Tier 2 + user profile management, config changes, root cause analysis, develop processes
- **Incident Response Coordination:** Lead technical response, coordinate with CSIRT, review RCA, document actions
- **Threat Intelligence Analyst:** Collect, assess, catalog threat indicators
- **Threat Hunter**
- **Security Engineer**

### SIEM Architecture
- Regular operations
- Incident detection
- Ticket generation
- Sent to incident response for SOC

### Frameworks
- MITRE ATT&CK (most important)
- NIST (next most important)

#### SIEM Vendors
- Crowdstrike
- IBM QRadar
- Cisco
- Trellix
- SolarWinds
- Fortinet
- Microsoft
- ManageEngine

#### Cloud Vendors
- Microsoft
- AWS
- Google
- Oracle Cloud

---

## ITIL (Infrastructure Technology and Information Library)
### Key Focus Areas
- Service strategy
- Service design
- Service transition
- Service operation
- Continual service improvement

### Day-to-Day Operations
- Incident management
- Service vectors
- Change management
- Problem management
- Capacity management

> **Note:** 10% technical skill, 90% process following

---

## Demo Credentials
- URL: fortigate.fortidemo.com
- Username: demo
- Password: demo
