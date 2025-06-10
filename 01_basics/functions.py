#question 1

def square(num):
    return  num ** 2
   
res = square(3)    
print(res)

#question 2
def sum(a, b):
    return a + b

print(sum(1,2))

#question 3
import math

def area(radius):
    return math.pi * radius ** 2

print(math.floor(area(3)))

#question 4
def greet(name='user'):
    return 'Hello, ' + name + '!'

print(greet())

#question 5 lambda functions
cube = lambda x: x ** 3
print(cube(3))

#question 6

# def sum_all(*args):
#     return sum(args)


# print(sum_all(2,3,4,5))
# print(sum_all(2,5))
# print(sum_all(2,3,4,5,8,9,6,4))
# print(sum_all(2,3,4,5,3,6,7))


#question 7
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_kwargs(name="shaktiman", power="lazer")
print_kwargs(name="shaktiman")
print_kwargs(name="shaktiman", power="lazer", enemy = "Dr. Jackaal")


#question 8
def even_generator(limit):
    for i in range(2, limit + 1, 2):
        yield i



for num in even_generator(10):
    print(num)


#question 9
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)