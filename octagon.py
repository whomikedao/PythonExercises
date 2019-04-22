import turtle
wn = turtle.Screen()
mike = turtle.Turtle()

def octagon(boy):
    for i in range(8):
        boy.forward(50)
        boy.left(45)

print(octagon(mike))

wn.exitonclick()
