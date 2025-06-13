import os
try:
  with open('programming.txt' , 'r') as file:
    print('File exists! Contents: ')
    print(file.read())
except:
      print('File not found')