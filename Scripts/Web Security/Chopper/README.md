### Chopper - Project KillChain
Chopper is a python script to scrape HTTP Headers from the requests. All you need is to supply a valid domain name. Chopper will automatically check for security related headers, thus saving much of your time.

Made with :heart: by [Kamran Saifullah](https://linkedin.com/in/KamranSaifullah)

![PKC](https://img.shields.io/badge/Project-%20Killchain-357441)
![Language](https://img.shields.io/badge/Language-%20Python-357441?style=flat-square)

<img src="https://img1.wsimg.com/blobby/go/1cf5bcbc-aad3-42e4-a7e0-6c0149aec441/downloads/BG%20Gradient%20(2).png" width="125" height="125">

----
## Overview

Chopper is a python script to scrape HTTP Headers from the requests. All you need is to supply a valid domain name. Chopper will automatically check for security related headers, thus saving much of your time.

Currently Chopper is able to check the following headers and flags.

## The Headers To Be In Place

1. Content-Security-Policy 
2. X-XSS-Protection
3. X-Frame-Headers
4. X-Content-Type
5. Strict-Transport-Security
6. Referrer-Policy
7. Feature-Policy
8. Cache-Control Policy
9. HttpOnly Flag
10. Secure Flag

## The Headers To Be Removed

1. Server Header 
2. X-Powered-By Header
3. X-AspNet-Version Header

## Additional Headers To Look At

1. Access-Control-Allow-Origin
2. Access-Control-Allow-Credentials


## Instructions for using the tool

### Installing Dependencies
In order for the script to work properly, there are few dependencies which are required to be installed. Do it with the following from within the folder or as you like. 

```pip install -r requirements.txt```

or you can install the dependecies one by one. 

1. Python3
2. Colorama
3. Validators
4. Requests

### Begin The Hunt

Execute the `Chopper.py` by doing simply as 
```python3 Chopper.py```. 

The scripts only take the URL as a parameter.

1. Scanning URL `Chopper.py <URL>`.

### Chopper - URL Scanning

![](/Scripts/Web%20Security/Chopper/Assets/image.png)

Many Thanks

[Kamran Saifullah](https://linkedin.com/in/KamranSaifullah)

----

### Contributions
Project Killchain values and appreciates contributions from the cybersecurity community. Feel free to contribute code, share new tools, update our knowledge base, or expand the IOC database. 

Please review the contributing guidelines before making any contributions.

https://github.com/CyDefOps/project-killchain#contributions

----