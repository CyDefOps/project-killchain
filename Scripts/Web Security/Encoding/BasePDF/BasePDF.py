import sys
from base64 import *
from colorama import *

def banner():
    
    starter = '''
 ______               __________________ 
| ___ \              | ___ \  _  \  ___|
| |_/ / __ _ ___  ___| |_/ / | | | |_   
| ___ \/ _` / __|/ _ \  __/| | | |  _|  
| |_/ / (_| \__ \  __/ |   | |/ /| |    
\____/ \__,_|___/\___\_|   |___/ \_|    

 Base64 to PDF File Generator
 ------------------------------
 Coded by Kamran Saifullah - Frog Man
 Twitter: https://twitter.com/deFr0ggy 
 GitHub: https://github.com/CyDefOps/project-killchain/
 LinkedIn: https://linkedin.com/in/kamransaifullah 
 Website: https://cydefops.com/

 Usage: ./BasePDF.py <Base64 File>
    
    '''
    
    print(Fore.GREEN + starter)

def BasePDF(data):
    
    try:

        f = open(sys.argv[1], "r")
        encodedData = f.read()
        decodedData = b64decode(encodedData)

        if decodedData[0:4] != b'%PDF':
            raise ValueError('Missing the PDF file signature')
        else:
            sample = open('sample.pdf', 'wb')
            sample.write(decodedData)
            sample.close()
            print(Fore.YELLOW + "File Has Been Created!\n")
        

    except:
        print(Fore.RED + "Base64 Encoded Data Cannot Be Validated!")

def main():

    banner()
    if len(sys.argv) < 2 or len(sys.argv) > 2:
            print("Invalid Arguments Provided!")
    else:
        BasePDF(sys.argv[1])

if __name__ =='__main__':
    main()