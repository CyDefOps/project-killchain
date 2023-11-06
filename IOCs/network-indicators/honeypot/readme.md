### Honeypot - Project KillChain
This repository is dedicated to providing an automated live feed of our threat intelligence data, specifically:
- Indicators of Compromise (IOCs)
- Attack Pattern data

All data is gathered from our SSH honeypots. Our honeypots simulate SSH servers and records detailed information about attack patterns, which can be ingested directly into SIEM solutions for real-time security analysis. 

Made with :heart: by [$HELLS](https://github.com/ntwrite).

![PKC](https://img.shields.io/badge/Project-%20Killchain-357441)
![Language](https://img.shields.io/badge/Language-%20Kusto-357441?style=flat-square)
[![TI IOC Automation - FETCH](https://github.com/CyDefOps/project-killchain/actions/workflows/main.yml/badge.svg)](https://github.com/CyDefOps/project-killchain/actions/workflows/main.yml)

<img src="https://camo.githubusercontent.com/1ff5370fbb2b1778bb50775f7a3e06790b6a878343688b9c5151dcbddd5b482a/68747470733a2f2f73757072656d652e73682f6173736574732f706b632e6a7067" width="125" height="125">

## Overview

Our SSH honeypot is built on top of robust open-source security projects and employs various levels of subterfuge to make it indistinguishable from a real SSH server. It captures and parses attack data, presenting clean and structured IOCs.

## IOCs and Data Structure

The IOCs provided here include:

- Timestamps
- Source IP Addresses
- Usernames and Passwords attempted
- SSHHASH
- SSH Client
- Status Returned by Honeypot

Data is structured in a JSON format, with fields corresponding to each type of IOC for easy parsing and ingestion by SIEM systems.

**Example IOC JSON structure:**

```
2023-11-03T12:00:30,43.243.74.20,SSH-2.0-libssh_0.9.6,f555226df1963d1d3c09daf865abdc9a,345gs5662d34,345gs5662d34,failed
2023-11-03T12:00:32,43.243.74.20,SSH-2.0-libssh_0.9.6,f555226df1963d1d3c09daf865abdc9a,root,3245gs5662d34,failed
2023-11-03T12:06:31,31.41.244.61,SSH-2.0-Go,4e066189c3bbeec38c99b1855113733a,crisam,123456,failed
2023-11-03T12:07:35,146.190.149.9,SSH-2.0-libssh_0.9.6,f555226df1963d1d3c09daf865abdc9a,root,Litu@1234,failed
2023-11-03T12:07:36,146.190.149.9,SSH-2.0-libssh_0.9.6,f555226df1963d1d3c09daf865abdc9a,root,3245gs5662d34,succeeded
2023-11-03T12:07:53,43.135.172.223,SSH-2.0-libssh_0.9.6,f555226df1963d1d3c09daf865abdc9a,345gs5662d34,345gs5662d34,failed
2023-11-03T12:07:54,43.135.172.223,SSH-2.0-libssh_0.9.6,f555226df1963d1d3c09daf865abdc9a,root,3245gs5662d34,succeeded
2023-11-03T12:08:12,129.226.208.154,SSH-2.0-libssh_0.9.6,f555226df1963d1d3c09daf865abdc9a,345gs5662d34,345gs5662d34,failed
2023-11-03T12:08:15,129.226.208.154,SSH-2.0-libssh_0.9.6,f555226df1963d1d3c09daf865abdc9a,root,3245gs5662d34,succeeded
2023-11-03T12:08:37,43.156.237.124,SSH-2.0-libssh_0.9.6,f555226df1963d1d3c09daf865abdc9a,345gs5662d34,345gs5662d34,failed
```

## [Attack Pattern](https://github.com/CyDefOps/project-killchain/IOCs/network-indicators/honeypot/attack-pattern)

Attack pattern logs are unlike our standard IOCs, these are for: 

- Security Research

By analysing patterns of commands and methods used in attacks, you can develop a better understanding of attack methodologies, tools, and procedures (TTPs).

- Tracking Threat Groups
  
Identifying patterns specific to certain threat actors can help in tracking their activities across different networks and over time. 

- Incident Response

During or after an incident, these logs can be crucial for understanding what an attacker did, which systems were compromised, and how the attack unfolded.

- Threat Hunting

Proactively searching through networks to detect and isolate advanced threats that evade existing security solutions can be informed by these logs. 

**Example Attack Pattern JSON Structure**
```
    "211.228.195.98": [
        {
            "timestamp": "2023-11-06T07:20:04.287477Z",
            "event": "command_input",
            "input": "./oinasf; dd if=/proc/self/exe bs=22 count=1 || while read i; do echo $i; done < /proc/self/exe || cat /proc/self/exe;",
            "session": "522aa271764c"
        }
    ],
    "49.36.41.217": [
        {
            "timestamp": "2023-11-06T07:26:28.362112Z",
            "event": "command_input",
            "input": "cd ~; chattr -ia .ssh; lockr -ia .ssh",
            "session": "375d1f771868"
        },
```

You may use this to identify various methods used by threat actors to gain persistence and enact lateral movement in an environment following initial access.
### Made with 🫶 by @[ntwrite](https://github.com/ntwrite) and @[KayaSEC](https://github.com/KayaSEC) 
