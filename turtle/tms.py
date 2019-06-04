import turtle, colorsys

def bryan():
	turtle.bgcolor("black")
	t = turtle.Turtle()
	w = turtle.Screen()
	t.speed(0)

	def why(idx):
		for i in range(idx):
			color = colorsys.hsv_to_rgb(i / float(idx), 1.0, 1.0)
			t.color(color)
			t.forward(10 + (i / 16))
			t.right(10)

	why(500)
	w.exitonclick()
