#Replace Last Value of Tuples in a List
def replace_last(tuples_list, new_value):
    return [t[:-1] + (new_value,) for t in tuples_list]

tuples_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
print(replace_last(tuples_list, 100))  # Output: [(1, 2, 100), (4, 5, 100), (7, 8, 100)]