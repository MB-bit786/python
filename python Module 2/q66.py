#Find the Maximum and Minimum Numbers from Specified Decimal Numbers
def max_min_numbers(decimal_numbers):
    return max(decimal_numbers), min(decimal_numbers)

# Example usage:
decimal_numbers = [3.4, 5.6, 1.2, 8.9, 2.3]
max_num, min_num = max_min_numbers(decimal_numbers)
print(f"Maximum number: {max_num}")  # Output: 8.9
print(f"Minimum number: {min_num}")  # Output: 1.2