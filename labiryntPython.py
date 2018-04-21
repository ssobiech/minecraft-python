from turtle import *

p = Turtle()


def element(a):
    t = 6
    for i in range(6):
        for k in range(2):
            p.fd(a*t)
            p.rt(90)
        t = t-1

def kwiat(a):
    bierz = p.pos()
    for l in range(4):
        element(a)
        p.pu()
        p.goto(bierz)
        p.seth(0)
        p.lt(l*90+90)
        p.pd()

def labirynt(n):
    a = 450/(n*12+(n+1))
    p.pu()
    p.rt(90)
    p.fd(450/2)
    p.rt(90)
    p.fd(450/2)
    p.rt(180)
    p.pd()
    for i in range(4):
        p.fd(450)
        p.lt(90)
    p.pu()
    p.fd(a*7)
    p.lt(90)
    p.fd(a*7)
    p.pd()
    p.seth(0)
    for j in range(n):
        for t in range(n):
            kwiat(a)
            p.pu()
            p.fd(13*a)
            p.pd()
        p.pu()
        p.bk(13*a*n)
        p.lt(90)
        p.fd(a*13)
        p.rt(90)
        p.pd()


p.speed(0)
labirynt(8)
done()
