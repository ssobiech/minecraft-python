import serwPol

import mcpi.block as block
import time
import random

bloki = random.randint(0, 2)
mc = serwPol.podlacz()

bridge = []

while True:
   pos = mc.player.getPos()
   pos.y = pos.y - 1
   belowBlock = mc.getBlock(pos)
   if belowBlock == block.AIR.id or belowBlock == block.WATER_FLOWING.id or belowBlock == block.WATER_STATIONARY.id:
     bridge.append(pos)
     bloki = random.randint(0, 1)
     if bloki == 0:
         mc.setBlock(pos, block.COMMAND_BLOCK)
     else:
         if bloki == 1:
             mc.setBlock(pos, block.STRUCTURE_BLOCK)
         elif bloki == 2:
            mc.setBlock(pos, block.BARRIER)
     if len(bridge) > 10:
         firstPos = bridge.pop(0)
         if not firstPos in bridge:
             mc.setBlock(firstPos, block.AIR)
   #time.sleep(0.05)
