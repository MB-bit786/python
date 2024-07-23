#Create and Display All Combinations of Letters from Different Keys in a Dictionary
import itertools

def letter_combinations(d):
    keys = sorted(d.keys())
    combinations = itertools.product(*(d[key] for key in keys))
    for combination in combinations:
        print(''.join(combination))

sample_data = {'1': ['a', 'b'], '2': ['c', 'd']}
letter_combinations(sample_data)
