from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Initialize the SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()


def analyze_sentiment(article):
    # Ensure you're passing the article as a dictionary
    content = article.get('content', '')  # Extract content, default to empty string if not found
    sentiment_score = sia.polarity_scores(content)

    # Return sentiment based on compound score
    if sentiment_score['compound'] >= 0.05:
        return 'positive'
    elif sentiment_score['compound'] <= -0.05:
        return 'negative'
    else:
        return 'neutral'
