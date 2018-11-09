#coding=utf-8
import turtle
import math

m=500     #绘图范围
a=100.0   #放缩比例
width=2   #图像粗细

str_x=""
str_y=""

colors=["black","red","orange","yellow","green","blue","purple"]

def getx(t):
    try:
        x = eval(str_x)    #设置函数
    except:
        print "t=%.5f"%t,"error"
        return None
    else:
        print "t=%.5f"%t,"x=%.5f"%x,"OK"
        return x

def gety(t):
    try:
        y = eval(str_y)    #设置函数
    except:
        print "t=%.5f"%t,"error"
        return None
    else:
        print "t=%.5f"%t,"y=%.5f"%y,"OK"
        return y

def gotoStart(r):
    nr = r
    while True:
        print "initing",
        if (getx(-r/a)==None)|(gety(-r/a)==None):
            r=r-1
            if -r>nr:
                print "init error"
                return None
        else:
            turtle.goto(getx((-r)/a)*a,gety((-r)/a)*a)
            print "initOK"
            return r

def init():
    turtle.speed(0)
    turtle.goto(1000,0)
    turtle.goto(-1000,0)
    turtle.up()
    turtle.goto(0,800)
    turtle.down()
    turtle.goto(0,-800)
    turtle.up()
    for i in range(-10,10):
        turtle.goto(i*a,0)
        turtle.dot()
        turtle.write(i)
    for i in range(-10,10):
        turtle.goto(0,i*a)
        turtle.dot()
        turtle.write(i)

def draw(index):
    global m
    turtle.up()
    r=m
    r = gotoStart(r)
    if r == None:
        return
    turtle.color(colors[index%7],colors[index%7])
    turtle.width(width)
    #turtle.down()
    print "Start Drawing"
    for i in range(-r,m,1):
        print "Drawing",
        t=i/a
        y=gety(t)
        x=getx(t)
        if (y==None)|(x==None):
            turtle.up()
            continue
        turtle.goto(x*a,y*a)
        turtle.dot()
    turtle.up()
    turtle.done()
    print "complete"


init()
index=0
turtle.Turtle().screen.delay(0)
while True:
    str_x=raw_input("x=")
    str_y=raw_input("y=")
    draw(index)
    index=index+1