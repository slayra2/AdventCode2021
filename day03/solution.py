input_file = 'day03/input_day03.txt'
#input_file = 'day03/sample_day03.txt'

from collections import Counter
import pandas as pd

# PART I
with open(input_file, 'r') as f:
    lines = f.readlines()

lines = [line.replace('\n', '') for line in lines]

df = pd.DataFrame(lines)
df = df[0].str.split(pat='', expand=True)
df = df.drop([0, len(df.columns)-1], axis=1)

diag_dict = {'gamma': '', 'epsilon': ''}

for col in df.columns:
    counter_dict = Counter(df[col])
    diag_dict['gamma'] = diag_dict['gamma'] + counter_dict.most_common(1)[0][0]
    diag_dict['epsilon'] = diag_dict['epsilon'] + counter_dict.most_common(2)[1][0]


sol = int(diag_dict['gamma'], 2) * int(diag_dict['epsilon'], 2)
print(f'The solution is {sol}')
#2640986

# ---------
# PART II

with open(input_file, 'r') as f:
    lines = f.readlines()

lines = [line.replace('\n', '') for line in lines]

df = pd.DataFrame(lines)
df = df[0].str.split(pat='', expand=True)
df = df.drop([0, len(df.columns)-1], axis=1)

diag_dict = {'oxygen': '', 'co2': ''}

df_ox = df.copy()
df_co = df.copy()

for col in df.columns:

    if len(df_ox) > 1:
        counter_dict = Counter(df_ox[col])
        diff = list(counter_dict.values())[0] != list(counter_dict.values())[1]

        if diff:
            most_common = counter_dict.most_common(1)[0][0]
        else:
            most_common = '1'
        df_ox = df_ox[df_ox[col]==most_common]
    
    if len(df_co) > 2:
        counter_dict = Counter(df_co[col])
        diff = list(counter_dict.values())[0] != list(counter_dict.values())[1]
        if diff:
            least_common = counter_dict.most_common(2)[1][0]
        else:
            least_common = '0'
        df_co = df_co[df_co[col]==least_common]

ox_bin = [''.join(i) for i in df_ox.values][0]
diag_dict['oxygen'] = ox_bin

co_bin = [''.join(i) for i in df_co.values][0]
diag_dict['co2'] = co_bin

sol = int(diag_dict['oxygen'], 2) * int(diag_dict['co2'], 2)
print(f'The solution is {sol}')
#6822109