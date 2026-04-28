import turtle as t
import random

t.bgcolor("black")
t.speed(0)
colors = ["#FF00FF", "#00FFFF", "#FFFF00", "#00FF00","#0000FF", "#FF0000"]

for i in range(50):
    t.pensize(random.randint(1, 20)) # Define brush size
    t.pencolor(random.choice(colors))

    # Move to random location
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)

    #t.up()
    #t.goto(x,y)
    #t.down()
    t.teleport(x, y)

    size = random.randint(20, 100)
    sides = random.randint(3, 5)

    for _ in range(sides):
        t.forward(size)
        t.left(360 / sides)

t.exitonclick()