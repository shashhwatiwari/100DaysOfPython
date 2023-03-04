from turtle import Turtle, Screen
from data import COLORS
import random

kachua = Turtle()
kachua.shape("turtle")
disp = Screen()
kachua.penup()
kachua.setx(-500)
kachua.sety(-250)
k = 50
for i in range(40, 810, 40):
    setcolour = random.choice(COLORS)
    kachua.penup()
    kachua.forward(80)
    kachua.color(setcolour)
    kachua.pendown()
    kachua.begin_fill()
    kachua.circle(15)
    kachua.end_fill()
    if i % 160 == 0:
        kachua.penup()
        kachua.setx(-500)
        kachua.sety(-250 + k)
        k += 50
disp.exitonclick()
