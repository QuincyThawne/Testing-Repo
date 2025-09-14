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
