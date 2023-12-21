from pyads import ADS
import argparse
import os
from colorama import *

def banner(): 

    banner1 = '''
        _    ____  ____ _____                        
       / \  |  _ \/ ___|_   _| __ __ _  ___ ___ _ __ 
      / _ \ | | | \___ \ | || '__/ _` |/ __/ _ \ '__|
     / ___ \| |_| |___) || || | | (_| | (_|  __/ |   
    /_/   \_\____/|____/ |_||_|  \__,_|\___\___|_| v1.0                                         
    
    Alternate Data Streams Extrator
    -------------------------------
    Coded by Kamran Saifullah & Shrefa Ashour
    https://cydefops.com/
    https://github.com/CyDefOps/project-killchain

    Usage: ADSTracer.py -h

'''
    print(Fore.GREEN + banner1 + Fore.RESET)

def tracer(file):
    
    if os.path.isfile(file):
        scanning = ADS(file)
        for stream in scanning:
            print(Fore.YELLOW + f"[+] File: {file}\n[+] Stream Found: {stream}\n\n{scanning.get_stream_content(stream)}\n" + Fore.RESET)

    elif os.path.isdir(file):
         for root, dirs, filenames in os.walk(file):
                for filename in filenames:
                    recurFile = os.path.join(root, filename)
                    scanning = ADS(recurFile)
                    for stream in scanning:
                          print(Fore.YELLOW + f"[+] File: {recurFile}\n[+] Stream Found: {stream}\n\n{scanning.get_stream_content(stream)}\n" + Fore.RESET)
                          
    else:
         print("No Stream Have Been Identified")
    

def main():

    banner()

    parser = argparse.ArgumentParser()
    parser.add_argument('-f', metavar="Single File", help="Path to a single file")
    parser.add_argument('-d', metavar="Directory", help="Path to directory containing files")
    args = vars(parser.parse_args())

    try:
        if args["f"]:
            tracer(args["f"])
        elif args["d"]:
            tracer(args["d"])
    except: KeyboardInterrupt


if __name__ == '__main__':
        main()