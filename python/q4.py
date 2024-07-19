"""Write python program that swap two number with temp
variable and without temp variable."""
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

print(f"Before swapping: x = {x}, y = {y}")
temp = x
x = y
y = temp

print(f"After swapping with temp variable: x = {x}, y = {y}")