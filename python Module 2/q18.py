#18. Write a Python program to check whether a list contains a sublist.
def contains_sublist(lst, sublist):
    sublist_len = len(sublist)
    return any(sublist == lst[i:i+sublist_len] for i in range(len(lst) - sublist_len + 1))

# Example usage
lst = [1, 2, 3, 4, 5]
sublist = [3, 4]
print(contains_sublist(lst, sublist))  # Output: True