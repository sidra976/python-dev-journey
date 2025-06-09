list = ['mango' , 'apple' , 'peach']
for fruit in list:
    print(fruit)

numbers = [0,-1,2,3,-4,-6,-9]
count_positive_int = 0

for x in numbers:
    if x > 0:
        count_positive_int = count_positive_int+1

print(count_positive_int)        

num = [1,2,3,4,5,6,7,8,9,10]
sumOfEvenNo = 0

for x in num:
    if x > 0 and x % 2 == 0:
        sumOfEvenNo+=x
print(sumOfEvenNo)    