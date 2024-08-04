### WhatThePhish - Project KillChain
A super rapid email phishing analysis tool. Made with :heart: by [KayaSEC](https://github.com/KayaSEC) + [$HELLS](https://github.com/ntwrite).

![PKC](https://img.shields.io/badge/Project-%20Killchain-357441)
![Language](https://img.shields.io/badge/Language-%20Python-357441?style=flat-square)
![PKC](https://img.shields.io/badge/Version-%201.1-357441)

<img src="https://img1.wsimg.com/blobby/go/1cf5bcbc-aad3-42e4-a7e0-6c0149aec441/downloads/BG%20Gradient%20(2).png" width="125" height="125">

## Overview

The purpose of this script is intended to do various, rapid investigation actions a SOC/CSIRT analyst may do when investigating a phishing email. The script checks:
- Hops 
- Authentication Results
- URLs
- Domains
- Attachments
- Parses Email Body (Plaintext or HTML) and prints to terminal window
Using this tool, you should be able to easily analyse, and at very least, have a strong understanding of whether the email is a phish, spam or a false positive. 

---

## Instructions for using the tool

From within your folder with requirements file and py script:
```pip install -r requirements.txt```

Then run it (Added Argparse): 
```python3 wtp.py --message <path_to_msg>```

- Need to add a sample output (!!)

Please, submit any feedback or issues to our **GitHub:** https://github.com/CyDefOps/project-killchain

Thanks ($HELLS + KayaSEC).

----

### Updates Added (v1.1)
- Color Coded Auth Results
- Decode Safelinks Logic
- Highlight Decoded Links in Body (w/ color)
- Detect Phishing Simulation Logic

# Updates Coming (v1.2)
- SpamAssassin or Similar Capability Pip package for analysis report
- Enhanced Auth Parsing Hops

----

### Contributions
Project Killchain values and appreciates contributions from the cybersecurity community. Feel free to contribute code, share new tools, update our knowledge base, or expand the IOC database. 

Please review the contributing guidelines before making any contributions.

https://github.com/CyDefOps/project-killchain#contributions
