from minecraftstuff import *
import serwPol


mc = serwPol.podlacz()
pos = mc.player.getTilePos()

p = minecraftstuff.MinecraftTurtle(mc, pos)



def element(a):
    t = 6
    for i in range(6):
        for k in range(2):
            p.forward(a*t)
            p.right(90)
        t = t-1

def przejscie(p,x,y,z,i):
    p.penup()
    p.setposition(x,y,z)
    p.setverticalheading(0)
    p.setheading(0)
    p.left(i*90+90)
    p.pendown()


def kwiat(a):

    b = p.position
    x = b.x
    y = b.y
    z = b.z
    for l in range(4):
        element(a)
        przejscie(p,x,y,z,l)

def labirynt(n,w):
    a = w/(n*12+(n+1))
    for i in range(4):
        p.forward(w)
        p.left(90)
    p.penup()
    p.forward(a*7)
    p.left(90)
    p.forward(a*7)
    p.pendown()
    p.setheading(0)
    p.setverticalheading(0)
    for j in range(n):
        for t in range(n):
            kwiat(a)
            p.penup()
            p.forward(13*a)
            p.pendown()
        p.penup()
        p.backward(13*a*n)
        p.left(90)
        p.forward(a*13)
        p.right(90)
        p.pendown()


p.speed(0)
labirynt(8, 500)
