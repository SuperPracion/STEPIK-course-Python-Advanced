import turtle
turtle.showturtle()

def draw_honeycomb(side):
    for _ in range(6):
        for _ in range(6):
            turtle.forward(side)
            turtle.left(60)

        turtle.forward(side)
        turtle.right(60)

draw_honeycomb(30)