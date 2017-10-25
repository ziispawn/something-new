import pygame, sys
from pygame.locals import *

pygame.init()
pygame.display.set_caption('Traffic Light')

W = 500 # window width
H = 500 # window height
ws = pygame.display.set_mode((W, H))  # window surface
#ds = pygame.Surface((W,H), pygame.SRCALPHA, 32)
ds = ws.convert_alpha() # display surface

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()
frameNum = 1;   # variable to keep track of animation frames

class TrafficLight:

    def __init__(self):
        self.setState('green')
        self.redXY = (int(W/2), int(H*1/6))
        self.yellowXY = (int(W/2), int(H*2/6))
        self.greenXY = (int(W/2), int(H*3/6))
        self.purpleXY = (int(W/2), int(H*4/6))
        self.blueXY = (int(W/2), int(H*5/6))
        
        self.blinking = False

    def setState(self, stateStr):
        self.state = stateStr

    def setBlinking(self, blinkBool):
        self.blinking = blinkBool

    def drawLight(self, rgbaColor, xyPos):
        pygame.draw.circle(ds, rgbaColor, xyPos, 50)

    def update(self):
         if self.blinking:
                
            if event.key == pygame.K_SPACE and frameNum %30 < 5:
                self.setState('red')
                print("red")

       
            if frameNum % 30 < 5:
                self.setState('green')
                print ('green')
            else:
                self.setState('off')

        
            if frameNum %30 <= 5 and event.key != pygame.space :
                self.setState('yellow')
                print('yellow')
            if self.selfstate()==self.state('yellow') and event.key == pygame.space :
                self.setState('red')
            if self.selfstate()==self.state('blue') and event.key == pygame.space :
                self.setState('red')
            if self.selfstate()==self.state('purple') and event.key == pygame.space :
                self.setState('red')
            if selfstate== selfstate('red') and event.key == pygame.g:
                self.setState('red')
            if self.selfstate()==self.state('purple') and event.key == pygame.g :
                self.setState('green')
        
            else:
                self.setState('off')

    def draw(self):

        if self.state == 'green':
            self.drawLight((0, 255, 0, 255), self.greenXY)
        else:
            self.drawLight((0, 255, 0, 0), self.greenXY)

        if self.state == 'yellow':
            self.drawLight((255, 255, 0, 255), self.yellowXY)
        else:
            self.drawLight((255, 255, 0, 0), self.yellowXY)

        if self.state == 'red':
            self.drawLight((255, 0, 0, 255), self.redXY)
        else:
            self.drawLight((255, 0, 0, 0), self.redXY)


trafficLight = TrafficLight()

while True: # main game loop

    ws.fill((0, 0, 0))
    trafficLight.update()
    trafficLight.draw()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            trafficLight.setBlinking(True)
            print("mouse down!")
        elif event.type == pygame.MOUSEBUTTONUP:
            trafficLight.setBlinking(False)
            print("mouse up!")
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("space key!")

    if frameNum < 90:
        frameNum += 1
    else:
        frameNum = 0

    ws.blit(ds, (0,0))
    pygame.display.update()
    fpsClock.tick(FPS)
