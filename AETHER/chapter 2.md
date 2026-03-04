
# **CHAPTER 2 – LITERATURE SURVEY**

---

## **2.1 Introduction to Literature Review**

With the increasing complexity of cyber threats, research in cybersecurity has expanded toward automation, intelligence, and adaptability. Traditional penetration testing and vulnerability assessment approaches often rely on manual intervention and static rules, which limits their effectiveness against dynamic and evolving attack surfaces. Recent studies explore the use of artificial intelligence, graph-based models, and knowledge-driven frameworks to improve security assessment, attack path identification, and threat detection.

This literature review analyzes existing research works related to automated penetration testing, attack path modeling, AI-driven threat detection, and cyber resilience. The limitations of these approaches are identified, and the need for an integrated AI-enhanced threat enumeration and reconnaissance platform is established.

---

## **2.2 Existing Solutions**

### **Paper 1: GAT-APG – Graph Attention Network-Based Attack Path Generation** [1]

**Description:**
This paper proposes a Graph Attention Network (GAT) model to generate attack paths for security simulation by analyzing relationships between vulnerabilities and system components.

**Limitation:**
The approach relies on predefined system graphs and is primarily simulation-based, lacking real-time reconnaissance and early-stage threat enumeration.

**Solution Provided by AETHER:**
AETHER dynamically constructs threat graphs using live reconnaissance data, enabling real-time threat enumeration before attack path prioritization.

---

### **Paper 2: SPGNN-API – Transferable Graph Neural Network for Attack Path Identification** [2]

**Description:**
This work introduces a transferable GNN model to identify attack paths and support autonomous mitigation across different environments.

**Limitation:**
The system assumes the availability of structured attack graphs and focuses mainly on attack path identification rather than holistic security assessment.

**Solution Provided by AETHER:**
AETHER automates the generation of threat graphs directly from reconnaissance outputs, removing dependency on pre-existing structured graphs.

---

### **Paper 3: Cyber-Security Knowledge Graph Generation by Hierarchical Nonnegative Matrix Factorization** [3]

**Description:**
This study presents a method for generating cybersecurity knowledge graphs using hierarchical nonnegative matrix factorization techniques.

**Limitation:**
The approach focuses on knowledge representation and does not integrate live reconnaissance or vulnerability enumeration mechanisms.

**Solution Provided by AETHER:**
AETHER integrates knowledge-based reasoning with continuous reconnaissance and enumeration to maintain up-to-date security intelligence.

---

### **Paper 4: AIPenTool – A Unified Approach to Automated Penetration Testing** [4]

**Description:**
This paper proposes an automated penetration testing framework aimed at enhancing network and web application security.

**Limitation:**
The framework relies heavily on predefined testing logic and lacks adaptive intelligence for dynamic attack surfaces.

**Solution Provided by AETHER:**
AETHER emphasizes AI-assisted threat enumeration and contextual prioritization rather than static exploitation workflows.

---

### **Paper 5: Automated Penetration Testing Tool** [5]

**Description:**
This work presents an automated tool for penetration testing that reduces manual effort through scripted vulnerability detection.

**Limitation:**
The tool is rule-based and does not adapt to unknown vulnerabilities or changing system behavior.

**Solution Provided by AETHER:**
AETHER uses AI-driven analysis to prioritize threats dynamically based on reconnaissance data.

---

### **Paper 6: Automated Security Penetration Testing Based on Machine Learning** [6]

**Description:**
This paper applies machine learning techniques to automate penetration testing decisions and improve detection accuracy.

**Limitation:**
The approach requires extensive training data and focuses primarily on exploitation rather than reconnaissance.

**Solution Provided by AETHER:**
AETHER focuses on early-stage reconnaissance and enumeration, reducing dependence on large labeled datasets.

---

### **Paper 7: Automated Penetration Testing Architecture Using Metasploit and OWASP ZAP** [7]

**Description:**
This study integrates Metasploit and OWASP ZAP to automate web application penetration testing.

**Limitation:**
The architecture depends on existing tools and produces large volumes of uncorrelated vulnerability data.

**Solution Provided by AETHER:**
AETHER correlates reconnaissance outputs into structured threat models to reduce alert overload.

---

### **Paper 8: Automated Penetration Testing Based on Adversarial Inverse Reinforcement Learning** [8]

**Description:**
This work applies adversarial inverse reinforcement learning to enable penetration testing systems to learn attack strategies.

**Limitation:**
The model is complex, computationally intensive, and focuses mainly on exploitation strategies.

**Solution Provided by AETHER:**
AETHER applies lightweight AI techniques for prioritization and reasoning rather than exploitation learning.

---

### **Paper 9: Automated Penetration Testing – A Systematic Review** [9]

**Description:**
This paper provides a comprehensive review of automated penetration testing techniques and tools.

**Limitation:**
The review highlights fragmentation and lack of integration among existing solutions.

**Solution Provided by AETHER:**
AETHER provides a unified platform integrating reconnaissance, enumeration, and prioritization.

---

### **Paper 10: Open Source Solutions for Vulnerability Assessment** [10]

**Description:**
This study compares open-source vulnerability assessment tools used in cybersecurity.

**Limitation:**
The tools operate independently and lack intelligent prioritization mechanisms.

**Solution Provided by AETHER:**
AETHER aggregates findings into a unified threat intelligence model.

---

### **Paper 11: Scorpio – Automated Penetration Testing Tool** [11]

**Description:**
This paper presents an automated penetration testing tool integrated with a cyber range.

**Limitation:**
The tool is primarily designed for training environments and lacks real-world adaptability.

**Solution Provided by AETHER:**
AETHER is designed for real-world deployment with dynamic reconnaissance capabilities.

---

### **Paper 12: SoURCERER – Developer-Driven Security Testing Framework** [12]

**Description:**
This framework focuses on developer-driven security testing for Android applications.

**Limitation:**
It is platform-specific and limited to application-level testing.

**Solution Provided by AETHER:**
AETHER adopts a platform-agnostic approach applicable to networks and web applications.

---

### **Paper 13: Parallelized Cyber Reconnaissance Automation** [13]

**Description:**
This study proposes a real-time and scheduled cyber reconnaissance automation framework.

**Limitation:**
The approach lacks intelligent analysis and prioritization of reconnaissance results.

**Solution Provided by AETHER:**
AETHER enhances reconnaissance outputs with AI-driven threat enumeration and prioritization.

---

### **Paper 14: webFuzz – Grey-Box Fuzzing for Web Applications** [14]

**Description:**
This paper introduces a grey-box fuzzing technique for web applications.

**Limitation:**
The approach focuses on input fuzzing and does not provide holistic system-level threat analysis.

**Solution Provided by AETHER:**
AETHER integrates fuzzing outputs into a broader threat enumeration framework.

---

### **Paper 15: B2SMatcher – Fine-Grained Version Identification** [15]

**Description:**
This work focuses on identifying open-source software versions in binary files.

**Limitation:**
The approach is limited to software identification and does not assess exploitability.

**Solution Provided by AETHER:**
AETHER correlates version identification results with known vulnerabilities and attack surfaces.

---

### **Paper 16: Key Vulnerable Nodes Discovery Using Bayesian Attack Subgraphs** [16]

**Description:**
This paper proposes identifying key vulnerable nodes using Bayesian attack subgraphs and clustering.

**Limitation:**
The method requires structured attack graphs and high computational resources.

**Solution Provided by AETHER:**
AETHER builds lightweight dynamic graphs from real-world reconnaissance data.

---

### **Paper 17: Automated Penetration Testing with Multiple Vulnerability Scanners** [17]

**Description:**
This study combines multiple vulnerability scanners to improve detection coverage.

**Limitation:**
Combining scanners increases redundancy and false positives.

**Solution Provided by AETHER:**
AETHER performs intelligent correlation and prioritization to reduce noise.

---

### **Paper 18: AI-Driven Attack Detection for Industrial Control Systems** [18]

**Description:**
This paper applies AI techniques to detect attacks and enhance cyber resilience in ICS environments.

**Limitation:**
The focus is on detection rather than proactive threat enumeration.

**Solution Provided by AETHER:**
AETHER complements detection systems with proactive reconnaissance-driven threat modeling.

---

### **Paper 19: AI-Driven Cybersecurity in IoT – TRIM-SEC Framework** [19]

**Description:**
This framework focuses on adaptive malware detection and lightweight encryption for IoT systems.

**Limitation:**
The approach does not address attack surface enumeration.

**Solution Provided by AETHER:**
AETHER extends AI-driven security by focusing on reconnaissance and threat enumeration.

---

### **Paper 20: AI-Driven Threat Hunting Using CNN-LSTM Models** [20]

**Description:**
This study proposes hybrid CNN-LSTM models for anomaly detection in enterprise networks.

**Limitation:**
The system operates post-compromise and lacks proactive analysis.

**Solution Provided by AETHER:**
AETHER focuses on pre-attack reconnaissance and enumeration.

---

### **Paper 21: Comparative Analysis of Automated and Manual Penetration Testing** [21]

**Description:**
This paper compares automated scanning and manual penetration testing techniques.

**Limitation:**
The study highlights inefficiencies and alert overload in automated tools.

**Solution Provided by AETHER:**
AETHER reduces analyst burden through AI-assisted prioritization.

---

### **Paper 22: Techno-Human Vulnerability Analysis in ICS** [22]

**Description:**
This work analyzes cybersecurity risks considering both technical and human factors.

**Limitation:**
The approach lacks automated threat enumeration mechanisms.

**Solution Provided by AETHER:**
AETHER automates technical threat enumeration to complement human-centric analysis.

---

### **Paper 23: Managing Cyber Harm – Survey of Challenges** [23]

**Description:**
This paper surveys cyber harm management practices and challenges.

**Limitation:**
The study is conceptual and lacks implementation-oriented solutions.

**Solution Provided by AETHER:**
AETHER provides an implementable platform for proactive risk identification.

---

### **Paper 24: Building Cyber-Resilience in Maritime Transport** [24]

**Description:**
This paper examines cyber resilience strategies in maritime transport systems.

**Limitation:**
The work focuses on policy-level mitigation rather than technical enumeration.

**Solution Provided by AETHER:**
AETHER supports technical threat enumeration adaptable to critical infrastructure.

---

### **Paper 25: AgCyRAG – Agentic Knowledge Graph-based RAG Framework** [25]

**Description:**
This framework integrates knowledge graphs and retrieval-augmented generation for security analysis.

**Limitation:**
The approach lacks automated attack surface discovery.

**Solution Provided by AETHER:**
AETHER integrates RAG-based reasoning with continuous reconnaissance and enumeration.

---

## **2.3 Comparative Analysis of Existing Solutions**

Most existing solutions address specific cybersecurity stages such as scanning, detection, or attack path modeling. However, they lack unified integration across reconnaissance, enumeration, and intelligent prioritization.

---

## **2.4 Identified Research Gaps**

The literature indicates a gap in platforms that combine real-time reconnaissance, AI-driven threat enumeration, and contextual prioritization into a single system.

---

## **2.5 Motivation for the Proposed System**

The identified gaps motivate the development of AETHER, an AI-enhanced threat enumeration and reconnaissance platform.

---

## **2.6 Summary of Findings from Literature**

The reviewed works demonstrate advancements in cybersecurity automation but reveal limitations in integration, adaptability, and proactive threat modeling.

---

## **2.7 Chapter Summary**

This chapter analyzed existing cybersecurity solutions individually, identified their limitations, and established the need for an integrated AI-enhanced threat enumeration and reconnaissance platform.

---

If you want, next I can:

* Compress **2.2** without losing marks
* Align **Chapter 3** perfectly with these gaps
* Convert **2.2** into a **table version** (if allowed)
