import os
try:
  with open('programmingy.txt' , 'r') as file:
    print('File exists! Contents: ')
    print(file.read())
except:
      print('File not found')