#Check Whether a Number is in a Given Range
def is_in_range(n, start, end):
    return start <= n <= end

print(is_in_range(5, 1, 10))  # Output: True
print(is_in_range(11, 1, 10))  # Output: False