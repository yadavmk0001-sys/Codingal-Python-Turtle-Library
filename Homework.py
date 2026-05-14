import turtle

turtle.Screen().bgcolor("orange")
turtle.Screen().setup(400, 400)

polygon = turtle.Turtle()

num_sides = 4
length = 80
angle = 360/num_sides

for i in range(4):
    turtle.forward(length)
    turtle.right(angle)

turtle.done()