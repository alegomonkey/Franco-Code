from bs4 import BeautifulSoup
import requests
import pandas as pd
#import time
import copy

data = {"collection": [], "test": []}

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

    collection = soup.select_one('div#collection div.element-text p a')
    if(collection != None):
        new_row["collection"].append(collection.text)

    for key in new_row:
        if new_row[key] == []:
            new_row[key].append(pd.NA)

    #print(new_row)
    df = pd.concat([df, pd.DataFrame(new_row)], ignore_index=True)

df.to_excel('categories.xlsx')
print("DONE!")