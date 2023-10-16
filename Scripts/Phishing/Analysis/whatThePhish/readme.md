### whatThePhish - Project KillChain
A super rapid email phishing analysis tool. Made with <3 by [KayaSEC](https://github.com/KayaSEC) + [$HELLS](https://github.com/ntwrite).

![PKC](https://img.shields.io/badge/Project-%20Killchain-357441)

<img src="https://camo.githubusercontent.com/1ff5370fbb2b1778bb50775f7a3e06790b6a878343688b9c5151dcbddd5b482a/68747470733a2f2f73757072656d652e73682f6173736574732f706b632e6a7067" width="125" height="125">

----
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

Then run it: 
```python3 wtp.py```

Fill out prompt with full file path (or file name if same dir, e.g.):
Enter the path of the .eml file to analyze: ```users/user/Downloads/email.eml```
or (try this)

Enter the path of the .eml file to analyze: ```email.eml```

Sample Output (a real phishing email, via and with thanks to: rf-peixoto/phishing_pot) regrettably, the output is not yet perfect in terms of parsing of HTML Email Body, but 
it is good enough for analysis

```
Received Headers:
+-----+--------------------------------------------------------------------------------------------+
| Hop |                                      From/By Servers                                       |
+-----+--------------------------------------------------------------------------------------------+
|  1  |         a9-14.smtp-out.amazonses.com -> DM6NAM11FT019.mail.protection.outlook.com          |
|  2  | DM6NAM11FT019.eop-nam11.prod.protection.outlook.com -> DM6PR10CA0006.outlook.office365.com |
|  3  |     DM6PR10CA0006.namprd10.prod.outlook.com -> DS7PR19MB6351.namprd19.prod.outlook.com     |
|  4  |     DS7PR19MB6351.namprd19.prod.outlook.com -> MN0PR19MB6312.namprd19.prod.outlook.com     |
+-----+--------------------------------------------------------------------------------------------+

Authentication Results:
spf=pass (sender IP is 54.240.9.14) smtp.mailfrom=amazonses.com; dkim=pass (signature was verified) header.d=promotix.com;dmarc=pass action=none 
header.from=promotix.com;compauth=pass reason=100

Email Content:
Domains:
www.kif.re.kr
URLs:
http://www.kif.re.kr/kif2///publication/viewer.aspx?controlno=229274&returnurl=http://taurus-
http://www.kif.re.kr/kif2///publication/viewer.aspx?controlno=229274&returnurl=http://taurus-
Attachments: 1

Email Body:
#

**_
Withdrawals are now available_**

_Dear customer,_


**You have been identified as an eligible client to begin withdrawing digital
assets from your FTX account.**

Withdrawals will be dispatched in USD-C matched to the balance of digital
assets held in your Wallet account at the time of the platform pause. You can
now withdraw to an external ERC-20 wallet on a by clicking the Withdraw Now
button below. Wallet account balances were calculated based on the digital
assets held in your Wallet account at the time of the platform pause. If you
initiated a trade, transfer, or withdrawal request after the platform pause,
these transactions have been updated as displayed in the "Transaction History"
section of the dashboard page in your account.


Please note that, due to the high volume of requests, withdrawals may **take
90 days or more** to process once submitted. FTX will process withdrawals as
quickly as possible while maintaining security protocols. You can check the
status of your withdrawal request in the Transaction History section of your
FTX account dashboard page upon connecting an ERC-20 wallet. Additionally,
withdrawals are subject to any applicable third-party transaction fees and/or
withdrawal fees, which are based on transaction processing costs and may be
adjusted from time to time based on market conditions, as set forth in the FTX
Terms of Service.


[
](http://www.kif.re.kr/kif2///publication/viewer.aspx?controlno=229274&returnurl=http://taurus-
online.ch/wp/pf/)

[Withdraw
Now](http://www.kif.re.kr/kif2///publication/viewer.aspx?controlno=229274&returnurl=http://taurus-
online.ch/wp/pf/)

_We are grateful for your willingness to assist us in navigating this process.
Should you have any queries or require additional information, our customer
service representatives are available to provide assistance. We thank you for
your consideration on this matter.
_

FTX EU Ltd (ex.K-DNA Financial Services Ltd) is a company authorized and
regulated by the Cyprus Securities and Exchange Commission (license no.
273/15) with Registered Office at 23 Spyrou Kyprianou Protopapas Building 3rd
floor 4001, Limassol, Cyprus
```

Please, submit any feedback or issues to our GitHub: CyDefOps/project-killchain
Thanks. $HELLS + KayaSEC.


----

### Updates Coming...
- Color Coded Auth Results (the seconds matter!)
- Enhanced Body Parsing
- CTI Integrations for URLs/Domains
- Args Direct to Script (w/o exec) for further speed + automation
e.g. ```python3 wtp.py --path /a/b/c/sample.eml```

----

## Contributions

Project Killchain values and appreciates contributions from the cybersecurity community. Feel free to contribute code, share new tools, update our knowledge base, or expand the IOC database. Please review the contributing guidelines before making any contributions.

----
