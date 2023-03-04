from turtle import Turtle, Screen
import random

kachua1 = Turtle()
kachua1.shape("turtle")
kachua1.penup()
kachua1.color("tomato1")
kachua1.sety(10)
kachua2 = Turtle()
kachua2.penup()
kachua2.shape("turtle")
kachua2.color("medium spring green")
kachua2.sety(30)
kachua3 = Turtle()
kachua3.penup()
kachua3.shape("turtle")
kachua3.color("turquoise1")
kachua3.sety(50)
kachua4 = Turtle()
kachua4.penup()
kachua4.shape("turtle")
kachua4.color("MediumOrchid1")
kachua4.sety(70)
kachua5 = Turtle()
kachua5.penup()
kachua5.shape("turtle")
kachua5.color("yellow2")
kachua5.sety(90)

kachua1.setx(-100)
kachua2.setx(-100)
kachua3.setx(-100)
kachua4.setx(-100)
kachua5.setx(-100)


def moveturt():
    cont = True
    while cont:
        steps = random.randint(15, 29)
        kachua1.forward(steps)
        steps = random.randint(15, 29)
        kachua2.forward(steps)
        steps = random.randint(15, 29)
        kachua3.forward(steps)
        steps = random.randint(15, 29)
        kachua4.forward(steps)
        steps = random.randint(15, 29)
        kachua5.forward(steps)
        if kachua1.xcor() > 700:
            cont = False
            break
        elif kachua2.xcor() > 700:
            cont = False
            break
        elif kachua3.xcor() > 700:
            cont = False
            break
        elif kachua4.xcor() > 700:
            cont = False
            break
        elif kachua5.xcor() > 700:
            cont = False
            break


screen = Screen()
screen.listen()
screen.onkey(key="space", fun=moveturt)
screen.exitonclick()
