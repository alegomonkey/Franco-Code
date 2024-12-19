import pandas as pd
import spacy

# Download & Load the French multilingual model
# DOWNLOAD -> python -m spacy download fr_core_news_sm
nlp = spacy.load("fr_core_news_sm")

# Read the description CSV 
df = pd.read_csv("franco_articles_comp_D_cleaned.csv", encoding="utf-8")

# Process description column
discriptionLocations = []
for _, row in df.iterrows():
    doc = nlp(row['description'])
    
    # Extract location entities (GPE and LOC types)
    # GPE - countries, cities, states
    # LOC - non gpe locations: mountain ranges, bodies of water
    location_entities = [ent.text for ent in doc.ents if ent.label_ in ['GPE', 'LOC']]
    
    # Clean up location names (e.g., remove punctuation)
    cleaned_locations = [''.join(e for e in loc if e.isalnum() or e.isspace()).strip().lower() for loc in location_entities]
    
    discriptionLocations.extend(cleaned_locations)

# Store extracted locations in DF
Locdf = pd.DataFrame(discriptionLocations, columns=["location"])

# Export CSV
Locdf.to_csv("descriptionLocations.csv")

#######################
# Compare to coverage #
#######################

# open the coverage CSV
df = pd.read_csv("franco_articles_comp_C_cleaned.csv", encoding="utf-8")

# Process coverage column
coverageLocations = []
for _, row in df.iterrows():
    doc = nlp(row['coverage'])
    
    # Extract location entities (GPE and LOC types)
    # GPE - countries, cities, states
    # LOC - non gpe locations: mountain ranges, bodies of water
    location_entities = [ent.text for ent in doc.ents if ent.label_ in ['GPE', 'LOC']]
    
    # Clean up location names (e.g., remove punctuation)
    cleaned_locations = [''.join(e for e in loc if e.isalnum() or e.isspace()).strip().lower() for loc in location_entities]
    
    coverageLocations.extend(cleaned_locations)

# Store extracted locations in DF
Locdf = pd.DataFrame(coverageLocations, columns=["location"])

# Export CSV
Locdf.to_csv("coverageLocations.csv")