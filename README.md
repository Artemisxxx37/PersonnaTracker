# PersonaTracker - OSINT Digital Footprint Analyzer

PersonaTracker is a Python-based tool designed for gathering information about social media accounts and checking for email breaches. It utilizes various APIs to provide insights into a user's digital footprint.

## Features

- **Search Social Media**: Look up usernames on Twitter and Reddit.
- **Email Breach Check**: Check if an email has been involved in any data breaches using the Have I Been Pwned API.
- **Google Search**: Perform a Google search to find digital footprints.
- **Instagram Profile Scraping**: Scrape Instagram profiles for public information (note: scraping may violate Instagram's terms of service).
- **Results Output**: Save results to a JSON file or print them to the console.

## Requirements

- Python 3.x
- Required Python packages:
  - `requests`
  - `json`
  - `argparse`
  - `beautifulsoup4`
  - `tweepy`
  - `praw`

You can install the required packages using pip:

```bash
pip install requests beautifulsoup4 tweepy praw

Setup

    Clone the Repository:
		git clone https://github.com/yourusername/PersonaTracker.git
		cd PersonaTracker
Set Up Environment Variables: Create a .env file in the root directory of the project or set the environment variables in your system. The following variables are required:
TWITTER_API_KEY=your_twitter_api_key
TWITTER_API_SECRET=your_twitter_api_secret
TWITTER_ACCESS_TOKEN=your_twitter_access_token
TWITTER_ACCESS_TOKEN_SECRET=your_twitter_access_token_secret
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
HIBP_API_KEY=your_haveibeenpwned_api_key
GOOGLE_API_KEY=your_google_api_key
SEARCH_ENGINE_ID=your_google_search_engine_id


Obtain API Keys:

    Twitter: Create a Twitter Developer account and generate API keys.
    Reddit: Create a Reddit app to get your client ID and secret.
    Have I Been Pwned: Sign up for an API key.
    Google Custom Search: Set up a Google Cloud project and enable the Custom Search API.

Usage

Run the script from the command line with the following options:
python persona_tracker.py -u <username> -e <email> -g <query> -o <output_file>
Options:

    -u, --username: Search social media by username.
    -e, --email: Check email in public databases for breaches.
    -g, --google: Perform a Google search for digital footprints.
    -o, --output: Specify the output file name to save results in JSON format.

Example:
python persona_tracker.py -u example_username -e example@example.com -g "example query" -o results.json
