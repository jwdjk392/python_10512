import turtle as t
import random
t.bgcolor("black")
t.speed(0)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(1000):
    t.pencolor(colors[i%6])
    t.pensize(i/10 + 1)
    t.forward(i*2)
    t.left(59)
    #t.left(random.randint(0, 360))

t.exitonclick()