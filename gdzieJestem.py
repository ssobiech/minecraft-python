import mcpi.minecraft as minecraft
import serwPol
import time


def gdzieJestem():
    mc = serwPol.podlacz()
    while True:
        time.sleep(1)
        pos = mc.player.getTilePos()
        mc.postToChat("x="+str(pos.x) + " y="+str(pos.y) + " z="+str(pos.z))


if __name__ == "__main__":
    gdzieJestem()
