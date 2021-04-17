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
  output = "\n".join(list(result['google_api_result'].values()))
  return output


# To Retrieve db data containing specific keyword
def get_search_results(recent_searched_word):
  
  searched_results = []

  for key,val in db.items():
    if recent_searched_word in val:
      print ("val", val, type(val))
      val = json.loads(val)
      searched_results.append(val["searched_words"])
  output = "\n".join([str(a) for a in searched_results])
  # return db.getAll()

  return output
