Welcome to the Franco-American Bibliography of Published Works Data Migration and Geolocation Project!
Here are the files and process of transferring Franco-American published works from francolibrary.com to francolibrary.org.
Process:
1. webscrape francolibrary.com
2. Sanitize dataset for accented characters and normalize tags
3. Categorize data into collections
4. Import to Omeka via CSV import plugin
Adding Geolocation Data
5. Try mapping solutions
6. Output tags to txt file as searchable links
7. input geolocation data in omeka

File Breakdown: 
Webscrape_Sanitize : Python, CSV, and Excel files for webscraping and sanitizing data
Datasets : Combination of CSVs and Excel files that hold varying states of Published works
	- csv_Outs : Categories that can be imported to Omeka via CSV import plugin
	- OldCSVs  : Ogininal webscrapes of francolibrary.com
	- outs	   : excels of categories for transformations due to accented character artifacts
Map :  Attempt at using natural language processing and initial webscrape to geolocate works based on locations mentioned in coverage and description
taglinks.py & taglinks.txt : python script and output txt that has HTML elements that link to a search for the tag. To be input for geolocation data to make it clickable. 

