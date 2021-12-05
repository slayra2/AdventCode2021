input_file = 'day05/input_day05.txt'
#input_file = 'day05/sample_day05.txt'

from collections import Counter
import re

# PART I
with open(input_file, 'r') as f:
    lines = f.readlines()

lines = [line.replace('\n', '') for line in lines]

# create the list of points from input
curr_list = []
for line in lines:
    digits = re.findall(r'\d+', line)
    
    # horizontal increase
    if digits[1]==digits[3]:
        fixed = int(digits[1])
        start = min(int(digits[0]), int(digits[2]))
        end = max(int(digits[0]), int(digits[2]))

        for i in range(start, end+1):
            curr_list.append((i, fixed))

    #vertical increase
    elif digits[0]==digits[2]:
        fixed = int(digits[0])
        start = min(int(digits[1]), int(digits[3]))
        end = max(int(digits[1]), int(digits[3]))

        for i in range(start, end+1):
            curr_list.append((fixed, i))

count_values = Counter(curr_list)
sol = sum(1 for item in count_values.values() if item > 1)

print(f'The solution is {sol}')
#6007


# ---------
# PART II

input_file = 'day05/input_day05.txt'
#input_file = 'day05/sample_day05.txt'

# PART I
with open(input_file, 'r') as f:
    lines = f.readlines()

lines = [line.replace('\n', '') for line in lines]

# create the list of points from input
curr_list = []
for line in lines:
    digits = re.findall(r'\d+', line)
    
    # horizontal increase
    if digits[1]==digits[3]:
        fixed = int(digits[1])
        start = min(int(digits[0]), int(digits[2]))
        end = max(int(digits[0]), int(digits[2]))

        for i in range(start, end+1):
            curr_list.append((i, fixed))

    #vertical increase
    elif digits[0]==digits[2]:
        fixed = int(digits[0])
        start = min(int(digits[1]), int(digits[3]))
        end = max(int(digits[1]), int(digits[3]))

        for i in range(start, end+1):
            curr_list.append((fixed, i))
    
    # diagonal increase (45 degrees)
    else:
        startx = min(int(digits[0]), int(digits[2]))
        endx = max(int(digits[0]), int(digits[2]))
        
        # x,y both increase or x,y both decrease
        if ((int(digits[0]) < int(digits[2])) and (int(digits[1]) < int(digits[3]))) or \
            ((int(digits[0]) > int(digits[2])) and (int(digits[1]) > int(digits[3]))):
            starty = min(int(digits[1]), int(digits[3]))
            for i in range(startx, endx+1):
                curr_list.append((i, starty))
                starty = starty+1
        
        # x decreases while y increases or vice-versa
        else:
            starty = max(int(digits[1]), int(digits[3]))
            for i in range(startx, endx+1):
                curr_list.append((i, starty))
                starty = starty-1

count_values = Counter(curr_list)
sol = sum(1 for item in count_values.values() if item > 1)
print(f'The solution is {sol}')
#19349