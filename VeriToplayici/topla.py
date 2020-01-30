#-*- coding: utf-8 -*-
import requests
from requests.exceptions import HTTPError

import re

from bs4 import BeautifulSoup
from html.parser import HTMLParser

class GetTheData(HTMLParser):
    def handle_starttag(self,tag,attrs):
        pass#print("found a start tag:", tag)
    def handle_endtag(self,tag):
        pass#print("Found an end tag:",tag)
    def handle_data(self,data):
        print(data,end="\n\n")

parser = GetTheData()
"""
parser.feed('<title>JournalDev HTMLParser</title>'
            '<h1>Python html.parse module</h1>')
"""

urls = []
fl = open("links","r")
urls = fl.read().split()

data = []
documents = []
st = ""
for url in urls:
    try:
        print("Getting Data from:",url)
        response = requests.get(url)

        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
        continue
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
        continue
    else:
        print('Success!')
    soup = BeautifulSoup(response.text,features="html.parser")
    for script in soup("script"):
        script.extract()
    documents.append(soup)

for soup in documents:
    for content in soup.find_all("p"):
        st = st+"\n" + re.sub(' +', ' ',content.text.replace("\n"," "))
        data.append(content)

print(st)
