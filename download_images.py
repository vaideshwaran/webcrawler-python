import urllib
import urllib.request
from bs4 import BeautifulSoup
import os
from string import ascii_lowercase
import re
import requests

i=1

#fetches the url & parse the html content using beautifulsoap
def fetch(url):
    thepage= urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata

soup = fetch("https://pixels.com/")

#fetches all the href links in the <a> tag & prints the same
for link in soup.findAll('a', attrs={'href': re.compile("^https://")}):
    href_links = link.get('href')
    print(href_links)
    
#fetches all the src content in the <img> tag of the page & prints the same    
for img in soup.findAll('img', attrs={'src': re.compile("^https://")}):
    temp=img.get('src')
    
    if temp[:1]=="/":
        image = "https://pixels.com/" + temp
    else:
        image = temp
        
    print(image)

#Naming the files which are to be donwloaded
    nametemp = img.get('alt')
    if len(nametemp)==0:
        filename=str(i)
        i=i+1
    else:
        filename=nametemp

 #Writing the files & downloading images
    imagefile = open(filename + ".jpeg", 'wb')
    imagefile.write(urllib.request.urlopen(image).read())
    imagefile.close()
