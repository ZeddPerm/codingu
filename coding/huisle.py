import pygame
import time
import random
from pygame.locals import *
screen=pygame.display.set_mode((900, 900))
pygame.display.set_caption("FLAPPLYBIRD")
pygame.init()
red=(255,0,0)
green=(0,255,0)
blue=(0,175,255)
skyblue=(0,0,)
white=(255,255,255)
black=(0,0,0)
yellow=(255,255,0)
das=(175,174,0)
orange=(255,165,0)
screen.fill((white))
birdx=450
birdy=450
pipx=900
pipy=0
height=random.randint(50,650)
pipex=600
pipey=600
pygame.display.update()
pipxl=1
pipexl=1
ychange=1
def show_text(msg,x,y,red):
    fontobj= pygame.font.SysFont("freesans",32)
    msgobj = fontobj.render(msg,False,red)
    screen.blit(msgobj,(x,y))
def show_txt(msg,x,y,red):
    fontobj= pygame.font.SysFont("freesans",32)
    msgobj = fontobj.render(msg,False,red)
    screen.blit(msgobj,(x,y))
while True:
    pygame.display.update()
    screen.fill((white))
    pygame.draw.circle(screen,yellow,(birdx,birdy),(30), )
    pygame.draw.rect(screen, green, (pipx, 0, 100, height), )
    pygame.draw.rect(screen, green, (pipx, height+200, 100, 900), )
    pygame.draw.circle(screen,black,(birdx+15,birdy-7),(4), )
    pygame.draw.rect(screen, orange, (birdx+15,birdy, 20, 5), )
    #pygame.draw.circle(screen, das, (birdx-15
    show_text (str(pipy),425,35,red)
    pipx=pipx-1
    if pipx==0:
        height=random.randint(50,650)
        pipx=800
    if birdx+30==pipx and birdy not in range(height, height+200):
        show_txt ("You lose!",405,100,blue)
        pygame.display.update()
        break
    if (birdy-30< height or birdy+30 > height + 200) and birdx in range(pipx, pipx+100):
        show_txt ("You lose!",405,100,blue)
        pygame.display.update()
        break
    elif birdx-100==pipx and birdy in range(height, height+200):        
        pipy=pipy+1
        pygame.display.update()
    if pipy==10:
        show_txt ("You win!",405,100,blue)
        pygame.display.update()
        break
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYUP:
            if event.key == K_SPACE:
                ychange=2
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                ychange=-2
        
        


    birdy=birdy+ychange
    if birdy-30==0:
        ychange=0
        show_txt ("You lose!",405,100,blue)
        pygame.display.update()
        break
    if birdy+30==900:
        ychange=0
        show_txt ("You lose!",405,100,blue)
        pygame.display.update()
        break
        




