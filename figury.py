import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import math
import serwPol


def diament(x, y, z, promien):
    for i in range (-promien, promien+1):
        for j in range (-promien, promien+1):
            for k in range (-promien, promien+1):
                if (math.fabs(i) + math.fabs(j) + math.fabs(k)) <= promien:
                    mc.setBlock(x+i, y+j, z+k, block.STONE.id)


def kula(x, y, z, promien):
    for i in range (-promien, promien+1):
        for j in range (-promien, promien+1):
            for k in range (-promien, promien+1):
                if (math.sqrt(i*i+j*j+k*k)) <= promien:
                    mc.setBlock(x+i, y+j, z+k, block.STONE.id)

def cygaro(x, y, z, promien, odksztalcenieY):
    for i in range (-promien, promien+1):
        for j in range (int(-promien*odksztalcenieY), int(promien*odksztalcenieY)+1):
            for k in range (-promien, promien+1):
                if (math.sqrt(i*i+(j*j/odksztalcenieY/odksztalcenieY)+k*k)) <= promien:
                    mc.setBlock(x+i, y+j, z+k, block.STONE.id)


def walec(x, y, z, wysokosc, promien):
    for i in range (-promien, promien+1):
        for j in range (0, wysokosc+1):
            for k in range (-promien, promien+1):
                if (math.sqrt(i*i+k*k)) <= promien:
                    mc.setBlock(x+i, y+j, z+k, block.STONE.id)


def stozek(x, y, z, wysokosc, promien):
    for i in range (-promien, promien+1):
        for j in range (0, wysokosc+1):
            for k in range (-promien, promien+1):
                if (math.sqrt(i*i+k*k)) <= int(float(promien)*(1-float(j)/float(wysokosc))):
                    mc.setBlock(x+i, y+j, z+k, block.STONE.id)


def ostroslup(x, y, z, wysokosc, promien):
    for i in range (-promien, promien+1):
        for j in range (0, wysokosc+1):
            for k in range (-promien, promien+1):
                if (math.fabs(i)+math.fabs(k)) <= int(float(promien)*(1-float(j)/float(wysokosc))):
                    mc.setBlock(x+i, y+j, z+k, block.STONE.id)

mc = serwPol.podlacz()

poz = mc.player.getPos()
kula(poz.x+20, poz.y+10, poz.z+20, 15)

#ostroslup(poz.x+50, poz.y+1, poz.z+50, 50, 20)

time.sleep(0.5)
mc.postToChat("gotowe")
