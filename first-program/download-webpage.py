import urllib.request
import sys

urlToLoad = 'http://www.google.com'

crawledWebLinks = {}

while urlToLoad != '':
    urlToLoad = input('Please enter a URL to crawl: ')
    if urlToLoad == '':
        print('Exiting program')
        break
    shortName = input('Please enter a short name for the URL ' + urlToLoad + ': ')
    webFile = urllib.request.urlopen(urlToLoad).read()
    crawledWebLinks[shortName] = webFile
print(crawledWebLinks.keys())