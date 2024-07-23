#Combine Values in Python List of Dictionaries

from collections import Counter

def combine_values(dicts):
    combined = Counter()
    for d in dicts:
        combined[d['item']] += d['amount']
    return combined

sample_data = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
print(combine_values(sample_data))  # Output: Counter({'item1': 1150, 'item2': 300})