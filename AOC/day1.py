import numpy as np

input_data = np.loadtxt('inputs/input1.txt')
current_freq = 0
doubled_freq = 0
freqs = []
is_found = False

for freq in input_data:

    freqs.append(current_freq)
    current_freq += freq

    if current_freq in freqs and not is_found:
        doubled_freq = current_freq
        is_found = True

print('Final frequency: {}'.format(current_freq))
print('{} occurred twice as first'.format(doubled_freq))
