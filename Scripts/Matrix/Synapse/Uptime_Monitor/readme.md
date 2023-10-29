### Synapse Homeserver Automation - Uptime Check
Automation of Matrix Synapse, this script checks if a server is online, and if it goes down, it sends a webhook to your IFTTT webhook endpoint (i.e. your phone) so you can fix it. Made with :heart: by [$HELLS](https://github.com/ntwrite).

![PKC](https://img.shields.io/badge/Project-%20Killchain-357441)
![Language](https://img.shields.io/badge/Language-%20Shell-357441?style=flat-square)

<img src="https://camo.githubusercontent.com/1ff5370fbb2b1778bb50775f7a3e06790b6a878343688b9c5151dcbddd5b482a/68747470733a2f2f73757072656d652e73682f6173736574732f706b632e6a7067" width="125" height="125">

----
## Overview

The purpose of this script is intended to purely check if your server is online. It offers
- Easy Uptime Monitoring
- It's free
- Convenient/ Easy, it literally goes to your phone

---

## Instructions for using the script 

Replace, {your_server_ip}, as in your Matrix Homeserver IP as well as {your_trigger} and {your_key} from IFTTT. 

Then, naturally add it as a cron task:

```
# m h  dom mon dow   command
0 0/5 * 1/1 * ? * /home/user/automation/conn_check.sh
```

Please, submit any feedback or issues to our **GitHub:** https://github.com/CyDefOps/project-killchain

Thanks.

----

### No Planned Updates/ Maintenance

----

----

### Contributions
Project Killchain values and appreciates contributions from the cybersecurity community. Feel free to contribute code, share new tools, update our knowledge base, or expand the IOC database. 

Please review the contributing guidelines before making any contributions.

https://github.com/CyDefOps/project-killchain#contributions

----

