import urllib
from urllib.request import urlopen as uReq  # Web client
from bs4 import BeautifulSoup as soup # to parse HTML
import re
import requests

    page_url = "https://pixels.com/"
    uClient = uReq(page_url)
    page_soup = soup(uClient.read(), "html.parser")
    uClient.close()
    
    for link in page_soup.findAll('a', attrs={'href': re.compile("^https://")}):
        href_links = link.get('href')
        print(href_links)

    for image in page_soup.findAll('img', attrs={'src': re.compile("^https://")}):
        images_list = image.get('src')
        print(images_list)
