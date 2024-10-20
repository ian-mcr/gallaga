import pgzrun
WIDTH=800
HEIGHT=600
TITLE="Gallaga"
coolship=Actor("coolship")
coolship.pos=(400,550)
alienbug=Actor("alienbug")
alienbug.pos=(400,50)
def draw():
    screen.blit("space",(0,0))
    coolship.draw()
    alienbug.draw()



def update():
    alienbug.y=alienbug.y+3
 

pgzrun.go()