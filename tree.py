import turtle as t
import random


def tree(length, pen_size):
    angle = random.randint(20, 30)
    branch = random.uniform(0.6, 0.9)
    r_color = random.choice(color_list)

    if length < 35:
        t.color(r_color)
        t.stamp()
        t.color("#6e1b10")
    
    if length > 15:
        t.pensize(pen_size)
        pen_size *= 0.7
        t.forward(length * 1.1)
        t.left(angle)
        tree(length * branch, pen_size)
        t.right(angle * 2)
        tree(length * branch, pen_size)
        t.left(angle)
        t.backward(length * 1.1)


def grass():
    t.up()
    t.goto(-380, -280)
    t.shapesize(7)
    while t.xcor() < 380:
        t.setheading(0)
        t.forward(15)
        t.color(random.choice(color_list))
        t.setheading(random.randint(60, 120))
        t.stamp()

color_list = ["green", "darkgreen", "forestgreen", "yellowgreen"]

t.bgcolor("lightblue")

for i in range(2):
    t.setheading(90)
    t.speed(0)
    t.up()
    t.goto(0, -300)
    t.down()
    t.color("brown")

    tree(100, 10)

grass()

t.exitonclick()