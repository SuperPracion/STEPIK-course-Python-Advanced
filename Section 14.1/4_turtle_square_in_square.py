import turtle
turtle.showturtle()

def square(side):
    for _ in range(2):
        turtle.left(45)
        for _ in range(4):
            turtle.left(90)
            for _ in range(4):
                turtle.left(90)
                turtle.forward(side)


square(100)