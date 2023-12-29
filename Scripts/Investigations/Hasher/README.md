### HASHER - Project KillChain
A automated script to help incidnet responders, ethical hackers, IT professionals generate hashes of single file or multiple files and have it automatically saved in a CSV format. 

Made with :heart: by  + [Kamran Saifullah](https://linkedin.com/in/KamranSaifullah)

![PKC](https://img.shields.io/badge/Project-%20Killchain-357441)
![Language](https://img.shields.io/badge/Language-%20Python-357441?style=flat-square)

<img src="https://img1.wsimg.com/blobby/go/1cf5bcbc-aad3-42e4-a7e0-6c0149aec441/downloads/BG%20Gradient%20(2).png" width="125" height="125">

----
## Overview

The purpose of this script is to help teams calculate hashes of files as per their daily use and for the incident responders to generate hashes of large number of files all together. 

Generating hashes one by one have a ton of overhead and thus is not recommended. Using `HASHER` enable its users to generate hashes on the fly for the following algorithms. 

1. MD5
2. SHA1
3. SHA256
4. SHA512

The script after calculating the hashes not only displayes it as an output but also saves all the hases in a `CSV` file named `hashes.csv`. The following columns are provided with the CSV results. 

The script saves the following in the CSV file:

1. File Name
2. MD5
3. SHA1
4. SHA256
5. SHA512

---

## Instructions for using the tool

### Installing Dependencies
In order for the script to work properly, there are few dependencies which are required to be installed. Do it with the following from within the folder or as you like. 

```pip install -r requirements.txt```

or have them installed manually.

### Begin The Hunt

Execute the `Hasher.py` by doing simply as 
```python3 Hasher.py```. 

The scripts supports 2 parameters which are automatically verified.

1. For single File `Hasher.py <FileName>`.
2. For directory  `Hasher.py <PATH>`.


### Single File - In Action

![](https://github.com/deFr0ggy/deFr0ggy.github.io/blob/master/assets/hasher1.png?raw=true)

### Directory - In Action

![](https://github.com/deFr0ggy/deFr0ggy.github.io/blob/master/assets/hasher2.png?raw=true)


### Saved Results (CSV/Excel)

![](https://github.com/deFr0ggy/deFr0ggy.github.io/blob/master/assets/hasher3.png?raw=true)

## Feedback & Issues

Please, submit any feedback or issues to our **GitHub:** https://github.com/CyDefOps/project-killchain

Many Thanks

[Kamran Saifullah](https://linkedin.com/in/KamranSaifullah)

----

### Updates Coming...
- Securing API Keys - OS ENV
- More Integrations
- Dashboarding 
- Many more..

----

### Contributions
Project Killchain values and appreciates contributions from the cybersecurity community. Feel free to contribute code, share new tools, update our knowledge base, or expand the IOC database. 

Please review the contributing guidelines before making any contributions.

https://github.com/CyDefOps/project-killchain#contributions

----
