# Bloomberg News Scraper

## Description
This repository contains a Python-based web scraping tool designed to extract news articles from specified sections of the Bloomberg website. The tool uses the Playwright framework to navigate the site and scrape the latest news articles, organizing them from newest to oldest.

## Features
- Scrape news articles from specific Bloomberg sections.
- Automatically sort articles from newest to oldest.
- Extract article titles, URLs, and content.

## Installation
To set up the scraping tool, follow these steps:
1. Clone the repository: `git clone [repository URL]`
2. Install the required Python packages: `pip install -r requirements.txt`
3. Ensure Playwright is set up correctly: `playwright install`

## Usage
To start scraping articles, run the following command:

1. Scrape the titles and urls of a specified sections of Bloomberg news.
   ```
   python get_title_url.py
   ```
3. Scrape the contents of each articles.
   ```
   python get_cookies.py
   python get_articles.py
   ```

## Legal Notice
- **Important**: This tool is for educational purposes only. Users are responsible for complying with Bloomberg's Terms of Service and any applicable laws or regulations.
- Web scraping can have legal implications. Ensure you are not violating any copyright laws or terms of service agreements.
- It is advised to review Bloomberg's Terms of Service and seek legal advice if necessary before using this tool for scraping.
