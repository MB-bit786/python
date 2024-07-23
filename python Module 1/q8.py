'''''• Write a Python program that will return true if the
two given integervalues are equal or their sum or
difference is 5.'''''

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a == b or abs(a - b) == 5 or abs(a + b) == 5:
    print("True")
else:
    print("False")
    