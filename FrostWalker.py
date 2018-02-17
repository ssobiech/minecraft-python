import serwPol

import mcpi.block as block
import time
import random

bloki = random.randint(0, 2)
mc = serwPol.podlacz()

bridge = []
typy = []
typy.append(block.FROSTED_ICE)

while True:
   pos = mc.player.getPos()
   pos.y = pos.y - 1
   belowBlock = mc.getBlock(pos)
   if belowBlock == block.WATER_FLOWING.id or belowBlock == block.WATER_STATIONARY.id:
     bridge.append(pos)
     bloki = random.randint(0, len(typy)-1)
     mc.setBlock(pos, typy[bloki])
     print("wylosowano: " + str(bloki) + ", blok:" +str(typy[bloki]))
   #time.sleep(0.05)
