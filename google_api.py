import json
import requests
import os


# Fun to get search results using google api
def get_google_search_results(word_to_search):
  links = {}
  url = "https://www.googleapis.com/customsearch/v1"
  PARAMS = {
    "key":os.getenv("KEY"),
    "cx":os.getenv("cx"),
    "q":word_to_search
  }
  response = requests.get(
    url,
    params=PARAMS
  )
  if response.status_code==200:
    response_data = json.loads(response.text)
    # Parsing only links from response data to a dict with count as key 
    for index, val in enumerate(response_data.get('items')):
      links[index+1]=val.get("link")
  return links 