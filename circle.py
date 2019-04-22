import turtle
wn = turtle.Screen()
mike = turtle.Turtle()

def circle(boy):
    for i in range(360):
        boy.forward(2)
        boy.left(1)

print(circle(mike))

wn.exitonclick()
