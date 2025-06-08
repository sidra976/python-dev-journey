#for taking userinput
# userInput = input('Enter age: ')
userInput = 12
userInput = int(userInput) #input always stored in string so we convert it by using int, float etc

if userInput < 13 :
    print('Child')
elif userInput < 20 :
    print('Teen')
elif userInput < 59 :
    print('Adult')
else :
    print('Senior')  

#movie ticket 
day = 'Tuesday'  # Day of the week
age = 29         # Person's age

# Set base price: $12 for adults (18+), $8 for children
price = 12 if age >= 18 else 8 

# Apply $2 discount if it's Wednesday
if day == 'Wednesday':
    price = price - 2
else:
    price = price    

print(price)  # Output the final ticket price

marks = 123
#for exiting the program we use exit()
if marks >= 100 or marks < 0:
    print('Please enter marks between 0 - 100')
    exit()

if marks >= 90:
    grade = 'A'
elif marks >= 80:
    grade = 'B'
elif marks >= 70:
    grade = 'C'
elif marks >= 60:
    grade = 'D'
else:
    grade = 'F'    
print(grade)        

fruit = 'Banana'
color = 'Yellow'

if fruit == 'Banana':
    if color == 'Green':
        print('Unripe')
    elif color == 'Yellow':
        print('ripe')
    elif color == 'Brown':
        print('OverRipe')      




                 
