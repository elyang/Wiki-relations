
# Import the web-scapping tool
from bs4 import BeautifulSoup

# Get webpages
import requests

# Dataframe
import pandas as pd

# save Coronavirus Wikipedia page as a "response" object
url = requests.get('https://en.m.wikipedia.org/wiki/Coronavirus')

soup = BeautifulSoup(url.content, 'html.parser')

# Define functions that locate tags that contain terms we want

# Each term has these 2 attributes defined: href and title
def has_href_and_title(tag):
    return tag.has_attr('href') and tag.has_attr('title') 

# The url in each term direct to a English Wikipedia page
def to_wiki_page(tag):
    if has_href_and_title(tag):
        base_url = '/wiki/'
        return tag['href'].startswith(base_url)
    return False
# The attribute value of 'title' is equal to the string enclosed by that tag
def herf_eql_str(tag):
    if to_wiki_page(tag):
        return tag['title'].lower() == tag.text[:].lower()
    return False

# Find all such tags
records = soup.find_all(herf_eql_str) 
# record is a ResultSet object
# Create a dictionary to store the term: url pairs
virus_dict = {}

# Loop through all terms to get the name and url
# Save the records into a Dataframe
for record in records:
    print(record.text)
    
    name = record.text[:]
    url = record['href']
    # use a dictionary of terms to remove duplicates
    virus_dict[name] = url

print(virus_dict)
    
# #df_coronavirus = pd.Dataframe(records)
# print(records)
# # Exporting as a CSV file