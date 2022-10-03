import turtle
turtle.Screen().bgcolor('green')
turtle.shape('turtle')
turtle.showturtle()
turtle.penup()
len_line = 5

for _ in range(50):
    turtle.forward(len_line)
    turtle.right(90)
    turtle.stamp()
    turtle.left(90)
    turtle.backward(len_line)
    turtle.right(10)
    len_line += 2
