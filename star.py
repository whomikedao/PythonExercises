import turtle
wn = turtle.Screen()
mike = turtle.Turtle()

def star(boy):
    for i in range(5):
        boy.forward(50)
        boy.left(144)

print(star(mike))

wn.exitonclick()
