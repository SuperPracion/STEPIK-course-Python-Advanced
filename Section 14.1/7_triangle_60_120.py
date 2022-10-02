import turtle
turtle.showturtle()

def draw_triangle(side):
    for i in range(4):
        turtle.forward(side)
        turtle.left((60 if i % 2 == 0 else 120))

draw_triangle(50)