import pgzrun
import random
WIDTH=800
HEIGHT=600
TITLE="Gallaga"
ammo=[]
coolship=Actor("coolship")
coolship.pos=(400,550)
alienbug=Actor("alienbug")
alienbug.pos=(400,50)
def draw():
    screen.blit("space",(0,0))
    coolship.draw()
    alienbug.draw()
    for bullet in ammo:
        bullet.draw()



def update():
    
    alienbug.y=alienbug.y+3
    for bullet in ammo:
        bullet.y=bullet.y-3
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
    if key==keys.UP:
        bullet=Actor("bullet")
        bullet.pos=coolship.pos
        ammo.append(bullet) 
    



 

pgzrun.go()