import turtle
import random

t = turtle.Turtle()
win = turtle.Screen()


def pause():
    win.exitonclick()
    return


def move(distance):
    t.hideturtle()
    t.forward(distance)
    return


def angle(degree):
    t.hideturtle()
    if degree > 360:
        return ValueError("Degree cannot exceed 360")
    if degree < -360:
        return ValueError("Degree cannot exceed -360")
    if degree >= 0:
        t.right(degree)
    if degree <= 0:
        t.left(degree)
    else:
        return
    return


def color(boolean, *args):
    t.hideturtle()
    t.screen.colormode(255)

    if args:
        return t.color(args[0], args[1], args[2])
    if boolean is True:
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)

        t.color(red, green, blue)
        return

    if boolean is False:
        return t.color('black')


def repeater(iterations):
    return int(iterations)


def run(iterations, length):
    while repeater(iterations) > 0:
        color(False)
        move(length)
        angle(123)
        length = length + 5

run(100, 5)
