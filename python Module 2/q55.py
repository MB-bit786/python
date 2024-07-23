#Check Whether a Number is Perfect or Not
def is_perfect(n):
    return n == sum(i for i in range(1, n) if n % i == 0)

print(is_perfect(6))  # Output: True
print(is_perfect(28))  # Output: True
print(is_perfect(10))  # Output: False