import os
import json
# names = ["Liam","Emma","Noah","Olivia","Ethan","Ava","Lucas","Sophia","Mason","Mia"]

def save_names(names):
  with open('randomNames.txt', 'w') as file:
    json.dump(names, file)

def load_names():
    if os.path.exists('randomNames.txt'):
        with open('randomNames.txt', 'r') as file:
            return json.load(file)
    else:
       print('No names available at the moment')    
       return[]

my_names = load_names()
my_names.append('Liam')
save_names(my_names)