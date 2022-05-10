import pygame
import time
import random
from pygame.locals import *
screen=pygame.display.set_mode((900, 900))
pygame.display.set_caption("pong")
pygame.init()
red=(255,0,0)
green=(0,255,0)
blue=(0,175,255)
white=(255,255,255)
black=(0,0,0)
screen.fill((white))
def show_text(msg,x,y,red):
    fontobj= pygame.font.SysFont("freesans",32)
    msgobj = fontobj.render(msg,False,red)
    screen.blit(msgobj,(x,y))
def show_texasddast(msg,x,y,blue):
    fontobj= pygame.font.SysFont("freesans",32)
    msgobj = fontobj.render(msg,False,blue)
    screen.blit(msgobj,(x,y))
def show_tezxcadfafxt(msg,x,y,green):
    fontobj= pygame.font.SysFont("freesans",64)
    msgobj = fontobj.render(msg,False,green)
    screen.blit(msgobj,(x,y))
def show_texfdgsydfgaut(msg,x,y,green):
    fontobj= pygame.font.SysFont("freesans",64)
    msgobj = fontobj.render(msg,False,green)
    screen.blit(msgobj,(x,y))
fpsclock = pygame.time.Clock()
a=840
o=350
k=35
b=350
hi=351
ii=350
u=400
i=450
f=1
p=o-100
l=b-100
op=0
ur=0
left_pad_down=0
left_pad_up=0
right_pad_down=0
right_pad_up=0
##nasa=[]
##for lop in range(0, 5, 1):
##    s=pygame.Surface((100, 100))
##    nasa.append(s)
##for lep in range(0, 5, 1):
##    a=random.randint(1, 899)
##    b=random.randint(1, 899)
##    screen.blit(nasa[lep],(a, b))
##while True:
##    pygame.display.update()
##    for event in pygame.event.get():
##        if event.type == QUIT:
##            pygame.quit()
##            exit()
pygame.draw.rect(screen, red, (k, o, 25, 100), )
pygame.draw.rect(screen, blue, (a, b, 25, 100), )
pygame.display.update()
ichange=1
uchange=1
while True:
    pygame.display.update()
    screen.fill((white))
    pygame.draw.circle(screen, red, (i, u), (25), )
    pygame.draw.rect(screen, red, (k, o, 25, 100), )
    pygame.draw.rect(screen, blue, (a, b, 25, 100), )
    show_text (str(op),25,25,red)
    show_texasddast (str(ur),843,25,blue)
    i=i+ichange
    u=u+uchange
    if i>=875:
       ichange=-1
       op=op+1
       pygame.display.update()
    if i<=25:
       ichange=1
       ur=ur+1
       pygame.display.update()
    if u>=875:
       uchange=-1
    if u<=25:
       uchange=1
    if op>=20:
        show_tezxcadfafxt ("Red Wins!",350,350,green)
        pygame.display.update()
        time.sleep(2)
        break
    if ur>=20:
        show_texfdgsydfgaut ("Blue Wins!",350,350,green)
        pygame.display.update()
        time.sleep(2)
        break
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_s:
                left_pad_down=1
            if event.key == K_w:
                left_pad_up=1
            if event.key == K_DOWN:
                right_pad_down=1
            if event.key == K_UP:
                right_pad_up=1
        elif event.type == KEYUP:
            if event.key ==K_s:
                left_pad_down=0
            if event.key == K_w:
                left_pad_up=0
            if event.key == K_DOWN:
                right_pad_down=0
            if event.key == K_UP:
                right_pad_up=0
    if left_pad_down ==1:
        o=o+2
    if left_pad_up ==1:
        o=o-2
    if o<=0:
        left_pad_up=0
    if o>=800:
        left_pad_down=0
    if right_pad_down ==1:
        b=b+2
    if right_pad_up ==1:
        b=b-2
    if b<=0:
        right_pad_up=0
    if b>=800:
        right_pad_down=0
        
    ##print(i+50,u,b)
    if (i+25) in range(840,890) and u in range(b-15, b+100):
        ichange=-1
    if (i-25) in range(35, 50) and u in range(o-15, o+100):
        ichange=1
           
                    
                    
                    
        
                    
                    
