import numpy as np
import urllib
from urllib import response
import pip._vendor
from pip._vendor import requests
import time
import csv
import json
import numpy as np
import cv2

def url_to_image(url):
  resp = urllib.urlopen(url)
  image = np.asarray(bytearray(resp.read()), dtype="uint8")
  image = cv2.imdecode(image, cv2.IMREAD_COLOR)
  return image

response = requests.get("https://thesimpsonsquoteapi.glitch.me/quotes")

quotes_dict = {"character": "Homer", "quote": "Doh!"}

def simpsons_quotes():
  while True:
    response = requests.get("https://thesimpsonsquoteapi.glitch.me/quotes")
    json_file = response.json()[0]
    if(json_file['character'] == "Lisa Simpson"):
      with open('/Users/javierfm/Documents/GitHub/Javier_EDEM2022/SimpsonsExercise/main/lisa_quotes.csv', 'a') as Lisa:
        quotes_dict = {'character': json_file['character'], 'quote': json_file['quote'], 
                      'image': url_to_image(json_file['image'])}
        w = csv.DictWriter(Lisa, quotes_dict.keys())
        w.writerow(quotes_dict)
      with open('/Users/javierfm/Documents/GitHub/Javier_EDEM2022/SimpsonsExercise/main/general.csv', 'a') as General:
        w2 = csv.DictWriter(General, quotes_dict.keys())
        w2.writerow(quotes_dict)
    elif(json_file['character'] == "Homer Simpson"):
      with open('/Users/javierfm/Documents/GitHub/Javier_EDEM2022/SimpsonsExercise/main/homer_quotes.csv', 'a') as Homer:
        quotes_dict = {'character': json_file['character'], 'quote': json_file['quote'], 
                      'image': url_to_image(json_file['image'])}
        w3 = csv.DictWriter(Homer, quotes_dict.keys())
        w3.writerow(quotes_dict)
      with open('/Users/javierfm/Documents/GitHub/Javier_EDEM2022/SimpsonsExercise/main/general.csv', 'a') as General:
        w4 = csv.DictWriter(General, quotes_dict.keys())
        w4.writerow(quotes_dict)   
    else:
      with open('/Users/javierfm/Documents/GitHub/Javier_EDEM2022/SimpsonsExercise/main/general.csv', 'a') as General:
        quotes_dict = {'character': json_file['character'], 'quote': json_file['quote'], 
                      'image': url_to_image(json_file['image'])}
        w5 = csv.DictWriter(General, quotes_dict.keys())
        w5.writerow(quotes_dict)
    print(quotes_dict)
    time.sleep(30)
    
simpsons_quotes()