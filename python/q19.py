#• Write a Python function to insert a string in the middle of a string.

string = input("Enter a string: ")
sub_string = input("Enter a sub-string: ")
middle_index = int(len(string) / 2)
new_string = string[:middle_index] + sub_string + string[middle_index:]
print(new_string)