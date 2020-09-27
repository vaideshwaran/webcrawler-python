import urllib
import urllib.request
from bs4 import BeautifulSoup
import os
from string import ascii_lowercase
import re
import requests

i=1
def fetch(url):
    thepage= urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata

soup = fetch("https://pixels.com/")
for img in soup.findAll('img', attrs={'src': re.compile("^https://")}):
    temp=img.get('src')
    if temp[:1]=="/":
        image = "https://pixels.com/" + temp
    else:
        image = temp

    print(image)

    nametemp = img.get('alt')
    if len(nametemp)==0:
        filename=str(i)
        i=i+1
    else:
        filename=nametemp


    imagefile = open(filename + ".jpeg", 'wb')
    imagefile.write(urllib.request.urlopen(image).read())
    imagefile.close()
