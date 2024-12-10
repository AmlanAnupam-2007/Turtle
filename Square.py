import turtle
turtle.Screen().bgcolor("yellow")
s = turtle.Screen()
s.setup(350,550)
s.title("My Turtle")
d = turtle.Turtle()

for i in range(4):
    d.forward(100)
    d.left(90)
turtle.done()