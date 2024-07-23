#13. Write a Python function that takes a list and returns a new list with unique elements of the first list.
def unique_elements(lst):
    return list(set(lst))

# Example usage
lst = [1, 2, 2, 3, 4, 4, 5]
print(unique_elements(lst))  # Output: [1, 2, 3, 4, 5]