import pygame
import time
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((900, 900))
pygame.display.set_caption('cdrrdr')
def s(x,y):
    pygame.draw.line(screen, (255, 255, 255), (300, 0), (300, 900), )
    pygame.draw.line(screen, (255, 255, 255), (00, 600), (900, 600), )
    pygame.draw.line(screen, (255, 255, 255), (0, 300), (900, 300), )
    pygame.draw.line(screen, (255, 255, 255), (600, 0), (600, 900), )
s(1,1)
def show_text(msg,  red):
    fontobj= pygame.font.SysFont("freesans",200)
    msgobj = fontobj.render(msg,False,red)
    screen.blit(msgobj,(150,350))
    
def show_tooxt(msg,  red):
    fontobj= pygame.font.SysFont("freesans",200)
    msgobj = fontobj.render(msg,False,red)
    screen.blit(msgobj,(150,350))
    
def hehe(msg,  red):
    fontobj= pygame.font.SysFont("freesans",200)
    msgobj = fontobj.render(msg,False,red)
    screen.blit(msgobj,(275,350))
diji={1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' '}
player = ''
    
def drawX(x,y):
    global diji
    if x in range(0, 300) and y in range(0, 300):
        q=1
        if diji[1]==' ':  
            diji[q]='x'
            pygame.draw.line(screen, (255, 255, 255), (0, 0), (300, 300), )
            pygame.draw.line(screen, (255, 255, 255), (300, 0), (0, 300), )
            pygame.display.update()
            return 'o'
    if x in range(300, 600) and y in range(0, 300):
        q=2
        if diji[2]==' ':
            diji[q]='x'
            pygame.draw.line(screen, (255, 255, 255), (300, 0), (600, 300), )
            pygame.draw.line(screen, (255, 255, 255), (600, 0), (300, 300), )
            pygame.display.update()
            return 'o'
    if x in range(600, 900) and y in range(0, 300):
        q=3
        if diji[3]==' ': 
            diji[q]='x'
            pygame.draw.line(screen, (255, 255, 255), (600, 0), (900, 300), )
            pygame.draw.line(screen, (255, 255, 255), (900, 0), (600, 300), )
            pygame.display.update()
            return 'o'
    if x in range(0, 300) and y in range(300, 600):
        q=4
        if diji[4]==' ': 
            diji[q]='x'
            pygame.draw.line(screen, (255, 255, 255), (0, 300), (300, 600), )
            pygame.draw.line(screen, (255, 255, 255), (300, 300), (0, 600), )
            pygame.display.update()
            return 'o'
    if x in range(300, 600) and y in range(300, 600):
        q=5
        if diji[5]==' ': 
            diji[q]='x'
            pygame.draw.line(screen, (255, 255, 255), (300, 300), (600, 600), )
            pygame.draw.line(screen, (255, 255, 255), (600, 300), (300, 600), )
            pygame.display.update()
            return 'o'
    if x in range(600, 900) and y in range(300, 600):
        q=6
        if diji[6]==' ': 
            diji[q]='x'
            pygame.draw.line(screen, (255, 255, 255), (600, 300), (900, 600), )
            pygame.draw.line(screen, (255, 255, 255), (900, 300), (600, 600), )
            pygame.display.update()
            return 'o'
    if x in range(0, 300) and y in range(600, 900):
        q=7
        if diji[7]==' ': 
            diji[q]='x'
            pygame.draw.line(screen, (255, 255, 255), (0, 600), (300, 900), )
            pygame.draw.line(screen, (255, 255, 255), (300, 600), (0, 900), )
            pygame.display.update()
            return 'o'
    if x in range(300, 600) and y in range(600, 900):
        q=8
        if diji[8]==' ': 
            diji[q]='x'
            pygame.draw.line(screen, (255, 255, 255), (300, 600), (600, 900), )
            pygame.draw.line(screen, (255, 255, 255), (600, 600), (300, 900), )
            pygame.display.update()
            return 'o'
    if x in range(600, 900) and y in range(600, 900):
        q=9
        if diji[9]==' ': 
            diji[q]='x'
            pygame.draw.line(screen, (255, 255, 255), (600, 600), (900, 900), )
            pygame.draw.line(screen, (255, 255, 255), (900, 600), (600, 900), )
            pygame.display.update()
            return 'o'
    return 'x'

def drawO(x,y):
    global diji
    
    if x in range(0, 300) and y in range(0, 300):
        q=1
        if diji[1] == ' ':
            diji[q]='o'
            pygame.draw.circle(screen, (255, 255, 255), (150, 150), 150, 1)
            pygame.display.update()
            return 'x'
    if x in range(300, 600) and y in range(0, 300):
        q=2
        if diji[2]==' ': 
            diji[q]='o'
            pygame.draw.circle(screen, (255, 255, 255), (450, 150), 150, 1)
            pygame.display.update()
            return 'x'
    if x in range(600, 900) and y in range(0, 300):
        q=3
        if diji[3]==' ': 
            diji[q]='o'
            pygame.draw.circle(screen, (255, 255, 255), (750, 150), 150, 1)
            pygame.display.update()
            return 'x'
    if x in range(0, 300) and y in range(300, 600):
        q=4
        if diji[4]==' ': 
            diji[q]='o'
            pygame.draw.circle(screen, (255, 255, 255), (150, 450), 150, 1)
            pygame.display.update()
            return 'x'
    if x in range(300, 600) and y in range(300, 600):
        q=5
        if diji[5]==' ': 
            diji[q]='o'
            pygame.draw.circle(screen, (255, 255, 255), (450, 450), 150, 1)
            pygame.display.update()
            return 'x'
    if x in range(600, 900) and y in range(300, 600):
        q=6
        if diji[6]==' ': 
            diji[q]='o'
            pygame.draw.circle(screen, (255, 255, 255), (750, 450), 150, 1)
            pygame.display.update()
            return 'x'
    if x in range(0, 300) and y in range(600, 900):
        q=7
        if diji[7]==' ': 
            diji[q]='o'
            pygame.draw.circle(screen, (255, 255, 255), (150, 750), 150, 1)
            pygame.display.update()
            return 'x'
    if x in range(300, 600) and y in range(600, 900):
        q=8
        if diji[8]==' ': 
            diji[q]='o'
            pygame.draw.circle(screen, (255, 255, 255), (450, 750), 150, 1)
            pygame.display.update()
            return 'x'
    if x in range(600, 900) and y in range(600, 900):
        q=9
        if diji[9]==' ': 
            diji[q]='o'
            pygame.draw.circle(screen, (255, 255, 255), (750, 750), 150, 1)
            pygame.display.update()
            return 'x'
    return 'o'
player=input('Do you want to be x or o: ')
while player!='x' and player != 'o':
    print('error type in again')
    player=input('Do you want to be x or o: ')
red=255,0,0
blue=0,175,255
green=0,255,0
while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print("You pressed the left mouse button at",event.pos)
            x,y=event.pos
            
            if player == 'x':
                pygame.display.update()
                player = drawX(x,y)
                print(diji)
                print("Player's Turn: ", player)
            elif player == 'o':
                pygame.display.update()
                player = drawO(x,y)
                print(diji)
                print("Player's Turn: ", player)
            else:
                print ("Error")
                break
            if diji[1]=='x' and diji[2]=='x' and diji[3]=='x':
                show_text('X Wins!', red)
                pygame.display.update()
                time.sleep(1.5)
                # import h
                diji={1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' '}
                # h.menu()
            elif diji[1]=='o' and diji[2]=='o' and diji[3]=='o':
                show_tooxt('O Wins!', blue)
                pygame.display.update()
                time.sleep(1.5)
                # import h
                diji={1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' '}
                # h.menu()
            if diji[4]=='x' and diji[5]=='x' and diji[6]=='x':
                show_text('X Wins!', red)
                pygame.display.update()
                time.sleep(1.5)
                # import h
                diji={1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' '}
                # h.menu()
            elif diji[4]=='o' and diji[5]=='o' and diji[6]=='o':
                show_tooxt('O Wins!', blue)
                pygame.display.update()
                time.sleep(1.5)
                # import h
                diji={1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' '}
                # h.menu()
            if diji[7]=='x' and diji[8]=='x' and diji[9]=='x':
                show_text('X Wins!', red)
                pygame.display.update()
                time.sleep(1.5)
                # import h
                diji={1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' '}
                # h.menu()
            elif diji[7]=='o' and diji[8]=='o' and diji[9]=='o':
                show_tooxt('O Wins!', blue)
                pygame.display.update()
                time.sleep(1.5)
                # import h
                diji={1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' '}
                # h.menu()
            if diji[1]=='x' and diji[5]=='x' and diji[9]=='x':
                show_text('X Wins!', red)
                pygame.display.update()
                time.sleep(1.5)
                # import h
                diji={1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' '}
                # h.menu()
            elif diji[1]=='o' and diji[5]=='o' and diji[9]=='o':
                show_tooxt('O Wins!', blue)
                pygame.display.update()
                time.sleep(1.5)
                # import h
                diji={1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' '}
                # h.menu()
            if diji[1]=='x' and diji[4]=='x' and diji[7]=='x':
                show_text('X Wins!', red)
                pygame.display.update()
                time.sleep(1.5)
                # import h
                diji={1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' '}
                # h.menu()
            elif diji[1]=='o' and diji[4]=='o' and diji[7]=='o':
                show_tooxt('O Wins!', blue)
                pygame.display.update()
                time.sleep(1.5)
                # import h
                diji={1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' '}
                # h.menu()
            if diji[2]=='x' and diji[5]=='x' and diji[8]=='x':
                show_text('X Wins!', red)
                pygame.display.update()
                time.sleep(1.5)
                # import h
                diji={1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' '}
                # h.menu()
            elif diji[2]=='o' and diji[5]=='o' and diji[8]=='o':
                show_tooxt('O Wins!', blue)
                pygame.display.update()
                time.sleep(1.5)
                # import h
                diji={1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' '}
                # h.menu()
            if diji[3]=='x' and diji[6]=='x' and diji[9]=='x':
                show_text('X Wins!', red)
                pygame.display.update()
                time.sleep(1.5)
                # import h
                diji={1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' '}
                # h.menu()
            elif diji[3]=='o' and diji[6]=='o' and diji[9]=='o':
                show_tooxt('O Wins!', blue)
                pygame.display.update()
                time.sleep(1.5)
                # import h
                diji={1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' '}
                # h.menu()
            if diji[3]=='x' and diji[5]=='x' and diji[7]=='x':
                show_text('X Wins!', red)
                pygame.display.update()
                time.sleep(1.5)
                # import h
                diji={1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' '}
                # h.menu()
            elif diji[3]=='o' and diji[5]=='o' and diji[7]=='o':
                show_tooxt('O Wins!', blue)
                pygame.display.update()
                time.sleep(1.5)
                # import h
                diji={1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' '}
                # h.menu()
            if ' ' not in diji.values():
                    hehe('Tie!', green)
                    pygame.display.update()
                    time.sleep(1.5)
                    # import h
                    diji={1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' '}
                    # h.menu()
                
        
