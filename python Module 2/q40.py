#Check if Multiple Keys Exist in a Dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
keys = {'a', 'b'}
print(keys.issubset(my_dict.keys()))  # Output: True