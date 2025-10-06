import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()


def get_news_data():
    data = requests.get(os.environ["GDELT_URL"]).json()
    js = {}
    entries = []
    for entry in data['articles']:
        d = {'title': entry['title'], 'url': entry['url'], 'pubDate': entry['seendate'],
             'country': entry['sourcecountry']}
        entries.append(d)
    js['entries'] = entries
    with open('../../data/gdelt.json', 'w', encoding='utf-8') as file:
        json.dump(js, file)


if __name__ == "__main__":
    get_news_data()