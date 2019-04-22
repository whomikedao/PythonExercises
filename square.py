import turtle
wn = turtle.Screen()
mike = turtle.Turtle()

def triangle(boy):
    for i in range(4):
        boy.forward(50)
        boy.left(90)

print(triangle(mike))

wn.exitonclick()
