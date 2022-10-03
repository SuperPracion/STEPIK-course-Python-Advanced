import turtle
turtle.shape('turtle')
turtle.showturtle()

def draw_circle_with_stamps(line_size, count_beams):
    angle = 360 / count_beams
    turtle.penup()
    for _ in range(count_beams):
        turtle.forward(line_size)
        turtle.stamp()
        turtle.backward(line_size)
        turtle.left(angle)

draw_circle_with_stamps(50, 8)