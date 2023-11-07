### Honeypot - Project KillChain
This repository is dedicated to providing an automated live feed of our threat intelligence data, specifically:
- Indicators of Compromise (IOCs)
- Attack Pattern data

All data is gathered from our SSH honeypots. Our honeypots simulate SSH servers and records detailed information about attack patterns, which can be ingested directly into SIEM solutions for real-time security analysis. 

Made with :heart: by [$HELLS](https://github.com/ntwrite).

![PKC](https://img.shields.io/badge/Project-%20Killchain-357441)
![Language](https://img.shields.io/badge/Language-%20Kusto-357441?style=flat-square)
[![TI IOC Automation - FETCH](https://github.com/CyDefOps/project-killchain/actions/workflows/main.yml/badge.svg)](https://github.com/CyDefOps/project-killchain/actions/workflows/main.yml)

<img src="https://img1.wsimg.com/blobby/go/1cf5bcbc-aad3-42e4-a7e0-6c0149aec441/downloads/BG%20Gradient%20(2).png" width="125" height="125">

## Overview

Our SSH honeypot is built on top of robust open-source security projects and employs various levels of subterfuge to make it indistinguishable from a real SSH server. It captures and parses attack data, presenting clean and structured IOCs.

Using this data, you can ingest inline to your SIEM, cross reference for Threat Hunting or Incident Response or for Detection Engineering enhancements using our Attack Pattern data.

## IOCs and Data Structure 🧙

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

## [Attack Pattern](https://github.com/CyDefOps/project-killchain/IOCs/network-indicators/honeypot/attack-pattern) 🛡️

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
    "159.75.4.174": [
        {
            "timestamp": "2023-11-04T23:00:37.519500Z",
            "event": "command_input",
            "input": "cd ~; chattr -ia .ssh; lockr -ia .ssh",
            "session": "b1efa8762cce"
        },
        {
            "timestamp": "2023-11-04T23:00:38.125037Z",
            "event": "command_input",
            "input": "cd ~ && rm -rf .ssh && mkdir .ssh && echo \"ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr\">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~",
            "session": "b1efa8762cce"
        },
        {
            "timestamp": "2023-11-04T23:00:38.306419Z",
            "event": "file_download",
            "details": "File downloaded: /root/.ssh/authorized_keys (SHA-256: a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2)",
            "session": "b1efa8762cce"
        },
        {
            "timestamp": "2023-11-04T23:01:02.521878Z",
            "event": "command_input",
            "input": "cat /proc/cpuinfo | grep name | wc -l",
            "session": "b1efa8762cce"
        },
```

You may use this to identify various methods used by threat actors to gain persistence and enact lateral movement in an environment following initial access.

## Kusto Ingestion Inline 🤓

### NOTE: For Azure Sentinel/ Advanced Threat Protection (KQL BASED)

Finally, you can also ingest this data inline to Azure Sentinel or ATP, as they are written in Kusto. This will allow you to cross reference any of your logs, to our Threat Intel data with no extra effort required on your part. (I do not recommend doing this in ATP, ATP is not a strong query engine like Sentinel).

```
let pkc_honeypot = (externaldata(ext_iocs: string) [@"https://github.com/CyDefOps/project-killchain/raw/main/IOCs/network-indicators/honeypot/iocs-14d.csv"]
    with (format="txt"))
    | where ext_iocs !startswith "#";
pkc_honeypot
| extend arr_split = tostring(split(ext_iocs,','))
| extend TimeGenerated = todatetime(parse_json(arr_split)[0]),
    malicious_ip = tostring(parse_json(arr_split)[1]),
    ssh_client = tostring(parse_json(arr_split)[2]),
    sshhash = tostring(parse_json(arr_split)[3]),
    username_attempt = tostring(parse_json(arr_split)[4]),
    password_attempt = tostring(parse_json(arr_split)[5])
| project-away arr_split, ext_iocs
```
From here, just join to your other telemetry tables you wish to match our data on 😄

Thanks ($HELLS + KayaSEC).

----

### Updates Coming...
- Increased Nodes/ Diversification
- Variations of datatypes

----

### Contributions
Project Killchain values and appreciates contributions from the cybersecurity community. Feel free to contribute code, share new tools, update our knowledge base, or expand the IOC database. 

Please review the contributing guidelines before making any contributions.

https://github.com/CyDefOps/project-killchain#contributions
