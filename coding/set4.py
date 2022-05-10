import pygame
import time
import random
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
fpsclock = pygame.time.Clock()
screen.fill((white))
x=450
y=450
pygame.draw.circle(screen, blue, (x, y), (100), )
pygame.display.update()
c=1
xchange = random.randint(1, 5)
ychange = random.randint(1, 5)
while True:
      screen.fill((black))
      d=-2
      x=x+xchange
      y=y+ychange
      pygame.draw.circle(screen, blue, (x, y), (100), )
      pygame.display.update()
      if x>=900:
            c=-1
      if x==0:
            c=1
      if x>=900:
            xchange = random.randint(-5, -1)
      if x<=0:
            xchange = random.randint(1, 5)
      if y>=900:
            ychange=random.randint(-5, -1)
      if y<=0:
            ychange=random.randint(1, 5)
##plist = []
##for l in range(1, 50, 1):
##      x = [ random.randint(0, 900), random.randint(0, 900) ]
##      plist.append(x)
##      pygame.draw.circle(screen, white, (l), (2), )
##      pygame.display.update()
##      screen.fill((black))
##      pygame.display.update()
##      pygame.draw.circle(screen, white, (l), (2), )
##      pygame.display.update()
##      

##while True:
##      for i in plist:
##            pygame.draw.circle(screen, white, i, 2)
##            i[1]=i[1]+1
##            if i[1]==900:
##                  i[1]=0
##                  i[0]=random.randint(0, 900)
##      pygame.display.update()
##      a=random.randint(30, 250)
##      pygame.display.update()
##      fpsclock.tick(a)
##      screen.fill((black))
##tyvg=[]
##for er in range(1, 6, 1):
##      s = pygame.Surface((100, 100))
##      i=random.randint(0, 700)
##      pygame.draw.circle(s, blue, (50, 50), (20), )
##      tyvg.append(s)
##      print(tyvg)
##while True:
##      for v in range(0, 5, 1):
##            screen.blit(tyvg[v], (i, i))
##            pygame.display.update()
      
