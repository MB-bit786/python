#Create a Dictionary from a String
def string_to_dict(s):
    return Counter(s)

sample_string = 'w3resource'
print(string_to_dict(sample_string))
# Output: Counter({'r': 2, 'e': 2, 'w': 1, '3': 1, 's': 1, 'o': 1, 'u': 1, 'c': 1})