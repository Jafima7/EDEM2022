import numpy as np
import urllib
from urllib import response
import pip._vendor
from pip._vendor import requests
import time
import csv
import json
import os

response = requests.get("https://thesimpsonsquoteapi.glitch.me/quotes")

quotes_dict = {"character": "Homer", "quote": "Doh!"}

def simpsons_quotes():
  while True:
    response = requests.get("https://thesimpsonsquoteapi.glitch.me/quotes")
    json_file = response.json()[0]
    if(json_file['character'] == "Lisa Simpson"):
      with open('Lisa Simpson/lisa.csv', 'a') as Lisa:
        quotes_dict = {'character': json_file['character'], 'quote': json_file['quote']}
        w = csv.DictWriter(Lisa, quotes_dict.keys())
        w.writerow(quotes_dict)
        urllib.request.urlretrieve(json_file['image'],'Lisa Simpson/image.jpeg')
      with open('general.csv', 'a') as General:
        w2 = csv.DictWriter(General, quotes_dict.keys())
        w2.writerow(quotes_dict)
    elif(json_file['character'] == "Homer Simpson"):
      with open('Homer Simpson/homer.csv', 'a') as Homer:
        quotes_dict = {'character': json_file['character'], 'quote': json_file['quote']}
        w3 = csv.DictWriter(Homer, quotes_dict.keys())
        w3.writerow(quotes_dict)
        urllib.request.urlretrieve(json_file['image'],'Homer Simpson/image.jpeg')  
      with open('general.csv', 'a') as General:
        w4 = csv.DictWriter(General, quotes_dict.keys())
        w4.writerow(quotes_dict)    
    else:
      char = json_file['character']
      if not os.path.exists(f'''{char}'''):
        os.makedirs(f'''{char}''')
        urllib.request.urlretrieve(json_file['image'],f'''{char}/image.jpeg''')
      with open(f'''{char}/{char}.csv''', 'a') as char:
        quotes_dict = {'character': json_file['character'], 'quote': json_file['quote']}
        w5 = csv.DictWriter(char, quotes_dict.keys())
        w5.writerow(quotes_dict) 
      with open('general.csv', 'a') as General:
        quotes_dict = {'character': json_file['character'], 'quote': json_file['quote']}
        w5 = csv.DictWriter(General, quotes_dict.keys())
        w5.writerow(quotes_dict)

    count = {}
    input_line = json_file['quote']
    list_of_words = input_line.split()
    for word in list_of_words:
      count[word] = count.get(word, 0) + 1
    print('Word Frequency')
    for key in count.keys():
      print(key, count[key])

    time.sleep(30)
    
simpsons_quotes()