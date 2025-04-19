import nltk
from src.news_fetcher import fetch_news
from src.preprocess_data import preprocess_data
from src.sentiment_analysis import analyze_sentiment
from pymongo import MongoClient

# Download necessary NLTK data files
nltk.download('punkt')
nltk.download('stopwords')

def main():
    # Fetch news articles from NewsAPI
    articles = fetch_news()
    if not articles:
        print("No articles found.")
        return

    # Preprocess articles
    preprocessed_data = preprocess_data(articles)

    # Analyze sentiment and insert into DB
    client = MongoClient('mongodb://localhost:27017/')
    db = client['news_database']
    collection = db['news_articles']

    for article in preprocessed_data:
        sentiment = analyze_sentiment(article)
        article['sentiment'] = sentiment

        # ✅ Print title, content, and sentiment to terminal
        print(f"Title: {article['title']}")
        print(f"Published At: {article['publishedAt']}")
        print(f"Content: {article['content']}")
        print(f"Sentiment: {article['sentiment']}")
        print("-" * 80)

        # ✅ Prepare and insert only required fields to MongoDB (excluding title and content)
        data_to_insert = {
            'keywords': article['keywords'],
            'author': article['author'],
            'publishedAt': article['publishedAt'],
            'sentiment': sentiment
        }
        collection.insert_one(data_to_insert)

    print("Data has been inserted into MongoDB.")

if __name__ == "__main__":
    main()
