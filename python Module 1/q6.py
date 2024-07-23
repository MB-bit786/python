'''''• Write a Python program to test whether a passed letter is a
vowel or not.'''''

letter = input("Enter a letter: ")
vowels = ["a", "e", "i", "o", "u"]

if letter in vowels:
    print(f"{letter} is a vowel.")
else:
    print(f"{letter} is not a vowel.")


