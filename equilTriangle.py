import turtle
wn = turtle.Screen()
mike = turtle.Turtle()

def triangle(boy):
    for i in range(3):
        boy.forward(50)
        boy.left(120)

print(triangle(mike))

wn.exitonclick()
