import turtle
turtle.showturtle()

def rectangle(width, height):
    for i in range(2):
        turtle.forward((width if i % 2 == 0 else height))
        turtle.right(90)

rectangle(100, 50)