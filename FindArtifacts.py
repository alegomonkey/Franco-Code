import pandas as pd
import re

df = pd.read_csv('franco_articles_comp - v2.csv', encoding='utf-8', index_col=0)
def count_non_alphabet_special_chars(df):
    result = {}
    
    # Iterate over each column in the DataFrame
    for column in df.columns:
        # Initialize count for each character to 0
        char_count = {}
        
        # Iterate over each string value in the column
        for text in df[column]:
            if isinstance(text, str):
                # Count occurrences of non-alphabet characters
                for char in re.findall(r'[^a-zA-Z]', text):
                    char_count[char] = char_count.get(char, 0) + 1
        
        # Add counts to result dictionary
        result[column] = char_count
    
    return result

# Example usage
# Assuming you have a DataFrame named 'df'
result = count_non_alphabet_special_chars(df)

# Print the results
for column, char_counts in result.items():
    print(f"Column: {column}")
    for char, count in char_counts.items():
        print(f"  {char}: {count}")
    print()
