import serwPol
import logger

mc = serwPol.podlacz()
logger = logger.Logger()
pos = mc.player.getTilePos()
def zczytaj():
    logger.info("zczytaj")
    for i in range(16):
        block = mc.getBlock(pos.x, pos.y+i, pos.z)
        
        if block == 56:
            mc.postToChat("diament y+"+str(i))
    for l in range(16):
        block2 = mc.getBlock(pos.x+l, pos.y, pos.z)
        if block2 == 56:
            #mc.postToChat("diament %d %d %d" % (w, pos.y, pos.z))
            mc.postToChat("diament x+" + str(l))
    for k in range(16):
        block3 = mc.getBlock(pos.x, pos.y, pos.z+k)
        if block3 == 56:
            mc.postToChat("diament z+"+str(k))
    for j in range(16):
        block = mc.getBlock(pos.x, pos.y-j, pos.z)
        
        if block == 56:
            mc.postToChat("diament y-"+str(j))
    for t in range(16):
        block2 = mc.getBlock(pos.x-t, pos.y, pos.z)
        if block2 == 56:
            #mc.postToChat("diament %d %d %d" % (w, pos.y, pos.z))
            mc.postToChat("diament x-"+str(t))
    for s in range(16):
        block3 = mc.getBlock(pos.x, pos.y, pos.z-s)
        if block3 == 56:
            mc.postToChat("diament z-"+str(s))

zczytaj()
