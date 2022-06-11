import numpy as np
import time
import copy
import random
import itertools

def resultOfGame(gs):
    if gs[0][0] == gs[0][1] == gs[0][2] != "":
        return gs[0][0],"done"
    if gs[1][0] == gs[1][1] == gs[1][2] != "":
        return gs[1][0],"done"
    if gs[2][0] == gs[2][1] == gs[2][2] != "":
        return gs[2][0],"done"
    if gs[0][0] == gs[1][1] == gs[2][2] != "":
        return gs[0][0],"done"
    if gs[0][1] == gs[1][1] == gs[2][1] != "":
        return gs[0][1],"done"
    if gs[0][2] == gs[1][2] == gs[2][2] != "":
        return gs[0][2],"done"
    if gs[0][2] == gs[1][1] == gs[2][0] != "":
        return gs[0][2],"done"
    if gs[0][0] == gs[1][0] == gs[2][0] != "":
        return gs[0][0],"done"
    if '' not in gs[0] and '' not in gs[1] and '' not in gs[2]:
        return None,'draw'
    return None,'not done'

def bestPossibleMove(gs,cur_player):
    open_spaces = []
    possible_values = []
    print(all_gamestates.index(gs),gs)
    for i in range(len(gs)):
        for j in range(len(gs[i])):
            if gs[i][j] == '':
                temp_gs = copy.deepcopy(gs)
                temp_gs[i][j] = cur_player
                open_spaces.append([i,j])
                # print(temp_gs)
                # print(gs)
                if temp_gs in all_gamestates:
                    # if cur_player == 'x':
                        # possible_values.append(aiX[all_gamestates.index(temp_gs)])
                    if cur_player == 'o':
                        possible_values.append(aiO[all_gamestates.index(temp_gs)])
                        print(all_gamestates.index(temp_gs),temp_gs,aiO[all_gamestates.index(temp_gs)])
    print(possible_values,open_spaces[np.argmax(possible_values)])
    return open_spaces[np.argmax(possible_values)]
    # return open_spaces

states = ['','x','o']
all_gamestate = itertools.product(states, repeat=9)
all_gamestates = []
for i in all_gamestate:
    i = [list(i[0:3]),list(i[3:6]),list(i[6:9])]
    all_gamestates.append(i)

aiO = np.loadtxt("aiO.txt", dtype=np.float64)
gamestate = [['','',''],
            ['','',''],
            ['','','']]
_,result = resultOfGame(gamestate)
players = ['x','o']
# player = players[random.randint(0,1)]
player = 'x'

while result == 'not done':
    print(gamestate[0])
    print(gamestate[1])
    print(gamestate[2])
    if player == 'x':
        x_coord = int(input("Choose the X coordinate for your shape: "))
        y_coord = int(input("Choose the Y coordinate for your shape: "))
        if gamestate[y_coord][x_coord] == '':
            gamestate[y_coord][x_coord] = player
            _,result = resultOfGame(gamestate)
            player = 'o'
    elif player == 'o':
        best_o_move = bestPossibleMove(gamestate,'o')
        gamestate[best_o_move[0]][best_o_move[1]] = player
        _,result = resultOfGame(gamestate)
        player = 'x'
