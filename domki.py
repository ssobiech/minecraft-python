# -*- coding: cp1250 -*-

import mcpi.minecraft as minecraft
import mcpi.block as block
import serwPol


def pietro(x, y, z):
    mc.setBlocks(0+x, 0+y, 0+z, 3+x, 2+y, 3+z, block.STONE.id)   #sciany
    mc.setBlocks(0+x, 1+y, 1+z, 3+x, 2+y, 2+z, block.GLASS.id)   #okna1
    mc.setBlocks(1+x, 1+y, 0+z, 2+x, 2+y, 3+z, block.GLASS.id)   #okna2
    mc.setBlocks(1+x, 0+y, 1+z, 2+x, 2+y, 2+z, block.AIR.id)     #puste wnetrze
    mc.setBlocks(0+x, 0+y, 1+z, 0+x, 2+y, 1+z, block.GLASS.id)   #drzwi
    mc.setBlocks(0+x, 3+y, 0+z, 3+x, 3+y, 3+z, block.BEDROCK.id) #sufit


def domek(x, z):
    mc.setBlocks(x-1, -1, z-1, x+4, -1, z+4, block.GRASS.id)  #trawnik/podloga
    pietro(x, 0, z)


def domekPietrowy(x, z, pietra):
    mc.setBlocks(x-1, -1, z-1, x+4, -1, z+4, block.GRASS.id)  #trawnik/podloga
    for i in range(0, pietra*4, 4):
        pietro(x, i, z)

mc = serwPol.podlacz()

pos = mc.player.getPos()

domekPietrowy(pos.x+5, pos.z, 4)
