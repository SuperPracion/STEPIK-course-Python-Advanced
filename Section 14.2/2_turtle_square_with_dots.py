import turtle
turtle.speed(1)
turtle.pensize(3)

def draw_square_with_dots(width, height):
    size = [width, height]
    for _ in range(2):
        for i in range(2):
            turtle.forward(size[i])
            turtle.dot()
            turtle.left(90)

draw_square_with_dots(100, 50)