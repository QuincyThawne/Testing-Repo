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
