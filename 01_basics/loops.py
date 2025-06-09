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
   
      