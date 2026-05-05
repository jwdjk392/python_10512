import turtle as t
import random
t.setheading(90)

t.teleport(0, -200)

t.speed(0)

def tree(length):
    angle = random.randint(15, 30)
    branch = random.uniform(0.6, 0.9)

    if length > 12:
        t.forward(length)
        t.left(angle)
        tree(length * branch)
        t.right(angle * 2)
        tree(length * branch)
        t.left(angle)
        t.backward(length)

tree(100)

t.exitonclick()