from bs4 import BeautifulSoup
import requests
import pandas as pd
#import time
import copy

data = {"z_url": []}

new_row = copy.deepcopy(data)
df = pd.DataFrame(data)

base_url = "https://francolibrary.com/items/show/"
page = 3
current_url = base_url + str(page)


while (page <= 2202): 
    new_row = copy.deepcopy(data)
    current_url = base_url + str(page)
    page += 1
    print("current page " + str(page-1))

    response = requests.get(current_url)
    #print(response)

    html = response.content
    #print(html)

    soup = BeautifulSoup(html, "lxml")
    #print(soup)
    all_articles = soup.find_all("div", class_="element-set")
    for article in all_articles:
        zotero_url = article.select('div#zotero-url .element-text')
        if(zotero_url != None):
            z_urllist = ""
            for z_url in zotero_url:
                z_urllist += (str(z_url)) + ";"
            if z_urllist != "":
                new_row["z_url"].append(z_urllist[:-1])

    for key in new_row:
        if new_row[key] == []:
            new_row[key].append(pd.NA)

    #print(new_row)
    df = pd.concat([df, pd.DataFrame(new_row)], ignore_index=True)

print(df)

df.to_excel('z_urls.xlsx', index=False)
print("DONE!")