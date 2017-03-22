def tear(t):
    for times in range(10):
        t.circle(times * 2)
        t.left(10)
        t.forward(10)
        
def L(t,distance,angle):
    t.forward(distance)
    t.left(angle)
    t.forward(distance)
    

def polygon(t, sides, distance):
    angle = 360 / sides
    t.begin_fill()
    for times in range(sides):
        t.forward(distance)
        t.left(angle)
    t.end_fill()

def cool(t):
    t.color("black")
    polygon(t,4,10)
    t.color("orange")
    polygon(t,3,10)


def coolsquare(t):
    for times in range(4):
        cool(t)
        t.left(90)

def jump(t,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

def dumbell2(t,size):
    
    t.width(10)
    t.begin_fill()
    t.circle(size)
    t.forward(size)
    t.right(180)
    t.circle(size)
    t.end_fill()

def triangle(t,angle):
    polygon(t,3,50)
    t.left(36)
    t.forward(30)

def circle(t,size):
    t.width(5)
    t.circle(1000,size)
    t.left(90)

def star(t,angle):
    for times in range (5):
        t.left(36)
        polygon(t,4,10)
        t.left(36)

def project(t):
    



    for times in range(100):
    
        dumbell2(t,4)
        t.left(36)
    
        dumbell2(t,5)
        t.forward(times * 10)
        t.left(36)

        t.pu()
        t.goto(0,200)
        t.pd()
        star(t,36)
    

        t.circle(times * 10)
        t.left(12)

        t.circle(times * 10)
        t.right(12)

        t.pu()
        t.goto(260,0)
        t.left(36)
        t.pd()
        t.left(times * 10)
        dumbell2(t,10)

        t.pu()
        t.goto(-260,0)
        t.pd()
        t.left(times * 10)
        dumbell2(t,10)

        polygon(t,1,10)
        t.forward(times * 10)
        t.left(90)



    

        t.pu()
        t.goto(260,0)
        t.left(36)
        t.pd()
        t.left(times * 10)
        dumbell2(t,10)

        t.pu()
        t.goto(-260,0)
        t.pd()
        t.left(times * 10)
        dumbell2(t,10)

        polygon(t,1,10)
        t.forward(times * 10)
        t.left(90)


    

