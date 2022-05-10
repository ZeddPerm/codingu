import pygame
import time
import random
from pygame.locals import *
screen=pygame.display.set_mode((900, 900))
pygame.display.set_caption("anniemayshunz")
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
screen.fill((black))
birdx=450
birdy=450
pipx=900
pipy=0
fpsclock = pygame.time.Clock()
height=random.randint(50,650)
pipex=600
pipey=600
pygame.display.update()
pipxl=1
pipexl=1
ychange=1
xstart=-500
ystart=100
feuigtu=0
selttiks=0
oof=270
index=0
k=xstart+300
lp=0
shoot=0
while True:
    pygame.display.update() 
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_b:
                screen.fill((black))
            if event.key == K_w:
                screen.fill((white))
            
        
    
