import turtle
def pale(color= '#556B2F'):
    turtle.penup()
    turtle.home()
    turtle.setposition(-115,200)
    turtle.color(color)
    turtle.pendown()
    turtle.begin_fill()
    turtle.left(180)
    turtle.forward(114)
    turtle.left(90)
    turtle.forward(364)
    turtle.left(71)


    turtle.speed(0)
    for x in range(39):
        turtle.forward(3)
        turtle.left(1)

    turtle.left(70)
    turtle.forward(364)
    turtle.end_fill()

def fess(color= '#556B2F'):
    turtle.penup()
    turtle.home()
    turtle.color(color)
    turtle.pendown()
    turtle.begin_fill()
    turtle.left(90)
    turtle.forward(80)
    turtle.left(90)
    turtle.forward(344)
    turtle.left(90)
    turtle.forward(93)
    turtle.left(90)
    turtle.forward(344)
    turtle.left(90)
    turtle.forward(13)
    turtle.end_fill()

def bend(color= '#556B2F'):
    turtle.penup()
    turtle.home()
    turtle.color(color)
    turtle.pendown()
    turtle.begin_fill()
    turtle.left(142)
    turtle.forward(326)
    turtle.left(38)
    turtle.forward(87)

    turtle.left(90)
    turtle.forward(85)
    turtle.left(52)
    turtle.forward(379)
    turtle.left(85)
    turtle.speed(0)
    for x in range(40):
        turtle.forward(3)
        turtle.left(1)
    turtle.end_fill()


def saltire(color= '#556B2F'):
    #first part
    turtle.penup()
    turtle.home()
    turtle.color(color)
    turtle.pendown()
    turtle.begin_fill()
    turtle.left(142)
    turtle.forward(326)
    turtle.left(38)
    turtle.forward(87)

    turtle.left(90)
    turtle.forward(85)
    turtle.left(52)
    turtle.forward(379)
    turtle.left(85)
    turtle.speed(0)
    for x in range(40):
        turtle.forward(3)
        turtle.left(1)
    turtle.end_fill()

    #second part
    turtle.penup()
    turtle.home()
    turtle.setposition(-344,0)
    turtle.color(color)
    turtle.pendown()
    turtle.begin_fill()
    turtle.left(38)
    turtle.forward(326)
    turtle.right(38)
    turtle.forward(87)

    turtle.right(90)
    turtle.forward(85)
    turtle.right(52)
    turtle.forward(379)
    turtle.right(85)
    turtle.speed(0)
    for x in range(40):
        turtle.forward(3)
        turtle.right(1)
    turtle.end_fill()


def chevron(color= '#556B2F'):
    turtle.penup()
    turtle.home()
    turtle.color(color)
    turtle.pendown()
    turtle.begin_fill()
    turtle.left(142)
    turtle.forward(220)
    turtle.left(76)
    turtle.forward(218)

    turtle.left(51)
    turtle.speed(0)
    for x in range(30):
        turtle.forward(3)
        turtle.left(1)

    turtle.left(100)
    turtle.forward(195)
    #drugi krak
    turtle.right(79)
    turtle.forward(196)

    turtle.left(100)
    turtle.speed(0)
    for x in range(30):
        turtle.forward(3)
        turtle.left(1)

    turtle.end_fill()

def pall(color= '#556B2F'):
    turtle.penup()
    turtle.home()
    turtle.setposition(0,135)
    turtle.color(color)
    turtle.pendown()
    turtle.begin_fill()
    turtle.left(90)
    turtle.forward(65)
    turtle.left(90)
    turtle.forward(65)
    turtle.left(45)
    turtle.forward(153)
    #drugi krak
    turtle.right(90)
    turtle.forward(153)
    turtle.left(45)
    turtle.forward(65)
    turtle.left(90)
    turtle.forward(65)
    turtle.left(45)
    turtle.forward(184)

    #treci krak
    turtle.right(45)
    turtle.forward(174)

    turtle.left(76)
    turtle.speed(0)
    for x in range(29):
        turtle.forward(3)
        turtle.left(1)

    turtle.left(75)
    turtle.forward(174)
    turtle.right(45)
    turtle.forward(185)
    turtle.end_fill()

def chief(color= '#556B2F'):
    turtle.speed(6)
    turtle.home()
    turtle.setposition(0,80)
    turtle.color(color)
    turtle.begin_fill()

    turtle.left(90)
    turtle.forward(120)
    turtle.left(90)
    turtle.forward(344)
    turtle.left(90)
    turtle.forward(120)
    turtle.left(90)
    turtle.forward(344)
    turtle.end_fill()


def bordure(color= '#556B2F'):
    turtle.penup()
    turtle.home()
    turtle.color(color)
    turtle.pensize(38)
    turtle.pendown()
    turtle.speed(6)
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


