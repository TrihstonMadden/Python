import turtle
t = turtle.Pen()
turtle.bgcolor("black")
t.color("red")
t.speed(0)
t.width(5)
t.hideturtle()
t.left(90)
for x in range(180):
    t.forward(1)
    t.right(1)
for x in range(180):
    t.back(1)
    t.right(1)
