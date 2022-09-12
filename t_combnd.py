import turtle
# defining the function of square
def sq(side):
    for i in range(4):
        t.fd(side)
        t.left(90)
        side -=2
# define function of Hexagonal spiral
def hex(side):
    for i in range(6):
        t.fd(side)
        t.left(300)
        side -= 2  #FOX
# define triangle function
def tri(side):
    for i in range(3):
        t.fd(side)
        t.left(120)
        side -=10
# setting screen
wn = turtle.Screen()
wn.bgcolor("Pink")
wn.title("Graphic Spiral")
t = turtle.Turtle()
# draw the combined spiral
t.color("Black")
t.pensize(5.75)
side = 100
t.penup()
t.goto(-200, -200)
t.pendown()
for i in range(3):
    sq(side)
    side -= 10
t.penup()
t.goto(-200, 200)
t.pendown()
for i in range(3):
    hex(side)
    side += 12
t.penup()
t.goto(50, 50)
t.pendown()
for i in range(3):
    tri(side)
    side += 30
turtle.done()