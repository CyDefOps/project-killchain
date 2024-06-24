import requests
from colorama import Fore
import argparse
from tabulate import tabulate
import csv
from simple_colors import *

AbuseIPDB_KEY = ""
VT_KEY = ""

def banner():

  banned =  '''


     _    _                        ___ ____  ____  ____  
    / \  | |__  _   _ ___  ___ _ _|_ _|  _ \|  _ \| __ ) 
   / _ \ | '_ \| | | / __|/ _ \ '__| || |_) | | | |  _ \ 
  / ___ \| |_) | |_| \__ \  __/ |  | ||  __/| |_| | |_) |
 /_/   \_\_.__/ \__,_|___/\___|_| |___|_|   |____/|____/ v1.0         

 Check IPs against AbuseIPDB & VirusTotal at ease!
 ------------------------------------
 Coded by Shrefa Ashour & Kamran Saifullah
 https://cydefops.com/
 https://github.com/CyDefOps/project-killchain

 Usage: python3 AbUserIPDB.py -h
 '''
  
  print(Fore.RED + banned + Fore.RESET)

def check(value):

    url = 'https://api.abuseipdb.com/api/v2/check'

    VTurl = "https://www.virustotal.com/api/v3/ip_addresses/" + value

    VTheaders = {
    "accept": "application/json",
    "x-apikey": VT_KEY
}

    querystring = {
        'ipAddress': value,
        'maxAgeInDays': '90'
    }

    headers = {
        'Accept': 'application/json',
        'Key': AbuseIPDB_KEY
    }

    while True:
        response = requests.request(method='GET', url=url, headers=headers, params=querystring)
        
        decodedResponse = response.json()

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

    table_data = [

        ["Domain Name", decodedResponse["data"]["domain"]],
        ["Abuse Confidence Score", str(decodedResponse["data"]["abuseConfidenceScore"])],
        ["Country Code", str(decodedResponse["data"]["countryCode"])],
        ["Internet Service Provider", str(decodedResponse["data"]["isp"])],
        ["Total Reports",  str(decodedResponse["data"]["totalReports"])],
        ["Last Reported Date", str(decodedResponse["data"]["lastReportedAt"])]
    ]
    
    try:
        print(green("\n[+] AbuseIPDB Results\n"))
        print(yellow(tabulate(table_data, tablefmt="fancy_outline") + "\n"))
        print(green("[+] VirusTotal Results\n"))
        print(yellow(tabulate(VT_table_data,tablefmt="fancy_outline") + "\n"))

    except:
        exit

    csvCreator(decodedResponse, VTdecodedResponse)

def csvCreator(response, vtresponse):

    with open("Final.csv", mode='a', newline='') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0:
            header = ["IP Address"
                      , "Domain Name"
                      , "Abuse Confidence Score"
                      , "Country Code"
                      , "Internet Service Provider"
                      , "Total Reports"
                      , "Last Reported Date"
                      , "VT Harmless Score"
                      , "VT Undetected Score"
                      , "VT Malicious Score"
                      , "VT Suspicious Score"
                      ]
            writer.writerow(header)

        # AbuseIPDB Values
        ip_address = response["data"]["ipAddress"]
        domain = response["data"]["domain"]
        abuse_confidence_score = response["data"]["abuseConfidenceScore"]
        country_code = response["data"]["countryCode"]
        isp = response["data"]["isp"]
        total_reports = response["data"]["totalReports"]
        last_reported_date = response["data"]["lastReportedAt"]

        # VT Values
        harmless = str(vtresponse["data"]["attributes"]["last_analysis_stats"]["harmless"])
        malicious = str(vtresponse["data"]["attributes"]["last_analysis_stats"]["malicious"])
        suspicious = str(vtresponse["data"]["attributes"]["last_analysis_stats"]["suspicious"])
        undetected = str(vtresponse["data"]["attributes"]["last_analysis_stats"]["undetected"])

        data = [ip_address, domain, abuse_confidence_score, country_code, isp, total_reports, last_reported_date, harmless, undetected, malicious, suspicious]
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
                    check(line.strip())
    except: KeyboardInterrupt
        
if __name__ == '__main__':
    main()
