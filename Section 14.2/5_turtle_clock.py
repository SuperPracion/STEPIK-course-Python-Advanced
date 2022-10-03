import turtle
turtle.Screen().bgcolor('cyan')
turtle.shape('turtle')

def draw_clock(line_size):
    angle = 30
    turtle.penup()
    for _ in range(12):
        turtle.forward(line_size - 30)
        turtle.pendown()
        turtle.forward(20)
        turtle.penup()
        turtle.forward(10)
        turtle.stamp()
        turtle.backward(line_size)
        turtle.left(angle)

draw_clock(100)