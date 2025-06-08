user = {
    'name' : 'Liza',
    'age' : 21,
    'country' : 'paris'
}
print(user) #for printing all values and keys
print(user['age']) #for print the specific value
print(user.get('age')) #another way for print the specific value

user['name'] = 'Alexa' #for changing the value of key value
print(user)

#looping on maps
#for getting keys
for keys in user:
    print(keys)

#for getting keys with values    
for keys in user:
    print(keys, user[keys])
