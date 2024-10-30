import pandas as pd

data = {"title":[1], "description":[1], "creator":[1], "source":[1], "publisher":[1], "date":[1],
        "contributor":[1], "language":[1], "rights":[1], "relation":[1], "format":[1], "type1":[1],
        "identifier":[1], "coverage":[1], "zotero_genre":[1],"zotero_distributor":[1],"zotero_director":[1],
        "z_performer":[1],"zotero_episode_number":[1], "zotero_language":[1],"zotero_network":[1],
        "zotero_audio_recording_format":[1],"zotero_label":[1], "zotero_running_time":[1],
        "zotero_num_pages":[1],"zotero_place":[1],"zotero_publisher":[1],
        "zotero_issn":[1],"zotero_isbn":[1],"zotero_issue":[1],"zotero_publication_title":[1],"z_url":[1],
        "zotero_volume":[1],"zotero_short_title":[1],"z_ref":[1],"type2":[1],"files":[1],
        "tags":[1]}

new_row = data
df = pd.DataFrame(data)
print(df.head())