from replit import db
from google_api import get_google_search_results
import json


# To Create Db Entries
def update_search_history(searched_words, user):
  result = {
    "user":user.name,
    "searched_words":searched_words,
    "google_api_result": get_google_search_results(searched_words)
  }
  
  db[len(db)+1] = json.dumps(result)
  # print(db['searched_words'])
  # return result['google_api_result']
  return result['google_api_result']


# To Retrieve db data containing specific keyword
def get_search_results(recent_searched_word):
  
  searched_results = []

  for key,val in db.items():
    if recent_searched_word in val:
      searched_results.append(val)
  # return db.getAll()

  return searched_results
