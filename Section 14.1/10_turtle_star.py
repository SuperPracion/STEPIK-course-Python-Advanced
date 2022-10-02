import turtle
turtle.showturtle()
turtle.speed(100)

def draw_star(side):
    for _ in range(6):
        turtle.left(72)
        turtle.forward(side)

draw_star(100)