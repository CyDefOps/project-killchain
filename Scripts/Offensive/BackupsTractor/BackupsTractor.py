import os
import argparse

def banner():
    banner = """                                                 
    ____             __                   ______                __            
   / __ )____ ______/ /____  ______  ____/_  __/________ ______/ /_____  _____
  / __  / __ `/ ___/ //_/ / / / __ \/ ___// / / ___/ __ `/ ___/ __/ __ \/ ___/
 / /_/ / /_/ / /__/ ,< / /_/ / /_/ (__  )/ / / /  / /_/ / /__/ /_/ /_/ / /    
/_____/\__,_/\___/_/|_|\__,_/ .___/____//_/ /_/   \__,_/\___/\__/\____/_/     
                           /_/                                                

Coded By: Kamran Saifullah, Umar Javed
https://cydefops.com
https://github.com/CyDefOps/project-killchain

Usage: BackupsTractor.py <Search String>
    """
    print(banner)

def search_files(search_path, keyword):
    for root, dirs, files in os.walk(search_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if keyword.lower() in content.lower():
                        print(f"Found '{keyword}' in: {file_path}")
                    else:
                        print(f"Not Found '{keyword}' in: {file_path}")
            except Exception as e:
                print(f"Error reading {file_path}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Search for a keyword in Notepad++ backup files.")
    parser.add_argument("keyword", type=str, help="The string to search for in files.")

    args = parser.parse_args()

    user_folder_path = "C:\\Users"
    for user_name in os.listdir(user_folder_path):
        user_path = os.path.join(user_folder_path, user_name)
        backup_path = os.path.join(user_path, "AppData", "Roaming", "Notepad++", "backup")

        if os.path.exists(backup_path):
            print(f"Searching in {backup_path} for '{args.keyword}'\n")
            search_files(backup_path, args.keyword)

if __name__ == "__main__":
    banner()
    main()
