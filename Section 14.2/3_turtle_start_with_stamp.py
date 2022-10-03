import turtle
turtle.pensize(3)

def draw_star_with_stamps(line_size, count_beams):
    angle = 360 / count_beams
    for _ in range(count_beams):
        turtle.left(angle)
        turtle.forward(line_size)
        turtle.stamp()
        turtle.backward(line_size)

draw_star_with_stamps(100, 8)