""" Write a Python program to get the Fibonacci series of given
range."""
num = int(input("Enter the number of terms in the Fibonacci sequence: "))
a, b = 0, 1
print("Fibonacci sequence:")
for _ in range(num):
    print(a, end=" ")
    a, b = b, a + b