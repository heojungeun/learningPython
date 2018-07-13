import turtle

wn = turtle.Screen()
t1 = turtle.Turtle()

t1.penup()
t1.right(90)
t1.forward(200)
t1.left(90)
t1.pendown()

t1.circle(200)
t1.circle(200, 360, 4)

turtle.done()