import requests

def generate_questions():
  response = requests.get("https://opentdb.com/api.php? amount=10&category=18&difficulty=easy&type=multiple")
  #print(response.json())
  return response.json()
  
  