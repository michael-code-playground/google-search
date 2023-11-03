from googlesearch import search
from email_scraper import *
for result in search("facial hair products", advanced=True, num_results=5):
    
    if "amazon" in result.url:
        continue
    emails = scrape_mail(result.url)
    
    
    print(f'Title: {result.title}, Link: {result.url}')
    print()
    print(f'Scraped mails: {emails}')
