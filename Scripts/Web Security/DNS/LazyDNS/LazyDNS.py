import sys
import dns.resolver
from colorama import *
import validators
from validators import *
import requests
import re

def banner():
    banner = r"""  

            __      __ 
 /  __     /  )/| )(   
(__(//_(/ /(_// |/__)  
       /               v1.0
                                                                                   
 Lazy DNS - Simply Query DNS Records
 ------------------------------
 Coded by Kamran Saifullah - Frog Man
 Twitter: https://twitter.com/deFr0ggy 
 GitHub: https://github.com/CyDefOps/project-killchain
 LinkedIn: https://linkedin.com/in/kamransaifullah 
 Website: https://cydefops.com/

 Usage: ./LazyDNS.py <http|https://example.com>
"""

    print(Fore.YELLOW + banner + Fore.RESET)

def domCheck(url):

    starts = ['http://', 'https://', 'http://www.', 'https://www.']

    if validators.url(url) == True:
        print(Fore.CYAN + "[+] Initiating The Initial Information Gathering \n")
        print(Fore.BLUE + " => Target Domain: " + url)
        try:
            r = requests.get(url, allow_redirects=True)
            if r.status_code == requests.codes.ok:

                for values in starts:
                    try:
                        if url.startswith(values):
                            final = re.sub(values, '', url)
                    except:
                        print("Something Might Have Gone Wrong!")

            lazyDNS(final)

        except requests.exceptions.SSLError:
            print(Fore.CYAN +  "\n[E] - SSL can not be verified - Turning Off SSL Verification!\n\n")
            r = requests.get(url, verify=False)

        except requests.exceptions.ConnectionError:
            print(Fore.CYAN +  "\n[E] - Connection Error - Please Try Again!\n\n")

    else:
        print(Fore.RED + "[-] Domain is not correct!\n")  

def lazyDNS(domain):

    records = ['A', 'AAAA', 'NS', 'MX', 'CNAME', 'SOA', 'PTR', 'TXT']

    for record in records:
        try:
            print(Fore.GREEN + "\n" + f"[+] Record Type - {record}" +  Fore.RESET)
            responses = dns.resolver.resolve(domain, record)
            for values in responses:
                print(values.to_text())
        except:
            print(Fore.RED + "\n" + f"[-] No Record Found - {record}" + Fore.RESET)
            pass

    evilZonedDNS(domain)

def evilZonedDNS(domain):

    print(Fore.CYAN + "\n[+] Evil Stuff - Checking SPF Records! \n" + Fore.RESET)

    try:
        spfCheck = dns.resolver.resolve('_spf.' + domain, 'TXT')
        for data in spfCheck:
            if 'spf' in str(data):
                print(Fore.RED + "SPF Record Found :" + Fore.RESET, Fore.GREEN + data.to_text() + Fore.RESET)

    except:
        print (Fore.RED + "[-] SPF Record Not Found!\n")

    print(Fore.CYAN + "\n[+] Evil Stuff - Checking DMARC Records! \n" + Fore.RESET)

    try:
        dmarcdata = dns.resolver.resolve('_dmarc.' + domain, 'TXT')
        for data in dmarcdata:
            if 'DMARC' in str(data):
                print (Fore.RED + "DMARC Record Found :" + Fore.RESET, Fore.GREEN + data.to_text() + "\n" + Fore.RESET)

    except:
        print (Fore.RED + "[-] DMARC Record Not Found\n")
        

    print(Fore.CYAN + "\n[+] Evil Stuff - Checking DKIM Records! \n" + Fore.RESET)

    try:
        dmarc = dns.resolver.resolve('._domainkey.' + domain, 'TXT')
        for data in dmarc:
            if 'DKIM' in str(data):
                print (Fore.RED + "DKIM Record Found :" + Fore.RESET, Fore.GREEN + data.to_text() + Fore.RESET)
    except:
        print (Fore.RED + "[-] DKIM Record Not Found\n")
        


    print(Fore.CYAN + "\n[+] Evil Stuff - Checking ZONE TRANSFERS! \n" + Fore.RESET)

    ns_answer = dns.resolver.resolve(domain, 'NS')

    for server in ns_answer:

        ip_resolv = dns.resolver.resolve(server.target, 'A')

        for ip in ip_resolv:
            print(Fore.GREEN + f"\nNS {server} Is Having IP {ip}\n")
            try:
                zoneTransfer = dns.zone.from_xfr(dns.query.xfr(str(ip), domain))
                for host in zoneTransfer:
                    print(Fore.YELLOW + f"  Hostname: {host}")
            except:
                print(Fore.RED + f"No Zone Transfer On {server}")
                continue

def main():

    banner()

    if len(sys.argv) < 2 or len(sys.argv) > 2:
        print("Invalid Arguments Provided!")
    else:
        domCheck(sys.argv[1])

if __name__ == '__main__':
    main()

