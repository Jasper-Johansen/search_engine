#Importing the library functionalities
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

# Function to fetch the HTML content of a page
def fetch_page(url):
   try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.text
   except requests.exceptions.HTTPError as http_err:
       print(f"HTTP error occurred: {http_err}")
   except Exception as e:
    print(f"Other error occurred: {e}")

# Function to extract all links from a webpage
def extract_links(html_content, base_url):
    soup = BeautifulSoup(html_content, 'html.parser')
    links = set()  # Using a set to avoid duplicate URLs
    for anchor in soup.find_all('a', href=True):
        full_url = urljoin(base_url, anchor['href'])
        links.add(full_url)
    return links

# Function to tokenize the text content of a webpage
def tokenize(text):
    tokens = word_tokenize(text)  # Using nltk to tokenize words
    return tokens

# Function to normalize tokens: lowercasing, removing stopwords, stemming/lemmatization
def normalize(tokens, use_stemming=False):
    tokens = [token.lower() for token in tokens]  # Convert all tokens to lowercase

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]

    # Apply stemming or lemmatization
    if use_stemming:
        stemmer = PorterStemmer()
        tokens = [stemmer.stem(token) for token in tokens]
    else:
        lemmatizer = WordNetLemmatizer()
        tokens = [lemmatizer.lemmatize(token) for token in tokens]
    
    return tokens

# Function to check if crawling a URL is allowed by robots.txt
robots_cache = {}

def can_crawl(url, user_agent="*"):
    base_url = url.split("/")[0] + "//" + url.split("/")[2]
    if base_url in robots_cache:
        rp = robots_cache[base_url]
    else:
        rp = urllib.robotparser.RobotFileParser()
        robots_txt_url = base_url + "/robots.txt"
        rp.set_url(robots_txt_url)
        rp.read()
        robots_cache[base_url] = rp
    return rp.can_fetch(user_agent, url)

# Inverted index structure
inverted_index = defaultdict(lambda: defaultdict(int))


# Function to build the inverted index
def add_to_index(url, tokens):
    for token in tokens:
        inverted_index[token][url] += 1

# Main crawler function
def crawl(seed_url, max_pages=10):
    to_crawl = [seed_url]  # List of pages to visit
    crawled = set()  # Set of pages already visited

    while to_crawl and len(crawled) < max_pages:
        url = to_crawl.pop(0)  # Get the next page to crawl
        if url in crawled:
            continue  # Skip if already crawled

        # Check if the URL is allowed to be crawled by robots.txt
        if not can_crawl(url):
            print(f"Blocked by robots.txt: {url}")
            continue

        print(f"Crawling: {url}")
        html_content = fetch_page(url)

        if html_content:
            # Extract the text content from the page
            soup = BeautifulSoup(html_content, 'html.parser')
            page_text = soup.get_text()

            # Tokenize and normalize the text content
            tokens = tokenize(page_text)
            normalized_tokens = normalize(tokens, use_stemming=True)  # You can set use_stemming=False for lemmatization

            # Add tokens to the inverted index
            add_to_index(url, tokens)

            print(f"Normalized Tokens: {normalized_tokens[:25]}")  # Print first 10 tokens for brevity

            # Extract and add new links to the to_crawl list
            links = extract_links(html_content, url)
            to_crawl.extend(links - crawled)  # Add new links to crawl
            crawled.add(url)

        time.sleep(0.4)  # Add a delay to avoid overwhelming servers

    print(f"Crawled {len(crawled)} pages")

# Start crawling from a seed URL
seed_url = "https://jasper-johansen.github.io/julia_documentation/"
crawl(seed_url)

# Display the inverted index
if inverted_index:
    print("Inverted Index Results:")
    for term, urls in inverted_index.items():
        print(f"Term: {term}")
        for url, freq in urls.items():
            print(f"  URL: {url}, Frequency: {freq}")
else:
    print("No data in the inverted index.")

def tokenize_and_normalize(text):
    # Step 1: Convert text to lowercase
    text = text.lower()
    
    # Step 2: Tokenize the text using nltk's word_tokenize
    tokens = word_tokenize(text)
    
    # Step 3: Remove punctuation from tokens
    tokens = [word for word in tokens if word.isalnum()]
    
    # Step 4: Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    
    return tokens

def process_query(query, inverted_index):
    # Step 1: Tokenize and normalize the query
    query_tokens = tokenize_and_normalize(query)
    
    # Step 2: Collect results from the inverted index
    results = {}
    
    for token in query_tokens:
        if token in inverted_index:
            for url, freq in inverted_index[token].items():  # Use .items() to get both URL and frequency
                if url in results:
                    results[url] += freq
                else:
                    results[url] = freq

    return sorted(results.items(), key=lambda x: x[1], reverse=True)

# Example usage:
query = "Julia language"
results = process_query(query, inverted_index)
for url, score in results[:5]:  # Get top 5 results
    print(f"URL: {url}, Score: {score}")


if __name__ == '__main__':
    crawl()  # Only runs if crawler.py is executed directly