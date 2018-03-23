import serwPol
import logger
from mineturtle import *
mc = serwPol.podlacz()


pos = mc.player.getTilePos()
p = Turtle()
def rysuj():
    for i in range(4):
        p.go(15)
        p.left(90)

rysuj()
