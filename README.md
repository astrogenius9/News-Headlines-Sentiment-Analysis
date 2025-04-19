
# News Headlines Sentiment Analysis

This project is a modular Python pipeline designed to perform **sentiment analysis on U.S. technology news headlines** using NewsAPI and MongoDB. The goal is to automate the process of fetching, storing, preprocessing, and analyzing news sentiment in a structured and scalable way.



## Abstract

In today's fast-paced digital landscape, real-time analysis of public sentiment plays a crucial role in understanding market trends, public opinion, and media influence. This project introduces a modular, Python-based pipeline for performing sentiment analysis on U.S. technology news headlines using data retrieved from the NewsAPI. The system is designed to fetch the most recent headlines, preprocess the textual data to make it suitable for analysis, and classify each headline according to its underlying sentiment—positive, negative, or neutral. The project utilizes standard natural language processing (NLP) techniques for text cleaning and transformation, with the option to implement machine learning or lexicon-based models for classification. The modularity of the codebase allows easy scalability, and the insights generated can serve various use cases, including financial analysis, public relations strategy, and real-time news monitoring.

## Introduction

The growing volume of digital content, especially in the form of news articles, poses both an opportunity and a challenge: while there is a wealth of information available, extracting meaningful insights quickly and efficiently requires robust automated systems. In particular, understanding the sentiment expressed in news media has become increasingly important for businesses, investors, researchers, and policy-makers. Sentiment analysis, a branch of natural language processing (NLP), seeks to determine the emotional tone behind textual data, offering valuable insights into public opinion and social trends.

This project focuses specifically on sentiment analysis of U.S.-based technology news headlines. Headlines, although concise, often carry strong emotional cues and are widely consumed by the public. By targeting this niche, the project not only captures trends in technological discourse but also provides a framework that can be extended to other categories and regions. Using Python and a structured set of scripts, the system automatically fetches recent news, processes the content, and applies sentiment analysis, thereby offering a foundation for real-time sentiment monitoring and analysis.

## Methodology

This project employs a modular pipeline in Python to automate sentiment analysis of news headlines. The process begins with ```news_fetcher.py```, which retrieves the latest U.S. technology headlines from NewsAPI. These headlines are then managed by ```fetch_data.py```, which stores them in a MongoDB database for structured, persistent storage. Preprocessing is handled by ```preprocess_data.py```, where text is cleaned—punctuation removed, converted to lowercase, stopwords eliminated, and tokenized—to prepare for sentiment classification. The cleaned data is analyzed in ```sentiment_analysis.py```, where each headline is labeled as positive, negative, or neutral using either lexicon-based tools like VADER or machine learning models. Utility functions in ```utils.py``` support reusability and streamline the overall workflow. The integration of MongoDB allows for efficient data management and sets the stage for future enhancements such as trend analysis or real-time dashboards.


## API Reference


You can get your own API key from: https://newsapi.org

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required:** Your API key |



## Deployment

**Clone the Repository**
```bash
git clone https://github.com/astrogenius9/News-Headlines-Sentiment-Analysis
```
**Install Dependencies**

```bash 
pip install -r requirements.txt
```

**Set Up Your NewsAPI Key**

- Go to https://newsapi.org and generate you own API key 

- In ```config.json``` file input your API key in place of YOUR_API_KEY. 

- Even in the ```news_fetcher.py``` enter your API key. 

**Run the pipeline**

- Run the ```run_analysis.py``` file to see the final result of the project. 

**Accessing MongoDB**

- Ensure MongoDB is installed. It is used to store the keywords of news headlines 

- Open the command-line interface of your operating system(eg. Terminal for Mac) and enter the following command:

  ```bash
  mongosh
  ```

- After running MongoDB, use
  ```bash
  show databases
  ```
  to see the databases available. 

- To access the database for the project, use
  ```bash
  use [DATABASE_NAME]
  ```
  (eg: ```use news_database```). 

- To access the collections,  run the command:
   ```bash
  show collections
   ``` 

- After selecting the collection that is storing the keywords, we can use the query:
  ```db.[COLLECTION_NAME].find()``` to see the keywords being stored for each headline. Other data like ```_id```, ```author```, ```publishedAt```, and ```sentiment``` are shown. 







