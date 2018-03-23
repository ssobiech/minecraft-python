from serwPol import *
from minecraftstuff import *


def kwadrat(turtle, size):
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)


if __name__ == "__main__":
    mc = podlacz()
    pos = mc.player.getTilePos()
    turtle = MinecraftTurtle(mc, pos)
    kwadrat(turtle, 10)
