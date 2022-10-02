import turtle
turtle.showturtle()
turtle.speed(100)

def draw_circle_by_rombs(side):
    for _ in range(10):
        turtle.left(24)
        for j in range(1, 5):
            turtle.left((120 if j % 3 == 0 else 60))
            turtle.forward(side)

draw_circle_by_rombs(50)