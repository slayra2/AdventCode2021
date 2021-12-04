input_file = 'day02/input_day02.txt'

import re

# PART I
with open(input_file, 'r') as f:
    lines = f.readlines()

dir_dict = {'forward': 0, 'depth': 0}

for line in lines:
    step = re.search(r'\d+', line).group(0)
    
    if 'forward' in line:
        dir_dict['forward'] = dir_dict['forward'] + int(step)
    
    elif 'up' in line:
        dir_dict['depth'] = dir_dict['depth'] - int(step)
    
    else:
        dir_dict['depth'] = dir_dict['depth'] + int(step)

sol = dir_dict['forward'] * dir_dict['depth']
print(f'The multiplied depth by forward is {sol}')


# ---------
# PART II

with open(input_file, 'r') as f:
    lines = f.readlines()

dir_dict = {'forward': 0, 'depth': 0, 'aim': 0}

for line in lines:
    step = re.search(r'\d+', line).group(0)
    
    if 'forward' in line:
        dir_dict['forward'] = dir_dict['forward'] + int(step)
        dir_dict['depth'] = dir_dict['depth'] + dir_dict['aim']*int(step)
    
    elif 'up' in line:
        dir_dict['aim'] = dir_dict['aim'] - int(step)
    
    else:
        dir_dict['aim'] = dir_dict['aim'] + int(step)

sol = dir_dict['forward'] * dir_dict['depth']
print(f'The multiplied depth by forward is {sol}')


