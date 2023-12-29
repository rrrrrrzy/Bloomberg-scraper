from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import numpy as np
import time
import csv

def get_news(article):
    href = ''
    text = ''
    byline_text = ''
    a_tag = article.find("a")
    if a_tag:
        href = a_tag["href"]
        text = a_tag.text

    byline_div = article.find("div", {"data-component":"byline"})
    byline_text = byline_div.text if byline_div else ""
        
    return {'url':href, 'headline':text, 'author':byline_text}
    

def run(playwright):
    browser = playwright.chromium.launch_persistent_context(
        user_data_dir="chrome_cache",
        accept_downloads=True,
        headless=False,
        bypass_csp=True,
        slow_mo=100,
        channel="chrome",
        args=['--disable-blink-features=AutomationControlled']
    )
    
    page = browser.new_page()

    page.goto("https://www.bloomberg.com/markets")
    #page.goto("https://www.bloomberg.com/economics")
    #page.goto("https://www.bloomberg.com/technology")
    page.mouse.wheel(0, 100000)
    

    count = 0
    
    with open('./dta/tech_news.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        writer.writerow(['url', 'header', 'author'])
        
        loop = 1
        while 1:
            loop = loop + 1
            #print('extracting articles')
            # articles = page.query_selector_all("article")
            soup = BeautifulSoup(page.content())
            articles = soup.find_all('article')
            
            #print('extracting news')
            for article in articles[count:]:
                news_line = get_news(article)
                writer.writerow([news_line['url'], news_line['headline'], news_line['author']])
                print(news_line)
                
            count = len(articles)

            #print('clicking button')
            page.click('button[aria-label="more stories"]', timeout = 0)
            #print('waiting for button')
            page.wait_for_selector('button[aria-label="more stories"]', timeout = 0)
            #print('scrolling')
            page.mouse.wheel(0, 100000)
            # time.sleep(np.random.rand() * 10)
            print(loop)
            
            # if loop % 50 == 0:
            #     time.sleep(60)


with sync_playwright() as playwright:
    run(playwright)