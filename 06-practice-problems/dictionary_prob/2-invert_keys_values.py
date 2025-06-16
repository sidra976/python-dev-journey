values = {'a': 1, 'b': 2}
inverted = {}
for key in values:
    val = values[key]
    inverted[val] = key

print(inverted)

#another way 
# new_dict = {new_key: new_value for key, value in old_dict.items()}
inverted_dic = {k:v for k , v in values.items()}
print(inverted_dic)

words = {'a': 1, 'b': 2}
upper_keys = {k.upper(): v for k, v in words.items()}
# ➝ {'A': 1, 'B': 2}




