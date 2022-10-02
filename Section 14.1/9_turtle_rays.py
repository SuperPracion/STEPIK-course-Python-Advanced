import turtle
turtle.showturtle()

def draw_rays(quantity, side):
    angle_of_rotation = 360 / quantity
    for _ in range(quantity):
        turtle.left(angle_of_rotation)
        turtle.forward(side / 2)
        turtle.backward(side)
        turtle.forward(side / 2)


draw_rays(6, 100)