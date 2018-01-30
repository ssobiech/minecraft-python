import mcpi.minecraft as minecraft
from mineturtle import *
import mcpi.block as block
import server
import sys
import serwPol as mine

a = 15

def bok():
    p.go(a)
    p.left(60)
    p.go(a)
    p.right(120)
    
    p.go(a)
    p.left(60)
    p.go(a)
    p.right(180-135)


if __name__ == "__main__":
    mc = mine.podlacz()
    playerPos = mc.player.getPos()
    p = Turtle(mc)
    p.angle(90)
    p.verticalangle(0)
 #   p.setverticalheading(90)
    for i in range(8):
        bok()
