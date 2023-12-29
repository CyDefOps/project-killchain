import sys
import os
import hashlib
import csv
from colorama import *

def banner():

    gogo = '''

 __  __     ______     ______     __  __     ______     ______    
/\ \_\ \   /\  __ \   /\  ___\   /\ \_\ \   /\  ___\   /\  == \   
\ \  __ \  \ \  __ \  \ \___  \  \ \  __ \  \ \  __\   \ \  __<   
 \ \_\ \_\  \ \_\ \_\  \/\_____\  \ \_\ \_\  \ \_____\  \ \_\ \_\ 
  \/_/\/_/   \/_/\/_/   \/_____/   \/_/\/_/   \/_____/   \/_/ /_/ v1.0
                                                                    
 An Automated Hash Calculator
 ------------------------------
 Coded by Kamran Saifullah
 https://cydefops.com/
 https://github.com/CyDefOps/project-killchain

 Usage: python3 Hasher.py File/Directory
    
    '''

    print(Fore.YELLOW + gogo)

def hashMe(sample):
    
    try:

        md5 = hashlib.md5()
        sha1 = hashlib.sha1()
        sha256 = hashlib.sha256()
        sha512 = hashlib.sha512()

        md5Hash = md5.hexdigest()
        sha1Hash = sha1.hexdigest()
        sha256Hash = sha256.hexdigest()
        sha512Hash = sha512.hexdigest()
        
        with open(sample, "rb") as file:
            EOF = 0
            while EOF != b'':
                EOF = file.read()
                md5.update(EOF)
                sha512.update(EOF)
                sha256.update(EOF)
                sha1.update(EOF)

        print(Fore.GREEN + "MD5: " + Fore.LIGHTMAGENTA_EX + md5Hash)
        print(Fore.GREEN + "SHA1: " + Fore.LIGHTMAGENTA_EX + sha1Hash)
        print(Fore.GREEN + "SHA256: " + Fore.LIGHTMAGENTA_EX + sha256Hash)
        print(Fore.GREEN + "SHA512: " + Fore.LIGHTMAGENTA_EX + sha512Hash)
        print(Fore.RESET)

        with open('hashes.csv', 'a', newline='') as hashed:
            writer = csv.writer(hashed)
            if hashed.tell() == 0:
                header = ["File Name", "MD5", "SHA1", "SHA256", "SHA512"]
                writer.writerow(header)

            data = [sample, md5Hash, sha1Hash, sha256Hash, sha512Hash]
            writer.writerow(data)

    except:
        print("Nano!")

def main():

    banner()

    if len(sys.argv) < 2 or len(sys.argv) > 2:
        print("Invalid Arguments Provided!")
    else:
        if os.path.isfile(sys.argv[1]):
            print(Fore.WHITE + "File Name: ", sys.argv[1] + "\n" + Fore.RESET)
            hashMe(sys.argv[1])

        if os.path.isdir(sys.argv[1]):

            for root, dirs, filenames in os.walk(sys.argv[1]):
                for filename in filenames:
                    recurFile = os.path.join(root, filename)
                    print(Fore.WHITE + "File Name: ", recurFile + "\n" + Fore.RESET)
                    hashMe(recurFile)
               
if __name__ == '__main__':
    main()