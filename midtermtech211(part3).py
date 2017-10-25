import pygame, os, sys
from pygame.locals import *
from qhue import Bridge
b=Bridge("192.168.2.","nnUS6rndMcOE0XIWIVsxMA8EA-0xJH4Yqk1A-hCDf")
ds = pygame.display.set_mode((400, 300))

redColor = (255, 0, 0)
greenColor = (0, 255, 0)
blueColor = (0, 0, 255)
purpleColor = (255, 0, 255)
lights=b.lights
blueHue=b.lights[1].state(hue=46900)
yellowHue=b.lights[2].state(hue=12750)
greenHue=b.lights[3].state(hue=22500)
purpleHue=b.lights[3].state(hue=56100)
redHue=b.lights[3].state(hue=56100)
pygame.init()


        



if (keys[b] or[B]):
        b.lights[1]
        pygame.draw.circle(ds, blueColor, (200, 150), 50)
	
if (keys[g] or keys[G]):
        b.lights[2]
        pygame.draw.circle(ds, greenColor, (200, 150), 50)
	
if (keys[r] or keys[R]):
        b.lights[3]
        pygame.draw.circle(ds, redColor, (200, 150), 50)
if (keys[p] or keys[P]):
        b.lights[4]
        pygame.draw.circle(ds, purpleColor, (200, 150), 50)
    

    





    
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            pygame.display.update()
    
    

