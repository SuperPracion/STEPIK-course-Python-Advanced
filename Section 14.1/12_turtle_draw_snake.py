import turtle
turtle.showturtle()
turtle.speed(100)

def draw_snake(side):
    for i in range(1, side):
        turtle.left(90)
        turtle.forward(i * 5)

draw_snake(54)