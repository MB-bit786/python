#17. Write a Python program to get unique values from a list.
def unique_values(lst):
    return list(set(lst))

# Example usage
lst = [1, 2, 2, 3, 4, 4, 5]
print(unique_values(lst))  # Output: [1, 2, 3, 4, 5]