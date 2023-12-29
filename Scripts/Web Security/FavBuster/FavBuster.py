import requests
import mmh3
import base64
import argparse
from colorama import *

def banner():

    banned = '''

   ___            ___           _            
  / __\_ ___   __/ __\_   _ ___| |_ ___ _ __ 
 / _\/ _` \ \ / /__\// | | / __| __/ _ \ '__|
/ / | (_| |\ V / \/  \ |_| \__ \ ||  __/ |   
\/   \__,_| \_/\_____/\__,_|___/\__\___|_|   
                                             v1.0

 FavBuster - Favicon MMH3 Hash Calculator
 ------------------------------
 Coded by Kamran Saifullah & Shrefa Ashour
 GitHub: https://github.com/CyDefOps/project-killchain
 Website: https://cydefops.com/

 Usage: ./FavBuster.py -h

'''
    print(Fore.YELLOW + banned)

def urlFavicon(URL): 

    try:
        response = requests.get(URL)

        if response.status_code == 200:
            favicon = base64.encodebytes(response.content)
            finalHash = mmh3.hash(favicon)
            print(Fore.CYAN + f"Favicon URL: {URL}\n")
            print(Fore.GREEN + f"[Hash] {mmh3.hash(favicon)}")
            print(Fore.GREEN + f"[Shodan Query] http.favicon.hash:{mmh3.hash(favicon)}")
            print(Fore.GREEN + f"[FOFA Query] icon_hash=\"{mmh3.hash(favicon)}\"")
            print(Fore.GREEN + f"[ZoomEye Query] iconhash:\"{mmh3.hash(favicon)}\"")
            

    except:
        print("Something Went Wrong")
    
def fileFavicon(File):

    with open(File, 'rb') as gotCha:
        content = gotCha.read()
        encodeContent = base64.encodebytes(content)
        print(Fore.CYAN + f"File: {File}\n")
        print(Fore.GREEN + f"[Hash] {mmh3.hash(encodeContent)}")
        print(Fore.GREEN + f"[Shodan Query] http.favicon.hash:{mmh3.hash(encodeContent)}")
        print(Fore.GREEN + f"[FOFA Query] icon_hash=\"{mmh3.hash(encodeContent)}\"")

def main():

    banner()

    parser = argparse.ArgumentParser()
    parser.add_argument('-url', metavar="URL", help="Favicon URL")
    parser.add_argument('-file', metavar="favicon.ico", help="Favicon File")
    args = vars(parser.parse_args())

    try:
        if args["url"]:
            urlFavicon(args["url"])
        elif args["file"]:
            fileFavicon(args["file"])
    except: KeyboardInterrupt
    
if __name__ == '__main__':
    main()