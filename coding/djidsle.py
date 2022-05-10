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
pipx=2
pipy=0
fpsClock = pygame.time.Clock()
height=random.randint(50,650)
pipex=600
pipey=600
pygame.display.update()
pipxl=1
pipexl=1
ychange=1
xstart=-500
ystart=200
feuigtu=0
selttiks=0
oof=370
index=0
k=xstart+125
lp=0
shoot=0
qwerty=-10
e=1
crouchvar=1
s =1
def show_text(msg,x,y,red):
    fontobj= pygame.font.SysFont("freesans",32)
    msgobj = fontobj.render(msg,False,red)
    screen.blit(msgobj,(x,y))
def show_txt(msg,x,y,red):
    fontobj= pygame.font.SysFont("freesans",32)
    msgobj = fontobj.render(msg,False,red)
    screen.blit(msgobj,(x,y))
bionic=[
pygame.image.load("walk1.png"),
pygame.image.load("walk2.png"),
pygame.image.load("walk3.png"),
pygame.image.load("walk4.png"),
pygame.image.load("walk5.png")]
cinoib=[
pygame.image.load("klaw1.png"),
pygame.image.load("klaw2.png"),
pygame.image.load("klaw3.png"),
pygame.image.load("klaw4.png"),
pygame.image.load("klaw5.png")]
bullet = pygame.image.load("bullet.png")
cinob = [
    pygame.image.load("crouch1.png"),
    pygame.image.load("crouch2.png"),
    pygame.image.load("crouch3.png"),
    pygame.image.load("crouch4.png"),
    pygame.image.load("crouch5.png")]

def moveleft(selttiks, cinoib, index, xstart, ystart):
    for leftloop in range(1, 5, 1):
        screen.fill((black))
        screen.blit(cinoib[leftloop],(xstart, ystart))
        pygame.display.update()
        fpsClock.tick(20)
##    if selttiks==1:
##        screen.blit(cinoib[index],(xstart, ystart))
##        index=index+1
##        xstart=xstart-5
##        if index==5:
##            index=0
def moveright(feuigtu, bionic, index, xstart, ystart):
    for rightloop in range(1, 5, 1):
        screen.fill((black))
        screen.blit(bionic[rightloop],(xstart, ystart))
        pygame.display.update()
        fpsClock.tick(20)
##    for img in bionic:
##        for stepy in range(ystart, ystart+100, 5):
##            for stepx in range(xstart, xstart+100, 5):
##                screen.fill((black))
##                screen.blit(img,(stepx,stepy))
##                pygame.display.update()
##                fpsclock.tick(10)


##    if feuigtu==1:
##        screen.blit(bionic[index],(xstart, ystart))
##        index=index+1
##        xstart=xstart+5
##        if index==5:
##            index=0
def crouch(pipx, cinob, crouchvar, xstart, ystart, e, index):
    for leftshift in range(1, 5, 1):
        screen.fill((black))
        screen.blit(cinob[leftshift],(xstart, ystart-150))
        pygame.display.update()

##def move(animation):
##    for img in animation:
##        screen.fill(black)
##        screen.blit(img, (50,50))
##        pygame.display.update()



while True:
    if selttiks==1:
        moveleft(selttiks, cinoib, index, xstart, ystart)
        xstart=xstart-20
        fpsClock.tick(60)
    if feuigtu==1:
        moveright(feuigtu, bionic, index, xstart, ystart)
        xstart=xstart+20

        fpsClock.tick(60)
    if pipx==1:
        crouch(pipx, cinob, crouchvar, xstart, ystart, e, index)
##    else:
##        if lp==0:
##            screen.blit(bionic[index],(xstart, ystart))
##        if lp==0 and s==0:
##            screen.blit(cinob[crouchvar],(xstart, ystart-100))
##            pygame.display.update()
##        if lp==1:
##            screen.blit(cinoib[index],(xstart, ystart))
##        if lp==2:
##            screen.blit(cinob[crouchvar],(xstart, ystart-100))
##        if lp==2:
##            screen.fill((black))
##            pygame.display.update()
    #player^\
##        for crouchvar in range(0, 4, 1):
##            screen.blit(cinob[e],(xstart, ystart-100))
##            crouchvar=crouchvar+1
##    pygame.display.update()
    if shoot==1 and lp==0:
        screen.blit(bullet,(k, oof))
        screen.fill((black))
        pygame.display.update()
        
        k=k+100
        if k==-9000:
            screen.fill((black))
    if shoot==1 and lp==1:
        screen.blit(bullet,(k, oof))
        screen.blit(bullet,(k, oof))

        k=k-100
        if k==9000:
            screen.fill((black))
    if pipy==1:
        ystart=ystart+qwerty
        if ystart==60:
                    qwerty=20
        elif ystart==200:
                    pipy=0
                    qwerty=-10
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                feuigtu=1
            if event.key == K_c:
                pipx=1
            if event.key == K_UP:
                pipy=1
            if event.key == K_RIGHT and lp==2:
                xstart=xstart+1
            if event.key == K_LEFT:
                selttiks=1
            if event.key == K_SPACE:
                k=xstart+125
                shoot=1
            if event.key == K_b:
                black=(0, 0, 0)
                screen.fill((black))
                pygame.display.update()
            if event.key == K_w:
                black=(255, 255, 255)
                screen.fill((black))
                pygame.display.update()
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                feuigtu=0
            if event.key == K_LEFT:
                selttiks=0
            if event.key == K_c:
                pipx=0

