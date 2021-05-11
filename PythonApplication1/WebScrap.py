import urllib.request, urllib.parse , urllib.parse
fhand=urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
counts=dict()
for line in fhand:
    words=line.decode().split()
    for word in words:
        counts[word]=counts.get(word,0)+1

print(counts)

print("-------------Seperate------------")


from bs4 import BeautifulSoup
url=input("Enter = ")
html=urllib.request.urlopen(url).read()
soup=BeautifulSoup(html,"html.parser")

tags=soup("a")
for tag in tags:
    print(tag.get("href",None))


print("-------------Seperate------------")

import ssl
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url=input("Enter = ")
html=urllib.request.urlopen(url,context=ctx).read()
soup=BeautifulSoup(html,"html.parser")


tags=soup("a")
for tag in tags:
    print(tag.get("href",None))

print("-------------Assigment------------")

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)
