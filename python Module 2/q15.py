#15. Write a Python program to select an item randomly from a list.
import random

def random_item(lst):
    return random.choice(lst)

# Example usage
lst = [1, 2, 3, 4, 5]
print(random_item(lst))  # Output: Random item from the list
