import pygame
import time
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((900, 900))
pygame.display.set_caption('cdrrdr')
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
pygame.draw.line(screen, (255, 255, 255), (300, 0), (300, 900), )
pygame.draw.line(screen, (255, 255, 255), (00, 600), (900, 600), )
pygame.draw.line(screen, (255, 255, 255), (0, 300), (900, 300), )
pygame.draw.line(screen, (255, 255, 255), (600, 0), (600, 900), )
player = 'x'
blue=0,175,255
red=255,0,0
points=[]
flag=True
while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print("You pressed the left mouse button at",event.pos)
            a,b=event.pos
            print(a,b)
            x=a//300*300
            y=b//300*300
            pt=[x,y] in points
            if flag == True and pt == False:
                print(x,y)
                pygame.draw.circle(screen,blue,(x+150,y+150),(100),1)
                points.append([x,y])
                flag=False
                print(points)
            elif flag == False and pt == False:
                print(x,y)
                pygame.draw.line(screen, red, (x+10, y+10), (x+290, y+290),1)
                pygame.draw.line(screen, red, (x+290, y+10), (x+10, y+290),1)
                points.append([x,y])
                flag=True
                print(points)
                
     
                
            

