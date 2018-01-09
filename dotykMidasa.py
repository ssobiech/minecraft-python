import mcpi.minecraft as minecraft
import time

mc = minecraft.Minecraft.create()

def dotykMidasa():
    gold = 41
    water = 9
    air = 0

    while True:
	    pos = mc.player.getTilePos()
	    blockBelow = mc.getBlock(pos.x, pos.y - 1, pos.z)
	    if blockBelow != air and blockBelow != water:
   		    mc.setBlock(pos.x, pos.y - 1, pos.z, gold)
	    time.sleep(0.5)

dotykMidasa()
