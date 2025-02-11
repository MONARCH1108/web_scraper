# 🧠 Philosophy Web Scraper 🌐

Welcome to the **Philosophy Web Scraper** project! This repository contains Python scripts and resources for efficiently scraping data about various philosophers and their philosophies from Wikipedia.

## 📂 Project Structure

- **source.py**: for page source extraction
- **Extraction.ipynb & site_extraction.ipynb**: for extraction of text from page source.
- **site_scraper/**: A Scrapy project folder for organized web scraping.

## 📜 Extraction Methods

1. **Beautiful Soup**: 
   - Parsed HTML files to extract relevant paragraph information.
   - Utilized the `requests` module for direct scraping from the Wikipedia website.

2. **Scrapy**:
   - Employed for structured scraping of additional philosopher data, including images and captions.
   - To run the Scrapy crawler, navigate to the **site_scraper** folder, then proceed to the **spiders** directory.
   - Execute the desired crawler with the following command:
     ```bash
     scrapy crawl <crawler_name> -o output.json
     ```
   - Note: The name of the crawler can be found in the corresponding file. You can output the data in various formats such as JSON, CSV, etc.

## 🚀 Getting Started

### Prerequisites

Make sure you have the following Python packages installed in your system:

- `beautifulsoup4`
- `requests`
- `lxml`
- `scrapy`

You can install these packages using pip:

```bash
pip install beautifulsoup4 requests lxml scrapy
