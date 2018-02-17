import serwPol
import mcpi.block as block

mc = serwPol.podlacz()

pos = mc.player.getTilePos()
# Ask the user how big a space to clear
size = int(input("podaj obszar do wyczyszczenia? "))
# Clear a space size by size*size*size, by setting it to AIR
mc.setBlocks(pos.x, pos.y, pos.z, pos.x+size, pos.y+size, pos.z+size, block.AIR.id)

