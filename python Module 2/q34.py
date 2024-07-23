#Sort a Dictionary by Value (Ascending and Descending)
my_dict = {'a': 3, 'b': 1, 'c': 2}

# Ascending
sorted_asc = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print(sorted_asc)  # Output: {'b': 1, 'c': 2, 'a': 3}

# Descending
sorted_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print(sorted_desc)  # Output: {'a': 3, 'c': 2, 'b': 1}