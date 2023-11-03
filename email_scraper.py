from bs4 import BeautifulSoup
import requests
import requests.exceptions
import urllib.parse
from collections import deque
import re

def scrape_mail(user_url):
  
  #user_url = str(input('[+] Enter target URL to scan: '))
  urls = deque([user_url])

  scraped_urls = set()
  emails = set()

  count = 0
  try:
    while len(urls):
      count += 1
      if count == 200:
        break
      url = urls.popleft()
      scraped_urls.add(url)

      parts = urllib.parse.urlsplit(url)
      base_url = '{0.scheme}://{0.netloc}'.format(parts)
      initial_base_url = base_url
      
      path = url[:url.rfind('/')+1] if '/' in parts.path else url

      print('[%d] Processing %s' % (count, url))
      try:
        response = requests.get(url)
      except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
        continue

      new_emails = set(re.findall(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+', response.text, re.I))
      emails.update(new_emails)

      soup = BeautifulSoup(response.text, features="lxml")

      for anchor in soup.find_all("a"):
        link = anchor.attrs['href'] if 'href' in anchor.attrs else ''
        
        if link.startswith('/'):
          link = base_url + link
        elif not link.startswith('http'):
          link = path + link
        if not link in urls and not link in scraped_urls:
          
          if not initial_base_url in link or "product" in link:
            continue
          
          urls.append(link)
          
          
  except KeyboardInterrupt:
    print('[-] Closing!')

  #for mail in emails:
    #if "jpg" in mail:
      #continue
    #print(mail)
  return emails    
