#Remove Empty Tuple(s) from a List of Tuples
def remove_empty(tuples_list):
    return [t for t in tuples_list if t]

tuples_list = [(), (1, 2), (), (3, 4, 5), ()]
print(remove_empty(tuples_list))  # Output: [(1, 2), (3, 4, 5)]