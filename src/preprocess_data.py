import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re

nltk.download('punkt')
nltk.download('stopwords')


def preprocess_data(articles):
    stop_words = set(stopwords.words('english'))
    preprocessed_articles = []

    for article in articles:
        content = article.get('content', '')
        clean_content = re.sub(r'\W+', ' ', content)
        tokens = word_tokenize(clean_content.lower())
        filtered_tokens = [word for word in tokens if word not in stop_words]

        # Extract keywords (top 5 most frequent words)
        freq = {}
        for word in filtered_tokens:
            freq[word] = freq.get(word, 0) + 1
        keywords = sorted(freq, key=freq.get, reverse=True)[:5]

        preprocessed_articles.append({
            'keywords': keywords,
            'content': ' '.join(filtered_tokens),
            'author': article.get('author', 'Unknown'),
            'publishedAt': article.get('publishedAt', 'Unknown'),
            'title': article.get('title', 'Unknown')  # only for display, not saved in DB
        })

    return preprocessed_articles
