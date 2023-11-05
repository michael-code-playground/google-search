from googlesearch import search
from email_scraper import *

#Skip large product pages to save time - extend
skip = ["amazon", "ebay"]
query = input("Enter what you're looking for: ")

for result in search(query, advanced=True, num_results=5):
    
    if any(skip_item in result.url for skip_item in skip):
        continue
    emails = scrape_mail(result.url)
    
    
    print(f'Title: {result.title}, Link: {result.url}')
    print()
    print(f'Scraped mails: {emails}')
