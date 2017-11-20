import turtle

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


def color(red, green, blue):
    t.hideturtle()
    t.screen.colormode(255)

    if red | green | blue > 255:
        return ValueError("Colors cannot exceed 255")
    else:
        t.pencolor(red, green, blue)
    return


def repeater(iterations):
    return int(iterations)

length = 5
for i in range(repeater(100)):
    color(70, 175, 154)
    move(length)
    angle(240)
    length = length + 5
pause()
