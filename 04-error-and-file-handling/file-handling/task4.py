import json
fruits = ['Apple' , 'Mango' , 'Orange']
with open('fruits.json' , 'w') as file:
    json.dump(fruits, file)