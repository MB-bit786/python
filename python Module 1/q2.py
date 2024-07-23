#Write a Python program to get the Factorial number of given number
number = int(input("Enter a number to find its factorial: "))
result = 1
for i in range(1, number + 1):
    result *= i
print(f"Factorial of {number} is: {result}")
number