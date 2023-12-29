from playwright.sync_api import sync_playwright
import json

def run(playwright):
    
    browser = playwright.chromium.connect_over_cdp('http://localhost:12345/')
    context = browser.contexts[0]

    # get Cookies
    cookies = context.cookies()
    print(cookies)

    # save cookie
    with open("./dta/cookies.json", "w") as f:
        json.dump(cookies, f)

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
