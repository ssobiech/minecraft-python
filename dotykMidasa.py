import time
import serwPol
import logger
from random import randint


mc = serwPol.podlacz()
logger = logger.Logger()

def losuj_blok():
    losuj = randint(1,255)
    bloki_nie = [2,6,8,9.10,11,12,13,26,30,31]
    while losuj in bloki_nie:
        losuj = randint(1,255)

    return losuj
    
    
        
def dotykMidasa():
	gold = 41
	water = 9
	air = 0
	logger.info("dotyk start - test")        
	while True:
		pos = mc.player.getTilePos()
		x = pos.x
		blockBelow = mc.getBlock(pos.x, pos.y - 1, pos.z)
		if blockBelow != air and blockBelow != water:
   			mc.setBlock(pos.x, pos.y - 1, pos.z, losuj_blok)
		time.sleep(0.0000001)

dotykMidasa()
