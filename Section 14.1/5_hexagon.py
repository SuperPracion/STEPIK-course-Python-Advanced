import turtle
turtle.showturtle()

def hexagon(side):
    for _ in range(6):
        turtle.forward(side)
        turtle.left(45)

hexagon(100)