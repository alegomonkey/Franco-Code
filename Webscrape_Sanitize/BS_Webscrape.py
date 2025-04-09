#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 9:03 2024
Creator: Johnny Sylvain
Based on Chaofan Chen's example BS
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd
#import time

#SETUP PANDAS DATAFRAME
data = {"title":[], "description":[], "creator":[], "source":[], "publisher":[], "date":[],
         "contributor":[], "language":[], "rights":[], "relation":[], "format":[], "type1":[],
         "identifier":[], "coverage":[], "zotero_genre":[],"zotero_distributor":[],"zotero_director":[],
         "z_performer":[],"zotero_episode_number":[], "zotero_language":[],"zotero_network":[],
         "zotero_audio_recording_format":[],"zotero_label":[], "zotero_running_time":[],
         "zotero_num_pages":[],"zotero_place":[],"zotero_publisher":[],
         "zotero_issn":[],"zotero_isbn":[],"zotero_issue":[],"zotero_publication_title":[],"z_url":[],
         "zotero_volume":[],"zotero_short_title":[],"z_ref":[],"type2":[],"files":[],
         "tags":[]}
df = pd.DataFrame(data)


testurl = "https://francolibrary.com/items/show/3"
first_url = "https://francolibrary.com/items/show/3"
url = "https://scholar.google.com/scholar?as_ylo=2024&q=machine+learning&hl=en&as_sdt=0,20"

#URL LOOPING
base_url = "https://francolibrary.com/items/show/"
page = 3
current_url = base_url + str(page)

"""
while (page <= 2202): 
    current_url = base_url + str(page)
    page += 1
"""


response = requests.get(testurl)
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
    creators = article.select('div#dublin-core-creator .element-text')
    if(creators != None):
        for creator in creators:
            print(creator.text)
    sources = article.select('div#dublin-core-source .element-text')
    if(sources != None):
        for source in sources:
            print(source.text)
    publishers = article.select('div#dublin-core-publisher .element-text')
    if(publishers != None):
        for publisher in publishers:
            print(publisher.text)
    date = article.select_one('div#dublin-core-date .element-text')
    if(date != None):
        print(date.text)
    contributors = article.select('div#dublin-core-contributor .element-text')
    if(contributors != None):
        for contributor in contributors:
            print(contributor.text)
    languages = article.select('div#dublin-core-language .element-text')
    if(languages != None):
        for language in languages:
            print(language.text)
    rights = article.select_one('div#dublin-core-rights .element-text')
    if(rights != None):
        print(rights.text)
    relation = article.select_one('div#dublin-core-relation .element-text')
    if(relation != None):
        print(relation.text)
    format = article.select_one('div#dublin-core-format .element-text')
    if(format != None):
        print(format.text)
    ########### ENTRY TYPE (might not be filled?) #############
    type1 = article.select_one('div#dublin-core-type .element-text')
    if(type1 != None):
        print(type1.text)
    ###### Identifier usually is html for a link ######
    identifiers = article.select('div#dublin-core-identifier .element-text a')
    if(identifiers != None):
        for identifier in identifiers:
            print(identifier.text)
    coverage = article.select_one('div#dublin-core-coverage .element-text')
    if(coverage != None):
        print(coverage.text)

    ########### IGNORING CONTRIBUTION FORM ############
    ########### ZOTERO ###########
    
    zotero_genre = article.select_one('div#zotero-genre .element-text')
    if(zotero_genre != None):
        print(zotero_genre.text)
    zotero_distributor = article.select_one('div#zotero-distributor .element-text')
    if(zotero_distributor != None):
        print(zotero_distributor.text)
    zotero_director = article.select_one('div#zotero-director .element-text')
    if(zotero_director != None):
        print(zotero_director.text)
    zotero_performer = article.select('div#zotero-performer .element-text')
    if(zotero_performer != None):
        for z_performer in zotero_performer:
            print(z_performer.text)
    zotero_episode_number = article.select_one('div#zotero-episode-number .element-text')
    if(zotero_episode_number != None):
        print(zotero_episode_number.text)
    zotero_language = article.select_one('div#zotero-language .element-text')
    if(zotero_language != None):
        print(zotero_language.text)
    zotero_network = article.select_one('div#zotero-network .element-text')
    if(zotero_network != None):
        print(zotero_network.text)
    zotero_audio_recording_format = article.select_one('div#zotero-audio-recording-format .element-text')
    if(zotero_audio_recording_format != None):
        print(zotero_audio_recording_format.text)
    zotero_label = article.select_one('div#zotero-label .element-text')
    if(zotero_label != None):
        print(zotero_label.text)
    zotero_running_time = article.select_one('div#zotero-running-time .element-text')
    if(zotero_running_time != None):
        print(zotero_running_time.text)
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
    zotero_isbn = article.select_one('div#zotero-isbn .element-text')
    if(zotero_isbn != None):
        print(zotero_isbn.text)
    zotero_issue = article.select_one('div#zotero-issue .element-text')
    if(zotero_issue != None):
        print(zotero_issue.text)
    zotero_publication_title = article.select_one('div#zotero-publication-title .element-text')
    if(zotero_publication_title != None):
        print(zotero_publication_title.text)
    zotero_url = article.select('div#zotero-url .element-text')
    if(zotero_url != None):
        for z_url in zotero_url:
            print(z_url.text)
    zotero_volume = article.select_one('div#zotero-volume .element-text')
    if(zotero_volume != None):
        print(zotero_volume.text)
    zotero_short_title = article.select_one('div#zotero-short-title .element-text')
    if(zotero_short_title != None):
        print(zotero_short_title.text)
    zotero_references = article.select('div#zotero-references .element-text')
    if(zotero_references != None):
        for z_ref in zotero_references:
            print(z_ref.text)

    ############### TYPE AGAIN ##############
    type2 = article.select_one('h2')
    if(type2 != None):
        print(type2.text)
    
    

    #print(authors_venue_year.get_text(strip=False))

# NEED CHECKER FOR JPG vs other filetypes 
itemfiles = soup.select('div#itemfiles div.element-text a')
for itemF in itemfiles:
    files = itemF.get('href', '')
    print(files)

collection = soup.select_one('div#collection div.element-text p a')
print("COLLECTION: ")
print(collection.text)

# |||||||||||||||||| TAGS HERE do checks? |||||||||||||||||||||||||
tags = soup.select('div#item-tags div.element-text a')
#for tag in tags:
#    print(tag.text)

print()
df.head()

