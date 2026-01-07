#!/usr/bin/env python3
"""
PersonnaTracker v3.0 - Advanced OSINT Tool
Author: Artemis37
No API keys required
"""

import requests
import json
import argparse
import time
import re
import sys
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'

class PersonnaTracker:
    def __init__(self, timeout=10, verbose=False):
        self.timeout = timeout
        self.verbose = verbose
        self.results = {
            'username': None,
            'email': None,
            'phone': None,
            'timestamp': datetime.now().isoformat(),
            'found_accounts': [],
            'total_found': 0,
            'platforms_checked': 0
        }
        
        self.platforms = {
            'Instagram': {'url': 'https://www.instagram.com/{}/', 'error_msg': 'Sorry, this page isn\'t available'},
            'Twitter': {'url': 'https://twitter.com/{}', 'error_msg': 'This account doesn\'t exist'},
            'GitHub': {'url': 'https://github.com/{}', 'error_msg': 'Not Found'},
            'Reddit': {'url': 'https://www.reddit.com/user/{}', 'error_msg': 'page not found'},
            'TikTok': {'url': 'https://www.tiktok.com/@{}', 'error_msg': 'Couldn\'t find this account'},
            'YouTube': {'url': 'https://www.youtube.com/@{}', 'error_msg': 'This page isn\'t available'},
            'Facebook': {'url': 'https://www.facebook.com/{}', 'error_msg': 'This content isn\'t available'},
            'LinkedIn': {'url': 'https://www.linkedin.com/in/{}', 'error_msg': 'Page not found'},
            'Pinterest': {'url': 'https://www.pinterest.com/{}/', 'error_msg': 'Sorry!'},
            'Tumblr': {'url': 'https://{}.tumblr.com', 'error_msg': 'There\'s nothing here'},
            'Medium': {'url': 'https://medium.com/@{}', 'error_msg': 'Page not found'},
            'Dev.to': {'url': 'https://dev.to/{}', 'error_msg': '404'},
            'GitLab': {'url': 'https://gitlab.com/{}', 'error_msg': 'The repository for this page has been moved'},
            'HackerOne': {'url': 'https://hackerone.com/{}', 'error_msg': 'Page not found'},
            'HackerRank': {'url': 'https://www.hackerrank.com/{}', 'error_msg': 'Something went wrong'},
            'CodePen': {'url': 'https://codepen.io/{}', 'error_msg': 'Page Not Found'},
            'StackOverflow': {'url': 'https://stackoverflow.com/users/{}', 'error_msg': 'User not found'},
            'Kaggle': {'url': 'https://www.kaggle.com/{}', 'error_msg': 'not found'},
            'Twitch': {'url': 'https://www.twitch.tv/{}', 'error_msg': 'Sorry. Unless you\'ve got a time machine'},
            'Steam': {'url': 'https://steamcommunity.com/id/{}', 'error_msg': 'The specified profile could not be found'},
            'Discord': {'url': 'https://discord.com/users/{}', 'error_msg': 'User not found'},
            'Telegram': {'url': 'https://t.me/{}', 'error_msg': 'If you have Telegram'},
            'Spotify': {'url': 'https://open.spotify.com/user/{}', 'error_msg': 'Page not found'},
            'SoundCloud': {'url': 'https://soundcloud.com/{}', 'error_msg': 'Sorry! Something went wrong'},
            'Behance': {'url': 'https://www.behance.net/{}', 'error_msg': 'Oops!'},
            'Dribbble': {'url': 'https://dribbble.com/{}', 'error_msg': 'Whoops, that page is gone'},
            'AngelList': {'url': 'https://angel.co/u/{}', 'error_msg': 'doesn\'t exist'},
            'Patreon': {'url': 'https://www.patreon.com/{}', 'error_msg': 'Page Not Found'},
            'Flickr': {'url': 'https://www.flickr.com/people/{}', 'error_msg': 'doesn\'t exist'},
            'Vimeo': {'url': 'https://vimeo.com/{}', 'error_msg': 'There is no such user'},
            '500px': {'url': 'https://500px.com/p/{}', 'error_msg': 'Page Not Found'},
            'AboutMe': {'url': 'https://about.me/{}', 'error_msg': 'page not found'},
            'ProductHunt': {'url': 'https://www.producthunt.com/@{}', 'error_msg': 'Not Found'},
            'Goodreads': {'url': 'https://www.goodreads.com/{}', 'error_msg': 'Page not found'},
            'Lastfm': {'url': 'https://www.last.fm/user/{}', 'error_msg': 'Whoops, this page doesn\'t exist'},
            'Keybase': {'url': 'https://keybase.io/{}', 'error_msg': 'doesn\'t exist'},
            'HackerNews': {'url': 'https://news.ycombinator.com/user?id={}', 'error_msg': 'No such user'},
            'Mastodon': {'url': 'https://mastodon.social/@{}', 'error_msg': 'The page you are looking for isn\'t here'},
            'Quora': {'url': 'https://www.quora.com/profile/{}', 'error_msg': 'Page Not Found'},
            'Replit': {'url': 'https://replit.com/@{}', 'error_msg': 'page not found'},
            'Hackster': {'url': 'https://www.hackster.io/{}', 'error_msg': 'Page not found'},
        }

    def print_banner(self):
        banner = f"""
{Colors.CYAN}╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║   {Colors.BOLD}PersonnaTracker v2.0{Colors.END}{Colors.CYAN} - Advanced OSINT Tool           ║
║   {Colors.YELLOW}Author: Artemis37{Colors.END}{Colors.CYAN} | {len(self.platforms)} Platforms              ║
║   {Colors.GREEN}No API Keys Required{Colors.END}{Colors.CYAN} | Pure Intelligence         ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝{Colors.END}
        """
        print(banner)

    def get_session(self):
        session = requests.Session()
        session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'DNT': '1',
            'Connection': 'keep-alive',
        })
        return session

    def check_platform(self, platform_name, platform_data, username):
        url = platform_data['url'].format(username)
        session = self.get_session()
        
        try:
            response = session.get(url, timeout=self.timeout, allow_redirects=True)
            
            if response.status_code == 200:
                if platform_data['error_msg'].lower() not in response.text.lower():
                    return {'platform': platform_name, 'url': url, 'status': 'FOUND', 'status_code': response.status_code}
            return None
            
        except requests.exceptions.Timeout:
            if self.verbose:
                print(f"{Colors.YELLOW}[!] Timeout: {platform_name}{Colors.END}")
            return None
        except requests.exceptions.RequestException:
            if self.verbose:
                print(f"{Colors.RED}[!] Error: {platform_name}{Colors.END}")
            return None

    def search_username(self, username):
        self.results['username'] = username
        self.results['platforms_checked'] = len(self.platforms)
        
        print(f"\n{Colors.BOLD}[*] Target: {Colors.GREEN}{username}{Colors.END}")
        print(f"{Colors.BOLD}[*] Scanning {len(self.platforms)} platforms...{Colors.END}\n")
        
        start_time = time.time()
        found_count = 0
        
        print(f"{Colors.CYAN}[*] Working... (~60 seconds){Colors.END}\n")
        
        with ThreadPoolExecutor(max_workers=30) as executor:
            future_to_platform = {
                executor.submit(self.check_platform, name, data, username): name 
                for name, data in self.platforms.items()
            }
            
            for future in as_completed(future_to_platform):
                result = future.result()
                
                if result:
                    found_count += 1
                    self.results['found_accounts'].append(result)
                    print(f"{Colors.GREEN}[+] {result['platform']:20} {Colors.CYAN}{result['url']}{Colors.END}")
        
        elapsed_time = time.time() - start_time
        self.results['total_found'] = found_count
        
        print(f"\n{Colors.BOLD}{'='*60}{Colors.END}")
        print(f"{Colors.BOLD}[*] Complete | Found: {Colors.GREEN}{found_count}{Colors.END}{Colors.BOLD}/{len(self.platforms)} | Time: {elapsed_time:.2f}s{Colors.END}")
        print(f"{Colors.BOLD}{'='*60}{Colors.END}\n")
        
        return found_count > 0

    def check_email(self, email):
        self.results['email'] = email
        print(f"\n{Colors.BOLD}[*] Email Analysis: {Colors.GREEN}{email}{Colors.END}\n")
        
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        is_valid = bool(re.match(email_pattern, email))
        
        if is_valid:
            print(f"{Colors.GREEN}[+] Valid format{Colors.END}")
            username = email.split('@')[0]
            domain = email.split('@')[1]
            
            print(f"{Colors.CYAN}[*] Username: {username}{Colors.END}")
            print(f"{Colors.CYAN}[*] Domain: {domain}{Colors.END}")
            
            variations = [username, username.replace('.', ''), username.replace('_', ''), username.split('.')[0] if '.' in username else username]
            
            print(f"\n{Colors.BOLD}[*] Username variations:{Colors.END}")
            for var in set(variations):
                print(f"  {Colors.CYAN}- {var}{Colors.END}")
        else:
            print(f"{Colors.RED}[!] Invalid format{Colors.END}")

    def check_phone(self, phone):
        self.results['phone'] = phone
        print(f"\n{Colors.BOLD}[*] Phone Number Intelligence: {Colors.GREEN}{phone}{Colors.END}\n")
        
        cleaned = re.sub(r'[^\d+]', '', phone)
        
        country_codes = {
            '226': {'country': 'Burkina Faso', 'format': '+226 XX XX XX XX', 'operators': {
                '5': 'Orange BF', '6': 'Orange BF', '7': 'Telecel Faso', '01': 'Moov Africa', '02': 'Moov Africa',
                '03': 'Moov Africa', '04': 'Moov Africa', '05': 'Moov Africa', '51': 'Orange BF', '52': 'Orange BF',
                '53': 'Orange BF', '54': 'Orange BF', '55': 'Orange BF', '56': 'Orange BF', '57': 'Orange BF',
                '58': 'Orange BF', '59': 'Orange BF', '60': 'Orange BF', '61': 'Orange BF', '62': 'Orange BF',
                '63': 'Orange BF', '64': 'Orange BF', '65': 'Orange BF', '66': 'Orange BF', '67': 'Orange BF',
                '68': 'Orange BF', '69': 'Orange BF', '70': 'Telecel Faso', '71': 'Telecel Faso', '72': 'Telecel Faso',
                '73': 'Telecel Faso', '74': 'Telecel Faso', '75': 'Telecel Faso', '76': 'Telecel Faso', '77': 'Telecel Faso',
                '78': 'Telecel Faso', '79': 'Telecel Faso'
            }},
            '33': {'country': 'France', 'format': '+33 X XX XX XX XX'},
            '1': {'country': 'USA/Canada', 'format': '+1 XXX XXX XXXX'},
            '44': {'country': 'United Kingdom', 'format': '+44 XXXX XXXXXX'},
            '225': {'country': 'Côte d\'Ivoire', 'format': '+225 XX XX XX XX XX'},
            '223': {'country': 'Mali', 'format': '+223 XX XX XX XX'},
            '227': {'country': 'Niger', 'format': '+227 XX XX XX XX'},
            '228': {'country': 'Togo', 'format': '+228 XX XX XX XX'},
            '229': {'country': 'Benin', 'format': '+229 XX XX XX XX'},
            '221': {'country': 'Senegal', 'format': '+221 XX XXX XX XX'},
            '234': {'country': 'Nigeria', 'format': '+234 XXX XXX XXXX'},
            '212': {'country': 'Morocco', 'format': '+212 XXX XXXXXX'},
            '213': {'country': 'Algeria', 'format': '+213 XXX XX XX XX'},
            '216': {'country': 'Tunisia', 'format': '+216 XX XXX XXX'},
            '27': {'country': 'South Africa', 'format': '+27 XX XXX XXXX'},
            '20': {'country': 'Egypt', 'format': '+20 XXX XXX XXXX'},
        }
        
        detected_country = None
        operator = None
        
        if cleaned.startswith('+226') or (len(cleaned) == 8 and cleaned[0] in ['5', '6', '7', '0']):
            if not cleaned.startswith('+'):
                cleaned = '+226' + cleaned
            detected_country = 'Burkina Faso'
            
            number_part = cleaned.replace('+226', '')
            if len(number_part) >= 2:
                prefix = number_part[:2]
                if prefix in country_codes['226']['operators']:
                    operator = country_codes['226']['operators'][prefix]
                else:
                    prefix = number_part[0]
                    if prefix in country_codes['226']['operators']:
                        operator = country_codes['226']['operators'][prefix]
        else:
            for code, info in country_codes.items():
                if cleaned.startswith(f'+{code}'):
                    detected_country = info['country']
                    break
        
        print(f"{Colors.CYAN}[*] Formatted: {cleaned}{Colors.END}")
        if detected_country:
            print(f"{Colors.GREEN}[+] Country: {detected_country}{Colors.END}")
        if operator:
            print(f"{Colors.GREEN}[+] Operator: {operator}{Colors.END}")
        
        variations = [
            cleaned,
            cleaned.replace('+', ''),
            cleaned.replace('+226', '0') if '+226' in cleaned else cleaned,
        ]
        
        print(f"\n{Colors.BOLD}[*] Number variations:{Colors.END}")
        for var in set(variations):
            print(f"  {Colors.CYAN}- {var}{Colors.END}")
        
        social_platforms = {
            'WhatsApp': f'https://wa.me/{cleaned.replace("+", "")}',
            'Telegram': f'https://t.me/{cleaned.replace("+", "")}',
            'Viber': f'viber://chat?number={cleaned.replace("+", "")}',
            'Signal': f'Signal number: {cleaned}',
        }
        
        print(f"\n{Colors.BOLD}[*] Social Media Links:{Colors.END}")
        for platform, link in social_platforms.items():
            print(f"  {Colors.GREEN}[+] {platform:12} {Colors.CYAN}{link}{Colors.END}")
        
        dorks = [
            f'"{cleaned}"',
            f'"{cleaned.replace("+", "")}"',
            f'"{phone}"',
            f'"{cleaned}" site:facebook.com',
            f'"{cleaned}" site:linkedin.com',
            f'"{cleaned}" site:twitter.com',
            f'"{cleaned}" intext:"contact" OR intext:"tel"',
            f'"{cleaned}" site:pagesjaunes.bf' if detected_country == 'Burkina Faso' else f'"{cleaned}" intext:"contact"',
            f'"{cleaned}" OR "{cleaned.replace("+226", "0")}"' if '+226' in cleaned else f'"{cleaned}"',
        ]
        
        print(f"\n{Colors.BOLD}[*] Google Dorks:{Colors.END}")
        for dork in dorks:
            print(f"  {Colors.CYAN}{dork}{Colors.END}")
        
        if detected_country == 'Burkina Faso':
            print(f"\n{Colors.YELLOW}[*] Burkina Faso Specific Resources:{Colors.END}")
            print(f"  {Colors.CYAN}- Check pagesjaunes.bf (Yellow Pages){Colors.END}")
            print(f"  {Colors.CYAN}- Check local business directories{Colors.END}")
            print(f"  {Colors.CYAN}- Try WhatsApp/Telegram with {cleaned}{Colors.END}")
            print(f"  {Colors.CYAN}- Search on Facebook with phone number{Colors.END}")

    def google_dorks(self, query):
        print(f"\n{Colors.BOLD}[*] Google Dorks: {Colors.GREEN}{query}{Colors.END}\n")
        
        dorks = [
            f'"{query}"',
            f'"{query}" site:linkedin.com',
            f'"{query}" site:github.com',
            f'"{query}" site:twitter.com',
            f'"{query}" site:facebook.com',
            f'"{query}" site:instagram.com',
            f'"{query}" intext:"email" OR intext:"contact"',
            f'"{query}" site:pastebin.com',
            f'"{query}" filetype:pdf',
            f'"{query}" inurl:profile',
            f'"{query}" site:reddit.com',
            f'"{query}" site:medium.com',
        ]
        
        for dork in dorks:
            print(f"  {Colors.CYAN}{dork}{Colors.END}")

    def save_report(self, filename=None):
        if not filename:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            target = self.results.get('username') or self.results.get('email') or 'unknown'
            filename = f'personnatracker_{target}_{timestamp}.json'
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.results, f, indent=2, ensure_ascii=False)
        
        print(f"{Colors.GREEN}[+] Report saved: {filename}{Colors.END}")
        
        txt_filename = filename.replace('.json', '.txt')
        with open(txt_filename, 'w', encoding='utf-8') as f:
            f.write("=" * 60 + "\n")
            f.write("PersonnaTracker OSINT Report\n")
            f.write(f"Author: Artemis37\n")
            f.write("=" * 60 + "\n\n")
            f.write(f"Target: {self.results.get('username') or self.results.get('email') or 'N/A'}\n")
            f.write(f"Date: {self.results['timestamp']}\n")
            f.write(f"Found: {self.results['total_found']} accounts\n\n")
            
            f.write("FOUND ACCOUNTS:\n")
            f.write("-" * 60 + "\n")
            for account in self.results['found_accounts']:
                f.write(f"[+] {account['platform']:20} {account['url']}\n")
        
        print(f"{Colors.GREEN}[+] Text report: {txt_filename}{Colors.END}")

def main():
    parser = argparse.ArgumentParser(
        description='PersonnaTracker v2.0 - Advanced OSINT Tool by Artemis37',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 personnatracker.py -u username
  python3 personnatracker.py -u username -o report.json
  python3 personnatracker.py -e email@example.com
  python3 personnatracker.py -p +1234567890
  python3 personnatracker.py -g "John Doe"
        """
    )
    
    parser.add_argument('-u', '--username', help='Username to search')
    parser.add_argument('-e', '--email', help='Email to analyze')
    parser.add_argument('-p', '--phone', help='Phone number to analyze')
    parser.add_argument('-g', '--google', help='Generate Google dorks')
    parser.add_argument('-o', '--output', help='Output filename (JSON)')
    parser.add_argument('-t', '--timeout', type=int, default=10, help='Timeout (default: 10s)')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose mode')
    
    args = parser.parse_args()
    
    tracker = PersonnaTracker(timeout=args.timeout, verbose=args.verbose)
    tracker.print_banner()
    
    if not any([args.username, args.email, args.phone, args.google]):
        parser.print_help()
        sys.exit(0)
    
    if args.username:
        found = tracker.search_username(args.username)
        if found and args.output:
            tracker.save_report(args.output)
        elif found:
            save = input(f"\n{Colors.YELLOW}[?] Save report? (y/n): {Colors.END}").lower()
            if save == 'y':
                tracker.save_report()
    
    if args.email:
        tracker.check_email(args.email)
    
    if args.phone:
        tracker.check_phone(args.phone)
    
    if args.google:
        tracker.google_dorks(args.google)
    
    print(f"\n{Colors.GREEN}[*] Done. Use ethically.{Colors.END}\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.RED}[!] Interrupted{Colors.END}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Colors.RED}[!] Error: {str(e)}{Colors.END}")
        sys.exit(1)
