# List methods in Python

my_list = [1, 2, 3, 4, 5]

my_list[1:2] = [44] #we replace the no of 2 with 6
print(my_list)

#append(x): Adds an item to the end of the list
my_list.append(6)
print(my_list)

if 44 in my_list:
    print('Found it!')

#remove(x): Removes the first item from the list whose value is equal to x
my_list.remove(3)

# pop([i]): Removes and returns the item at the given position (default last)
my_list.pop()  # Removes last item
my_list.pop(0) # Removes first item    

# insert(i, x): Inserts an item at a given position
my_list.insert(0, "addedd")
print(my_list)

#copy(): Returns a shallow copy of the list
new_list = my_list.copy()

#extend(iterable): Extends the list by appending elements from the iterable
my_list.extend([7, 8])





# 6. clear(): Removes all items from the list
my_list.clear()

# 7. index(x[, start[, end]]): Returns the index of the first item whose value is x
my_list = [1, 2, 3, 2, 4]
idx = my_list.index(2)  # Returns 1

# 8. count(x): Returns the number of times x appears in the list
count_2 = my_list.count(2)  # Returns 2

# 9. sort(key=None, reverse=False): Sorts the list in ascending order
my_list.sort()

# 10. reverse(): Reverses the elements of the list in place
my_list.reverse()



