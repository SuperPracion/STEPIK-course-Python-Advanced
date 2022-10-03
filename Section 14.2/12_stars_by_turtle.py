import turtle
import random
turtle.showturtle()
turtle.speed(50)

def draw_corner():
    turtle.left(45)
    turtle.forward(6)
    turtle.backward(6)
    turtle.right(90)
    turtle.forward(6)
    turtle.backward(6)
    turtle.left(45)

def draw_snowflake(x_pos, y_pos):
    turtle.pendown()
    for _ in range(8):
        turtle.left(45)
        for _ in range(4):
            draw_corner()
            turtle.forward(10)

        turtle.goto(x_pos, y_pos)


for _ in range(5):
    x_pos = random.randint(-200, 200)
    y_pos = random.randint(-200, 200)

    turtle.penup()
    turtle.goto(x_pos, y_pos)
    draw_snowflake(x_pos, y_pos)