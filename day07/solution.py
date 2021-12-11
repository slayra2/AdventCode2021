input_file = 'day07/input_day07.txt'
#input_file = 'day07/sample_day07.txt'

import numpy as np

# PART I
with open(input_file, 'r') as f:
    lines = f.readlines()

input_crabs = [int(fish) for fish in lines[0].split(',')]

closest = np.median(input_crabs)

fuel = 0
for c in input_crabs:
    fuel = fuel + abs(c-closest)

print(f'The solution is {fuel}')
# 352254

# PART II

input_file = 'day07/input_day07.txt'
#input_file = 'day07/sample_day07.txt'

with open(input_file, 'r') as f:
    lines = f.readlines()

input_crabs = [int(fish) for fish in lines[0].split(',')]

less_fuel = 99119651
for pos in range(min(input_crabs), max(input_crabs)):
    curr_fuel = 0
    for c in input_crabs:
        diff = abs(c-pos)
        calc_weight = (diff*(diff+1))/2
        curr_fuel = curr_fuel + calc_weight
    
    less_fuel = min(curr_fuel, less_fuel)

print(f'The solution is {less_fuel}')

# 99119651 is too high
99053143