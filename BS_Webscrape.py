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
    ######## DUBLIN CORE ##########
    #title = article.find("div", class_="dublin-core-title")
    title = article.select_one('div#dublin-core-title .element-text')
    if(title != None):
        print(title.text)
    description = article.select_one('div#dublin-core-description .element-text')
    if(description != None):
        print(description.text)
    creator = article.select_one('div#dublin-core-creator .element-text')
    if(creator != None):
        print(creator.text)
    date = article.select_one('div#dublin-core-date .element-text')
    if(date != None):
        print(date.text)
    language = article.select_one('div#dublin-core-language .element-text')
    if(language != None):
        print(language.text)
    ########### ENTRY TYPE (might not be filled?) #############
    type1 = article.select_one('div#dublin-core-type .element-text')
    if(type1 != None):
        print(type1.text)
    ###### Identifier usually is html for a link ######
    identifier = article.select_one('div#dublin-core-identifier .element-text a')
    if(identifier != None):
        print(identifier)
    coverage = article.select_one('div#dublin-core-coverage .element-text')
    if(coverage != None):
        print(coverage.text)

    ########### IGNORING CONTRIBUTION FORM ############
    ########### ZOTERO ###########
    zotero_num_pages = article.select_one('div#zotero-num-pages .element-text')
    if(zotero_num_pages != None):
        print(zotero_num_pages.text)
    zotero_place = article.select_one('div#zotero-place .element-text')
    if(zotero_place != None):
        print(zotero_place.text)
    zotero_publisher = article.select_one('div#zotero-publisher .element-text')
    if(zotero_publisher != None):
        print(zotero_publisher.text)
    zotero_issn = article.select_one('div#zotero-issn .element-text')
    if(zotero_issn != None):
        print(zotero_issn.text)
    zotero_issue = article.select_one('div#zotero-issue .element-text')
    if(zotero_issue != None):
        print(zotero_issue.text)
    zotero_publication_title = article.select_one('div#zotero-publication-title .element-text')
    if(zotero_publication_title != None):
        print(zotero_publication_title.text)
    zotero_url = article.select_one('div#zotero-url .element-text')
    if(zotero_url != None):
        print(zotero_url.text)
    zotero_volume = article.select_one('div#zotero-volume .element-text')
    if(zotero_volume != None):
        print(zotero_volume.text)

    ############### TYPE AGAIN ##############
    type2 = article.select_one('h2')
    if(type2 != None):
        print(type2.text)
    
    

    #print(authors_venue_year.get_text(strip=False))

itemfiles = soup.select_one('div#itemfiles div.element-text a')
href = itemfiles.get('href', '')
print(href)

collection = soup.select_one('div#collection div.element-text p a')
print(collection.text)

# |||||||||||||||||| TAGS HERE do checks? |||||||||||||||||||||||||
tags = soup.select('div#item-tags div.element-text a')
#for tag in tags:
#    print(tag.text)

print()