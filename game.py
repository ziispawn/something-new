import pygame, sys
from pygame.locals import *

pygame.init()
pygame.display.set_caption('game')

W = 500 # window width
H = 500 # window height
ws = pygame.display.set_mode((W, H))  # window surface
#ds = pygame.Surface((W,H), pygame.SRCALPHA, 32)
ds = ws.convert_alpha() # display surface

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()
frameNum = 1;   # variable to keep track of animation frames

class player:
    def __init__(self):
        keys = pygame.key.get_pressed()
        playerlv=1
        statpoints=10
        attack = 1
        defense = 4
        speed = 0
        hp = 1
        leg_armor = 1
        helmet = 1
        arm_armor = 1
        chest_armor = 1
        mp = 1
        magics = 0
        direction=0
    def draw(self):
        myfont = pygame.font.SysFont("monospace", 15)
        # render text
        
        print ("Y/N")
        if (keys[y])
            start = True
            print ("increase stats")
            print ("playerlv=1")
            print ("statpoints=10")
            print ("attack = 1")
            print ("defense = 4")
            print ("speed = 0")
            print ("leg_armor = 1")
            print ("helmet = 1")
            print ("chest_armor = 1")
            print ("mp = 1")
            print ("magics = 0")
            print ("press m for mp, d for defense, a for attack, M for speed, h for hp")
        if (statpoints>0 and start=True and keys[m]):
            mp+=1
        if (statpoints>0 and start=True and keys[d]):
            defense+=1
        if (statpoints>0 and start=True and keys[a]):
            attack+=1
        if (statpoints>0 and start=True and keys[M]):
            speed+=1
        if (statpoints>0 and start=True and keys[h]):
            hp+=1
        if (statpoints=0 and start=True):
            print ("press n for north, s for south, w for west, e for east")
        if (statpoints and start=True and keys[n]):
            diirections=1
            
            
        
        
        
class lv_1_enemy:
    def __init__(self):
         attack = 2
        defense = 5
        hp = 5
        mp = 1
        magics = 0
        speed=2
    if playerlv==1 and lv_1_enemy(hp)=0:
        xp+=10
    if xp==100 and playerlv==1:
        playerlv=2
    if playerlv==2 and lv_1_enemy(hp)=0:
        xp+=8
    if xp==200 and playerlv==2:
        playerlv=3
    if playerlv==3 and lv_1_enemy(hp)=0:
        xp+=5
    if xp==300 and playerlv==3:
        playerlv=4
    if playerlv==4 and lv_1_enemy(hp)=0:
        xp+=2
    if xp==400 and playerlv==4:
        playerlv=5
    if playerlv==5 and lv_1_enemy(hp)=0:
        xp+=0
    if xp==500 and playerlv==5:
        playerlv=5
        
        
        
class lv_2_enemy:
    def __init__(self):
        attack = 5
        defense = 18
        hp = 10
        mp = 5
        magics = 1
        magic =fireball, iceball, wind_slice, water_slash
        wind_slice = -4
        firball = -2
        iceball = -2
        water_slash=-4
    if playerlv==1 and lv_2_enemy(hp)=0:
        xp+=27
    if xp==100 and playerlv==1:
        playerlv=2
        stat points+20
        
    if playerlv==2 and lv_3_enemy(hp)=0:
        xp+=24
        
    if xp==200 and playerlv==2:
        playerlv=3
        statpoints+=30
        
    if playerlv==3 and lv_2_enemy(hp)=0:
        xp+=21
        
    if xp==300 and playerlv==3:
        playerlv=4
        statpoints+=40
        
    if playerlv==4 and lv_2_enemy(hp)=0:
        xp+=18
        
    if xp==400 and playerlv==4:
        playerlv=5
        statpoints+=50
        
    if playerlv==5 and lv_2_enemy(hp)=0:
        xp+=15
        
    if xp==500 and playerlv==5:
        playerlv=6
        statpoints+=60
        
    if playerlv==6 and lv_2_enemy(hp)=0:
        xp+=12
        
    if xp==600 and playerlv==6:
        playerlv=7
        statpoints+=70
    if playerlv==6 and lv_2_enemy(hp)=0:
        xp+=9
    if xp==700 and playerlv==7:
        playerlv=8
        statpoints+=80
        
    if playerlv==6 and lv_2_enemy(hp)=0:
        xp+=6
        
    if xp==800 and playerlv==8:
        playerlv=9
        statpoints+=90
        
    if playerlv==9 and lv_2_enemy(hp)=9:
        xp+=3
        
    if xp==600 and playerlv==6:
        playerlv=10
        statpoints+=100
        

class lv_3_enemy:
    def __init__(self):
        attack = 15
        defense = 63
        hp = 35
        mp = 18
        magics = 3
        magic =fireball, iceball, wind_slice, water_slice, flame, freeze,wind_slash, water_slice 

    if playerlv==1 and lv_3_enemy(hp)=0:
        xp+=225

    if xp==100 and playerlv==1:
        playerlv=2
        statpoints+=20

    if playerlv==2 and lv_3_enemy(hp)=0:
        xp+=210

    if xp==200 and playerlv==2:
        playerlv=3
        statpoints+=30

    if playerlv==3 and lv_3_enemy(hp)=0:
        xp+=195

    if xp==300 and playerlv==3:
        playerlv=4
        statpoints+=40

    if playerlv==4 and lv_3_enemy(hp)=0:
        xp+=180

    if xp==400 and playerlv==4:
        playerlv=5
        statpoints+=50

    if playerlv==5 and lv_3_enemy(hp)=0:
        xp+=165

    if xp==500 and playerlv==5:
        playerlv=6
        statpoints+=60

    if playerlv==6 and lv_3_enemy(hp)=0:
        xp+=150

    if xp==600 and playerlv==6:
        playerlv=7
        statpoints+=70

    if playerlv==7 and lv_3_enemy(hp)=0:
        xp+=135

    if xp==700 and playerlv==7:
        playerlv=8
        statpoints+=80

    if playerlv==8 and lv_3_enemy(hp)=0:
        xp+=120

    if xp==800 and playerlv==8:
        playerlv=9
        statpoints+=90

    if playerlv==9 and lv_3_enemy(hp)=0:
        xp+=105

    if xp==1000 and playerlv==9:
        playerlv=10
        statpoints+=100

    if playerlv==11 and lv_3_enemy(hp)=0:
        xp+=90
        
    if xp==1200 and playerlv==12:
        playerlv=12
        statpoints+=120
    if playerlv==11 and lv_3_enemy(hp)=0:
        xp+=75
        
    if xp==1300 and playerlv==12:
        playerlv=13
        statpoints+=130
    if playerlv==13 and lv_3_enemy(hp)=0:
        xp+=60
        
    if xp==1300 and playerlv==13:
        playerlv=14
        statpoints+=140
    if playerlv==14 and lv_3_enemy(hp)=0:
        xp+=45
        
    if xp==1400 and playerlv==14:
        playerlv=14
        statpoints+=140
    if playerlv==15 and lv_3_enemy(hp)=0:
        xp+=30
        
    if xp==1500 and playerlv==14:
        playerlv=15
        statpoints+=150
        
        
        
        
class lv_4_enemy:
    def __init__(self):
        attack = 60
        defense = 252
        hp = 140
        mp = 72
        magics = 4
        magic =fireball, iceball, wind_slice, water_slice, flame, freeze,wind_slash, water_slice,incinerate, flood, storm , glacier
    if playerlv==1 and lv_4_enemy(hp)=0:
        xp+=920

    if xp==100 and playerlv==1:
        playerlv=2
        statpoints+=20
        
    if playerlv==2 and lv_4_enemy(hp)=0:
        xp+=840
        
    if xp==200 and playerlv==2:
        playerlv=3
        statpoint+=30
        
    if playerlv==3 and lv_4_enemy(hp)=0:
        xp+=800
        
    if xp==300 and playerlv==3:
        playerlv=4
        statpoints+=40
        
    if playerlv==4 and lv_4_enemy(hp)=0:
        xp+=760
        
    if xp==400 and playerlv==4:
        playerlv=5
        statpoints+=50
        
    if playerlv==5 and lv_4_enemy(hp)=0:
        xp+=720
        
    if xp==500 and playerlv==5:
        playerlv=6
        statpoints+=60
        
    if playerlv==6 and lv_4_enemy(hp)=0:
        xp+=680
        
    if xp==600 and playerlv==6:
        playerlv=7
        statpoints+=70
        
    if playerlv==7 and lv_4_enemy(hp)=0:
        xp+=640
        
    if xp==700 and playerlv==7:
        playerlv=8
        statpoint+=80
        
    if playerlv==8 and lv_4_enemy(hp)=0:
        xp+=600
        
    if xp==800 and playerlv==8:
        playerlv=9
        statpoints+=90
        
    if playerlv==9 and lv_4_enemy(hp)=0:
        xp+=560
        
    if xp==1000 and playerlv==9:
        playerlv=10
        statpoint+=100
        
    if playerlv==10 and lv_4_enemy(hp)=0:
        xp+=520
        
    if xp==1100 and playerlv==10:
        playerlv=11
        statpoints+=110
        
    if playerlv==11 and lv_4_enemy(hp)=0:
        xp+=480
        
    if xp==1200 and playerlv==11:
        playerlv=12
        statpoints+=120
        
    if playerlv==12 and lv_4_enemy(hp)=0:
        xp+=440
        
    if xp==1300 and playerlv==12:
        playerlv=13
        statpoints+=120
        
    if playerlv==13 and lv_4_enemy(hp)=0:
        xp+=400
        
    if xp==1400 and playerlv==13:
        playerlv=14
        statpoints+=130
        
    if playerlv==14 and lv_4_enemy(hp)=0:
        xp+=460
        
    if xp==1500 and playerlv==14:
        playerlv=15
        statpoints+=150
        
    if playerlv==15 and lv_4_enemy(hp)=0:
        xp+=420
        
    if xp==1600 and playerlv==15:
        playerlv=16
        statpoints+=160
        
    if playerlv==16 and lv_4_enemy(hp)=0:
        xp+=380
        
    if xp==1700 and playerlv==16:
        playerlv=17
        statpoints+=170

    if playerlv==17 and lv_4_enemy(hp)=0:
        xp+=340
        
    if xp==1800 and playerlv==17:
        playerlv=18
        statpoints+=180
        
    if playerlv==18 and lv_4_enemy(hp)=0:
        xp+=300
        
    if xp==1900 and playerlv==19:
        playerlv=19
        statpoints+=190

    if playerlv==18 and lv_4_enemy(hp)=0:
        xp+=300
        
    if xp==1900 and playerlv==20:
        playerlv=20
        statpoints+=200
        


        
        
        
    
