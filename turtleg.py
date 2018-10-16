import turtle

tris=turtle.Turtle()
tris.speed(0)
tris.color('red')
turtle.bgcolor('black')
rotate = int(360)
def drawturtle(t,size):
    for i in range(120):
        turtle.turtle(size)
        size=-4
def drawSpecial(t,size,repeat):
    for i in range(repeat):
        drawturtle(t,size)
        turtle.right(360/repeat)
drawSpecial(t,100,10)

exitonclick()
