import turtle

#turtle speed
# ‘fastest’ :  0
# ‘fast’    :  10
# ‘normal’  :  6
# ‘slow’    :  3
# ‘slowest’ :  1

def field(color = '#556B2F'):
    turtle.color(color)
    turtle.begin_fill()
    turtle.speed(6)
    turtle.Screen().setup(width=.75, height=.75)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(344)
    turtle.left(90)
    turtle.forward(200)
    # turtle.right(90)
    turtle.speed(0)
    for x in range(181):
        turtle.forward(3)
        turtle.left(1)

    turtle.end_fill()


def per_pale(color = '#556B2F'):
    turtle.speed(6)
    turtle.home()
    turtle.color(color)
    turtle.begin_fill()

    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(172)
    turtle.left(90)
    turtle.forward(373)
    turtle.left(90)
    turtle.circle(176,82)
    turtle.end_fill()

def per_fess(color = '#556B2F'):
    turtle.speed(6)
    turtle.home()
    turtle.color(color)
    turtle.begin_fill()

    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(344)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(344)
    turtle.end_fill()

def per_bend(color = '#556B2F'):
    turtle.speed(6)
    turtle.home()
    turtle.color(color)
    turtle.begin_fill()

    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(344)
    turtle.right(-135)
    turtle.forward(435)
    turtle.left(98)

    # turtle.circle(105,62)
    for x in range(43):
        turtle.forward(3)
        turtle.left(1)
    turtle.end_fill()


def per_saltire(color = '#556B2F'):
    turtle.speed(6)

    # turtle.home()
    turtle.setposition(0.0,200.0)
    turtle.color(color)
    turtle.begin_fill()

    
    turtle.left(89)
    turtle.forward(344)
    turtle.right(-135)
    turtle.forward(434)
    turtle.right(83)

    # turtle.circle(105,62)
    for x in range(105):
        turtle.forward(3)
        turtle.right(1)
    turtle.end_fill()


def per_chervon(color = '#556B2F'):
    turtle.home()
    turtle.color(color)
    turtle.begin_fill()
    turtle.speed(6)
    turtle.Screen().setup(width=.75, height=.75)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(344)
    turtle.left(90)
    turtle.forward(200)
    # turtle.right(90)
    turtle.speed(0)
    for x in range(40):
        turtle.forward(3)
        turtle.left(1)
    turtle.left(90)
    turtle.speed(6)
    turtle.forward(180)
    turtle.right(83)
    turtle.forward(173)
    turtle.left(90)
    turtle.speed(0)
    turtle.circle(150,50)

    # for x in range(60):
    #     turtle.forward(2)
    #     turtle.left(1)
    turtle.end_fill()


def per_pall(color1= '#556B2F', color2= '#8FBC8F'):

    # turtle.setposition(0.0,200.0)
    turtle.home()
    turtle.color(color1)
    turtle.begin_fill()

    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(172)
    turtle.left(90)
    turtle.forward(170)
    turtle.left(45)
    turtle.forward(193)
    turtle.left(98)

    for x in range(43):
        turtle.forward(3)
        turtle.left(1)
    turtle.end_fill()

    turtle.penup()

    #second part 
    turtle.setposition(-344.0,0.0)
    turtle.color(color2)
    turtle.begin_fill()

    # turtle.right(1)
    turtle.pendown()
    turtle.right(6)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(172)
    turtle.right(90)
    turtle.forward(170)
    turtle.right(45)
    turtle.forward(193)
    turtle.right(98)

    for x in range(43):
        turtle.forward(3)
        turtle.right(1)
    turtle.end_fill()

    # turtle.color(field_color)
    turtle.penup()

def per_pall_second_part(color2):
    #second part 
    turtle.setposition(-344.0,0.0)
    turtle.color(color2)
    turtle.begin_fill()

    turtle.right(1)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(172)
    turtle.right(90)
    turtle.forward(170)
    turtle.right(45)
    turtle.forward(193)
    turtle.right(98)

    for x in range(43):
        turtle.forward(3)
        turtle.right(1)
    turtle.end_fill()

    




