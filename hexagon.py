import turtle
wn = turtle.Screen()
mike = turtle.Turtle()

def hexagon(boy):
    for i in range(6):
        boy.forward(50)
        boy.left(60)

print(hexagon(mike))

wn.exitonclick()
