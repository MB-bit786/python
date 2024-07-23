#Convert a List of Tuples into a Dictionary
def list_to_dict(tuples_list):
    return dict(tuples_list)

tuples_list = [('a', 1), ('b', 2), ('c', 3)]
print(list_to_dict(tuples_list))  # Output: {'a': 1, 'b': 2, 'c': 3}