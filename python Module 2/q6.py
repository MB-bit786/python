#6. Write a Python function to get the largest number, smallest number, and sum of all from a list.
def list_stats(numbers):
    largest = max(numbers)
    smallest = min(numbers)
    total_sum = sum(numbers)
    return largest, smallest, total_sum

# Example usage
numbers = [2, 33, 222, 14, 25]
largest, smallest, total_sum = list_stats(numbers)
print(f"Largest: {largest}, Smallest: {smallest}, Sum: {total_sum}")
# Output: Largest: 222, Smallest: 2, Sum: 296