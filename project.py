from myfunction import *

import turtle



bob=turtle.Turtle()

jason=turtle.Turtle()

tingye=turtle.Turtle()

ty=turtle.Turtle()

j=turtle.Turtle()

c=turtle.Turtle()

g=turtle.Turtle()

y=turtle.Turtle()

turtle.bgcolor("black")

turtle.colormode(255)
bob.color(255,0,0)
jason.color(0,255,255)
tingye.color(255,255,0)
ty.color(255,0,255)
j.color(0,0,255)
c.color(100,0,100)
g.color(0,100,100)
y.color(0,100,0)

bob.speed(0)
tingye.speed(0)
jason.speed(0)
ty.speed(0)
j.speed(0)
c.speed(0)
g.speed(0)
y.speed(0)

for times in range(55):
    
    dumbell2(bob,4)
    bob.left(36)
    
    dumbell2(jason,5)
    jason.forward(times * 10)
    jason.left(36)

    tingye.pu()
    tingye.goto(0,200)
    tingye.pd()
    star(tingye,36)
    

    ty.circle(times * 10)
    ty.left(12)

    g.circle(times * 10)
    g.right(12)


    

    j.pu()
    j.goto(260,0)
    j.left(36)
    j.pd()
    j.left(times * 10)
    dumbell2(j,10)

    c.pu()
    c.goto(-260,0)
    c.pd()
    c.left(times * 10)
    dumbell2(c,10)

    polygon(y,1,10)
    y.forward(times * 10)
    y.left(90)

    turtle.ht()




    





    

