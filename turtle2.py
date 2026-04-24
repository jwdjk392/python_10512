import turtle as t
import random

t.bgcolor("black")

color = ("red", "blue", "green", "yellow", "cyan", "magenta", "pink", "white", "indigo", "lime")

t.speed(0)

for x in range(1000):
    t.pensize(random.randint(0, 10))
    t.bgcolor(random.choice(color))
    t.up()
    t.goto(random.randint(-300, 300), random.randint(-300, 300))
    t.down()
    t.color(random.choice(color))

    t.begin_fill()

    starSize = random.randint(10, 50)
    for i in range(5):
        t.forward(starSize)
        t.left(144)
        t.forward(starSize)
        t.right(72)
        
    t.end_fill()


t.exitonclick()