import turtle
wn = turtle.Screen()
mike = turtle.Turtle()

def pentagon(boy):
    for i in range(5):
        boy.forward(50)
        boy.left(72)

def star(boy):
    for i in range(5):
        boy.forward(50)
        boy.left(144)

def square(boy):
    for i in range(4):
        boy.forward(50)
        boy.left(90)

def octagon(boy):
    for i in range(8):
        boy.forward(50)
        boy.left(45)

def hexagon(boy):
    for i in range(6):
        boy.forward(50)
        boy.left(60)

def triangle(boy):
    for i in range(3):
        boy.forward(50)
        boy.left(120)   

def circle(boy):
    for i in range(360):
        boy.forward(2)
        boy.left(1)  

def move(boy):
    mike.up()
    mike.forward(100)
    mike.down()


print(pentagon(mike))
print(move(mike))
print(circle(mike))
print(move(mike))
print(star(mike))
print(move(mike))
print(octagon(mike))
print(move(mike))
print(hexagon(mike))
print(move(mike))
print(square(mike))
print(move(mike))
print(triangle(mike))



wn.exitonclick()
