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
new_row = data
#df = pd.DataFrame(data)
#df.head()


testurl = "https://francolibrary.com/items/show/1922"
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
        new_row["title"].append(title.text)
    
    description = article.select_one('div#dublin-core-description .element-text')
    if(description != None):
        new_row["description"].append(description.text)

    creators = article.select('div#dublin-core-creator .element-text')
    if(creators != None):
        creatorStr = ""
        for creator in creators:
            creatorStr += creator.text + ";"
        if creatorStr != "":
            new_row["creator"].append(creatorStr[:-1])
    
    sources = article.select('div#dublin-core-source .element-text')
    if(sources != None):
        sourcelist = ""
        for source in sources:
            sourcelist += source.text + ";"
        if sourcelist != "":
            new_row["source"].append(sourcelist[:-1])
    
    publishers = article.select('div#dublin-core-publisher .element-text')
    if(publishers != None):
        publisherlist = ""
        for publisher in publishers:
            publisherlist += (publisher.text) + ";"
        if publisherlist != "":
            new_row["publisher"].append(publisherlist[:-1])
    
    date = article.select_one('div#dublin-core-date .element-text')
    if(date != None):
        new_row["date"].append(date.text)
    
    contributors = article.select('div#dublin-core-contributor .element-text')
    if(contributors != None):
        contributorlist = ""
        for contributor in contributors:
            contributorlist += (contributor.text) + ";"
        if contributorlist != "":
            new_row["contributor"].append(contributorlist[:-1])
    
    languages = article.select('div#dublin-core-language .element-text')
    if(languages != None):
        languagelist = ""
        for language in languages:
            languagelist += (language.text) + ";"
        if languagelist != "":
            new_row["language"].append(languagelist[:-1])
   
    rights = article.select_one('div#dublin-core-rights .element-text')
    if(rights != None):
        new_row["rights"].append(rights.text)
    
    relation = article.select_one('div#dublin-core-relation .element-text')
    if(relation != None):
        new_row["relation"].append(relation.text)
    
    format = article.select_one('div#dublin-core-format .element-text')
    if(format != None):
        new_row["format"].append(format.text)
    ########### ENTRY TYPE (might not be filled?) #############
    type1 = article.select_one('div#dublin-core-type .element-text')
    if(type1 != None):
        new_row["type1"].append(type1.text)
    ###### Identifier usually is html for a link ######
    identifiers = article.select('div#dublin-core-identifier .element-text a')
    if(identifiers != None):
        identifierlist = ""
        for identifier in identifiers:
            identifierlist += str(identifier) + ";"
        if identifierlist != "":
            new_row["identifier"].append(identifierlist[:-1])

    coverage = article.select_one('div#dublin-core-coverage .element-text')
    if(coverage != None):
        new_row["coverage"].append(coverage.text)

    ########### IGNORING CONTRIBUTION FORM ############
    ########### ZOTERO ###########
    zotero_genre = article.select_one('div#zotero-genre .element-text')
    if(zotero_genre != None):
        new_row["zotero_genre"].append(zotero_genre.text)
    
    zotero_distributor = article.select_one('div#zotero-distributor .element-text')
    if(zotero_distributor != None):
        new_row["zotero_distributor"].append(zotero_distributor.text)
    
    zotero_director = article.select_one('div#zotero-director .element-text')
    if(zotero_director != None):
        new_row["zotero_director"].append(zotero_director.text)
    
    zotero_performer = article.select('div#zotero-performer .element-text')
    if(zotero_performer != None):
        z_performerlist = ""
        for z_performer in zotero_performer:
            z_performerlist += (z_performer.text) + ";"
        if z_performerlist != "":
            new_row["z_performer"].append(z_performerlist[:-1])
    
    zotero_episode_number = article.select_one('div#zotero-episode-number .element-text')
    if(zotero_episode_number != None):
        new_row["zotero_episode_number"].append(zotero_episode_number.text)
    
    zotero_language = article.select_one('div#zotero-language .element-text')
    if(zotero_language != None):
        new_row["zotero_language"].append(zotero_language.text)
    
    zotero_network = article.select_one('div#zotero-network .element-text')
    if(zotero_network != None):
        new_row["zotero_network"].append(zotero_network.text)
    
    zotero_audio_recording_format = article.select_one('div#zotero-audio-recording-format .element-text')
    if(zotero_audio_recording_format != None):
        new_row["zotero_audio_recording_format"].append(zotero_audio_recording_format.text)
    
    zotero_label = article.select_one('div#zotero-label .element-text')
    if(zotero_label != None):
        new_row["zotero_label"].append(zotero_label.text)
    
    zotero_running_time = article.select_one('div#zotero-running-time .element-text')
    if(zotero_running_time != None):
        new_row["zotero_running_time"].append(zotero_running_time.text)
    
    zotero_num_pages = article.select_one('div#zotero-num-pages .element-text')
    if(zotero_num_pages != None):
        new_row["zotero_num_pages"].append(zotero_num_pages.text)
    
    zotero_place = article.select_one('div#zotero-place .element-text')
    if(zotero_place != None):
        new_row["zotero_place"].append(zotero_place.text)
    
    zotero_publisher = article.select_one('div#zotero-publisher .element-text')
    if(zotero_publisher != None):
        new_row["zotero_publisher"].append(zotero_publisher.text)
    
    zotero_issn = article.select_one('div#zotero-issn .element-text')
    if(zotero_issn != None):
        new_row["zotero_issn"].append(zotero_issn.text)
    
    zotero_isbn = article.select_one('div#zotero-isbn .element-text')
    if(zotero_isbn != None):
        new_row["zotero_isbn"].append(zotero_isbn.text)
    
    zotero_issue = article.select_one('div#zotero-issue .element-text')
    if(zotero_issue != None):
        new_row["zotero_issue"].append(zotero_issue.text)
    
    zotero_publication_title = article.select_one('div#zotero-publication-title .element-text')
    if(zotero_publication_title != None):
        new_row["zotero_publication_title"].append(zotero_publication_title.text)
    
    zotero_url = article.select('div#zotero-url .element-text')
    if(zotero_url != None):
        z_urllist = ""
        for z_url in zotero_url:
            z_urllist += (z_url.text) + ";"
        if z_urllist != "":
            new_row["z_url"].append(z_urllist[:-1])

    zotero_volume = article.select_one('div#zotero-volume .element-text')
    if(zotero_volume != None):
        new_row["zotero_volume"].append(zotero_volume.text)
    
    zotero_short_title = article.select_one('div#zotero-short-title .element-text')
    if(zotero_short_title != None):
        new_row["zotero_short_title"].append(zotero_short_title.text)
    
    zotero_references = article.select('div#zotero-references .element-text')
    if(zotero_references != None):
        z_reflist = ""
        for z_ref in zotero_references:
            z_reflist += (z_ref.text) + ";"
        if z_reflist != "":
            new_row["z_ref"].append(z_reflist[:-1])

    ############### TYPE AGAIN ##############
    # Ignoring - Dont need repitions
    #type2 = article.select_one('h2')
    #if(type2 != None):
    #    new_row["type2"].append(type2.text)
    
    

    #print(authors_venue_year.get_text(strip=False))

# NEED CHECKER FOR JPG vs other filetypes 
itemfiles = soup.select('div#itemfiles div.element-text a')
fileslist = ""
for itemF in itemfiles:
    files = itemF.get('href', '')
    fileslist += (files) + ";"
if fileslist != "":
    new_row["files"].append(fileslist[:-1])

collection = soup.select_one('div#collection div.element-text p a')
#print(collection.text)

# |||||||||||||||||| TAGS HERE do checks? |||||||||||||||||||||||||
tags = soup.select('div#item-tags div.element-text a')
taglist = ""
for tag in tags:
    taglist += tag.text + ";"
new_row["tags"].append(taglist[:-1])

for key in new_row:
    if new_row[key] == []:
        new_row[key].append(pd.NA)

#for key in new_row:
#    print(new_row[key])

#print(new_row)
#df = pd.DataFrame.from_records(new_row)

#print(new)
#df = pd.DataFrame.from_records(data)
df = pd.DataFrame(new_row)
df.to_csv('franco_articles.csv')
#df.head()



