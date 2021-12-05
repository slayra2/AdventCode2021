input_file = 'day04/input_day04.txt'
#input_file = 'day04/sample_day04.txt'

import numpy as np

# PART I
with open(input_file, 'r') as f:
    lines = f.readlines()

lines = [line.replace('\n', '') for line in lines]

input_bingo = lines[0].split(',')

cards = []
new_card = []
for card in lines[1:]:
    if len(card) > 0:
        new_line = card.split(' ')
        new_card.append([i for i in new_line if i.isdigit()])
    
    else:
        cards.append(new_card)
        new_card = []

# add last Bingo card and remove empty cards
cards.append(new_card)
cards = [card for card in cards if len(card)>0]

# Function to check if it is bingo by row or column
def is_bingo(card, input_list):

    # check for bingo in rows
    for r in card:
        if set(r).issubset(set(input_list)):
            return True

    # check for columns
    card_t = np.array(card).T
    for r in card_t:
        if set(r).issubset(set(input_list)):
            return True
    
    return False

final_numb = ''
list_inputs = []
final_card = []
bingo = False
i = 0

while (not bingo) and (i <= len(input_bingo)+1):

    i = i+1
    curr_bingo = input_bingo[:i]

    for card in cards:
        if is_bingo(card=card, input_list=curr_bingo):
            print(f'Bingo! At i={i} for input {curr_bingo}')
            final_numb = input_bingo[i-1]
            final_card = card
            bingo = True
            

# calculate final solution
card_flat = [numb for sublist in final_card for numb in sublist]
unmarked_numbs = set(card_flat).difference(set(curr_bingo))

sol = int(final_numb)*sum([int(i) for i in unmarked_numbs])
print(f'The solution is {sol}')
#51776


# ---------
# PART II

with open(input_file, 'r') as f:
    lines = f.readlines()

lines = [line.replace('\n', '') for line in lines]

input_bingo = lines[0].split(',')

cards = []
new_card = []
for card in lines[1:]:
    if len(card) > 0:
        new_line = card.split(' ')
        new_card.append([i for i in new_line if i.isdigit()])
    
    else:
        cards.append(new_card)
        new_card = []

# add last Bingo card and remove empty cards
cards.append(new_card)
cards = [card for card in cards if len(card)>0]

# Function to check if it is bingo by row or column
def is_bingo(card, input_list):

    # check for bingo in rows
    for r in card:
        if set(r).issubset(set(input_list)):
            return True

    # check for columns
    card_t = np.array(card).T
    for r in card_t:
        if set(r).issubset(set(input_list)):
            return True
    
    return False

final_numb = ''
final_card = []
last_bingo = [i for i in range(len(cards))]
i = 0

while (len(last_bingo) > 1) and (i <= len(input_bingo)+1):
    i = i+1
    curr_bingo = input_bingo[:i]
    #print(f"There are still {len(last_bingo)} cards in play")

    for card_ind in last_bingo:
        card = cards[card_ind]
        if is_bingo(card=card, input_list=curr_bingo):
            last_bingo.remove(card_ind)

final_card = cards[last_bingo[0]]
#i=85

while not is_bingo(card=final_card, input_list=curr_bingo):
    i = i+1
    curr_bingo = input_bingo[:i]

final_numb = input_bingo[i-1]

# calculate final solution
card_flat = [numb for sublist in final_card for numb in sublist]
unmarked_numbs = set(card_flat).difference(set(curr_bingo))

sol = int(final_numb)*sum([int(i) for i in unmarked_numbs])
print(f'The solution is {sol}')
#16830