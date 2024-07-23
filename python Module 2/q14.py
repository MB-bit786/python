#14. Write a Python program to convert a list of characters into a string.
def list_to_string(char_list):
    return ''.join(char_list)

# Example usage
char_list = ['H', 'e', 'l', 'l', 'o']
print(list_to_string(char_list))  # Output: "Hello"