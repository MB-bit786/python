#Read a Random Line from a File

import random

def random_line(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return random.choice(lines)

print(random_line('sample.txt'))