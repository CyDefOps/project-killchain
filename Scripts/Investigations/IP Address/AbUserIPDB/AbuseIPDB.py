import requests
from colorama import Fore
import argparse
import tabulate
from tabulate import tabulate
import csv

ABUSE_IPDB_KEY = ""

def banner():
 

  banned =  '''

     _    _                        ___ ____  ____  ____  
    / \  | |__  _   _ ___  ___ _ _|_ _|  _ \|  _ \| __ ) 
   / _ \ | '_ \| | | / __|/ _ \ '__| || |_) | | | |  _ \ 
  / ___ \| |_) | |_| \__ \  __/ |  | ||  __/| |_| | |_) |
 /_/   \_\_.__/ \__,_|___/\___|_| |___|_|   |____/|____/ v1.0         

 Check IPs against AbuseIPDB at ease!
 ------------------------------------
 Coded by Shrefa Ashour & Kamran Saifullah
 https://cydefops.com/
 https://github.com/CyDefOps/project-killchain

 Usage: python3 AbuseIPDB.py -h
 '''
  
  print(banned)
 
 
def check(value):
 
    url = 'https://api.abuseipdb.com/api/v2/check'
 
    querystring = {
        'ipAddress': value,
        'maxAgeInDays': '90'
    }
 
    headers = {
        'Accept': 'application/json',
        'Key': ABUSE_IPDB_KEY
    }
 
 
    while True:
        response = requests.request(method='GET', url=url, headers=headers, params=querystring)
        decodedResponse = response.json()
 
        print(decodedResponse)
        break
 
    print(Fore.CYAN +"\n[+] IP Being Checked: " + Fore.RESET, value + "\n")
   
    table_data = [
 
        ["Domain Name", decodedResponse["data"]["domain"]],
        ["Abuse Confidence Score", str(decodedResponse["data"]["abuseConfidenceScore"])],
        ["Country Code", str(decodedResponse["data"]["countryCode"])],
        ["Internet Service Provider", str(decodedResponse["data"]["isp"])],
        ["Total Reports",  str(decodedResponse["data"]["totalReports"])],
        ["Last Reported Date", str(decodedResponse["data"]["lastReportedAt"])]
    ]
   
    try:
        print((tabulate(table_data, tablefmt="fancy_outline") + "\n"))
    except:
        exit
 
    csvCreator(decodedResponse)
 
 
def csvCreator(response):
 
    with open("Final.csv", mode='a', newline='') as csv_file:
        writer = csv.writer(csv_file)
 
        if csv_file.tell() == 0:
            header = ["IP Address", "Domain Name", "Abuse Confidence Score","Is Whitelisted", "Country Code", "Internet Service Provider", "Total Reports", "Last Reported Date", "Actions"]
            writer.writerow(header)
 
        ip_address = response["data"]["ipAddress"]
        domain = response["data"]["domain"]
        abuse_confidence_score = response["data"]["abuseConfidenceScore"]
        country_code = response["data"]["countryCode"]
        isp = response["data"]["isp"]
        total_reports = response["data"]["totalReports"]
        last_reported_date = response["data"]["lastReportedAt"]
        is_whitelisted = response["data"]["isWhitelisted"]
 
        if abuse_confidence_score > 4:
            take_actions = "Yes"
        else:
            take_actions = "No"
 
        data = [ip_address, domain, abuse_confidence_score, is_whitelisted, country_code, isp, total_reports, last_reported_date, take_actions]
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