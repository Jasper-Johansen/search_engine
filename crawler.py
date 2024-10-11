import re
import requests
from bs4 import BeautifulSoup
import time
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize
import urllib.robotparser
from urllib.parse import urljoin
from collections import defaultdict
import json

# Inverted index structure
inverted_index = defaultdict(lambda: defaultdict(int))

# Function to fetch the HTML content of a page
def fetch_page(url):
    try:
        response = requests.get(url, timeout=5)  # Reduced timeout
        response.raise_for_status()
        return response.text
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as e:
        print(f"Error occurred: {e}")

# Function to tokenize the text content of a webpage
def tokenize(text):
    tokens = word_tokenize(text)  # Using nltk to tokenize words
    return tokens

# Function to normalize tokens
def normalize(tokens, use_stemming=False):
    tokens = [token.lower() for token in tokens]  # Convert all tokens to lowercase
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token.isalnum() and token not in stop_words]  # Remove punctuation and stopwords

    if use_stemming:
        stemmer = PorterStemmer()
        tokens = [stemmer.stem(token) for token in tokens]
    else:
        lemmatizer = WordNetLemmatizer()
        tokens = [lemmatizer.lemmatize(token) for token in tokens]
    
    return tokens

# Function to build the inverted index
def add_to_index(url, tokens):
    for token in tokens:
        inverted_index[token][url] += 1

# Function to crawl and store results in JSON
def crawl(seed_url, max_pages=10):
    to_crawl = [seed_url]
    crawled = set()

    while to_crawl and len(crawled) < max_pages:
        url = to_crawl.pop(0)
        if url in crawled:
            continue

        print(f"Crawling: {url}")
        html_content = fetch_page(url)
        if html_content:
            soup = BeautifulSoup(html_content, 'html.parser')
            page_text = soup.get_text()
            tokens = tokenize(page_text)
            normalized_tokens = normalize(tokens, use_stemming=True)
            add_to_index(url, normalized_tokens)

            # Extract and add new links to to_crawl
            links = extract_links(html_content, url)
            to_crawl.extend(links - crawled)
            crawled.add(url)

        time.sleep(0.4)

    # Save the inverted index to a JSON file
    with open("inverted_index.json", "w") as f:
        json.dump(inverted_index, f)

    print(f"Crawled {len(crawled)} pages")

# Function to extract links
def extract_links(html_content, base_url):
    soup = BeautifulSoup(html_content, 'html.parser')
    links = set()
    for anchor in soup.find_all('a', href=True):
        full_url = urljoin(base_url, anchor['href'])
        links.add(full_url)
    return links

# Function to process search queries using the pre-stored inverted index
def process_query(query):
    query_tokens = tokenize_and_normalize(query)

    with open("inverted_index.json", "r") as f:
        inverted_index = json.load(f)

    results = {}
    for token in query_tokens:
        if token in inverted_index:
            for url, freq in inverted_index[token].items():
                results[url] = results.get(url, 0) + freq

    return sorted(results.items(), key=lambda x: x[1], reverse=True)

# Example usage:
crawl("https://jasper-johansen.github.io/julia_documentation/")
