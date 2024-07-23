#12. Write a Python program to generate and print a list of first and last 5 elements where the values are squares of numbers between 1 and 30.
def squares_list():
    squares = [i**2 for i in range(1, 31)]
    return squares[:5] + squares[-5:]

# Example usage
print(squares_list())  # Output: [1, 4, 9, 16, 25, 676, 729, 784, 841, 900]