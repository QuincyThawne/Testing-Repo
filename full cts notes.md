
# Cybersecurity Self-Learning Handbook

This document contains half-page notes for all the major topics in the Self-Learning Cybersecurity Program.  

---

## 1. Cybersecurity Overview  
Cybersecurity is the practice of protecting systems, networks, and data from unauthorized access, theft, or damage. With the increasing dependence on technology, organizations face a wide range of threats such as malware, phishing, ransomware, and denial-of-service attacks. Cybersecurity ensures that information remains safe, reliable, and available.  

The **CIA Triad** forms the foundation of cybersecurity:  
- **Confidentiality** – Ensuring only authorized people access data. Example: Encryption.  
- **Integrity** – Preventing unauthorized changes to data. Example: Hashing.  
- **Availability** – Making sure systems and data are accessible when needed. Example: Redundancy, backups.  

Cybersecurity also includes protecting users, devices, applications, and networks. This involves preventive controls (firewalls, antivirus), detective controls (IDS/IPS, monitoring), and response measures (incident handling, recovery). The field is broad and continuously evolving due to emerging technologies like IoT, AI, and cloud computing.  

**Key takeaway:** Cybersecurity is not just a technical domain but also a business enabler—protecting customer trust, legal compliance, and organizational resilience.  

---

## 2. Firewall & WAF  
A **firewall** is a network security device that monitors and filters traffic based on predefined rules. It creates a barrier between a trusted internal network and untrusted external networks (like the internet). Firewalls can be hardware-based or software-based and operate at different layers of the OSI model. Common types include **packet-filtering firewalls, stateful firewalls, and next-generation firewalls (NGFWs)** that incorporate intrusion prevention and deep packet inspection.  

A **Web Application Firewall (WAF)** specifically protects web applications by monitoring HTTP/HTTPS traffic. It prevents attacks such as SQL injection, cross-site scripting (XSS), and file inclusion. Unlike traditional firewalls, which filter traffic at the network or transport layer, a WAF works at the application layer.  

Together, firewalls and WAFs form the first line of defense against cyber threats. For example, a firewall may block unauthorized remote access attempts, while a WAF ensures that malicious input fields in a website cannot be exploited. In modern architectures, cloud-based WAFs are widely used to secure SaaS applications.  

**Key takeaway:** Firewalls safeguard networks, while WAFs secure applications. Both are critical for layered defense strategies.  

---

## 3. IDS & IPS  
An **Intrusion Detection System (IDS)** is a monitoring tool that identifies suspicious or malicious activities on a network. It works by comparing traffic patterns against known attack signatures or anomaly-based rules. IDS systems are passive—they only detect and alert administrators about potential attacks.  

An **Intrusion Prevention System (IPS)** goes a step further. It not only detects but also blocks malicious traffic in real time. IPS solutions are placed inline within the network so that they can actively prevent threats like port scanning, brute-force attacks, or malware injection.  

There are two main types of IDS/IPS:  
- **Signature-based** – Detects known attack patterns.  
- **Anomaly-based** – Identifies unusual activity compared to normal baselines.  

**Key takeaway:** IDS provides visibility into threats, while IPS provides protection. Organizations often use both to ensure layered network defense.  

---

## 4. Proxy & VPN  
A **proxy server** acts as an intermediary between users and the internet. It hides user IP addresses, filters web content, and can enforce access policies. Proxies are often used for content filtering in organizations, caching frequently accessed content, and maintaining anonymity.  

A **Virtual Private Network (VPN)**, on the other hand, provides a secure and encrypted connection between the user and the destination network. VPNs are essential for remote employees to securely access corporate resources. They prevent eavesdropping by encrypting data packets transmitted over public networks.  

**Comparison:**  
- Proxy provides anonymity but may not encrypt traffic.  
- VPN ensures encryption and confidentiality, protecting against man-in-the-middle attacks.  

**Key takeaway:** Proxies help with anonymity and access control, while VPNs ensure secure communication over untrusted networks.  

---

## 5. Endpoint & Email Security  
Endpoints such as laptops, mobile devices, and desktops are primary targets for attackers. **Endpoint security** ensures that these devices are protected using antivirus software, firewalls, and advanced tools like Endpoint Detection and Response (EDR). Modern solutions like Microsoft Defender XDR use AI and threat intelligence to detect advanced attacks.  

**Email security** focuses on preventing phishing, spam, malware, and ransomware delivered through emails. Techniques include spam filters, attachment sandboxing, and anti-phishing solutions. Since emails are the most common attack vector, security awareness training for employees is equally important.  

**Key takeaway:** Protecting endpoints and email systems prevents attackers from exploiting the weakest link—end users.  

---

## 6. SIEM & SOC  
**SIEM (Security Information and Event Management)** is a solution that collects logs from across the IT infrastructure, correlates them, and detects potential threats. Examples include Splunk, IBM QRadar, and ArcSight. SIEMs are essential for compliance, forensics, and monitoring.  

A **SOC (Security Operations Center)** is a centralized team responsible for monitoring, analyzing, and responding to security incidents using SIEM tools. SOC teams usually operate 24/7 to ensure continuous protection. They follow processes like threat hunting, incident response, and digital forensics.  

**Key takeaway:** SIEM provides the tools, while SOC provides the people and processes to actively defend an organization.  

---

## 7. Cloud Security  
Cloud security refers to practices that protect data, applications, and services hosted in cloud environments like AWS, Azure, or Google Cloud. Risks include misconfigurations, insider threats, insecure APIs, and compliance issues.  

Best practices include:  
- Shared Responsibility Model (cloud provider secures infrastructure, customer secures data).  
- Encrypting data at rest and in transit.  
- Using IAM policies for least-privilege access.  
- Regular auditing and monitoring.  

**Key takeaway:** Cloud offers scalability but requires robust security policies to prevent breaches.  

---

## 8. Identity & Access Management (IAM)  
**IAM** ensures that only authorized individuals have access to the right resources at the right time. It manages digital identities and enforces authentication and authorization.  

**Key concepts:**  
- **Authentication** – Verifying identity (passwords, biometrics, MFA).  
- **Authorization** – Granting access rights.  
- **PAM** – Secures privileged accounts like system admins.  
- **IGA** – Governs identity lifecycle, ensuring compliance.  
- **SSO & Federation** – Simplify user login across systems.  

**Key takeaway:** IAM reduces insider threats, improves compliance, and strengthens security posture.  

---

## 9. Threat & Vulnerability Management  
This involves identifying, classifying, prioritizing, and remediating weaknesses in IT systems. Tools like Nessus, Qualys, and OpenVAS help scan for vulnerabilities.  

Main processes include:  
- **Vulnerability Assessment** – Identifying flaws.  
- **Penetration Testing** – Simulating attacks to exploit flaws.  
- **Patch Management** – Updating systems regularly.  
- **Risk Prioritization** – Addressing high-risk vulnerabilities first.  

**Key takeaway:** Proactive vulnerability management reduces the attack surface and prevents breaches.  

---

## 10. Application Security  
Application security protects software from design to deployment. The major methods include:  
- **SAST (Static Application Security Testing)** – Analyzes source code for vulnerabilities.  
- **DAST (Dynamic Application Security Testing)** – Tests running applications for security flaws.  
- **SCA (Software Composition Analysis)** – Identifies risks in open-source components.  
- **Threat Modeling** – Anticipates attack vectors during design.  

**Key takeaway:** Secure coding and regular testing help prevent exploits like SQL injection, XSS, and insecure APIs.  

---

## 11. DevSecOps  
DevSecOps integrates security into the DevOps pipeline. Instead of treating security as a separate step, it becomes continuous throughout development, testing, and deployment. Automated tools check for vulnerabilities, misconfigurations, and compliance issues.  

**Benefits:** Faster detection of issues, reduced cost of fixing vulnerabilities, and enhanced overall security.  

**Key takeaway:** Security must be built into development, not added as an afterthought.  

---

## 12. Data Protection & Privacy  
Data protection ensures data is safe from loss, corruption, or unauthorized access. Privacy ensures data is accessed only by authorized individuals and according to laws (GDPR, IT Act).  

**Techniques:** Encryption, access controls, data masking, backups, and disaster recovery.  

**Key takeaway:** Protecting user data builds trust, ensures compliance, and reduces legal/financial risks.  

---

## 13. Cryptography & PKI  
Cryptography secures information through encryption, hashing, and digital signatures.  
- **Symmetric encryption (AES)** – Same key for encryption & decryption.  
- **Asymmetric encryption (RSA)** – Public-private key pair.  
- **Hashing (SHA-256)** – One-way function for integrity.  
- **Digital signatures** – Ensure authenticity.  

**PKI (Public Key Infrastructure)** provides the framework for managing digital certificates and encryption keys. It underpins secure communications like HTTPS and VPNs.  

**Key takeaway:** Cryptography enables confidentiality, integrity, and authentication across digital systems.  

---

## 14. Data Discovery & Classification  
Organizations must know where sensitive data resides. **Data discovery** identifies stored, shared, or transmitted data, while **classification** labels data based on sensitivity (public, internal, confidential).  

This helps in applying correct protections like encryption or access restrictions. Tools such as Microsoft Purview or Varonis automate this process.  

**Key takeaway:** Data discovery and classification are prerequisites for strong data protection strategies.  

---

## 15. Data Activity Monitoring  
Data Activity Monitoring (DAM) tools track and analyze all database activity. They help prevent insider threats, detect unauthorized access, and meet compliance requirements.  

Examples: IBM Guardium, Imperva DAM. They can alert or block suspicious queries, reducing risks of data exfiltration.  

**Key takeaway:** DAM provides real-time visibility into sensitive data access.  

---

## 16. Cybersecurity Mock Tests  
Mock tests allow learners to practice and validate their knowledge in key areas like network security, penetration testing, and cryptography. These help prepare for certification exams (CompTIA Security+, CEH, CISSP) and interviews.  

**Key takeaway:** Regular practice with mock tests reinforces concepts and identifies knowledge gaps.  


---

## 17. AWS KMS Basics  
**AWS Key Management Service (KMS)** is a managed service that allows users to create, control, and manage cryptographic keys used to protect data. It integrates with many AWS services such as S3, RDS, and Lambda to provide encryption at rest and in transit.  

**Key features:**  
- Centralized key management for AWS workloads.  
- Customer Managed Keys (CMKs) and AWS Managed Keys.  
- Integration with AWS CloudTrail for auditing.  
- Automatic key rotation policies.  

**Use case:** Encrypting S3 objects, database fields, or securing secrets for applications.  

**Key takeaway:** AWS KMS makes enterprise-grade encryption accessible and manageable without having to handle key infrastructure manually.  

---

## 18. Azure Key Vault Basics  
**Azure Key Vault** is a cloud service for securely storing and accessing secrets, keys, and certificates. It helps safeguard cryptographic keys and secrets used by applications and cloud services.  

**Key features:**  
- Centralized secret management (API keys, connection strings).  
- Hardware Security Module (HSM) for key protection.  
- Integration with Azure Active Directory for access control.  
- Logging and monitoring via Azure Monitor.  

**Key takeaway:** Azure Key Vault reduces the risk of secret leakage and centralizes security management for cloud-native applications.  

---

## 19. Key Lifecycle Management Basics  
Key Lifecycle Management (KLM) covers the creation, distribution, rotation, storage, and eventual destruction of cryptographic keys. Proper KLM ensures that compromised or expired keys don’t weaken security.  

**Lifecycle stages:**  
1. **Generation** – Creating strong keys.  
2. **Distribution** – Securely sharing keys with authorized systems.  
3. **Use** – Encrypting/decrypting or signing.  
4. **Rotation** – Periodically changing keys.  
5. **Revocation/Destruction** – Retiring keys safely.  

**Key takeaway:** Proper key lifecycle management ensures continuous cryptographic strength and compliance.  

---

## 20. OpenSSL  
**OpenSSL** is an open-source toolkit that implements SSL/TLS protocols for secure communication. It provides cryptographic functions such as key generation, certificate signing, and encryption.  

**Common uses:**  
- Generating RSA key pairs.  
- Creating Certificate Signing Requests (CSRs).  
- Managing X.509 certificates.  
- Encrypting files and messages.  

**Key takeaway:** OpenSSL is the backbone of modern cryptographic operations and secure web communications (HTTPS).  

---

## 21. PKI Architecture Overview & Deployment  
**Public Key Infrastructure (PKI)** provides a framework for issuing, managing, and validating digital certificates. It enables secure data exchange over untrusted networks.  

**PKI components:**  
- **Certificate Authority (CA)** – Issues certificates.  
- **Registration Authority (RA)** – Verifies identity before issuing.  
- **Certificate Repository** – Stores and distributes certificates.  
- **Revocation System** – Lists invalid/expired certificates.  

**Deployment steps:** Establish a CA, configure policies, distribute certificates, and implement revocation lists (CRLs/OCSP).  

**Key takeaway:** PKI underpins trust in digital communications like HTTPS, VPNs, and email security.  

---

## 22. DevSecOps  
**DevSecOps** integrates security practices into every stage of the DevOps lifecycle. Instead of applying security at the end, it is automated and continuous.  

**Practices:**  
- Shift-left security (catch issues early in development).  
- Automated vulnerability scanning in CI/CD pipelines.  
- Infrastructure as Code (IaC) security.  
- Continuous monitoring.  

**Key takeaway:** DevSecOps reduces costs, improves security posture, and ensures compliance without slowing down development.  

---

## 23. Identity Governance & Administration (IGA)  
**IGA** focuses on managing digital identities, access rights, and compliance. It automates identity lifecycle processes such as provisioning, role management, and access reviews.  

**Capabilities:**  
- User provisioning/de-provisioning.  
- Role-based access control.  
- Audit and compliance reporting.  
- Access certification.  

**Key takeaway:** IGA improves efficiency, reduces insider risks, and ensures regulatory compliance.  

---

## 24. Privileged Access Management (PAM)  
**PAM** secures accounts with elevated privileges like system administrators, database admins, and root users. These accounts are prime targets for attackers.  

**Techniques:**  
- Vaulting credentials.  
- Session recording and monitoring.  
- Just-in-time (JIT) privileged access.  
- Least privilege enforcement.  

**Key takeaway:** PAM prevents misuse of powerful accounts and protects organizations from insider threats and external attackers.  

---

## 25. Identity & Access Governance (IAG)  
**IAG** is often used interchangeably with IGA but emphasizes governance over who has access to what resources. It focuses on enforcing access policies and ensuring accountability.  

**Functions:**  
- Enforcing segregation of duties (SoD).  
- Monitoring high-risk access.  
- Generating compliance reports.  

**Key takeaway:** IAG strengthens IAM by embedding governance, accountability, and compliance.  

---

## 26. Splunk (SIEM)  
**Splunk** is a leading SIEM platform that collects, indexes, and analyzes machine data in real-time. It provides dashboards, alerts, and advanced analytics.  

**Capabilities:**  
- Log aggregation and search.  
- Real-time threat detection.  
- Security automation and orchestration.  
- Compliance reporting.  

**Key takeaway:** Splunk empowers SOC teams with powerful insights for faster threat detection and response.  

---

## 27. Zscaler (SASE/Proxy)  
**Zscaler** provides cloud-based security through a Secure Access Service Edge (SASE) framework. It acts as a proxy, inspecting and securing traffic before reaching applications.  

**Features:**  
- Zero Trust Network Access (ZTNA).  
- Cloud firewall and secure web gateway.  
- Data Loss Prevention (DLP).  
- Secure remote access for employees.  

**Key takeaway:** Zscaler eliminates the need for traditional VPNs and enables secure, cloud-first networking.  

---

## 28. Palo Alto (Firewall)  
**Palo Alto Networks** provides Next-Generation Firewalls (NGFWs) with deep inspection, intrusion prevention, and advanced malware protection.  

**Key strengths:**  
- Application-aware filtering.  
- Threat intelligence with WildFire.  
- Cloud integration (Prisma Access).  
- Strong segmentation and Zero Trust adoption.  

**Key takeaway:** Palo Alto is a leader in enterprise-grade firewalls and advanced threat protection.  

---

## 29. Microsoft Defender XDR  
**Microsoft Defender XDR** is an extended detection and response solution that integrates security across endpoints, identities, emails, and applications.  

**Capabilities:**  
- Endpoint detection & response (EDR).  
- Threat intelligence integration.  
- Automated incident investigation & response.  
- Cloud-based analytics.  

**Key takeaway:** Defender XDR provides holistic security visibility and automated defense for enterprise environments.  

---

## 30. SSO vs MFA  
- **Single Sign-On (SSO):** Allows users to authenticate once and access multiple applications without re-entering credentials. Improves user convenience.  
- **Multi-Factor Authentication (MFA):** Requires additional verification factors (OTP, biometrics, tokens) beyond a password. Improves security.  

**Comparison:**  
- SSO improves usability but can become a single point of failure.  
- MFA adds layers of defense against compromised credentials.  

**Key takeaway:** Best practice is to combine SSO with MFA for balance between security and usability.  

---

## 31. Federation  
**Federation** allows identity information to be shared across trusted domains/organizations. It enables users to authenticate once and access resources in different systems using federated trust.  

**Example:** A university account allowing login to cloud-based student resources.  

**Key takeaway:** Federation simplifies identity management across multiple organizations.  

---

## 32. Identity Federation  
**Identity Federation** extends the concept of federation by enabling users to use the same digital identity across multiple systems, applications, or organizations.  

**Technologies:** SAML, OAuth, OpenID Connect.  
**Example:** Logging into third-party apps using Google or Microsoft credentials.  

**Key takeaway:** Identity federation provides seamless access across ecosystems while reducing password fatigue and administrative overhead.  


---

# Abbreviation Legend

- **CIA**: Confidentiality, Integrity, Availability
- **WAF**: Web Application Firewall
- **IDS**: Intrusion Detection System
- **IPS**: Intrusion Prevention System
- **VPN**: Virtual Private Network
- **EDR**: Endpoint Detection and Response
- **XDR**: Extended Detection and Response
- **SIEM**: Security Information and Event Management
- **SOC**: Security Operations Center
- **IAM**: Identity and Access Management
- **IGA**: Identity Governance and Administration
- **IAG**: Identity and Access Governance
- **PAM**: Privileged Access Management
- **MFA**: Multi-Factor Authentication
- **SSO**: Single Sign-On
- **PKI**: Public Key Infrastructure
- **KMS**: Key Management Service
- **HSM**: Hardware Security Module
- **CSR**: Certificate Signing Request
- **CA**: Certificate Authority
- **RA**: Registration Authority
- **CRL**: Certificate Revocation List
- **OCSP**: Online Certificate Status Protocol
- **SASE**: Secure Access Service Edge
- **ZTNA**: Zero Trust Network Access
- **SoD**: Segregation of Duties
- **DLP**: Data Loss Prevention
- **SAML**: Security Assertion Markup Language
- **OAuth**: Open Authorization
- **API**: Application Programming Interface
- **IaC**: Infrastructure as Code


---

# CTS SME 1 Summary

## Session Details
- **Date & Time:** 10:16 AM, 18-03-2025

---

## Speakers
- **Karthick**: GenZ leader (25 yr exp), CSP
- **Sivakumar Swaminathan**: SAST/DAST Expert

---

## Cybersecurity Controls
- GRC
- Threat and Vulnerability Management
- Data Protection & Management
- Identity and Access Management
- Cloud & Infra Security

---

## Vulnerability Management
### Phase 1
- What is vulnerability
- The need for vulnerability management
- Vulnerability, threat and risk
- CIA triad
- Types of vulnerabilities

#### Vulnerability
A vulnerability is a weakness or flaw in a system, application, or network that attackers can exploit to gain unauthorized access or control.

#### Key Areas of Vulnerability Management
- Protects sensitive data
- Reduces risk
- Ensures compliance
- Maintains system integrity
- Prevents financial loss
- Enhances reputation
- Improves incident response
- Supports business continuity
- Facilitates proactive security
- Adapts to evolving threats

#### Honeypot
A network hosted by an organization to attract attackers and is exposed to the internet.

#### Types of Vulnerabilities
- Software vulnerabilities
- Network vulnerabilities
- Misconfigurations
- Unsecured APIs
- Outdated or unpatched software
- Access control issues
- Zero-Day
- Human error

> **Note:** HDFC bank is not safe (every vulnerability was explained with HDFC bank as example)

---

### Phase 2
- Vulnerability management lifecycle
- Basics of vulnerability assessment methodologies
- Vulnerability management workflow
- Common vulnerability scanning tools
- Brief about vulnerability management

#### Vulnerability Management Lifecycle
1. Discover assets
2. Assess the vulnerability and assets
3. Prioritize the assets and risk
4. Report the findings to stakeholders
5. Remediate the assets from risk of exploitation
6. Verify the remediation was successful (false positives)

#### Types of Assets
- Internet facing assets (higher priority)
- Internal facing assets (lower priority)

#### CVSS (Common Vulnerability Scoring System)
- 5: Highest score
- 4: High level vulnerability
- 3: Medium level vulnerability
- 2,1: Low level vulnerability

#### Vulnerability Management Workflow
- Planning and preparation
- Information gathering
- Vulnerability identification
- Vulnerability analysis
- Risk assessment
- Reporting

#### Scanning Methodologies
- Remote Scanning (using IPs)
- Agent-Based Scanning (software planted such as Anti-Virus)
- Credential-Based Scanning (authenticated scan to reduce false positives)
- Non-Credential-Based Scanning (Blackbox testing with no authenticity or public accessibility)
- Passive Scanning
- Active Scanning
- Internal Scanning (conducted from within network)
- External Scanning (conducted from outside the network)
- Network Mapping
- Port Scanning

---

## Penetration Testing (PT)
Penetration testing is a simulated attack against your computer system or web servers to check for exploitable vulnerabilities.

### PT Classification
- **White box:** Given the entire configuration, code, architecture, and credentials to conduct the PT
- **Black box:** Little to no information given for testing (only IP or URL)
- **Grey box:** Combination of both

### Different Ways of Testing
- Automated Penetration Testing
- Manual Penetration Testing

### Phases
1. Setup - create sandbox and configure tools
2. Discovery - identify target
3. Enumeration - scan
4. Detection - identify and assess
5. Exploitation - use the exploit
6. Post exploitation - assess the damage
7. Reporting - report the above results
8. Readout - present the report
9. Remediation - fix any and all exploits
10. Final testing - do it all over again

---

## Audit, VA, and PT
- Security audits ensure governance and compliance in an enterprise
- Vulnerability assessment
- Penetration testing

### Benefits of VAPT
- Proactive mitigation
- Assurance
- Achieve compliance
- Evaluate efficiency of network
- Reduce impact

#### Common Ports
- 135, 445 (Windows)
- 137, 139
- 22

#### Tool Example
- QUALYS (lab)

---

## DAST/SAST (Siva)

### DAST (Dynamic Application Security Testing)
- Tests are done without access to source code
- Identifies issues in runtime
- Done by simulated testing
- Can be either black-box or grey-box

#### DAST Process (Grey-box)
1. Application profiling (collect data from dev team such as URLs)
2. Automated scan (use tool such as Vulnerability scan)
3. Analyze false positives (filter false positives)
4. Manual testing (find false +ve and false -ve)
5. Reporting (inform stakeholders)
6. Remediation (aid devs to fix the vulnerabilities)
7. Rescan and closure (all over again)

#### Web Application Vulnerabilities
- **Logical vulnerabilities:** Detected by human errors (business logic, race conditions, input validation, etc.)
    - Transaction logic falls
    - Session management
    - Error handling
    - Unintended functionalities
- **Technical vulnerabilities:** Detected by tools (injection attacks, SSRF, CSRF, OWASP TOP 10)
    - Refer to OWASP Top 10 vulnerabilities

#### DAST Tools
- OWASP ZAP
- Burp Suite
- Veracode
- Microfocus

---

### SAST & SCA
- **SAST:** Static Application Security Testing
    - Tests are done with access to source code
    - Done by simulated testing
    - White-box testing
    - Must be automated

#### SAST Methodology
1. Source code with associated libraries
2. Compile the source code using IDE and import to workspace for automated scanning
3. Tools report security issues with dashboard based on vulnerabilities and priorities
4. Analyze security issues and eliminate false positives, benchmark with OWASP Top 9, and prepare risk-based prioritized vulnerability reports
5. Report walkthrough sessions with dev teams on remediation procedures and iterative rescan of code fixed by development team

#### OWASP Top 9
- Input validation
- Source code design (insecure code design)
- Information leakage and error handling (unhandled exception)
- Direct object reference (direct reference to file system or DB)
- Resource usage (insecure file creation and file system object)
- API usage (insecure database calls and random number creation)
- Best practices (variable aliasing and unsafe initialization)
- Weak session management (passing cookies over non SSL)
- Using HTTP GET query strings (passing URL query string)

#### SQL Injections
- **Tautologies:** Using `OR 1=1`
- **UNION Queries:** Union used with the number of columns in the first query

**Prevention:**
- Prepared statement and input validation
- Least privilege
- Whitelist input validation

---

### SCA (Software Composition Analysis)
- SCA is a process or set of tools used to inspect software components and their dependencies to identify compliance concerns
- Dependencies often form complex graphs; SCA tools build a complete picture of this graph
- The dependency graph and Common Vulnerabilities and Exposure (CVE) databases are used by SCA tools to identify risks

#### SCA Tools
- OWASP Dependency-Check
- SpotBugs
- DEV Skim
- SonarQube
- Snyk

---

## SDLC (Software Development Life Cycle)
| Aspect      | SAST                | DAST                        | SCA                                 |
|-------------|---------------------|-----------------------------|-------------------------------------|
| When        | Early (coding, build)| Late (testing, staging, prod)| Throughout the SDLC                 |
| Focus Area  | Application's own code| Running application behavior | Third-party libraries and dependencies|
| Detects     | Code level vulns, coding flaws| Runtime vulns, config issues| Known vulns, license risks          |
| Requires    | Source code         | Running application         | Project dependencies info           |
| Advantages  | Early detection, precise location| Real-world perspective, no source code needed| Addresses third-party risks, license management|
| Disadvantages|                     |                             |                                     |

---
---

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


---

# CTS SME 3 Summary

## Session Details
- **Date & Time:** 09:43 AM, 16-04-2025

---

## Speakers
- **Vinoth Shankar:** 20+ years of experience
- **Kasthuri:** 12+ years of experience

---

## Topics Covered
- Cybersecurity practice
- Identity and Access Management (IAM) overview
- IAM functional services
- Privileged Access Management (PAM) in detail (CyberArk)
- Access Management in detail (OKTA)
- Data protection and security

---

## Cybersecurity Practice - Service Offering
- GRC (Governance, Risk and Compliance)
- TVM (Threat and Vulnerability Management)
- Data Protection and Privacy
- Identity and Access Management
- Cloud and Infra Security

---

## Identity and Access Management (IAM)
- Enables the right people to access the right resources at the right time for the right reasons
- Manages users, accounts, authentication, authorization, and privileges across systems and enterprise boundaries
- Automates user identity and permission management

### Common Challenges
- Automating identity lifecycle (joiner, leaver, mover, termination)
- Weak passwords, periodic resets
- Admin password reset overhead
- Manual user access
- Timely revocation of user access
- Isolated identity storage, manual provisioning
- Multiple passwords and sign-on attempts
- Excessive/anonymous access
- Lack of strong second-level authentication
- Lack of secure integration with external partners/cloud SaaS
- Managing/auditing shared privileged admin accounts
- Lack of access review, certification, remediation
- Missing audit/compliance controls (SOX)

### Efficiencies
- Efficient user onboarding (JLM process automation)
- Improved admin productivity
- Seamless user experience (no multiple passwords)
- Reduced IT/support costs and operational expenses

#### Example: HIPAA

### IAM Offerings & Products
- **Identity Management:** Provisioning, password management
    - Products: SailPoint IdentityIQ, Oracle Identity Manager, ForgeRock OpenIDM
- **Access Management:** Authentication, authorization
    - Products: Okta, Azure AD, Ping Access
- **Federation:** Single sign-on, OAuth
    - Products: Ping Federate, ForgeRock OpenAM
- **Multifactor Authentication:** Token/OTP/Biometric
    - Products: RSA Adaptive AuthN, Truu
- **RBAC:** Role, attribute, policy
- **Access Governance:** Role mining, lifecycle, access request/review, certification
- **Customer IAM:** SSO, gamification, identity relationship management
- **API Security:** Securing API gateways, integration, policies
- **IDaaS/Cloud Security:** Azure/AWS/Google native IAM/MFA/hybrid identity
- **PAM:** Privileged passwords/session management, endpoint privileged
    - Product: CyberArk

---

## IAM Functional Areas
1. **Identity Management & Governance:** Automate identity lifecycle, enable seamless access
2. **Access Management:** Implement authentication, MFA, secure access to assets/applications/cloud
3. **Customer IAM**
4. **Privileged Access Management (PAM):** CyberArk PAM tool

---

## Privileged Access Management (PAM)
- Privileged accounts can change/impact business operations ("keys to the kingdom")
    - Examples: Windows administrator, UNIX root
- 80% of compromised data is due to misconfigured privileged accounts

### Privilege Lifecycle
1. Penetration
2. Credential theft
3. Reconnaissance
4. Lateral movement
5. Privilege escalation
6. Repeat

### Protection, Detection, Response
- **Proactive Protection:** Secured credentials, authorized users, accountability, session isolation, limited privilege scope
- **Targeted Detection:** Continuous monitoring, detect malicious/high-risk behavior, alerts
- **Real-Time Response:** Full forensic monitoring

#### CyberArk Tool Components
- **Digital Vault:** Secure server for privileged account info
- **Password Vault Web Access**
- **Central Policy Manager (CPM)**
- **Privileged Session Manager (PSM)**

---

## Access Management - OKTA
- Aids in access management

### Features
- Single sign-on
- Universal directory
- Directory integrations
- MFA
- Lifecycle management
- Governance and access management

### Use Cases
- Application integrations
- User profiles
- MFA
- Different policies

---

## Data Protection and Security (Kasthuri)

### Agenda
- Data security overview
- Discovery and classification
- PKI and certificate management
- Data protection and privacy
- Key and secret management
- Data activity monitoring
- Future scope in DPP

### Cognizant Data Privacy and Protection - Solution Offering
- **Discover & Classify:** Data discovery, data classification
- **Protect:** Data anonymization, encryption (at rest & transit), keys/secrets management, IRM/DRM
- **Detect, Monitor, Respond & Recover:** Data activity monitoring, data leak prevention, data access governance, incident response management

### Data Classification
- Sensitive data
- Classified data
- Proprietary data
- Public data

### Security Layers
- Critical assets
- Data
- Application
- Endpoint
- Network
- Perimeter
- Human

### Sensitive Data Types
- **Personal info:** Names, addresses, social security numbers, financial data
- **Medical info:** Health records, diagnosis
- **Intellectual property:** Trade secrets, patents, copyrights
- **Government data:** Classified info, national security secrets

### Key Functional Areas of Data Protection & Privacy
- **Detect:** Discover, classify, label, assess risk (structured, semi-structured, unstructured data)
- **Protect:** Encryption, tokenization, masking, anonymization (data in transit, rest, use)
- **Govern:** Activity monitoring, access control, privilege audit, compliance adherence

### IT Compliance Requirements
- **Financial Data:** PCI DSS, SWIFT CSP, Sarbanes-Oxley Act (SOX)

### Technical Workflow
- Data discovery → Automated scanning → Pattern matching → Metadata analysis
- Data classification → Email address → Financial/PII → Credit card → Labels

#### Steps
1. Identify sensitive data
2. Classify and categorize sensitive data
3. Apply data protection controls

### Data Protection & Privacy Techniques
- Encryption
- Format-preserving encryption
- Tokenization
- Masking
- Hashing

### Key Lifecycle Management
- Creation
- Backup
- Deployment
- Monitoring
- Rotation
- Expiration
- Archival
- Destruction

### Federal Info Processing Standards
- Level 1: Use encryption
- ... up to Level 5

### Secret Management
- Centralized key management system for keys and OTPs

#### How It Works
1. Enable the database secrets engine
2. Configure the secrets engine
3. Create a vault role
4. Generate database credentials


---


##  **DATA PROTECTION AND PRIVACY**

---

### 🛡️ **Data Protection & Privacy**  
**Definition**:  
The practice of securing sensitive data from unauthorized access or misuse, while ensuring individuals’ privacy rights.  
It involves encryption, access control, and compliance with laws like GDPR and HIPAA.  
Focuses on data at rest, in transit, and in use.  
Drives both technical and legal frameworks for data security.

**Key Takeaways**:  
- Use encryption (AES, TLS) for protection.  
- Ensure compliance with regulations (GDPR, CCPA).  
- Data must be protected across all states: rest, transit, use.  
- Privacy enforces rights like consent and access control.

---

### 🔐 **Cryptography – Data Protection**  
**Definition**:  
Secures data through algorithms that transform it into unreadable formats.  
Includes encryption, decryption, hashing, and digital signatures.  
Used to protect confidentiality, integrity, and authentication.  
Two main types: symmetric (same key) and asymmetric (public/private key).

**Key Takeaways**:  
- **AES** for symmetric encryption, **RSA/ECC** for asymmetric.  
- **Hashing** (e.g., SHA-256) for data integrity.  
- TLS uses both symmetric & asymmetric encryption.  
- Foundation for secure communication and data storage.

---

### 🔍 **Data Discovery & Classification**  
**Definition**:  
Identifies where sensitive or regulated data (like PII, PCI, PHI) is stored.  
Applies classifications like confidential, internal, or public.  
Essential for risk management, compliance, and automated protection.  
Uses tools to tag, label, and act on data types.

**Key Takeaways**:  
- You can’t protect what you don’t know exists.  
- Enables policy-based controls (masking, encryption).  
- Tools: Azure Purview, AWS Macie, IBM Guardium.  
- Supports audits and regulatory requirements.

---

### 🧾 **Introduction to Public Key Infrastructure (PKI)**  
**Definition**:  
PKI uses digital certificates to secure identities and data through asymmetric encryption.  
Enables trust in digital communications and transactions.  
Operates on a trust hierarchy of Certificate Authorities (CAs).  
Core to HTTPS, email encryption, and digital signatures.

**Key Takeaways**:  
- **Public/private keys** manage identity and secure exchange.  
- Certificates issued and validated by **CAs**.  
- Supports digital signatures and encryption.  
- Enables secure authentication and trust models.

---

### 🏗️ **PKI Architecture Overview & Deployment**  
**Definition**:  
Describes the structure and components of PKI: Root CA, Intermediate CA, OCSP, CRLs, etc.  
Guides implementation for secure issuance and management of certificates.  
Addresses scalability, automation, and security (e.g., using HSMs).  
Used internally (enterprise) or externally (public trust).

**Key Takeaways**:  
- Trust hierarchy: Root → Intermediate → End Entity.  
- Certificate validation via **CRL/OCSP**.  
- Automate cert renewal with tools like Let’s Encrypt.  
- Store private keys securely with HSMs.

---

### 🔧 **OpenSSL**  
**Definition**:  
A powerful open-source toolkit for implementing SSL/TLS and performing cryptographic operations.  
Used to generate private keys, CSRs, certificates, and test secure connections.  
Widely used in web servers, VPNs, and testing environments.  
Command-line tool for security practitioners and devs.

**Key Takeaways**:  
- Generate key: `openssl genrsa -out key.pem 2048`  
- Create CSR: `openssl req -new -key key.pem -out csr.pem`  
- View cert: `openssl x509 -in cert.pem -text`  
- Essential for manual cert management and testing.

---

### 🔑 **Key Lifecycle Management Basics**  
**Definition**:  
Covers secure handling of encryption keys throughout their lifecycle: creation to destruction.  
Ensures keys are rotated, revoked, and stored properly.  
Protects against data breaches from key misuse.  
Implemented using HSMs or cloud key vaults.

**Key Takeaways**:  
- Phases: Generate → Store → Rotate → Revoke → Destroy.  
- Keys must be encrypted at rest and in transit.  
- HSMs and vaults (Azure/AWS) manage this process.  
- Automation reduces human error and enhances compliance.

---

### ☁️ **Azure Key Vault Basics**  
**Definition**:  
A cloud-based service for managing keys, secrets, and certificates in Azure securely.  
Supports role-based access and integration with Azure services.  
Automates secret rotation and versioning.  
Prevents hardcoding secrets in apps.

**Key Takeaways**:  
- Store secrets, keys, and certs securely.  
- Use RBAC and managed identities.  
- Supports logging, monitoring, and alerting.  
- Centralized control over sensitive info.

---

### ☁️ **AWS KMS Basics**  
**Definition**:  
AWS Key Management Service handles encryption key generation, storage, and use across AWS.  
Supports envelope encryption and tight integration with AWS services.  
Offers automatic key rotation and audit logs.  
Can use AWS-managed or customer-managed keys.

**Key Takeaways**:  
- Manages symmetric/asymmetric encryption keys.  
- Integrates with S3, EBS, RDS, Lambda, etc.  
- Supports access control via IAM policies.  
- Key usage is logged in AWS CloudTrail.

---

### 🕵️‍♂️ **Data Activity Monitoring (DAM)**  
**Definition**:  
Monitors who accesses what data, when, and how.  
Detects anomalous or unauthorized activity in real-time.  
Supports compliance and threat detection.  
Feeds alerts to SIEM systems.

**Key Takeaways**:  
- Tracks user actions on sensitive data.  
- Helps meet audit and compliance goals.  
- Can detect insider threats or data leaks.  
- Used across databases, file systems, and cloud apps.

---

### 🧠 **IBM Guardium – Data Activity Monitoring**  
**Definition**:  
An enterprise-grade platform for monitoring, auditing, and protecting sensitive data.  
Supports multiple DBs and platforms, on-prem and cloud.  
Provides real-time alerts, masking, and policy enforcement.  
Used to meet regulatory and security objectives.

**Key Takeaways**:  
- Tracks and logs data access events.  
- Performs vulnerability assessments.  
- Integrates with SIEM and compliance tools.  
- Enables data-centric security across hybrid environments.

---
80/20
---

### 🛡️ 1. **Core of Data Protection & Privacy**
- **Goal**: Protect data **at rest**, **in transit**, and **in use** from unauthorized access, modification, or destruction.
- **Privacy** ensures that personal data is handled according to regulations (e.g., GDPR, HIPAA).

#### Must-Know:
- **Data at rest**: Use encryption (e.g., AES-256).
- **Data in transit**: Use TLS (HTTPS).
- **Data in use**: Use secure enclaves or runtime protections.
- **Regulations**: Understand GDPR, CCPA, etc., and how they influence data practices.

---

### 🔐 2. **Cryptography for Data Protection**
- **Symmetric encryption** (same key for encrypt/decrypt): Fast (e.g., AES).
- **Asymmetric encryption** (public/private keys): Used for secure key exchange and digital signatures (e.g., RSA, ECC).

#### Must-Know:
- **AES**: Standard for encrypting data.
- **RSA/ECC**: Used in digital certificates and key exchange.
- **Hashing**: Ensures data integrity (e.g., SHA-256).

---

### 🔍 3. **Data Discovery & Classification**
- **Purpose**: Identify **where sensitive data resides** and label it appropriately (e.g., PII, PCI, PHI).
- **Why it matters**: You can’t protect what you don’t know you have.

#### Must-Know:
- Tools like **Azure Purview**, **AWS Macie**, or **IBM Guardium** help automate this.
- Classifications trigger policy enforcement (e.g., encryption, masking).

---

### 🧾 4. **Public Key Infrastructure (PKI) Overview**
- **Purpose**: Trust model that manages keys and digital certificates for secure communication.

#### Must-Know:
- **Certificate Authority (CA)**: Issues and verifies digital certificates.
- **Digital Certificate**: Binds a public key to an identity.
- **Trust Chain**: Root CA > Intermediate CA > End Entity Cert.

---

### 🏗️ 5. **PKI Architecture & Deployment**
- **Components**:
  - Root & Intermediate CAs
  - Certificate Revocation Lists (CRL)
  - Online Certificate Status Protocol (OCSP)
- **Deployment Tips**:
  - Use hardware security modules (HSMs).
  - Automate cert renewal (e.g., Let's Encrypt + ACME protocol).

---

### 🔧 6. **OpenSSL**
- **Tool** for managing certs, keys, and crypto ops.

#### Must-Know Commands:
- Generate private key: `openssl genrsa -out key.pem 2048`
- Create CSR: `openssl req -new -key key.pem -out csr.pem`
- View cert: `openssl x509 -in cert.pem -text`

---

### 🔑 7. **Key Lifecycle Management (KLM)**
- **Phases**:
  1. Key generation
  2. Distribution
  3. Rotation
  4. Revocation
  5. Destruction

#### Must-Know:
- Keys should be rotated regularly and securely stored.
- Use **HSMs** or **cloud key vaults** for security.

---

### ☁️ 8. **Azure Key Vault & AWS KMS**
- Both are **cloud-native key management** services.

#### Azure Key Vault:
- Stores secrets, keys, and certs securely.
- Integrates with RBAC & managed identities.

#### AWS KMS:
- Centralized key mgmt with tight integration to AWS services.
- Uses customer-managed or AWS-managed keys.

---

### 🕵️‍♂️ 9. **Data Activity Monitoring (DAM)**
- **Why**: Detect and alert on suspicious access patterns or data exfiltration.
- **Tools**: IBM Guardium, Imperva, native cloud solutions.

#### Must-Know:
- Tracks **who accessed what**, **when**, and **how**.
- Often integrated with SIEM systems for correlation & alerting.

---

### 🧠 10. **IBM Guardium Overview**
- Enterprise DAM solution.
- Can monitor databases (Oracle, SQL Server, DB2, etc.)
- Features: Vulnerability assessment, real-time monitoring, data masking, policy-based alerts.

---

## ⚡ TL;DR Summary:
| Area | What to Remember |
|------|------------------|
| Encryption | AES (symmetric), RSA/ECC (asymmetric), TLS for data in transit |
| PKI | Trust model for certs, CAs issue & manage certs |
| Key Mgmt | Use vaults (Azure Key Vault, AWS KMS), manage lifecycle |
| Data Discovery | Classify & protect sensitive data automatically |
| Monitoring | Use DAM tools (IBM Guardium) to detect data misuse |
| Tools | Learn basic OpenSSL commands for hands-on |

---


---

### **1. Cloud Security Fundamentals (Azure)**
   - **Shared Responsibility Model**: Understand what security responsibilities lie with the cloud provider vs. the customer.
   - **IAM (Identity & Access Management)**: Role-based access control (RBAC), least privilege principle.
   - **Data Protection**: Encryption (at rest & in transit), key management in Azure Key Vault.
   - **Networking in Cloud**: Virtual Networks (VNets), Network Security Groups (NSG), and Private Endpoints.
   - **Cloud Security Posture Management (CSPM)**: Tools like Microsoft Defender for Cloud to monitor cloud security risks.

### **2. Firewall & Web Application Firewall (WAF) (Palo Alto)**
   - **Traditional Firewalls vs. Next-Gen Firewalls (NGFWs)**: Deep Packet Inspection, Application Layer Filtering.
   - **WAF Protection**: Defends against SQL injection, XSS, CSRF attacks.
   - **Zero Trust Policy**: Implementing least privilege access and segmentation.

### **3. Intrusion Detection & Prevention (IDS/IPS) (Zscaler SASE)**
   - **Difference between IDS & IPS**: IDS detects threats, IPS blocks them.
   - **Anomaly-Based vs. Signature-Based Detection**: How threats are identified.
   - **SASE (Secure Access Service Edge)**: Merging network security with cloud-delivered services.

### **4. Proxy, VPN & Secure Access (Zscaler)**
   - **VPN vs. Zero Trust Network Access (ZTNA)**: VPNs create private tunnels; ZTNA authenticates users dynamically.
   - **Secure Web Gateway (SWG)**: Filters internet traffic to prevent malicious sites.
   - **Cloud Proxy Services**: How Zscaler inspects encrypted traffic to prevent threats.

### **5. Endpoint & Email Security (Microsoft Defender XDR)**
   - **Endpoint Detection & Response (EDR)**: Behavioral analytics and automated response.
   - **Phishing & Business Email Compromise (BEC) Defense**: AI-based email filtering, DKIM, SPF, DMARC.
   - **Malware Sandboxing**: Isolating suspicious files before execution.

### **6. Security Information & Event Management (SIEM) & Security Operations Center (SOC) (Splunk)**
   - **SIEM vs. SOC**: SIEM aggregates logs; SOC actively monitors & responds.
   - **Threat Intelligence & Correlation**: Using SIEM rules to detect anomalies.
   - **Incident Response Playbooks**: Standard procedures for security events.

### **7. Cloud Computing in Business Scenarios**
   - **Understanding Multi-Cloud & Hybrid Cloud Security**.
   - **Compliance & Regulations**: GDPR, HIPAA, and SOC 2.
   - **Real-World Attacks**: Case studies of cloud breaches and lessons learned.

        
________________________________________________________________

#
                        
### **1. Cloud Security Fundamentals (Azure)**  
Cloud security is built on the **Shared Responsibility Model**, where cloud providers secure infrastructure, but customers must protect their data, identities, and applications. **Identity & Access Management (IAM)** enforces role-based access control (**RBAC**) and the principle of least privilege to minimize risk. Data security relies on **encryption (at rest and in transit)**, with services like **Azure Key Vault** managing cryptographic keys securely. Cloud networks are safeguarded using **Virtual Networks (VNets), Network Security Groups (NSG), and Private Endpoints**, restricting unauthorized access. Security monitoring tools like **Microsoft Defender for Cloud** continuously scan for misconfigurations and threats to maintain compliance and reduce attack surfaces.  

### **2. Firewall & Web Application Firewall (WAF) (Palo Alto)**  
Traditional firewalls control network traffic using **IP addresses and port filtering**, but **Next-Generation Firewalls (NGFWs)** add **deep packet inspection, application-level filtering, and threat intelligence** to detect modern attacks. A **Web Application Firewall (WAF)** protects web applications by filtering and monitoring **HTTP traffic** to block **SQL injection, Cross-Site Scripting (XSS), and Cross-Site Request Forgery (CSRF)** attacks. Implementing a **Zero Trust** approach ensures that all traffic is continuously verified before granting access, preventing unauthorized access and lateral movement within a network.  

### **3. Intrusion Detection & Prevention (IDS/IPS) (Zscaler SASE)**  
Intrusion Detection Systems (**IDS**) monitor network traffic for suspicious activity and alert administrators, while **Intrusion Prevention Systems (IPS)** actively block identified threats. **Signature-based detection** relies on known attack patterns, whereas **anomaly-based detection** flags deviations from normal behavior. The **Secure Access Service Edge (SASE)** model integrates **network security with cloud-based services**, ensuring secure remote access without traditional network constraints. By combining **firewall, SWG, CASB, ZTNA, and SD-WAN**, SASE enhances security while maintaining performance for distributed workforces.  

### **4. Proxy, VPN & Secure Access (Zscaler)**  
Proxies and VPNs secure internet access and remote connectivity, but traditional **VPNs** often grant excessive access, increasing the risk of lateral movement attacks. **Zero Trust Network Access (ZTNA)** improves security by verifying users and devices before granting access, ensuring minimal privileges. **Secure Web Gateways (SWG)** filter web traffic, blocking malicious sites and enforcing compliance policies. **Cloud proxies**, like **Zscaler Internet Access (ZIA)**, inspect encrypted traffic to detect malware, preventing unauthorized data exfiltration while enabling safe cloud usage.  

### **5. Endpoint & Email Security (Microsoft Defender XDR)**  
Endpoints are a prime target for cyberattacks, making **Endpoint Detection & Response (EDR)** essential for identifying and mitigating threats in real time. **Microsoft Defender XDR** leverages **behavioral analytics and AI** to detect suspicious activity across devices, applications, and identities. **Email security** is crucial for preventing **phishing, Business Email Compromise (BEC), and malware attacks**, using technologies like **DKIM, SPF, and DMARC** for sender authentication. Advanced features like **malware sandboxing** analyze suspicious attachments in an isolated environment before delivering them to end users.  

### **6. SIEM & SOC (Splunk)**  
**Security Information and Event Management (SIEM)** platforms collect and analyze security logs from multiple sources, using correlation rules and threat intelligence to detect attacks. **Splunk** is a leading SIEM solution that helps organizations **identify, investigate, and respond** to security incidents in real-time. The **Security Operations Center (SOC)** is a dedicated team that monitors, investigates, and mitigates threats 24/7, leveraging **incident response playbooks** to contain breaches effectively. Automating **event correlation and anomaly detection** helps security teams stay ahead of evolving cyber threats.  

### **7. Cloud Security in Business**  
As businesses adopt **multi-cloud and hybrid cloud** environments, securing workloads across different cloud providers becomes challenging. Organizations must comply with regulations like **GDPR, HIPAA, and SOC 2** to protect sensitive data and maintain legal compliance. **Cloud security case studies** reveal common attack vectors, such as **misconfigured storage buckets, weak IAM policies, and unpatched vulnerabilities**, emphasizing the need for proactive security measures. **Cloud Security Posture Management (CSPM)** tools continuously monitor configurations to prevent breaches and ensure security best practices are followed.  

