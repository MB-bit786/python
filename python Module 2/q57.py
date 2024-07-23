#Pattern Matching in Python
'''Pattern matching in Python can be performed using 
regular expressions with the re module.'''

import re    

def match_pattern(pattern, string):
    if re.match(pattern, string):
        return True
    return False

print(match_pattern(r'^a...s$', 'abyss'))  # Output: True
print(match_pattern(r'^a...s$', 'abacus'))  # Output: False