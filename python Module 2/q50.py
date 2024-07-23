#Find the Highest 3 Values in a Dictionary
def highest_3_values(d):
    return sorted(d.values(), reverse=True)[:3]

sample_dict = {'a': 50, 'b': 100, 'c': 200, 'd': 150}
print(highest_3_values(sample_dict))  # Output: [200, 150, 100]