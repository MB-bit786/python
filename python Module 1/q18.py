"""• Write a Python program to get a string made of the first 2
and the last 2 chars from a given a string. If the string length
is less than 2, return instead of the empty string.
o Sample String: w3resource' o
Expected Result: 'w3ce' o
Sample String: 'w3' o Expected
Result:
'w3w3' o Sample String: ' w' o
Expected Result: Empty String"""


string = input("Enter a string: ")
if len(string) < 2:
    print("Empty String")
else:
    print(string[:2] + string[-2:])