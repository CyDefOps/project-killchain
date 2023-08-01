import re
import os

def process_bind_file():
    bind_file_path = input("Please enter the path to your BIND file: ")

    base_file_path = os.path.splitext(bind_file_path)[0]

    output_file_path = f"{base_file_path}.txt"

    with open(bind_file_path, 'r') as f:
        content = f.readlines()

    content = content[2:]

    new_content = []
    for line in content:
        line = re.sub(r"^\\\d{1,3}", "@", line)

        line = re.sub(r"AWS\tALIAS\tA{1,4}", "IN\tCNAME", line)

        line = re.sub(r"\s\w{14}\s(true|false)$", "", line)
        
        new_content.append(line)

    with open(output_file_path, 'w') as f:
        f.writelines(new_content)

process_bind_file()