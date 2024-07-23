#11. Write a Python function that takes two lists and returns true if they have at least one common member
def common_member(lst1, lst2):
    return bool(set(lst1) & set(lst2))

# Example usage
lst1 = [1, 2, 3]
lst2 = [3, 4, 5]
print(common_member(lst1, lst2))  # Output: True