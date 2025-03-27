import requests
import json
import argparse
from bs4 import BeautifulSoup
import os
import tweepy  # For Twitter API
import praw    # For Reddit API

class PersonaTracker:
    def __init__(self):
        self.results = {}
        # Initialize API keys (replace with your own)
        self.twitter_auth = tweepy.OAuthHandler('API_KEY', 'API_SECRET')
        self.reddit = praw.Reddit(client_id='CLIENT_ID',
                                  client_secret='CLIENT_SECRET',
                                  user_agent='PersonaTracker/1.0')

    def search_social_media(self, username):
        """Search for username across multiple platforms"""
        self._search_twitter(username)
        self._search_reddit(username)
        self._search_instagram(username)
        return self.results

    def _search_twitter(self, username):
        """Search Twitter profiles"""
        try:
            api = tweepy.API(self.twitter_auth)
            user = api.get_user(screen_name=username)
            self.results['twitter'] = {
                'name': user.name,
                'followers': user.followers_count,
                'tweets': user.statuses_count,
                'verified': user.verified
            }
        except tweepy.TweepError:
            self.results['twitter'] = "No account found"

    def _search_reddit(self, username):
        """Search Reddit profiles"""
        try:
            user = self.reddit.redditor(username)
            self.results['reddit'] = {
                'karma': user.link_karma + user.comment_karma,
                'account_age': user.created_utc,
                'trophies': [trophy.name for trophy in user.trophies()]
            }
        except Exception:
            self.results['reddit'] = "No account found"

    def _search_instagram(self, username):
        """Web scrape Instagram (note: Instagram API restrictions apply)"""
        try:
            url = f"https://www.instagram.com/{username}/"
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            meta = soup.find("meta", property="og:description")
            if meta:
                self.results['instagram'] = meta['content'].strip()
            else:
                self.results['instagram'] = "No account found"
        except Exception as e:
            self.results['instagram'] = str(e)

    def search_public_db(self, email):
        """Check public databases for email breaches"""
        url = "https://haveibeenpwned.com/api/v3/breachedaccount/" + email
        headers = {'hibp-api-key': 'YOUR_API_KEY'}
        try:
            response = requests.get(url, headers=headers)
            self.results['breaches'] = json.loads(response.text)
        except Exception as e:
            self.results['breaches'] = str(e)

    def google_search(self, query):
        """Search Google for digital footprints"""
        url = "https://customsearch.googleapis.com/customsearch/v1"
        params = {
            'q': query,
            'key': 'GOOGLE_API_KEY',
            'cx': 'SEARCH_ENGINE_ID'
        }
        try:
            response = requests.get(url, params=params)
            self.results['google'] = json.loads(response.text)
        except Exception as e:
            self.results['google'] = str(e)

    def save_results(self, filename):
        """Save results to JSON file"""
        with open(filename, 'w') as f:
            json.dump(self.results, f, indent=2)

def main():
    parser = argparse.ArgumentParser(description="PersonaTracker - OSINT Digital Footprint Analyzer")
    parser.add_argument('-u', '--username', help="Search social media by username")
    parser.add_argument('-e', '--email', help="Check email in public databases")
    parser.add_argument('-g', '--google', help="Perform Google search")
    parser.add_argument('-o', '--output', help="Output file name")

    args = parser.parse_args()
    pt = PersonaTracker()

    if args.username:
        pt.search_social_media(args.username)
    if args.email:
        pt.search_public_db(args.email)
    if args.google:
        pt.google_search(args.google)
    if args.output:
        pt.save_results(args.output)
    else:
        print(json.dumps(pt.results, indent=2))

if __name__ == "__main__":
    main()
