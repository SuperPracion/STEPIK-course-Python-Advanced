import turtle

turtle.showturtle()


def triangle(side):
    for i in range(1, 4):
        turtle.setheading(120 * i)
        turtle.forward(side)


triangle(100)
