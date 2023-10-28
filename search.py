from googlesearch import search

for result in search("on-call interpreting", advanced=True):
    print(f'Title: {result.title}, Link: {result.url}')
