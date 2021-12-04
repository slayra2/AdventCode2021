input_file = 'day01/input_day01.txt'

import pandas as pd

# PART I
df = pd.read_csv(input_file, header=None)

df['prev'] = df[0].shift()
df['larger'] = (df[0] > df['prev'])*1

numb_increases = df['larger'].sum()
print(f"Number of increases is {numb_increases}")
#1162

# ---------
# PART II

df = pd.read_csv(input_file, header=None)
df['prev1'] = df[0].shift()
df['prev2'] = df[0].shift(2)
df['sum_3'] = df[0] + df['prev1'] + df['prev2']
df = df[2:]

df['sum_3_prev'] = df['sum_3'].shift()
df['larger'] = (df['sum_3'] > df['sum_3_prev'])*1

numb_increases = df['larger'].sum()
print(f"Number of increases is {numb_increases}")
#1190


