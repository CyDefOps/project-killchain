
  

# Project Killchain [PKC]

  

<img  src="https://img1.wsimg.com/blobby/go/1cf5bcbc-aad3-42e4-a7e0-6c0149aec441/downloads/BG%20Gradient%20(2).png"  width="250"  height="250">

![GitHub last commit (by committer)](https://img.shields.io/github/last-commit/CyDefOps/project-killchain?style=flat-square&color=357441)
![GitHub contributors](https://img.shields.io/github/contributors/CyDefOps/project-killchain?style=flat-square&color=357441)
![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed/cydefops/project-killchain?style=flat-square)
![Website](https://img.shields.io/website?up_message=UP&up_color=357441&down_message=DOWN&down_color=880808&url=https%3A%2F%2Fcydefops.com&style=flat-square)
![PKC Members](https://img.shields.io/badge/PKC%20Members-%20126-357441?style=flat-square)
![PKC Associates](https://img.shields.io/badge/PKC%20Associates-%2067-357441?style=flat-square)

### Project Summary 

  

- **Red Team Resources**

Collection of penetration testing tools, scripts, and techniques for comprehensive vulnerability assessment.

- **Blue Team Resources**

Wide range of tools for incident response, digital forensics, threat hunting, and hardening security infrastructures.

- **IOC Database**

A database of IOCs, which includes but are not limited to IP addresses, domain names, URLs, file hashes, etc., associated with known threat actors and their campaigns.

- **Knowledge Base**

Detailed guides, walkthroughs, and tips related to the latest offensive and defensive cybersecurity tactics, techniques, and procedures (TTPs).

- **Open Source**

Open-source repository welcoming contributions from the community.



# Table of Contents
- [Project Killchain \[PKC\]](#project-killchain-pkc)
- [Table of Contents](#table-of-contents)
- [Contributions](#contributions)
- [IOCs](#iocs)
	- [CrowdStrike Phishing](/IOCs/Crowdstrike_phishing/)
	- [Phishing Websites](/IOCs/Phishing/)
	- [Network Indicators](/IOCs/network-indicators/)
	- [Stealers](#stealers)
		- [Redline](#redline)
		- [Amadey](#amadey)
	- [Loaders](#loaders)
		- [Smoke Loader](#smoke-loader)
		- [Threat Hunts](#threat-hunts)
- [Research](#research)
	- [KillChain Research Papers](/Research/Papers/)
	- [PyPi Research](/Research/PyPi%20Packages/)
- [Scripts](#scripts)
  	- [Azure](https://github.com/CyDefOps/project-killchain/tree/main/Scripts/Azure)
  	  	- [KQL](https://github.com/CyDefOps/project-killchain/tree/main/Scripts/Azure/KQL)
  	- [Investigations](https://github.com/CyDefOps/project-killchain/tree/main/Scripts/Investigations)
  		- [IP Address](https://github.com/CyDefOps/project-killchain/tree/main/Scripts/Investigations/IP%20Address)
  	 		- [AbUserIPDB](https://github.com/CyDefOps/project-killchain/tree/main/Scripts/Investigations/IP%20Address/AbUserIPDB)
	- [Hasher](/Scripts/Investigations/Hasher/)
	- [Matrix](/Scripts/Matrix/)
	- [Synapse](/Scripts/Matrix/Synapse/)
	- [Phishing](https://github.com/CyDefOps/project-killchain/tree/main/Scripts/Phishing)
    	- [Analysis](https://github.com/CyDefOps/project-killchain/tree/main/Scripts/Phishing/Analysis)
  	    	- [WhatThePhish](https://github.com/CyDefOps/project-killchain/tree/main/Scripts/Phishing/Analysis/whatThePhish)
  	    	- [NightOwl](https://github.com/CyDefOps/project-killchain/)
	- [Web Security](#web-security)
		- [Chopper](/Scripts/Web%20Security/Chopper/)
		- [DNS](#dns)
		- [Encoding](#encoding)	
		- [FavBuster](/Scripts/Web%20Security/FavBuster/)
		- [Postman](#postman)
	- [Windows](/Scripts/Windows/)
		- [ADS-Tracer](/Scripts/Windows/ADS-Tracer/)
		- [PowerShell](/Scripts/Windows/PowerShell/)
	- [Reverse Engineering](#reverse-engineering)
 		- [PE Executables](#pe-executables)
   		- [Cryptography](#cryptography)
   			- [Hash Calculation](https://github.com/CyDefOps/project-killchain/)
- [General Resources](/General%20Resources/)
	- [Analyst Tools](/General%20Resources/Analyst%20Tools/)
	- [Command & Control Frameworks](/General%20Resources/C&Cs/)
	- [Certification Organizations](/General%20Resources/Certification%20Organizations/)
	- [Hacking OS](/General%20Resources/Hacking%20OS/)
	- [Living Off The Lands](/General%20Resources/LOLs/)
	- [Packet Analysis](/General%20Resources/Packet%20Analysis/)
	- [Reporting](/General%20Resources/Reporting/)
	- [Reverse Engineering](/General%20Resources/Reverse%20Engineering/)
	- [SIEMs](/General%20Resources/SIEMs/)
- [Reporting](#reporting)
	- [Project KillChain - VAPT Reporting Format](/Reporting/)
- [Community Contributions](https://github.com/CyDefOps/project-killchain/tree/main/Community%20Contributions/)
	- [Articles](/Community%20Contributions/Articles/)
	- [Practical Labs](https://github.com/CyDefOps/project-killchain/tree/main/Community%20Contributions/Practical%20Labs)  
- [Wallpapers](https://github.com/CyDefOps/project-killchain/tree/main/Wallpapers)
	- [Graphic Designs by Project KillChain Contributors](https://github.com/CyDefOps/project-killchain/tree/main/Wallpapers)		 	  
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

<center><img width="632" alt="image" src="https://github.com/CyDefOps/project-killchain/assets/110534650/7ee2781b-9590-4029-aa48-3660de83c145"></center>

Currently the selection of available papers include:

1. [Dissecting Malicious PyPi Packages](https://cydefops.com/dissecting-pypi-packages)
2. [Chinese Scammers Targeting Qatar Residents](https://cydefops.com/chinese-sms-scams-qatar)
3. [Malicious PyPi Packages Leading To Phishing Websites](https://cydefops.com/malicious-pypi-packages)
4. [Malicious PyPi Packages Leading To Phishing Websites - Part 2](https://cydefops.com/malicious-pypi-part-2)
5. [Deconstructing Deception - Cl0p](https://cydefops.com/deconstructing-deception)
6. [VSCode - Forwarded Ports For Data Exfiltration](https://cydefops.com/vscode-data-exfiltration)
7. [Cracking The Code - DevTunnels Unleashed](https://cydefops.com/devtunnels-unleashed)


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

### [Web-Security-Headers](https://github.com/CyDefOps/project-killchain/tree/main/Scripts/Web%20Security/Web-Security-Headers, "PKC Web-Security-Headers,Web-Security-Headers Repo")

Here you'll find scripts geared towards automating the process of validating and verifying HTTP Security Headers in the web application specifically designed for the web application penetration tester and web developers keen towards building safe and secure web applications.

## [Reverse-Engineering]((https://github.com/CyDefOps/project-killchain/tree/main/Scripts/Reverse%20Engineering), "PKC Reverse Engineering, Scripts Repo")

### [PE Executables]((https://github.com/CyDefOps/project-killchain/tree/main/Scripts/Reverse%20Engineering/PE%20Executables/), "PKC Reverse-Engineering PE-Executables, Scripts Repo")

Here you'll find scripts geared towards performing reverse engineering static as well as dynamic based on Microsoft Windows a.k.a PE Executables for all architectures. 


## [Cryptography]((https://github.com/CyDefOps/project-killchain/tree/main/Scripts/Cryptography), "PKC Cryptography, Scripts Repo")

Here you'll find scripts geared towards cryptographic algorithms, encryption & decryption as well as hash calulations etc. 

# [Reporting](https://github.com/CyDefOps/project-killchain/tree/main/Reporting, "Reporting")

Here you'll find `Reporting Formats` created and designed by Project-KillChain Team for community use.

# Project Killchain Team

The Project Killchain Team consists of few cybersecurity practitioners aiming to share knowledge with the community, the team are all volunteers and contribute to this project in their own time, they are:

- [Umar Javed](https://www.linkedin.com/in/ujaved/  "Umar Javed on LinkedIn")

  

Umar is CEO at Cyber Defence Operations (CyDefOps), Director of Security Consulting at Kyndryl and Cyber Special at the UK's National Crime Agency

- [Kamran Saifullah](https://www.linkedin.com/in/kamransaifullah/  "Kamran Saifullah on LinkedIn")

  

Kamran is Lead Security Assessments/DFIR at Commercial Bank of Qatar, Principal Cyber Defence Researcher at CyDefOps, Technical Education Advisory Board at NCFE UK and Lead Maintainer of Project-KillChain.


- [Cam Coller](https://www.linkedin.com/in/cam-str/  "Cam Coller on LinkedIn")

  
Cam is Senior Security Engineer at Komainu, Defensive Security Researcher at Cyber Defence Operations (CyDefOps), Technical Education Advisory Board at NCFE and Lead Maintainer of Project-KillChain.

- [Htet Naing Aung](https://www.linkedin.com/in/hnaung/  "Htet Naing Aung on LinkedIn")

  

Htet is a Principal Security Architect (Global Security & Resiliency) at Kyndryl

----
