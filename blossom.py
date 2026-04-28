import turtle as t
import random
t.bgcolor("#ECEDF2")
#t.pensize(1)
t.speed(0)

color = ("#DA0F47", "#D31044", "#EC548F", "#B03563", "#EB568E", "#DE6180", "#F8F2F2", "#CBAEB9")

for x in range(20):
    #t.up()
    #t.goto(random.randint(-300, 300), random.randint(-300, 300))
    #t.down()
    t.teleport(random.randint(-300, 300), random.randint(-300, 300))
    t.color(random.choice(color))

    t.begin_fill()
    star_size = (random.randint(10, 60))
    t.pensize(star_size)

    for i in range(5):
        t.forward(star_size)
        t.left(144)
        t.forward(star_size)
        t.left(72)
    t.end_fill()

t.done()