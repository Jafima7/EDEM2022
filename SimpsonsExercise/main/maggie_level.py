from urllib import response
import pip._vendor
from pip._vendor import requests
import time
import csv
import json

response = requests.get("https://thesimpsonsquoteapi.glitch.me/quotes")

quotes_dict = {"character": "Homer", "quote": "Doh!"}

def simpsons_quotes():
  while True:
    response = requests.get("https://thesimpsonsquoteapi.glitch.me/quotes")
    json_file = response.json()[0]
    if(json_file['character'] == "Lisa Simpson"):
      with open('Lisa/lisa_quotes.csv', 'a') as Lisa:
        quotes_dict = {'character': json_file['character'], 'quote': json_file['quote']}
        w = csv.DictWriter(Lisa, quotes_dict.keys())
        w.writerow(quotes_dict)
      with open('General/general.csv', 'a') as General:
        w2 = csv.DictWriter(General, quotes_dict.keys())
        w2.writerow(quotes_dict)
    elif(json_file['character'] == "Homer Simpson"):
      with open('Homer/homer_quotes.csv', 'a') as Homer:
        quotes_dict = {'character': json_file['character'], 'quote': json_file['quote']}
        w3 = csv.DictWriter(Homer, quotes_dict.keys())
        w3.writerow(quotes_dict)
      with open('General/general.csv', 'a') as General:
        w4 = csv.DictWriter(General, quotes_dict.keys())
        w4.writerow(quotes_dict)   
    else:
      with open('General/general.csv', 'a') as General:
        quotes_dict = {'character': json_file['character'], 'quote': json_file['quote']}
        w5 = csv.DictWriter(General, quotes_dict.keys())
        w5.writerow(quotes_dict)
    print(quotes_dict)
    time.sleep(30)
    
simpsons_quotes()

  
  


  







