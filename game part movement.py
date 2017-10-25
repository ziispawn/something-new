
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
        direction="d"
        stamina=3
    def draw(self):
        myfont = pygame.font.SysFont("monospace", 15)
        # render text
        print("start")
        print ("Y/N")
        if (keys[y]):
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
        if (statpoints>0 and start==True and keys[m]):
            mp+=1
        if (statpoints>0 and start==True and keys[d]):
            defense+=1
        if (statpoints>0 and start==True and keys[a]):
            attack+=1
        if (statpoints>0 and start==True and keys[M]):
            speed+=1
        if (statpoints>0 and start==True and keys[h]):
            hp+=1
        if (statpoints==0 and start==True):
            print ("press n for north, s for south, w for west, e for east")
        if (statpoints and start==True and keys[n]):
            diirections+=n
            stamina-=1
        if (statpoints and start==True and keys[s]):
            diirections+=s
            stamina-=1
        if (statpoints and start==True and keys[w]):
            diirections+=w
            stamina-=1
        if (statpoints and start==True and keys[e]):
            diirections+=e
            stamina-=1
        if (stamina==0):
             print("player is asleep")
             
    
