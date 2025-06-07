#importing library
import math 
import random
x = 1
y = 2
z = 2

res1 = x + y * z #avoid this method 
res2 = (x + y) * z #we use this in industry level

print(res1)
print(res2)

#avoid using diff data types even if its no
a = 9
b = 6.7
add1 = a + b
#convert the value explictly
add2 = a + int(b)

print(add1)
print(add2)

print(a, b)
# print(2 ** 10000)

print(repr('paris'))
print(str('paris'))
print('paris')
# repr() : use for clear representation and debugging and mainly use by developer. 
# str() :  represent as readable for human.
# print() : internally it use str() to get object and print it.

num1 = 2.2
num2 = 7
mul = math.floor(num1 * num2)
print(mul)

#for hexadecimal,octal and binary calculation
#method 1
print(oct(23))
print(hex(14))
print(bin(6))
#method 2
# Convert string representations of numbers in different bases to decimal (base 10)
octal_number = '56'
decimal_from_octal = int(octal_number, 8)  # 8 is the base for octal numbers
print(decimal_from_octal)  # Output: 46

print(random.random())
print(random.randint(1,10))

l1 = ['newyork' , 'paris' , 'korea', 'london' , 'Austria']
print(random.choice(l1))
random.shuffle(l1)
print(l1)

setone = {1,2,3,4}
re = setone & {1,3}
re1 = setone | {1,3}
print(re, res1)
print(res1)