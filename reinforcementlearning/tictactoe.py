import itertools
import numpy as np
import time
gamestate = [['','',''],
            ['','',''],
            ['','','']]
players = ['x','o']
states = ['','x','o']

all_gamestate = itertools.product(states, repeat=9)
all_gamestates = []

aiX = []
aiO = []

def resultOfGame(gs):
    if gs[0][0] == gs[0][1] == gs[0][2]:
        return gs[0][0]
    if gs[1][0] == gs[1][1] == gs[1][2]:
        return gs[1][0]
    if gs[2][0] == gs[2][1] == gs[2][2]:
        return gs[2][0]
    if gs[0][0] == gs[1][1] == gs[2][2]:
        return gs[0][0]
    if gs[0][1] == gs[1][1] == gs[2][1]:
        return gs[0][1]
    if gs[0][2] == gs[1][2] == gs[2][2]:
        return gs[0][2]
    if gs[0][2] == gs[1][1] == gs[2][0]:
        return gs[0][2]
    if gs[0][0] == gs[1][0] == gs[2][0]:
        return gs[0][0]
    if '' not in gs[0] and '' not in gs[1] and '' not in gs[2]:
        return 'draw'
print('a',resultOfGame([['', '', 'x'], ['', '', 'x'], ['', 'x', '']]))
def bestPossibleMove(gs,cur_player):
    open_spaces = []
    possible_values = []
    for i in range(len(gs)):
        for j in range(len(gs[i])):
            if gs[i][j] == '':
                gs[i][j] = cur_player
                open_spaces.append([i,j])
                print(gs)
                if cur_player == 'x':
                    # print(type(all_gamestates))
                    # print('a',all_gamestates.index(gs))
                    if gs in all_gamestates:
                        # print(len(aiX))
                        # print(aiX[all_gamestates.index(gs)])
                        possible_values.append(aiX[all_gamestates.index(gs)])
    print(open_spaces,possible_values)
    # return open_spaces

for i in all_gamestate:
    i = [list(i[0:3]),list(i[3:6]),list(i[6:9])]
    all_gamestates.append(i)
    if resultOfGame(i) == 'x':
        # print(i,all_gamestates[all_gamestates.index(i)])
        # time.sleep(1)
        aiX.append(1)
        aiO.append(-1)
    elif resultOfGame(i) == 'o':
        # print(i,all_gamestates[all_gamestates.index(i)])
        # time.sleep(1)
        aiO.append(1)
        aiX.append(-1)
    elif resultOfGame(i) == 'draw' or resultOfGame(i) == '':
        # print(i,all_gamestates[all_gamestates.index(i)])
        # time.sleep(1)
        aiO.append(0)
        aiX.append(0)

value_of_gamestate = {}

# print(all_gamestates)
# print('aegh',all_gamestates.index(aiX[1][1]))
# print('aegh',aiX[1])
# print(list(all_gamestate))
# print(all_gamestates[0])
print(bestPossibleMove([['x','','x'],['x','o','o'],['x','o','x']], 'x'))