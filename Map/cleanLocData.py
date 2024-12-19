import pandas as pd

# import csv and drop rows with NAN in description or coverage
df = pd.read_csv('franco_articles_comp - v2.csv', encoding='utf-8', index_col=0)
df_d_cleaned = df.dropna(subset=['description'])
df_d_cleaned.to_csv('franco_articles_comp_D_cleaned.csv')

df = pd.read_csv('franco_articles_comp - v2.csv', encoding='utf-8', index_col=0)
df_c_cleaned = df.dropna(subset=['coverage'])
df_c_cleaned.to_csv('franco_articles_comp_C_cleaned.csv')