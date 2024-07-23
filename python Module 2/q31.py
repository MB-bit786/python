#Unzip a List of Tuples into Individual Lists

def unzip(tuples_list):
    return list(zip(*tuples_list))

tuples_list = [(1, 'a'), (2, 'b'), (3, 'c')]
print(unzip(tuples_list))  # Output: [(1, 2, 3), ('a', 'b', 'c')]