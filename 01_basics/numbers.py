import math #importing library
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

print(oct(23))
print(hex(14))
print(bin(6))
