import requests
import json
from datetime import datetime

API_KEY = 'YOUR_NEWS_API_KEY'
KEYWORDS = ['election', 'attack', 'war', 'crisis', 'emergency', 'policy']

def update_news():
    url = f"https://newsapi.org/v2/top-headlines?language=en&apiKey={API_KEY}"
    response = requests.get(url).json()
    
    daily = []
    weekly = []
    
    for article in response.get('articles', []):
        item = {'title': article['title'], 'url': article['url'], 'source': article['source']['name']}
        if any(k in article.get('title', '').lower() for k in KEYWORDS):
            weekly.append(item)
        else:
            daily.append(item)
            
    with open('news.json', 'w') as f:
        json.dump({'daily': daily, 'weekly': weekly}, f)

if __name__ == "__main__":
    update_news()
