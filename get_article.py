from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import json
import time
import pandas as pd

def prepare_browser(playwright):
    context = playwright.chromium.launch_persistent_context(
        user_data_dir="",
        accept_downloads=True,
        headless=False,
        bypass_csp=True,
        slow_mo=100,
        channel="chromium",
        args=['--disable-blink-features=AutomationControlled']
    )

    # load Cookies
    with open('./dta/cookies.json', 'r') as f:
        cookies = json.loads(f.read().replace("'", '"'))
    context.add_cookies(cookies)
    
    return context

def save_cookie(context):
    cookies = context.cookies()
    with open("cookies.json", "w") as f:
        json.dump(cookies, f)
    context.close()
    
def get_article(context, url):
    text = ''
    page = context.pages[0]
    page.goto(url, timeout = 0)
    soup = BeautifulSoup(page.content())
    article = soup.find('div', class_='body-content')
    if article:
        text = article.text
        
    return text
    
    
# read csv
df = pd.read_csv('./dta/market_news.csv') 
    
with sync_playwright() as playwright:
    context = prepare_browser(playwright)
    
    # write article
    with open('./dta/market_news_articles.json', 'w') as file:
        count = 0
        
        for index, row in df.iterrows():
            count = count + 1
        
            # renew browser
            if index % 50 == 0:
                print('============renewing browser============')
                save_cookie(context)
                context = prepare_browser(playwright)
                
            # get article
            try:
                article = get_article(context, 'https://www.bloomberg.com' + row['url'])
            except:
                time.sleep(30)
                context = prepare_browser(playwright)
                article = '####ERROR####'
                
            json.dump([row['header'], article], file)
            file.write('\n')
            print(f"{count}: {article[:50]}...")
            
    context.close()
