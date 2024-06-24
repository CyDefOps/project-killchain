```
 ________  _______   ___           ___    ___ ________  _______   ________     
|\   __  \|\  ___ \ |\  \         |\  \  /  /|\_____  \|\  ___ \ |\   __  \    
\ \  \|\  \ \   __/|\ \  \        \ \  \/  / /\|___/  /\ \   __/|\ \  \|\  \   
 \ \   ____\ \  \_|/_\ \  \        \ \    / /     /  / /\ \  \_|/_\ \   _  _\  
  \ \  \___|\ \  \_|\ \ \  \____    \/  /  /     /  /_/__\ \  \_|\ \ \  \\  \| 
   \ \__\    \ \_______\ \_______\__/  / /      |\________\ \_______\ \__\\ _\ 
    \|__|     \|_______|\|_______|\___/ /        \|_______|\|_______|\|__|\|__|
                                 \|___|/                                       
                                                                                                                 
 An Automated Static PE File Characterisitcs Analyzer
 ------------------------------------
 Coded by Kamran Saifullah - Frog Man
 Twitter: https://twitter.com/deFr0ggy 
 GitHub: https://github.com/CyDefOps/project-killchain/
 LinkedIn: https://linkedin.com/in/kamransaifullah 
 Website: https://cydefops.com/

 Usage: ./PELyzer.py <PE Executable>
```

<h4 align="center"> PELyzer - An Automated Static PE File Characteristics Analyzer</h4>

PLyzer is a simple and effecient tool to fetch the details required during the initial phase (Basic Static Analysis) of Malware Analysis.

There are times when you have an exetable on your linux machines and sometimes within the WSL. So, there should be an easy way out to find out the initial information of the executable. On the basis on which further investigations can be done.

PLyzer is able to provide you with the following information. 

- File Type
- File Hashes (MD5, SHA1, SHA256, SHA 512)
- DOS Header
- PE Pointer Header
- No of Sections
- Characteristics
- File Creation Date
- Signature: PE Executable
- File Architecture
- PE Sections
- Imported Modules

