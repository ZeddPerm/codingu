import pygame
import time
import jaksle
##import menu
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((900, 900))
pygame.display.set_caption('cdrrdr')
red=255,0,0
blue=0,175,255
green=0,255,0
white=255,255,255
black=0,0,0
yellow=255,255,0
def show_ext(msg,  red):
    fontobj= pygame.font.SysFont("freesans",100)
    msgobj = fontobj.render(msg,False,red)
    screen.blit(msgobj,(75,350))
def show_ooxt(msg,  red):
    fontobj= pygame.font.SysFont("freesans",100)
    msgobj = fontobj.render(msg,False,red)
    screen.blit(msgobj,(575,350))
pygame.draw.rect(screen, blue, (0, 0,450,900), )
pygame.draw.rect(screen, yellow, (450, 0,450,900), )
show_ext('PLAY',yellow)
show_ooxt('QUIT',blue)
pygame.display.update()

def menu():
    pygame.draw.rect(screen, blue, (0, 0,450,900), )
    pygame.draw.rect(screen, yellow, (450, 0,450,900), )
    show_ext('PLAY',yellow)
    show_ooxt('QUIT',blue)
    pygame.display.update() 
    while True:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                print("You pressed the left mouse button at",event.pos)
                x,y=event.pos
                pygame.display.update()
                if x in range (0,450) and y in range (0,900):
                        screen.fill((0,0,0))
                        jaksle.s(x, y)
                        jaksle.ghh(x, y)
                        pygame.draw.rect(screen, blue, (0, 0,450,900), )
                        pygame.draw.rect(screen, yellow, (450, 0,450,900), )
                        show_ext('PLAY',yellow)
                        show_ooxt('QUIT',blue)
                        pygame.display.update()

                if x in range (450,900) and y in range (0,900):
                    exit()
menu()
    

