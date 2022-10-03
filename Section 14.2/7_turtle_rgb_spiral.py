import turtle
import random

turtle.showturtle()
turtle.speed(50)

pen_size = 1
pen_colors = ['red', 'blue', 'green', 'brown', 'violet', 'yellow']

def draw_octagon(count_lines, line_len, pen_size):
    for _ in range(count_lines):
        turtle.pensize(pen_size)
        turtle.pencolor(random.choice(pen_colors))
        turtle.forward(line_len)
        turtle.left(45)
        pen_size += 1
        line_len += 5


draw_octagon(100, 10, 1)

