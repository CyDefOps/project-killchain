from email import policy
from email.parser import BytesParser
import re
from urllib.parse import urlparse
import hashlib
import json
from tabulate import tabulate
from html2text import html2text

def process_received_headers(received_headers):
    hop_info = []
    for i, header in enumerate(reversed(received_headers)):
        from_server = re.search(r'from (.+?) ', header)
        by_server = re.search(r'by (.+?) ', header)
        from_server = from_server.group(1) if from_server else "Unknown"
        by_server = by_server.group(1) if by_server else "Unknown"
        hop_info.append((i + 1, f"{from_server} -> {by_server}"))
    return hop_info

def analyze_eml(file_path):
    with open(file_path, "rb") as f:
        msg = BytesParser(policy=policy.default).parse(f)

    received_headers = msg.get_all("Received")
    auth_results = msg.get("Authentication-Results")
    
    received_headers = process_received_headers(received_headers)
    
    auth_results_list = []
    if auth_results:
        for item in auth_results.split(';'):
            kv = item.strip().split('=')
            if len(kv) == 2:
                auth_results_list.append((kv[0], kv[1]))

    body = None
    urls = []
    domains = []

    for part in msg.walk():
        if part.get_content_type() == 'text/plain':
            body = part.get_payload(decode=True).decode()
            break
        elif part.get_content_type() == 'text/html':
            html_body = part.get_payload(decode=True).decode()
            body = html2text(html_body)
            break

    if body:
        urls = re.findall(r'https?://\S+', body)
        domains = [urlparse(url).netloc for url in urls]

    attachments = []
    for part in msg.iter_attachments():
        content_type = part.get_content_type()
        content = part.get_payload(decode=True)
        file_hash = hashlib.sha256(content).hexdigest()
        attachments.append({'type': content_type, 'hash': file_hash})
    
    return {
        'received_headers': received_headers,
        'auth_results': auth_results,
        'domains': domains,
        'urls': urls,
        'attachments': attachments,
        'body': body
    }

if __name__ == "__main__":
    file_path = input("Enter the path of the .eml file to analyze: ")
    result = analyze_eml(file_path)

    print("\nReceived Headers:")
    print(tabulate(result['received_headers'], headers=['Hop', 'From/By Servers'], tablefmt='pretty'))

    if result['auth_results']:
        print("\nAuthentication Results:")
        print(result['auth_results'])

    print("\nEmail Content:")
    print('Domains:')
    for domain in set(result['domains']):
        print(domain)
    print('URLs:')
    for url in result['urls']:
        print(url)
    print(f"Attachments: {len(result['attachments'])}")

    print("\nEmail Body:")
    clean_body = re.sub(r'!\[.*\]\(.*\)', '', result.get('body', 'No plain text body available'))
    print(clean_body)