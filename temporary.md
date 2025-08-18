
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
