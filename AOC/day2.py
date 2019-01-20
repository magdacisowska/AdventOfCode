import numpy as np
import pandas as pd

boxes = open('inputs/input2.txt').read().splitlines()
twos, threes = 0, 0
is_two, is_three = False, False

for box_code in boxes:

    for letter in box_code:
        occurrences = box_code.count(letter)
        if occurrences == 2 and not is_two:
            twos += 1
            is_two = True
        if occurrences == 3 and not is_three:
            threes += 1
            is_three = True

    is_two = False
    is_three = False

print('two letters occurrences: in {} codes, three letters occurrences: in {} codes'.format(twos, threes))
