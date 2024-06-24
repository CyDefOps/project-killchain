import requests
from colorama import Fore
import argparse
from tabulate import tabulate
import csv
from simple_colors import *

VT_KEY = ""

def banner():

  banned =  '''

     _    _                        ___ ____  ____  ____  
    / \  | |__  _   _ ___  ___ _ _|_ _|  _ \|  _ \| __ ) 
   / _ \ | '_ \| | | / __|/ _ \ '__| || |_) | | | |  _ \ 
  / ___ \| |_) | |_| \__ \  __/ |  | ||  __/| |_| | |_) |
 /_/   \_\_.__/ \__,_|___/\___|_| |___|_|   |____/|____/ v1.0         

 Check IPs against VirusTotal at ease!
 ------------------------------------
 Coded by Shrefa Ashour & Kamran Saifullah
 https://cydefops.com/
 https://github.com/CyDefOps/project-killchain

 Usage: python3 VTExplorer.py -h
 '''
  
  print(Fore.RED + banned + Fore.RESET)

def check(value):


    VTurl = "https://www.virustotal.com/api/v3/ip_addresses/" + value

    VTheaders = {
    "accept": "application/json",
    "x-apikey": VT_KEY
}

   

    while True:


        VTResponse = requests.get(VTurl, headers=VTheaders)

        VTdecodedResponse = VTResponse.json()

        break

    print(Fore.CYAN +"\n[+] IP Being Checked: " + Fore.RESET, value + "\n")

    VT_table_data = [

         ["Subnet", str(VTdecodedResponse["data"]["attributes"]["network"])],
         ["Harmless", str(VTdecodedResponse["data"]["attributes"]["last_analysis_stats"]["harmless"])],
         ["Malicious", str(VTdecodedResponse["data"]["attributes"]["last_analysis_stats"]["malicious"])],
         ["Suspicious", str(VTdecodedResponse["data"]["attributes"]["last_analysis_stats"]["suspicious"])],
         ["Undetected", str(VTdecodedResponse["data"]["attributes"]["last_analysis_stats"]["undetected"])]

    ]

    try:

        print(green("[+] VirusTotal Results\n"))
        print(yellow(tabulate(VT_table_data,tablefmt="fancy_outline") + "\n"))

    except:
        exit

    csvCreator(value, VTdecodedResponse)

def csvCreator(value, vtresponse):

    with open("Final.csv", mode='a', newline='') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0:
            header = ["IP Address"
                      , "VT Harmless Score"
                      , "VT Undetected Score"
                      , "VT Malicious Score"
                      , "VT Suspicious Score"
                      ]
            writer.writerow(header)


        # VT Values
        IPAddress = str(value)
        harmless = str(vtresponse["data"]["attributes"]["last_analysis_stats"]["harmless"])
        malicious = str(vtresponse["data"]["attributes"]["last_analysis_stats"]["malicious"])
        suspicious = str(vtresponse["data"]["attributes"]["last_analysis_stats"]["suspicious"])
        undetected = str(vtresponse["data"]["attributes"]["last_analysis_stats"]["undetected"])

        data = [IPAddress, harmless, undetected, malicious, suspicious]
        writer.writerow(data)


def main():
    
    banner()

    parser = argparse.ArgumentParser()
    parser.add_argument('-ip', metavar="IP Address", help="Single IP_Address")
    parser.add_argument('-file', metavar="IPAddress.txt", help="List of IP addresses in a text file")
    args = vars(parser.parse_args())

    try:
        if args["ip"]:
            check(args["ip"])
        elif args["file"]:
            IpFile = args["file"]
            with open(IpFile, 'r') as ipfile:
                for line in ipfile:
                    print(line)
                    check(line.strip())
    except: KeyboardInterrupt
        
if __name__ == '__main__':
    main()
