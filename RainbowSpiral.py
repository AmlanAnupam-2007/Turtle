import random,turtle
turtle.Screen().bgcolor("yellow")
v=["red","green","blue"]
a=turtle.Turtle()

for i in range(100):
    a.pencolor(random.choice(v))
    a.forward((i*10))
    a.right(90)
turtle.done()