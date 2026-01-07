# 🔍 PersonnaTracker v3.0

<div align="center">

![Version](https://img.shields.io/badge/version-3.0-cyan?style=for-the-badge)
![Python](https://img.shields.io/badge/python-3.8+-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/status-active-success?style=for-the-badge)

**Advanced OSINT Tool for Digital Intelligence Gathering**

*Username Tracking • Phone Intelligence • Email Analysis • Social Media Discovery*

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Examples](#-examples) • [Demo](#-demo)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Installation](#-installation)
- [Usage](#-usage)
- [Examples](#-examples)
- [Modules](#-modules)
- [Demo Videos](#-demo-videos)
- [Legal Disclaimer](#-legal-disclaimer)
- [Contributing](#-contributing)
- [Author](#-author)

---

## 🎯 Overview

**PersonnaTracker** is a comprehensive OSINT (Open Source Intelligence) tool designed for security researchers, penetration testers, and digital investigators. It combines multiple intelligence gathering techniques into a single, powerful Python script.

### What Makes PersonnaTracker Unique?

✨ **No API Keys Required** - Pure web scraping and OSINT techniques  
🚀 **Multi-threaded Scanning** - Fast concurrent checks across 40+ platforms  
📱 **Complete Phone Intelligence** - WhatsApp, Telegram, carrier identification  
🌍 **International Support** - Special focus on West African telecom operators  
💾 **Detailed Reporting** - JSON and TXT export with full metadata  
🎨 **Beautiful CLI** - Colored output with progress indicators  

---

## ✨ Features

### 🔍 Username Intelligence
- ✅ Scan **40+ social media platforms** simultaneously
- ✅ Multi-threaded execution (30 concurrent workers)
- ✅ Smart detection with error message matching
- ✅ Platforms include: GitHub, Twitter, Instagram, LinkedIn, Reddit, TikTok, and more
- ✅ Real-time progress with colored output

### 📱 Phone Number Intelligence
- ✅ **Country identification** from 15+ countries
- ✅ **Carrier/Operator detection** (special focus on Burkina Faso, Côte d'Ivoire, Mali, Senegal)
- ✅ **WhatsApp verification** with profile name extraction
- ✅ **Telegram detection** with desktop app integration
- ✅ **Auto-open feature** - launch WhatsApp/Telegram directly
- ✅ Number format variations generation
- ✅ Social media search links (Facebook, LinkedIn, Instagram)
- ✅ Google Dorks generation for deep searches

### 📧 Email Analysis
- ✅ Email format validation
- ✅ Domain extraction and analysis
- ✅ Username variations generation
- ✅ Potential social media username discovery

### 🔎 Google Dorks Generator
- ✅ Advanced search queries for any target
- ✅ Platform-specific dorks (LinkedIn, GitHub, Facebook)
- ✅ Document search (PDF, DOC)
- ✅ Pastebin and breach detection queries

### 📊 Reporting
- ✅ **JSON format** - Machine-readable with full metadata
- ✅ **TXT format** - Human-readable summary report
- ✅ Timestamp tracking
- ✅ Success rate statistics

---

## 🚀 Installation

### Prerequisites
```bash
Python 3.8 or higher
pip (Python package manager)
```

### Quick Install

```bash
# Clone the repository
git clone https://github.com/Artemisxxx37/PersonnaTracker.git
cd PersonnaTracker

# Install dependencies
pip install -r requirements.txt

# Make executable
chmod +x personna.py

# Run
python3 personna.py -h
```

### Dependencies

Create a `requirements.txt` file:
```txt
requests>=2.31.0
beautifulsoup4>=4.12.0
lxml>=4.9.0
```

Install with:
```bash
pip install -r requirements.txt
```

---

## 💻 Usage

### Command Line Interface

```bash
python3 personna.py [OPTIONS]
```

### Options

| Flag | Long Form | Description |
|------|-----------|-------------|
| `-u` | `--username` | Username to search across platforms |
| `-p` | `--phone` | Phone number intelligence (WhatsApp, Telegram, carrier) |
| `-e` | `--email` | Email address analysis |
| `-g` | `--google` | Generate Google dorks for target |
| `-o` | `--output` | Save report to specified JSON file |
| `-t` | `--timeout` | Request timeout in seconds (default: 10) |
| `-v` | `--verbose` | Enable verbose output |
| `--open` | | Auto-open WhatsApp/Telegram in browser |
| `-h` | `--help` | Show help message |

---

## 📚 Examples

### 1. Username Search
Search for a username across all supported platforms:

```bash
python3 personna.py -u foxy
```

**Output:**
```
[*] Target: foxy
[*] Scanning 40 platforms...

[+] GitHub               https://github.com/foxy
[+] Twitter              https://twitter.com/foxy
[+] Instagram            https://www.instagram.com/foxy/
[+] Reddit               https://www.reddit.com/user/foxy

[*] Complete | Found: 4/40 | Time: 12.34s
```

### 2. Phone Intelligence
Analyze a phone number with WhatsApp/Telegram detection:

```bash
python3 personna.py -p +22670123456
```

**Output:**
```
📱 COMPLETE PHONE INTELLIGENCE REPORT
============================================================

🎯 Target Number: +226 70 12 34 56

🌍 LOCATION INTELLIGENCE
  ├─ Country: 🇧🇫 Burkina Faso (BF)
  ├─ Country Code: +226
  └─ Capital: Ouagadougou

📡 CARRIER INFORMATION
  └─ Operator: Telecel Faso

💬 MESSAGING APPS STATUS
  ✅ WhatsApp: REGISTERED
  ├─ Name: John Doe
  └─ Link: https://wa.me/22670123456

  ✅ Telegram: FOUND
  ├─ Name: @johndoe
  └─ Web: https://t.me/22670123456
```

### 3. Auto-Open WhatsApp/Telegram
Launch messaging apps directly:

```bash
python3 personna.py -p +22670123456 --open
```

### 4. Email Analysis
Analyze email and generate username variations:

```bash
python3 personna.py -e john.doe@example.com
```

**Output:**
```
[*] Email Analysis: john.doe@example.com

[+] Valid format
[*] Username: john.doe
[*] Domain: example.com

[*] Username variations:
  - john.doe
  - johndoe
  - john
  - doe
```

### 5. Google Dorks Generation
Create advanced search queries:

```bash
python3 personna.py -g "John Doe"
```

**Output:**
```
[*] Google Dorks: John Doe

  "John Doe"
  "John Doe" site:linkedin.com
  "John Doe" site:github.com
  "John Doe" site:twitter.com
  "John Doe" intext:"email" OR intext:"contact"
  "John Doe" site:pastebin.com
```

### 6. Save Report
Export results to JSON and TXT:

```bash
python3 personna.py -u foxy -o report.json
```

Creates:
- `report.json` - Machine-readable format
- `report.txt` - Human-readable summary

### 7. Verbose Mode
See detailed progress and errors:

```bash
python3 personna.py -u foxy -v
```

### 8. Combined Intelligence
Use multiple modules together:

```bash
python3 personna.py -u foxy -e foxy@example.com -p +22670123456 -o full_report.json
```

---

## 🔧 Modules

### Module 1: Username Tracker
**Purpose:** Search username across 40+ platforms

**Supported Platforms:**
- **Social Media:** Instagram, Twitter, Facebook, TikTok, LinkedIn, Reddit
- **Developer:** GitHub, GitLab, Stack Overflow, Dev.to, CodePen, Replit
- **Creative:** Behance, Dribbble, 500px, Flickr, Vimeo, SoundCloud
- **Professional:** HackerOne, HackerRank, Kaggle, AngelList, ProductHunt
- **Gaming:** Twitch, Steam, Discord
- **Music:** Spotify, Last.fm, SoundCloud
- **Other:** Medium, Tumblr, Pinterest, Patreon, Keybase, Mastodon

**Technology:**
- Multi-threaded with `ThreadPoolExecutor`
- 30 concurrent workers for speed
- Smart error detection with platform-specific messages
- HTTP status code validation

### Module 2: Phone Intelligence
**Purpose:** Complete phone number OSINT

**Capabilities:**
- **15+ Country Detection:** 🇧🇫 🇨🇮 🇲🇱 🇸🇳 🇳🇪 🇹🇬 🇧🇯 🇬🇳 🇫🇷 🇺🇸 and more
- **Carrier Identification:** 50+ operators mapped
- **WhatsApp Verification:** Profile name, status, picture
- **Telegram Detection:** Username and registration status
- **Number Variations:** Multiple format generations
- **Social Search:** Direct links to search on Facebook, LinkedIn, Instagram
- **Google Dorks:** Automated dork generation

**Special Focus - West Africa:**
- Burkina Faso (Orange BF, Moov Africa, Telecel Faso)
- Côte d'Ivoire (MTN, Orange, Moov)
- Mali (Orange Mali, Malitel)
- Senegal (Orange SN, Free SN)

### Module 3: Email Analyzer
**Purpose:** Extract intelligence from email addresses

**Features:**
- RFC-compliant validation
- Domain extraction
- Username parsing
- Variation generation for username searches
- Suggested social media profiles

### Module 4: Google Dorks Generator
**Purpose:** Create advanced search queries

**Dork Types:**
- Platform-specific searches
- Document searches (PDF, DOC)
- Contact information discovery
- Breach detection (Pastebin)
- Profile searches



## 📊 Report Format

### JSON Report Structure

```json
{
  "username": "foxy",
  "email": "foxy@example.com",
  "phone": "+22670123456",
  "timestamp": "2025-01-07T14:30:00",
  "found_accounts": [
    {
      "platform": "GitHub",
      "url": "https://github.com/foxy",
      "status": "FOUND",
      "status_code": 200
    }
  ],
  "total_found": 4,
  "platforms_checked": 40,
  "phone_intel": {
    "country": "Burkina Faso",
    "operator": "Telecel Faso",
    "whatsapp": {
      "exists": true,
      "name": "John Doe",
      "registered": true
    }
  }
}
```



## 🔒 Privacy & Ethics

### Responsible Use Guidelines

⚠️ **Important:** This tool is designed for legitimate security research and OSINT purposes only.

**Legal Uses:**
- ✅ Security research and penetration testing (with permission)
- ✅ Digital forensics investigations
- ✅ OSINT training and education
- ✅ Personal privacy auditing
- ✅ Threat intelligence gathering

**Prohibited Uses:**
- ❌ Stalking or harassment
- ❌ Unauthorized surveillance
- ❌ Identity theft
- ❌ Doxxing
- ❌ Any illegal activity

### Data Privacy
- PersonnaTracker only queries **publicly available information**
- No data is stored on external servers
- All reports are saved locally
- No API keys or authentication required
- No tracking or analytics

---

## ⚖️ Legal Disclaimer

```
DISCLAIMER: This tool is provided for educational and research purposes only.

The author (Artemis37) is not responsible for any misuse or damage caused 
by this tool. Users are responsible for complying with all applicable laws 
and regulations in their jurisdiction.

By using PersonnaTracker, you agree to:
1. Use the tool only for legitimate security research
2. Respect privacy and applicable laws
3. Obtain proper authorization before testing
4. Not use the tool for any malicious purposes

This tool queries publicly available information only. Users must ensure 
their use complies with:
- Computer Fraud and Abuse Act (CFAA)
- General Data Protection Regulation (GDPR)
- Local privacy and cybersecurity laws
```

---

## 🛠️ Technical Details

### Architecture

```
PersonnaTracker/
├── Core Engine
│   ├── Multi-threaded Scanner
│   ├── HTTP Session Manager
│   └── Error Handler
├── Modules
│   ├── Username Tracker (40+ platforms)
│   ├── Phone Intelligence (WhatsApp/Telegram)
│   ├── Email Analyzer
│   └── Google Dorks Generator
└── Output
    ├── JSON Reporter
    ├── TXT Reporter
    └── Console Formatter
```

### Performance

- **Concurrency:** 30 simultaneous platform checks
- **Timeout:** Configurable (default: 10s per request)
- **Average Speed:** 40 platforms in ~15-20 seconds
- **Memory:** Low footprint (~50MB)
- **CPU:** Multi-core optimized with ThreadPoolExecutor

### Dependencies

```python
requests>=2.31.0      # HTTP library
beautifulsoup4>=4.12.0  # HTML parsing
lxml>=4.9.0           # XML/HTML processing
```

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### Ways to Contribute

1. **Add New Platforms**
   - Edit the `platforms` dictionary
   - Add platform URL and error message
   - Test thoroughly

2. **Improve Phone Intelligence**
   - Add new country codes
   - Map additional carriers
   - Enhance detection algorithms

3. **Bug Fixes**
   - Report issues on GitHub
   - Submit pull requests
   - Improve error handling

4. **Documentation**
   - Improve README
   - Add usage examples
   - Create tutorials

### Contribution Guidelines

```bash
# Fork the repository
git clone https://github.com/Artemisxxx37/PersonnaTracker.git

# Create feature branch
git checkout -b feature/amazing-feature

# Make changes and commit
git commit -m "Add amazing feature"

# Push to branch
git push origin feature/amazing-feature

# Open Pull Request on GitHub
```

---


## 👨‍💻 Author

**Artemis37**

🔗 **Connect with me:**
- GitHub: [@Artemisxxx37](https://github.com/Artemisxxx37)
- LinkedIn: [artemis37](https://www.linkedin.com/in/artemis37)
- Twitter: [@tapsoba_jacob](https://x.com/tapsoba_jacob)
- HackTheBox: [Profile](https://app.hackthebox.com/profile/1442922)
- TryHackMe: [artemis6x](https://tryhackme.com/p/artemis6x)

---

## 📄 License

```
MIT License

Copyright (c) 2025 Artemis37

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

---

## ⭐ Star History

If you find this tool useful, please consider giving it a star! ⭐

```bash
# Star this repository
https://github.com/Artemisxxx37/PersonnaTracker
```

---

## 🙏 Acknowledgments

- **Artemis Community** 🛡️ - For continuous support and testing
- **OSINT Community** - For inspiration and techniques
- **Contributors** - Everyone who helped improve this tool

---

<div align="center">

**Made with ❤️ by Artemis37**

*Use responsibly. Stay ethical. Keep learning.*

[⬆ Back to Top](#-personnatracker-v30)

</div>
