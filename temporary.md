# Intrusion Detection Unit Test Answers (13 marks)



---

## **1. Taxonomy of IDS**

Intrusion Detection Systems (IDS) can be classified using four key dimensions:

### **a) Audit Source Location (E-box Focus)**

* **Host-Based IDS (HIDS):** Analyzes audit logs from a single host (e.g., C2 audit trails). Monitors system files, user activity, and application logs.
* **Network-Based IDS (NIDS):** Monitors real-time network traffic using packet sniffers. Deployed at network chokepoints.
* **Application-Based IDS (APIDS):** Targets logs and behaviors of specific applications like web or database servers.

### **b) Detection Method (A-box Focus)**

* **Misuse-Based Detection:** Uses known attack signatures. Effective against known threats but fails against new (zero-day) attacks.
* **Anomaly-Based Detection:** Flags deviations from baseline behavior. Can detect unknown attacks but has higher false positive rates.

### **c) Detection Frequency (Usage Frequency)**

* **Real-Time IDS:** Continuously analyzes live data (suitable for NIDS). Enables immediate response.
* **Batch/Offline IDS:** Analyzes logs periodically. Suited for historical forensics or environments with limited resources.

### **d) Behavior on Detection (R-box Focus)**

* **Passive IDS:** Generates alerts and logs incidents for human intervention.
* **Active IDS (IPS):** Automatically initiates responses (e.g., blocking IPs, killing processes) upon detecting an intrusion.

---

## **2. Types of Intrusions, Threats, and Intruder Behavior**

### **a) Types of Intrusions**

* **Remote-to-Local (R2L):** Unauthorized remote access to a local system (e.g., password guessing).
* **User-to-Root (U2R):** A local user escalates privileges to gain root access.
* **Denial of Service (DoS):** Overwhelming a service to make it unavailable.
* **Probing/Scanning:** Gathering information via port scans, etc.
* **Malware Intrusions:** Via trojans, worms, viruses.

### **b) Threat Actors / Intruders**

* **Masquerader:** External attacker using stolen credentials.
* **Misfeasor:** Insider misusing their legitimate access.
* **Clandestine User:** Gains supervisory control and disables security mechanisms.

### **c) Intruder Behavior Pattern**

Typical stages:

1. **Reconnaissance:** Scanning networks (e.g., Nmap).
2. **Exploitation:** Gaining unauthorized access.
3. **Privilege Escalation:** Moving from user to admin.
4. **Persistence:** Installing rootkits or backdoors.
5. **Covering Tracks:** Modifying or deleting logs.

#### **Example:**

An attacker gains access to a web server using an SQL injection (R2L), escalates privileges via a kernel exploit (U2R), installs a sniffer, and exports credit card data.

---

## **3. CIDF Architecture and Component Roles**

### **Common Intrusion Detection Framework (CIDF)**

CIDF standardizes IDS component interaction to facilitate scalability, interoperability, and modular design. It comprises:

### **a) E-Box (Event Box)**

* Captures raw audit data (e.g., logs, network packets).
* Filters and converts data into usable events for analysis.

### **b) A-Box (Analysis Box)**

* Analyzes events from the E-box.
* Can use misuse detection (signatures) or anomaly detection (behavior).
* Generates alarms and higher-level events.

### **c) D-Box (Database Box)**

* Stores audit logs, intrusion signatures, and behavior profiles.
* Used for training anomaly detectors and forensic investigations.

### **d) R-Box (Response Box)**

* Takes action based on alerts from the A-box.
* Can be passive (alerts/logs) or active (blocking traffic, resetting connections).

### **Collective Contribution to Intrusion Response**

* **E-Box** detects raw activity → **A-Box** interprets it → **D-Box** provides historical or signature context → **R-Box** acts.
* This modular setup ensures flexibility, real-time response, and robust post-attack analysis.

---

## **4. Anomaly Detection vs. Misuse Detection in Modern IDS**

| Feature       | **Anomaly Detection**                           | **Misuse Detection**                           |
| ------------- | ----------------------------------------------- | ---------------------------------------------- |
| **Approach**  | Learns normal behavior and flags deviations     | Uses known attack patterns (signatures)        |
| **Strengths** | Detects unknown (zero-day) attacks              | Accurate for known threats                     |
| **Drawbacks** | High false positives, requires training data    | Cannot detect novel attacks                    |
| **Tools**     | Often AI/ML based (e.g., unsupervised learning) | Rule-based engines like Snort                  |
| **Best Use**  | Dynamic environments where user behavior varies | Static environments with known threat patterns |

### **Evaluation in Modern Context:**

* **Hybrid Systems (e.g., Suricata, Snort with anomaly plugins)** combine both methods for increased coverage.
* Anomaly detection is increasingly augmented by **machine learning** to reduce false alarms.
* Misuse detection remains essential for compliance and rapid response to known threats.

---

## **Conclusion**

A strong IDS involves a comprehensive taxonomy, awareness of intruder behavior, a modular CIDF architecture, and balanced detection strategies. The integration of anomaly and misuse detection enhances the ability to detect both known and unknown threats, while component-based designs (CIDF) ensure scalability and flexibility in deployment.

---
