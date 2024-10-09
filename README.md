# Custom Search Engine Project

## Overview
This project aims to build a custom search engine from scratch. The search engine follows a structured, step-by-step approach, covering essential components such as web crawling, tokenization, normalization, indexing, and ranking. The goal is to develop a fully functional search engine to retrieve information from crawled websites efficiently.

### Steps to Build the Search Engine:
1. **Web Crawling** (Completed)
2. **Tokenization and Normalization** (In Progress)
3. **Indexing** (Next Step)
4. **Ranking Algorithms**
5. **Query Processing**
6. **Search Engine Interface**

---

## Step 1: Web Crawling
The first step of building the search engine involves **web crawling**, where we programmatically fetch web pages using a seed URL and extract the links to visit other web pages. The crawler has been implemented in Python using libraries like `requests` and `BeautifulSoup`. 

### Key Features:
- Respect for `robots.txt`: Ensures the crawler does not violate the site's crawling policies.
- Token extraction from HTML: Extracts the textual content from the HTML for further processing.

---

## Step 2: Tokenization and Normalization (In Progress)
After crawling web pages, the next step is **tokenization** and **normalization**. This step processes the raw text into tokens (words) that can be used for indexing and searching.

### Tokenization:
- Splitting the text into individual words or tokens using regular expressions.

### Normalization:
- Converting tokens to lowercase.
- Removing stopwords (common words that do not add meaning, e.g., "the", "is").
- Optionally applying stemming or lemmatization to reduce words to their base or root forms.

## Installation

To get started with this project, you can clone this repository and run the crawler locally.

### Requirements:
- Python 3.x
- Jupyter Notebook
- Libraries: `requests`, `beautifulsoup4`, `nltk`
-- Install using: `pip install requests beautifulsoup4 nltk`

### Steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/USERNAME/REPO.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Web-Crawler-Project
    ```
3. Open the Jupyter Notebook:
    ```bash
    jupyter notebook crawler.ipynb
    ```

## Usage

To run the crawler, open `crawler.ipynb` and run the cells. You can modify the seed URL and adjust the crawler settings to fit your needs.

## Contributing

Feel free to contribute by adding new features or improving existing code. Fork the repository, make your changes, and submit a pull request!
