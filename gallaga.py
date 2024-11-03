import pgzrun
import random
WIDTH=800
HEIGHT=600
TITLE="Gallaga"
score=0
ammo=[]
coolship=Actor("coolship")
coolship.pos=(400,550)
alienbug=Actor("alienbug")
alienbug.pos=(400,50)
def draw():
    screen.blit("space",(0,0))
    coolship.draw()
    alienbug.draw()
    screen.draw.text("score="+str(score),(10,25),color="blue",fontsize=40)
    for bullet in ammo:
        bullet.draw()



def update():
    global score
    alienbug.y=alienbug.y+3
    for bullet in ammo:
       bullet.y=bullet.y-3
       if bullet.colliderect(alienbug):
        score=score+1
        alienbug.pos=(random.randint(50,WIDTH),0)
        ammo.remove(bullet)
       if bullet.y<0:
        ammo.remove(bullet)

    if alienbug.y>HEIGHT:
        alienbug.pos=(random.randint(50,WIDTH),0)
    if coolship.x>WIDTH:
        coolship.x=+0
    if coolship.x<0:
        coolship.x=WIDTH
    if keyboard.left:
        coolship.x=coolship.x-7
    if keyboard.right:
        coolship.x=coolship.x+7 
    
    

def on_key_down(key):
    if key==keys.UP and len(ammo)<3:
        bullet=Actor("bullet")
        bullet.pos=coolship.pos
        ammo.append(bullet) 
    



 

pgzrun.go()