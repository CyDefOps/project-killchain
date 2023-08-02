import sys
import pefile
import colorama
import magic
import hashlib
from colorama import Fore

colorama.init(autoreset=True)

mtype = {
    "0x0" : "any machine type",
    "0x1d3" : "Matsushita AM33",
    "0x8664" : "x64",
    "0x1c0" : "ARM little endian",
    "0xaa64" : "ARM64 little endian",
    "0x1c4" : "ARM Thumb-2 little endian",
    "0xebc" : "EFI byte code",
    "0x14c" : "Intel 386 or later processors and compatible processors",
    "0x200" : "Intel Itanium processor family",
    "0x6232" : "LoongArch 32-bit processor family",
    "0x6264" : "LoongArch 64-bit processor family",
    "0x9041" : "Mitsubishi M32R little endian",
    "0x266" : "MIPS16",
    "0x366" : "MIPS with FPU",
    "0x466" : "MIPS16 with FPU",
    "0x1f0" : "Power PC little endian",
    "0x1f1" : "Power PC with floating point support",
    "0x166" : "MIPS little endian",
    "0x5032" : "RISC-V 32-bit address space",
    "0x5064" : "RISC-V 64-bit address space",
    "0x5128" : "RISC-V 128-bit address space",
    "0x1a2" : "Hitachi SH3",
    "0x1a3" : "Hitachi SH3 DSP",
    "0x1a6" : "Hitachi SH4",
    "0x1a8" : "Hitachi SH5",
    "0x1c2" : "Thumb",
    "0x169" : "MIPS little-endian WCE v2"
}

sigValues = {
    "0x4550" : "PE Executable",
    "0x19b" : "PE32 Executable",
    "0x20b" : "PE64 Executable",
    "0x19B" : "PE32 Executable",
    "0x20B" : "PE64 Executable"
}

def banner():

    banned = """

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
    
    """
    print(Fore.YELLOW + banned)

def hashCalc(file):

    print(Fore.BLUE + "[+] Calculating File Hashes\n")

    try:
        sameplFile = file
        md5 = hashlib.md5()
        sha1 = hashlib.sha1()
        sha256 = hashlib.sha256()
        sha512 = hashlib.sha512()

        with open(sameplFile, "rb") as file:
            EOF = 0
            while EOF != b'':
                EOF = file.read()
                md5.update(EOF)
                sha512.update(EOF)
                sha256.update(EOF)
                sha1.update(EOF)

        print(Fore.GREEN + "MD5: " + Fore.LIGHTMAGENTA_EX + md5.hexdigest())
        print(Fore.GREEN + "SHA1: " + Fore.LIGHTMAGENTA_EX + sha1.hexdigest())
        print(Fore.GREEN + "SHA256: " + Fore.LIGHTMAGENTA_EX + sha256.hexdigest())
        print(Fore.GREEN + "SHA512: " + Fore.LIGHTMAGENTA_EX + sha512.hexdigest())
        print(Fore.RESET)

    except:
        print(Fore.RED + "[+] Nano Hashes! Check Manually!") 

    

def realWork(file):
    
    print(Fore.BLUE + "[+] File Type: " + Fore.RESET + magic.from_file(file)) 

    hashCalc(file)

    try:

        # Loading the file
        analysis = pefile.PE(file, fast_load=True)
        analysis.parse_data_directories()
        
        # Printing the DOS Header

        if hex(analysis.DOS_HEADER.e_magic) == '0x5a4d' or '0x5A4D':
            
            print(Fore.BLUE + "[+] DOS Header:" + Fore.RESET + " MZ (0x5a4d)")
            print(Fore.BLUE + "[+] PE Pointer Header: " + Fore.RESET + hex(analysis.DOS_HEADER.e_lfanew))
            print(Fore.BLUE + "[+] No of Sections: " + Fore.RESET + hex(analysis.FILE_HEADER.NumberOfSections))
            print(Fore.BLUE + "[+] Characteristics: " + Fore.RESET + hex(analysis.FILE_HEADER.Characteristics))
            print(Fore.BLUE + "[+] File Creation Date : " + Fore.RESET + analysis.FILE_HEADER.dump_dict()['TimeDateStamp']['Value'].split('[')[1][:-1])

            if hex(analysis.NT_HEADERS.Signature) in sigValues:
    
                print(Fore.BLUE + "[+] Signature: "  + Fore.RESET + sigValues[hex(analysis.NT_HEADERS.Signature)] + " - " + hex(analysis.NT_HEADERS.Signature))

            else:

                print(Fore.RED + "[+] Signature: " + hex(analysis.NT_HEADERS.Signature))
            
            if hex(analysis.FILE_HEADER.Machine) in mtype:

                print(Fore.BLUE + "[+] File Architecture: " + Fore.RESET + mtype[hex(analysis.FILE_HEADER.Machine)])

            else:

                print(Fore.BLUE + "[+] File Architecture: " + Fore.RESET + hex(analysis.FILE_HEADER.Machine)) 

            print(Fore.BLUE + "\n[+] PE Sections\n")

            for sect in analysis.sections:
                
                print(Fore.CYAN + sect.Name.decode().rstrip('\x00') + Fore.RESET + "\n\nVitual Size : " + hex(sect.Misc_VirtualSize) + "\n\nVirutalAddress : " + hex(sect.VirtualAddress) + "\n\nSizeOfRawData : " + hex(sect.SizeOfRawData) + "\n\nPointerToRawData : " + hex(sect.PointerToRawData) + "\n\nCharacterisitcs : " + hex(sect.Characteristics)+'\n')  

            print(Fore.BLUE + "[+] Imported Modules\n")

            for entry in analysis.DIRECTORY_ENTRY_IMPORT:
                
                dllEntries = entry.dll
                print(Fore.GREEN + dllEntries.decode())

                for imp in entry.imports:

                    dllImports = imp
                    print('\t', dllImports.address, dllImports.name)

        else:
            print(Fore.RED + "[x] Manually validate the file!")

    except pefile.PEFormatError:
        print("DOS Header Magic Not Found")

def main():
    
    if len(sys.argv) < 2 or len(sys.argv) > 2:
        print("Invalid Arguments Provided!")
    else:
        banner()
        realWork(sys.argv[1])

if __name__ == '__main__':
    main()
