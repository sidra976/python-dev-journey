list = ['mango' , 'apple' , 'peach']
for fruit in list:
    print(fruit)

numbers = [0,-1,2,3,-4,-6,-9]
count_positive_int = 0

for x in numbers:
    if x > 0:
        count_positive_int = count_positive_int+1

print(count_positive_int)        

n = 10
sumOfEvenNo = 0

for x in range(1, n+1):
    if x % 2 == 0:
        sumOfEvenNo+=1
print(sumOfEvenNo)    

table = 5
for i in range(1,11):
    if i == 5:
        continue
    print(table, '*' , i , '=' , table * i)

str = 'Python'
reverse_str = ''

for i in str:
    reverse_str = i + reverse_str
print(reverse_str)    


user_string = 'javascript'

for char in user_string:
    if user_string.count(char) == 1:
       print(char)
       break

num = 5
result = 1
i = num
while i > 0:
    result *= i
    i -= 1
print("Factorial of", num, "is", result)

while True:
    userNum = int(input('Enter a num between 1 to 10: '))
    if 1<= userNum <= 10:
        print("Correct Input")
        break
    else:
        print("Invalid Input, try again: ")
       
num = 5
is_prime = True

if num < 2:
    is_prime = False
else:
    for i in range(2, num):
        if (num % i) == 0:
            is_prime = False
            break

print(num, "is a prime number" if is_prime else "is not a prime number")

items = ["apple", "banana", "orange", "apple", "mango"]

unique_item = set()

for item in items:
    if item in unique_item:
        print("Duplicate: ", item)
        break
    unique_item.add(item)


import time

wait_time = 1
max_retries = 5
attempts = 0

while attempts < max_retries:
    print("Attempt", attempts + 1, "- wait time", wait_time)
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1


      