import urllib
from bs4 import BeautifulSoup
import urlparse

url = "http://www.mileycyrus.com/" #Enter Your Address here
urls = [url]
visited = [url]

while len(urls)>0:
    try:
        html=urllib.urlopen(urls[0]).read()
    except:
        print "error"
    urls.pop(0)
    print len(urls)
    soup=BeautifulSoup(html)
    for tag in soup.findAll('a',href=True):
        tag['href']=urlparse.urljoin(url,tag['href'])
        if url in tag['href'] and tag['href'] not in visited:
            urls.append(tag['href'])
            visited.append(tag['href'])
print visited
