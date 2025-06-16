# from collections import Counter

# animals = ['cat', 'dog', 'cat']
# frequency = Counter(animals)

# print(frequency)

#problem 1
animals = ['cat', 'dog', 'cat']
frequency = {}
for animal in animals:
    if animal in frequency:
     frequency[animal]+=1
    else:
       frequency[animal]=1
print(frequency)

#problem 2
word = "butterfly"
vowel_counter = {}

for i in word:
    if i in 'aeiou':
        if i in vowel_counter:
            vowel_counter[i] += 1
        else:
            vowel_counter[i] = 1

print(vowel_counter)

#problem 3
num = 112223
digit_counter = {}

for i in str(num):
   if i in digit_counter:
      digit_counter[i] +=1
   else:
      digit_counter[i] =1

print(digit_counter)

#problem 4
sentence = "hello world"

letter_counter = {}
for i in sentence:
   if i == " ":
      continue
   if i in letter_counter:
      letter_counter[i] +=1
   else:
      letter_counter[i] = 1

print(letter_counter)      
   
