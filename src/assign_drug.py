def assign_drug(filename):
    number = int(filename[13:-4])
    result =''
    if number % 2 == 0:
        result = 'placebo'
    else:
        result = 'tylenol'
    return result
assert assign_drug('inflammation_01.dat') == 'tylenol'
assert assign_drug('inflammation_04.dat') == 'placebo'
