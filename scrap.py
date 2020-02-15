
# Import the web-scapping tool
from bs4 import BeautifulSoup

# Get webpages
import requests

# Dataframe
import pandas as pd

# save Coronavirus Wikipedia page as a "response" object
url = requests.get('https://en.wikipedia.org/wiki/Coronavirus')

soup = BeautifulSoup(url.content, 'html.parser')

# Define functions that locate tags that contain terms we want

# Each term has these 2 attributes defined: href and title
def has_href_and_title(tag):
    return tag.has_attr('href') and tag.has_attr('title') 
# The tag attribute 'title' is equal to the string enclosed
# def herf_eql_str(tag):
#     title = tag['title']
#     string = 
# The url in each term direct to a English Wikipedia page
def to_wiki_page(tag):
    if has_href_and_title(tag):
        base_url = '/wiki/'
        print(tag['href'])
        print(type(tag['href']))
        return tag['href'].startswith(base_url)
    return False


# Find all such tags
records = soup.find_all(to_wiki_page) 
# record is a ResultSet object


# Loop through all terms to get the name and url
# Save the records into a Dataframe

for record in records:

    print(record.text)
#     if base_url in link.get('herf'):

#         record.content.find_all('a')



#         name = term.get('title')
#         url = term.get('href')

#     records.append((name, url))

# #df_coronavirus = pd.Dataframe(records)
# print(records)
# # Exporting as a CSV file