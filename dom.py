import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import serwPol
mc = serwPol.podlacz()
playerPos = mc.player.getPos()

def init():
    mc.setBlocks(playerPos.x -2, playerPos.y, playerPos.z -1, playerPos.x +6, playerPos.y +5, playerPos.z +7, block.AIR)

def podloga():
    mc.setBlocks(playerPos.x -1, playerPos.y -1, playerPos.z, playerPos.x +5, playerPos.y -1, playerPos.z +6, block.BRICK_BLOCK) #podloga
    
def sufit():
    mc.setBlocks(playerPos.x, playerPos.y +3, playerPos.z +1, playerPos.x +4, playerPos.y +3, playerPos.z +5, block.BRICK_BLOCK) #sufit
    
def sciany():
    mc.setBlocks(playerPos.x +5, playerPos.y, playerPos.z +6, playerPos.x, playerPos.y +2, playerPos.z +6, block.BRICK_BLOCK) #sciana1(przod)
    mc.setBlocks(playerPos.x +5, playerPos.y, playerPos.z +5, playerPos.x +5, playerPos.y +2, playerPos.z, block.BRICK_BLOCK) #sciana2(lewa)
    mc.setBlocks(playerPos.x +4, playerPos.y, playerPos.z, playerPos.x, playerPos.y +2, playerPos.z, block.BRICK_BLOCK) #sciana3(tyl)
    mc.setBlocks(playerPos.x-1, playerPos.y, playerPos.z +6, playerPos.x-1, playerPos.y +2, playerPos.z, block.BRICK_BLOCK) #sciana4(prawa)
    
def drzwi():
    mc.setBlock(playerPos.x -1, playerPos.y, playerPos.z +3, block.AIR)#drzwi1
    mc.setBlock(playerPos.x -1, playerPos.y +1, playerPos.z +3, block.AIR) #drzwi2
    mc.setBlock(playerPos.x -1, playerPos.y, playerPos.z +3, block.DOOR_WOOD) #daje drzwi :P
    mc.setBlock(playerPos.x -1, playerPos.y -1, playerPos.z +3, block.WOOD_PLANKS_OAK) #drzwi podloga

def scierzka():
    mc.setBlocks(playerPos.x-2, playerPos.y -1, playerPos.z +1, playerPos.x -2, playerPos.y -1, playerPos.z +4, block.GRASS_PATH) #scierzka

def swiatlo():
    mc.setBlock(playerPos.x, playerPos.y, playerPos.z +1, block.TORCH)
    mc.setBlock(playerPos.x, playerPos.y, playerPos.z +5, block.TORCH)
    mc.setBlock(playerPos.x -1, playerPos.y +3, playerPos.z +3, block.TORCH)
    mc.setBlock(playerPos.x +5, playerPos.y +2, playerPos.z +3, block.GLOWSTONE_BLOCK)

def designErr():
    mc.setBlock(playerPos.x +3, playerPos.y, playerPos.z +5, block.BED_OBJECT) #nie dziala!
    mc.setBlock(playerPos.x +4, playerPos.y, playerPos.z +5, block.BED) #nie dziala!

def design():
    mc.setBlock(playerPos.x +4, playerPos.y, playerPos.z +1, block.CRAFTING_TABLE)
    mc.setBlock(playerPos.x +4, playerPos.y, playerPos.z +2, block.FURNACE_INACTIVE)    
    mc.setBlock(playerPos.x +4, playerPos.y, playerPos.z +3, block.CHEST)
    mc.setBlock(playerPos.x +4, playerPos.y, playerPos.z +4, block.CHEST)
    mc.setBlock(playerPos.x +4, playerPos.y +1, playerPos.z +3, block.CHEST)
    mc.setBlock(playerPos.x +4, playerPos.y +1, playerPos.z +4, block.CHEST)
    
def okna():
    mc.setBlocks(playerPos.x -1, playerPos.y +1, playerPos.z, playerPos.x +4, playerPos.y +1, playerPos.z, block.GLASS)
    mc.setBlocks(playerPos.x -1, playerPos.y +1, playerPos.z, playerPos.x -1, playerPos.y +1, playerPos.z +6, block.GLASS)
    mc.setBlocks(playerPos.x -1, playerPos.y +1, playerPos.z +6, playerPos.x +4, playerPos.y +1, playerPos.z +6, block.GLASS)

def end():
    mc.player.setPos(playerPos.x +1, playerPos.y, playerPos.z +1)

def dom():
    init()
    podloga()
    sufit()
    sciany()
    scierzka()
    swiatlo()
    design()
    okna()
    drzwi()
    end()
    
dom()
