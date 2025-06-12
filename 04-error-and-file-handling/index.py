file = open('test.py' , 'w') #by writing w it automatically create test.py if its not exist
#we use try and catch for file handling

try:
    file.write('File')
finally:
    file.close()

#better way instead of using try catch we use this 

with open('test.py') as file:
    file.write('Hello world')     