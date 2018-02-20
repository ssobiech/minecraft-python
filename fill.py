import serwPol
import logger
from mineturtle import *
from mcpi.vec3 import Vec3
from mcpi.block import *
import time

mc = serwPol.podlacz()
log = logger.Logger()

pozycje = []
p = Turtle(mc)


def fd(lenght):
    pozycje.append(mc.player.getTilePos())
    p.go(lenght)
    pozycje.append(mc.player.getTilePos())


def rysuj():
    pos = mc.player.getTilePos()
    for i in range(3):
        fd(15)
        p.left(120)

    min = minimalny(pos)
    max = maxymalny(pos)
    log.info("minimalny: " + str(min) + ", maksymalny: " + str(max))
    time.sleep(3.5)
    mc.setBlocks(min, max, GOLD_BLOCK.id)


def minimalny(pos):
    minimalnyx = pos.x
    minimalnyy = pos.y
    minimalnyz = pos.z
    for pos in pozycje:
        if pos.x < minimalnyx:
            minimalnyx = pos.x
        if pos.y < minimalnyy:
            minimalnyy = pos.y
        if pos.z < minimalnyz:
            minimalnyz = pos.z
    return Vec3(minimalnyx, minimalnyy, minimalnyz)


def maxymalny(pos):
    maxymalnyx = pos.x
    maxymalnyy = pos.y
    maxymalnyz = pos.z
    for pos in pozycje:
        if pos.x > maxymalnyx:
            maxymalnyx = pos.x
        if pos.y > maxymalnyy:
            maxymalnyy = pos.y
        if pos.z > maxymalnyz:
            maxymalnyz = pos.z
    return Vec3(maxymalnyx, maxymalnyy, maxymalnyz)

p.angle(0)
rysuj()
