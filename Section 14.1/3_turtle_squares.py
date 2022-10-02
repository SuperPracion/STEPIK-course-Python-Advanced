import turtle
turtle.showturtle()

def square(side):
    for i in range(3):
        turtle.right(24)
        for _ in range(4):
            turtle.left(90)
            turtle.forward(side)

square(100)
