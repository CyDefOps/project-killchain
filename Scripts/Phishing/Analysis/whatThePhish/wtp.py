import argparse
import extract_msg
import re
from urllib.parse import urlparse, unquote
from bs4 import BeautifulSoup
import os

header = r"""
 __    __ _           _  _____ _            ___ _     _     _     
/ / /\ \ \ |__   __ _| |/__   \ |__   ___  / _ \ |__ (_)___| |__  
\ \/  \/ / '_ \ / _ | __|/ /\/ '_ \ / _ \/ /_)/ '_ \| / __| '_ \ 
 \  /\  /| | | | (_| | |_/ /  | | | |  __/ ___/| | | | \__ \ | | |
  \/  \/ |_| |_|\__,_|\__\/   |_| |_|\___\/    |_| |_|_|___/_| |_| v1.1
A super rapid email phishing analysis tool. 
------------------------------------------------------
GitHub: https://github.com/CyDefOps/project-killchain/
Made with ❤️ by KayaSEC + CC
❗Usage: python3 wtp.py -msg <path_to_msg_file>
"""

os.environ['FORCE_COLOR'] = '1'

# ANSI color codes
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def setup_argparse():
    parser = argparse.ArgumentParser(description="What's The Phish - A rapid email phishing analysis tool.")
    parser.add_argument('-msg', '--message', required=True, help='Path to the .msg file to analyze')
    return parser.parse_args()

def print_banner(text, color=Colors.BLUE):
    banner_width = 80
    print(f"\n{color}{Colors.BOLD}{'=' * banner_width}")
    print(f"{text:^{banner_width}}")
    print(f"{'=' * banner_width}{Colors.ENDC}")

def print_section(title):
    print(f"\n{Colors.GREEN}{Colors.BOLD}{title}")
    print(f"{'-' * len(title)}{Colors.ENDC}")

def print_key_value(key, value, color=Colors.BLUE):
    print(f"{color}{key}:{Colors.ENDC} {value}")

def decode_safelinks(url):
    parsed = urlparse(url)
    if parsed.netloc.endswith('.protection.outlook.com'):
        query = dict(q.split('=') for q in parsed.query.split('&'))
        if 'url' in query:
            return unquote(query['url'])
    return url

def decode_urls_in_text(text):
    def replace_url(match):
        url = match.group(0)
        decoded_url = decode_safelinks(url)
        if decoded_url != url:
            return f"{Colors.BOLD}{Colors.BLUE}LINK: {decoded_url}{Colors.ENDC} {Colors.YELLOW}[SafeLinks]{Colors.ENDC}"
        else:
            return f"{Colors.BOLD}{Colors.BLUE}LINK: {url}{Colors.ENDC}"
    
    url_pattern = r'https?://\S+'
    return re.sub(url_pattern, replace_url, text)

def analyze_msg_file(file_path):
    msg = extract_msg.Message(file_path)
    
    subject = msg.subject
    sender = msg.sender
    to = msg.to
    cc = msg.cc
    
    headers = dict(msg.header)
    
    body = msg.body
    
    # Extract plain text from HTML if body is HTML
    if body.strip().startswith('<'):
        soup = BeautifulSoup(body, 'html.parser')
        body = soup.get_text(separator='\n', strip=True)
    
    # Decode URLs in the body
    body = decode_urls_in_text(body)
    
    urls = re.findall(r'https?://\S+', body)
    urls = [decode_safelinks(url.rstrip('>')) for url in urls]
    domains = list(set([urlparse(url).netloc for url in urls]))
    
    # Phishing Sim Detection Module
    has_received_headers = any(header.startswith('Received:') for header in headers)
    has_antispam_headers = any('X-Microsoft-Antispam' in header for header in headers)
    has_authentication_results = 'Authentication-Results' in headers
    
    is_phishing_sim = has_antispam_headers and not has_received_headers and not has_authentication_results
    
    return {
        'subject': subject,
        'from': sender,
        'to': to,
        'cc': cc,
        'headers': headers,
        'urls': urls,
        'domains': domains,
        'body': body,
        'is_phishing_sim': is_phishing_sim
    }

def main():
    global header
    print(header)
    args = setup_argparse()
    file_path = args.message
    result = analyze_msg_file(file_path)

    print_banner("Email Analysis Report", Colors.BLUE)

    print_section("Email Details")
    print_key_value("Subject", result['subject'])
    print_key_value("From", result['from'])
    print_key_value("To", result['to'])
    print_key_value("CC", result['cc'] if result['cc'] else "None")

    if result['is_phishing_sim']:
        print_banner("WARNING: Potential Phishing Simulation", Colors.YELLOW)
        print(f"{Colors.YELLOW}This email contains Microsoft anti-spam headers but lacks typical email routing headers.")
        print(f"It may be part of a phishing awareness exercise.{Colors.ENDC}")
    else:
        print_banner("Standard Email", Colors.GREEN)
        print(f"{Colors.GREEN}This appears to be a standard email with expected headers.{Colors.ENDC}")

    print_section("Key Headers")
    important_headers = ['Received', 'Authentication-Results', 'SPF', 'DKIM', 'DMARC', 'X-Microsoft-Antispam']
    for header, value in result['headers'].items():
        if any(h.lower() in header.lower() for h in important_headers):
            print_key_value(header, value, Colors.YELLOW)

    print_section("Domains")
    for domain in result['domains']:
        print(domain)

    print_section("Decoded URLs")
    for url in result['urls']:
        print(url)

    print_section("Email Body (with decoded URLs)")
    print(result['body'])

    print_banner("End of Report", Colors.BLUE)

if __name__ == "__main__":
    main()