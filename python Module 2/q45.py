#Print All Unique Values in a Dictionary
def unique_values(d):
    unique_vals = set(d.values())
    print(unique_vals)

sample_dict = {'a': 1, 'b': 2, 'c': 2, 'd': 3}
unique_values(sample_dict)  # Output: {1, 2, 3}