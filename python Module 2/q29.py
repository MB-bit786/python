#Find the Repeated Items of a Tuple
def find_repeats(tup):
    return [item for item in set(tup) if tup.count(item) > 1]

my_tuple = (1, 2, 2, 3, 3, 3, 4, 5)
print(find_repeats(my_tuple))  # Output: [2, 3]