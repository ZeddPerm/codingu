import itertools
import copy
import numpy as np
import time
import random
gamestate = [['','',''],
            ['','',''],
            ['','','']]
players = ['x','o']
states = ['','x','o']

all_gamestate = itertools.product(states, repeat=9)
all_gamestates = []

aiX = []
aiO = []

epsilon = 0.3

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
    print('not done')
    return 'not done'
# print('a',resultOfGame([['', '', 'x'], ['', '', 'x'], ['', 'x', '']]))
def bestPossibleMove(gs,cur_player):
    global epsilon
    open_spaces = []
    possible_values = []
    for i in range(len(gs)):
        for j in range(len(gs[i])):
            if gs[i][j] == '':
                temp_gs = copy.deepcopy(gs)
                temp_gs[i][j] = cur_player
                open_spaces.append([i,j])
                # print(temp_gs)
                # print(gs)
                if temp_gs in all_gamestates:
                    if cur_player == 'x':
                        possible_values.append(aiX[all_gamestates.index(temp_gs)])
                    elif cur_player == 'o':
                        possible_values.append(aiO[all_gamestates.index(temp_gs)])
    # print(open_spaces,possible_values)
    v = random.random()
    if v > epsilon:
        return open_spaces[np.argmax(possible_values)]
    else:
        epsilon -= 0.01
        return open_spaces[random.randint(0,len(open_spaces)-1)]
    # return open_spaces

for i in all_gamestate:
    i = [list(i[0:3]),list(i[3:6]),list(i[6:9])]
    all_gamestates.append(i)
    result = resultOfGame(i)
    if result == 'x':
        aiX.append(1)
        aiO.append(-1)
    elif result == 'o':
        aiO.append(1)
        aiX.append(-1)
    else:
        aiO.append(0)
        aiX.append(0)
value_of_gamestate = {}

# print('ag',len(all_gamestates))
# print('x',len(aiX))
# print('o',len(aiO))
# print(bestPossibleMove([['x','','o'],
#                         ['o','',''],
#                         ['x','o','o']], 'o'))
results = 0
player = players[random.randint(0,1)]
while results != 10:
    move = bestPossibleMove(gamestate,player)
    gamestate[move[0]][move[1]] = player
    results += 1
    print(resultOfGame(gamestate))
    if player == 'x':
        player = 'o'
    elif player == 'o':
        player = 'x'
    print('g',gamestate)