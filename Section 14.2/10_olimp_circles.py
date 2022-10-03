import turtle
turtle.speed(50)

colors = ['blue', 'black', 'red', 'yellow', 'green']

for i in range(3):
    turtle.pendown()
    turtle.color(colors[i])
    turtle.circle(15)
    turtle.penup()
    turtle.forward(20)

turtle.goto(10, -10)

for i in range(2):
    turtle.pendown()
    turtle.color(colors[i + 3])
    turtle.circle(15)
    turtle.penup()
    turtle.forward(20)