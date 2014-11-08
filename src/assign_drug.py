def assign_drug(filename):
    '''Assigns a drug to a filename'''
    number = int(filename[-6:-4])
    result =''
    if number % 2 == 0:
        result = 'placebo'
    else:
        result = 'tylenol'
    return result

import sys

filename = sys.argv[1]
print assign_drug(filename)

assert assign_drug('inflammation_01.dat') == 'tylenol'
assert assign_drug('inflammation_04.dat') == 'placebo'

