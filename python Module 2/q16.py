#16. Write a Python program to find the second smallest number in a list.

def second_smallest(lst):
    unique_lst = list(set(lst))
    unique_lst.sort()
    return unique_lst[1]

# Example usage
lst = [1, 2, 2, 3, 4, 4, 5]
print(second_smallest(lst))  # Output: 2