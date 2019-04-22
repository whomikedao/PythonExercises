import turtle
wn = turtle.Screen()
mike = turtle.Turtle()

def pentagon(boy):
    for i in range(5):
        boy.forward(50)
        boy.left(72)

print(pentagon(mike))

wn.exitonclick()
