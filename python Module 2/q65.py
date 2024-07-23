#Returns Sum of All Divisors of a Number
def sum_of_divisors(n):
    return sum(i for i in range(1, n + 1) if n % i == 0)

# Example usage:
num = 28
print(f"Sum of all divisors of {num}: {sum_of_divisors(num)}")  # Output: 56