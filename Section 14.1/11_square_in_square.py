import turtle
turtle.showturtle()
turtle.speed(100)

def draw_square_in_square(side):
    diff_squares = side / 30
    for _ in range(30):
        for _ in range(4):
            turtle.left(90)
            turtle.forward(side)

        side -= diff_squares

draw_square_in_square(100)