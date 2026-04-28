import turtle as t

t.bgcolor("white")
t.speed(0)

for i in range(50):
    # t.pensize(i)
    t.pensize(i/3)
    t.pencolor("black")
    # t.circle(i*5)
    t.circle(i*10)
    t.up()
    # t.sety(-i*5)
    t.sety(-i*5 - 40)
    t.down()

t.exitonclick()
