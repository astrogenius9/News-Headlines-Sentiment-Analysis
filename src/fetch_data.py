# src/fetch_data.py

import requests
from .mongo_operations import insert_article  # Add this import

def fetch_articles(api_key, query='technology'):
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={api_key}"
    response = requests.get(url)
    data = response.json()

    articles = data.get('articles', [])

    for article in articles:
        formatted_article = {
            "title": article.get("title"),
            "content": article.get("content"),
            "author": article.get("author"),
            "publishedAt": article.get("publishedAt"),
            "url": article.get("url"),
            "source": article.get("source", {}).get("name"),
            "sentiment": None  # We'll fill this after sentiment analysis
        }
        insert_article(formatted_article)

    print(f"✅ {len(articles)} articles inserted into MongoDB.")
    return articles
