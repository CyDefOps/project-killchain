### FavBuster - Project KillChain
A python script to automate MMH3 hash calculation of favicons. 

> https://en.wikipedia.org/wiki/MurmurHash

Made with :heart: by [Kamran Saifullah](https://linkedin.com/in/KamranSaifullah) + [Shrefa Ashour](https://www.linkedin.com/in/shrefa-salem-37b876290)

![PKC](https://img.shields.io/badge/Project-%20Killchain-357441)
![Language](https://img.shields.io/badge/Language-%20Python-357441?style=flat-square)

<img src="https://img1.wsimg.com/blobby/go/1cf5bcbc-aad3-42e4-a7e0-6c0149aec441/downloads/BG%20Gradient%20(2).png" width="125" height="125">

----
## Overview

FavIcons are the small icons shown with the title of the web page for most of the web applications. Leveraging this hash, it is possible to uncover vulnerabilities, exposed assets as well as fruitful for bug bounties. This script enables the ethical hackers to calculate the hashes firectly from the URL and with the provided icon file. 

The script provides you with the queries for the following 2 platforms to be search on for your specific target. 

1. [Shodan](https://shodan.io)
2. [FOFA](https://en.fofa.info)
3. [ZoomEye]()

## Instructions for using the tool

### Installing Dependencies
In order for the script to work properly, there are few dependencies which are required to be installed. Do it with the following from within the folder or as you like. 

```pip install -r requirements.txt```

or you can install the dependecies one by one. 

```pip install colorama```
```pip install mmh3```

### Begin The Hunt

Execute the `FavHuster.py` by doing simply as 
```python3 FavBuster.py```. 

The scripts supports 3 parameters.

1. For help `FavBuster.py -h`.
2. For single file `FavBuster.py -url`.
3. For directory `FavBuster.py -file`.


### Favicon - Icon URL

![](/Scripts/Web%20Security/FavBuster/Assets/image.png)

### Favicon - Icon File

![](/Scripts/Web%20Security/FavBuster/Assets/image%20copy.png)

Many Thanks

[Shrefa Ashour](https://www.linkedin.com/in/shrefa-salem-37b876290) + [Kamran Saifullah](https://linkedin.com/in/KamranSaifullah)

----

### Contributions
Project Killchain values and appreciates contributions from the cybersecurity community. Feel free to contribute code, share new tools, update our knowledge base, or expand the IOC database. 

Please review the contributing guidelines before making any contributions.

https://github.com/CyDefOps/project-killchain#contributions

----