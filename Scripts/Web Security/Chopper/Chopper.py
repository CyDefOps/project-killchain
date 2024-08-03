import requests
from colorama import *
import sys
import validators
from validators.domain import domain
import urllib3

urllib3.disable_warnings()

def banner():
    banner = r"""
  ____ _                                 _ 
 / ___| |__   ___  _ __  _ __   ___ _ __| |
| |   | '_ \ / _ \| '_ \| '_ \ / _ \ '__| |
| |___| | | | (_) | |_) | |_) |  __/ |  |_|
 \____|_| |_|\___/| .__/| .__/ \___|_|  (_) v1.0
                  |_|   |_|                

 An Automated Security Headers Analyzer
 ------------------------------
 Coded by Kamran Saifullah - Frog Man
 Twitter: https://twitter.com/deFr0ggy 
 GitHub: https://github.com/CyDefOps/project-killchain
 LinkedIn: https://linkedin.com/in/kamransaifullah 
 Website: https://cydefops.com/

 Usage: ./Chopper.py <http|https://example.com>
"""

    print(Fore.GREEN + banner)


def realWork(URL):

    if validators.url(URL) == True:
        print(Fore.YELLOW + "Domain: " + URL + "\n")
        try:
            r = requests.get(URL)

            if r.status_code == requests.codes.ok:
                headerGrabbing(URL)

        except requests.exceptions.SSLError:
            print(Fore.CYAN +  "\n[E] - SSL can not be verified - Turning off SSL Verification!\n\n")
            r = requests.get(URL, verify=False)

        except requests.exceptions.ProxyError:
            print(Fore.CYAN + "\n[E] - There is an issue with your proxy. Please verify your ENV Variables/Internal Network Proxy!\n")

    else:
        print(Fore.RED + "The URL Supplied is not correct!")

def headerGrabbing(URL):
        try:

            r = requests.get(URL, verify=False)

            if r.status_code == requests.codes.ok:
                if r.headers['Server'] != "":
                    print(Fore.GREEN + "[X] Server: " +
                    Fore.RESET + r.headers['Server'].strip(";"))
                    print(Fore.RED + "[/] Server Header is in place!")        

        except KeyError:
            print(Fore.MAGENTA + "[-] Server Header is not in place!")

        try:

            if r.status_code == requests.codes.ok:
                if r.headers['X-Powered-By'] != "":
                    print(Fore.GREEN + "[X] X-Powered-By: " +
                    Fore.RESET + r.headers['X-Powered-By'].strip(";"))
                    print(Fore.RED + "[/] X-Powered-By Header is in place!")        

        except KeyError:
            print(Fore.MAGENTA + "[-] X-Powered-By Header is not in place!")

        try:

            if r.status_code == requests.codes.ok:
                if r.headers['X-AspNet-Version'] != "":
                    print(Fore.GREEN + "[X] X-AspNet-Version: " +
                    Fore.RESET + r.headers['X-AspNet-Version'].strip(";"))
                    print(Fore.RED + "[/] X-AspNet-Version Header is in place!")        

        except KeyError:
            print(Fore.MAGENTA + "[-] X-AspNet-Version Header is not in place!")

        try:

            if r.status_code == requests.codes.ok:
                if r.headers['X-AspNetMvc-Version'] != "":
                    print(Fore.GREEN + "[X] X-AspNetMvc-Version: " +
                    Fore.RESET + r.headers['X-AspNetMvc-Version'].strip(";"))
                    print(Fore.RED + "[/] X-AspNetMvc-Version Header is in place!")        

        except KeyError:
            print(Fore.MAGENTA + "[-] X-AspNetMvc-Version Header is not in place!")

        try: 

            if r.status_code == requests.codes.ok:
                if r.headers['Content-Security-Policy'] != "":
                    print(Fore.GREEN + "[X] Content-Security-Policy: " + Fore.RESET + r.headers['Content-Security-Policy'].strip(";"))
                    print(Fore.MAGENTA + "[/] Content Security Protection Is Enforced!")
  
        except KeyError:
            print(Fore.RED + "[-] Content-Security-Policy is not in place!")

        try:

            if r.status_code == requests.codes.ok:
                if r.headers['X-XSS-Protection'] != "":
                    print(Fore.GREEN + "[X] X-XSS-Protection: " +
                    Fore.RESET + r.headers['X-XSS-Protection'].strip(";"))
                    print(Fore.MAGENTA + "[/] Cross Site Scripting Protection Is Enforced!")        

        except KeyError:
            print(Fore.RED + "[-] X-XSS-Protection - XSS Protection is not in place!")

        try:

            if r.status_code == requests.codes.ok:
                if r.headers['X-Frame-Options'] != "":
                    print(Fore.GREEN + "[X] X-Frame-Options: " +
                    Fore.RESET + r.headers['X-Frame-Options'].strip(";"))
                    print(Fore.MAGENTA + "[/] ClickJacking Protection Is Enforced!")
        
        except KeyError:
            print(Fore.RED + "[-] X-Frame-Headers - ClickJacking Protection is not in place!")
        
        try:

            if r.status_code == requests.codes.ok:
                if r.headers['X-Content-Type-Options'] != "":
                    print(Fore.GREEN + "[X] X-Content-Type-Options: " +
                    Fore.RESET + r.headers['X-Content-Type-Options'].strip(";"))
                    print(Fore.MAGENTA + "[/] MIME Sniffing Protection Is Enforced!")          
        
        except KeyError:
            print(Fore.RED + "[-] X-Content-Type - MIME Sniffing Protection is not in place!")
        
        try:

            if r.status_code == requests.codes.ok:
                if r.headers['Strict-Transport-Security'] != "":
                    print(Fore.GREEN + "[X] Strict-Transport-Security: " +
                    Fore.RESET + r.headers['Strict-Transport-Security'].strip(";"))
                    print(Fore.MAGENTA + "[/] HTTP Strict Transport Security Protection Is Enforced!")
  
        except KeyError:
            print(Fore.RED + "[-] Strict-Transport-Security - Protection is not in place!")

        try:

            if r.status_code == requests.codes.ok:
                if r.headers['Referrer-Policy'] != "":
                    print(Fore.GREEN + "[X] Referrer-Policy: " +
                    Fore.RESET + r.headers['Referrer-Policy'].strip(";"))
                    print(Fore.MAGENTA + "[/] Referrer Policy Is Enforced!")
                    
        except KeyError:
            print(Fore.RED + "[-] Referrer-Policy is not in place!")

        try:

                if r.status_code == requests.codes.ok:
                    if r.headers['Feature-Policy'] != "":
                        print(Fore.GREEN + "[X] Feature-Policy: " +
                        Fore.RESET + r.headers['Feature-Policy'].strip(";"))
                        print(Fore.MAGENTA + "[/] Feature Policy Is Enforced!")
        
        except KeyError:
            print(Fore.RED + "[-] Feature-Policy is not in place!")
        
        try:

                if r.status_code == requests.codes.ok:
                    if r.headers['Cache-Control'] != "":
                        print(Fore.GREEN + "[X] Cache-Control: " +
                        Fore.RESET + r.headers['Cache-Control'].strip(";"))
                        print(Fore.MAGENTA + "[/] Private Caching or No-Cache is enforced!")
        
        except KeyError:
            print(Fore.RED + "[-] Cache-Control Policy is not in place!")
        
        try:

                if r.status_code == requests.codes.ok:
                    if r.headers['Access-Control-Allow-Origin'] != "":
                        print(Fore.GREEN + "[X] Access-Control-Allow-Origin: " +
                        Fore.RESET + r.headers['Access-Control-Allow-Origin'].strip(";"))
                        print(Fore.MAGENTA + "[/] CORS Policy is enforced!")

        except KeyError:
            print(Fore.RED + "[-] Access-Control-Allow-Origin - CORS Policy is not in place!")

        try:

                if r.status_code == requests.codes.ok:
                    if r.headers['Access-Controls-Allow-Credentials'] != "":
                        print(Fore.GREEN + "[X] Access-Control-Allow-Credentials: " +
                        Fore.RESET + r.headers['Access-Control-Allow-Credentials'].strip(";"))
                        print(Fore.MAGENTA + "[/] CORS Policy is enforced!")

        except KeyError:
            print(Fore.RED + "[-] Access-Control-Allow-Credentials - CORS Policy is not in place!")

        try:

                if r.status_code == requests.codes.ok:
                    if r.headers['Set-Cookie'] != "":
                        onlyFlag = r.headers['Set-Cookie'].find("HttpOnly")
                        if onlyFlag != -1:
                            print(Fore.GREEN + "[X] Set-Cookie: " +
                        Fore.RESET + r.headers['Set-Cookie'].strip(";"))
                            print(Fore.MAGENTA + "[/] HttpOnly Flag is enforced!")
                        else:
                            print(Fore.RED + "[-] HttpOnly Flag is not in place!")
        
        except KeyError:
            print(Fore.RED + "[-] HttpOnly Flag is not in place!")

        try:
                if r.status_code == requests.codes.ok:
                    if r.headers['Set-Cookie'] != "":
                        secureFlag = r.headers['Set-Cookie'].find("Secure")
                        if secureFlag != -1:
                            print(Fore.GREEN + "[X] Set-Cookie: " +
                        Fore.RESET + r.headers['Set-Cookie'].strip(";"))
                            print(Fore.MAGENTA + "[/] Secure Flag is enforced!")
                        else:
                            print(Fore.RED + "[-] Secure Flag is not in place!")
        
        except KeyError:
            print(Fore.RED + "[-] Secure Flag is not in place!")
        
        print(Fore.BLUE + "\n\n[-] Check These Headers Out! \n\n")

        try:
            for headers in r.headers:
                print(Fore.YELLOW + headers + ":  " + Fore.WHITE + r.headers[headers])
            print("\n\n")
        except KeyError:
            print("ERROR")

def main():

    banner()

    if len(sys.argv) < 2 or len(sys.argv) > 2:
        print("Invalid Arguments Provided!")
    else:
        realWork(sys.argv[1])

if __name__ == '__main__':
    main()
