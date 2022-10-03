import turtle
import random

turtle.speed(30)
colors = ['red', 'green', 'yellow', 'blue', 'gray', 'cyan', 'brown']
start_side = 5

def draw_square(side):
    for _ in range(4):
        turtle.forward(side)
        turtle.left(90)

for _ in range(60):
    turtle.circle(start_side)
    turtle.right(5)

    turtle.color(random.choice(colors))
    start_side += 4