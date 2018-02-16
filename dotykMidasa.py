import time
import serwPol
import logger
from random import randint


mc = serwPol.podlacz()
logger = logger.Logger()

def losuj_blok():
    losuj = randint(1,255)
    bloki_nie = [2,6,8,9.10,11,12,13,26,30,31,37,38,50,51,64,65,71,77,79,78,81,83,85,95,102,107,143,
                 171,175,145,174,252,76,50,40,39,65,106,111,139,130,120,113,198,200,199,188,321,323,
                 397,416,425,426,331,356,404,427,428,429,430,431,69,72,76,27,28,66,157,183,184,185,186,187,330,324,96,70,72,162,295,361,362,435,372]
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
   			mc.setBlock(pos.x, pos.y - 1, pos.z, losuj_blok())
		time.sleep(0.5)

dotykMidasa()
