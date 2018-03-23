import serwPol
import mcpi.block as block
import random
from math import sqrt

mc = serwPol.podlacz()
pos = mc.player.getTilePos()

def pien(r):
    for i in range(-r,r+1):
        for j in range(-r,r+1):
            for k in range(-r,r+1):
                mc.setBlock(pos.x + i, pos.y + k, pos.z + j, block.WOOD.id)

def pien2(r,w):
    for i in range(-r, r + 1):
        for j in range (0, w):
            for k in range(-r, r + 1):
                if sqrt(i ** 2 + k ** 2) <= r:
                    mc.setBlock(pos.x + i, pos.y + j, pos.z + k, block.DIAMOND_BLOCK.id)

def kula(r,w):
    for i in range(-r, r + 1):
        for j in range (-r, r+1):
            for k in range(-r, r + 1):
                punkt = sqrt(i ** 2 + k ** 2+ j**2)
                if  punkt <= r  and random.randint (0, 5) == 0:
                    mc.setBlock(pos.x + i, pos.y + j+w+r-3, pos.z + k, block.WOOL_LIME.id,5)

def stozek(r,h):
    for i in range(-r, r):
        for j in range (-h, 0):
            for k in range(-r, r):
                x = pos.x +i
                y = pos.y + j
                z = pos.z + k

                if (x-pos.x)**2 + (z-pos.z)**2 <= (((pos.y-y)*r)/h)**2 and random.randint (0, 5) == 0:
                    mc.setBlock(x, y, z, 251,13)

def figura(r,h):
    for i in range(-r, r):
        for j in range (-h, 0):
            for k in range(-r, r):
                x = pos.x +i
                y = pos.y + j
                z = pos.z + k

                if ((pos.x)**2 / (i)**2) + (pos.z**2 + j**2) - (pos.y**2 + k**2) == 1:
                    mc.setBlock(x, y, z, 251,13)
pien2(3,13)y
pos.y = pos.y + 36
#kula(16,-26)
figura(13,26)
