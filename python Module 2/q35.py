#Concatenate Dictionaries to Create a New One
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5, 'f': 6}

new_dict = {**dict1, **dict2, **dict3}
print(new_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}