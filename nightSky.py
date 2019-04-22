import turtle
import random
wn = turtle.Screen()
wn.bgcolor("black")
mike = turtle.Turtle()
mike.color("white")

amountOfStars = random.randint(1, 15)

def star(size):
    for i in range(5):
        mike.forward(size)
        mike.left(144)

def fplacement(distance):
    mike.up()
    mike.forward(distance)
    mike.down()

def upPlacement(distance):
    mike.up()
    mike.left(90)
    mike.forward(distance)
    mike.down

def downPlacement(distance):
    mike.up()
    mike.right(90)
    mike.forward(distance)
    mike.down()

print(amountOfStars)
stars = amountOfStars
while stars > 0:
    starSize = random.randint(1, 40)
    placementOfStars = random.randint(1, 4)
    distanceOfStars = random.randint(25, 70)
    print(star(starSize))
    if placementOfStars == 1:
        print(upPlacement(distanceOfStars))
    elif placementOfStars == 2:
        print(fplacement(distanceOfStars))
    elif placementOfStars == 3:
        print(downPlacement(distanceOfStars))
    stars -= 1
    print(stars)


wn.exitonclick()
