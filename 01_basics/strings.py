city = 'paris'
print(city[0:2]) #slicing method
print(city[3]) #getting 3rd character
print(city)

num = '0123456789'
print(num[0:9:3]) #last index 3 means we take values after 3 digits like 0,3,6
print(city.upper())
name = '     sara        '
print(name.strip()) #to remove spaces

teaName = 'Lemon tea'
print(teaName.replace('Lemon' , 'ginger'))

fruits = "apple, banana, mango, orange"
print(fruits.split()) #to convert string into list (default splits on whitespace)
print(fruits.split(", ")) #splits on comma and space
country = 'Us England Uk'
print(country.find('England')) #to find the index of that string 
alph = 'A B B B C D E E E E Z Z Z Z'
print(alph.count('B'))

#order format
order = "I want {} pieces of {}."
print(order.format(3, "cake"))

# Example: Convert list to string
letters = ['H', 'e', 'l', 'l', 'o']
print("".join(letters))  # Output: Hello
print("-".join(letters))
print(len(city)) #for finding the length
for letter in city:
    print(letter)

#Using escape character to include quotes in a string
dialogue = 'She replied, \"I prefer coffee.\"'
print(dialogue)

#Using raw strings (r"").
print(r"C:\Users\username\Documents")

# Using \n for newline
print("Line 1\nLine 2\nLine 3")

