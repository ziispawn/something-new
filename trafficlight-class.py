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
        self.redX = (int(W/2))
        self.redY = (int(H*1/4))
        self.redX2 = (int(W/2+20))
        self.redY2 = (int(H*1/4-20))
        self.redX3 = (int(W/2-20))
        self.redY3 = (int(H*1/4-20))
        self.redX4 = (int(W/2-25))
        self.redY4 = (int(H*1/4-15))
        self.redX5 = (int(W/2+25))
        self.redY5 = (int(H*1/4-15))
        self.redX6 = (int(W/2+75))
        self.redY6 = (int(H*1/4-25))
        self.redX7 = (int(W/2+10))
        self.redY7 = (int(H*1/4-25))
        self.yellowX = (int(W/2))
        self.yellowY = (int(H*1/2))
        self.yellowX2 = (int(W/2+20))
        self.yellowY2 = (int(H*1/2-20))
        self.yellowX3 = (int(W/2)-20)
        self.yellowY3 = (int(H*1/2-20))
        self.yellowX4 = (int(W/2-25))
        self.yellowY4 = (int(H*1/2-25))
        self.yellowX5 = (int(W/2+25))
        self.yellowY5 = (int(H*1/2-25))
        self.yellowX6 = (int(W/2-75))
        self.yellowY6 = (int(H*1/2-35))
        self.yellowX7 = (int(W/2+75))
        self.yellowY7 = (int(H*1/2-35))
        self.greenX = (int(W/2))
        self.greenY = (int(H*3/4))
        self.greenX2 = (int(W/2+20))
        self.greenY2 = (int(H*3/4-20))
        self.greenX3 = (int(W/2-20))
        self.greenY3 = (int(H*3/4-20))
        self.greenX4 = (int(W/2-20))
        self.greenY4 = (int(H*3/4-20))
        self.greenX5 = (int(W/2-35))
        self.greenY5 = (int(H*3/4-20))
        self.blinking = False

    def setState(self, stateStr):
        self.state = stateStr

    def setBlinking(self, blinkBool):
        self.blinking = blinkBool

    def drawLight(self, rgbaColor, xyPos):
        pygame.draw.circle(ds, rgbaColor, (self.redX,self.redY) , 50)
    def drawLight2(self, rgbaColor, xyPos):
        pygame.draw.circle(ds, rgbaColor, (self.yellowX,self.yellowY) , 50)
    def drawLight3(self, rgbaColor, xyPos):
        pygame.draw.circle(ds, rgbaColor, (self.greenX,self.greenY) , 50)
    

    def drawLighteyes(self, rgbaColor, xyPos):
        pygame.draw.circle(ds, rgbaColor, (self.redX2,self.redY2), 10)
    def drawLighteyes2(self, rgbaColor, xyPos):
        pygame.draw.circle(ds, rgbaColor, (self.redX3,self.redY3), 10)
    def drawLighteyes3(self, rgbaColor, xyPos):
        pygame.draw.circle(ds, rgbaColor, (self.yellowX2,self.yellowY2), 10)
    def drawLighteyes4(self, rgbaColor, xyPos):
        pygame.draw.circle(ds, rgbaColor, (self.yellowX3,self.yellowY3), 10)
    def drawLighteyes5(self, rgbaColor, xyPos):
        pygame.draw.circle(ds, rgbaColor, (self.greenX2,self.greenY2), 10)
    def drawLighteyes6(self, rgbaColor, xyPos):
        pygame.draw.circle(ds, rgbaColor, (self.greenX3,self.greenY3), 10)
        #red pupils
    def drawLighteyespupils(self, rgbaColor, xyPos):
        pygame.draw.circle(ds, rgbaColor, (self.redX4,self.redY4), 3)
    def drawLighteyespupils2(self, rgbaColor, xyPos):
        pygame.draw.circle(ds, rgbaColor, (self.redX5,self.redY5), 3)
        #yellow pupils
    def drawLighteyespupils3(self, rgbaColor, xyPos):
        pygame.draw.circle(ds, rgbaColor, (self.redX4,self.yellowY4), 3)
    def drawLighteyespupils4(self, rgbaColor, xyPos):
        pygame.draw.circle(ds, rgbaColor, (self.redX5,self.yellowY5), 3)
        #green pupils
    def drawLighteyespupils5(self, rgbaColor, xyPos):
        pygame.draw.circle(ds, rgbaColor, (self.greenX4,self.greenY4), 3)
    def drawLighteyespupils6(self, rgbaColor, xyPos):
        pygame.draw.circle(ds, rgbaColor, (self.greenX5,self.greenY5), 3)

    #red
    def drawLighteyebrows(self, rgbaColor, xyPos):
        pygame.draw.rect(ds, rgbaColor, (5, 2, self.redX6,self.redY6))
    def drawLighteyebrows2(self, rgbaColor, xyPos):
        pygame.draw.rect(ds, rgbaColor, (5, 2, self.redX7, self.redY7))

    #yellow
    def drawLighteyebrows3(self, rgbaColor, xyPos):
        pygame.draw.rect(ds, rgbaColor, (5, 2, self.yellowX6, self.yellowY6))
    def drawLighteyebrows4(self, rgbaColor, xyPos):
        pygame.draw.rect(ds, rgbaColor, (5, 2, self.yellowX7, self.yellowY7))
    #green
    def drawLighteyebrows5(self, rgbaColor, xyPos):
        pygame.draw.rect(ds, rgbaColor, ( 5,2, self.greenX6,self.greenY6))
    def drawLighteyebrows6(self, rgbaColor, xyPos):
        pygame.draw.rect(ds, rgbaColor, ( 5,5,self.greenX7, self.greenY7))

    
    def update(self):

        if self.blinking:
            if frameNum % 30 < 15:
                self.setState('red')
            else:
                self.setState('off')

        elif frameNum < 30:
            self.setState('green')
        elif frameNum < 60:
            self.setState('yellow')
        elif frameNum < 90:
            self.setState('red')
        else:
            self.setState('off')

    def draw(self):

        if self.state == 'green':
            self.greenX5=int(W/2+25)+1
            self.drawLight3((0, 255, 0, 255), self.greenX)
            self.drawLight3((0, 255, 0, 255), self.greenY)
            self.drawLighteyes5((255, 255, 255, 255), self.greenX2)
            self.drawLighteyes5((255, 255, 255, 255), self.greenY2)
            self.drawLighteyes6((255, 255, 255, 255), self.greenX3)
            self.drawLighteyes6((255, 255, 255, 255), self.greenY3)
            self.drawLighteyespupils5((0, 0, 0, 255), self.greenY4)
            self.drawLighteyespupils5((0, 0, 0, 255), self.greenX4)
            self.drawLighteyespupils6((0, 0, 0, 255), self.greenX5)
            self.drawLighteyespupils6((0, 0, 0, 255), self.greenY5)
           
        else:
            self.drawLight3((0, 255, 0, 100), self.greenX)
            self.drawLight3((0, 255, 0, 100), self.greenY)
            self.drawLighteyes5((255, 255, 255, 100), self.greenX2)
            self.drawLighteyes5((255, 255, 255, 100), self.greenY2)
            self.drawLighteyes6((255, 255, 255, 100), self.greenX3)
            self.drawLighteyes6((255, 255, 255, 100), self.greenY3)
            self.drawLighteyespupils5((0, 0, 0, 100), self.greenX4)
            self.drawLighteyespupils5((0, 0, 0, 100), self.greenY4)
            self.drawLighteyespupils6((0, 0, 0, 100), self.greenX5)
            self.drawLighteyespupils6((0, 0, 0, 100), self.greenY5)

        if self.state == 'yellow':
            self.drawLight2((255, 255, 0, 255), self.yellowX)
            self.drawLight2((255, 255, 0, 255), self.yellowY)
            self.drawLighteyes3((255, 255, 255, 255), self.yellowX2)
            self.drawLighteyes3((255, 255, 255, 255), self.yellowY2)
            self.drawLighteyes4((255, 255, 255, 255), self.yellowX3)
            self.drawLighteyes4((255, 255, 255, 255), self.yellowY3)
            self.drawLighteyespupils3((0, 0, 0, 255), self.yellowY4)
            self.drawLighteyespupils3((0, 0, 0, 255), self.yellowX4)
            self.drawLighteyespupils4((0, 0, 0, 255), self.yellowX5)
            self.drawLighteyespupils4((0, 0, 0, 255), self.yellowY5)
            self.drawLighteyebrows3((0, 0, 0, 100), self.yellowX6)
            self.drawLighteyebrows3((0, 0, 0, 100), self.yellowY6)
            self.drawLighteyebrows4((0, 0, 0, 100), self.yellowX7)
            self.drawLighteyebrows4((0, 0, 0, 100), self.yellowY7)
            
        else:
            self.drawLight2((255, 255, 0, 100), self.yellowX)
            self.drawLight2((255, 255, 0, 100), self.yellowY)
            self.drawLighteyes3((255, 255, 255, 100), self.yellowX2)
            self.drawLighteyes3((255, 255, 255, 100), self.yellowY2)
            self.drawLighteyes4((255, 255, 255, 100), self.yellowX3)
            self.drawLighteyes4((255, 255, 255, 100), self.yellowY3)
            self.drawLighteyespupils3((0, 0, 0, 100), self.yellowY4)
            self.drawLighteyespupils3((0, 0, 0, 100), self.yellowX4)
            self.drawLighteyespupils4((0, 0, 0, 100), self.yellowX5)
            self.drawLighteyespupils4((0, 0, 0, 100), self.yellowY5)


        if self.state == 'red':
            self.drawLight((255, 0, 0, 255), self.redX)
            self.drawLight((255, 0, 0, 255), self.redY)
            self.drawLighteyes((255, 255, 255, 255), self.redX2)
            self.drawLighteyes((255, 255, 255, 255), self.redY2)
            self.drawLighteyes2((255, 255, 255, 255), self.redX3)
            self.drawLighteyes2((255, 255, 255, 255), self.redY3)
            self.drawLighteyespupils((0, 0, 0, 255), self.redY4)
            self.drawLighteyespupils((0, 0, 0, 255), self.redX4)
            self.drawLighteyespupils2((0, 0, 0, 255), self.redX5)
            self.drawLighteyespupils2((0, 0, 0, 255), self.redY5)
            self.drawLighteyebrows((0, 0, 0, 100), self.redX6)
            self.drawLighteyebrows((0, 0, 0, 100), self.redY6)
            self.drawLighteyebrows2((0, 0, 0, 100), self.redX7)
            self.drawLighteyebrows2((0, 0, 0, 100), self.redY7)

        else:
            self.drawLight((255, 0, 0, 100), self.redX)
            self.drawLight((255, 0, 0, 100), self.redY)
            self.drawLighteyes((255, 255, 255, 100), self.redX2)
            self.drawLighteyes((255, 255, 255, 100), self.redY2)
            self.drawLighteyes2((255, 255, 255, 100), self.redX3)
            self.drawLighteyes2((255, 255, 255, 100), self.redY3)
            self.drawLighteyespupils((0, 0, 0, 100), self.redY4)
            self.drawLighteyespupils((0, 0, 0, 100), self.redX4)
            self.drawLighteyespupils((0, 0, 0, 100), self.redX5)
            self.drawLighteyespupils2((0, 0, 0, 100), self.redY5)
            self.drawLighteyespupils2((0, 0, 0, 255), self.redY5)




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

    if frameNum < 90:
        frameNum += 1
    else:
        frameNum = 0

    ws.blit(ds, (0,0))
    pygame.display.update()
    fpsClock.tick(FPS)
