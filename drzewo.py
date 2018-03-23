import serwPol

import mcpi.block as block
import time
import random
mc = serwPol.podlacz()
pos = mc.player.getPos()

r = 10

def kolo(pos, r, id):
    for i in range(-r, r + 1):
        for k in range(-r, r + 1):
            if i ** 2 + k ** 2 <= r ** 2:
                mc.setBlock(pos.x + i, pos.y, pos.z + k, id)


def walec(pos, r, h, id):
    for j in range(0,h):
        pos.y = pos.y + 1
        kolo(pos, r, id)


def kula(pos, r, id, maxRandom):
    for i in range(-r, r + 1):
        for j in range(-r, r + 1):
            for k in range(-r, r + 1):
                if i ** 2 + j ** 2 + k ** 2 <= r ** 2 and (random.randint (0, maxRandom) == 0):
                    mc.setBlock(pos.x + i, pos.y + j, pos.z + k, id)

def drzewo(pos):
    r_pnia = 3
    h_pnia = 15
    #rysowanie pnia
    walec(pos, r_pnia, h_pnia, block.WOOD.id)
    pos.y = pos.y + 10
    h_korony =  r_pnia + 10
    #rysowanie korony
    kula(pos, h_korony, block.CONCRETE_BLOCK_LIME.id, 5)

pos = mc.player.getPos()
mc.player.setPos(pos.x+10, pos.y, pos.z)
drzewo(pos)
