from turtle import *
import math
t = Turtle()
t.forward(100)
for _ in range(4):
    for i in range(0,11):
        xFrom = 0
        yFrom = (10-i) * 20
        xTo = i * 20
        yTo = 0
        t.penup()
        t.goto(xFrom,yFrom)
        t.pendown()
        t.goto(xTo,yTo)
    t.right(180)
for _ in range(4):
    triangle(t, 40, 10)
exitonclick()