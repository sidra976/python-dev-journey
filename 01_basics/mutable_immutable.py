# Immutable example: integers
x = 10  # x points to the integer object 10
y = x  # y also points to the same integer object 10
print(x)  # output: 10
print(y)  # output: 10

x = 15  # x now points to a new integer object 15, y still points to 10
print(x)  # output: 15
print(y)  # output: 10

# What's happening:
# - Integers are immutable, so when x is reassigned to 15, it doesn't change the original object 10.
# - Instead, x points to a new integer object 15, while y still references the original object 10.
