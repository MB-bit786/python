"""• Write a Python program to get a single string from two
given strings, separated by a space and swap the first two
characters of each string."""


string1 = input("Enter first string: ")
string2 = input("Enter second string: ")
new_string = string2[:2] + string1[2:] + " " + string1[:2] + string2[2:]
print(new_string)
