#Convert a Tuple to a String
def tuple_to_string(tup):
    return ''.join(map(str, tup))

my_tuple = ('a', 'b', 'c')
print(tuple_to_string(my_tuple))  # Output: "abc"