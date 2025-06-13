import json
import os

def load_tasks():
   try:
    os.path.exists('fruits.json')
    with open('fruits.json' , 'r') as file:
      return json.load(file)
   except:
        return []
   

def save_tasks(fruits):
   with open('fruits.txt', 'w') as file:
      json.dump(fruits, file)
       
