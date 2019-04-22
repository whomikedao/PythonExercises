import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
mike = turtle.Turtle()
mike.color("blue")

import turtle
wn = turtle.Screen()
mike = turtle.Turtle()

def pentagon(size, fill):
    mike.fill(fill)
    for i in range(5):
        mike.forward(size)
        mike.left(72)
    mike.fill(False)
    
print(pentagon(30, True))



wn.exitonclick()
