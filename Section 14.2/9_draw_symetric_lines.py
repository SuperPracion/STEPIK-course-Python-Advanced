import turtle
turtle.speed(10)
turtle.pencolor('cyan')

for i in range(-200, 200, 40):
    turtle.goto(i, 200)
    turtle.dot()
    turtle.goto(0, 0)
