user = {
    'name' : 'Liza',
    'age' : 21,
    'country' : 'France',
    'city' : 'paris'
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

#another way of printing keys with values
for key, value in user.items():
    print(key, "-> ", value)

#using conditionals in maps
if "age" in user:
    print('have it')
#for finding the length 
print(len(user))    

#for adding values 
user['isLoggedIn'] = 'true'
print(user)

#for removing specific value we need to provide key
user.pop('age')
print(user)
#for removing last value with key
user.popitem()
print(user)

#for deleting any key+value directly from memory
del user['city']
print(user)

#for copying the ref 
userCpy = user.copy()

#dictionary inside dictionary
person = {
    "name": "John",
    "age": 30,
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "state": "NY",
        "zip": "10001"
    }
}
print(person['address']['city'])


# Create a list of keys
keys = ['Apple', 'Mango', 'Orange']

# Set a default value for all keys
default_value = "Fruits"

# Create a new dictionary with the specified keys and default value
new_addict = dict.fromkeys(keys, default_value)

# Print the new dictionary
print(new_addict)

new_addict = dict.fromkeys(keys, keys)
print(new_addict)


