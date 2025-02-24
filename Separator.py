## SEPARATE csv into categories
import pandas as pd
#df = pd.read_csv('franco_articles_comp - v2.csv', encoding='utf-8', errors='replace', index_col=0)
#print(df)

#df = pd.read_csv('franco_articles_comp - v2.csv', encoding='utf-8', encoding_errors='surrogateescape',index_col=0)
df = pd.read_excel('Full_Unseparated_FAC.xlsx', index_col=0)
dfs = {value: df[df['collection'] == value] 
       for value in df['collection'].unique()}

count = 0 
for sheet_name, dataf in dfs.items():
       name = str(count)+'out.xlsx'
       #print(name)
       #print(type(val))
       print(str(count) + " " + str(sheet_name))
       count += 1
       #dataf.to_excel(name)
       
#print(dfs)
#df.to_excel('testoutput.xlsx')
    

