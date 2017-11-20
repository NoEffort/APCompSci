import turtle
import random

t = turtle.Turtle()
win = turtle.Screen()


def pause():
    win.exitonclick()
    return


def end():
    win.bye()
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


def color(*args):
    t.hideturtle()
    t.screen.colormode(255)

    if args is int():
        return t.color(args[0], args[1], args[2])
    if args[0] is True:
        if int(args[1]) > 255 | int(args[1]) < 0:
            return ValueError("Value must be in range of 0, 255")
        else:
            red = random.randint(0, int(args[1]))
            green = random.randint(0, int(args[1]))
            blue = random.randint(0, int(args[1]))

            t.color(red, green, blue)
            return

    if args[0] is False:
        try:
            end()
        except ConnectionError:
            print("Window cannot be closed")
        return print("Please manually define your colors based upon the RGB scale. Usage: color(RED, GREEN, BLUE)")


def repeater(iterations):
    return int(iterations)


length = 5
for i in range(repeater(99)):
    color(32, 67, 98)
    move(length)
    angle(123)
    length = length + 5
pause()
