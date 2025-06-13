import json
with open('fruits.json' , 'r') as file:
    fruit = json.load(file)

print('Fruits: ', fruit)   

