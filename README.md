# Web Crawler Project

This repository contains the implementation of a web crawler, which is the first step towards building a basic search engine. The crawler fetches pages from the web and follows links to discover and index more content. This project is divided into six key steps, and each step will be added progressively to this repository.

## Project Overview

### Goal:
To develop a fully functional web crawler as part of a larger search engine project. The crawler will start with a set of seed URLs, fetch data from websites, and continue exploring by following hyperlinks. The data will be processed, indexed, and made searchable in future steps.

### Features:
1. Crawl web pages starting from a seed URL.
2. Extract data and follow hyperlinks for continued exploration.
3. Keep track of visited pages to avoid re-crawling.
4. Implement basic data cleaning and storage.
5. Progressively build a search index (to be implemented in future steps).

## Project Structure

### Current Status:
- **Step 1: Web Crawler** (In progress)

    The crawler is built using Python. The main file is `crawler.ipynb`, which contains the initial implementation of the web crawling mechanism.

### Upcoming:
- **Step 2: Parsing and Indexing**
- **Step 3: Search Query Processing**
- **Step 4: Ranking Algorithms**
- **Step 5: UI for Search Engine**
- **Step 6: Optimizations**

## Installation

To get started with this project, you can clone this repository and run the crawler locally.

### Requirements:
- Python 3.x
- Jupyter Notebook
- Libraries: `requests`, `beautifulsoup4`

### Steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/USERNAME/REPO.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Web-Crawler-Project
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Open the Jupyter Notebook:
    ```bash
    jupyter notebook crawler.ipynb
    ```

## Usage

To run the crawler, open `crawler.ipynb` and run the cells. You can modify the seed URL and adjust the crawler settings to fit your needs.

## Contributing

Feel free to contribute by adding new features or improving existing code. Fork the repository, make your changes, and submit a pull request!
