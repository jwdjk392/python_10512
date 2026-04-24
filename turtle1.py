import turtle

turtle.bgcolor("#bbb")
turtle.color("#f0f")
turtle.pensize(1)
turtle.shape("turtle")

#polygon = int(turtle.numinput("제목", "질문:  몇각형을 그릴까요?"))

#for i in range(polygon):
#    turtle.forward(50)
#    turtle.left(360/polygon)

polygon = 3
while True:
    for i in range(polygon): 
        turtle.forward(50)
        turtle.left(360/polygon)
    polygon+=1

#turtle.done()
turtle.exitonclick()