import serwPol
import logger

from minecraftstuff import *


mc = serwPol.podlacz()
logger = logger.Logger()

pos = mc.player.getTilePos()
p = MinecraftTurtle(mc, pos)
a = 10


def trojkat():
    for i in range(3):
        p.forward(a)
        p.right(60)
        p.forward(a)
        p.left(120)
        p.forward(a*2)
        p.right(120)
        p.forward(a)
        p.left(60)
        p.forward(a)
        p.left(120)

def pas(l):
    for i in range(l):
        trojkat()
        p.penup()
        p.forward(a*4)
        p.pendown()
    p.penup()
    p.backward(a*4*l)
    p.left(60)
    p.forward(a*4)
    p.right(60)
    p.pendown()

def piramida():
    t = 4
    for i in range(t):
        pas(t)
        t = t-1

p.speed(0)
piramida()
