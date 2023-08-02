### Project Summary

  

- Red Team Resources: Collection of penetration testing tools, scripts, and techniques for comprehensive vulnerability assessment.

- Blue Team Resources: Wide range of tools for incident response, digital forensics, threat hunting, and hardening security infrastructures.

- IOC Database: A database of IOCs, which includes but are not limited to IP addresses, domain names, URLs, file hashes, etc., associated with known threat actors and their campaigns.

- Knowledge Base: Detailed guides, walkthroughs, and tips related to the latest offensive and defensive cybersecurity tactics, techniques, and procedures (TTPs).

- Open Source: Open-source repository welcoming contributions from the community.

  
  

# Project Killchain [PKC]

  

<img  src="https://supreme.sh/assets/pkc.png"  width="250"  height="250">

  
# Table of Contents
- [Project Killchain \[PKC\]](#project-killchain-pkc)
- [Table of Contents](#table-of-contents)
- [Contributions](#contributions)
- [IOCs](#iocs)
  - [Stealers](#stealers)
		 - [Redline](#redline)
		 - [Amadey](#amadey)
  - [Loaders](#loaders)
		 - [Smoke Loader](#smoke-loader)
- [Threat Hunts](#threat-hunts)
- [Research](#research)
- [Scripts](#scripts)
	- [Web Security](#web-security)
		- [DNS](#dns)
		- [Postman](#postman)
		- [Encoding](#encoding)
	- [Reverse-Engineering](#reverse-engineering)
 		- [PE-Executables](#pe-executables) 
- [Project Killchain Team](#project-killchain-team)

# Contributions

Project Killchain values and appreciates contributions from the cybersecurity community. Feel free to contribute code, share new tools, update our knowledge base, or expand the IOC database. Please review the contributing guidelines before making any contributions.
- Warning, attempts to become a 'contributor' via reusing old code, IOCs or not following the rules will get you blacklisted from contributing to this repo. 

# [IOCs](https://github.com/CyDefOps/project-killchain/tree/main/IOCs  "PKC IOCs Repo")

The IOC Database of Project Killchain is a rich repository of Indicators of Compromise (IOCs) tied to cyber threats. These IOCs, including static indicators:

- IP Addresses

- Domain Names

- URLs

- File Hashes

  

As well as heuristic behavioural patterns, are used to detect and analyze malicious network or system activities linked to known threat actors or campaigns.


<img width="490" alt="image" src="https://github.com/CyDefOps/project-killchain/assets/110534650/b78342e2-257d-4002-a575-3c7a25ea56d6">


<sub>Snap of Amadey IOC dump: 01 Aug 23</sub>

By cross-referencing system or network activities with this database, quick detection and response to threats are facilitated. Constantly updated to tackle evolving threats, this IOC Database is key to understanding threat actors' techniques.

  

-------------

  

### [Stealers](https://github.com/CyDefOps/project-killchain/tree/main/IOCs/stealers  "PKC Stealers Repo")

Stealer malware, or info-stealing malware, is malicious software designed to extract sensitive data like login credentials and credit card details from compromised systems. Project Killchain tracks this malware to proactively identify, analyze, and neutralize threats using Indicators of Compromise (IOCs), which are signs of potential malicious activity. IOCs may include unique malware attributes, communication IP addresses or domains, and suspicious system modifications. This aids in quicker detection, response, and prevention of damage, providing insights for future threat hunting activities.

#### [Redline](https://github.com/CyDefOps/project-killchain/tree/main/IOCs/stealers/redline  "PKC Stealers/Redline Repo")

Redline is a type of information-stealing malware designed to collect sensitive data from infected systems. It operates by extracting browser-based data such as cookies, login credentials, credit card information, and auto-fill form data. Notorious for its user-friendly interface and inexpensive cost on the dark web, Redline has gained popularity among cybercriminals. The malware employs advanced evasion techniques to avoid detection by standard antivirus software, making it a significant threat to personal and organizational cybersecurity.

#### [Amadey](https://github.com/CyDefOps/project-killchain/tree/main/IOCs/stealers/amadey "PKC Stealers/Amadey Repo")

Amadey is a simple yet effective trojan used primarily for reconnaissance in cyberattack operations. It's known for its "as-a-service" model on underground markets, where it's often bought by less technically skilled cybercriminals. Once deployed, Amadey scans the infected system, collecting information such as system settings, installed programs, and running processes. This gathered data helps threat actors to understand the landscape of the compromised system and plan subsequent, more sophisticated attacks. Its simplicity and stealth make Amadey a widely used tool in the initial stages of many cybercrime campaigns.

  

-------------

  

### [Loaders](https://github.com/CyDefOps/project-killchain/tree/main/IOCs/loaders  "PKC Loaders Repo")

Loader malware is a category of malicious software designed to download and install additional malware onto a compromised system. Often used as the initial stage of a multi-tier attack, loaders enable threat actors to deploy a variety of secondary payloads, such as ransomware, banking trojans, or info-stealers, depending on their objectives. With their ability to bypass detection mechanisms and regularly update payloads, loaders present a dynamic and ongoing threat to cybersecurity.

##### [Smoke Loader](https://github.com/CyDefOps/project-killchain/tree/main/IOCs/loaders/smoke_loader  "PKC Loaders/Smoke Loader Repo")

Smoke Loader is a notorious loader malware that's been in the cyber threat landscape for several years. It's used primarily to download and install additional malware onto infected systems, effectively acting as a gateway for more destructive attacks. Smoke Loader is known for its robust evasion techniques, which include code obfuscation and living-off-the-land tactics, where it leverages legitimate system processes to hide its activities. Its persistent presence and adaptability to new defensive measures make Smoke Loader a significant and continuous threat.

  
  

# [Threat Hunts](https://github.com/CyDefOps/project-killchain/tree/main/Threat%20Hunts  "PKC Threat Hunts Repo")

The Threat Hunting Repository in Project Killchain serves as a structured collection of resources, methodologies, tools, and techniques to assist in the proactive search for potential threats within a network. This repository could include:

  

- TTPs (Tactics, Techniques, and Procedures): Detailed descriptions and examples of the methods used by threat actors to infiltrate and exploit networks. This helps threat hunters to anticipate and counteract malicious activities.

  

- Hunting Queries: Pre-defined search queries for popular security tools and platforms, such as Splunk or Microsoft Security, that can help in spotting anomalies or suspicious patterns.

  

- Analytical Tools: References to, or scripts for, various tools used in the threat hunting process. This could involve data aggregation, pattern recognition, and anomaly detection tools.

  

- Hunting Procedures: Methodologies and best practices for conducting threat hunts, including advice on structuring hunts, prioritizing resources, and effectively communicating findings.

  

- Case Studies: Detailed examples of previous successful threat hunts, providing practical examples and lessons learned.

<img width="816" alt="image" src="https://github.com/CyDefOps/project-killchain/assets/110534650/0ecbfc22-da1d-4160-8d86-8542a894e784">


<sub>PKC - Abnormal Scheduled Task Creation, via Stealer Malware IOCs</sub>

The aim of the Threat Hunting Repository is to equip security teams with the necessary resources to proactively find, isolate, and neutralize threats before they result in a security breach.


# [Research](https://github.com/CyDefOps/project-killchain/tree/main/Research "PKC Research Repo")

The Research Repository in Project Killchain acts as the releases of curated intelligence from the Cyber Defence Operations (cydefops.com) team. 

<img width="632" alt="image" src="https://github.com/CyDefOps/project-killchain/assets/110534650/7ee2781b-9590-4029-aa48-3660de83c145">


<sub>Deconstructing Deception - cl0p</sub>

Currently the selection of available papers include:
1. [Dissecting Malicious PyPi Packages](https://cydefops.com/dissecting-pypi-packages)
2. [Chinese Scammers Targeting Qatar Residents](https://cydefops.com/chinese-sms-scams-qatar)
3. [Malicious PyPi Packages Leading To Phishing Websites](https://cydefops.com/malicious-pypi-packages)
4. [Malicious PyPi Packages Leading To Phishing Websites - Part 2](https://cydefops.com/malicious-pypi-part-2)
5. [Deconstructing Deception - Cl0p](https://cydefops.com/deconstructing-deception)


# [Scripts](https://github.com/CyDefOps/project-killchain/tree/main/Scripts "PKC Scripts Repo")

The Scripts repository in Project Killchain is a collection of scripts for time-saving whether in automation, security, forensics, or red teaming, you can find many categories of useful scripts here. Currently, the scripts here are made by us, if they are not this will be disclosed.

## [Web Security](https://github.com/CyDefOps/project-killchain/tree/main/Scripts/Web%20Security "PKC Web-Security, Scripts Repo")

This repository contains scripts for various aspects of web security, aiding in automating vulnerability assessment, security checks, and other essential tasks.

###  [DNS](https://github.com/CyDefOps/project-killchain/tree/main/Scripts/Web%20Security/DNS "PKC Web-Security DNS, Scripts Repo")

This folder contains scripts for handling DNS-related security tasks, including monitoring DNS traffic, conducting reconnaissance, and improving DNS configuration security.

<img width="505" alt="image" src="https://github.com/CyDefOps/project-killchain/assets/110534650/96a424e9-d87f-4fb0-968e-0819bcffebbf">


<sub>LazyDNS, by Kamran Saifullah</sub>

### [Postman](https://github.com/CyDefOps/project-killchain/tree/main/Scripts/Web%20Security/Postman, "PKC Web-Security Postman, Scripts Repo")

Here you'll find scripts geared towards Postman, useful for automating API testing, managing mock servers, and enhancing the overall efficiency of API development.

### [Encoding](https://github.com/CyDefOps/project-killchain/tree/main/Scripts/Web%20Security/Encoding, "PKC Web-Security Encoding, Scripts Repo")

Here you'll find scripts geared towards automating the process of encoding a wide range of encoding algorithms for CTI, Red Teaming, Penetration Testing etc. 

## [Reverse-Engineering](https://github.com/CyDefOps/project-killchain/tree/main/Scripts/Web%20Security](https://github.com/CyDefOps/project-killchain/tree/main/Scripts/Reverse%20Engineering), "PKC Reverse Engineering, Scripts Repo")

### [PE Executables](https://github.com/CyDefOps/project-killchain/tree/main/Scripts/Web%20Security/Encoding](https://github.com/CyDefOps/project-killchain/tree/main/Scripts/Reverse%20Engineering/PE%20Executables/), "PKC Reverse-Engineering PE-Executables, Scripts Repo")

Here you'll find scripts geared towards performing reverse engineering static as well as dynamic based on Microsoft Windows a.k.a PE Executables for all architectures. 

# Project Killchain Team

The Project Killchain Team consists of few cybersecurity practitioners aiming to share knowledge with the community, the team are all volunteers and contribute to this project in their own time, they are:

- [Umar Javed](https://www.linkedin.com/in/ujaved/  "Umar Javed on LinkedIn")

  

Umar is CEO at Cyber Defence Operations (CyDefOps), Cyber Threat Hunter at Kyndryl and Cyber Special at the UK's National Crime Agency

- [Kamran Saifullah](https://www.linkedin.com/in/kamransaifullah/  "Kamran Saifullah on LinkedIn")

  

Kamran is Manager of Security Assessments and DFIR at Commercial Bank, Principal Cyber Defence Researcher at Cyber Defence Operations (CyDefOps) AND Senior Mentor & Volunteer for ThincsCorp Internship Program (Community Welfare)

- [Htet Naing Aung](https://www.linkedin.com/in/hnaung/  "Htet Naing Aung on LinkedIn")

  

Htet is a Principal Security Architect (Global Security & Resiliency) at Kyndryl

- [Cam Coller](https://www.linkedin.com/in/cam-str/  "Cam Coller on LinkedIn")

  

Cam is Security Operations Manager at Snowplow Analytics, Offensive Security Researcher at Cyber Defence Operations (CyDefOps) and Technical Advisory Board at NCFE

----
