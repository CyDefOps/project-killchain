### Alternate Data Streams Tracer - ADSTracer - Project KillChain
A python script to automate hunting of ADS (Alternate Data Streams) which can include some hidden/confidential information. 

**Idea:** The development idea for this tiny tool came from testing the DLP (Data Loss Prevention) controls and trying to exfiltrate the data using Alternate Data Streams in Windows Environment. 

### Understanding Alternate Data Streams

- https://learn.microsoft.com/en-us/windows/win32/fileio/file-streams?source=post_page-----54b144a831f1--------------------------------
- https://www.ired.team/offensive-security/defense-evasion/t1096-alternate-data-streams
- https://blog.ironmansoftware.com/daily-powershell/powershell-alternate-data-streams/

Made with :heart: by [Kamran Saifullah](https://linkedin.com/in/KamranSaifullah) + [Shrefa Ashour](https://www.linkedin.com/in/shrefa-salem-37b876290)

![PKC](https://img.shields.io/badge/Project-%20Killchain-357441)
![Language](https://img.shields.io/badge/Language-%20Python-357441?style=flat-square)

<img src="https://img1.wsimg.com/blobby/go/1cf5bcbc-aad3-42e4-a7e0-6c0149aec441/downloads/BG%20Gradient%20(2).png" width="125" height="125">

----
## Overview

The purpose of this script is to identofy the Alternate Data Streams from the files which have been flagged for the investigation. It is a really good rechnique which can be used by Insider Threats or Threat Actors to deliver their tools from the arsenal and to exfiltrate the sensitive information out of the network. 

By simply looking onto the files no information is provided. Thus, a step ahead is taken to look into the number of streams available within the file which is to be investigated. It can be done manually for a number of files but not easy when there are huge number of files. 

Thus, we created this script to automate the process of hunting low hanging fruits and then taking forward the investigation.

The script does the following:

- **Single File Scan**
  - Checks for all Alternate Data Streams
  - Outputs the data observed in Alternate Data Streams
- **Directory Scan**
  - Checks for all Alternate Data Streams for each file available in the provided directory.
  - Outputs the data observed in Alternate Data Streams for each file.
- **Output Directory**
  - All the extracted data will be added to the Output Directory under the stream name observed.
---

## Instructions for using the tool

### Installing Dependencies
In order for the script to work properly, there are few dependencies which are required to be installed. Do it with the following from within the folder or as you like. 

```pip install -r requirements.txt```

or you can install the dependecies one by one. 

```pip install colorama```

Finally, the main module on which ADSTracer is relying on. Great work done by the guys behind creating a full fledge module.

> https://github.com/RobinDavid/pyADS/tree/master

Ensure to keep the `pyads.py` in the same directory.

### Begin The Hunt

Execute the `ADSTracer.py` by doing simply as 
```python3 ADSTracer.py```. 

The scripts supports 3 parameters.

1. For help `ADSTracer.py -h`.
2. For single file `ADSTracer.py -f`.
3. For directory `ADSTracer.py -d`.


### Help Section

![](https://raw.githubusercontent.com/deFr0ggy/deFr0ggy.github.io/master/assets/ADSTracer/help.png )

### Single File Scan - In Action

![](https://raw.githubusercontent.com/deFr0ggy/deFr0ggy.github.io/master/assets/ADSTracer/file.png )

### Directory Scan - In Action

![](https://raw.githubusercontent.com/deFr0ggy/deFr0ggy.github.io/master/assets/ADSTracer/directory.png )

### Extracting Streams Data - In Action

![](https://raw.githubusercontent.com/deFr0ggy/deFr0ggy.github.io/master/assets/ADSTracer/Output.png )

## Feedback & Issues

Please, submit any feedback or issues to our **GitHub:** https://github.com/CyDefOps/project-killchain

Many Thanks

[Shrefa Ashour](https://www.linkedin.com/in/shrefa-salem-37b876290) + [Kamran Saifullah](https://linkedin.com/in/KamranSaifullah)

----

### Updates Coming...
- [x] Extracting Embedded Files/Streams.
  - [x] 22nd Dec 2023
- [ ] Want anything else to be added? Reach out to us.
----

### Contributions
Project Killchain values and appreciates contributions from the cybersecurity community. Feel free to contribute code, share new tools, update our knowledge base, or expand the IOC database. 

Please review the contributing guidelines before making any contributions.

https://github.com/CyDefOps/project-killchain#contributions

----