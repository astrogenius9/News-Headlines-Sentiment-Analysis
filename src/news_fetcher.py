import requests


def fetch_news():
    url = 'https://newsapi.org/v2/everything'
    params = {
        'q': 'technology',  # or any search query you prefer
        'apiKey': 'YOUR_API_KEY',  # Replace with your actual API key
        'pageSize': 20,  # Limit the results to 20 articles
        'sortBy': 'publishedAt',  # Sort by most recent
    }
    response = requests.get(url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        return response.json()['articles']
    else:
        print("Error fetching news:", response.status_code)
        return []
