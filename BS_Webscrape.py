#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 9:03 2024
Creator: Johnny Sylvain
Based on Chaofan Chen's example BS
"""

from bs4 import BeautifulSoup
import requests
#import time
first_url = "https://francolibrary.com/items/show/3"
url = "https://scholar.google.com/scholar?as_ylo=2024&q=machine+learning&hl=en&as_sdt=0,20"
response = requests.get(first_url)
#print(response)

html = response.content
#print(html)

soup = BeautifulSoup(html, "lxml")
#print(soup)


all_articles = soup.find_all("div", class_="element-set")
for article in all_articles:
    #title = article.find("div", class_="dublin-core-title")
    title = article.select_one('div#dublin-core-title .element-text')
    if(title != None):
        print(title.text)
    description = article.select_one('div#dublin-core-description .element-text')
    if(description != None):
        print(description.text)
    #print(authors_venue_year.get_text(strip=False))

itemfiles = soup.select_one('div#itemfiles div.element-text a')
href = itemfiles.get('href', '')
print(href)

collection = soup.select_one('div#collection div.element-text p a')
print(collection.text)

# |||||||||||||||||| TAGS HERE do checks? |||||||||||||||||||||||||
tags = soup.select('div#item-tags div.element-text a')
for tag in tags:
    print(tag.text)

print()